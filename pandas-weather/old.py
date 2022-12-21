# import csv
#
# with open("./weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")

# all columns (entire file):    dataFrame type in Pandas
# one column:                   series type in Pandas

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(round(average, 2))

print(data["temp"].mean())
print(data.temp.max())

# Working with rows
print(data[data.day == "Tuesday"])
print(data[data.temp == data.temp.max()])

tuesday = data[data.day == "Tuesday"]
print(tuesday.condition)
tuesday_temp = int(tuesday.temp)
tuesday_temp_fahrenheight = tuesday_temp * 9/5 + 32
print(tuesday_temp_fahrenheight)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_data.csv")
print(data2)






