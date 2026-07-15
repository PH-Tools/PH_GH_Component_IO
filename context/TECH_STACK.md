---
DATE: 2026-07-15
STATUS: CANONICAL
---

# PH-GH-Component-IO — Tech Stack

## Runtime

- **IronPython 2.7** (Rhino's GHPython interpreter). Every module carries `# -*- Python Version: 2.7 -*-`. Declared `requires-python = ">=3.10"` covers the CPython tooling/typing side, but the shipping code must stay IPy2.7-safe.

## Dependencies

- **Runtime: none** (`dependencies = []`). It wraps Rhino/GH APIs that exist only at runtime; `ladybug_rhino` and similar are imported defensively where needed.
- Dev extras: `black`, `isort`, `Grasshopper-stubs`, `Rhino-stubs` (stubs for static checking against the GH/Rhino API).

## Packaging & distribution

- `pyproject.toml` has real `[project]` metadata (name `PH-GH-Component-IO`, GPL-3.0), single package `ph_gh_component_io`.
- **Distributed via GitHub, not PyPI.** Installed onto the Rhino Python path by the plugin installers / vendored by consumers.

## Versioning

- `bump-my-version` updates the version in `pyproject.toml` and tags `v{version}`. **No publish step** — tag only.

## CI

- `.github/workflows/ci.yml` runs on push/PR to main: `python -m pytest tests/ || echo "No tests found — skipping"` (tests are a no-op until a `tests/` dir exists), then auto bump-and-tag + GitHub Release.

## Formatting

- **Black**, line length 120 (no ruff configured here).

## Docs

- No `docs/` folder / docs-hub spoke in this repo.
