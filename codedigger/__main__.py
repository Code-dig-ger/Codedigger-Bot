import os
import logging
import discord

from dotenv import load_dotenv
from discord.ext import commands

from api import user

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        logging.error('Token required')
        return
    
    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix=commands.when_mentioned_or('\\'), 
                        strip_after_prefix=True,
                        intents=intents)
    
    @bot.command()
    async def verify(ctx:commands.context, username): 
        print('Author : ', type(ctx.author.name))
        print('Username : ', type(username))
        response = user.bot_verify(username, ctx.author.name+'#'+ctx.author.discriminator)
        print(response.json())
        await ctx.send('pong')

    bot.run(TOKEN)


if __name__ == '__main__':
    main()