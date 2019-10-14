from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def nekoo(ctx):
    await ctx.send('にゃおーん')
    
@bot.command()
async def on_message(message):
    if bot.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？ + /n + いや読んでないか' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

bot.run(token)
