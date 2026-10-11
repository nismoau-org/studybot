# StudyBot — Mining Feasibility Study AI Skill

> Turn dense mining technical reports (PEA / PFS / FS) into structured, comparable, decision-ready summaries.

StudyBot is an **AI Skill** for parsing, structuring, and evaluating
mining feasibility studies prepared under **NI 43-101** and **JORC** reporting standards.
You install it into an AI assistant (ChatGPT shown below), hand it a technical
report PDF, and get back a standardized techno-economic summary with
completeness checks — instead of a free-form chat answer.

## What it does

1. **Ingests** a technical report (PDF) — PEA, PFS, or Feasibility Study.
2. **Extracts** techno-economic data into a canonical schema (geology, mining, metallurgy,
   CAPEX/OPEX, economics, ESG, risks).
3. **Validates** completeness against a NI 43-101 / JORC checklist.
4. **Emits** a standardized summary using a versioned template.

## Setup with ChatGPT (step by step)

### What you need

- A **ChatGPT account**. Note: OpenAI currently makes Skills available on eligible
  **Business, Enterprise, Healthcare, and Edu** workspaces (subject to admin settings).
  If you don't see the menu in step 4, check your plan or ask your workspace admin
  to enable skills and skill uploading.
- **This repo** downloaded to your computer (step 2).
- A **mining technical report PDF** you want analyzed (for step 5).

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

### Step 3 — Prepare the upload file

ChatGPT installs a skill from a single folder/zip, and this repo's root folder
**is** the skill (its `SKILL.md` is the entrypoint). Before zipping, leave out
two things ChatGPT doesn't need:

- The hidden `.git` folder (version-control plumbing).
- `training/output/` — ~157 MB of example reports used for skill development.
  The skill never loads these at run time.

```bash
# from inside the studybot folder:
zip -r studybot-skill.zip . -x ".git/*" "training/output/*"
```

No command line? Right-click the `studybot` folder → **Compress**, then delete
`training/output/*.pdf` from the copy first if you're tight on size.

### Step 4 — Install the skill in ChatGPT

1. In the ChatGPT sidebar, select **Plugins**.
2. Open the **Plugin Directory** and select the **Skills** tab.
3. Select **Create** → **Upload from your computer**.
4. Choose the `studybot-skill.zip` file from step 3.
5. ChatGPT scans the upload (this is automatic). Once it passes, **install** it.
   - If it shows *Needs Review*, check the details before proceeding.
   - If your workspace blocks uploads, your admin needs to allow skill uploading.

Reference: OpenAI's [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
help article and [Build skills](https://learn.chatgpt.com/docs/build-skills) guide.

### Step 5 — Analyze your first report

1. Start a new chat.
2. **Attach your report PDF** (paperclip / `+` button) and ask for what you want, e.g.:

   > Summarize this feasibility study using the StudyBot template: headline
   > economics with full basis, resources vs reserves, CAPEX/OPEX, and a
   > completeness gap list.

   More examples:

   > Is this report a PEA, PFS, or FS, and what does that imply for how I
   > should treat its numbers?

   > Compare these two attached studies side by side: scale, costs, NPV/IRR
   > on a stated basis, and top risks.

3. ChatGPT picks up the skill automatically when your request matches it
   (that's the skill's `description` doing its job). To force it, mention the
   skill explicitly with `@` and select it.
4. Check the answer the way you'd check an analyst: every number should cite a
   **page/section**, economics should state **discount rate, price deck, FX, and
   tax basis**, and gaps should be listed, not hidden. If any of that is missing,
   ask a follow-up — the skill's rules require it.

## Tips and limits

- **One report per chat** keeps answers clean; start a fresh chat per project.
- The skill **reports** the study's price deck — it doesn't forecast prices.
- It is **not** a Qualified Person sign-off, mine plan, or legal advice on filings.
- Large reports (400–900 pages) work fine as attachments; you don't need to
  pre-read or split them.
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
| `assets/` | Diagrams, logos, static files | Humans |

Want to contribute or extend the skill? Read `AGENTS.md` first.

## Status

🚧 **Build phase** — skill scaffolding, four training reports (Otelnuk FS 2015,
LDI FS 2018, Marathon FS 2025, Kami PFS 2024), and a report-anatomy guide are in.
Gold summaries and eval cases are next. See `docs/roadmap.md`.

## Standards

- Skill format: [Agent Skills open standard](https://learn.chatgpt.com/docs/build-skills)
  (`SKILL.md` + `references/` + `scripts/` + `assets/`) — works in ChatGPT, Codex,
  Claude, and other compatible assistants.
- Reporting standards covered: NI 43-101 (Canada), JORC Code (Australia).
- Study levels: PEA / Scoping → PFS / Pre-Feasibility → FS / Feasibility (see `docs/taxonomy-study-types.md`).
