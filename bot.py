import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")
    canal = bot.get_channel(1443311641281167492) 
    if canal:
        await canal.send("Oi! Digite /poluicao para mais informações.")

@bot.command()
async def poluicao(ctx):
    await ctx.send("Oi! Eu sou um bot que te informará quanto tempo um item demora para se decompor.")
    await ctx.send("Use /itens para descobrir quais itens são disponíveis.")

@bot.command()
async def itens(ctx):
    await ctx.send("Os itens disponíveis são Cascas, Cigarros, Tampinhas, Baterias, Papeis, Plastico, Chicletes, Metal, Vidro, Couro, Nylon, Isopor e Tecido.")
    await ctx.send("Use o comando /item para descobrir informações (ex.: /Cascas)")

@bot.command()
async def Cascas(ctx):
    await ctx.send("As cascas, de frutas e legumes, demoram de 1 a 3 meses para se decomporem na natureza. Elas devem ser jogadas em lixos comuns.")

@bot.command()
async def Cigarros(ctx):
    await ctx.send("Os cigarros demoram cerca de 2 anos para se decomporem, e devem ser jogados em lixos comuns.")

@bot.command()
async def Tampinhas(ctx):
    await ctx.send("As tampinhas de garrafa demoram entre 100 e 500 anos para se decomporem, o que é muito tempo. Elas devem ser descartadas em lixos recicláveis.")

@bot.command()
async def Baterias(ctx):
    await ctx.send("As baterias e pilhas demoram entre 100 e 500 anos para se decomporem. Elas devem ser descartadas de modo diferente: Armazene, Embale (com sacolas plásticas), e leve até um ponto de coleta (supermercados, farmácias, lojas de eletrônicos, assistências técnicas, etc.). Eles saberão como descartar.")

@bot.command()
async def Papeis(ctx):
    await ctx.send("Papéis como embalagens ou jornais demoram de 1 a 4 meses para se decomporem. Eles devem ser jogados em lixos recicláveis.")

@bot.command()
async def Plastico(ctx):
    await ctx.send("Plásticos diversos, como sacolas, garrafas, copos descartáveis, etc., demoram cerca de 400 anos para se decomporem. Descarte no lixo reciclável")

@bot.command()
async def Chicletes(ctx):
    await ctx.send("Chicletes demoram até 5 anos para se decomporem. Descarte em lixos comuns.")

@bot.command()
async def Metal(ctx):
    await ctx.send("O metal demora mais de 200 anos para se decompor. Descarte em lixo reciclável.")

@bot.command()
async def Vidro(ctx):
    await ctx.send("O vidro demora mais de 1000 anos para se decompor. Descarte em lixo reciclável")

@bot.command()
async def Couro(ctx):
    await ctx.send("O couro demora cerca de 50 anos para se decompor. Descarte em empresas de reciclagem especializada ou doe para escolas/artistas. Se não for possível, descarte em lixo comum.")

@bot.command()
async def Nylon(ctx):
    await ctx.send("O nylon, encontrado principalmente em roupas, demora mais de 30 anos para se decompor. Descarte em lixo reciclável.")

@bot.command()
async def Isopor(ctx):
    await ctx.send("O isopor demora cerca de 8 anos para se decompor. Limpe e descarte no lixo reciclável.")

@bot.command()
async def Tecido(ctx):
    await ctx.send("O tecido demora entre 6 e 12 meses para se decompor. Tente doar ou vender. Se não for possível, entregue num ponto de coleta especializado. Se não for possível, descarte em lixo reciclável.")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            arquivo_nome = attachment.filename
            await attachment.save(f"./{arquivo_nome}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels,txt", image_path=arquivo_nome))

    else:
        await ctx.send("Você não anexou nenhuma imagem.")


bot.run("MTQ1MDkxMzU1MjM5MDE2NDUzMA.GC4zwK.SYiEYKXbJZN42swmmMuUlOrYpX02wGGFEm4e7o")