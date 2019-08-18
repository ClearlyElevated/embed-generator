from discord.ext import commands as cmd


class Help(cmd.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cmd.command()
    async def help(self, ctx, *args):
        """Help Me"""
        if len(args) == 0:
            await ctx.send(f"""
__**Embed Generator**__

**- How do I use it?**
<https://www.discord.club/tools/embed-generator/>

**- How do I mention someone or something?**
<https://discordapp.com/developers/docs/reference#message-formatting-formats>

**- Where and how can I use Markdown?**
You can use markdown in the description and field values. <https://gist.github.com/ringmatthew/9f7bbfd102003963f9be7dbcf7d40e51>

<https://discord.club/discord>
            """)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
