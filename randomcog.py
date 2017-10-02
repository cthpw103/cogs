import discord
import sys
from discord.ext import commands

class CthsRandomStuff:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def brainfuck(self, ctx, code=""):
        c = [0] * 30000
        p = 0
        loop = []
        rv = []
        ts = list(code)
        l = len(ts)
        i = 0;
        while i < l:
            t = ts[i]
            if t == ">": p += 1
            if t == "<": p -= 1
            if t == "+": c[p] += 1
            if t == "-": c[p] -= 1
            if t == ".": rv.append(chr(c[p]))
            if t == ",": pass
            if t == "[":
                if c[p] == 0:
                    while ts[i] != "]": i += 1
                    loop.pop()
                else:
                    loop.append(i - 1)
            if t == "]": i = loop[-1]
            i += 1
        await ctx.send("".join(rv))
                
        
def setup(bot):
    print("installing the best cog ever")
    bot.add_cog(CthsRandomStuff(bot))
	print("thanks for using cth's random stuff cog :D")
