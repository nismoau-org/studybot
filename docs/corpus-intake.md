# Corpus Intake — Organizing Dozens of Input Docs

> Answers: how does a pile of mine-site documents become a citable corpus?
> Build the manifest **before** composing a single study section.

## 1. Manifest (one row per input doc)

| Doc ID | Title / type | Date | Author / QP? | Covers (study §§) | Status |
|---|---|---|---|---|---|
| GEO-01 | Drilling report, Zone A | 2024-05-10 | … | §7–12 | final |
| MET-02 | Flotation pilot results | 2023-11-02 | … | §13 | draft |

Rules (conventional inbox: the repo's `../input/` folder — see its README;
the manifest records the path either way):

- Stable ID prefixes by discipline: `GEO-` geology/drilling/QAQC, `MET-` metallurgy,
  `MINE-` mining/geotech/hydro, `COST-` capex/opex/quotes, `ENV-` permits/ESG/water,
  `MKT-` markets/contracts, `PROP-` tenure/history/access.
- Record each doc's own effective/basis date — they feed different study bases.
- Superseded docs stay listed as `superseded` (audit trail) and are never sourced.

## 2. Citation convention

`[DocID p.N §x]` after every sourced claim — one claim, one citation minimum.
Every table carries a source line naming its Doc IDs.

## 3. Conflict rule

Two inputs disagree → state **both** with IDs/dates in the study text, recommend
a resolution path in §26. Never silently pick one.

## 4. Maturity signal per doc

Note what each doc can support: bench-scale met → PEA; pilot/operational → PFS/FS;
factored estimate → PEA; vendor quote → FS. The weakest link gates the study level
(see `taxonomy-study-types.md`).

## 5. Quarantine

Unreadable, un-cited, or confidential-restricted material goes on a quarantine list,
not into the study. Report it as a gap.

## Related

- Pipeline: `workflow.md` · Level gates: `taxonomy-study-types.md`
- Target shape: `report-anatomy.md` · Deliverable: `../templates/feasibility-study.md`
