#script for purge command - remove all messages for user in channel
import logging
from discord.ext import commands
import discord

class Purge:
    def __init__(self, ctx, user: discord.User, bot: commands.bot):
        self.ctx = ctx
        self.user = user
        self.bot = bot
    
    async def execute_command(self):    
        await self.ctx.send(f'Are you sure you want to delete messages for {self.user.mention}? [YES/NO]')
        
        was_timeout_exceeded = False
        user_response = ''
        
        try:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == self.ctx.author, timeout=60)
            user_response = msg.content.lower()
        except:
            logging.debug(f'Timeout for response exceeded.')
            was_timeout_exceeded = True        
            
        if user_response == 'yes' and was_timeout_exceeded == False:
            try:
                deleted_count = 0
                async for message in self.ctx.channel.history(limit=None):
                    if message.author.name == self.user.name:
                        await message.delete()
                        deleted_count += 1

                await self.ctx.send(f'Deleted {deleted_count} messages from {self.user.mention}.')
            except Exception as e:
                logging.error(f'Error: {e}')
        else:
            await self.ctx.send(f'Purge operation was aborted.')
            logging.debug(f'Purge operation was aborted.')