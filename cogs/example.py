import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.story = ""
        self.channelid = ""
        self.running = False

    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return
        
        ctx = await self.client.get_context(message)
        
        if ctx.valid == False:
            if self.channelid == message.channel:
                if self.running == True:
                    self.story += message.content + " "
        
    @commands.command(aliases = ['p'])
    async def play(self, ctx):
        if ctx.message.channel == self.channelid:
            if self.story != "":
                await ctx.send("Continuing with:" + self.story)
                return
        if self.running:
            await ctx.send("Already Running")
            return
        self.running = True
        self.channelid = ctx.message.channel
        await ctx.send("Ready!")

    @commands.command(aliases = ['t'])
    async def trace(self, ctx):
        if self.running:
            await ctx.send(self.story)
        return

    @commands.command(aliases = ['s'])
    async def stop(self,ctx):
        self.running = False
        try:
            if ctx.message.channel == self.channelid:
                await ctx.send(self.story)
        except:
            pass
        self.channelid = ""
        self.story = ""
        return

    @commands.command(aliases = ['c'])
    async def clear(self, ctx):
        self.story = ""

    @commands.command()
    async def pause(self, ctx):
        if ctx.message.channel == self.channelid:
            self.running = False
            ctx.send("Paused")

    @commands.command()
    async def unpause(self, ctx):
        if ctx.message.channel == self.channelid:
            self.running = True
            ctx.send("Un-Paused")

    @commands.command(aliases = ['h'])
    async def helpplis(self, ctx):
            await ctx.send("play/p\nstop/s\ntrace/t\nclear/c")

def setup(client):
    client.add_cog(Example(client))