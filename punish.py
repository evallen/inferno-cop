async def punish(message, rule_broken):
    await message.channel.send(f"**ALERT:** {message.author.mention} broke rule `{rule_broken}`!")

    if rule_broken in punishment_dictionary:
        await punishment_dictionary[rule_broken](message)
    else:
        await no_punish(message)


async def no_punish(message):
    await message.channel.send("You're lucky, kid. No punishment has been set for this one yet.")


async def punish_next(message):
    await message.channel.send("Your name has been changed to Poopyhead.")
    await message.author.edit(nick="Poopyhead")


async def punish_wft(message):
    await message.channel.send("You must change your profile picture to the Washington Football Team logo.")


async def punish_gword(message):
    await message.channel.send("Your name has been changed to goP noipmahC.")
    await message.author.edit(nick="goP noipmahC")


punishment_dictionary = {
    "next": punish_next,
    "washington_football_team": punish_wft,
    "g_word": punish_gword
}