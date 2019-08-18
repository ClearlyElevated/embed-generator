from discord.ext import commands as cmd
from aiohttp import ClientSession


class EmbedGenerator(cmd.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=self._prefix_callable,
                         shard_count=self.config.shard_count,
                         shard_ids=self.config.shard_ids,
                         fetch_offline_members=False)

        self.session = ClientSession(loop=self.loop)
        for ext in self.config.extensions:
            self.load_extension(ext)

        print(f"Loaded {len(self.cogs)} cogs")

    async def on_shard_ready(self, shard_id):
        print(f"Shard {shard_id} ready")

    async def on_ready(self):
        print(
            f"Fetched {len(self.users)} members on {len(self.guilds)} guilds")

    async def on_resumed(self):
        print(f"Bot resumed")

    def _prefix_callable(self, bot, msg):
        valid = [f"<@{self.user.id}> ",
                 f"<@!{self.user.id}> ",
                 f"<@{self.user.id}>",
                 f"<@!{self.user.id}>",
                 self.config.prefix]

        return valid

    @property
    def config(self):
        return __import__("config")

    def run(self):
        super().run(self.config.token)

    async def close(self):
        await super().close()
        await self.session.close()


bot = EmbedGenerator()
bot.run()
