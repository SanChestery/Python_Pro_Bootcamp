'''with open("weather_data.csv", "r") as f:
    lines = f.readlines()

print(lines)'''

'''import csv

with open("weather_data.csv") as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)
'''

import pandas

data = pandas.read_csv("weather_data.csv")
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

# First Task
print("Calc avg temp")

avg = sum(temp_list) / len(temp_list)

print(avg)

# Second challenge
print(data['temp'].max())

# Return row
print(data[data.day == "Monday"])

# Challenge 3
print(data[data.temp == data.temp.max()])

# Challenge 4
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
far_monday_temp = monday_temp * (9/5) + 32

print(far_monday_temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 45, 55]
}

dataframe = pandas.DataFrame(data_dict)
print(dataframe)
dataframe.to_csv("new_data.csv")
