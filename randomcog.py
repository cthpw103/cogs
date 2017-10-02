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
            elif t == "<": p -= 1
            elif t == "+": c[p] += 1
            elif t == "-": c[p] -= 1
            elif t == ".": rv.append(chr(c[p]))
            elif t == ",": pass
            elif t == "[":
                if c[p] == 0:
                    while ts[i] != "]": i += 1
                    loop.pop()
                else:
                loop.append(i - 1)
            elif t == "]": i = loop[-1]
            i += 1
        await ctx.send("".join(rv))
    @commands.command()
    async def cthsrandomhelp(self, ctx):
        await ctx.send("only >brainfuck, more is coming soon.")
        
def setup(bot):
    print("installing the best cog ever")
    bot.add_cog(CthsRandomStuff(bot))
	print("thanks for using cth's random stuff cog :D")
