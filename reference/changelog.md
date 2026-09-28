# Changelog

All notable changes to this package are documented here.

This project follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — Initial release

First public release. Requires **Unity 6000.0 LTS** or newer.

### Two runtimes, one AI

- **Standalone** — the full AI with no networking and **no external
  dependencies**. Drop an enemy in a scene and press Play.
- **Photon Fusion 2** — the same enemies networked in Host (or Server) mode,
  where the host simulates and clients render replicated state. Requires
  Photon Fusion 2 and the Fusion FSM addon (both free, obtained from Photon).
  The Fusion demo scenes additionally use Photon's SimpleKCC addon and Unity's
  Input System for their sample player.
- **Works with your own launcher** — enemy authority comes from Fusion itself,
  and players become targets as soon as their `NetworkedTarget` spawns. The
  included `FusionBootstrapper` is a demo launcher, not a requirement.

The networked assemblies enable themselves automatically once their
dependencies are detected; no scripting defines to set by hand. Unity's Input
System and AI Navigation packages are optional at compile time: without them,
only the parts that need them (the demo players, the demo-scene NavMesh bake)
are left out.

### Behaviour

- **Gradual detection** — awareness builds while a target is visible and
  decays when it isn't, crossing a suspicion threshold to investigate and a
  detection threshold to commit. Not a line-of-sight boolean.
- **Hearing** — footstep noise, attenuated by blocker layers, raises
  suspicion and sends the enemy to investigate.
- **Patrol** — random-area or waypoint.
- **Chase and melee attack**, including an optional jump-lunge.
- **Ranged combat** — hitscan fire on a cooldown, kiting to hold a preferred
  distance, and cover-seeking when the target closes in.
- **Call for help** — an alert bus that raises the awareness of nearby allies
  on detection or on an ally's death.
- **Fleeing** — triggered by low health, being outnumbered, or an ally going
  down; each toggled per enemy. A fleeing enemy heads for a regeneration zone,
  or backs away from the threat.
- **Recovery** — passive regeneration while injured, faster healing inside
  regeneration zones, and an optional per-enemy switch to regenerate back to
  full health between fights.
- **Runtime ability swapping** — change how an enemy chases, attacks or flees
  while it's alive.
- **Ragdoll on death**, simulated per-peer so it costs no bandwidth.

### Archetypes

Melee, Stealth, Shooter, Waves and Boss Configurator presets, with ready-made
enemies for each and sample scenes for Melee, Shooter, Waves and Boss in both
runtimes. Includes a wave system with per-wave enemy composition and
automatic progression, and health-threshold boss phases.

### Editor tooling

- **Setup window** — checks the project for the layers, tags and settings the
  AI needs, and fixes them at a button press (never unprompted).
- **Enemy Configurator** — pick an archetype, tune it, and generate the
  ScriptableObjects plus a ready-to-use prefab in one click. Each enemy gets
  its own folder; re-opening an enemy updates it in place and keeps its
  runtime.
- **Scene Doctor** — checks an open scene for the setup mistakes that fail
  silently, with a jump-to-culprit button on every finding.
- **Demo Scene builder** — builds a playable single-player test scene around
  an enemy prefab, NavMesh baked.
- **Add Cover To Open Scene** — drops Obstacle-layer cover into any scene.
- Range, field-of-view and waypoint gizmos, plus custom inspectors for wave
  and boss configuration with play-mode controls.
- The package can live anywhere under `Assets/`.

### Configuration and extending

- An enemy definition plus six ScriptableObjects cover stats, senses, patrol,
  combat, injured behaviour and healing. Per-enemy alert, flee and recovery
  switches live on the enemy component. Cross-field validation catches
  inconsistent setups before play mode.
- Custom behaviours plug in through `IAbility` — simulation hooks for logic,
  render hooks for visuals — and run unchanged on both runtimes. See
  [Extending the AI](/guides/extending.md).

---

<!--
Template for subsequent entries:

## [1.0.1] — YYYY-MM-DD

### Fixed
- ...

### Changed
- ...

### Added
- ...
-->
