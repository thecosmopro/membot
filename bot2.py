import discord
from discord.ext import commands
from botmantik import sifre_olusturucu, double_letter, yazitura
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send('Merhaba Nasılsın?')

@bot.command()
async def sa(ctx):
    await ctx.send('İyi olduğuna sevindim!')

@bot.command()
async def kötüyüm(ctx):
    await ctx.send('Senin için ne yapabilirim?')

@bot.command('sifreOluştur')
async def sifre_olustur(ctx):
    await ctx.send(f'Senin için 10 Haneli Şifre Oluşturdum: {sifre_olusturucu(10)}')

@bot.command()
async def cift_harf(ctx):
    await ctx.send(f'Hello kelimesini senin için iki defa yazdım: {double_letter("hello")}')

@bot.command()
async def yazi_turaa(ctx):
    await ctx.send(f'Senin için yazı tura attım ve sonuç: {yazitura()}')

@bot.command()
async def standartmem(ctx):
    folder_item = os.listdir('images')
    img = random.choice(folder_item)

    with open(f'images/{img}', 'rb') as f:
        # discord.File(f) komutu sizin görselinizi bir discord dosyasına dönüştürüp saklıyor.
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def hayvanmem(ctx):
    folder_item2 = os.listdir('hayvanmem')
    img2 = random.choice(folder_item2)

    with open(f'hayvanmem/{img2}', 'rb') as f:
        # discord.File(f) komutu sizin görselinizi bir discord dosyasına dönüştürüp saklıyor.
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def minecraftmem(ctx):
    folder_item3 = os.listdir('minecraftmem')
    img3 = random.choice(folder_item3)

    with open(f'minecraftmem/{img3}', 'rb') as f:
        # discorsd.File(f) komutu sizin görselinizi bir discord dosyasına dönüştürüp saklıyor.
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('metin')
async def ftr(ctx):
    with open('file.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
    await ctx.send(text)

bot.run("token")
