import discord
from discord.ext import commands, tasks

TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace this with your bot token
CHANNEL_ID = 123456789012345678  # Replace with the Discord channel ID

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    if not send_message_every_two_weeks.is_running():
        send_message_every_two_weeks.start()

@tasks.loop(weeks=2)
async def send_message_every_two_weeks():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("🔔 Biweekly reminder!")
    else:
        print("Channel not found")

bot.run(TOKEN)
