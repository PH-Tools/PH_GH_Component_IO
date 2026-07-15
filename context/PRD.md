---
DATE: 2026-07-15
STATUS: CANONICAL PRD
---

# PH-GH-Component-IO — Product Requirements

## 1. Goal

Give the PH-Tools Grasshopper component libraries one shared, tested place for the boilerplate every GH Python component needs: a Rhino/GH API seam (`IGH`), input reading/cleaning, object preview, input validation, and CPython subprocess dispatch. Write it once here instead of copy-pasting it into each plugin.

## 2. Who uses it

The Grasshopper plugin repos — `honeybee_grasshopper_ph`, `honeybee_grasshopper_ph_plus`, `honeybee_REVIVE_grasshopper` — import these helpers at runtime inside Rhino (IronPython 2.7).

## 3. What belongs here

- The `IGH` interface and component input/output wiring (`gh_io.py`).
- Input cleaning/conversion utilities (`input_tools.py`).
- Object preview (`preview.py`).
- Input validators (`validators.py`).
- The CPython subprocess bridge (`run_subprocess.py`).

Generic, reusable GH-component plumbing — nothing domain-specific (no Passive House model logic).

## 4. Non-goals

- **No domain/model logic** — that lives in the honeybee-* libraries.
- **No components** — this is the plumbing components are built *on*, not components themselves.
- **No runtime dependencies** — it wraps Rhino/GH APIs available only at runtime.

## 5. Success criteria

- Loads and runs under IronPython 2.7 in Rhino.
- A stable public API the plugin repos can rely on (`IGH`, input helpers, validators).
- Eventually, a `tests/` suite (CI already looks for one — see `planning/`).

## 6. Direction

- Adding a test suite and firming up the public API are the main open items — `planning/STATUS.md`.
