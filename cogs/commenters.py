from discord.ext import commands
from chatbot import getchatbot
from random import random


class Commenters(commands.Cog):
    
    @commands.Cog.listener()
    async def on_message(self, message):
        # don't respond to ourselves
        print('message.author.id = ', message.author.id)
        print('message.author.bot = ', message.author.bot)
        if message.author.bot:
            return
        
        if message.content.startswith('-'):
            print('Commenter detected a command.. ignoring.')
            return 
        
        chance = random()
        if (chance < 0.9):
            print('Commenter decided not to comment.')
            return 
        
        chatbot = getchatbot()
        print('Commenter is parsing the string: ', message.content)
        response = chatbot.get_response(message.content)
        print('Commenter is sending the string: ', response)
        await message.channel.send(response)
            
def setup(bot):
    return 