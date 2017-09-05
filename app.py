import fileinput

data = ""

for line in fileinput.input():
	if line.rstrip():
		data += line

data = [line.split(",") for line in data.splitlines()]
target = float(data[0][1][1:])
menu_items = [line[0] for line in data][1:]
prices = [float(line[1][1:]) for line in data][1:]
	

def subset_sum(numbers, target,	partial=[]):
	s = sum(partial)
	# check if the partial sum is equals to target
	if s == target: 
		answer = [[menu_items[prices.index(price)], price] for price in partial]
		print ("Success!", dict(answer))
		return True
	if s >= target:
		return  # if we reach the number why bother to continue

	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		if subset_sum(remaining, target, partial + [n]) == True:
			return True;


if subset_sum(prices, target) is not True:
	print("No solution exists");