# S&P 500 Earnings Season Update

## Problem Statement
Assessing a company's financial health from its quarterly earnings reports is harder than it should be. Earnings data is spread across inconsistent formats, buried in dense filings, and hard to compare across companies or time periods. This makes it slow and error-prone for investors and analysts to answer a simple question: is this company's financial performance actually improving?

This challenge is especially relevant right now. Corporate earnings growth in 2026 has been unusually strong across most sectors, with several sectors posting double-digit revenue growth and analysts projecting continued strong growth into the second half of the year. Stock valuations have also climbed above their historical averages, making it even more important for investors to look past headline numbers and understand the underlying financial health driving these trends — rather than reacting to hype alone.

This project aims to build a small, reusable pipeline that acquires, cleans, and analyzes company earnings data, surfacing key financial health indicators (such as revenue growth, EPS trends, and margins) in a clear, comparable format — helping a stakeholder make faster, better-informed decisions.

## Stakeholder & User
The primary stakeholder is an individual investor who needs to decide whether to buy, hold, or sell a stock based on the company's financial health. This person is not a professional analyst — they have some investing knowledge but limited time to manually dig through dense earnings reports and financial filings.

The user relies on this analysis around earnings season, when companies release their quarterly results, since that's when new financial health signals become available. Outside of earnings season, they may also check back periodically to track how a company's financial health is trending over time.

The workflow context: the investor wants a quick, clear view of key financial health indicators (revenue growth, EPS trends, margins) rather than raw, unprocessed filings — enabling them to make a faster, more confident decision without needing deep financial expertise.

## Useful Answer & Decision
This project produces a descriptive answer — summarizing and clarifying a company's existing financial health based on its reported earnings data, rather than predicting future stock movements or establishing causal relationships.

Metric: Key financial health indicators, including revenue growth rate, EPS (earnings per share) trend, and profit margin, compared across recent quarters.

Artifact to deliver: A cleaned dataset and summary table/notebook showing these indicators for a chosen company (or set of companies), making it easy for the stakeholder to quickly assess financial health trends at a glance.

## Assumptions & Constraints
- Assumes publicly available earnings data (e.g., from sources like Yahoo Finance or company investor relations pages) is accurate and sufficiently up to date for analysis.
- Assumes the stakeholder is analyzing publicly traded companies that are required to report quarterly earnings (e.g., S&P 500 companies), not private companies.
- Limited to data that can be accessed for free or through the tools available in this course (no paid financial data subscriptions).
- Analysis is based on historical/reported data only — no real-time or intraday data processing.
- Time and scope are limited to what can reasonably be built within a single course project (a small number of companies/metrics, not a full-scale financial platform).
- Data storage and processing are done locally (on a personal laptop), not in a cloud/production environment.

## Known Unknowns / Risks
It's unclear how consistent earnings data formatting will be across different companies or data sources — this may require extra cleaning work not yet anticipated.
Some companies may have missing or delayed earnings data, which could create gaps in the analysis.
The chosen financial health metrics (revenue growth, EPS, margins) may not fully capture a company's true financial health — other factors (like debt levels or cash flow) could also matter but aren't covered in this initial scope.
Risk of data acquisition issues (e.g., API rate limits, source websites changing structure) disrupting the pipeline.
Will test the pipeline using a small set of known companies first, comparing outputs against publicly reported figures to confirm accuracy before scaling to more companies.
Will monitor for unexpected null/missing values or outliers during the data cleaning stage, and document any manual adjustments made.

## Lifecycle Mapping
Goal → Stage → Deliverable

- Define the problem and stakeholder → Problem Framing & Scoping (Stage 01) → This README
- Set up tools and project structure → Tooling Setup (Stage 02) → Repo and folder structure
- Build reusable code → Python Fundamentals (Stage 03) → src/utils.py
- Collect earnings data → Data Acquisition (Stage 04) → Raw data files
- Store data properly → Data Storage (Stage 05) → Processed data files
- Clean the data → Data Preprocessing (Stage 06) → Cleaned dataset


## Repo Plan
~~~
bootcamp_matthew_raymond/
│
├── class_materials/          ← handouts; gitignored, never pushed
│   ├── stage00_preclass-setup/
│   ├── stage01_problem-framing-and-scoping/
│   ├── stage02_tooling-setup/
│   └── ...                   one folder per stage
│
├── homework/                 ← each folder holds ONLY what that week uses
│   ├── homework00/           setup only — no data folders
│   ├── homework01/           problem framing — no data folders
│   ├── homework02/           full structure, built once as practice
│   ├── homework03/
│   │   ├── data/raw/
│   │   ├── data/processed/
│   │   └── src/
│   └── ...                   continues through the course
│
├── project/                  ← built once in Stage 02, filled in every stage after
│   ├── data/
│   │   ├── raw/              unmodified, as acquired
│   │   └── processed/        cleaned, reproducible
│   ├── notebooks/
│   ├── src/
│   ├── reports/
│   │   └── images/
│   ├── model/
│   ├── docs/
│   └── README.md
│
├── .gitignore
└── README.md
~~~


