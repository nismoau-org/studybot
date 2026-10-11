# AGENTS.md — Working in This Repo

Instructions for any AI agent (or human) modifying this repo.

## 1. Entry order

1. `SKILL.md` — runtime contract. Do not break its routing promises.
2. `docs/INDEX.md` — authoritative file map. Update it when you add/move any `.md`.
3. This file (`AGENTS.md`) — repo conventions below.

## 2. Conventions

- **Progressive disclosure:** keep `SKILL.md` under ~80 lines. Push detail into
  `docs/`, `references/`, `templates/`. Never inline a whole reference file.
- **One concept per file:** each file in `docs/` answers one question.
  Cross-link with relative paths, don't duplicate content.
- **Frontmatter:** only `SKILL.md` carries skill frontmatter (`name`, `description`).
  Do not add frontmatter to other files unless tooling requires it.
- **Templates are contracts:** changing a template field requires a matching change in
  `docs/data-schema.md` + a note in `docs/roadmap.md` or a commit message.
- **References are ground truth:** only add claims traceable to NI 43-101, JORC,
  CIM definitions, or a cited technical report. No invented thresholds.
- **Scripts:** Python preferred, `argparse` CLI, no network calls by default,
  deterministic output. Document each script in `scripts/README.md`.
- **Training data:** never commit non-public reports without rights.
  Record source + date + QP in `training/README.md` for every file.
- **No contamination:** `training/output/` artifacts are structural models of finished
  studies. Never source their numbers into a generated study; live engagement docs stay
  out of version control unless rights-cleared.

## 3. Allowed / disallowed

- ✅ Add docs under `docs/`, refs under `references/`, templates under `templates/`.
- ✅ Add `scripts/*.py` with a `--help` entrypoint and a README section.
- ✅ Add eval cases under `training/evals/` per `docs/evaluation.md`.
- ❌ Do not nest a second skill (no `skill/` subdirectory with its own `SKILL.md`).
  This repo **is** the skill; root `SKILL.md` is canonical.
  (A legacy empty `skill/` dir was removed for this reason.)
- ❌ Do not commit large binaries except curated PDFs in `training/`; keep each < 50 MB.
- ❌ Do not edit `training/output/*.pdf` in place — add new files, update the README table.

## 4. Definition of done (per change)

- [ ] `docs/INDEX.md` still lists every `.md` file accurately.
- [ ] Links resolve (relative paths, correct case).
- [ ] `SKILL.md` routing section mentions any new load-on-demand file.
- [ ] Markdown renders on GitHub (headings, tables, code fences).

## 5. Commit guidance

- Small, scoped commits: `docs: …`, `templates: …`, `references: …`, `scripts: …`, `training: …`.
- State which checklist/schema version the change targets.
