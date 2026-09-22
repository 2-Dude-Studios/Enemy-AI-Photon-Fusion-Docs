#!/usr/bin/env python
"""Sync the package documentation into this docs site.

The Markdown that ships inside the Unity package
(<project>/Assets/EnemyAI/Documentation/*.md) is the single source of truth.
This script copies each file to its place in the site, rewrites the
`SomeFile.md` cross-references into site links, injects the video callouts,
and assembles reference/troubleshooting.md from the troubleshooting tables.

Usage:
    python tools/sync_from_package.py                # default sibling project
    python tools/sync_from_package.py <path to Assets/EnemyAI/Documentation>

Hand-written pages (installation-*.md, videos/README.md) are never touched.
"""
import pathlib
import re
import sys

SITE = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SRC = (SITE.parent / "Enemy-AI-Fusion-FSM" / "Assets" / "EnemyAI"
               / "Documentation")

# package file -> (site path, link title)
PAGES = {
    "README.md":        ("README.md",                        "Overview"),
    "QuickStart.md":    ("getting-started/quick-start.md",    "Quick start"),
    "RequiredSetup.md": ("getting-started/required-setup.md", "Required project setup"),
    "FusionSetup.md":   ("networking/fusion-setup.md",        "Photon Fusion 2 setup"),
    "Archetypes.md":    ("guides/archetypes.md",              "Archetypes"),
    "Extending.md":     ("guides/extending.md",               "Extending the AI"),
    "ThirdParty.md":    ("reference/third-party.md",          "Third-party notices"),
    "CHANGELOG.md":     ("reference/changelog.md",            "Changelog"),
}

def site_link(pkg_file: str) -> str:
    path, title = PAGES[pkg_file]
    route = "/" if path == "README.md" else "/" + path
    return f"[{title}]({route})"

LINK_RE = re.compile(r"`(" + "|".join(re.escape(k) for k in PAGES) + r")`")

def rewrite_links(text: str) -> str:
    return LINK_RE.sub(lambda m: site_link(m.group(1)), text)

# ---- video callouts injected into synced pages ---------------------------

VIDEO = {
    "melee":   ("/videos/?id=melee-patrol-rush-attack",      "Melee: patrol, rush, attack"),
    "jump":    ("/videos/?id=melee-jump-lunge",              "Melee: jump-lunge attack"),
    "shooter": ("/videos/?id=shooter-patrol-rush-attack-flee", "Shooter: patrol, rush, fire, fall back to cover"),
    "install": ("/getting-started/installation-standalone.md", "Installing the package (video)"),
}

def callout(*keys):
    items = " · ".join(f"[{VIDEO[k][1]}]({VIDEO[k][0]})" for k in keys)
    return f"\n> 🎬 **See it in action:** {items}\n"

def inject_after_heading(text: str, heading_prefix: str, snippet: str) -> str:
    """Insert snippet after the first heading line starting with heading_prefix."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith(heading_prefix):
            lines.insert(i + 1, snippet)
            return "\n".join(lines)
    print(f"  ! heading not found: {heading_prefix!r}")
    return text

HOME_BANNER = """
> **New here?** Install the package
> ([single-player](/getting-started/installation-standalone.md) ·
> [Photon Fusion 2](/getting-started/installation-fusion.md)), do the
> two-minute [required project setup](/getting-started/required-setup.md), then
> follow the [quick start](/getting-started/quick-start.md). Prefer watching?
> Every step is on the [video tutorials](/videos/) page.
"""

INJECTIONS = {
    "README.md":     [("first-rule", HOME_BANNER)],
    "QuickStart.md": [("# Quick start", callout("install", "melee"))],
    "Archetypes.md": [("## Custom", callout("melee", "jump")),
                      ("## Shooter", callout("shooter"))],
}

def apply_injections(pkg_file: str, text: str) -> str:
    for where, snippet in INJECTIONS.get(pkg_file, []):
        if where == "first-rule":
            text = text.replace("\n---\n", snippet + "\n---\n", 1)
        else:
            text = inject_after_heading(text, where, snippet)
    return text

# ---- troubleshooting page assembled from the source tables ---------------

def extract_section(text: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*$", text, flags=re.M)
    if not m:
        return ""
    body = text[m.end():]
    end = re.search(r"^(## |---\s*$)", body, flags=re.M)
    body = (body[:end.start()] if end else body).strip()
    # Drop the source page's own lead-in sentence and re-point "see above".
    body = re.sub(r"^Symptom first[^\n]*\n+", "", body)
    return body.replace("see above", "see the setup page")

def build_troubleshooting(src: pathlib.Path) -> str:
    req = extract_section((src / "RequiredSetup.md").read_text("utf-8"), "Troubleshooting")
    fus = extract_section((src / "FusionSetup.md").read_text("utf-8"), "Troubleshooting")
    return rewrite_links(f"""# Troubleshooting

Symptom first, because that's how you arrive here. Every row below is
collected from the setup pages; follow the link under each table for the
full explanation and fix.

Whatever the symptom, **`Tools ▸ EnemyAI ▸ Scene Doctor`** is the first thing
to run. Every check it makes corresponds to a real failure that has bitten
this AI before, and each finding has a **Select** button that jumps to the
culprit.

---

## Scene setup, targets and vision

{req}

Full context: `RequiredSetup.md`.

---

## Photon Fusion 2

{fus}

Full context: `FusionSetup.md`, including the fix for newer Fusion versions.

---

## Still stuck?

See the **Support** section on the [overview page](/).
""")

# ---- main ----------------------------------------------------------------

def main():
    src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    if not src.is_dir():
        sys.exit(f"Documentation folder not found: {src}")
    print(f"Syncing from {src}")
    for pkg_file, (site_path, _) in PAGES.items():
        text = (src / pkg_file).read_text("utf-8")
        text = apply_injections(pkg_file, rewrite_links(text))
        out = SITE / site_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, "utf-8", newline="\n")
        print(f"  {pkg_file:18} -> {site_path}")
    out = SITE / "reference" / "troubleshooting.md"
    out.write_text(build_troubleshooting(src), "utf-8", newline="\n")
    print(f"  {'(assembled)':18} -> reference/troubleshooting.md")

if __name__ == "__main__":
    main()
