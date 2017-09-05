import fileinput

# Import data from csv file
data = ""

for line in fileinput.input():
	if line.rstrip():
		data += line
	
# Extract variables
try:
	data = [line.split(",") for line in data.splitlines()]
	target_value = float(data[0][1][1:])
	food_list = [line[0].strip() for line in data][1:]
	prices = [float(line[1].strip()[1:]) for line in data][1:]
except Exception:
	print("Problem formatting variables, please make sure input points to a valid csv file")

	
# Look for any combinations of numbers from a list that add up to a target
def subset_sum(numbers, target, menu_items,	partial=[]):
	s = sum(partial)
	
	if s == target:
		answer = dict([[menu_items[prices.index(price)], 
		"${:,.2f}".format(price)] for price in partial])
		
		print ("\n".join("{}: {}".format(k, v) for k, v in answer.items()), 
		"\nTotal: ${:,.2f}".format(target)) 
		
		return True # Pass flag
	if s > target:
		return  

	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		if subset_sum(remaining, target, menu_items, partial + [n]) == True: # Pass flag
			return True; 

			
try:			
	if subset_sum(prices, target_value, food_list) is not True: # Check flag while running function
		print("No solution exists");
except Exception as e:
	print(e)	
