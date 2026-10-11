# Workflow — 6-Step Pipeline

1. **Intake + manifest**
   - Register every input per `corpus-intake.md` (ID, type, date, QP/status, §§ covered).
     Conventional source: the repo's `../input/` folder (git-ignored); in web chat,
     attached files play the same role.
   - Quarantine unreadable or restricted material; report it as a gap, not content.
2. **Assess maturity → gate level**
   - Map the corpus against `taxonomy-study-types.md` input gates; declare the PEA/PFS/FS
     target with evidence. If inputs can't support the requested level, say so and offer
     the lower level plus a work program.
3. **Compose section by section**
   - Draft §§1–27 per `../templates/feasibility-study.md`, shaping each to
     `report-anatomy.md`. Every claim cites Doc ID + page; conflicts surface both sides.
4. **Normalize**
   - Canonical units (t, Mt, g/t, %, US$/t, US$M); one FX/price-deck/discount basis
     (flag where inputs used different bases); pre-tax and post-tax kept separate.
5. **Validate**
   - Run `../references/ni-43-101-checklist.md` as a gate: each item ends composed /
     gap-flagged / N/A-with-reason. Cross-check arithmetic (tonnes × grade ≈ metal;
     capex build-ups sum; NPV inputs consistent).
6. **Deliver + advance**
   - Emit: (a) draft study, (b) schema tables, (c) gap list + §26-style work program
     with budget to reach the next level.

## Stop conditions

- Cannot determine an achievable level → stop and ask, don't default to FS.
- No QP-amenable basis for resources/reserves → cap at screening level, flag blocking gap.
- Economics basis (discount, prices, FX, tax) not establishable from corpus → present
  physicals/costs only, mark economics incomplete.
- Never fill a gap with training-artifact data or general knowledge stated as site fact.
