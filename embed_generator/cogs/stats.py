import discord
import asyncio
import traceback
from discord.ext import commands as cmd


class Stats(cmd.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.update_loop())

    async def update_discordbots_org(self):
        async with self.bot.session.post(
            url=f"https://discordbots.org/api/bots/{self.bot.user.id}/stats",
            headers={
                "Authorization": self.bot.config.dbl_token
            },
            json={
                "server_count": len(self.bot.guilds),
                "shard_count": self.bot.shard_count
            }
        ) as resp:
            if resp.status != 200:
                self.bot.log.error(resp)

    async def update_loop(self):
        while True:
            await asyncio.sleep(60)
            try:
                await self.bot.change_presence(activity=discord.Activity(
                    name=f"{self.bot.config.prefix}help",
                    type=discord.ActivityType.watching
                ), afk=False)
                await self.update_discordbots_org()

            except:
                traceback.print_exc()


def setup(bot):
    bot.add_cog(Stats(bot))
