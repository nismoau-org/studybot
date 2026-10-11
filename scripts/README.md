# Scripts

Deterministic helpers. None implemented yet (Roadmap Phase 2).

Planned:

| Script | Purpose |
|---|---|
| `extract_tables.py` | PDF tables → CSV for key §§ (resources, CAPEX, economics) |
| `validate_summary.py` | Check a rendered summary against `../docs/data-schema.md` + NI 43-101 checklist |

Conventions (see `AGENTS.md`): Python, `argparse`, `--help` works,
no network by default, deterministic stdout.
