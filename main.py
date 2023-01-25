from pip import main
import discord
import os
import re
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        msg = message.content.lower()

        if "quoi" in msg:
            await message.channel.send("FEUR !")

        if msg.startswith("oui") or msg.endswith("oui"):
            await message.channel.send("Fi !")
        
        if msg.startswith("non") or msg.endswith("non"):
            await message.channel.send("Bril !")

        if "di" in msg:
            list_di_word = re.findall(r'di\w*',msg)
            for word in list_di_word:
                if len(word) > 4:
                    await message.channel.send(word[2:] + " !")

def main():          
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    client = MyClient()
    client.run(TOKEN)

if __name__ == "__main__":
    main()