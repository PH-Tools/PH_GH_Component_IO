---
DATE: 2026-07-15
STATUS: CANONICAL ENGINEERING STANDARD
---

# PH-GH-Component-IO — Coding Standards

## 1. IronPython 2.7 compatibility (mandatory)

This library loads in Rhino. It must run under IronPython 2.7.

- No f-strings — use `.format()`. No `pathlib`/modern-stdlib-only features.
- Comment-style type hints (`# type: (str) -> int`), not inline annotations.
- Guard `typing` imports (`try: from typing import ... except ImportError: pass`).
- Keep the `# -*- Python Version: 2.7 -*-` header on every module.
- Import Rhino/GH/`ladybug_rhino` APIs defensively — they only exist at runtime.

## 2. Public API stability

`IGH` (and its input/output wiring), the `input_tools` helpers, and the `validators` are imported by multiple plugin repos. Their signatures are a contract:

- Adding optional parameters/new helpers is fine.
- Changing or removing a signature is a **breaking change** — expect to update every consuming plugin. Don't do it casually.
- `output_tools.object_preview` is a legacy alias of `preview.object_preview` — keep both importable.

## 3. The validator pattern

Validators subclass `Validated` (a descriptor) and are used as class attributes to validate/clean a component input on assignment. New validators follow that descriptor pattern.

## 4. No runtime dependencies

`dependencies = []` is intentional. Do not add a pip runtime dependency — this wraps runtime-only Rhino/GH APIs.

## 5. Formatting

- **Black**, line length 120.

## 6. Testing

- CI runs `python -m pytest tests/` but **no `tests/` exists yet**. Adding one is an open improvement (`planning/`). If you add tests, they must exercise the IPy2.7-safe code paths under CPython (mocking the Rhino/GH API via the stubs).

## Closeout checklist

- [ ] IPy2.7-safe (no f-strings/pathlib; guarded `typing`; comment hints; 2.7 header; defensive Rhino imports).
- [ ] No breaking change to `IGH` / input helpers / validators without updating consumers (or flagging it).
- [ ] No new runtime dependency.
- [ ] black clean.
