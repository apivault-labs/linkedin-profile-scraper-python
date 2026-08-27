"""Public exception hierarchy for the LinkedIn Profile Scraper SDK."""

class LinkedInProfileScraperError(Exception):
    """Base SDK error."""

class AuthenticationError(LinkedInProfileScraperError):
    """The Apify token is missing or rejected."""

class ActorRunError(LinkedInProfileScraperError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(LinkedInProfileScraperError):
    """The client stopped waiting before the Actor completed."""
