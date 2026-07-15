---
DATE: 2026-07-15
STATUS: CANONICAL
---

# PH-GH-Component-IO — Architecture

## The role

This is a **leaf utility library**: the plumbing every PH-Tools Grasshopper component is built on. A component in a plugin repo (`GHCompo_*`) receives an `IGH` and uses these helpers to read inputs, validate them, preview objects, and dispatch heavy compute — none of that boilerplate is re-implemented per plugin.

## Modules

- **`gh_io.py`** — the heart. `IGH` is the interface object that hides all Rhino / Grasshopper / `ladybug_rhino` API calls behind one seam, so component logic stays testable and Rhino-API-free. Also defines `ComponentInput` / `ComponentOutput` and the helpers that wire a component's inputs/outputs (`handle_inputs`, `setup_component_inputs`, `setup_component_outputs`). This is the same `IGH` seam the plugin repos route through.
- **`input_tools.py`** — input hygiene: `input_to_int`, `clean_get` / `clean_tree_get` / `cleaner_get` (safe indexed access into lists/GH trees with defaults), `memoize`.
- **`preview.py`** — `object_preview(obj, ...)` for recursively pretty-printing an object and its sub-objects on the canvas. `output_tools.py` is a **legacy duplicate** of the same function (kept for import compatibility).
- **`validators.py`** — a `Validated` descriptor base plus concrete validators (`NotNone`, `HBName`, `IntegerNonZero`, `IntegerPositiveValueOrZero`, `Float`, …) used as class descriptors to validate/clean component inputs.
- **`run_subprocess.py`** — `run_subprocess(...)` / `run_subprocess_from_shell(...)`: run a CPython subprocess from an IronPython component and marshal stdout/stderr back through `IGH`. This is how GH components dispatch compute that can't run in IPy2.7 (e.g. ADORB/pandas).

## API stability

`IGH`, the `input_tools` helpers, and the validators are imported across multiple plugin repos. Their signatures are a contract — see `CODING_STANDARDS.md`.
