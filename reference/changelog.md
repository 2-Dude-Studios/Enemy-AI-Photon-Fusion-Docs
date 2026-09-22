# Changelog

All notable changes to this package are documented here.

This project follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — Initial release

First public release. Requires **Unity 6000.0 LTS** or newer.

### Two runtimes, one AI

- **Standalone** — the full AI with no networking and **no external
  dependencies**. Drop an enemy in a scene and press Play.
- **Photon Fusion 2** — the same enemies networked in host mode, where the
  host simulates and clients render replicated state. Requires Photon Fusion 2
  and the Fusion FSM addon (both free, obtained from Photon).

The networked assemblies enable themselves automatically once both
dependencies are detected; no scripting defines to set by hand.

### Behaviour

- **Gradual detection** — awareness builds while a target is visible and
  decays when it isn't, crossing a suspicion threshold to investigate and a
  detection threshold to commit. Not a line-of-sight boolean.
- **Patrol** — random-area or waypoint.
- **Chase and melee attack**, including an optional jump-lunge.
- **Ranged combat** — hitscan fire on a cooldown, kiting to hold a preferred
  distance, and cover-seeking when the target closes in.
- **Call for help** — an alert bus that raises the awareness of nearby allies
  on detection or on an ally's death.
- **Fleeing** — triggered by low health, being outnumbered, or an ally going
  down; each toggled per enemy.
- **Runtime ability swapping** — change how an enemy chases, attacks or flees
  while it's alive.
- **Ragdoll on death**, simulated per-peer so it costs no bandwidth.

### Archetypes

Melee, Stealth, Shooter, Waves and Boss — each a Configurator preset with a
sample scene. Includes a wave system with per-wave enemy composition and
automatic progression, and health-threshold boss phases.

### Editor tooling

- **Enemy Configurator** — pick an archetype, tune it, and generate the
  ScriptableObjects plus a ready-to-use prefab in one click.
- **Scene Doctor** — checks an open scene for the setup mistakes that fail
  silently, with a jump-to-culprit button on every finding.
- **Demo Scene builder** — builds a playable single-player test scene around
  an enemy prefab, NavMesh baked.
- **Add Cover To Open Scene** — drops Obstacle-layer cover into any scene.
- Range, field-of-view and waypoint gizmos, plus custom inspectors for wave
  and boss configuration with play-mode controls.

### Configuration

Seven ScriptableObjects per enemy covering stats, senses, patrol, combat,
injured behaviour, healing and per-enemy behaviour toggles. Cross-field
validation catches inconsistent setups before play mode.

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
