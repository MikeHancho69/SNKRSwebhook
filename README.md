# SNKRSwebhook

A webhook notification system for Nike SNKRS releases.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your tokens:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and add your Discord webhook URL:
   - Go to your Discord server
   - Server Settings > Integrations > Webhooks
   - Create a new webhook and copy the URL
   - Paste the URL in your `.env` file

## Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_WEBHOOK_URL` | Yes | Your Discord webhook URL for notifications |
| `DISCORD_SUCCESS_WEBHOOK_URL` | No | Separate webhook for success notifications |
| `SLACK_WEBHOOK_URL` | No | Slack webhook for notifications |
| `CHECK_INTERVAL_SECONDS` | No | How often to check for updates (default: 30) |
| `REGION` | No | Nike region code (default: US) |

## Usage

```python
from config import config

if config.validate():
    # Your webhook logic here
    print(f"Webhook configured for region: {config.REGION}")
```