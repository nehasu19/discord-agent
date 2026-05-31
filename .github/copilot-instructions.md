# Discord Bot Agent - Development Instructions

A Python Discord bot with an agent system that reads and replies to messages.

## Project Structure

- **discord_only.py**: Main bot with integrated agent that handles all message processing and replies
- **requirements.txt**: Python dependencies (discord.py, python-dotenv, aiohttp)
- **.env**: Environment file with Discord bot token

## Setup Instructions

1. Install dependencies: `pip install -r requirements.txt`
2. Add your Discord bot token to `.env` file
3. Run bot: `python3 discord_only.py`

## Key Components

- **Bot Events**: `on_ready()` - Bot initialization, `on_message()` - Message handling
- **Message Processing**: `process_message()` - Analyzes content and generates replies
- **Agent Logic**: Responds to greetings, questions, help commands, and more
- **Environment Config**: Uses `.env` for secure token management

## Customization

Edit `discord_only.py` in the `process_message()` function to add more reply patterns and conversational logic based on message content.
