from linkedin_profile_scraper import LinkedInProfileScraperClient

client = LinkedInProfileScraperClient()
payload = {'profileUrls': ['https://www.linkedin.com/in/public-profile-handle/'],
 'enrich': True,
 'exportFormat': 'default',
 'useDemoOnEmpty': False}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
