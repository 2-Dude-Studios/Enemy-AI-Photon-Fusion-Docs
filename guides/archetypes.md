# Archetypes

Five starting points in the Enemy Configurator. Each is a set of sensible
values, not a locked-down type — pick the closest one and tune from there.

Everything here works identically on both runtimes. Pick **Standalone** or
**Fusion** in the Configurator's Runtime dropdown; the behaviour is the same.

> **Pick the archetype first, then tune.** Re-selecting an archetype re-applies
> its preset and overwrites your edits.

---

## At a glance

| Archetype | In one line | Needs scene setup? |
|---|---|---|
| **Custom** | Balanced melee baseline — the one to start from | No |
| **Stealth** | Slow to notice you, quick to lose you | No |
| **Shooter** | Keeps its distance, shoots, falls back to cover | **Yes** — cover geometry |
| **Waves** | Horde fodder that calls for help and never retreats | **Yes** — a spawner |
| **Boss** | High-health bruiser that never flees | **Yes** — a phase controller |

---

## Custom — the melee baseline

> 🎬 **See it in action:** [Melee enemy](/videos/?id=standalone-melee) · [Melee over Fusion](/videos/?id=fusion-melee)


Vision, random patrol, aggressive chase, melee attack with a jump-lunge, and
retreat when badly hurt. Every other archetype is this plus changes.

| | |
|---|---|
| Health | 100, flees below 15, recovers to 80 |
| Sight | 20 m, 90° cone |
| Chase | gives up past 25 m, moves at 3 |
| Attack | strikes at 2 m, lunges from 4 m |

**Good for:** most melee enemies. Start here unless you specifically need one
of the others.

---

## Stealth — gradual awareness

The same enemy with its senses re-tuned so it's beatable by sneaking: a
narrower cone, shorter sight, slow to build suspicion and fast to lose it.

| Changed from baseline | |
|---|---|
| Cone | 60° (from 90°) |
| Sight | 14 m (from 20 m) |
| Notices you | slowly — `detectionRiseRate` 0.6 |
| Forgets you | quickly — `detectionDecayRate` 0.8 |
| Shout radius | 10 m |

**Good for:** stealth sections, patrolling guards, anything where the player
should be able to slip past.

**Tuning:** `detectionRiseRate` and `detectionDecayRate` are the two dials that
matter. Raise rise-rate for tenser guards; raise decay for more forgiving ones.
For real hiding, enable line-of-sight occlusion — see [Required project setup](/getting-started/required-setup.md), since
it's off by default.

---

## Shooter — ranged, kiting, cover-seeking

> 🎬 **See it in action:** [Shooter enemy](/videos/?id=standalone-shooter) · [Shooter over Fusion](/videos/?id=fusion-shooter)


Holds around 12 m, fires on a cooldown, and retreats to cover when you close
in. This is the only archetype that damages the target out of the box.

| | |
|---|---|
| Fires from | up to 12 m |
| Backs off inside | 6 m |
| Cooldown | 1.5 s, 8 damage per shot |
| Chase range | 30 m, sight 25 m, 100° cone |
| Jump-lunge | off — gunners don't lunge |

### It needs cover to work

Cover-seeking looks for geometry on the layer named by `coverMask`, and shots
are blocked by that same geometry. **With nothing on that layer, the shooter
has nowhere to hide and its shots pass through everything.**

- Put walls on your `Obstacle` layer and confirm `coverMask` points at it —
  re-pick it by name if your layer indices differ (see [Required project setup](/getting-started/required-setup.md)).
- `Tools ▸ EnemyAI ▸ Add Cover To Open Scene` drops a usable set of walls into
  any scene. **Re-bake the NavMesh afterwards**, or enemies will path through
  them.
- The demo-scene builder does both for you when you choose **Shooter**.

**Tuning:** `fireRange` and `minKeepDistance` define the band it tries to hold.
Keep `minKeepDistance` below `fireRange` — otherwise there's no distance at
which it will shoot, and Validate will tell you so.

---

## Waves — horde fodder

> 🎬 **See it in action:** [Waves over Fusion](/videos/?id=fusion-waves)


Built to be spawned in numbers: wide awareness, fast to spot you, quick to
re-engage, calls for help, and never retreats.

| Changed from baseline | |
|---|---|
| Cone | 120° |
| Notices you | fast — `detectionRiseRate` 2.5 |
| Retreat | off |
| Calls for help | on |

### It needs a spawner

The enemies come from a **wave spawner**, not from being placed in the scene.

1. Add a spawner — `StandaloneWaveSpawner` or `NetworkedWaveSpawner` to match
   your runtime.
2. Give it **spawn points** (child transforms work).
3. Assign a **`WaveDefinitionSO`**, then fill each wave's entries with your
   enemy prefab and a count. Waves can mix enemy types.

A wave clears when its enemies die, and the next begins after
`timeBetweenWaves`. Turn off `autoProgress` to drive it yourself with
`NextWave()`.

In play mode the spawner's inspector has **Begin** and **Next Wave** buttons.

**Networked note:** every prefab in a wave needs a `NetworkObject`, or the
networked spawner skips it. Scene Doctor flags this.

---

## Boss — the set-piece

High health, never flees, and — with a phase controller — changes behaviour as
it's worn down.

| Changed from baseline | |
|---|---|
| Health | 600 |
| Retreat | never (all flee triggers off) |
| Speed | 3 chasing and attacking |

### Phases

Phases swap the boss's abilities at health thresholds, using the same runtime
ability-swap the rest of the framework uses.

1. Add a **`BossPhaseController`** to the enemy — the same GameObject as the
   enemy component. *(The demo-scene builder adds it for you.)*
2. Assign a **`BossPhaseSO`** listing the phases.

Thresholds are health *fractions* and must **strictly descend**. A typical
three-phase fight:

| Phase | At | Behaviour |
|---|---|---|
| Opener | 1.0 | melee |
| Enraged | 0.6 | melee, shouts on entry |
| Desperation | 0.3 | melee |

`alertOnEnter` makes the boss shout as the phase begins, pulling nearby allies
in — an easy way to make an enrage read clearly.

Phase changes are **one-way**: healing back above a threshold doesn't revert
it. Scene Doctor warns if your thresholds don't descend.

**Tuning:** a phase can switch to `Projectile` attack, which reuses the same
combat settings as the Shooter (`fireRange`, `minKeepDistance`). It works, but
those fields aren't separately tuned for boss fights — expect to adjust them.

---

## Which do I pick?

- **Melee enemy** → Custom
- **Should be sneakable past** → Stealth
- **Shoots from range** → Shooter *(plus cover)*
- **Spawns in numbers** → Waves *(plus a spawner)*
- **A single big fight** → Boss *(plus phases)*

They're all the same underlying enemy. Nothing stops you giving a Boss the
Shooter's ranged settings, or a Waves enemy a stealth-tuned cone.
