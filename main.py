import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)

log_file_path = r"/root/mine-server/logs/latest.log"
channel_id = 1014947550480048178 

@tasks.loop(seconds=1) 
async def check_log():
    process = subprocess.Popen(['tail', '-n', '0', '-F', log_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        line = process.stdout.readline().decode().strip()
        if line:
            channel = client.get_channel(channel_id)
            await channel.send(line)

@client.event
async def on_ready():
    print(f'Seu bot está logado como: {client.user}')
    check_log.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!testebot'):
        await message.channel.send('bot funcionando!')

client.run(os.getenv('TOKEN2'))
