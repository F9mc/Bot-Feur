from pip import main
import discord
import os
import re
import requests

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
        words = msg.split(" ")

        if "quoi" in words:
            await message.reply("FEUR !")

        if "oui" in words:
            await message.reply("Fi !")
        
        if "non" in words:
            await message.reply("Bril !")

        if "di" in msg:
            list_di_word = re.findall(r'di\w*',msg)
            for word in list_di_word:
                if len(word) > 4:
                    await message.reply(word[2:] + " !")

        if "mdr" in msg:
            await message.add_reaction("🤣")

        if msg.startswith("!help"):
            txt = requests.get("https://raw.githubusercontent.com/Efrei-Paul/Bot-Feur/main/README.md").text
            await message.reply(txt)

def main():          
    TOKEN = os.getenv("TOKEN")

    client = MyClient()
    client.run(TOKEN)

if __name__ == "__main__":
    main()