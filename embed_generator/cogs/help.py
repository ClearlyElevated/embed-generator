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
<https://discord.club/embedg/>

**- How do I mention someone or something?**
<https://discordapp.com/developers/docs/reference#message-formatting-formats>

**- Where and how can I use Markdown?**
You can use markdown in the description and field values. 
<https://gist.github.com/cblastin/432dc1bda68b0123b5b4a06c347f3c7b>

<https://discord.club/discord>
            """)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
