import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def animales1(ctx):
    await ctx.send(f'Adopta, no compres: Considera darle un hogar a un animal de un refugio. Muchos esperan una segunda oportunidad.!')

@bot.command()
async def animales2(ctx):
    await ctx.send(f'Veterinario es esencial: Visitas regulares para chequeos, vacunación y desparasitación (interna y externa). La esterilización es clave para prevenir enfermedades, camadas no deseadas y algunos problemas de comportamiento.!')


@bot.command()
async def animales3(ctx):
    await ctx.send(f'Dieta adecuada: Proporciónale alimento de buena calidad, apropiado para su especie, edad, tamaño y estado de salud. Evita darle sobras de comida humana, muchas son tóxicas (chocolate, cebolla, uvas, xylitol, etc.).!')

@bot.command()
async def plantas1(ctx):
    await ctx.send(f'Conoce las necesidades: Hay plantas de sol directo, sol indirecto/luz brillante (la mayoría de interiores) y sombra. Ponlas en el lugar correcto. Una planta estirada y pálida pide más luz; una con hojas quemadas, menos.!')

@bot.command()
async def plantas2(ctx):
    await ctx.send(f'Toca la tierra: Mete el dedo unos 2-3 cm en el sustrato. Si está seco, riega; si está húmedo, espera. El error más común es regar en exceso.!')

@bot.command()
async def plantas3(ctx):
    await ctx.send(f'Macetas con agujeros: Imprescindible. El agua estancada pudre las raíces.!')

@bot.command()
async def basura1(ctx):
    await ctx.send(f'Compra a granel: Lleva tus propios envases (bolsas de tela, frascos) para comprar legumbres, frutos secos, especias, etc.!')

@bot.command()
async def basura2(ctx):
    await ctx.send(f'Transforma los envases: Tarros de vidrio para almacenar, germinar o como vasos. Botellas de plástico cortadas como semilleros. Cajas como organizadores.!')

@bot.command()
async def basura3(ctx):
    await ctx.send(f'Limpia los envases: Enjuaga latas, briks y plásticos para evitar malos olores y facilitar el reciclaje.')

@bot.command()
async def secreto(ctx):
    await ctx.send(f'**El truco del café frío para plantas:** Prepara una infusión con los posos usados (1 parte de posos, 5 partes de agua) en un frasco por 24 horas. Úsala para regar plantas ácidas como rosales, hortensias, gardenias y cítricos. Les aporta nutrientes, acidifica ligeramente la tierra y ayuda a repeler babosas. **Importante:** nunca apliques los posos directamente sobre la tierra, ya que pueden enmohecerse.')



@bot.command()
async def ayuda(ctx):
    await ctx.send(f'''**COMANDOS DISPONIBLES:**

`$ayuda` - Muestra esta lista
`$animales1-3` - tips para cuidar animales
`$plantas1-3` - tips para cuidar plantas
`$basura1-3` - tips para manejar la basura''')



bot.run("token")
