from linkedin_profile_scraper import LinkedInProfileScraperClient

for count in (10, 100, 1000):
    print(count, LinkedInProfileScraperClient.estimate_cost(count), "USD estimated result charges")
