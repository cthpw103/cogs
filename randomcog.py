import discord
import sys
from discord.ext import commands
import os, urllib, PIL, cStringIO

class CthsRandomStuff:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ouchifell(self, ctx):
		try:
		    attachments = ctx.message.attachments
			for attachment in attachments:
				file = cStringIO.StringIO(urllib.urlopen(attachment['url']).read())
                img = Image.open(file)
				img = img.filter(ImageFilter.BLUR) 
				img.save("ouch.jpg", "JPEG") 
			    await bot.upload(final, filename='ouch.jpg')
				os.remove("ouch.jpg")
				
		except discord.errors.Forbidden:
			await self.bot.say("ouch cant send files")
		except Exception as e:
			await self.bot.say(e)
                
        
def setup(bot):
    bot.add_cog(CthsRandomStuff(bot))
