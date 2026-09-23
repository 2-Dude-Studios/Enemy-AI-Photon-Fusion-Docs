# Maintaining this site

This is a [Docsify](https://docsify.js.org) site: static files, no build step.
Any static host serves it, which is what lets it move to a sub-page of the
2 Dude Studios website later by copying the folder.

## Where the content comes from

| Content | Source |
|---|---|
| Overview, Quick start, Required setup, Fusion setup, Archetypes, Extending, Changelog, Third-party, Troubleshooting | **Generated** from the package docs by `tools/sync_from_package.py`. Edit the originals in `Assets/EnemyAI/Documentation/` in the Unity project, then re-run the script. |
| `getting-started/installation-*.md`, `videos/README.md`, `_sidebar.md`, `index.html`, `assets/site.css` | Hand-written here. |

Re-sync after changing package docs:

```bash
python tools/sync_from_package.py
```

It defaults to the sibling folder `../Enemy-AI-Fusion-FSM`; pass the path to
`Assets/EnemyAI/Documentation` to override.

## Videos

Files under `videos/` are served straight from the repo. Keep each under
GitHub's 100 MB limit (re-encode if needed; the Fusion guide is 79 MB). To
host one on YouTube instead, replace its `<video>` element with:

```html
<iframe src="https://www.youtube.com/embed/VIDEO_ID" title="..." allowfullscreen></iframe>
```

## Publishing on GitHub Pages

1. Push this repo to a **public** GitHub repository.
2. Settings ▸ Pages ▸ Source: *Deploy from a branch* ▸ `main` / `/ (root)`.
3. The site appears at `https://<org>.github.io/<repo>/` within a minute or two.

## Moving to the website

Copy the whole folder to e.g. `yoursite.com/docs/enemy-ai/`. Nothing needs to
change: routing is hash-based and all asset paths are relative.

## Preview locally

```bash
python -m http.server 8765
```

then open <http://localhost:8765>.

## To do

- Make the tutorial videos shorter (the Fusion install guide is 3:26 / 79 MB).
- Add subtitles. The narration scripts already exist as `.docx` files next to
  the captures; convert each to a WebVTT file in `videos/` and add
  `<track kind="subtitles" src="videos/<name>.vtt" srclang="en" label="English" default>`
  inside the matching `<video>` element.
