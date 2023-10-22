import dotenv from "dotenv";
import { Client, GatewayIntentBits } from "discord.js";
import OpenAI from "openai";
import { spawn } from "child_process";

dotenv.config();

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

const conversationCache = {};

client.on("messageCreate", async function (message) {
  if (message.author.bot) return;

  const conversationId = message.channel.id;
  const conversation = conversationCache[conversationId];

  // Check if the message mentions the bot
  const botMentioned = message.mentions.has(client.user);

  // Proompt engineering goes brrrrr 

  try {
    let messages = [
      { role: "system", content: "You are like a friend cum assistant which aims to help the user with their questions about the Apecoin DAO. You are provided with the additional context about a query, which you'll need to then respond accordingly. Try to be as helpful as you can and answer within the realm of the data provided." },
    ];

    if (conversation) {
      messages = [...messages, ...conversation];
    }

    messages.push({ role: "user", content: message.content });

    if (botMentioned) {
      const pythonScript = spawn("python", ["SimilaritySearch.py"]);

      // Send user input to the Python script
      pythonScript.stdin.write(message.content);
      pythonScript.stdin.end();

      let result = "";

      // Receive the generated response from the Python script
      pythonScript.stdout.on("data", (data) => {
        result += data.toString();
      });

      pythonScript.on("close", async () => {
        // Reply with the generated response
        await message.reply(result);
      });
    }

    // Cache the conversation history
    conversationCache[conversationId] = messages;

  } catch (err) {
    console.error(err);
    await message.reply("I'm sorry, I'm not smart enough to tell you that.");
  }
});

client.login(process.env.BOT_TOKEN);