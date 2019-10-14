import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
# 接続に必要なオブジェクトを生成
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def nekoo(ctx):
    await ctx.send('にゃおーん')
    
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

bot.run(token)
