# Overview

## What this skill is

An AI Skill that converts mining **Preliminary Economic Assessments (PEA)**,
**Pre-Feasibility Studies (PFS)**, and **Feasibility Studies (FS)** into
standardized, comparable summaries grounded in the source report.

## Who it serves

- Analysts screening projects (grade, scale, cost, NPV/IRR, risks).
- Engineers checking study completeness against NI 43-101 / JORC expectations.
- Any agent asked to "summarize / compare / screen" a mining technical report.

## What it is not

- Not a resource estimator, mine planner, or QP sign-off.
- Not a price forecaster — it reports the study's price deck, it doesn't invent one.
- Not legal/regulatory advice on filing requirements.

## Design principles

1. **Schema first, prose last** — see `data-schema.md` before `templates/`.
2. **Provenance on every number** — value + unit + page/section.
3. **Level-aware** — PEA numbers are conceptual; FS numbers are bankable.
   See `taxonomy-study-types.md`.
4. **Gaps are output** — missing sections are reported via
   `../references/ni-43-101-checklist.md`, never hidden.
5. **Progressive disclosure** — the agent loads one doc at a time via `INDEX.md`.

## End-to-end in one paragraph

Classify the study level → extract all `data-schema.md` fields with provenance →
validate against the NI 43-101 checklist → render with the matching template →
attach gaps + sensitivities. Full steps: `workflow.md`.
