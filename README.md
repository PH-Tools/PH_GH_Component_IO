# PH Grasshopper Component IO
### A utility library to support Rhino/Grasshopper Python components

`ph_gh_component_io` is the shared **input/output plumbing** used by the PH-Tools Grasshopper component libraries (Honeybee-PH, HBPH+, Honeybee-REVIVE, etc.). It provides the `IGH` interface that hides the Rhino/Grasshopper API behind one object, plus helpers for reading component inputs, previewing objects, validating user input, and shelling out to a CPython subprocess.

It runs inside Rhino's **IronPython 2.7** interpreter, so it is written to be Python-2.7 compatible.

## What's inside

- **`gh_io.py`** — the `IGH` interface class (the seam that hides Rhino/Grasshopper/`ladybug_rhino` API calls), plus `ComponentInput` / `ComponentOutput` and helpers to wire up component inputs/outputs.
- **`input_tools.py`** — clean/convert user inputs (`input_to_int`, `clean_get`, `clean_tree_get`, `memoize`).
- **`preview.py`** — `object_preview` for pretty-printing Python objects on the canvas. (`output_tools.py` is a legacy duplicate of the same.)
- **`run_subprocess.py`** — run a CPython subprocess from an IronPython component (how GH components dispatch heavy compute).
- **`validators.py`** — descriptor-based validators for component inputs (`NotNone`, `HBName`, `IntegerNonZero`, `Float`, …).

## Installation

Distributed via GitHub (not PyPI). It is installed onto the Rhino Python path by the PH-Tools plugin installers, or vendored by the consuming component libraries.

## Development

Must remain **IronPython 2.7** compatible (it loads in Rhino). For contributor/agent orientation see [`CLAUDE.md`](CLAUDE.md) and the [`context/`](context/) folder.

[![IronPython](https://img.shields.io/badge/ironpython-2.7-red.svg)](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8/)
