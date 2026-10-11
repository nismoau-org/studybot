# Scripts

Deterministic helpers. Conventions (see `AGENTS.md`): Python, `argparse`,
`--help` works, no network by default, deterministic stdout. Requires `fpdf2`
(`pip install fpdf2`).

| Script | Purpose | Status |
|---|---|---|
| `generate_study_pdf.py` | Content model (JSON) or `--demo` → NI 43-101-styled study **PDF** per `../templates/pdf-style.md` (cover, TOC+bookmarks, lists, dark-header/zebra tables, tornado figures, DRAFT marking) | ✅ Implemented |
| `build_manifest.py` | Doc pile → manifest csv per `../docs/corpus-intake.md` | Planned (Roadmap Phase 2) |
| `validate_study.py` | Check a draft against `../docs/data-schema.md` + checklist gate | Planned (Roadmap Phase 2) |

## generate_study_pdf.py

```bash
python3 scripts/generate_study_pdf.py --demo [--output Kestrel_Ridge-PEA-DRAFT.pdf]
python3 scripts/generate_study_pdf.py --content model.json [--output Study-draft.pdf]
```

The JSON model shape is documented in the script's `--help` / module docstring:
`title_block` (title, project, level, dates, basis, issuer, lead firm, QPs) plus
`sections` of `para` / `bullets` / `table` (caption, headers, rows, align, source) /
`figure_tornado` blocks. Content must already be composed per the skill workflow —
the script renders, it doesn't source facts.
