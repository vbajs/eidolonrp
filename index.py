from discord.ext import commands
import discord
import time
import uuid

print("start")
bot = commands.Bot(command_prefix="℅", self_bot=True)

@bot.event
async def on_ready():
	print("Connected!")
	print(f"Logged in with account {bot.user}.")
	print("Github: https://github.com/kairusds/eidolonrp")

	ms = time.time() * 1000
	timestamp = dict(start=ms)
	assets = dict(
		large_image=("largeimageID,NOTKEY"),
		large_text=("largetext"),
		small_image=("smallimageID,NOTKEY"),
		small_text=("smalltext")
	)

	activity = discord.Activity(
		application_id=int(("appid")),
		name=("name"),
		state=("state"),
		details=("details"),
		assets=assets,
		timestamps=timestamp,
		type=int(("type"))#,
		#url=("url")
	)
	await bot.change_presence(activity=activity, status=discord.Status.online)
	print("Changed rich presence.")

bot.run(("token"), bot=False)