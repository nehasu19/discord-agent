# Discord Bot Agent

A Discord bot with an agent system that reads messages and generates intelligent replies.

## Project Structure

```
discord/
├── src/
│   ├── agent.ts       # Bot agent logic for processing and replying
│   ├── server.ts      # Main server and bot client setup
├── dist/              # Compiled JavaScript (generated after build)
├── package.json       # Dependencies and scripts
├── tsconfig.json      # TypeScript configuration
├── .env.example       # Example environment variables
└── README.md          # This file
```

## Features

- **Agent-based Message Processing**: `BotAgent` reads incoming messages
- **Smart Replies**: Contextual responses based on message content
- **Error Handling**: Graceful error handling for failed operations
- **Typing Indicator**: Shows bot is "typing" before responding
- **DM & Server Support**: Works in both direct messages and text channels

## Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

Copy `.env.example` to `.env` and add your bot token:

```bash
cp .env.example .env
```

Edit `.env`:
```
DISCORD_TOKEN=your_bot_token_here
```

**To get a bot token:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and click "Add Bot"
4. Copy the token and paste in `.env`

### 3. Run the Bot

**Development mode** (with auto-reload):
```bash
npm run dev
```

**Build for production**:
```bash
npm run build
npm start
```

## How It Works

### Agent System

The `BotAgent` class processes messages:

1. **Receives**: Discord message object
2. **Processes**: Analyzes message content
3. **Generates**: Creates contextual reply
4. **Returns**: Reply string to server

### Server Flow

1. Bot starts and connects to Discord
2. Listens for new messages
3. Agent processes message
4. Bot sends reply with mention notification disabled

## Example Interactions

```
User: "hello"
Bot: "Hello username! 👋 How can I help you?"

User: "Can you help me?"
Bot: "Great question username! Let me think about that... 🤔"

User: "thanks"
Bot: "You're welcome username! Happy to help! 😊"
```

## Customization

Edit `src/agent.ts` to add more reply patterns and logic:

```typescript
private generateReply(content: string, message: Message): string {
  // Add your custom logic here
}
```

## Troubleshooting

- **Bot not responding**: Check token in `.env` is correct
- **"intents" error**: Ensure message content intent is enabled in Developer Portal
- **Connection issues**: Verify bot has permissions in your server

## Dependencies

- **discord.js**: Discord API library
- **dotenv**: Environment variable management
- **TypeScript**: Type-safe JavaScript

## License

MIT
