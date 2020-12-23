import os
import discord
from message_checker import MessageChecker
from config_loader import load_config
from punish import punish


class InfernoCop(discord.Client):
    """
    Top level class to represent the Inferno Cop bot.
    """

    def __init__(self, config, **options):
        super().__init__(**options)
        self.checker = MessageChecker(config)

    async def on_ready(self):
        print(f"We have logged in as {client.user}")

    async def on_message(self, message):
        if message.author == client.user:
            return

        rule_broken = self.checker.validate_message(message.content)
        if rule_broken is not None:
            await punish(message, rule_broken)


if __name__ == "__main__":
    config_file_path = "config.yaml"

    token = os.environ.get("TOKEN")

    loaded_config = load_config(config_file_path)
    client = InfernoCop(loaded_config)
    client.run(token)
