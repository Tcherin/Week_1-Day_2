stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append("Edinburgh Waverley")
stops.insert(0, "Glasgow Queen St")
stops.insert(4, "Polmont")
print(stops)

linlithgow_index = stops.index("Linlithgow")
print(linlithgow_index)

stops.remove("Livingston")
print(stops)

stops.pop(2)
print(stops)

stops_length = len(stops)
print(stops_length)

stops.sort()
print(stops)

stops.reverse()
print(stops)

for stop in stops:
    print(stop)











#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop
