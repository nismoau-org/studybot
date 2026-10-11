# input/ — Put the mine-site documents here

This folder is the skill's **inbox**. Drop every technical document the study must be
built from: drilling reports, QAQC memos, metallurgical testwork, geotech/hydro
studies, cost estimates and vendor quotes, environmental baselines, permits,
market/contract inputs, tenure records — PDFs, spreadsheets, drawings, anything.

## How it works

1. **Drop files in** — any filenames; the agent renames nothing.
2. **Agent builds a manifest** — each file gets a stable Doc ID (`GEO-01`, `MET-02`,
   …) recording type, date, author/QP status, and which study sections it feeds.
   Rules: `docs/corpus-intake.md`.
3. **Study composes from the manifest** — every claim cites `[Doc ID] + page`.
   Files here are the *only* allowed source of site facts.

## What stays out of version control

Everything you drop in here is **git-ignored** (only this README is committed).
Live engagement documents — especially non-public or client-confidential material —
must never be pushed to GitHub. Commit rights-cleared reference studies to
`training/output/` instead (see its README).

## Subfolders (optional, recommended for big piles)

`geology/  metallurgy/  mining/  costs/  environment/  markets/  property/`

The manifest records the path either way; sort only if it helps you.
