# Roadmap — Build Phases

## Phase 0 — Scaffold ✅ (this change)

- [x] Root `SKILL.md` + `README.md` + `AGENTS.md`
- [x] `docs/` hierarchy (this file + INDEX, overview, taxonomy, workflow, schema, evaluation)
- [x] `references/` + `templates/` + `scripts/` + `training/` skeletons
- [x] Remove redundant nested `skill/` dir (repo root **is** the skill)

## Phase 1 — Ground truth (next)

- [ ] Fill `references/ni-43-101-checklist.md` against actual NI 43-101 Form F1 items
- [ ] Fill `references/study-sections-canonical.md` (§1–§27 expectations)
- [ ] Write gold summary for `training/output/Lac_des_Iles-PEA-12222021.pdf`
- [ ] Add first eval case under `training/evals/pea-smoke/`

## Phase 2 — Deterministic helpers

- [ ] `scripts/extract_tables.py` (pdf → csv of key tables)
- [ ] `scripts/validate_summary.py` (summary vs `data-schema.md` completeness)
- [ ] Document both in `scripts/README.md`

## Phase 3 — Templates v1 + second commodity

- [ ] Harden `pfs-summary.md` / `fs-summary.md` / `comparison-table.md`
- [ ] Add a second training report (different commodity / PFS or FS level)

## Phase 4 — Hardening

- [ ] JORC mapping note, FX/price-deck normalization guide
- [ ] CI: markdown link check + schema-field coverage check

Record template/schema changes here or in the commit message per `AGENTS.md`.
