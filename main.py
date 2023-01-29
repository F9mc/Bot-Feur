from pip import main
import discord
import os
import re
import requests
from http import HTTPStatus

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
            await message.reply("FEUR !")

        elif msg.startswith("oui") or msg.endswith("oui"):
            await message.reply("Fi !")
        
        elif msg.startswith("non") or msg.endswith("non"):
            await message.reply("Bril !")

        elif "di" in msg:
            list_di_word = re.findall(r'di\w*',msg)
            for word in list_di_word:
                if len(word) > 4:
                    await message.reply(word[2:] + " !")

        elif msg.startswith("!help"):
            txt = requests.get("https://raw.githubusercontent.com/Efrei-Paul/Bot-Feur/main/README.md").text
            await message.reply(txt)
        else: # Discord HTTP status code 
            """
            https://docs.python.org/3/library/http.html
            list(HTTPStatus)
            print(print(val[0].value))
            """

            
            codeListe=list(HTTPStatus)
            
            pass

def main():          
    TOKEN = os.getenv("TOKEN")

    client = MyClient()
    client.run(TOKEN)

if __name__ == "__main__":
    main()