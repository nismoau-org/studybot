# StudyBot — Mining Feasibility Study AI Skill

> Turn dense mining technical reports (PEA / PFS / FS) into structured, comparable, decision-ready summaries.

StudyBot is an **AI Skill** (Claude-compatible) for parsing, structuring, and evaluating
mining feasibility studies prepared under **NI 43-101** and **JORC** reporting standards.

## What it does

1. **Ingests** a technical report (PDF) — PEA, PFS, or Feasibility Study.
2. **Extracts** techno-economic data into a canonical schema (geology, mining, metallurgy,
   CAPEX/OPEX, economics, ESG, risks).
3. **Validates** completeness against a NI 43-101 / JORC checklist.
4. **Emits** a standardized summary using a versioned template.

## Repo map

| Path | Purpose | Audience |
|---|---|---|
| `SKILL.md` | Skill entrypoint — routing + operating rules | AI agents |
| `AGENTS.md` | How to contribute / build in this repo | AI agents + humans |
| `docs/INDEX.md` | Hierarchical index of all agent docs | AI agents |
| `docs/` | Design docs: overview, taxonomy, workflow, schema, evals, roadmap | Both |
| `references/` | Ground-truth domain knowledge (checklists, glossaries) | AI at runtime |
| `templates/` | Output templates (PEA / PFS / FS / comparison) | AI at runtime |
| `scripts/` | Deterministic helpers (extract, validate, compare) | AI at runtime |
| `training/` | `input/` raw reports, `output/` gold summaries, `evals/` test cases | Builders |
| `assets/` | Diagrams, logos, static files | Humans |

## Quickstart (humans)

```bash
git clone <this-repo>
ls docs/INDEX.md        # start here for the full map
cat SKILL.md            # see what the agent sees
ls training/output/     # example source report(s)
```

## Quickstart (agents)

1. Read `SKILL.md`.
2. Read `docs/INDEX.md` and follow links **only as needed** (progressive disclosure).
3. Read `AGENTS.md` before writing code or docs.

## Status

🚧 **Scaffold phase** — directory layout + doc skeleton only. No extraction logic yet.
See `docs/roadmap.md` for build phases.

## Standards

- Skill format: [Anthropic Agent Skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) (`SKILL.md` + `references/` + `scripts/` + `assets/`).
- Reporting standards covered: NI 43-101 (Canada), JORC Code (Australia).
- Study levels: PEA / Scoping → PFS / Pre-Feasibility → FS / Feasibility (see `docs/taxonomy-study-types.md`).
