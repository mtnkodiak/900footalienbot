from datetime import datetime as d
from yt import YTDLSource
import random
import time
import discord

from discord.ext import commands
from games import eightball


# New - The Cog class must extend the commands.Cog class
class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name='ok',
        description="Okay."
    )
    async def ok_command(self, ctx, howmany = 1):
        connected = ctx.author.voice
        if connected:
            try:
                voice_client = await connected.channel.connect() # use the channel object you put into a variable
            except:
                print ("already connected, ok.")
                server = ctx.author.guild
                voice_client = server.voice_client
            
            print("howmany=" + str(howmany))
            x = 0

            if howmany > 10:
                await ctx.send('Too many OKs!  (max 10)')
                return

            while x < howmany:

                mp3name = 'ok' + str(random.randrange(1,47)) + '.mp3'

                print('playing:', mp3name)
                audio_source = discord.FFmpegPCMAudio('static/'+mp3name)
                if not voice_client.is_playing():
                    voice_client.play(audio_source, after=None)
                
                x = x + 1

                time.sleep(1)
        #voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
        
        # channel = author.voice.channel
        # vc = await channel.connect()

       
        #guild = ctx.guild
        #server = ctx.message.guild
        #voice_client = server.voice_client


    # voiceChannel.join().then(connection => {
    #   connection.voice.setSelfDeaf(true);
    # });

        # url = "https://youtu.be/oJ9AvIIJTrY"

        # channel = ctx.author.voice.channel
        # vc = await channel.connect()

        # server = ctx.message.guild
        # voice_channel = server.voice_client

        # async with ctx.typing():
        #     player = await YTDLSource.from_url(url)
        #     vc.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        # await ctx.send('Now playing: {}'.format(player.title))
        

    # Define a new command
    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
        # Gets the timestamp when the command was used

        msg = await ctx.send(content='Pinging')
        # Sends a message to the user in the channel the message with the command was received.
        # Notifies the user that pinging has started

        await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
        # Ping completed and round-trip duration show in ms
        # Since it takes a while to send the messages
        # it will calculate how much time it takes to edit an message.
        # It depends usually on your internet connection speed
        return

    @commands.command(name='8ball',
                      description='Ask the 8ball a question',
                      aliases=['8']
    )
    async def eightball_command(self, ctx):
        # Extracting the text sent by the user
        # ctx.invoked_with gives the alias used
        # ctx.prefix gives the prefix used while invoking the command
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        if text == '':
            # User didn't specify the text   
            await ctx.send(content='You need to specify a question to ask the 8-ball!')            
            pass
        else:
            # User specified the text.
            answer = await ctx.send(content='asking...')
            await answer.edit(content=eightball())
            pass

        return

    @commands.command(name='dm',
                      description='Talk to the 9FA bot',
                      aliases=[]
    )
#     @commands.is_owner()  # The account that owns the bot
    async def dm(self, ctx):
#         chatbot = getchatbot()
# #         channel = bot.get_channel('611325519807643648')
#         answer = await ctx.send(content='Thinking...')
#         response = chatbot.get_response(ctx.message.content)
#         await answer.edit(content=response)
#         
        return


def setup(bot):
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
    
    return
