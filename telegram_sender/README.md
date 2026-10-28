# Telegram sender (personal account)

Sends a message from your personal Telegram account through the MTProto API, using [Telethon](https://docs.telethon.dev).

## Setup

1. Get `api_id` and `api_hash` at https://my.telegram.org → **API development tools**.
2. Install the dependency:

   ```bash
   pip install -r telegram_sender/requirements.txt
   ```

3. Export the credentials (do not commit them):

   ```bash
   export TG_API_ID=12345678
   export TG_API_HASH=your_api_hash
   ```

## Usage

```bash
python telegram_sender/send_message.py me "Ahoj z Pythonu"
python telegram_sender/send_message.py @username "Ahoj"
```

The first run asks for your phone number, the login code from Telegram and, if enabled, the two-step verification password. The resulting session file is stored in `telegram_sender/session/` and is ignored by git. Anyone with that file can access the account, so keep it private.

## Notes

- Automating a personal account is not officially supported. Mass messaging or spam can get the account limited or banned.
- Telegram rate-limits frequent requests (`FloodWaitError`). Avoid sending in tight loops.
