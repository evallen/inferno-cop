import os
import discord
import random
from config_loader import load_config


class InfernoCop(discord.Client):
    """
    Top level class to represent the Inferno Cop bot.
    """

    def __init__(self, config, **options):
        super().__init__(**options)
        self.config = config
        self.counter = 0

    async def on_ready(self):
        print(f"We have logged in as {client.user}")

    async def on_message(self, message: discord.message):
        if random.random() < self.config["special_chance"]:
            await message.channel.send("**CONGRATULATIONS YOU WON THE SECRET PRIZE YAY 1/1000 CHANCE**")
            for i in range(20):
                await message.channel.send(f"https://tenor.com/view/when-the-drip-is-sus-gif-19616035")

        if message.author.name == "claytonsav":
            self.counter += 1

            if self.counter == self.config["frequency"]:
                self.counter = 0
                await message.channel.send(f"This really is clayton's best bit")


if __name__ == "__main__":
    config_file_path = "config.yaml"

    token = os.environ.get("TOKEN")

    loaded_config = load_config(config_file_path)
    client = InfernoCop(loaded_config)
    client.run(token)
