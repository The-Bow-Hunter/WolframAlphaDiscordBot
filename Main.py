import io
import discord
from urllib import parse as urlparse
import requests

print("starting...")

f = open("Discordtoken.txt", "r")
DSTOKEN = str(f.read())
f.close()
f = open("Wolframtoken.txt", "r")
WATOKEN = str(f.read())
f.close()
WABASICURL = str("http://api.wolframalpha.com/v1/simple?appid=" + WATOKEN + "&i=")


class MyClient(discord.Client):

    async def on_ready(self):
        activity = discord.Game("w|a help")
        await self.change_presence(activity=activity)
        print("Up and running!")

    async def on_message(self, message):

        if message.author.bot:
            if client.user in message.mentions:
                await message.channel.send("Du scheinst ein Bot zu sein, deshalb wird meine Nachricht sofort wierder "
                                            "gelöscht werden. Ich reagiere nicht auf andere Bots. "
                                            "(außer sie erwähnen mich wie du) Wenn ein Nutzer das lesen sollte "
                                            "kann er mich "
                                            "mit w|a help ansprechen", delete_after=20)

            return

        if message.content.lower() == "w|a help":
            embed = discord.Embed(title="Wolfram|Alpha", url="https://wolframalpha.com",
                                  description="Bot der Wolfram Alpha Seiten direkt in Discord sendet", color=0xff0a0a)
            embed.set_author(name="TM#5784", url="https://github.com/The-Bow-Hunter")
            embed.set_thumbnail(url="https://www.wolframalpha.com/_next/static/images/Logo_3KbuDCMc.svg")
            embed.add_field(name="Prefix", value="w|a", inline=False)
            embed.add_field(name="Nutzung", value="Schreibe einfach \"w|a \" (ohne Anführungszeichen) und dann den "
                                                  "Befehl den du auch in Wolfram Alpha eingeben würdest", inline=False)
            embed.add_field(name="Der Bot lädt lange",
                            value="Das ist normal. Wolfram Alpha braucht einen Moment um deine Ergebnisse zu berechnen "
                                  "genauso wie auf der Seite selbst",
                            inline=False)
            embed.add_field(name="Der Bot läuft nicht mehr",
                            value="Ich habe leider nur sehr wenige kostenlose Anfragen im Monat zur Verfügung. "
                                  "Mir reichen die Kosten um den Bot laufen zu lassen, deshalb gibt es jedoch "
                                  "irgendwann ein Ende",
                            inline=False)
            embed.add_field(name="Ich will den Bot auf meinem Server haben",
                            value="Ich habe leider nur sehr wenige kostenlose Anfragen im Monat zur Verfügung. "
                                  "Mir reichen die Kosten um den Bot laufen zu lassen. Um für meine eigenen Server "
                                  "die Anfragen freizuhalten ist der Bot nicht öffentlich. "
                                  "Wenn du es unbedingt willst kontaktiere mich persönlich",
                            inline=False)
            embed.set_footer(
                text="TM#5784 Dieser Bot wird in keiner Weise von Wolfram Alpha oder Discord unterstützt und basiert "
                     "nur auf der offiziellen Api")

            await message.channel.send(embed=embed)
            return
        elif message.content.lower().startswith("w|a "):

            await message.add_reaction("✅")
            question = message.content
            question = question[4:]
            questionurl = str(WABASICURL + str(urlparse.quote(question)))
            embed = discord.Embed(title="Wolfram|Alpha", url="https://wolframalpha.com/",
                                  description="Hier hast du deine Antwort von Wolfram Alpha")
            embed.set_author(name="TM")
            embed.set_footer(text="Bot by Tom")
            r = requests.get(questionurl)
            if r.content == "Error 1: Invalid appid":
                await message.channel.send("Es scheint als wäre ich momentan in Wartung. Sorry")
            else:
                await message.channel.send(file=discord.File(fp=io.BytesIO(r.content), filename="WolframAlphaBot.gif"))

            return

        elif client.user in message.mentions:
            await message.channel.send("Mein Prefix ist w|a. Ich helfe bei Mathe indem ich Wolfram "
                                       "Alpha Antworten sende. Wenn du mehr wissen willst schreibe bitte w|a help")

        elif message.author.id == 444548735075352576 and message.content == "wabot stop":
            print("Shutting Bot down...")
            await self.close()


client = MyClient()
client.run(DSTOKEN)