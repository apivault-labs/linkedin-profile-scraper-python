import json
from linkedin_profile_scraper import LinkedInProfileScraperClient

rows = LinkedInProfileScraperClient().run({'profileUrls': ['https://www.linkedin.com/in/public-profile-handle/'],
 'enrich': True,
 'exportFormat': 'default',
 'useDemoOnEmpty': False})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
