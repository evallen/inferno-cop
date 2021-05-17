import os
import discord
from config_loader import load_config


class InfernoCop(discord.Client):
    """
    Top level class to represent the Inferno Cop bot.
    """

    def __init__(self, config, **options):
        super().__init__(**options)

    async def on_ready(self):
        print(f"We have logged in as {client.user}")

    async def on_message(self, message: discord.message):
        if message.author.name == "claytonsav":
            await message.channel.send(f"This really is clayton's best bit")



if __name__ == "__main__":
    config_file_path = "config.yaml"

    token = os.environ.get("TOKEN")

    loaded_config = load_config(config_file_path)
    client = InfernoCop(loaded_config)
    client.run(token)
