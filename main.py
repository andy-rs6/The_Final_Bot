'''

Made byCeban Andrei (ancrei.ceban@isa.utm.md)

'''


# Importing all needed libraries and modules.
import discord
import time
import numpy
import random
from bot import train_bot
from calorie_calculator import calc_calories
import options

client = discord.Client()

ls  = []

@client.event
async def on_ready():
  print("I am running !")

@client.event
async def  on_message(message):
  if message.author == client.user:
    return 

  #Show the probability of each neuron
  results = train_bot.model.predict([train_bot.bag_of_words(message.content, train_bot.words)])[0]
  # print(results, "------")
  
  #Give us the index of the greatest value(neuron)
  results_index = numpy.argmax(results)
  #Put the results index
  tag = train_bot.labels[results_index]
  # print(tag, "+++++")

  id = client.get_guild(960985346705858670)

  if message.content.startswith("/"):
    
    if message.content == "/users":
      await message.channel.send(f"""We are {id.member_count} members !""")
      
    if message.content == "/workout_music":
      await message.channel.send("Best songs for workout !!!")
      await message.channel.send(random.choice(options.music))

    if message.content == "/lose_weight":
      await message.channel.send(options.lose)

    if message.content == "/snacks":
      await message.channel.send(file=options.Snacks1)
      await message.channel.send(file=options.Snacks2)
      await message.channel.send(file=options.Snacks3)

    if message.content == "/lunch":
      await message.channel.send(file=options.Lunch1)
      await message.channel.send(file=options.Lunch2)
      await message.channel.send(file=options.Lunch3)

    if message.content == "/dinner":
      await message.channel.send(file=options.Dinner1)
      await message.channel.send(file=options.Dinner2)

    if message.content == "/desserts":
      await message.channel.send(file=options.Desserts1)
      await message.channel.send(file=options.Desserts2)
      await message.channel.send(file=options.Desserts3)

    if message.content == "/breakfast":
      await message.channel.send(file=options.Breakfast1)
      await message.channel.send(file=options.Breakfast2)
      await message.channel.send(file=options.Breakfast3)

    if message.content == "/appetizers":
      await message.channel.send(file=options.Appetizers1)
      await message.channel.send(file=options.Appetizers2)
      await message.channel.send(file=options.Appetizers3)

    if message.content == "/help_me":
      await message.channel.send(options.thehelp)
      
    if message.content == "/gain_weight":
      await message.channel.send(options.gain)
    
      
    if message.content == "/S":
      await message.channel.send("Start :muscle:")
      for i in range(1, 31):
          time.sleep(1)
          if i < 32:
              await message.channel.send(i)
          else:
              await message.channel.send("Done  :white_check_mark:")

    
    if message.content.startswith("/calories"):
      await message.channel.send("Please answer the questions! The format: '/' + 'category' + 'space' + 'answer'")
      await message.channel.send("What is your age ?")
      await message.channel.send("What is your gender ?")
      await message.channel.send("What is your weight ?")
      await message.channel.send("What is your height ?")
      await message.channel.send("What is your activity level (none, light, moderate, heavy, or extreme) ?")
      await message.channel.send("Do you want to lose, maintain, or gain weight ?")
      age = 0
      weight = 0
      height = 0
    
    if message.content.startswith("/age"):
      age = int(message.content[5:])
      ls.append(age)
      print(ls)
    if message.content.startswith("/gender"):
      gender = str(message.content[8:])
      ls.append(gender)
      print(ls)
    if message.content.startswith("/weight"):
      weight = int(message.content[8:])
      ls.append(weight)
      print(ls)
    if message.content.startswith("/height"):
      height = int(message.content[8:])
      ls.append(height)
      print(ls)
    if message.content.startswith("/level"):
      level = str(message.content[7:])
      ls.append(level)
      print(ls)
    if message.content.startswith("/goals"):
      goals = str(message.content[7:])
      ls.append(goals)
      print(ls)
    if message.content.startswith("/reset_ls"):
      ls.clear()
  
    await message.channel.send(f""" Your energy consumption for a day is {calc_calories.BMR(ls[0],ls[1], ls[2], ls[3], ls[4], ls[5])} kcal !""")
    if ls[5] == 'gain':
      await message.channel.send(f""" If you want to {ls[5]} weight you need to consume about  \n{calc_calories.Calories(ls[0],ls[1], ls[2], ls[3], ls[4], ls[5])} kcal ! 
     For more information you can watch this video \n https://www.youtube.com/watch?v=vPf6iYIJX8I""")
    else:
      await message.channel.send(f""" If you want to {ls[5]} weight you need to consume about {calc_calories.Calories(ls[0],ls[1], ls[2], ls[3], ls[4], ls[5])} kcal ! 
     For more information you can watch this video https://www.youtube.com/watch?v=dpOnEkMF87s""")
      
    await message.channel.send('carbohydrates.')
    
  else:
    if results[results_index] > 0.75:
    #ne ducem in lista cu intents
      for tg in train_bot.data["intents"]:
        if tg['tag'] == tag:
          #alegem random un raspuns din optiuni
          response = random.choice(tg['responses'])
      await message.channel.send(response)
    else:
      for tg in train_bot.data["intents"]:
        rnd = random.choice(tg['random_q'])
      await message.channel.send(rnd)
    print("done !")
    
client.run("OTYwOTY3MzYwMDQxMzIwNDU4.Gwrdk6.SJc-Ho_xyzrMVif7I4iUewTM_eSC-BviPS2qaU")   
