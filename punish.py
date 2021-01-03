import random

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


async def punish_curse(message):
    normal_response = "Not on my good Christian Minecraft server!"

    # Navy Seal Copypasta
    # they asked for it i'm sorry
    special_response = "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo."

    if random.random() < 0.1:
        # I'm so sorry
        await message.channel.send(special_response)
    else:
        await message.channel.send(normal_response)


# --- DEPRECATED ----------------------------------------------------------------------------------------------------

# async def punish_pog(message):
#     await message.channel.send("You must end each of your messages this week with phrase (p-g, p-gchamp) "
#                                "that you violated this rule with. Failure to comply three times will result "
#                                "in demotion to the Kuso Gaki role until the end of the week.")

# async def punish_gword(message):
#     await message.channel.send("Your name has been changed to goP noipmahC.")
#     await message.author.edit(nick="goP noipmahC")

# --- PUNISHMENT DICTIONARY -----------------------------------------------------------------------------------------

punishment_dictionary = {
    "next": punish_next,
    "washington_football_team": punish_wft,
    "curse": punish_curse
}
