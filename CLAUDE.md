# PH-GH-Component-IO

The shared **input/output plumbing** for the PH-Tools Grasshopper component libraries — the `IGH` interface, input cleaning, object preview, input validators, and the CPython subprocess bridge. Consumed by Honeybee-PH, HBPH+, Honeybee-REVIVE-Grasshopper, etc. Source: https://github.com/PH-Tools/PH_GH_Component_IO (distributed via GitHub, not PyPI).

> **Runtime constraint (critical):** runs inside Rhino's **IronPython 2.7** interpreter — every module carries a `# -*- Python Version: 2.7 -*-` header. All code must be Python-2.7 safe. Apply the **ironpython-27-compatibility** skill; repo specifics in `context/CODING_STANDARDS.md`.

## What this repo is

A single package, `ph_gh_component_io`:

| Module | Purpose |
|--------|---------|
| `gh_io.py` | The `IGH` interface (hides Rhino/GH/`ladybug_rhino` API), `ComponentInput`/`ComponentOutput`, input/output wiring helpers |
| `input_tools.py` | Clean/convert user inputs (`input_to_int`, `clean_get`, `clean_tree_get`, `memoize`) |
| `preview.py` | `object_preview` — pretty-print objects on the canvas (`output_tools.py` is a legacy duplicate) |
| `run_subprocess.py` | Run a CPython subprocess from an IronPython component (heavy-compute dispatch) |
| `validators.py` | Descriptor-based input validators (`NotNone`, `HBName`, `IntegerNonZero`, `Float`, …) |

## Where things live — read before working

| Working on… | Read |
|-------------|------|
| Scope, what belongs here | `context/PRD.md` |
| What each module does, how `IGH` is used | `context/ARCHITECTURE.md` |
| IPy2.7 rules, validator pattern, testing | `context/CODING_STANDARDS.md` |
| Packaging, distribution, CI, versioning | `context/TECH_STACK.md` |
| Current / in-flight work | `planning/STATUS.md` |

Full context index: `context/README.md`. (No `docs/` hub spoke.)

## Hard rules

1. **IronPython 2.7 compatibility is mandatory.** No f-strings/`pathlib`/modern stdlib; comment-style type hints; guard `typing` imports; keep the `# -*- Python Version: 2.7 -*-` header. This library loads in Rhino — breaking IPy2.7 breaks every downstream GH plugin.
2. **This is a foundational dependency — keep the public API stable.** `IGH`, the input helpers, and the validators are imported by multiple plugin repos. Changing a signature ripples outward; treat it as a breaking change.
3. **No runtime dependencies.** `dependencies = []` on purpose (it wraps Rhino/GH APIs that only exist at runtime; `ladybug_rhino` etc. are imported defensively).
4. **Distribution is GitHub + tag only** (no PyPI publish). `bump-my-version` tags `v{version}` in `pyproject.toml`.
5. **Tests:** CI runs `python -m pytest tests/` but no `tests/` exists yet — adding a suite is an open improvement (`planning/`).

## Ecosystem

Consumed by the Grasshopper plugin repos (`honeybee_grasshopper_ph`, `honeybee_grasshopper_ph_plus`, `honeybee_REVIVE_grasshopper`) — this is where their shared `IGH` / IO helpers originate.
