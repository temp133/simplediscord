# SimpleDiscord

SimpleDiscord is an easy-to-use Discord API wrapper designed for beginners. It provides a simple interface for common Discord bot functionalities.

## Features

- **Easy Setup:** Get your bot up and running quickly with minimal configuration.
- **Command Handling:** Create commands effortlessly using SimpleDiscord's built-in command system.
- **Message Sending:** Send messages to Discord channels with just a few lines of code.
- **Flexible:** Customize your bot with ease and adapt it to different server and channel contexts.

## Installation

```python
pip install simplediscord
```

## Example
```python
from simplediscord import run, command, api_configure

bot_token = 'YOUR_BOT_TOKEN'

@command('hello')
async def hello_command(api, message_data):
    await api.send_message(message_data['channel_id'], 'Hello, World!')

run(bot_token, [hello_command]).start()
```

# Contributing
- **Contributions are welcome! Fork the repository, make your changes, and submit a pull request.**

# License
MIT License

Copyright (c) 2023 axxreal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
