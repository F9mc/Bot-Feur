from pip import main
import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            print("[>] pass...")
            return

        if "quoi" in message.content:
            await message.channel.send("-FEUR")

def main():          
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    client = MyClient()
    client.run(TOKEN)

if __name__ == "__main__":
    main()