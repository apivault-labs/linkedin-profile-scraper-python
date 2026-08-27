import csv
from linkedin_profile_scraper import LinkedInProfileScraperClient

rows = LinkedInProfileScraperClient().run({'profileUrls': ['https://www.linkedin.com/in/public-profile-handle/'],
 'enrich': True,
 'exportFormat': 'default',
 'useDemoOnEmpty': False})
if rows:
    scalar_keys = [k for k, v in rows[0].items() if not isinstance(v, (dict, list))]
    with open("results.csv", "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=scalar_keys)
        writer.writeheader()
        writer.writerows({k: row.get(k) for k in scalar_keys} for row in rows)
