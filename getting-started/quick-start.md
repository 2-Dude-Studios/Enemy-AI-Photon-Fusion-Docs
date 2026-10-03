# Quick start

> 🎬 **See it in action:** [Installing the package](/getting-started/installation-standalone.md) · [Editor tools walkthrough](/videos/?id=editor-tools) · [Melee enemy](/videos/?id=standalone-melee)


Goal: an enemy that patrols, spots you, chases you down and attacks — running
in about five minutes.

This walks the single-player path, because it needs no other downloads. The
networked runtime uses the *same* enemies and the same configuration; once
this works, see [Photon Fusion 2 setup](/networking/fusion-setup.md).

**Do [Required project setup](/getting-started/required-setup.md) first** if you haven't. It's two minutes, and without
it the enemy will patrol politely and ignore you forever.

---

## 1. Build an enemy

Open **`Tools ▸ EnemyAI ▸ Enemy Configurator`**.

1. **Runtime** — leave it on `Standalone`.
2. **Archetype** — pick `Custom`. That's the balanced melee baseline: vision,
   patrol, chase, melee attack, retreat when badly hurt.
   *Pick the archetype before you tune anything — changing it re-applies the
   preset and overwrites your edits.*
3. **Name** it something like `MyEnemy`, and choose an output **Folder**
   inside `Assets/`.
4. Leave **Generate prefab** ticked.
5. Hit **Validate**, then **Apply**.

You now have seven ScriptableObjects describing the enemy and a prefab wired
to them, all in their own folder — `<Folder>/MyEnemy/` — with the prefab
selected in the Project window.

To change the enemy later, select its definition asset and click **Open in
Enemy Configurator**; Apply then updates it in place. Applying a *new* enemy
with a name that already exists asks whether to update that one or make a
copy.

> **When you start tuning speeds, keep them whole numbers.** The animator's
> speed parameter is an integer, so `2.5` moves the enemy at 2.5 while playing
> the slower animation — it reads as foot-sliding. Validate warns you if you
> drift off a whole number.

---

## 2. Build a scene around it

With your new prefab **selected in the Project window**, run:

**`Tools ▸ EnemyAI ▸ Create Demo Scene ▸ Standalone — Melee`**

Choose where to save when prompted. You get a scene containing:

- a floor with a **baked NavMesh**
- a **TargetProvider** — what tells enemies which targets exist
- a **TargetCapsule** tagged `Player` — the thing your enemy hunts
- **your enemy**, placed on the NavMesh

---

## 3. Press Play

The enemy patrols. Move the target capsule into its view — select it in the
Hierarchy and drag it in the Scene view while playing, or add a movement
script — and watch:

**patrol → awareness builds → investigate → chase → attack**

Detection is gradual, not a switch. The enemy grows suspicious, moves to
investigate, and only commits to a chase once it's sure. Break line of sight
early and its interest decays.

Select the enemy while playing to see its ranges drawn in the Scene view —
sight range, field of view, chase and attack distances.

---

## 4. Check your work

Run **`Tools ▸ EnemyAI ▸ Scene Doctor`** any time something seems off. It
checks for the mistakes that fail *silently* — no NavMesh, no target
provider, animator on the wrong object, missing cover — and each finding has
a **Select** button that jumps you to the culprit.

---

## Putting an enemy in your own scene

The demo scene is scaffolding. For your real project you need four things:

1. **A baked NavMesh.** Enemies error on spawn without one.
2. **A `LocalTargetProvider`** on any GameObject in the scene. One is enough.
   It finds targets and hands them to every enemy.
3. **Something to hunt.** By default the provider registers everything tagged
   `Player`. Point `targetTag` at a different tag if you prefer, or add a
   `StandaloneTarget` component to specific objects and clear the tag field.
4. **Your enemy prefab**, dropped on the NavMesh.

That's the whole integration. The enemy finds the provider itself.

---

## The first things you'll want to change

All of these live on the ScriptableObjects the Configurator generated — edit
them directly, or reopen the Configurator.

| To change | Edit |
|---|---|
| How far it sees, and how wide | `Sense ▸ senseInitDistance`, `fieldOfView` |
| How quickly it notices you | `Sense ▸ detectionRiseRate` (raise it) |
| How fast it forgets | `Sense ▸ detectionDecayRate` |
| How far it chases before giving up | `Combat ▸ rushRange` |
| Reach of the melee attack | `Combat ▸ attackRange` |
| Toughness | `Stats ▸ MaxHealth` |
| Whether it flees when hurt | `Behavior Options ▸ fleeOnLowHealth` |
| Whether a fled enemy heals back to full between fights | `Behavior Options ▸ regenerateToFullOutOfCombat` (off: it rejoins at `Stats ▸ RecoveredHealthCap` and heals no further) |

Two settings that behave differently than you might expect:

- **Speeds should be whole numbers** — see the note in step 1.
- **`fleeWhenOutnumbered` needs allies.** A lone enemy counts itself as
  outnumbered and will retreat on contact instead of fighting. It's a
  pack behaviour — leave it off unless you're spawning groups.

---

## Where to go next

| | |
|---|---|
| Other enemy types | [Archetypes](/guides/archetypes.md) — shooter, stealth, waves, boss |
| Multiplayer | [Photon Fusion 2 setup](/networking/fusion-setup.md) |
| Custom behaviour in code | [Extending the AI](/guides/extending.md) |
