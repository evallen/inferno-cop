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
        self.cegan_username = "Praise the Morning Lord"
        self.counter_clayton = 0
        self.counter_patrick = 0
        self.counter_cegan = 0

    async def on_ready(self):
        print(f"We have logged in as {client.user}")

    async def on_user_update(before, after):
        if before.name == self.cegan_username:
            print(f"Updating Cegan's username. Was: {before.name}. Now: {after.name}")
            self.cegan_username = after.name

    async def on_message(self, message: discord.message):
        if (message.author.name != "Inferno Cop") and (random.random() < self.config["special_chance"]):
            await message.channel.send("**CONGRATULATIONS YOU WON THE SECRET PRIZE YAY 1/1000 CHANCE**")
            for i in range(20):
                await message.channel.send(f"https://tenor.com/view/when-the-drip-is-sus-gif-19616035")

        if (message.author.name != "Inferno Cop") and ("cookie" in message.content):
            await message.channel.send("""
            Here's a recipe for cookies: Preparation time: 40min

Ingredients: 2 cups all-purpose flour 1/2 teaspoon baking soda 1/2 teaspoon salt 3/4 cup unsalted butter melted 1 cup packed brown sugar 1/2 cup white sugar 1 tablespoon vanilla extract 1 egg 1 egg yolk 2 cups semisweet chocolate chips

Procedure: Preheat the oven to 325 degrees F (165 degrees C). Grease cookie sheets or line with parchment paper. Sift together the flour, baking soda and salt; set aside. In a medium bowl, cream together the melted butter, brown sugar and white sugar until well blended. Beat in the vanilla, egg, and egg yolk until light and creamy. Mix in the sifted ingredients until just blended. Stir in the chocolate chips by hand using a wooden spoon. Drop cookie dough 1/4 cup at a time onto the prepared cookie sheets. Cookies should be about 3 inches apart. Bake for 15 to 17 minutes in the preheated oven, or until the edges are lightly toasted. Cool on baking sheets for a few minutes before transferring to wire rack.﻿""")

        if message.author.name == "claytonsav":
            self.counter_clayton += 1

            if self.counter_clayton == self.config["frequency"]:
                self.counter_clayton = 0
                await message.channel.send(f"This really is clayton's best bit")

        elif message.author.name == "Hekc":
            self.counter_patrick += 1
            print(f"Patrick has sent {self.counter_patrick} messages.")


            if self.counter_patrick == (2*self.config["frequency"]):
                print(f"Resetting counter to zero, as Patrick has sent {self.counter_patrick} messages.")
                self.counter_patrick = 0
                await message.add_reaction(client.get_emoji(847670479116173363))
                await message.add_reaction(client.get_emoji(847670877063217182))

        elif message.author.name == self.cegan_username:
            self.counter_cegan += 1
            print(f"Cegan has sent {self.counter_cegan} messages.")

            if self.counter_cegan == self.config["frequency"]:
                print(f"Resetting counter to zero, as Cegan has sent {self.counter_cegan} messages.")
                self.counter_cegan = 0
                await message.channel.send("**THIS IS A CERTIFIED CEGANPOST™**")

if __name__ == "__main__":
    config_file_path = "config.yaml"

    token = os.environ.get("TOKEN")

    loaded_config = load_config(config_file_path)
    client = InfernoCop(loaded_config)
    client.run(token)
