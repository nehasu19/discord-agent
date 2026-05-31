import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Bot ready event
@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')
    print(f'🤖 Agent is ready to process messages')

# Message event - Bot reads and replies
@bot.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return
    
    try:
        # Show typing indicator
        async with message.channel.typing():
            # Process message and generate reply
            reply = await process_message(message)
            
            # Send reply if generated
            if reply:
                await message.reply(reply, mention_author=False)
    
    except Exception as error:
        print(f"Error processing message: {error}")
        try:
            await message.reply("Sorry, something went wrong! 😞")
        except Exception as reply_error:
            print(f"Error sending error message: {reply_error}")
    
    # Process bot commands
    await bot.process_commands(message)

# Message processing function
async def process_message(message):
    """Process incoming message and generate a reply"""
    content = message.content.lower()
    
    # Greetings
    if any(word in content for word in ['hello', 'hi', 'hey']):
        return f"Hello {message.author.name}! 👋 How can I help you?"
    
    # Questions
    if '?' in content:
        return f"Great question {message.author.name}! Let me think about that... 🤔"
    
    # Help command
    if 'help' in content:
        return (
            f"Here are some things I can do:\n"
            f"• Say 'hello' to greet me\n"
            f"• Ask me questions with '?'\n"
            f"• Just chat with me naturally!\n"
            f"📚 I'm here to help!"
        )
    
    # Thanks
    if any(word in content for word in ['thanks', 'thank you']):
        return f"You're welcome {message.author.name}! Happy to help! 😊"
    
    # Default reply
    return f"That's interesting, {message.author.name}! Tell me more! 👂"

# Run bot
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("❌ DISCORD_TOKEN not found in .env file")
    else:
        bot.run(DISCORD_TOKEN)
