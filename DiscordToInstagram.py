import discord
import os
import random
import instagrapi

from PIL import Image
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from instagrapi import Client


#dClient = Discord Client
class Client(commands.Bot):
    #https://www.youtube.com/watch?v=CWoXbL3oZFc
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="ib- ",intents = intents,  help_command=None)
    
    async def setup_hook(self):
        for filename in os.listdir('./cogs/'):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        
dClient = discord.Client()
status = cycle(["Prefix ib-","Instabot","Hello"])

#---INSTAGRAM SET UP---
#iBot = Instagram Bot

iBot = Client()
iBot.login(username = "USERNAME", password="PASSWORD")

#---If you get problems with where things get downloaded, change the line below and redirect it to the folder you want to download stuff in---
#os.chdir("C:\\Path\\To\\Download\\Folder\\")

#CODE
caption = "new Instabot Post by "

alreadyUploading = False

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

@dClient.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=365880135146012672))
    print("Ready!")

#if you use this command it could be, that the discord bot needs to reconnect
#could MAYBE be fixed with using a thread for either the discord or insta bot
@tree.command(name = "post", description="(DONT USE SLASH COMMANDS) uploads an image")
async def post(ctx,*, message:str):
    role = discord.utils.get(ctx.guild.roles, name="InstabotPoster")
    global alreadyUploading
    if role not in ctx.author.roles:
        await ctx.send(f'you dont have the {role.name} role.')
        return
    elif alreadyUploading == True:
        await ctx.send(f'wait for someone else to upload.')
        return
    print("new Post from : "+ctx.message.author.name)
    
    # https://stackoverflow.com/questions/65169339/download-csv-file-sent-by-user-discord-py
    try:
        print(len(ctx.message.attachments))
        if len(ctx.message.attachments) < 1: # Checks if there is an attachment on the message
            await ctx.send(f'you need something in the attachments')
            return
        elif len(ctx.message.attachments) == 1: # If there is only one, get the filename from message.attachments
            alreadyUploading = True
            split_v1 = str(ctx.message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            if filename.lower().endswith(".jpg"): # Checks if it is a .jpg file
                await ctx.message.attachments[0].save(fp=os.getcwd() + "\\" + format(filename)) # saves the file
                
                image = Image.open(os.getcwd() + "\\" + filename)
                image = image.convert("RGB")
                width, height = image.size
                if height >= 1080 or width >= 1080:
                    new_image = image.resize((1080, 1080))
                    new_image.save(os.getcwd() + "\\" + filename)
                
                iBot.photo_upload(os.getcwd() + "\\" + filename, "'"+message+"'\n"+caption + ctx.message.author.name)
                await ctx.send("new Post on Instagram by "+ctx.message.author.name)
                
                os.remove(os.getcwd() + "\\" + filename)

            elif filename.lower().endswith((".mp4")):
                await ctx.message.attachments[0].save(fp=os.getcwd() + "\\" + format(filename)) # saves the file

                iBot.video_upload(os.getcwd() + "\\" + filename, "'"+message+"'\n"+caption + ctx.message.author.name)
                await ctx.send("new Video on Instagram by "+ctx.message.author.name)

                os.remove(os.getcwd() + "\\" + filename)
                os.remove(os.getcwd() + "\\" + filename+".jpg")
                
            else:
                await ctx.send("The File format used is probably not supported by the instagram api")
        elif len(ctx.message.attachments) > 1: # if more, post an album
            print("multiple posts")
            
            alreadyUploading = True
            paths = []
            for i in ctx.message.attachments:
                fileStr = str(i).split("/")
                attachment = fileStr[len(fileStr)-1]
                await i.save(fp=os.getcwd() + "\\"+attachment)

                paths.append(os.getcwd() + "\\" +attachment)
                if attachment.lower().endswith((".mp4",".jpg")):
                    print(attachment + " works")
                else:
                   await ctx.send("The File format of " + attachment +" is probably not supported by the instagram api") 
            
            iBot.album_upload(paths, "'"+message+"'\n"+caption + ctx.message.author.name)
            
            for p in paths:
                os.remove(p)
                
            await ctx.send("new Album on Instagram by "+ctx.message.author.name)
    finally:                
        alreadyUploading = False

dClient.run("TOKEN")