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
        reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
        reply = f'{message.author.mention} いや読んでないか' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
        
@bot.event
async def on_message_a(message1):
    if message1.content.startswith('/join'):
        role = discord.utils.get(message1.guild.roles, name='member')
        await message1.author.add_roles(role)
        reply = f'{message1.author.mention} ようこそ！'
        await message1.channel.send(reply)
        
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def nekoo(ctx):
    await ctx.send('にゃおーん')

bot.run(token)
