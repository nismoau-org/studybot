# Data Schema — Canonical Extraction Fields (v0.1)

> Every field needs `value + unit + source (page/§)`. Missing → `null` + reason.
> Units default below; record conversions. Keep pre-tax / post-tax strictly separate.

## 1. Identity

| Field | Example |
|---|---|
| `project_name` | Lac des Iles |
| `location` (country, province/state) | Ontario, Canada |
| `commodities` | Pd, Pt, Au, Cu, Ni |
| `issuer / operator` | … |
| `report_date` | 2021-12-22 |
| `study_level` (PEA/PFS/FS + evidence) | PEA — title p.1 |
| `reporting_standard` (NI 43-101 / JORC) | NI 43-101 |
| `qualified_persons` | name, firm, § relied on |

## 2. Geology + resources

- `deposit_type`, `cutoff_grade` (+ basis: NSR / grade / price),
  `resources { measured, indicated, inferred }` → tonnes, grade(s), contained metal,
  `resource_date`, `estimation_method` (kriging/IDW/NN + SW used).

## 3. Reserves (PFS/FS only; PEA → expect `null`)

- `reserves { proven, probable }` → tonnes, grade, contained metal, modifying factors cited.

## 4. Mining

- `method` (open pit / UG / combo), `mine_life_years`, `total_mined_t`,
  `strip_ratio` (OP) or `dilution / recovery` (UG),
  `throughput_tpd`, `ramp_up`, `geotech/hydro_basis` (testwork level).

## 5. Processing / metallurgy

- `flowsheet` (crush/grind/flotation/leach…), `recovery_%` per metal,
  `concentrate_spec / payabilities`, `testwork_level` (bench / pilot / operational).

## 6. Infrastructure + environment + social

- `power / water / tailings / access`, `permits_status`,
  `closure_cost`, `ESG / Indigenous engagement` notes + section refs.

## 7. Capital + operating costs

- `capex_initial`, `capex_sustaining`, `capex_contingency_%`, `capex_basis_date`,
  `opex_mining / _processing / _ga` per tonne milled, `opex_total_LOM`,
  `closure_included? (y/n)`.

## 8. Economics

- `price_deck` per commodity (+ source, real/nominal), `fx`, `discount_rate_%`,
  `npv_pre_tax / npv_post_tax` (+ discount anchor), `irr_pre / irr_post`,
  `payback_years`, `annual_avg_production`, `cash_cost / aisc` (+ by-product treatment),
  `sensitivities` (price ±x%, grade, recovery, CAPEX/OPEX drivers).

## 9. Risks + opportunities + next steps

- Free-text bullets with section refs: permitting, geotech, metallurgical scale-up,
  price/FX exposure, stated recommendations / work program + budget.

## Change rule

Adding/removing a field here requires the same change in `../templates/`
(see `AGENTS.md`). Bump the `v0.x` above when you do.
