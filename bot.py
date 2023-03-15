import os
from config import *
import discord
import requests
from discord.utils import get
import logging

print(f"{GUILD} Discord Bot")

logging.basicConfig(
  filename=LOGFILE_PATH,
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s",
  datefmt="%m/%d/%Y %I:%M:%S %p",
)

intents = discord.Intents.default()
intents.members = True


class RegistrationClient(discord.Client):

  async def on_ready(self):
    guild = discord.utils.get(self.guilds, name=GUILD)
    logging.info(f"{self.user} has connected to Discord!")
    logging.info(f"{guild.name}(id: {guild.id})")

    await self.change_presence(status=discord.Status.online,
                               activity=discord.Game("Write me!"))
    print("BOT IS RUNNING!")

  # Automatic message when a user joins the chat
  async def on_member_join(self, member):
    logging.info(f"{member.name} joined the server")
    await member.create_dm()
    await member.dm_channel.send(WELCOME_MSG(member.name))

  # Answer on messages
  async def on_message(self, message):
    # don't respond to ourselves
    if message.author == self.user:
      return

    cnl = message.channel
    cont = message.content.lower().strip()
    logging.info(f"New Message from {message.author}: {cont}")

    # Case: Message starts with token prefix.
    if cont.startswith('!'):
      await self.verify(message, cont)
      return

    # Case: Help command.
    elif cont in ["!help", "help", '"help"']:
      await cnl.send(HELP_MSG)
      return

    # Case: Statistics command.
    elif cont in ["!stats", "!ping"]:
      await cnl.send(f"pong with {str(round(self.latency, 3))} s latency")
      return

    await cnl.send(UNKNOWN_MESSAGE)

  async def verify(self, message, cont):
    cnl = message.channel
    response = None

    try:
      response = requests.get('https://yourapi.com/verify?key=' + cont)

    except Exception as e:
      logging.warning(f"Could not access license server. Error: {e}")
      await cnl.send(ERROR_LICENSE_SERVER_DOWN)
      return

    if response.status_code == 200:
      try:
        json_response = response.json()
        if json_response['valid']:
          # Set role to student
          guild = discord.utils.get(self.guilds, name=GUILD)
          member = await guild.fetch_member(int(message.author.id))
          role = get(member.guild.roles, name=PRO_ROLE)
          await member.add_roles(role)
          logging.info(f"{member} got the role: {role}")
          await cnl.send(SUCCESS_SETTING_ROLE)
        else:
          await cnl.send(ERROR_LICENSE_NOT_VALID)

      except Exception as e:
        logging.error(f"Could not set user role. Error: {e}")
        await cnl.send(ERROR_SETTING_ROLE)
        return

    else:
      await cnl.send(ERROR_LICENSE_SERVER_ERROR)


bot = RegistrationClient(intents=intents)
bot.run(os.environ['TOKEN'])
