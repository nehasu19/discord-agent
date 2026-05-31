# Discord Bot Agent - Development Instructions

This is a Discord bot with an agent system that reads and replies to messages.

## Project Structure

- **src/server.ts**: Main bot server that listens to Discord events
- **src/agent.ts**: Bot agent that processes messages and generates replies
- **package.json**: Node.js dependencies (discord.js, dotenv, TypeScript)

## Setup Instructions

1. Install dependencies: `npm install`
2. Create `.env` file from `.env.example` and add your Discord bot token
3. Run development mode: `npm run dev`
4. Build for production: `npm run build && npm start`

## Key Components

- **BotAgent**: Processes messages and generates contextual replies
- **Server**: Discord.js client that handles bot lifecycle and message events
- **Environment Config**: Uses `.env` for secure token management

## Customization

Edit `src/agent.ts` to add more reply patterns and conversational logic in the `generateReply()` method.
