import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        
        if message.author.id == self.user.id:
            return

        if message.content.startswith('hi') or message.content.startswith('Hi'):
            await message.channel.send('Hello {0.author.mention} you can write your commands in the bots text channel.....Type s or S to learn about different commands of the different bots.'.format(message))
            print("Someone said Hi")

        elif message.content.startswith('p'):
            print("Someone is chatting with Pokecord.")

        elif message.content.startswith('S') or message.content.startswith('s'):
            await message.channel.send("""These are the Commands:-
1. s, S - Learn about commands
2. hi, Hi - The casual command
3. p!help - The command to learn to control Pokecord Bot. The messages sent by your bot can be seen on DM Messages.""")
            print("Someone is learning about Commands.")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!. Type s to learn about commands to control the bot.'.format(member, guild)
            await guild.system_channel.send(to_send)
            print("Someone has joined our server.....")

client = MyClient()
client.run('NTY2MjU3Njc4NTM2NDA5MDg5.XLCW5A.Aw_Q1cn6Z9EpnoQdYSzrhRPfsu0')
