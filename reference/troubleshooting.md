# Troubleshooting

Symptom first, because that's how you arrive here. Every row below is
collected from the setup pages; follow the link under each table for the
full explanation and fix.

Whatever the symptom, **`Tools ▸ EnemyAI ▸ Scene Doctor`** is the first thing
to run. Every check it makes corresponds to a real failure that has bitten
this AI before, and each finding has a **Select** button that jumps to the
culprit.

---

## Scene setup, targets and vision

| What you see | Almost always |
|---|---|
| Enemy patrols forever, never reacts, no errors | No target in the scene carrying the target tag, or no `LocalTargetProvider` |
| Enemy errors on spawn | No baked NavMesh |
| Shooter fires through walls | Cover geometry isn't on the layer its `coverMask` points at — re-pick the mask by name |
| Shooter never takes cover | Same cause; cover-seek needs colliders on the mask layer |
| Enemies never lose sight of you | Expected default — vision occlusion is off; see the setup page to enable it |
| Enemies are permanently blind | The floor is on the sight-blocker layer; take it off |
| Enemy walks in place | The animator has no transition for the state it entered |
| Enemy slides instead of running | A non-whole-number speed — the animator's speed parameter is an integer |

When in doubt, run **Scene Doctor**. Every check it makes corresponds to a
real failure that has bitten this AI before.

Full context: [Required project setup](/getting-started/required-setup.md).

---

## Photon Fusion 2

| What you see | Cause |
|---|---|
| `has not been weaved` / `FieldAccessException: Ptr` | `EnemyAI.Fusion` missing from `AssembliesToWeave` |
| Same errors after fixing that | Stale weave — delete `Library/ScriptAssemblies` and reopen Unity |
| Configurator offers only "Standalone" | Fusion or the FSM addon isn't installed; check the console line from Step 3 |
| Session never starts | No Photon App ID, or no internet — Fusion's cloud name server is required even on a LAN |
| Enemies frozen on clients, fine on host | Working as intended — clients don't simulate AI. If they're frozen on the *host* too, that's a NavMesh or target problem, not networking |
| Enemies do nothing at all | Confirm the scene's target registration; run `Tools ▸ EnemyAI ▸ Scene Doctor` |
| `does not implement interface member 'INetworkRunnerCallbacks....'` | Your Fusion is newer than the version this was validated against and Photon changed a callback signature. See **Newer Fusion versions** below — it is a two-line fix. |

Full context: [Photon Fusion 2 setup](/networking/fusion-setup.md), including the fix for newer Fusion versions.

---

## Still stuck?

See the **Support** section on the [overview page](/).
