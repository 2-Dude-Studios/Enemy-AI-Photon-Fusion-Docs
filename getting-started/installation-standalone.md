# Installing for single-player

The standalone runtime needs **nothing but Unity**: no Photon, no extra
packages, no scripting defines. Importing the package is the whole install.

Requires **Unity 6000.0 LTS or newer**.

<div class="video-single video-card">
  <video controls preload="metadata" src="videos/installation-standalone.mp4"></video>
  <div class="video-body">
    <h4>Standalone installation guide</h4>
    <p>Import the package and you're done. Under a minute.</p>
  </div>
</div>

## Steps

1. Open the Unity project you want the Enemy AI system in.
2. Import the **Enemy AI** package from the Package Manager (**Window ▸
   Package Manager ▸ My Assets**), or double-click the `.unitypackage`.
3. Keep everything selected in the import dialog and click **Import**.

That's it. Once the import finishes, `Tools ▸ EnemyAI` appears in the menu
bar and the single-player runtime is ready to use.

> The package also contains the networked runtime. Until Photon Fusion 2 and
> the Fusion FSM addon are installed it stays dormant: no errors, no missing
> scripts, nothing to configure. Add them later and it switches itself on. See
> [Install: Photon Fusion 2](/getting-started/installation-fusion.md).

## Next

1. [Required project setup](/getting-started/required-setup.md): two minutes
   of layers and tags. Skip it and enemies patrol forever without noticing you.
2. [Quick start](/getting-started/quick-start.md): a patrolling, chasing,
   attacking enemy in about five minutes.
3. Or open a sample scene under `Assets/EnemyAI/Samples/Standalone/`.
