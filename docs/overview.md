# Overview

## What this skill is

An AI Skill that turns a **corpus of mine-site technical documents** — geology and
drilling reports, metallurgical testwork, geotech/hydro studies, cost estimates,
environmental and market inputs — into a **single draft feasibility study**
(PEA, PFS, or FS) or a **mine-plan extract**, structured to NI 43-101 §1–§27.

The `training/output/` studies are examples of this done manually in the past.
The skill learns **structure, depth, and style** from them and applies that knowledge
to new input corpora. It never reuses their numbers.

## Who it serves

- Mine development teams assembling a study from consultant work packages.
- Owners checking what their existing inputs can (and can't) support.
- Any agent asked to "draft / advance / gap-check" a mining study from site documents.

## What it is not

- Not a QP sign-off — output is a **draft for QP review**, never a filed report.
- Not a resource estimator or mine planner from scratch — it synthesizes inputs,
  it doesn't replace engineering judgment or testwork.
- Not a price forecaster — economics use input-supplied or user-approved decks only.
- Not legal/regulatory advice on filing requirements.

## Design principles

1. **Corpus first** — manifest every input before composing (`corpus-intake.md`).
2. **Level-gated** — input maturity sets PEA/PFS/FS; the skill refuses what inputs
   can't support (`taxonomy-study-types.md`).
3. **Provenance on every claim** — input Doc ID + page/section, or a flagged gap.
4. **Gaps are output** — missing sections drive the §26 work program, never hidden.
5. **No contamination** — training artifacts teach shape, never supply facts.
6. **Progressive disclosure** — the agent loads one doc at a time via `INDEX.md`.

## End-to-end in one paragraph

Manifest the input corpus → assess maturity and gate the study level → compose
§§1–27 against the deliverable template with per-claim citations → normalize units
and bases → validate each section against the NI 43-101 checklist → deliver the
draft study plus gap list and budgeted work program. Full steps: `workflow.md`.
