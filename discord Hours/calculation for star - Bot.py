import discord
import re
from discord.ext import commands

# Define the bot's command prefix and intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Regular expression to extract volunteer hours
time_pattern = re.compile(r'(\d+)\s*(hours?|h)|(\d+)\s*(minutes?|m)|(\d+)\s*(seconds?|s)', re.IGNORECASE)

# Function to convert time strings to total minutes
def time_to_minutes(time_str):
    matches = time_pattern.findall(time_str)
    total_minutes = 0

    for match in matches:
        if match[0]:
            total_minutes += int(match[0]) * 60  # Hours to minutes
        if match[2]:
            total_minutes += int(match[2])  # Minutes
        if match[4]:
            total_minutes += int(match[4]) / 60  # Seconds to minutes

    return total_minutes

# Dictionary to accumulate volunteer hours for each user
user_volunteer_hours = {}

# Event that triggers when the bot starts
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event that triggers when a new message is received
@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore bot messages

    if ":" in message.content:  # Check if the message has the volunteer hour format
        parts = message.content.split(":")
        if len(parts) >= 3:
            user = parts[1].strip()  # Get the username
            time_str = parts[2].strip()  # Get the time part
            total_minutes = time_to_minutes(time_str)

            # Accumulate volunteer hours for the user
            if user not in user_volunteer_hours:
                user_volunteer_hours[user] = 0
            user_volunteer_hours[user] += total_minutes

    # Make sure the bot still handles other commands
    await bot.process_commands(message)

# Command to get total volunteer hours for each user
@bot.command()
async def volunteer_hours(ctx):
    response = "Volunteer Hours:\n"
    for user, total_minutes in user_volunteer_hours.items():
        total_hours = total_minutes / 60  # Convert to hours
        response += f"{user}: {total_hours:.2f} hours\n"
    await ctx.send(response)

# Run the bot (insert your Discord bot token below)
bot.run('YOUR_DISCORD_BOT_TOKEN')
