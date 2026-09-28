# Enemy AI — Networked FSM for Photon Fusion 2

Finite-state-machine enemy AI with a data-driven ability system. Built for
**Photon Fusion 2** host-mode multiplayer, and it also runs completely
standalone for single-player projects — the same enemies, the same
configuration, no networking in the scene.

Enemies patrol, notice you gradually rather than instantly, investigate,
chase, attack in melee or at range, take cover, call for help, flee when
hurt, and ragdoll on death. Everything is configured through ScriptableObjects
and an editor window; you don't have to write code to ship a working enemy.

> **New here?** Install the package
> ([single-player](/getting-started/installation-standalone.md) ·
> [Photon Fusion 2](/getting-started/installation-fusion.md)), do the
> two-minute [required project setup](/getting-started/required-setup.md), then
> follow the [quick start](/getting-started/quick-start.md). Prefer watching?
> Every step is on the [video tutorials](/videos/) page.

---

## Requirements

**Unity 6000.0 LTS or newer.**

What you need beyond that depends on which runtime you use:

| | Single-player (standalone) | Networked (Fusion) |
|---|---|---|
| Photon Fusion 2 | not needed | **required** |
| Fusion FSM addon | not needed | **required** |
| Photon SimpleKCC addon | not needed | demo scenes only |
| Input System package | demo scenes only | demo scenes only |
| AI Navigation package | to bake NavMeshes | to bake NavMeshes |

The single-player runtime has **no external dependencies at all** — it needs
nothing from outside Unity. Every Unity package above is optional at compile
time: without it, the part that needs it (a demo scene's player controller,
the demo-scene builder's NavMesh bake) is left out and everything else still
compiles. The debug health label on the template prefabs uses TextMesh Pro,
which ships inside uGUI in Unity 6.

### If you want the networked runtime, read this

Photon Fusion 2 cannot be redistributed, so it isn't included — and it needs
**two separate downloads**, both free, from Photon:

1. **Photon Fusion 2** — validated against `2.0.12`
2. **The Fusion FSM addon** (`Fusion.Addons.FSM`) — validated against `2.0.5`

The FSM addon is a *separate* download from the Fusion SDK itself. The
networked state machine is built on it, so Fusion alone is not enough.

Install both, then see [Photon Fusion 2 setup](/networking/fusion-setup.md) for the two remaining steps (your
Photon App ID and one weaver registration).

> **You do not need to set any scripting defines.** The package detects Fusion
> and the FSM addon automatically and enables the networked assemblies for
> you. Until both are present it simply runs in single-player mode — no
> errors, no missing scripts.

---

## Installing

1. Import the package.
2. Set up the required layers and tags — see [Required project setup](/getting-started/required-setup.md). This takes a
   minute and the AI will not see targets or take cover without it.
3. Open a sample scene from `Samples/`, or follow [Quick start](/getting-started/quick-start.md) to build an
   enemy from scratch.

If you're using the networked runtime, install Fusion and the FSM addon first,
then follow [Photon Fusion 2 setup](/networking/fusion-setup.md).

---

## What's in the box

> 🎬 **See it in action:** [Editor tools walkthrough](/videos/?id=editor-tools)


**Runtime**

- `EnemyAI.Core` — the AI itself: senses, patrol, chase, attack, injured and
  healing abilities, the blackboard, and the ScriptableObject configuration
  layer. Depends on nothing.
- `EnemyAI.Standalone` — a plain-C# state machine and enemy component for
  single-player.
- `EnemyAI.Fusion` — the networked enemy, state machine, spawning and target
  management. Compiles only when Fusion and the FSM addon are installed.

**Editor tooling**

- **Enemy Configurator** (`Tools ▸ EnemyAI ▸ Enemy Configurator`) — pick an
  archetype, tune it, and get the ScriptableObjects and a ready-to-use enemy
  prefab in one click.
- **Scene Doctor** (`Tools ▸ EnemyAI ▸ Scene Doctor`) — checks an open scene
  for the setup mistakes that cause silent failures (no NavMesh, no target
  provider, animator on the wrong object, missing cover, and more).
- **Demo Scene builder** (`Tools ▸ EnemyAI ▸ Create Demo Scene`) — builds a
  playable single-player test scene around an enemy prefab.
- Range and field-of-view gizmos, and custom inspectors for wave and boss
  configuration.

**Archetypes** — Melee, Stealth, Shooter, Waves and Boss, each available as a
Configurator preset and a sample scene.

---

## Documentation

| File | What it covers |
|---|---|
| [Quick start](/getting-started/quick-start.md) | A working enemy chasing a target, from nothing |
| [Required project setup](/getting-started/required-setup.md) | Layers and tags the AI needs, and why |
| [Photon Fusion 2 setup](/networking/fusion-setup.md) | Photon App ID, weaver registration, host mode |
| [Archetypes](/guides/archetypes.md) | The five archetypes and what to tune on each |
| [Extending the AI](/guides/extending.md) | Writing your own abilities and swapping them at runtime |
| [Third-party notices](/reference/third-party.md) | Third-party notices |
| [Changelog](/reference/changelog.md) | Version history |

---

## Support

Questions, bugs and feature requests are welcome — see the store listing for
the current contact address.
