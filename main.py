# rxc tip bot
TOKEN = "hahaaa nemore"
import discord
from discord.ext import commands
import backend
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("Bot is ready.")
    await client.change_presence(activity=discord.Game(name="!pomoc"))

@client.command()
async def ping(ctx):
    #await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
    user_id = ctx.author.id
    try: 
        get_balance = backend.get_balance(user_id)
    except:
        get_balance = "Error from rpc"
    embed = discord.Embed(title="Ping", description="Ping", color=0x00ff00)
    embed.add_field(name="Ping:", value=f"{round(client.latency * 1000)}ms", inline=False)
    if get_balance != "Error from rpc":
        embed.add_field(name="RPC:", value=f"Connected", inline=False)
    else:
        embed.add_field(name="RPC:", value=f"Error", inline=False)
    
    await ctx.send(embed=embed)


# commands balance, deposit, withdraw, tip, help

# help

# balance
@client.command()
async def balance(ctx):
    # check in db
    user_id = ctx.author.id
    get_balance = backend.get_balance(user_id)


    #await ctx.send(f"Your balance is {get_balance}")
    embed = discord.Embed(title="Balance", description="", color=0x00ff00)
    embed.add_field(name="RXC:", value=f"{get_balance}", inline=False)
    await ctx.send(embed=embed)

# deposit
@client.command()
async def deposit(ctx):
    # address_user(discord_id)
    user_id = ctx.author.id
    get_address = backend.address_user(user_id)
    #await ctx.send(f"Your deposit address is {get_address}")
    embed = discord.Embed(title="Deposit", description="", color=0x00ff00)
    embed.add_field(name="Deposit Address:", value=f"{get_address}", inline=False)
    await ctx.send(embed=embed)


# withdraw
@client.command()
async def withdraw(ctx, amount, address):
    # def withdraw_rxc(discord_id, amount, address):
    user_id = ctx.author.id
    withdraw_rxc = backend.withdraw_rxc(user_id, amount, address)
    #await ctx.send(f"You have withdrawn {amount} to {address}")
    #await ctx.send(f"Transaction link: https://explorer.crypto.ba/insight/tx/{withdraw_rxc}")
    embed = discord.Embed(title="Withdraw", description="", color=0x00ff00)
    embed.add_field(name="You have withdrawn", value=f"{amount} to {address}", inline=False)
    embed.add_field(name="Transaction link", value=f"https://explorer.crypto.ba/insight/tx/{withdraw_rxc}", inline=False)
    await ctx.send(embed=embed)



# tip
@client.command()
async def tip_test(ctx, amount, user: discord.Member):
    # def tip_user(discord_id_from, discord_id_to, amount):
    user_id_from = ctx.author.id
    user_id_to = user.id
    # check our balance
    get_balance = backend.get_balance(user_id_from)
    if float(get_balance) < float(amount):
        await ctx.send("Nemas dovoljno RXC-a")
        return
    
    tip_user = backend.tip_user(user_id_from, user_id_to, amount)
    embed = discord.Embed(title="Tip", description="", color=0x00ff00)
    embed.add_field(name="You have tipped", value=f"{amount} to {user}", inline=False)
    embed.add_field(name="Transaction link", value=f"https://explorer.crypto.ba/insight/tx/{tip_user}", inline=False)
    await ctx.send(embed=embed)

# tip 
@client.command()
async def tip(ctx, amount, user: discord.Member):
    # def tip_user(discord_id_from, discord_id_to, amount):
    user_id_from = ctx.author.id
    user_id_to = user.id
    # check our balance
    get_balance = backend.get_balance(user_id_from)
    if float(get_balance) < float(amount):
        await ctx.send("Nemas dovoljno RXC-a :(")
        return
    try:
        print("tip")
        # printaj sve
        print("user_id_from: " + str(user_id_from))
        print("user_id_to: " + str(user_id_to))
        print("amount: " + str(amount))
        tip_user = backend.tip_user(user_id_from, user_id_to, amount)
    except:
        await ctx.send("Error from rpc:")
        return
    embed = discord.Embed(title="Tip", description="Tip", color=0x00ff00)
    embed.add_field(name="You have tipped", value=f"{amount} to {user}", inline=False)
    embed.add_field(name="Transaction link", value=f"https://explorer.crypto.ba/insight/tx/{tip_user}", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def pomoc(ctx):
    embed = discord.Embed(title="Help", description="Commands", color=0x00ff00)
    embed.add_field(name="!balance", value="Shows your balance", inline=False)
    embed.add_field(name="!deposit", value="Shows your deposit address", inline=False)
    embed.add_field(name="!withdraw <amount> <address>", value="Withdraws <amount> to <address>", inline=False)
    embed.add_field(name="!tip <amount> <user>", value="Tips <amount> to <user>", inline=False)
    embed.add_field(name="!pomoc", value="Shows this message", inline=False)
    await ctx.send(embed=embed)



# if arguments are not right let user know
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nisi unio sve argumente, kao levat")
client.run(TOKEN)
