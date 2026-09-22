# Installing for Photon Fusion 2

Only needed for **networked** enemies. For single-player, use
[Install: single-player](/getting-started/installation-standalone.md) instead;
nothing on this page applies.

Requires **Unity 6000.0 LTS or newer** and three free downloads from Photon.

<div class="video-single video-card">
  <div class="video-pending">🎬 Fusion installation walkthrough<br>Video coming soon. The written steps below cover everything shown in it.</div>
  <!-- When the video is on YouTube, replace the div above with:
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Fusion installation guide" allowfullscreen></iframe>
  -->
  <div class="video-body">
    <h4>Fusion installation guide</h4>
    <p>Fusion SDK, the two addons, weaver registration and the App ID. About five minutes.</p>
  </div>
</div>

## What you need from Photon

| Download | Validated against | Needed by |
|---|---|---|
| **Photon Fusion 2** SDK | `2.0.12` | the networked runtime |
| **Fusion FSM** addon (`Fusion.Addons.FSM`) | `2.0.5` | the networked runtime |
| **Fusion Simple KCC** addon | current | the **Fusion sample scenes** only (their demo player) |

All three come from [Photon's Fusion page](https://www.photonengine.com/fusion)
and its addons section. The FSM addon is a *separate* download from the SDK;
Fusion on its own is not enough. Simple KCC is only used by the sample player
controller, so skip it if you delete the samples.

## Steps

1. Open the Unity project you want the Enemy AI system in.
2. Install the **Photon Fusion 2** SDK: import its `.unitypackage`, or install
   it from **Window ▸ Package Manager ▸ My Assets** if you got it from the
   Asset Store.
3. Import the **Enemy AI** package.
4. Import the **Fusion FSM** and **Fusion Simple KCC** addon packages. Order
   doesn't matter; you can install the addons before Enemy AI too.
5. Open **`Assets/Photon/Fusion/Resources/NetworkProjectConfig.fusion`** and,
   under **Assemblies To Weave**, add these two assemblies:

   ```
   EnemyAI.Fusion
   EnemyAI.Samples.Fusion
   ```

   Fusion rewrites ("weaves") any assembly containing networked code. An
   unweaved assembly compiles fine and then fails at runtime, so this step is
   the one people miss. `Fusion.Addons.FSM` should already be in the list;
   check rather than assume.
6. Paste your **Photon App ID** into the `PhotonAppSettings` asset (or via
   **Tools ▸ Fusion ▸ Fusion Hub**). Create the app in the
   [Photon dashboard](https://dashboard.photonengine.com) if you haven't.

## Check it worked

The console prints a one-time line once both dependencies are detected:

```
[EnemyAI] Fusion + FSM addon detected — enabled ENEMYAI_FUSION.
```

After that, the Enemy Configurator's **Runtime** dropdown offers **Fusion**
alongside Standalone, and `NetworkedEnemy` appears in the Add Component menu.

If you see `has not been weaved` or `FieldAccessException: Ptr` at runtime,
step 5 was skipped. If the errors persist after fixing it, close Unity, delete
`Library/ScriptAssemblies`, and reopen.

## Next

- [Photon Fusion 2 setup](/networking/fusion-setup.md): host mode, scene
  setup, troubleshooting, and what to do on a newer Fusion version.
- [Required project setup](/getting-started/required-setup.md): the layers
  and tags every enemy needs, networked or not.
- Open the Fusion sample scene under `Assets/EnemyAI/Samples/Fusion/` and use
  it as your reference rig.
