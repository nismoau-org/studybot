---
name: mining-feasibility-study
description: Generate a mining feasibility study (PEA/PFS/FS) or mine plan from a corpus of mine-site technical documents, using NI 43-101 structure and completeness rules. Use when the user provides multiple technical inputs (geology, drilling, metallurgy, costs...) and wants a synthesized study, or asks to draft, advance, or gap-check study sections.
---

# Mining Feasibility Study Skill

## Purpose

Synthesize dozens of mine-site technical inputs into a single feasibility study
(PEA, PFS, or FS) per `templates/feasibility-study.md`, structured to NI 43-101 §1–§27,
with every claim traced to an input document and gaps explicitly flagged.

`training/output/` holds past manually-built studies as **structural models only** —
never data sources. Their numbers must never appear in a generated study.

## Routing — read only what you need

1. **Always:** `docs/INDEX.md` (master map, 1 page).
2. **Gate the achievable level first:** `docs/taxonomy-study-types.md`.
3. **Then, as needed:**
   - Intake + manifest → `docs/corpus-intake.md`
   - Pipeline → `docs/workflow.md`
   - Output data model → `docs/data-schema.md`
   - Deliverable shape → `templates/README.md` + `templates/feasibility-study.md`
   - PDF house style → `templates/pdf-style.md` (render with `scripts/generate_study_pdf.py`)
   - Target anatomy → `docs/report-anatomy.md`
   - Domain terms → `references/glossary.md`
   - Section expectations → `references/study-sections-canonical.md`
   - Completeness gate → `references/ni-43-101-checklist.md`
4. **Never** load all of `references/` or `training/` into context by default.
   Load single files on demand.

## Operating rules

1. **Manifest first.** Index every input (ID, type, date, QP/status) per
   `docs/corpus-intake.md` before composing anything.
2. **Gate the level.** Input maturity decides PEA vs PFS vs FS. State it with evidence;
   refuse reserves or bankability the inputs can't support.
3. **Every claim needs provenance:** input Doc ID + page/section. Missing → gap, never invention.
4. **Compose → schema.** Each section populates `docs/data-schema.md` fields or records
   `null` + gap + work-program item.
5. **Validate as a gate:** each §1–§27 item ends composed / gap-flagged / N/A-with-reason
   per `references/ni-43-101-checklist.md`.
6. **Economics discipline:** basis on every number (discount, prices, FX, date),
   pre-tax vs post-tax separated, sensitivities from input ranges only.
7. **Draft, not signed:** output is for QP review; mark certificates TO BE SIGNED.
   Never present it as a filed report.
8. **PDF deliverable.** The study is always rendered as PDF per `templates/pdf-style.md`
   via `scripts/generate_study_pdf.py` — never a chat-only answer.

## Inputs / outputs

- **Input:** corpus of mine-site technical docs (conventionally the `input/` folder)
  + target level if known.
- **Output:** (a) draft study **as PDF** per `templates/feasibility-study.md` +
  `templates/pdf-style.md`, (b) schema tables, (c) gap list + work program to advance.
  See `docs/workflow.md`.

## Scripts

See `scripts/README.md`. PDF rendering is implemented (`generate_study_pdf.py` —
`--demo` or `--content` JSON). Compose content per schema; the script renders,
it doesn't source facts.

## Reference artifacts

- Past studies as structural models: `training/output/` (Otelnuk FS 2015, LDI FS 2018,
  Marathon FS 2025, Kami PFS 2024) — see `training/README.md` anti-contamination rule.
- Style demo (look at this first): `training/evals/pea-demo/` — synthetic PEA PDF +
  prompt + checks.
- Eval format (corpus → section checks): `docs/evaluation.md`.
