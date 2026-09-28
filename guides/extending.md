# Extending the AI

For when the ScriptableObjects run out of road and you want your own
behaviour in code.

The short version: **you can write your own abilities and drop them in at
runtime without modifying this package.** Adding a whole new *state* is a
bigger job, and this page is honest about where that line sits.

---

## How it fits together

```
ScriptableObjects        what the enemy is — ranges, speeds, thresholds
        │
EnemyBlackboard          per-enemy state + the only channel for state changes
        │
Ability layer            the behaviour: senses, patrol, chase, attack, flee
        │
State machine            standalone (plain C#) or Fusion (networked)
```

Two things make this extensible:

- **Abilities are plain C# objects** behind a three-method interface. They
  don't know which runtime they're in.
- **`IEnemyContext`** is how an ability talks to the enemy — movement, health,
  the blackboard — without naming a concrete `Enemy` or `NetworkedEnemy`.
  Write against it and your code works on both runtimes unchanged.

---

## Writing an ability

```csharp
public interface IAbility
{
    // Simulation — fixed step, only on the peer that simulates the enemy
    void Enter();         // once when the state becomes active
    void Tick();          // every fixed step while active
    void Exit();          // once when leaving

    // Render — once per frame, on every peer, after the state's base animation
    void EnterRender();   // e.g. override the state's animation
    void Render();        // per-frame presentation
    void ExitRender();
}
```

Put logic in the simulation hooks and visuals (animation overrides,
effects) in the render hooks. Both runtimes call both sets, so an ability
never needs to know which runtime it is running in. Leave a render hook
empty when there's nothing to show. A minimal example:

```csharp
using EnemyAI.Core;
using UnityEngine;

public class CircleStrafe : IAbility
{
    readonly IEnemyContext enemy;
    readonly EnemyBlackboard blackboard;
    float angle;

    public CircleStrafe(IEnemyContext enemy)
    {
        this.enemy = enemy;
        this.blackboard = enemy.Blackboard;
    }

    public void Enter() => enemy.SetSpeed(3f);   // whole numbers — see below

    public void Tick()
    {
        var target = blackboard.CurrentTarget;
        if (target == null) return;

        angle += enemy.DeltaTime;
        Vector3 offset = new Vector3(Mathf.Cos(angle), 0f, Mathf.Sin(angle)) * 5f;
        enemy.SetDestination(target.Transform.position + offset);
    }

    public void Exit() { }

    public void EnterRender() { }
    public void Render() { }
    public void ExitRender() { }
}
```

`IEnemyContext` gives you what you need:

| Member | For |
|---|---|
| `SetDestination`, `SetSpeed`, `SetStoppingDistance` | movement |
| `Transform`, `GameObject` | the usual |
| `DeltaTime` | the correct step for this runtime |
| `SimulationTime` | the clock `DeltaTime` steps — use it for any timestamp you store, never `Time.time` |
| `Blackboard` | current target, distance, current state |
| `Registry` | the ability systems, for swapping |
| `HasSimulationAuthority` | true standalone; host-only under Fusion |

---

## Dropping it in

Swap it onto a live enemy through the registry:

```csharp
var enemy = gameObject.GetComponent<IEnemyContext>();
enemy.Registry.SwapRush(new CircleStrafe(enemy));
```

`SwapRush`, `SwapAttack` and `SwapInjured` each take **either** a built-in
enum value **or** your own `IAbility`. The swap is lifecycle-safe: the
outgoing ability gets `Exit()`, the incoming one `Enter()`.

This is the intended extension route — no package files edited, and it
survives upgrading the package.

**Under Fusion, swap on the host only.** Clients don't simulate AI, so a swap
there changes nothing and desyncs your own expectations. Guard with
`HasSimulationAuthority` if the calling code runs on both.

### Making it selectable in the inspector

If you'd rather pick your ability from the dropdown on a `CombatAbilitySO`
instead of swapping in code, that **does** require editing the package: add a
value to the relevant enum (`RushAbilities`, `AttackAbilities`,
`InjuredAbilities`) and a case to that system's factory.

It's a two-line change, but it's a *fork* — you'll have to redo it when the
package updates. Prefer the runtime swap unless you need designers picking it
from a menu.

---

## Changing states, and the one rule

Abilities never call the state machine directly. They raise an event on the
blackboard:

```csharp
blackboard.InvokeOnSwitchStates(enemy, EnemyNetworkStates.patrol);
return;   // <- always
```

> **The rule: a state switch must be the last thing your tick does.**
>
> The event is **synchronous**. By the time `InvokeOnSwitchStates` returns, the
> new state's `Enter()` has already run and set up its movement. Any code after
> it — setting speed, a destination, root motion — overwrites what the new
> state just configured, and you get an enemy that animates on the spot or
> refuses to move.
>
> This has bitten this codebase more than once. Always `return` immediately.

---

## Adding a new state

The state set is a fixed enum:

```
none · patrol · investigate · rush · lostTrack · attack · injured · dead
```

Adding to it is deliberate work, not configuration:

1. Add the value to `EnemyNetworkStates`.
2. Add a state class to **both** state machines, or accept that the runtimes
   diverge.
3. Under Fusion the state replicates, so the assembly needs re-weaving —
   see [Photon Fusion 2 setup](/networking/fusion-setup.md).

**Before you do:** most "new state" ideas are really new *abilities*. A
different way of chasing, attacking or fleeing is an `IAbility` swap and costs
you nothing. Reach for a new state only when you need genuinely new transition
topology.

There's no visual state-graph editor. Transitions live in the ability code
that raises them.

---

## Things worth knowing

**Speeds must be whole numbers.** `SetSpeed` feeds the animator's `speed`
parameter, which is an **int**. `2.5` moves the agent at 2.5 while playing the
animation for 2 — it reads as foot-sliding. Use 1, 2, 3, 4.

**The AI only runs where it has authority.** Standalone: always. Fusion: the
host. `HasSimulationAuthority` tells you which, and animator
`StateMachineBehaviour`s in this package already gate on it — worth copying if
you write your own.

**One distance per tick.** `blackboard.DistanceToTarget()` is computed once per
tick and reused; prefer it to recomputing.

**Line-of-sight checks should be level.** Cast rays horizontally at a
consistent height. Aiming at a target's transform position when pivots sit at
different heights sends the ray over cover — a bug this package has already
had once.

---

## A note on assemblies

Your code needs an assembly definition referencing **`EnemyAI.Core`**. That's
enough for anything using `IAbility` and `IEnemyContext`.

Reference `EnemyAI.Fusion` only for genuinely networked code, and be aware
that doing so means your assembly won't compile in a project without Photon
Fusion installed. If you need both, mirror this package's approach: keep the
Fusion-specific parts in a separate assembly with a define constraint.
