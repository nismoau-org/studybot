# Evaluation — How Skill Quality Is Tested

## Principle

Every skill change must be checkable against a **source report → gold summary** pair.

## Layout

- `training/input/` — raw source PDFs (immutable, rights-cleared). Currently empty.
- `training/output/` — source reports used as fixtures (e.g. `Lac_des_Iles-PEA-12222021.pdf`).
  Gold markdown summaries sit **beside** the PDF with the same stem once written.
- `training/evals/` — one folder per case: ` lead question + expected checks`.

## Eval case format (`training/evals/<case>/`)

- `prompt.md` — the user request (e.g. "Summarize this PEA per pea-summary template").
- `checks.md` — bullet assertions: study level correct, ≥ N schema fields with provenance,
  economics basis stated, gaps listed. Prefer checkable facts over style opinions.
- `source.link` — relative pointer to the `training/` source file (don't duplicate PDFs).

## Seed cases (to build)

1. `pea-smoke` — Lac des Iles PEA → fills `pea-summary.md`, flags Inferred reliance.
2. `level-classify` — given title + §1 only, returns PEA/PFS/FS correctly.
3. `gap-detect` — report missing tailings/closure detail → checklist marks it missing.
4. `compare-two` — two summaries → one `comparison-table.md` row each, same-basis or flagged.

## Pass bar (v0.1, manual)

- Correct study level 100% of seed cases.
- Zero invented numbers (spot-check 5 figures → all trace to a page/section).
- Every economics output states discount rate + price deck + tax basis or says "not disclosed."

Automated scoring (scripts + CI) is a roadmap item — see `roadmap.md`.
