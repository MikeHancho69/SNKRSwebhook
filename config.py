"""
Configuration module for SNKRSwebhook.

Loads tokens and settings from environment variables.
Copy .env.example to .env and fill in your values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class that loads settings from environment variables."""

    # Discord webhooks
    DISCORD_WEBHOOK_URL: str = os.getenv("DISCORD_WEBHOOK_URL", "")
    DISCORD_SUCCESS_WEBHOOK_URL: str = os.getenv("DISCORD_SUCCESS_WEBHOOK_URL", "")

    # Slack webhook
    SLACK_WEBHOOK_URL: str = os.getenv("SLACK_WEBHOOK_URL", "")

    # Nike tokens (optional)
    NIKE_ACCESS_TOKEN: str = os.getenv("NIKE_ACCESS_TOKEN", "")
    NIKE_REFRESH_TOKEN: str = os.getenv("NIKE_REFRESH_TOKEN", "")

    # Monitor settings
    CHECK_INTERVAL_SECONDS: int = int(os.getenv("CHECK_INTERVAL_SECONDS", "30"))
    REGION: str = os.getenv("REGION", "US")

    @classmethod
    def validate(cls) -> bool:
        """Validate that required configuration is present."""
        if not cls.DISCORD_WEBHOOK_URL:
            print("Error: DISCORD_WEBHOOK_URL is required")
            print("Copy .env.example to .env and add your Discord webhook URL")
            return False
        return True


# Create a singleton instance
config = Config()
