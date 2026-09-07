# The Philippine Digital Economy by Region

## Problem Statement

I want to answer: "Which Philippine regions should be prioritized for digital economy investment based on their ICT sector performance, internet usage, and household income levels?"

The digital economy has become an important driver of economic growth, employment, and innovation in the Philippines. However, Philippine regions differ in terms of ICT sector performance, internet usage, and household income, resulting in varying levels of digital development and readiness. With limited resources for digital infrastructure and investment, it is important to identify regions where interventions can have the greatest impact. By comparing these key indicators across regions, this project aims to identify areas that may require greater support and provide insights to help government policymakers and regional development planners prioritize digital economy investments.

## Audience

This project is for government policymakers and regional development planners who need to identify regions that are leading or lagging in digital development in order to prioritize investment and development programs.

## Key Performance Indicators (KPIs)

The main metrics I want to track are:

Primary KPI
* ICT Revenue per Employee (Total ICT Revenue ÷ Total ICT Employment), measuring ICT business productivity per region

Supporting KPIs
* Number of ICT Establishments — indicates the size and concentration of the ICT industry in each region.
* Internet Usage Rate — measures the level of digital adoption among the population.
* Average Annual Family Income — represents the economic capacity of households in each region.

## Analytical Approach

This project will compare ICT business productivity, internet usage, and household income across Philippine regions to identify strengths, development gaps, and potential investment opportunities. Rather than evaluating regions using only one indicator, the analysis will examine how these dimensions interact to provide a more comprehensive view of regional digital development.

Specifically, the analysis will identify:

* Regions with high household income but relatively low ICT business productivity or internet usage, which may indicate untapped digital investment potential.
* Regions with high internet usage but relatively low ICT business productivity, which may suggest strong digital adoption but limited ICT industry development.
* Regions with strong ICT business productivity despite lower household income, which may represent emerging digital growth hubs worthy of further study.

## Likely Data Sources

I will explore:
* Philippine Statistics Authority (PSA) Annual Survey of Philippine Business and Industry (ASPBI) 2022 – Information and Communication Sector
* Philippine Statistics Authority (PSA) Family Income and Expenditure Survey (FIES) 2023
* https://openstat.psa.gov.ph/

* DICT - National ICT Household Survey 2019 and 2024 
* https://ictstatistics.dict.gov.ph/nicths2024/

These are the most recent publicly available datasets. Because they were collected across different years (2022, 2023, and 2024), comparisons between the datasets may be affected by the year gap.

## Data Source Notes

### Income (Household Economic Capacity)

#### Primary Source
- Name: Table 1 — Average Annual Family Income, by Per Capita Income Decile Class and by Region, Province and HUCs: 2018, 2021, and 2023p (Family Income and Expenditure Survey)
- URL: https://psa.gov.ph/statistics/income-expenditure/fies/stat-tables
- Format: xlsx
- Coverage: 2018, 2021, 2023p; **18 regions** (includes Negros Island Region as a separate region), with province and HUC-level rows nested under each region
- Why it fits the problem: Provides the direct data for the "Average Annual Family Income" supporting KPI, and the per capita income decile breakdown allows the analysis to go beyond a flat regional average to show how spread out income is within each region.
- Known limitations: Region XII and BARMM are not directly comparable across years because 63 barangays from North Cotabato were transferred to BARMM in 2023; this dataset reports 18 regions (Negros Island Region separated out), while ASPBI 2022 and NICTHS 2019/2024 both still report 17 regions with Negros folded into Region VI and VII — regional totals must be reconciled before merging across datasets; roughly a 1-2 year gap versus the 2022 ASPBI and 2024 NICTHS data.

#### Supporting Tables
- **Name: Table 1a — Coefficient of Variation (CV) of the Average Annual Family Income, by Per Capita Income Decile Class and by Region, Province and HUC: 2018, 2021, and 2023p**
  - URL: https://psa.gov.ph/statistics/income-expenditure/fies/stat-tables
  - Format: xlsx
  - Coverage: 2018, 2021, 2023p; same 18 regions as Table 1
  - Why it fits the problem: Reports the CV for each estimate in Table 1, used to flag which regional or provincial income figures have high variability (less reliable) before they're used in the KPI comparison.
  - Known limitations: Not usable on its own — it's a reliability indicator, not an income value, so it only adds value when merged with Table 1 by region. Same 18-region structure and mismatch issue as Table 1.
  
- **Name: Table 5 — Gini Coefficient and Palma Ratio, by Region, Province and HUC: 2018, 2021, and 2023p**
  - URL: https://psa.gov.ph/statistics/income-expenditure/fies/stat-tables
  - Format: xlsx
  - Coverage: 2018, 2021, 2023p; same 18 regions as Table 1
  - Why it fits the problem: Adds an inequality lens to the income capacity dimension, showing whether a region's high average income is broad-based or concentrated among a few, which strengthens the gap analysis.
  - Known limitations: Reported at region/province/HUC level only, with no decile breakdown, so it can only be joined to Table 1 at the region level, not cross-tabbed by decile. Same 18-region structure and mismatch issue as Table 1.


#### Fallback Source
- Name: Table 1 — Number of Families, Average Annual Family Income and Expenditure, by Region, Province, and HUC: 2023 (PSA OpenStat)
- URL: https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__1E__IE/0011E3ANIE0.px/
- Format: xlsx/csv export from interactive web table
- Coverage: 2023; same 18-region structure as Table 1
- Why it could still work: Same FIES 2023 survey, but combines Number of Families, Average Income, and Average Expenditure into a single table with a direct 2023 figure, rather than needing three separate files as with the primary source.
- Known limitations: No decile breakdown and no inequality measures (Gini/Palma), so the inequality dimension of the income analysis would be lost if this replaces the primary source. Carries the same 18-region mismatch against ASPBI and NICTHS as the primary source.

---

### ICT Performance (ICT Sector Productivity)

#### Primary Source
- Name: Table 1 — Summary Statistics for Information and Communication Establishments by Region and Industry Group: Philippines, 2022 (Annual Survey of Philippine Business and Industry, ASPBI)
- URL: https://psa.gov.ph/content/2022-annual-survey-philippine-business-and-industry-aspbi-information-and-communication-0
- Format: xlsx
- Coverage: 2022 only; **17 regions** (Negros Occidental and Negros Oriental are still counted within Region VI - Western Visayas and Region VII - Central Visayas, no separate Negros Island Region row), with industry group (PSIC code) breakdown nested under each region
- Why it fits the problem: Contains Number of Establishments, Total Employment, and Total Revenue in a single table, which are the exact raw inputs needed to compute both the primary KPI (ICT Revenue per Employee) and the supporting KPI (Number of ICT Establishments) without needing to merge in another table.
- Known limitations: Single year only (2022), so no year-over-year trend for the ICT sector dimension; covers only formal, registered establishments that met the ASPBI survey threshold, likely excluding informal or freelance digital economy activity; **uses the 17-region structure (pre-Negros Island Region), which does not match the 18-region structure used in the 2023 FIES income data** — Negros-related figures will need to be reconciled before cross-dataset comparison; roughly a 1-2 year gap versus the 2023 FIES and 2024 NICTHS data.

#### Fallback Source
- Name: Summary Statistics for Information and Communication Establishments by Geolocation, Industry Description, Year and Data Items (PSA OpenStat)
- URL: https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__2D__2022/0042D4BAJ00.px/
- Format: csv/xlsx export from interactive web table
- Coverage: 2022; **17 regions plus national total** (Negros Occidental and Negros Oriental still folded into Region VI and VII, no separate Negros Island Region row, same structure as the ASPBI primary source), with industry breakdown down to 14 sub-sectors under "Information and Communication"
- Why it could still work: Contains the same core variables as the ASPBI primary source — Number of Establishments, Total Employment, Paid Employees, and Total Revenue, so it can still compute both the primary KPI (ICT Revenue per Employee) and the supporting KPI (Number of ICT Establishments) without needing to merge in another table. 
- Known limitations: Same year (2022) and same 17-region structure as the ASPBI primary source, so it doesn't add a second year of coverage and **still requires the same Negros Island Region reconciliation against the 18-region FIES income data**. Revenue and employment figures may differ slightly from the ASPBI primary source's exact published table cuts since this is drawn from PSA's general OpenStat database rather than the ASPBI-specific publication page, so a cross-check between the two is advisable before final use.

---

### Internet Usage (Digital Adoption)

#### Primary Source
- Name: National ICT Household Survey (NICTHS) 2019 and 2024 — Tables 17 (Internet Access), 19 (Monthly Spending), 20 (Individuals Using Internet), 22 (Frequency), 24-25 (Barriers)
- URL: https://ictstatistics.dict.gov.ph/nicths2024/
- Format: xlsx
- Coverage: 2019 and 2024; **17 regions** (Negros Occidental and Negros Oriental still counted within Region VI and Region VII, no separate Negros Island Region row)
- Why it fits the problem: Provides the direct data for the "Internet Usage Rate" supporting KPI at both household and individual level, and the frequency and barrier tables add depth beyond a binary access rate, useful for explaining why a digital investment gap exists.
- Known limitations: Only two survey rounds (2019, 2024), so no continuous annual data and no interpolation for in-between years; the barrier tables (24-25) are 2024 only, with no 2019 comparison; **uses the same 17-region structure as ASPBI 2022, but does not match the 18-region structure used in the 2023 FIES income data** — Negros-related figures will need to be reconciled before cross-dataset comparison; roughly a 1-2 year gap versus the 2023 FIES and 2022 ASPBI data.

#### Fallback Source
- Name: Digital Connectivity - Mobile Network Access (Number and Percentage of Individuals Aged 10 Years and Over with Devices that is Working, has an Active SIM, and is Used for Communication by Type of Network Signal and Region, Philippines: 2024)
- URL: https://openstat.psa.gov.ph/Database/Environment-and-multi-domain-Statistics/Digital-Connectivity
- Format: csv
- Coverage: 2024; 17 regions (matches the same regional structure as NICTHS, no separate Negros Island Region row), broken down by type of network signal (2G/3G/4G/5G)
- Why it could still work: Measures individuals with a working, actively-used mobile device connected to a network, which functions as a proxy for digital access; also gives a network-quality angle (2G through 5G breakdown) that NICTHS doesn't have.
- Known limitations: Measures mobile network device usage, not internet usage directly, so it's a proxy rather than a replacement for the "Internet Usage Rate" KPI; only one year of data (2024), so it can't replace NICTHS's 2019-vs-2024 comparison; still needs the same 17-vs-18 region reconciliation against the FIES income data.

Most fallback sources listed above are from PSA OpenStat, as they contain the same or closely matching data as the primary sources and are the most reliable alternative if the primary source is unavailable. For primary sources without a listed fallback, no alternative was included because the original source was considered stable and accessible.

## Ingestion Method

The FIES income data and ASPBI ICT performance data are ingested through their respective PSA OpenStat PXWeb APIs, enabling automated retrieval of the raw datasets. The internet usage data (NICTHS) is ingested through the Google Sheets XLSX export endpoint, allowing the published spreadsheet to be downloaded programmatically as an Excel file. All source data are stored in their original raw format prior to any cleaning or transformation. No web scraping or manual file download is required for the current ingestion process.

## Possible Final Dashboard

The dashboard will enable decision-makers to compare ICT business productivity, digital adoption, and household income across Philippine regions. Comparisons are descriptive — the dashboard flags regions where the three indicators don't align in the expected direction (e.g. high income but low ICT productivity, high internet usage but low ICT productivity, high ICT productivity despite lower income), highlighting regional strengths and gaps worth further investigation as a first step in digital economy investment prioritization. This depends on first reconciling the region-count mismatch between data sources (FIES reports 18 regions with Negros Island Region separated out, while ASPBI and NICTHS report 17 with Negros folded into Region VI and VII), detailed in the Data Source Notes.
