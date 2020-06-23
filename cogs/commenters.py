import discord

from chatbot import getchatbot
from discord.ext import commands
import random
from discord.ext.commands import bot


class Commenters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Game("with the API")
        await self.bot.change_presence(status=discord.Status.idle, activity=game)
        
        
    @commands.Cog.listener()
    async def on_message(self, message):
        print("message.author.display_name: ", message.author.display_name)
#        print('message.author.bot = ', message.author.bot)
        print('message content = ', message.content)
        
        # don't respond to ourselves
        if '900FootAlien' in message.author.display_name:
#         if message.author == bot:
            print('Not responding to ourselves.')
            return
        
#         if message.author.bot and not 'Groovy' in message.author.display_name:
#             print('Bot message, not groovy. Ignoring!')
#             return
#         
        if message.content.startswith('=') or message.content.startswith('-'):
            print('Ignoring Bot command.')
            return 

        
        cleanstr = replace_trash(discord.utils.escape_markdown(message.content))
        
        print('cleanstr = ', cleanstr)
        
        if len(cleanstr) == 0:
            print('String to analyze is zero-length!  Looking like a Groovy comment.')
            
            return 

        if (message.content.startswith('Why')):
            print('Someone asked why!')
            response = await respondwhy(message, cleanstr)
            print('I said', response)
            return

        chance = random.random()
        if chance < 0.90:
            print('...but Commenter decided not to comment.')
            return 
        
        print('Commenter is ramping up...')
        chatbot = getchatbot()
        print('Commenter is parsing the string: ', cleanstr)
        response = chatbot.get_response(cleanstr)
        print('Commenter is sending the string: ', response)
        await message.channel.send(response)
           
async def respondwhy(message, cleanstr):
    response = ''
    print('Respondwhy is ramping up...')
    chatbot = getchatbot()
    print('Respondwhy is parsing the string: ', cleanstr)
    response = chatbot.get_response(cleanstr)
    print('Respondwhy is sending the string: ', response)
    await message.channel.send(response)
 
    return response

def replace_trash(unicode_string):
    for i in range(0, len(unicode_string)):
        try:
            unicode_string[i].encode("ascii")
        except:
            # means it's non-ASCII
            unicode_string = unicode_string[i].replace(" ")  # replacing it with a single space
    return unicode_string

  
def setup(bot):
    return 
