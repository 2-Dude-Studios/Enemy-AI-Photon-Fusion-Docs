# Video tutorials

Short, narrated captures. Each one links to the written page it belongs with,
so you can watch first and then read the details.

## Installation

<div class="video-grid">
  <div class="video-card" id="installation-standalone">
    <video controls preload="metadata" src="videos/installation-standalone.mp4"></video>
    <div class="video-body">
      <h4>Single-player installation</h4>
      <p>Import the package. No dependencies, no configuration.</p>
      <div class="video-links"><a href="#/getting-started/installation-standalone">Written guide</a><a href="#/getting-started/quick-start">Quick start</a></div>
    </div>
  </div>
  <div class="video-card" id="installation-fusion">
    <video controls preload="metadata" src="videos/installation-fusion.mp4"></video>
    <div class="video-body">
      <h4>Photon Fusion 2 installation</h4>
      <p>Fusion SDK, FSM and Simple KCC addons, weaver registration, App ID.</p>
      <div class="video-links"><a href="#/getting-started/installation-fusion">Written guide</a><a href="#/networking/fusion-setup">Fusion setup</a></div>
    </div>
  </div>
</div>

## Editor tools

<div class="video-grid">
  <div class="video-card" id="editor-tools">
    <video controls preload="metadata" src="videos/editor-tools.mp4"></video>
    <div class="video-body">
      <h4>Editor tools walkthrough</h4>
      <p>Enemy Configurator, Scene Doctor and the demo-scene builder: from an empty project to a configured enemy without writing code.</p>
      <div class="video-links"><a href="#/getting-started/quick-start">Quick start</a><a href="#/guides/archetypes">Archetypes</a></div>
    </div>
  </div>
</div>

## Single-player enemies

Standalone sample scenes, showing the state flow you'll see in your own
project: **patrol → awareness builds → rush → attack**, and for the shooter,
falling back to cover.

<div class="video-grid">
  <div class="video-card" id="standalone-melee">
    <video controls preload="metadata" src="videos/standalone-melee.mp4"></video>
    <div class="video-body">
      <h4>Melee enemy</h4>
      <p>The <em>Custom</em> archetype baseline: gradual detection, chase, melee strikes.</p>
      <div class="video-links"><a href="#/guides/archetypes">Archetype: Custom</a><a href="#/getting-started/quick-start">Quick start</a></div>
    </div>
  </div>
  <div class="video-card" id="standalone-shooter">
    <video controls preload="metadata" src="videos/standalone-shooter.mp4"></video>
    <div class="video-body">
      <h4>Shooter enemy</h4>
      <p>Holds its distance, fires on a cooldown, retreats to cover when you close in.</p>
      <div class="video-links"><a href="#/guides/archetypes">Archetype: Shooter</a><a href="#/getting-started/required-setup">Cover layer setup</a></div>
    </div>
  </div>
  <div class="video-card" id="melee-patrol-rush-attack">
    <video controls preload="metadata" src="videos/melee-patrol-rush-attack.mp4"></video>
    <div class="video-body">
      <h4>Melee: patrol, rush, attack</h4>
      <p>A closer look at the state transitions on the melee enemy.</p>
      <div class="video-links"><a href="#/guides/archetypes">Archetype: Custom</a></div>
    </div>
  </div>
  <div class="video-card" id="melee-jump-lunge">
    <video controls preload="metadata" src="videos/melee-patrol-rush-jump-attack.mp4"></video>
    <div class="video-body">
      <h4>Melee: jump-lunge attack</h4>
      <p>Same enemy with the optional jump-lunge, closing the last few metres in one leap.</p>
      <div class="video-links"><a href="#/guides/archetypes">Archetype: Custom</a></div>
    </div>
  </div>
  <div class="video-card" id="shooter-patrol-rush-attack-flee">
    <video controls preload="metadata" src="videos/shooter-patrol-rush-attack-flee.mp4"></video>
    <div class="video-body">
      <h4>Shooter: patrol, rush, fire, fall back</h4>
      <p>A closer look at the shooter's kiting and cover-seeking.</p>
      <div class="video-links"><a href="#/guides/archetypes">Archetype: Shooter</a></div>
    </div>
  </div>
</div>

## Networked enemies (Photon Fusion 2)

The same enemies in the Fusion sample scenes. The host simulates the AI;
clients render the replicated state.

<div class="video-grid">
  <div class="video-card" id="fusion-melee">
    <video controls preload="metadata" src="videos/fusion-melee.mp4"></video>
    <div class="video-body">
      <h4>Melee over Fusion</h4>
      <p>The melee enemy in a host-mode session.</p>
      <div class="video-links"><a href="#/networking/fusion-setup">Fusion setup</a><a href="#/guides/archetypes">Archetype: Custom</a></div>
    </div>
  </div>
  <div class="video-card" id="fusion-shooter">
    <video controls preload="metadata" src="videos/fusion-shooter.mp4"></video>
    <div class="video-body">
      <h4>Shooter over Fusion</h4>
      <p>Ranged combat and cover-seeking, replicated to clients.</p>
      <div class="video-links"><a href="#/networking/fusion-setup">Fusion setup</a><a href="#/guides/archetypes">Archetype: Shooter</a></div>
    </div>
  </div>
  <div class="video-card" id="fusion-waves">
    <video controls preload="metadata" src="videos/fusion-waves.mp4"></video>
    <div class="video-body">
      <h4>Waves over Fusion</h4>
      <p>The networked wave spawner: per-wave composition and automatic progression.</p>
      <div class="video-links"><a href="#/guides/archetypes">Archetype: Waves</a></div>
    </div>
  </div>
</div>

## Coming later

- Waves in single-player, and waves with mixed enemy types over Fusion
- Boss phases
