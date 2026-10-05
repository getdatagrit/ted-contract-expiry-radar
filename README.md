# TED Contract Expiry Radar - Recompete Leads

Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/ted-contract-expiry-radar) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/ted-contract-expiry-radar/)

**from $7.00 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

TED Contract Expiry Radar turns contract award notices from the official EU tender portal TED into a list of public contracts that are about to end across Europe. For every lot it returns the incumbent supplier, the buying authority and its country, the award value, the contract end date, the days left, contract length, renewal options and CPV codes. You choose the expiry window, for example the next 12 months, and optionally filter by keyword, buyer country, CPV code, supplier name and minimum value. Export the result as JSON, CSV or Excel, call it through the Apify API, or plug it into n8n, Make and AI agents through MCP.

## Quick start

1. Open [TED Contract Expiry Radar - Recompete Leads on Apify Store](https://apify.com/datagrit/ted-contract-expiry-radar) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "queries": [
    "software"
  ],
  "expiresAfterMonths": 0,
  "expiresBeforeMonths": 12,
  "maxItems": 20
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `queries` | array | Optional keywords. TED full-text search finds candidate notices, and a lot is returned only when a keyword appears in its own title or description, or in the contract or notice title (case-insensitive, in the language of the notice). Leave empty to list all expiring contracts. |
| `countries` | array | Optional. Two-letter country codes of the contracting authority, for example DE, FR, PL, NL, ES, IT. Leave empty for all countries covered by TED. |
| `cpvPrefixes` | array | Optional. Keep only contracts whose CPV classification starts with one of these digits, for example 72 (IT services), 90 (waste and cleaning) or 45 (construction). |
| `incumbents` | array | Optional. Keep only contracts won by suppliers whose name contains one of these words, for example to see when a competitor's contracts end. |
| `expiresAfterMonths` | integer | Start of the expiry window. 0 means contracts ending today or later. |
| `expiresBeforeMonths` | integer | End of the expiry window. 12 returns contracts ending within the next twelve months. Results are read in monthly slices, soonest expiry first. |
| `minValue` | number | Optional. Minimum awarded value in the contract's own currency (mostly EUR). Contracts without a published value are excluded when this is above 0. |
| `includeFrameworkAgreements` | boolean | Turn off to drop framework agreements and keep only stand-alone contracts. |
| `estimateMissingEndDates` | boolean | Most notices state a contract duration but no end date. When on, the end date is computed from start date (or award date) plus duration and marked in endDateSource. Turn off to return only end dates stated by the buyer. |
| `maxItems` | integer | Stop after this many contracts. |
| `proxyConfiguration` | object | Optional proxy. The TED API is public and needs no proxy; leave disabled. |

## Output

| Field | Type | Description |
|---|---|---|
| `query` | string | The keyword from your input found in this lot (lot title, lot description, contract title or notice title); null only when you gave no keywords. |
| `id` | string | Stable identifier: TED notice number plus the lot. One award notice can hold several lots, each returned as its own row. Empty only on the single status row emitted when nothing matched. |
| `noticeNumber` | string | Publication number of the contract award notice on TED. |
| `lotId` | string | Lot identifier inside the notice. |
| `title` | string | Title of the award notice as published on TED. |
| `contractTitle` | string | Title of the contract given by the buyer, when it differs from the notice title. Filled only when the notice has one contract title; empty when several contracts have different titles. |
| `lotTitle` | string | Title of this lot in the language of the notice. Matched to the lot by its identifier; empty when TED does not list one title per lot. |
| `lotDescription` | string | Description of this lot in the language of the notice, cut to 1000 characters. Matched to the lot by its identifier; empty when TED does not list one description per lot. |
| `sourceUrl` | string | Link to the award notice on TED. |
| `buyerName` | string | Contracting authority that awarded the contract, i.e. who will buy again. |
| `buyerCountry` | string | Three-letter ISO country code of the buyer. |
| `buyerCity` | string | City of the buyer. |
| `incumbentName` | string | Supplier that won this lot. Null when the notice does not allow a safe match of winner to lot; see allIncumbents. |
| `incumbentCountry` | string | Three-letter ISO country code of the incumbent supplier. |
| `incumbentSize` | string | Company size class of the incumbent as declared in the notice (micro, small, medium, large). |
| `incumbentId` | string | Company registration identifier of the incumbent as published in the notice. |
| `allIncumbents` | string | Names of all winning suppliers in the notice, separated by semicolons. Filled when winners cannot be matched to a single lot. |
| `awardValue` | number | Awarded value of the lot in the currency given in the currency field. |
| `currency` | string | Currency code of awardValue. |
| `awardDate` | string | Date the contract was concluded (YYYY-MM-DD). Filled only when the notice has one contract or all its contracts were concluded the same day; TED does not say which contract belongs to which lot, so otherwise empty. |
| `publishedAt` | string | Date the award notice was published (YYYY-MM-DD). |
| `contractStart` | string | Contract start date when stated in the notice (YYYY-MM-DD). |
| `contractEnd` | string | Contract end date (YYYY-MM-DD), stated by the buyer or computed; see endDateSource. |
| `endDateSource` | string | How contractEnd was obtained: stated (published by the buyer), start+duration or award+duration (estimated from the published duration). |
| `daysToExpiry` | integer | Days from the run date to contractEnd. |
| `monthsToExpiry` | number | Months from the run date to contractEnd, one decimal. |
| `contractLengthMonths` | number | Published contract duration in months. |
| `renewalOptionsMax` | integer | Maximum number of renewals the buyer reserved, when stated. |
| `renewalTerms` | string | Description of the renewal option, cut at 400 characters. |
| `frameworkAgreement` | boolean | True when the lot is a framework agreement rather than a stand-alone contract. |
| `frameworkType` | string | Framework agreement type as published, for example with or without reopening of competition. |
| `cpvCode` | string | Main CPV code of the lot (from TED main-classification-lot); the first code of the notice when TED gives no lot code. |
| `cpvScope` | string | lot when cpvCode is the lot's own code, notice when it falls back to the notice-level classification. |
| `cpvCodes` | string | All CPV codes of the notice, separated by commas. |
| `contractNature` | string | Supplies, services or works. |
| `lotCount` | integer | Number of lots in the award notice (TED lot list, identifier-lot); when TED gives no lot list, the number of awarded results. |
| `found` | boolean | False only for the single status row emitted when a run has no results. |
| `scrapedAt` | string | ISO 8601 timestamp of extraction. |

Sample record:

```json
{
  "query": "software",
  "id": "406127-2023/LOT-0001",
  "noticeNumber": "406127-2023",
  "lotId": "LOT-0001",
  "title": "Estonia – Software package and information systems – Public transport ticketing software",
  "contractTitle": "Ticketing system maintenance",
  "lotTitle": "Los 2 Dienstleistung",
  "lotDescription": "Support services for the licence administration.",
  "sourceUrl": "https://ted.europa.eu/en/notice/-/detail/406127-2023",
  "buyerName": "Tallinna Transpordiamet",
  "buyerCountry": "EST",
  "buyerCity": "Tallinn",
  "incumbentName": "AS Connecto Eesti",
  "incumbentCountry": "EST",
  "incumbentSize": "sme",
  "incumbentId": "10201316",
  "allIncumbents": "CIR FOOD S.C.; VIVENDA SPA",
  "awardValue": 500000,
  "currency": "EUR",
  "awardDate": "2023-10-16",
  "publishedAt": "2023-11-13",
  "contractStart": "2023-09-06",
  "contractEnd": "2026-09-05",
  "endDateSource": "start+duration",
  "daysToExpiry": 158,
  "monthsToExpiry": 5.2,
  "contractLengthMonths": 36,
  "renewalOptionsMax": 1,
  "renewalTerms": "The contract may be extended once for up to 12 months.",
  "frameworkAgreement": false,
  "frameworkType": "fa-w-rc",
  "cpvCode": "72000000",
  "cpvScope": "lot",
  "cpvCodes": "72000000, 48000000",
  "contractNature": "services",
  "lotCount": 3,
  "found": true,
  "scrapedAt": "2026-09-30T08:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~ted-contract-expiry-radar/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries":["software"],"expiresAfterMonths":0,"expiresBeforeMonths":12,"maxItems":20}'
```

## FAQ

**Does it list contracts that are not yet awarded?**  
No. It covers awarded contracts and shows when each one ends. Use the expiry window to find recompete opportunities early.

**Why are some contracts missing?**  
Four reasons. First, a notice with neither an end date nor a duration cannot be placed in an expiry window, and lots without a selected winner are skipped. Second, contracts with a stated end date are always found, but for estimated end dates the Actor asks TED only about common durations: 3, 6, 9, 12, 15, 18, 24, 30, 36, 42, 48, 60, 72, 84, 96 and 120 months, and 1 to 8 and 10 years. Contracts published with another length (for example 4, 11 or 20 months) or with a duration in days or weeks are found only when they also state an end date. In a sample of 2023 notices this leaves out roughly 7 percent of those that publish a duration. Third, TED lists conclusion dates per signed contract, not per lot, and does not say which contract belongs to which lot. When a notice has several contracts with different conclusion dates, the Actor does not guess: awardDate and contractTitle stay empty, and the end date is computed only from the lot's own start date. This is the most common reason a notice found by the duration search gives no row; the run status says how many of those notices produced one. Fourth, TED publishes the per-lot fields (end dates, durations, titles, CPV codes, renewal terms) as lists that follow the notice's lot list, and it sometimes leaves entries out: one notice with 46 lots had 45 end dates. The Actor matches each awarded lot to its entry by the lot identifier and uses a list only when it has exactly one entry per lot; otherwise those fields stay empty and a lot that cannot be placed in the window is not returned, because guessing would attach another lot's date. TED lets a single query read at most 15,000 notices, and 11 of the 24 queries of the default 12-month window match more. The Actor splits such a query into shorter date windows on its own, so nothing is dropped. Only a single day with more than 15,000 notices would be cut, and then the run status says INCOMPLETE and names the day.

**How long does a run take and are there limits?**  
TED rate-limits its public search API, so the Actor sends about one request per second. Results are read in monthly expiry slices, two queries per month (stated dates, then estimated ones). A window of 12 months means up to 24 queries. Each query can span many pages of 100 notices, one request per page. In a measurement on 30 September 2026 the default 12-month window without filters matched about 251,000 notices (64,000 for stated dates, 187,000 for estimated ones), which is roughly 2,600 requests and about 45 minutes; a window of two to three months took about 8 minutes. Narrow the window, add a country or CPV prefix, or set a maximum number of results to finish faster. Most runs finish much sooner, because the Actor stops as soon as it reaches your maximum results on the first pages. TED matches notices, not single lots: a notice is returned when any of its lots fits the window, and the Actor then keeps only the lots that really fit, so many lots read are discarded. The run status reports how many lots had a stated, estimated or missing end date. The Actor stops as soon as it reaches your maximum results, and a run that is migrated to another server continues without charging twice for the results it already returned.

**The run failed with "none has a contract end date". What does it mean?**  
TED returned awarded lots but none of them carried an end date or duration, which points to a change in the source data rather than to an empty search. The run fails on purpose so that you are not told there are no expiring contracts. Try again later or open an issue.

**Which countries are covered?**  
All buyers that publish award notices on TED, that is the EU member states and several other European countries.

**Why is the incumbent empty for some lots?**  
When a notice has several lots and the winners cannot be matched to lots reliably, the Actor leaves the incumbent empty and lists all winners in `allIncumbents` instead of guessing.

**How current is the data?**  
Every run reads the live TED API. Notices appear on TED shortly after publication.

**Can I schedule it?**  
Yes, use Apify schedules or call the Actor from your own workflow.

**Something looks wrong.**  
Open an issue with the input you used; layout or API changes at the source are fixed quickly.

## More from datagrit

- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.
- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.
- [Poland KRS New Company Registrations Feed](https://github.com/getdatagrit/poland-krs-new-companies) - Newly registered Polish companies, foundations and associations from the official KRS court register: NIP, address, PKD, capital, email, with filters and change detection.
- [Ashby Salary Scraper - Startup Job Pay Ranges](https://github.com/getdatagrit/ashby-salary-scraper) - Ashby job postings with normalized annual salary ranges, equity flags and new-since-last-run detection.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/ted-contract-expiry-radar). Examples are MIT licensed.
