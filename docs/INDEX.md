# Docs Index — Master Map

> Single router for agents. Start here, then open **only** the file(s) the task needs.

| # | File | Question it answers | Load when… |
|---|---|---|---|
| 0 | `overview.md` | What does this skill do, for whom, and what is out of scope? | Scoping any task |
| 1 | `taxonomy-study-types.md` | PEA vs PFS vs FS — accuracy, resource confidence, use limits? | Classifying a report (always) |
| 2 | `workflow.md` | What is the 6-step ingest → extract → validate → render pipeline? | Running the skill end-to-end |
| 3 | `data-schema.md` | Which fields must be extracted, with what units/provenance? | Extracting data |
| 4 | `evaluation.md` | How is skill quality tested (gold outputs, eval cases)? | Adding tests or judging output |
| 5 | `roadmap.md` | What is built vs planned, in what order? | Planning new work |

## Companion trees (load single files on demand)

- `../references/README.md` → `ni-43-101-checklist.md`, `study-sections-canonical.md`, `glossary.md`
- `../templates/README.md` → `pea-summary.md`, `pfs-summary.md`, `fs-summary.md`, `comparison-table.md`
- `../scripts/README.md` → helper scripts (none implemented yet)
- `../training/README.md` → source reports, gold outputs, eval cases
- `../assets/README.md` → static assets

## Rules

- Do not bulk-load a whole tree. Open the index row you need, then stop.
- If you add a doc, add a row here and link it from `../SKILL.md` routing if runtime-relevant.
