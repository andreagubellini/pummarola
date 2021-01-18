import sys
import asyncio
import toml
import discord
from discord.ext import commands

def main():
    pomodoro_standard = 300
    with open("./config.toml", mode="r") as config_file:
        config = toml.load(config_file)
        
    token = config["token"]["token"]

    client = commands.Bot(command_prefix='!')

    @client.event
    async def on_message(message):
	    await client.process_commands(message)

    @client.command()
    async def pummarola(ctx, *args):
        for arg in args:
            print(type(arg))
            if arg is None:
                await asyncio.sleep(arg)
                await pomodoro_end(ctx)
            elif arg in ["-h", "--help"]:
                embed = discord.Embed(title="Commands", description="pummarola commands list", color=0x00ff00)
                embed.add_field(name="!pummarola -h", value="toggles pummarola commands", inline=False)
                embed.add_field(name="!pummarola --help", value="toggles pummarola commands", inline=False)
                embed.add_field(name="!pummarola", value="starts a default 5 minutes pomodoro timers", inline=False)
                embed.add_field(name="!pummarola X", value="starts a pomodoro where timer equals X (X is seconds)", inline=False)
                await ctx.channel.send(embed=embed)
            elif isinstance(arg, str) not in ["-h", "--help"]:
                arg = int(arg)
                for left in range(arg, 0, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{} {:2d} seconds remaining.".format(ctx.author, left))
                    sys.stdout.flush()
                    await asyncio.sleep(1)
                await pomodoro_end(ctx)
            else:
                break

    async def pomodoro_end(ctx):
        await ctx.author.send('Your pummarola timer has come to an end!')

    client.run(token)

if __name__ == "__main__":
    main()