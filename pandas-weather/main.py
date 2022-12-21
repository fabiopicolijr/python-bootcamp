import pandas

data = pandas.read_csv("squirrel_data.csv")

# all columns (entire file):    dataFrame type in Pandas
# one column:                   series type in Pandas

#data = data_csv.to_dict()

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

squirrels_df = pandas.DataFrame(data_dict)
squirrels_df.to_csv("squirrels_count.csv")



# table = data_dict()
# print(data_dict)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")
# print(data2)

# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list) / len(temp_list)
# print(round(average, 2))

# print(data["temp"].mean())
# print(data.temp.max())

# Working with rows
# print(data[data.day == "Tuesday"])
# print(data[data.temp == data.temp.max()])
#
# tuesday = data[data.day == "Tuesday"]
# print(tuesday.condition)
# tuesday_temp = int(tuesday.temp)
# tuesday_temp_fahrenheight = tuesday_temp * 9/5 + 32
# print(tuesday_temp_fahrenheight)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")
# print(data2)






