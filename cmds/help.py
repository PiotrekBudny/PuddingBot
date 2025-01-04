import logging
import discord.ext
import discord.ext.commands
from resources import constants

class Help:
        def __init__(self, ctx, bot: discord.ext.commands.bot):
                self.ctx = ctx
                self.bot = bot
        
        async def execute_command(self):
                embed = discord.Embed(title=f'{constants.HELP_MANUAL_TITLE}')
                for command in self.bot.commands:
                        embed.add_field(name=f"{command.name}", value=command.help, inline=False)

                embed.set_footer(text=f'{constants.HELP_MANUAL_FOOTER}')
                await self.ctx.channel.send(embed = embed)
                logging.debug("Help was genereated and sent.")