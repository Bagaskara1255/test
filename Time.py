import os
import discord
from dotenv import load_dotenv

load_dotenv()
token=os.getenv('token')

client = discord.Client()

@client.event
async def on_ready():
  print("Sudah online !!!")
  
async def on_message():
  if message.author == Client.user:
    return
  
  if message.content.startswith('-+ping'):
    await message.channel.send('PING PONG')
    
client.run(token)