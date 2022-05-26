import discord

music = [
  "https://www.youtube.com/watch?v=O7x2YwnVrs4",
  "https://www.youtube.com/watch?v=wtFPIOV2bWM",
  "https://www.youtube.com/watch?v=oZOcmomoBCQ",
  "https://www.youtube.com/watch?v=As96HhiUwXo",
  "https://www.youtube.com/watch?v=bvmnEIOZ5lU"
]

thehelp = """

   Hi! : blush: I'm Gym Buddy, your best personal trainer! I can give you all the information you need for a healthier life and a more handsome body. Below are some commands to help you learn more about sports

    :pleading_face: `/help_me`: Gives you all the info you need to know about me.
    :technologist: `/users`: Get the number of users on the server
    :headphones: `/workout_music`: Best playlist for workout
    :man_cartwheeling: `/lose_weight`: Best exercices to lose weight
    :muscle: `/gain_weight`: Best exercices to gain weight
    :stopwatch: `/start_train`: If you want to set the timer between the sets 

    :headphones: `/healthy_diet`: Best playlist for workout
    :man_cartwheeling: `/lose_weight`: Best exercices to lose weight
    :muscle: `/proteins`: Best exercices to gain weight
    :stopwatch: `/carbohydrates`: If you want to set the timer between the sets 

"""

gain = """

      Best Exercises for Gain Weight

      1. Squats - increasing the strength and size of the lower body muscles, build muscle around your leg and butt areas.
      
      2. Push-Ups - build both your upper body and core strength, target your abdominals, chest muscles, shoulders,  triceps.
      
      3. Bench Dips -  targets the triceps but it also focuses on your chest and the front part of your shoulder.
      
      4. Crunches - target all the abdominal muscles but they primarily work the abdominal muscle and the obliques, also help in increasing your core strength.
      
      5. Pull-Ups - help in getting chiseled shoulders and ripped arms, also focus on your biceps and latissimus dorsi primarily.
Day1_workout
      6. Bench Press - helps in building shoulders, chest muscles, and triceps. 

"""

lose = """

      Best Exercises for Loss Weight
      
      1. Walking - burns around 167 calories per 30 minutes of walking at a moderate pace of 6.4 km/h. Reduce body fat and waist circumference by an average of 1.5% and   2.8 cm.
      
      2. Jogging/running - burns around 372 calories per 30 minutes of running at 
      9.7-km/h.  It help  to burn belly fat.
      
      3. Cycling - burns around 298 calories per 30 minutes on a bicycle at a moderate pace of 22.4 km/h. Increases insulin sensitivity and reduces the risk of certain chronic diseases.
      
      4. Swimming - swimming for 60 minutes 3 times per week significantly reduce body fat, improve flexibility, and reduce several heart disease risk factors, including high total cholesterol.

"""


with open('Snacks/1.png', 'rb') as f:
  Snacks1 = discord.File(f)
with open('Snacks/2.png', 'rb') as f:
  Snacks2 = discord.File(f)
with open('Snacks/3.png', 'rb') as f:
  Snacks3 = discord.File(f)
  
with open('Lunch/1.png', 'rb') as f:
  Lunch1 = discord.File(f)
with open('Lunch/2.png', 'rb') as f:
  Lunch2 = discord.File(f)
with open('Lunch/3.png', 'rb') as f:
  Lunch3 = discord.File(f)

with open('Dinner/1.png', 'rb') as f:
  Dinner1 = discord.File(f)
with open('Dinner/2.png', 'rb') as f:
  Dinner2 = discord.File(f)
  
with open('Desserts/1.png', 'rb') as f:
  Desserts1 = discord.File(f)
with open('Desserts/2.png', 'rb') as f:
  Desserts2 = discord.File(f)
with open('Desserts/3.png', 'rb') as f:
  Desserts3 = discord.File(f)
  
with open('Breakfast/1.png', 'rb') as f:
  Breakfast1 = discord.File(f)
with open('Breakfast/2.png', 'rb') as f:
  Breakfast2 = discord.File(f)
with open('Breakfast/3.png', 'rb') as f:
  Breakfast3 = discord.File(f)
  
with open('Appetizers/1.png', 'rb') as f:
  Appetizers1 = discord.File(f)
with open('Appetizers/2.png', 'rb') as f:
  Appetizers2 = discord.File(f)
with open('Appetizers/3.png', 'rb') as f:
  Appetizers3 = discord.File(f)

with open('Carbo/1.png', 'rb') as f:
  Carb1 = discord.File(f)
with open('Carbo/2.jpg', 'rb') as f:
  Carb2 = discord.File(f)
  
with open('Proteins/1.jpg', 'rb') as f:
  Protein1 = discord.File(f)

  


Day1_workout = """

Chest workout

Dumbbell Bench Press – target 3 sets of 10, 10, 8 (by adding weight) reps
Incline Dumbbell Bench Press – target 3 sets of 10 reps
Chest Dip – target 3 sets of MAX reps

Triceps workout

Skullcrushers – target 3 sets of 8-10 Reps
One Arm Dumbbell Extension – target 3 sets of 10 reps
Tricep Extension – target 3 sets of 10 reps

Shoulders workout

Barbell Front Raise – target 4 sets of 12 reps
Dumbbell Lateral Raise – target 4 sets of 15, 12, 8, 8 (by adding weight) reps

"""


Day2_workout = """
Back workout

Wide Grip Pull Up – target 3 sets of MAX reps
Lat Pull Down – target 3 sets of 10 reps
Straight Arm Lat Pull Down – target 3 sets of 10 reps
Machine Reverse Fly – target 3 sets of 10 reps
Upright Row – target 3 sets of 8 to 10 reps

Biceps workout

Standing Barbell Curl – target 3 sets of 8 to 10 reps
Preacher Curl – target 3 sets of 10 reps
Incline Dumbbell Curl – target 3 sets of 10 reps
"""

Day3_workout = """
Quads, Glutes and Hamstrings workout

Squat – target 4 sets of 10,10,8,8 reps
Dumbbell Lunge – target 3 sets of 8 on each leg
45 Degree Leg Press – target 3 sets of 12 reps
Leg Curl – target 3 sets of 15 reps
Leg Extension – target 3 sets of 15 reps

Calves workout

Standing Calf Raise – target 5 sets of 10,8,8,8,6 (of heavy)reps
Seated Calf Raise – target 5 sets of 15 (of light) reps
"""

Day4_workout = """
Chest workout

Barbell Bench Press – target 3 sets of 10, 10, 8 reps
Dumbbell Flys – target 3 sets of 10 reps
Cable Crossovers – target 3 sets of 10 reps

Triceps workout

Close Grip Bench Press – target 4 sets of 10, 10, 8, 6 reps
Lying Dumbbell Extension – target 3 sets of 10 reps
Tricep Kickback – target 3 sets of 10 reps

Shoulders workout

Seated Dumbbell Press – target 4 sets of 10, 10, 8, 8 reps
One Arm Cable Lateral Raise – target 3 sets of 12 reps
"""

Day5_workout = """
Back workout

Seated Row – target 4 sets of 10 reps
Bent Over Barbell Row – target 3 sets of 10 reps
Bent Over Row – target 3 sets of 12 reps
Smith Machine Upright Row – target 3 sets of 8-10 reps

Biceps workout

Cable Curl – target 4 sets of 8-10 reps
Concentration Curl – target 3 sets of 10 reps
Reverse Barbell Curl – target 3 sets of 10 reps
"""