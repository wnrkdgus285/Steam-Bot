import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("안녕하세요?")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요?")
    if message.content.startswith("!잘있어"):
        await message.channel.send("안녕히가세요")
    if message.content.startswith("씨발"):
        await message.channel.send("욕쓰면 안되")

    if message.content.startswith("!특정"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)



client.run("NDczMTIxNDY3MjE1OTA0Nzcy.XRcAJQ.k0FGqdkI7gZceRhSBS9y-vhhPaU")