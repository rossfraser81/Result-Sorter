print ("Welcome to the Exam Result Sorter")

#create empty list and prompt for user input
results = []

results.append(int(input("\nEnter your first result (0-100):")))
results.append(int(input("Enter your second result (0-100):")))
results.append(int(input("Enter your third result (0-100):")))
results.append(int(input("Enter your fourth result (0-100):")))

#print results in entered order then desc order
print("\nYour results are: " + str(results))

results.sort(reverse = True)

print("\nYour results from highest to lowest are: " + str(results))

#remove the two lowest value from list, confirm removal and diplay remaining results and highest on separate line
print("\nWe'll now remove your two lowest grades.")

remres1 = results.pop()
print("Removed result: " + str(remres1))
remres2 = results.pop()
print("Removed result: " + str(remres2))

print("\nYour remaining results are:" + str(results))
print("\nYour highest result was " + str(results[0]) + ".")





