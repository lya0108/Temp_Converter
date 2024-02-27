# get data from user and store it in a list, then display the most recent three entries nicely

# set up empty list
all_calculations = []

# get items of data
get_item = ""
max_calcs = 5

while get_item != "xxx":
    get_item = input("Enter an Item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

# show that everthing made it into list
print("\n\n=== The Full List ===")
print(all_calculations)

# print items starting at the end of the list
if len(all_calculations) >= max_calcs:
    print("\n=== Most Recent  ===")
    for item in range(0, max_calcs):
        print(all_calculations[len(all_calculations) - item - 1])

else:
    print("\n=== Items From Newest to Oldest ===")
    for item in all_calculations:
        print(all_calculations[len(all_calculations) - all_calculations.index(item) - 1])
