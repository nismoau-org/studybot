# PDF House Style — NI 43-101 Livery (v1)

> How a generated study must look. Measured from 4 training artifacts (Oct 2026):
> Marathon FS 2025 (Ausenco), Kami PFS 2024 (BBA), LDI FS 2018 (NAP), Otelnuk FS 2015.
> `scripts/generate_study_pdf.py` implements this spec — read both together.

## 1. Page

- US Letter (8.5×11"), portrait, ~25 mm margins. Body single column.
- Running header: issuer (left) + report short title (right), 9 pt sans, grey rule below.
- Running footer: report date (left) + section–page number (right, e.g. `1-30`),
  9 pt sans. Cover and TOC pages carry no header/footer.

## 2. Type

- Sans-serif throughout (Calibri/Century Gothic/Bahnschrift in the wild;
  generator uses Helvetica family): body 10–11 pt, table text 8–9 pt,
  captions 9 pt, footnotes/sources 8 pt italic.
- Headings: **bold, navy**, numbered NI-style — `1 SUMMARY`, `1.1 Headline`,
  `21 CAPITAL COSTS`. Section openers start on a new page.

## 3. Cover

- Full-width primary brand band carrying: report title (20–26 pt bold),
  project + location, study level, effective date vs report date (both — they
  routinely differ by months), issuer address, lead-firm address, QP list with firms.
- One accent element only (rule, block, or logo placeholder). No photography.

## 4. Front matter order

Cover → notices/QP-responsibility → Table of Contents (dot leaders, section–page
numbers: `1.16.12 … 1-45`) → List of Tables → List of Figures → Glossary (optional).
Bookmark/outline tree mirrors §§1–27 for PDF navigation.

## 5. Tables

- Caption **above**: `Table 21-1: Initial Capital Cost Breakdown (US$M)`.
- Header row: near-black/navy fill, white bold text. Body: alternating white /
  light-grey rows, hairline grey grid, right-aligned numerics, units in header
  or caption — never bare `$`.
- Source line **below**, 8 pt italic: `Source: COST-01 p.4.` Every table has one.

## 6. Figures

- Caption **below**: `Figure 22-1: Post-Tax NPV Sensitivity (Tornado)`.
- Source line under caption where data is external. Charts use the house palette
  (navy/teal/grey); no 3-D effects. Drawn vector where possible (tornado, cashflow).

## 7. Numbers discipline (visual)

- Money: amount + currency + basis together (`US$480M, Q1-2026`), pre/post-tax
  never share a column without labels. Rounding footnote where tables may not sum.
- Draft marking: `DRAFT — for QP review` on cover header and footer of every page
  until signed; unsigned QP certificates marked TO BE SIGNED.

## Palette (hex)

| Swatch | Value | Use |
|---|---|---|
| Primary navy | `#1D2D4F` | Cover band, headings, table headers |
| Accent teal | `#006B7F` | Charts, links, rules |
| Body text | `#1A1A1A` | Paragraphs |
| Zebra grey | `#F2F2F2` | Alternating table rows |
| Grid grey | `#BFBFBF` | Table gridlines |

## Related

- Generator: `../scripts/generate_study_pdf.py` (`../scripts/README.md`)
- Deliverable outline: `feasibility-study.md` · Target anatomy: `../docs/report-anatomy.md`
