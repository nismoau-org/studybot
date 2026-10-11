# Roadmap — Build Phases

## Phase 0 — Scaffold ✅ (this change)

- [x] Root `SKILL.md` + `README.md` + `AGENTS.md`
- [x] `docs/` hierarchy (this file + INDEX, overview, taxonomy, workflow, schema, evaluation)
- [x] `references/` + `templates/` + `scripts/` + `training/` skeletons
- [x] Remove redundant nested `skill/` dir (repo root **is** the skill)

## Phase 1 — Generator pivot (in progress)

> Pivot (Oct 2026): skill generates studies from input corpora; training studies are
> structural models, not summarization fixtures.

- [ ] Fill `references/ni-43-101-checklist.md` against actual NI 43-101 Form F1 items
- [ ] Fill `references/study-sections-canonical.md` (§1–§27 expectations)
- [x] `docs/report-anatomy.md` — target structure + style rules grounded in 4 past studies
  (Otelnuk FS 2015, LDI FS 2018, Marathon FS 2025, Kami PFS 2024)
- [x] `docs/corpus-intake.md` — manifest, citation, conflict, quarantine rules
- [x] `templates/feasibility-study.md` — deliverable outline (§1–27 + mine-plan extract)
- [x] `docs/taxonomy-study-types.md` — input maturity gates per level
- [ ] First eval cases under `training/evals/` (`manifest-build`, `level-gate`, `gap-detect`)
- [ ] Worked section example (e.g. §21 from sample cost inputs — synthetic, not fixture data)

## Phase 2 — Deterministic helpers

- [ ] `scripts/build_manifest.py` (doc pile → manifest csv)
- [ ] `scripts/validate_study.py` (draft vs `data-schema.md` + checklist gate)
- [ ] Document both in `scripts/README.md`

## Phase 3 — Templates v1 + economics guide

- [ ] Harden `feasibility-study.md` §21–22 guidance (capex build-up, price-deck handling)
- [ ] FX/price-deck normalization guide (multi-basis inputs)

## Phase 4 — Hardening

- [ ] JORC mapping note, FX/price-deck normalization guide
- [ ] CI: markdown link check + schema-field coverage check

Record template/schema changes here or in the commit message per `AGENTS.md`.
