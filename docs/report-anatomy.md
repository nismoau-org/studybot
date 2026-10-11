# Report Anatomy — What Real NI 43-101 Studies Look Like

> Grounded in 4 training fixtures (Oct 2026): Otelnuk FS 2015 (~485 pp),
> LDI FS 2018 (~889 pp), Marathon FS 2025 (~480 pp), Kami PFS 2024 (~558 pp).
> Answers: **where does each schema field live, and what does "good" look like?**
> Extract per `data-schema.md`, render per `templates/`, validate per
> `../references/ni-43-101-checklist.md` — this file is the locator, not a second schema.

## 1. Universal skeleton (all four follow it)

NI 43-101 Items §1–§27 **in order, no gaps**. §1 Summary is a mini-report
(~30–40 pp in FS) mirroring §§4–26 with subsections §1.1–§1.24. Front matter:
title page → QP responsibility matrix (§2) → TOC with dotted leaders →
List of Tables / List of Figures → Glossary/Abbreviations. Back matter:
QP certificates + signatures (§28–29) → Appendices (claims, variograms,
geomech, level plans, salvage).

Captions are per-section `Table/Figure X-Y: Title` throughout; modern reports
add `Source: Firm (year)` under figures (Marathon 2025).

## 2. Identity block — capture all four dates

| Item | Where | Example spread |
|---|---|---|
| Title + level + location | Cover p.1 | "Feasibility Study Report Update, Marathon, Ontario" |
| Issuer / operator | Cover + §2.1 | Generation Mining; LDIM/NAP; Champion Iron; LOM |
| Lead firm + collaborators | Cover + §2 | Ausenco+JDS+MMTS+KP+P&E; BBA+GMS+Soutex+AtkinsRéalis+WSP+SYSTRA |
| Effective date vs report/issue/signature date | Cover (they differ by months) | Marathon eff. 2024-11-01 / rep. 2025-03-28; Kami eff. 2023-12-22 / signed 2024-03-14; LDI eff. 2018-07-04 / rep. 2018-10-02; Otelnuk eff. 2015-03-25 / issue 2015-04-23 |
| QPs + section responsibility + site visits | §2 table + back certs | 8–10 QPs each; visits dated (e.g. 2020/2022/2024) |

Rule: record **both** dates; economics are anchored to the effective date,
costs to the basis date (§21).

## 3. Field locator (schema → where to look)

| Schema group | Primary home | What "good" cites |
|---|---|---|
| Resources (M/I/Inf) | §14 + §1.7–1.9 | Tonnes, grade(s), contained metal, **cutoff + basis** (NSR $/t or %/g/t), method (ID3/kriging), pit-constraint, date. E.g. Otelnuk 18% DTWR; Marathon C$13–16/t NSR; Kami 15% TFe |
| Reserves (P&P) | §15 + §1.10 | Only PFS/FS. **Reserve-shell price deck** (often conservative vs econ deck) + FX + SMU/dilution/modifying factors. E.g. Kami Platts 62% US$80/dmt+$20 adj., FX 1.30 |
| Mining | §16 + §1.11 | Method, pits/phases, bench height, strip ratio, total mined vs processed, throughput (tpd + Mtpa), life, pre-strip, geotech/hydro basis |
| Processing | §13+§17 + §1.12 | Staged flowsheet, recovery **per metal**, concentrate spec, testwork scale ladder: bench → pilot → bulk (Otelnuk 80 t) → operational (LDI mill) |
| Infra | §18 + §1.13 | Power/water/tailings/access; modern: CDA-2021/LRIA downstream design, discharge point, closure cost stated |
| Costs | §21 + §1.12–1.13 | CAPEX split direct/indirect/contingency/owners + sustaining **separate**; **basis date + currency** (Q4-2023 CAD, Q4-2024 C$, Dec-2014 USD); accuracy class (AACE 3/4); contingency method (Kami: Monte Carlo). OPEX per tonne milled by area (mine/proc/G&A/logistics/TCRC) + per payable unit + AISC with by-product treatment explicit |
| Economics | §22 + §1.14 (self-contained) | Currency, real vs nominal, discount rate (Marathon 6%; Kami/LDI/Otelnuk 8% + variants), **price deck table per commodity + source** (consensus/SNL/Platts 3-yr), FX, tax regime (e.g. 15% mining duty + 30% fed/prov ≈ 37%), pre/post-tax NPV/IRR/payback **separate**, cashflow period, closure/salvage/royalty/stream treatment (Marathon Wheaton −$236M), sensitivity tornado/spider (±20–30%; grade/FX/price dominate), scenarios (100% equity vs levered; base vs market) |
| ESG/permits | §20 + §1.15 | EA approval date (Marathon: 30-Nov-2022 Joint Panel CEAA 2012), Indigenous groups consulted + named agreements (Biigtigong 2022), EIA/closure status |
| Conclusions/Recs | §25–26 + §1.16 | Go/no-go + phased work program + budget (Kami Ph1 C$36.2M / Ph2 C$15.8M); PFS lists open items for FS (geotech, scale-up, firm rail/port pricing) |

## 4. Style rules for our output

1. **Units:** metric; g/t for PGE/Au, % for Cu/Ni/Fe, $/dmt for iron ore, troy oz contained/payable; Mt/Mwmt/Mdmt distinguished; dual C$/US$ columns where the report gives them.
2. **Basis on every money number:** amount + currency + date basis + pre/post-tax + discount anchor. Never carry a bare "$".
3. **Reserve vs resource:** state inclusive vs exclusive (LDI 2018 reports resources *inclusive* of reserves — flag it); PFS/FS economics use reserves only, Inferred excluded and flagged uncertain.
4. **Rounding notes:** reports round (§22 "totals may not sum") — repeat the caveat, don't force balance.
5. **Provenance format:** `value unit (§section, p. N)`.

## 5. Level signals (PFS vs FS depth)

- FS: firm quotes + % quoted, execution plan + schedule (§24 Implementation in Marathon/Kami), financing lens, "supports production decision."
- PFS: narrowed options with rejected alternatives, AACE Class 3 (plant) / Class 4 (TMF), open-items register, "viability subject to FS confirmation."
- PEA (absent from fixtures — wanted list in `../training/README.md`): expect factored costs, Inferred in economics with disclosure, no reserves, "not a production decision."

## 6. Red flags to call out

Missing QP matrix, effective/report date mismatch unexplained, single-date price (vs deck table),
economics without FX/tax/discount, AISC without by-product treatment, Inferred silently in cashflow,
reserve shell deck undisclosed, closure cost absent or excluded without statement.

## Related

- Fields: `data-schema.md` · Pipeline: `workflow.md` · Level: `taxonomy-study-types.md`
- Validate: `../references/ni-43-101-checklist.md` · Render: `../templates/README.md`
- Fixtures: `../training/README.md`
