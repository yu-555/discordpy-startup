from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
@bot.event
async def on_message(message):
    if bot.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？ + /n + いや読んでないか' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
        
@bot.command()
async def join(message):
    if message=='/join':
        role = discord.utils.get(message.guild.roles, name='test')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)
        
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def nekoo(ctx):
    await ctx.send('にゃおーん')

bot.run(token)
