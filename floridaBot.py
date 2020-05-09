import discord
import markovify
import pickle
client=discord.Client()



with open('floridaMarkov.pickle', 'rb') as gator:
    markovModel = pickle.load(gator)  
    floridaMarkov = markovify.Text.from_json(markovModel)



@client.event
async def on_ready():
    ##print('logged in as')
    ##print(client.user.name)
    ##print(client.user.id)
    ##print('-----')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Made By u/FormerAddictsThrow"))


    
@client.event
async def on_message(message):
    
    if message.content == '~florida':
        embed=discord.Embed(title= floridaMarkov.make_sentence(), color=0x720027)
        embed.set_author(name="{} News Update: Florida Man Edition!".format(message.guild.name))
        embed.set_thumbnail(url="https://github.com/Former-Addict/Florida-Man-Discord-Bot/blob/master/florida%20man.png?raw=true")
        await message.channel.send(embed=embed)    


client.run('NzA4NTAyNDE3Njg3MzE0NTAy.XrYS-A.YfcHyVC9moC3OsKr4BA5GkQDRe0')