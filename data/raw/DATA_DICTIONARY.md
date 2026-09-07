# Data Dictionary 

Documents the three raw datasets produced by `scripts/ingest.py` in `data/raw/`.

They are conceptually joined on **Region** during downstream cleaning and analysis. Grain differs
per dataset, so joins may require aggregating to a common regional key first.

## Data Sources Used

## 1. `fies_income_raw.csv`

**Source:** PSA OpenStat PXWeb API (FIES 2023) — Table 1, Number of Families, Average Annual Family Income and Expenditure by Region, Province, and HUC.

**Role:** Fallback source for Income.

**Grain:** One row per Region / Province / Highly Urbanized City (HUC). Provinces and HUCs are nested under their parent region row.

**Rows:** 138 · **Columns:** 4

| Column | Type | Description |
|---|---|---|
| `Region, Province, and HUC` | string | Name of the geographic area. Top-level region rows are in ALL CAPS (e.g. `NATIONAL CAPITAL REGION`); province/HUC rows nested underneath are title case (e.g. `City of Manila`). First row is `Philippines` (national total). |
| `Number of Families (In thousands)` | float | Estimated number of families, in thousands. |
| `Average Income (In thousands)` | float | Average annual family income, in thousand PHP. |
| `Average Expenditure (In thousands)` | float | Average annual family expenditure, in thousand PHP. |

---

## 2. `aspbi_ict_raw.csv`

**Source:** PSA OpenStat PXWeb API (ASPBI 2022) — Summary Statistics for Information and Communication Establishments by Geolocation, Industry Description, Year and Data Items.

**Role:** Fallback source for ICT Performance / ICT Sector Productivity.

**Grain:** One row per Region × Industry Description (Information and Communication sector total, plus its PSIC sub-industry breakdown).

**Rows:** 252 · **Columns:** 14

| Column | Type | Description |
|---|---|---|
| `Geolocation` | string | Region name, prefixed with `..` for regional rows (e.g. `..National Capital Region`); `PHILIPPINES` for the national total. |
| `Industry Description` | string | Industry group under Information and Communication (e.g. `Information and Communication` = sector total, or a sub-industry like `..Software publishing`). Dot-prefixes indicate nesting depth. |
| `2022 Number of Establishments` | numeric (string) | Count of ICT establishments — used for the "Number of ICT Establishments" KPI. |
| `2022 Total Employment` | numeric (string) | Total persons employed — denominator for the "ICT Revenue per Employee" KPI. |
| `2022 Paid Employees` | numeric (string) | Subset of employment that is paid staff. |
| `2022 Workers on Sub-Contract Agreement or Under Manpower Agencies/Contractors` | numeric (string) | Contracted/agency workers, not on payroll. |
| `2022 Total Revenue` | numeric (string) | Total revenue, in PHP thousands — numerator for the "ICT Revenue per Employee" KPI. |
| `2022 Total Expense` | numeric (string) | Total business expense. |
| `2022 Compensation` | numeric (string) | Total employee compensation paid. |
| `2022 Other Expense` | numeric (string) | Non-compensation expense. |
| `2022 Gross Additions to Tangible Fixed Assets` | numeric (string) | Capital expenditure on fixed assets. |
| `2022 Change in Inventories` | numeric (string) | Inventory value change. |
| `2022 Sales from E-Commerce Transactions` | numeric (string) | Revenue attributable to e-commerce. |
| `2022 Subsidies` | numeric (string) | Government subsidies received. |

---

## 3. `internet_usage_raw.xlsx`

**Source:** Department of Information and Communications Technology (DICT) — National ICT Household Survey (NICTHS) 2019 and 2024.

**Role:** **Primary source** for Internet Usage / Digital Adoption.

**Access Method:** Excel workbook obtained from the published NICTHS source through its available Excel file/export.

**Structure:** Multi-sheet workbook — **not** one flat table. The workbook contains an index/list sheet and multiple NICTHS survey tables covering household- and individual-level indicators.

### Primary Tables Used

| Table | Topic | Purpose |
|---|---|---|
| 17 | Internet Access | Primary basis for the Internet Usage Rate KPI |
| 19 | Monthly Spending | Internet spending indicator |
| 20 | Individuals Using Internet | Internet adoption indicator |
| 22 | Frequency | Internet usage frequency |
| 24–25 | Barriers | Barriers to internet access/connection |

### Workbook Structure

| Sheet name | Table # | Description |
|---|---:|---|
| `LIST` | — | Index mapping table numbers to sheet names. |
| `Estimated Totals` | 1–2 | Estimated households / individuals aged 10+ by region. |
| `i_C17-18` | 17 | Households with internet access by region, 2019 vs. 2024. **Primary source for the "Internet Usage Rate" KPI.** |
| `i_C17&20` | 19–20 | Household monthly spending on internet and individuals using the internet, by region. |
| `i_C21&25` | 22 | Individuals using the internet by frequency, by region. |
| `i_C21&27` / `i_C21E23&35` etc. | 24–25 | Barriers to internet access/connection (2024 only), by region. |
| *(remaining sheets)* | 3–16, 26–44 | Other NICTHS topics not directly used by this project's KPIs. |

---

## Cross-Dataset Reconciliation Note

| Dataset | Source Role | Region Count | Negros Handling |
|---|---|---:|---|
| `fies_income_raw.csv` | Income — Fallback | 18 | Negros Island Region reported separately |
| `aspbi_ict_raw.csv` | ICT Performance — Fallback | 17 | Negros Occidental/Oriental folded into Region VI/VII |
| `internet_usage_raw.xlsx` | Internet Usage — **Primary** | 17 | Negros Occidental/Oriental folded into Region VI/VII |

Because the datasets use different regional structures, regional keys must
be standardized during downstream cleaning before joining the datasets.
