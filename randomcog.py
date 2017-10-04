import discord
import sys
from discord.ext import commands
import os, urllib, PIL
from io import StringIO
class CthsRandomStuff:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ouchifell(self, ctx):
                file = StringIO(urllib.request.urlopen(ctx.message.attachments[0].url).read())
                img = Image.open(file)
                img = img.filter(ImageFilter.BLUR) 
                img.save("ouch.jpg", "JPEG") 
                with open('ouch.jpg', 'rb') as f:
                     await bot.send_file(crx.message.channel, f)
                os.remove("ouch.jpg")

    @commands.command()
    async def halp(self, ctx):
                try:
                    bot.say("only command is >ouchifell, send image using the ouchifell command")
                except Exception as e:
                    awaitself.bot.say(e)
                
        
def setup(bot):
    bot.add_cog(CthsRandomStuff(bot))
