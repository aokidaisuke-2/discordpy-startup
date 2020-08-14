from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("はろー"):
        m = "こんにちは、" + message.author.name + "さん"
        await client.send_message(message.channel,m)


# Botの起動とDiscordサーバーへの接続
client.run('token')
