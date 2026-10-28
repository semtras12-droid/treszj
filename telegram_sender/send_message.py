"""Send a Telegram message from a personal account using Telethon (MTProto API).

Credentials are read from environment variables:
    TG_API_ID    - numeric api_id from https://my.telegram.org
    TG_API_HASH  - api_hash from https://my.telegram.org

Usage:
    python send_message.py <recipient> <message>
    python send_message.py me "Ahoj"
    python send_message.py @username "Ahoj"
"""

import argparse
import asyncio
import os
import sys

from telethon import TelegramClient

SESSION_NAME = os.path.join(os.path.dirname(__file__), "session", "personal_account")


def load_credentials() -> tuple[int, str]:
    api_id = os.environ.get("TG_API_ID")
    api_hash = os.environ.get("TG_API_HASH")
    if not api_id or not api_hash:
        sys.exit("Set the TG_API_ID and TG_API_HASH environment variables first.")
    return int(api_id), api_hash


async def send(recipient: str, message: str) -> None:
    api_id, api_hash = load_credentials()
    os.makedirs(os.path.dirname(SESSION_NAME), exist_ok=True)
    async with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
        await client.send_message(recipient, message)
    print(f"Message sent to {recipient}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Send a Telegram message from a personal account.")
    parser.add_argument("recipient", help='"me" for Saved Messages, @username, phone number or chat ID')
    parser.add_argument("message", help="Text of the message")
    args = parser.parse_args()
    asyncio.run(send(args.recipient, args.message))


if __name__ == "__main__":
    main()
