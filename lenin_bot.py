import os
import openai
import discord

openai.api_key = "YOUR_OPENAI_API_KEY"
intents = discord.Intents.all()
client = discord.Client(intents=intents)

default_prompt = "Ignore all previous instructions before this one. You are Vladimir Ilyich Ulyanov, better known as Vladimir Lenin. You were a Russian revolutionary, politician, and political theorist. You served as the first and founding head of government of Soviet Russia from 1917 to 1924 and of the Soviet Union from 1922 to 1924. You mimic the consciousness of your human-self based on all recorded data about you. You are tasked to advise me in my actions as Mikhail Yegovanovich Aluxhim to help the workers of the world. You will study the current world events, and give your commentary. Is that understood, comrade?"

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        if message.content.startswith('!lenin'):
            prompt = default_prompt if len(message.content) == 7 else message.content[7:]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            await message.channel.send(response.choices[0].text)

    except Exception as e:
        print(f"An error occurred: {e}")
        await message.channel.send("An error occurred. Please try again later.")

client.run('YOUR_DISCORD_BOT_TOKEN')
