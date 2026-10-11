# Training

> ⛔ **Anti-contamination rule:** `output/` holds past manually-built studies as
> **structural models** — the skill learns target shape, depth, and style from them.
> Their numbers must **never** appear in a generated study. Any figure in a draft must
> trace to an input-corpus Doc ID, never to these files.

## input/ — moved to repo root

Live engagement docs now go in the top-level `../input/` folder (git-ignored inbox —
see its README). This `training/input/` directory is retained only for eval-case
corpora (see `../docs/evaluation.md`).

## output/ — reference artifacts (finished studies, manually built in the past)

| File | Project / level | Source | Size | Model notes |
|---|---|---|---|---|
| `ceaa_020-12-1222-0009-RF-Rev2_-_Sommaire_anglais.pdf` | CEAA summary (English) — provenance TBD | pre-existing in repo | 14 MB | n/a — not a study model |
| `Lac_Otelnuk-FS-20150325.pdf` | Lac Otelnuk iron ore **FS** (NI 43-101, effective 2015-03-25, Met-Chem) | `https://minedocs.com/19/Lac-Otelnuk-FS-03252015.pdf` | 66,159,438 bytes, verified PDF, ~485 pp | FS §§1–27 depth; bulk-sample met program; phased capex |
| `Lac_des_Iles-FS-20181002.pdf` | Lac des Iles palladium **FS** (NI 43-101, Nordmin, report 2018-10-02) | `https://s21.q4cdn.com/326998455/files/doc_downloads/2018/10/NAP-43-101-Technical-Report-October-2-2018.pdf` | 43,139,415 bytes, verified PDF, ~889 pp | UG-heavy FS; inclusive resource reporting; AISC build-up |
| `Marathon-FS-20250328.pdf` | Marathon Cu-Pd **FS update** (NI 43-101, Ausenco, effective 2024-11-01, report 2025-03-28) | `https://genmining.com/site/assets/files/3815/2025_feasibility_study_report_update.pdf` | 24,103,980 bytes, verified PDF, ~480 pp | Modern FS; stream/royalty treatment; Indigenous agreements |
| `Kami-PFS-20240314.pdf` | Kamistiatusset (Kami) iron ore **PFS** (NI 43-101, BBA, effective 2023-12-22, report 2024-03-14) | `https://www.championiron.com/wp-content/uploads/2024/03/2024-03-14-champion-iron-pre-feasibility-study-for-the-kamistiatusset-kami-iron-ore-property.pdf` | 14,491,553 bytes, verified PDF, ~558 pp | PFS depth marker; Monte Carlo contingency; dual price cases |

## Wanted as PEA-level structural model (blocked — need original URLs)

| Report | Why blocked |
|---|---|
| Lac des Iles palladium **2015 PEA** (Hatch, amended 2015-04-20) | `napalladium.com` / `nap.com` dead (Cloudflare 523/challenge); SEDAR-only otherwise. Old Q4 CDN filenames 404. |
| Kipawa **PEA 2012** (~29 MB, `Rep_Matamec-Fin-PEA-000-20120314-SEDAR-Com.pdf`) | `matamec.com` Cloudflare-blocked (403). |
| Kipawa **FS 2013** (~78–80 MB, `matamecfs2013sedar.pdf` + appendices) | Same as above; `qpmcorp.ca` down; Fury site links to no PDF. |

## evals/ — test cases (empty; format in `../docs/evaluation.md`)

Planned: `manifest-build/`, `level-gate/`, `section-compose/`, `gap-detect/`.

## Conventions

- Filename: `<Project>-<LEVEL>-<YYYYMMDD>.pdf` (LEVEL = PEA/PFS/FS).
- Record source URL + effective date in the table above for every file.
- Keep each PDF < 100 MB (GitHub file limit; no LFS configured).
