import fileinput

data = ""

for line in fileinput.input():
	if line.rstrip():
		data += line

data = [line.split(",") for line in data.splitlines()]
target = float(data[0][1][1:])
menu_items = [line[0] for line in data][1:]
prices = [float(line[1][1:]) for line in data][1:]
	
print(target, menu_items, prices)

def subset_sum(numbers, target,	partial=[]):
	s = sum(partial)
	# check if the partial sum is equals to target
	if s == target: 
		print ("SUCCESS!!!!", partial, target)
	if s >= target:
		return  # if we reach the number why bother to continue

	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		subset_sum(remaining, target, partial + [n]) 
		
subset_sum(prices, target)