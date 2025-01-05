from discord.ext import commands
from resources import constants

class ErrorHandler:
    async def command_executor_is_not_admin(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{constants.NO_ADMIN_PRIVILIGES_MESSAGE}')