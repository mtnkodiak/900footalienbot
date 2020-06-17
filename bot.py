# Work with Python 3.6
import discord
from discord.ext import commands
import logging
from cogs.basic import Basic
from cogs.greetings import Greetings
from cogs.commenters import Commenters

logging.basicConfig(level=logging.INFO)

tokenfile = open(".auth", "r")
TOKEN = tokenfile.readline().strip()
print('Obtained token: ', TOKEN)
def get_prefix(client, message):

    prefixes = ['=', '==']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['==']   # Only allow '==' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command. Also optional
    # Do `return prefixes` if u don't want to allow mentions instead of prefix.
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                         # Create a new bot
    command_prefix=get_prefix,              # Set the prefix
    description='900 Foot Alien Bot',  # Set a description for the bot
    owner_id=611325519807643648,            # Your unique User ID
    case_insensitive=True                   # Make the commands case insensitive
)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.add_cog(Basic(bot))
    bot.add_cog(Greetings(bot))
    bot.add_cog(Commenters(bot))
#     for cog in cogs:
#         bot.load_extension(cog)
#    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the world's problems"))    
#    activity = discord.(name="the world's problems")
    activity = discord.Activity(type=discord.ActivityType.listening, name="the world's problems")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    
    return 

cogs = ['cogs.basic', 'cogs.greetings', 'cogs.commenters']

bot.run(TOKEN, bot=True, reconnect=True)


'''
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return
    if message.content.startswith('!9famembers'):
        if message.content.startswith('!9famembers list'):
            msg = "No members."
            await bot.send_message(message.channel, msg)
            raise NotImplementedError("Not implemented.")
    
    if message.content.startswith('!8ball'):
        answer = eightball()
        await bot.send_message(message.channel, answer)
'''
