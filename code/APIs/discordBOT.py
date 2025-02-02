import discord
from discord.ext import commands

# Enable intents (if you need to fetch channels or members)
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent if needed

# Create the bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # Access the general channel by name
    for guild in bot.guilds:  # Loop through all guilds the bot is part of
        channel = discord.utils.get(guild.channels, name="generale")  # Find the "general" channel
        if channel and isinstance(channel, discord.TextChannel):  # Check if it's a text channel
            await channel.send("Hello, I am your bot!")  # Send a message to the general channel

# Command: Send a message to the general channel on command
@bot.command()
async def hello(ctx):
    channel = discord.utils.get(ctx.guild.channels, name="general")
    if channel and isinstance(channel, discord.TextChannel):
        await channel.send("Hi from the bot!")
    else:
        await ctx.send("I couldn't find the general channel!")

# Run the bot
#TOKEN = ""
bot.run(TOKEN)
