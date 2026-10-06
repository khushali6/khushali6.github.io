# Khushali Pariyal — Portfolio

Static portfolio site for **khushali6.github.io**. No framework, no build step needed to serve it.

- `index.html`, `meadow/`, `casora/`, `splitmate/`, `laya/`, `work/` — generated pages
- `assets/` — CSS, JS, and illustrative UI mockups (SVG). No personal photos.
- `tools/build.py` — regenerates every page from one source: `python3 tools/build.py`
- Live data: `assets/app.js` pulls repo metadata and the "workbench" grid from the public GitHub API (cached 10 min per tab; degrades gracefully if rate-limited).

## Deploy
Repo Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`. `.nojekyll` is included.
