import random

import pandas

names = ["james", "david", "salomon", "chihuahua"]

student_score = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_score.items() if score >= 60}

print(passed_students)


sentence = "Hey there again we are on the right joerney and this is awsome man very proud of you keep up the good work"
sentenced_splited = {word:len(word) for word in sentence.split()}
sentenced_word_len = {word: index for index, word in enumerate(sentence.split())}
print(sentenced_splited)
print(sentenced_word_len)

# Down is a weather dict exr
weather_dict = {
    'Monday': 25,
    'Tuesday': 20,
    'Wednesday': 18,
    'Thursday': 22,
    'Friday': 28,
    'Saturday': 23,
    'Sunday': 15
}
weather_c = weather_dict
weather_f = {day:temp*3 for (day,temp) in weather_c.items()}
print(weather_f)
print("$$$$"*50)

#Down is dict iteration
coffee_machine = {
    "brand": "ExampleCoffee",
    "model": "EspressoMaster",
    "capacity": 10,  # in cups
    "power": "1200W",
    "color": "Black",
    "features": ["Espresso", "Cappuccino", "Latte", "Hot Water"],
    "water_level": 8,  # current water level in cups
    "coffee_grounds_bin": "Removable",
    "milk_frother": True,
    "display": "Touchscreen",
    "is_on": False  # whether the machine is currently turned on or off
}
coffe_data_frame = pandas.DataFrame(coffee_machine)
print(coffe_data_frame)

