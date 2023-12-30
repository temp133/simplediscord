import requests
import json
import websockets
import asyncio
from functools import wraps

def send_message(bot_token, channel_id, message):
    headers = {
        'Authorization': f'Bot {bot_token}',
        'Content-Type': 'application/json',
    }

    data = {
        'content': message,
    }

    response = requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

    return response.json()

async def receive_messages(bot_token):
    gateway_url = f'https://discord.com/api/v10/gateway/bot'
    headers = {
        'Authorization': f'Bot {bot_token}',
    }

    response = requests.get(gateway_url, headers=headers)
    gateway_data = response.json()
    gateway_socket_url = gateway_data['url']

    async with websockets.connect(gateway_socket_url) as ws:
        while True:
            event_data = json.loads(await ws.recv())
            event_type = event_data['t']

            if event_type == 'MESSAGE_CREATE':
                message_data = event_data['d']
                print(f"Received message: {message_data['content']}")

class Command:
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback

def command(name):
    def decorator(callback):
        @wraps(callback)
        def wrapper(*args, **kwargs):
            return callback(*args, **kwargs)
        return Command(name, wrapper)
    return decorator

def send_message(bot_token, channel_id, message):
    headers = {
        'Authorization': f'Bot {bot_token}',
        'Content-Type': 'application/json',
    }

    data = {
        'content': message,
    }

    response = requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

    return response.json()

async def receive_messages(bot_token, commands):
    gateway_url = f'https://discord.com/api/v10/gateway/bot'
    headers = {
        'Authorization': f'Bot {bot_token}',
    }

    response = requests.get(gateway_url, headers=headers)
    gateway_data = response.json()
    gateway_socket_url = gateway_data['url']

    async with websockets.connect(gateway_socket_url) as ws:
        while True:
            event_data = json.loads(await ws.recv())
            event_type = event_data['t']

            if event_type == 'MESSAGE_CREATE':
                message_data = event_data['d']
                content = message_data.get('content', '')
                author_id = message_data['author']['id']

                if content.startswith('!') and author_id != bot_token:
                    command_name = content.split(' ')[0][1:]
                    for command in commands:
                        if isinstance(command, Command) and command.name == command_name:
                            await command.callback(message_data)

def run(bot_token, commands):
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(receive_messages(bot_token, commands))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

def set_status(bot_token, status_type, status_text):
    headers = {
        'Authorization': f'Bot {bot_token}',
        'Content-Type': 'application/json',
    }

    data = {
        'status': status_type,
        'afk': False,
        'since': None,
        'game': {
            'name': status_text,
            'type': 0,
        },
    }

    response = requests.patch(f'https://discord.com/api/v10/gateway/bot', headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Failed to set status. Status code: {response.status_code}, Response: {response.text}")


def run(bot_token):
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(receive_messages(bot_token, command))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

