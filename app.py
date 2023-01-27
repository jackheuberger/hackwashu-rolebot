import discord
import os
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    users = []
    adminchannel = 1030137634649026600

    async def on_ready(self):
        f = open("users.txt", "r")
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n","")
            self.users.append(line)
        f.close()
        self.users.append("Jackwustl#2373")
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        # member is just <string>#<delim>
        guild = member.guild
        unverified = guild.get_role(1018545692991557652)
        admin = guild.get_channel(self.adminchannel)
        modlog = guild.get_channel(1018529616719249510)

        if str(member) in self.users:
            try:
                await member.remove_roles(unverified, atomic=True)
                hasRole = unverified in member.roles
                # If after remove_role the user still has unverified, request manual verification
                if hasRole:
                    await member.send("You haven't been automatically verified, but that's ok! I sent the exec team a message and they'll verify you shortly. Welcome to Hack WashU!")
                    await admin.send("Need to verify " + str(member))
                else:
                    print("Verified", str(member))
                    await member.send("You've been automatically verified! Welcome to Hack WashU")
                    await modlog.send("Verified " + str(member))
            except discord.HTTPException as e:
                print(e)
                pass
        else:
            await admin.send(str(member) + " is not in the verified user list")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
