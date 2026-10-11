# Workflow — 6-Step Pipeline

1. **Acquire + identify**
   - Confirm file, report date, issuer, QPs, regime (NI 43-101 / JORC).
   - Classify PEA / PFS / FS per `taxonomy-study-types.md`. State level + evidence (title page, §1).
2. **Extract to schema**
   - Populate every field in `data-schema.md` with value + unit + source page/section.
   - Missing → `null` + `gap:` note. Never carry a number without provenance.
3. **Normalize**
   - Convert to canonical units (t, Mt, g/t, %, US$/t, US$M), state FX + price deck + date basis.
   - Keep pre-tax and post-tax economics separate; record discount rate.
4. **Validate**
   - Run `../references/ni-43-101-checklist.md` item by item → pass / partial / missing.
   - Cross-check: tonnes × grade ≈ contained metal; CAPEX + contingency ≈ total; NPV inputs consistent.
5. **Render**
   - Pick template from `../templates/README.md` matching the study level.
   - Fill template from schema only — no new numbers in prose.
6. **Review + file**
   - Emit: (a) schema table, (b) rendered summary, (c) gap list + sensitivities.
   - For comparisons, add one `comparison-table.md` row per project; same price basis or flag the mismatch.

## Stop conditions

- Cannot determine study level → stop and ask, don't default to FS.
- No QP statement / no resource classification → flag as blocking gap, continue as "screening only."
- Economics without stated discount rate, prices, or tax basis → report as incomplete, don't back-solve silently.
