import discord
import os

from discord import app_commands 
from keep_alive import keep_alive
from datetime import datetime

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=299153367890919424)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

    async def on_message(self, message):
        global interact
        msg = message.content

        # not reply to itself
        if message.author == client.user:
            return

        if msg.lower().startswith('$activity'):
            return

        if msg.startswith("$tw"):
            embedmsg = discord.Embed(
                title="test1",
                url=
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
                description="test2\n This is cotton candy color\n",
                color=discord.Color.from_rgb(254, 200, 216))
            embedmsg.set_image(
                url=          "https://media.discordapp.net/attachments/1014105423344844920/1106127240716111912/20230505_185338.jpg?width=585&height=585"
            )
            wokege = '<a:catEat:1090893806972452925> <a:CATBEDOINGTHELAUNDRY:671437010187059200>'
            Tanwa_id = '@Tanwa3k#9184'
            await message.channel.send(wokege)
            await message.channel.send(Tanwa_id)
            await message.channel.send(embed=embedmsg)

        #if msg.startswith("$tw"):
        #    await message.reply(Tanwa_id, mention_author=True)


async def time_module():
  print("time module in use")
  while True:
    current_time = datetime.now().strftime("%H:%M") #hour %H min %M sec %S am:pm %p 
    if current_time == "08:00": # enter the time you wish 
      print("time module ended")
      channel = client.get_channel(1101109237926609009)
      Tanwa_id = os.environ['TANWA_ID']
      await channel.send(f"Good morning Master {Tanwa_id}")
      break

async def greetings():
  await client.wait_until_ready()
  day_of_week = datetime.today().strftime('%A').lower()
  channel = client.get_channel(1101109237926609009)
  Tanwa_id = os.environ['TANWA_ID']
  await channel.send(f"Good morning Master {Tanwa_id}")
  # await study_room_channel.send(embed=embedVar)

time_module()
greetings()

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=299153367890919424), name = 'greetings', description='greets you') #guild specific slash command
async def slash2(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Greeting Mr.{name}')

@tree.command(guild = discord.Object(id=299153367890919424), name = 'activity', description='change bot activity') #guild specific slash command
async def activity(interaction: discord.Interaction, new_activity: str):
    await client.change_presence(activity=discord.Streaming(name=new_activity, url="https://www.youtube.com/watch?v=a5uQMwRMHcs&ab_channel=DaftPunkVEVO"))
    await interaction.response.send_message(f'Successfully change activity to {new_activity}')
    # https://stackoverflow.com/questions/59126137/how-to-change-activity-of-a-discord-py-bot


keep_alive()
client.run(os.getenv('TOKEN'))