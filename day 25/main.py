import pandas

datasheet = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data = datasheet['Primary Fur Color']

sum_gray = len(data[data == "Gray"])
sum_black = len(data[data == "Black"])
sum_cin = len(data[data == "Cinnamon"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [sum_gray, sum_cin, sum_black]
}

dataframe = pandas.DataFrame(data_dict)
print(dataframe)
dataframe.to_csv("new_data.csv")
