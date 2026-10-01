# Required project setup

Two minutes of setup, and the AI needs it. Skip it and the most likely
outcome isn't an error message — it's an enemy that patrols forever and
never notices you, or a shooter that fires straight through walls.

Run **`Tools ▸ EnemyAI ▸ Scene Doctor`** at any point to check a scene
against everything on this page.

---

## Why layer numbers matter here

Unity stores a LayerMask as a **bit value**, not a layer name. A mask of
`2048` means "bit 11" — whatever layer 11 happens to be called in *your*
project.

The ScriptableObjects shipped with this package were authored in a project
where layer 11 was `Obstacle`. **If your layer 11 is something else, the
shipped masks point at the wrong layer.** They won't error; they'll just
quietly do nothing.

You have two options, and the second is safer:

1. Create your `Obstacle` layer **at index 11**, so the shipped values line up.
2. Create it wherever you like, then **re-pick the mask** in the inspector on
   any `CombatAbilitySO` you use (the `coverMask` field). Picking it by name
   in the dropdown writes the correct bit value for *your* project.

The same caution applies if you ever reorder layers later: every stored mask
silently starts pointing somewhere else.

---

## Layers

| Layer | Used for | Required? |
|---|---|---|
| `Obstacle` | Cover geometry — blocks ranged shots and gives the Shooter something to hide behind (`CombatAbilitySO.coverMask`) | Yes, for the Shooter archetype |
| *(a spare empty layer)* | The default value of vision's `obstacleMask` — see below | Yes, leave one empty |

Put your **walls and cover** on the `Obstacle` layer. Do **not** put the floor
on it — see the next section for why that specifically matters.

### Vision line-of-sight is off by default

`SenseAbilitySO.obstacleMask` ships as `8` — bit 3, which in most projects is
an **empty layer**. A raycast against an empty layer hits nothing, so
line-of-sight checks always pass. **Out of the box, enemies can see through
walls.**

That default is deliberate, because of how the check works: the ray is cast
from the enemy's transform position to the target's transform position. Both
pivots normally sit at **floor level**, so the ray travels along the ground.
If the floor is on the same layer as your walls, every line-of-sight check is
blocked by the floor itself and enemies go permanently blind — a far worse
failure than seeing too much.

**To enable real wall occlusion:**

1. Create a dedicated layer for sight blockers — say `SightBlocker`.
2. Put your **walls on it, and nothing horizontal** (no floors, no ground, no
   ramps).
3. Set `obstacleMask` on your Vision `SenseAbilitySO` to that layer alone.

You can use the same geometry for cover and sight-blocking by assigning both
layers' purposes to the same walls — just keep the floor out of the sight mask.

> ### Two masks, two jobs — set both
>
> These are separate fields and they are easy to half-configure, because
> setting one gets you *most* of the behaviour and the gap is not obvious:
>
> | Field | Lives on | Decides |
> |---|---|---|
> | `obstacleMask` | Vision `SenseAbilitySO` | whether a wall **hides** you from the enemy's eyes |
> | `coverMask` | `CombatAbilitySO` | whether a wall **stops a bullet** and counts as cover |
>
> Set only `coverMask` and the Shooter will refuse to fire through a wall but
> still track you through it. Set only `obstacleMask` and it loses sight of you
> while its shots keep landing. Both want your wall geometry.

---

## Tags

| Tag | Used for | Required? |
|---|---|---|
| `Player` | What single-player enemies treat as a target. `LocalTargetProvider.targetTag` defaults to this and auto-registers everything carrying it | Yes, for single-player |
| `RegenerationZone` | A trigger volume where a retreating enemy heals | Only if you use the Retreat injured behaviour |

`Player` is just a default — you can point `targetTag` at any tag you prefer,
or clear it and register targets manually with a `StandaloneTarget` component.

If the tag named in `targetTag` doesn't exist in your project, the provider
logs an error rather than failing silently.

---

## A NavMesh, always

Every enemy drives a `NavMeshAgent`, so the scene needs a **baked NavMesh** or
enemies error the moment they spawn.

Bake one with a `NavMeshSurface` (Unity's AI Navigation package) or the legacy
`Window ▸ AI ▸ Navigation` workflow. The demo-scene builder
(`Tools ▸ EnemyAI ▸ Create Demo Scene`) bakes one for you.

If you add cover or geometry to an existing scene afterwards, **re-bake** —
otherwise enemies path straight through the new walls.

---

## TextMesh Pro essentials

The enemy's floating health label uses TextMesh Pro's default font, which
lives in TMP's **Essential Resources** rather than in this package. If your
project hasn't imported them yet, Unity usually offers to the first time a
label appears; otherwise use `Window ▸ TextMeshPro ▸ Import TMP Essential
Resources`. Until then the label is blank — the AI itself is unaffected.

---

## Troubleshooting

Symptom first, because that's how you'll arrive here.

| What you see | Almost always |
|---|---|
| Enemy patrols forever, never reacts, no errors | No target in the scene carrying the target tag, or no `LocalTargetProvider` |
| Enemy errors on spawn | No baked NavMesh |
| Shooter fires through walls | Cover geometry isn't on the layer its `coverMask` points at — re-pick the mask by name |
| Shooter never takes cover | Same cause; cover-seek needs colliders on the mask layer |
| Enemies never lose sight of you | Expected default — vision occlusion is off; see above to enable it |
| Enemies are permanently blind | The floor is on the sight-blocker layer; take it off |
| Enemy walks in place | The animator has no transition for the state it entered |
| Enemy slides instead of running | A non-whole-number speed — the animator's speed parameter is an integer |
| Health label above the enemy is blank | TMP Essential Resources not imported; see above |
| Demo enemies and props render pink | The project isn't on URP — the demo content is authored for it (see the Render pipeline note in [Overview](/)) |

When in doubt, run **Scene Doctor**. Every check it makes corresponds to a
real failure that has bitten this AI before.
