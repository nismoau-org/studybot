---
name: mining-feasibility-study
description: Parse, structure, and summarize mining PEA/PFS/Feasibility technical reports (NI 43-101, JORC) into standardized techno-economic summaries with completeness validation. Use when the user provides a mining technical report, asks for a PEA/PFS/FS summary, comparison, or investment screening.
---

# Mining Feasibility Study Skill

## Purpose

Convert a mining technical report (PEA, PFS, FS) into a structured summary conforming to
`docs/data-schema.md`, validated against `references/ni-43-101-checklist.md`, rendered with
a template from `templates/`.

## Routing — read only what you need

1. **Always:** `docs/INDEX.md` (master map, 1 page).
2. **Classify study level first:** `docs/taxonomy-study-types.md`.
3. **Then, as needed:**
   - Workflow → `docs/workflow.md`
   - Extraction fields → `docs/data-schema.md`
   - Output shape → `templates/README.md` + the matching template
   - Domain terms → `references/glossary.md`
   - Section expectations → `references/study-sections-canonical.md`
   - Completeness check → `references/ni-43-101-checklist.md`
   - Report anatomy (where facts live) → `docs/report-anatomy.md`
4. **Never** load all of `references/` or `training/` into context by default.
   Load single files on demand.

## Operating rules

1. **Identify level** (PEA vs PFS vs FS) before extracting. State it and its
   confidence implications (see `docs/taxonomy-study-types.md`).
2. **Extract → schema first.** Populate every field in `docs/data-schema.md`;
   use `null` + `source_section` note when missing. Never silently invent numbers.
3. **Every number needs provenance:** value + unit + source page/section.
4. **Validate:** run the `references/ni-43-101-checklist.md` check; report gaps explicitly.
5. **Render last:** use the matching template in `templates/` — do not free-form the output.
6. **Economics discipline:** always report basis (discount rate, metal prices, FX, date),
   pre-tax vs post-tax NPV/IRR, payback, and sensitivities if disclosed.
7. **Escalate, don't guess:** flag Inferred-resource reliance in PEA economics,
   missing QP statements, or stale price decks.

## Inputs / outputs

- **Input:** PDF (or text) of a technical report + declared study level if known.
- **Output:** (a) structured data per schema, (b) rendered markdown summary per template,
  (c) gap list per checklist. See `docs/workflow.md` for the 6-step pipeline.

## Scripts

See `scripts/README.md`. Prefer deterministic scripts over LLM arithmetic when available.
Currently no scripts are implemented — do extraction manually per schema.

## Gold example

- Sources: `training/output/Marathon-FS-20250328.pdf` (FS) · `training/output/Kami-PFS-20240314.pdf` (PFS) — see `training/README.md` for all four fixtures
- Expected output shape: `templates/fs-summary.md` / `templates/pfs-summary.md`
- (Gold summaries + eval cases to be added under `training/` — see `docs/evaluation.md`.)
