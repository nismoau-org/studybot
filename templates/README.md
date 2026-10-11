# Templates — Output Contracts

> Compose **from the input corpus only** (`../docs/corpus-intake.md` citation rules apply).
> No new numbers in prose that aren't in the schema tables. Training artifacts teach
> shape, never supply facts. The deliverable is always a **PDF** built by
> `../scripts/generate_study_pdf.py` per `pdf-style.md` — never a chat-only answer.

| Template | Use when… |
|---|---|
| `feasibility-study.md` | **Primary deliverable** — drafting the full study (§§1–27) or a mine-plan extract (§§15–16 + schedule) |
| `pdf-style.md` | Visual spec the PDF must meet (cover, headers/footers, tables, figures, palette) |
| `pea-summary.md` | Shaping the §1 Executive Summary of a PEA-level draft |
| `pfs-summary.md` | Shaping the §1 Executive Summary of a PFS-level draft |
| `fs-summary.md` | Shaping the §1 Executive Summary of an FS-level draft |
| `comparison-table.md` | Comparing ≥ 2 completed studies or scenarios |

Rule: schema change → template change (see `AGENTS.md`). PFS/FS summary templates are
currently thin stubs inheriting the PEA shape plus reserve/execution sections —
to be hardened in Roadmap Phase 3.
