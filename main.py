import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)

log_file_path = r"/root/mine-server-fabric/logs/latest.log"
channel_id = 000000000006829  # ID do canal do Discord onde as mensagens serão enviadas

@tasks.loop(seconds=1)  # Define a frequência com que o log será verificado (1 segundo neste exemplo)
async def check_log():
    process = await asyncio.create_subprocess_exec(
        'tail', '-n', '0', '-F', log_file_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    while True:
        line = await process.stdout.readline()
        if line:
            channel = client.get_channel(channel_id)
            await channel.send(line.decode().strip())

@client.event
async def on_ready():
    print(f'Seu bot está logado como: {client.user}')
    check_log.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bot'):
        await message.channel.send('BOT OK!')

client.run(os.getenv('TOKEN2'))
