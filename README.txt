# SimpleDiscord

SimpleDiscord is a lightweight Discord API wrapper designed for beginners. It aims to provide a straightforward and easy-to-understand interface, making it simple for users to set up and interact with the Discord API.

## Features

- **Simplified Commands:** Create and manage bot commands with ease using the simple and intuitive command system.
- **Customizable Prefix:** Define your own command prefix to suit your bot's style and preferences.
- **Basic Bot Configuration:** Set up your bot quickly with minimal boilerplate code.
- **Designed for Beginners:** SimpleDiscord is tailored to be beginner-friendly, making it accessible to users new to Discord bot development.

## Installation

You can install SimpleDiscord using pip:

pip install simplediscord


Quick Start
Here's a quick example of setting up a bot with SimpleDiscord:

==================================================================================

from simplediscord import run, command, send_message, set_status, api_configure

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = "YOUR_BOT_TOKEN"

# Set up the bot using the desired syntax
bot = run(bot_token, [])

# Configure the bot using the desired syntax
bot.simplediscord.api_configure(token=bot_token, prefix="!")

@command('hello')
async def hello_command(message_data):
    channel_id = message_data['channel_id']
    await send_message(bot_token, channel_id, 'Hello!')

# Start the bot
bot.start()

==================================================================================

Copyright 2023 axx
