# Discord Bot Agent

A Python Discord bot that reads and replies to messages intelligently.

## Project Structure

```
discord/
├── discord_only.py       # Main bot with integrated agent
├── requirements.txt      # Python dependencies
├── .env                  # Bot token (not in version control)
├── .gitignore
├── .github/              # GitHub configuration
│   └── copilot-instructions.md
└── README.md             # This file
```

## Features

- **Message Processing**: Reads incoming messages and generates intelligent replies
- **Smart Replies**: Contextual responses based on message content
- **Error Handling**: Graceful error handling for failed operations
- **Typing Indicator**: Shows bot is "typing" before responding
- **DM & Server Support**: Works in both direct messages and text channels

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Add your Discord bot token to `.env`:

```
DISCORD_TOKEN=your_bot_token_here
```

**To get a bot token:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and click "Add Bot"
4. Copy the token and paste in `.env`
5. Enable "Message Content Intent" in your bot settings

### 3. Run the Bot

```bash
python3 discord_only.py
```

Or run in the background:
```bash
python3 discord_only.py &
```

## How It Works

### Message Processing Flow

1. **Bot starts**: Connects to Discord and loads intents
2. **Receives message**: `on_message()` event triggered
3. **Processes content**: `process_message()` analyzes the message
4. **Generates reply**: Creates contextual response based on triggers
5. **Sends reply**: Posts response in the same channel

### Reply Patterns

The bot responds to:
- **Greetings** ("hello", "hi", "hey") → Friendly greeting
- **Questions** (any message with "?") → Shows thinking
- **Help requests** ("help") → Lists capabilities
- **Thanks** ("thanks", "thank you") → Appreciation response
- **Default** → Encourages conversation

## Example Interactions

```
User: "hello"
Bot: "Hello username! 👋 How can I help you?"

User: "Can you help me?"
Bot: "Great question username! Let me think about that... 🤔"

User: "thanks"
Bot: "You're welcome username! Happy to help! 😊"

example
<img width="1219" height="739" alt="image" src="https://github.com/user-attachments/assets/ed3c7f0d-d2de-4942-972b-76d28e86ecad" />

```

## Customization

Edit `discord_only.py` in the `process_message()` function to add more reply patterns:

```python
async def process_message(message):
    """Process incoming message and generate a reply"""
    content = message.content.lower()
    
    # Add your custom logic here
    if 'your_keyword' in content:
        return "Your custom response"
```

## Troubleshooting

- **Bot not responding**: Check token in `.env` is correct
- **ModuleNotFoundError**: Run `pip install -r requirements.txt`
- **"intents" error**: Ensure Message Content Intent is enabled in Developer Portal
- **Connection issues**: Verify bot has permissions in your server

## Dependencies

- **discord.py**: Discord API library (v2.7.1)
- **python-dotenv**: Environment variable management
- **aiohttp**: Async HTTP client (required by discord.py)

## License

MIT
