# Evaluation — How Skill Quality Is Tested

## Principle

Every skill change must be checkable against an **input corpus → generated section**
pair. `training/output/` studies are structural references for judging shape and depth —
their numbers are never expected content.

## Layout

- `../input/` — the inbox for live engagement docs (git-ignored; confidential
  material stays uncommitted). Eval cases carry their own `corpus/` or `corpus.manifest`.
- `training/output/` — past manually-built studies as target-shape models
  (see `training/README.md` anti-contamination rule).
- `training/evals/` — one folder per case: task + corpus pointer + expected checks.

## Eval case format (`training/evals/<case>/`)

- `prompt.md` — the user request (e.g. "Draft §22 economics from COST-01..03 at PFS level").
- `corpus/` or `corpus.manifest` — the input docs (or a manifest pointing at them).
- `checks.md` — bullet assertions: level gated correctly, ≥ N schema fields populated
  with Doc-ID provenance, economics basis stated, gaps listed, zero figures traceable
  to training artifacts. Prefer checkable facts over style opinions.

## Seed cases (pea-demo ✅, rest to build)

0. `pea-demo` ✅ — synthetic corpus → full PEA PDF; checks style, gating, provenance, gaps.
1. `manifest-build` — messy doc pile → correct manifest with IDs, §§ coverage, quarantines.
2. `level-gate` — thin corpus (Inferred-only, bench met, factored costs) → PEA cap with evidence.
3. `section-compose` — cost inputs → §21 table with build-up, basis date, contingency treatment.
4. `gap-detect` — corpus missing tailings/closure inputs → §18/§20 gap-flagged + work-program item.

## Pass bar (v0.1, manual)

- Correct level gating 100% of seed cases.
- Zero invented numbers (spot-check 5 figures → all trace to a corpus Doc ID + page).
- Zero contamination (no figure traceable to a `training/output/` artifact).
- Every economics output states discount rate + price deck + tax basis or says "not establishable."

Automated scoring (scripts + CI) is a roadmap item — see `roadmap.md`.
