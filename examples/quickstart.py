from linkedin_profile_scraper import LinkedInProfileScraperClient

client = LinkedInProfileScraperClient()
rows = client.run({'profileUrls': ['https://www.linkedin.com/in/public-profile-handle/'],
 'enrich': True,
 'exportFormat': 'default',
 'useDemoOnEmpty': False})
print(rows[0] if rows else "No results")
