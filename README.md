# LinkedIn Profile Scraper — Python SDK

Python client for the [LinkedIn Profile Scraper Apify Actor](https://apify.com/apivault_labs/linkedin-profile-scraper-no-cookies). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/linkedin-profile-scraper-no-cookies)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Available public identity and career fields
- Nested JSON or flat CRM rows
- Caller-provided CRM correlation IDs
- Explicit completeness and missing-section metadata

Profile-field availability varies by public visibility. The SDK exposes only the Actor's public contract; collection and processing remain inside the hosted Actor.

## Install

```bash
pip install git+https://github.com/apivault-labs/linkedin-profile-scraper-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from linkedin_profile_scraper import LinkedInProfileScraperClient

client = LinkedInProfileScraperClient(api_token="apify_api_xxxxxx")
rows = client.run({'profileUrls': ['https://www.linkedin.com/in/public-profile-handle/'],
 'enrich': True,
 'exportFormat': 'default',
 'useDemoOnEmpty': False})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `profileUrls` | `array` | `—` | Full public /in/ URLs or bare usernames. Exact duplicates are removed. Up to 100 unique profiles per run. |
| `profiles` | `array` | `[]` | Optional objects with url and id. The id is copied to output as inputId. Up to 100 records per run. |
| `enrich` | `boolean` | `True` | Derive seniority, tenure and lead-research signals from available public fields. These heuristics may be incomplete and must not be used as employment or eligibility decisions. |
| `exportFormat` | `string` | `default` | Choose complete nested JSON or a flat row suitable for CSV, Excel and CRM imports. |
| `maxConcurrency` | `integer` | `5` | Maximum number of profiles processed at the same time. |
| `timeout` | `integer` | `60` | Stop waiting for an unavailable profile after this time and continue the batch. |
| `useDemoOnEmpty` | `boolean` | `True` | When enabled, an empty run processes one public demo profile and bills one result if successful. Disable it to finish an empty run without a Dataset item. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/linkedin-profile-scraper-no-cookies).

## Pricing

Pay per delivered result through Apify, starting around **$2/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
