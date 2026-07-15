# context/ — canonical repo documentation

Stable, ground-truth documentation for PH-GH-Component-IO. Distinct from `planning/` (in-flight work). This repo has no `docs/` folder.

`CLAUDE.md` at the repo root is the dispatcher; this folder holds the docs it routes to.

## Index

| Doc | Read when you need… |
|-----|---------------------|
| [`PRD.md`](PRD.md) | What this library is for and what belongs here |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | What each module does and how `IGH` is used |
| [`TECH_STACK.md`](TECH_STACK.md) | Packaging, distribution, CI, versioning |
| [`CODING_STANDARDS.md`](CODING_STANDARDS.md) | IPy2.7 rules, the validator pattern, API stability, testing |

## Maintenance rule

When the public API (`IGH`, input helpers, validators) changes, update the relevant doc here and treat it as a breaking change for downstream plugins.
