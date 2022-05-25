class calc_calories():
  def Calories(age, gender,weight, height,activity_level, goals):    
    if gender == 'male':
      c1 = 66.5
      hm = 5.003 * height
      wm = 13.75 * weight
      am = 6.75 * age
    elif gender == 'female':
      c1 = 655.1
      hm = 1.850 * height
      wm = 9.563 * weight
      am = 4.676 * age
  
    #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
    bmr_result = c1 + hm + wm - am
    # print("BMR", bmr_result)
  
    # activity_level = input('What is your activity level (sedentary, light, moderate, heavy, or extreme): ')
  
    if activity_level == 'sedentary':
        activity_level = int(1.2 * bmr_result)
    elif activity_level == 'light':
        activity_level = int(1.375 * bmr_result)
    elif activity_level == 'moderate':
        activity_level = int(1.55 * bmr_result)
    elif activity_level == 'heavy':
        activity_level = int(1.725 * bmr_result)
    elif activity_level == 'extreme':
        activity_level = int(1.9 * bmr_result)
    # print("ACT ->", activity_level)
    
    # goals = input('Do you want to lose, maintain, or gain weight: ')
  
    if goals == 'lose':
        calories = activity_level - 500
    elif goals == 'maintain':
        calories = activity_level
    elif goals == 'gain':
        calories = activity_level + 750
    # print(calories)
    return calories

  def BMR(age, gender,weight, height,activity_level, goals):    
    if gender == 'male':
      c1 = 66.5
      hm = 5.003 * height
      wm = 13.75 * weight
      am = 6.75 * age
    elif gender == 'female':
      c1 = 655.1
      hm = 1.850 * height
      wm = 9.563 * weight
      am = 4.676 * age
  
    #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
    bmr_result = c1 + hm + wm - am
    # print("BMR", bmr_result)
  
    # activity_level = input('What is your activity level (sedentary, light, moderate, heavy, or extreme): ')
  
    if activity_level == 'sedentary':
        activity_level = int(1.2 * bmr_result)
    elif activity_level == 'light':
        activity_level = int(1.375 * bmr_result)
    elif activity_level == 'moderate':
        activity_level = int(1.55 * bmr_result)
    elif activity_level == 'heavy':
        activity_level = int(1.725 * bmr_result)
    elif activity_level == 'extreme':
        activity_level = int(1.9 * bmr_result)
    return activity_level

    
