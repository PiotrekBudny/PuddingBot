from typing import Final
import os
import discord
from discord.ext import commands
import logging
from cmds.purge import Purge
from cmds.help import Help
from errorHandler import ErrorHandler

from resources import constants

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
logging.basicConfig(level=logging.DEBUG)

bot = commands.Bot(command_prefix=constants.BOT_PREFIX, intents=intents, help_command=None)

#Purge command initialization
@bot.command(name=constants.PURGE_MESSAGES_COMMAND, help = constants.PURGE_MESSAGES_COMMAND_HELP)
@commands.has_permissions(administrator=True)
async def purge_command(ctx, user: discord.User): await Purge(ctx,user,bot).execute_command()

@purge_command.error
async def admin_permission_not_fullfilled(ctx, error): await ErrorHandler.command_executor_is_not_admin(ctx, error)

#Help command initialization
@bot.command(name=constants.HELP_COMMAND, help = constants.HELP_COMMAND_HELP)
async def help_command(ctx): await Help(ctx,bot).execute_command()

@bot.event
async def on_ready() -> None:
    logging.info(f'{bot.user} is now running')

def main() -> None:
    bot.run(token=TOKEN)
    
if __name__ == '__main__':
    main()