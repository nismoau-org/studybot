# StudyBot — Mining Feasibility Study AI Skill

> Turn a pile of mine-site technical documents into a structured draft feasibility study.

StudyBot is an **AI Skill** that ingests dozens of technical documents from a mine site
(geology and drilling reports, metallurgical testwork, geotech/hydro studies, cost
estimates, environmental and market inputs) and synthesizes them into a **single draft
feasibility study** (PEA, PFS, or FS) or **mine plan**, structured to **NI 43-101** /
**JORC** expectations. The example studies in `training/output/` show this done manually
in the past — the skill learns their structure and applies it to your documents.
You install it into an AI assistant (ChatGPT shown below), supply your site documents,
and get back a draft study with completeness gaps and a work program — instead of a
free-form chat answer.

## What it does

1. **Ingests** dozens of site documents and indexes them into a citable manifest.
2. **Gates the level** — your inputs' maturity decides what can be claimed
   (PEA vs PFS vs FS); it refuses reserves or bankability the inputs can't support.
3. **Composes** the study section by section (§§1–27), every claim traced to your documents.
4. **Validates** completeness against a NI 43-101 / JORC checklist; gaps become a
   budgeted work program to reach the next level.

The deliverable is always a **PDF study document** in NI 43-101 livery (cover, TOC,
tables, figures) built with `scripts/generate_study_pdf.py` — never a chat-only answer.

## Setup with ChatGPT (step by step)

### What you need

- A **ChatGPT account**. Note: OpenAI currently makes Skills available on eligible
  **Business, Enterprise, Healthcare, and Edu** workspaces (subject to admin settings).
  If you don't see the menu in step 5, check your plan or ask your workspace admin
  to enable skills and skill uploading.
- **This repo** downloaded to your computer (step 2).
- A **mining technical report PDF** you want analyzed (for step 6).

### Step 1 — Get ChatGPT

1. Go to [chatgpt.com](https://chatgpt.com) and sign in (or create an account).
2. Optionally install the desktop or mobile app for easier file handling —
   the skill works the same on web, desktop, and mobile.

### Step 2 — Download this repo

Pick whichever feels easier:

**Option A — Git clone (if you use git):**

```bash
git clone https://github.com/nismoau-org/studybot.git
cd studybot
```

**Option B — ZIP download (no git needed):**

1. Go to [github.com/nismoau-org/studybot](https://github.com/nismoau-org/studybot).
2. Click the green **Code** button → **Download ZIP**.
3. Unzip it. You'll get a folder called `studybot` containing `SKILL.md` plus
   `docs/`, `references/`, `templates/`, and other folders.

### Step 3 — Put your documents in `input/`

All site documents go in **one place**: the **`input/`** folder at the top of this repo.

- **Working locally or with Codex/CLI:** copy your files into `input/` — drilling
  reports, testwork, cost estimates, permits, spreadsheets, drawings, any filenames.
  Optional subfolders (`geology/`, `metallurgy/`, `costs/` …) help on big piles.
  Details: `input/README.md`.
- **Working in ChatGPT web/app:** you can instead just **attach files to the chat** —
  they play the same role.
- **Private by default:** everything you put in `input/` is git-ignored and stays off
  GitHub (only `input/README.md` is tracked). Leave `input/` contents out of the
  skill upload zip in the next step, too.

### Step 4 — Prepare the upload file

ChatGPT installs a skill from a single folder/zip, and this repo's root folder
**is** the skill (its `SKILL.md` is the entrypoint). Before zipping, leave out
two things ChatGPT doesn't need:

- The hidden `.git` folder (version-control plumbing).
- `training/output/` — ~157 MB of example reports used for skill development.
  The skill never loads these at run time.

```bash
# from inside the studybot folder:
zip -r studybot-skill.zip . -x ".git/*" "training/output/*" "input/*"
```

No command line? Right-click the `studybot` folder → **Compress**, then delete
`training/output/*.pdf` from the copy first if you're tight on size.

### Step 5 — Install the skill in ChatGPT

1. In the ChatGPT sidebar, select **Plugins**.
2. Open the **Plugin Directory** and select the **Skills** tab.
3. Select **Create** → **Upload from your computer**.
4. Choose the `studybot-skill.zip` file from step 4.
5. ChatGPT scans the upload (this is automatic). Once it passes, **install** it.
   - If it shows *Needs Review*, check the details before proceeding.
   - If your workspace blocks uploads, your admin needs to allow skill uploading.

Reference: OpenAI's [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
help article and [Build skills](https://learn.chatgpt.com/docs/build-skills) guide.

### Step 6 — Build your first study

1. Start a new chat.
2. **Supply your site documents** — from your `input/` folder (step 3) or attached
   to the chat — and ask for what you want, e.g.:

   > Here are our drilling, metallurgy, and cost files for Project X. Build a
   > manifest of these inputs, tell me the highest study level they support,
   > and draft the study with full provenance and a gap list.

   More examples:

   > Given these inputs, can we claim PFS, or are we capped at PEA? Show your
   > reasoning per gate.

   > Draft §21–22 (costs and economics) from the attached cost files at PFS level.

   > Draft a standalone mine plan (§§15–16 + production schedule) from these inputs.

3. ChatGPT picks up the skill automatically when your request matches it
   (that's the skill's `description` doing its job). To force it, mention the
   skill explicitly with `@` and select it.
4. Check the answer the way you'd check a consultant's draft: every number should cite
   an **input document + page**, the study level should be **gated with evidence**,
   economics should state **discount rate, price deck, FX, and tax basis**, and gaps
   should come with a **work program**, not silence. If any of that is missing,
   ask a follow-up — the skill's rules require it.

## Tips and limits

- **One project per chat** keeps answers clean; work section by section for big builds.
- The skill's output is a **draft for QP review** — never a signed or filed report.
- The skill **reports** price decks from your inputs — it doesn't forecast prices,
  and it never borrows numbers from its example studies.
- Large document sets are fine as attachments; you don't need to pre-read them.
  If two inputs conflict, the draft should surface both, not pick silently.
- **Deliverable is a PDF** — ask for the file itself, not just chat text.
- To share with colleagues, use your workspace's skill-sharing options
  (*Shared with me / Shared by workspace*) rather than re-uploading.

## Repo map (for the curious)

| Path | Purpose | Audience |
|---|---|---|
| `SKILL.md` | Skill entrypoint — routing + operating rules | AI agents |
| `AGENTS.md` | How to contribute / build in this repo | AI agents + humans |
| `docs/INDEX.md` | Hierarchical index of all agent docs | AI agents |
| `docs/` | Design docs: overview, taxonomy, workflow, schema, report anatomy, roadmap | Both |
| `references/` | Ground-truth domain knowledge (checklists, glossaries) | AI at runtime |
| `templates/` | Output templates (PEA / PFS / FS / comparison) | AI at runtime |
| `scripts/` | Deterministic helpers (extract, validate, compare) | AI at runtime |
| `training/` | `output/` example reports, `evals/` test cases | Builders |
| `input/` | **Your inbox** — drop site documents here (git-ignored, never committed) | Humans |
| `assets/` | Diagrams, logos, static files | Humans |

Want to contribute or extend the skill? Read `AGENTS.md` first.

## Status

🚧 **Build phase** — generator pivot in progress: input-manifest rules, level gates,
deliverable template (`templates/feasibility-study.md`), and four past studies as
structural models (Otelnuk FS 2015, LDI FS 2018, Marathon FS 2025, Kami PFS 2024)
are in. Worked examples and eval cases are next. See `docs/roadmap.md`.

## Standards

- Skill format: [Agent Skills open standard](https://learn.chatgpt.com/docs/build-skills)
  (`SKILL.md` + `references/` + `scripts/` + `assets/`) — works in ChatGPT, Codex,
  Claude, and other compatible assistants.
- Reporting standards covered: NI 43-101 (Canada), JORC Code (Australia).
- Study levels: PEA / Scoping → PFS / Pre-Feasibility → FS / Feasibility (see `docs/taxonomy-study-types.md`).
