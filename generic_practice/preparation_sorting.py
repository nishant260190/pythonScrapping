x = [5,1,4,-2,8]

# # Bubble sort
# i = 0
# while i < len(x):
# 	change = False
# 	for i in range(len(x)-1):
# 		if x[i]>x[i+1]:
# 			x[i], x[i+1] = x[i+1], x[i]
# 			change = True

# 	if not change :
# 		i = len(x)

# # Selection sort
# for i in range(len(x)-1):
# 	minval = x[i]
# 	index = i
# 	change = False
# 	for j in range(i+1, len(x)):
# 		if x[j] < minval:
# 			minval = x[j]
# 			index = j
# 			change = True
# 	if change :
# 		x[i], x[index] = minval, x[i]


# # Insertion sort

# for i in range(1, len(x)):
# 	current_key = x[i]
# 	j = i-1
# 	while j >= 0 and x[j] > current_key :
# 		x[j+1] = x[j]
# 		j = j-1

# 	x[j+1] = current_key
# 	# print(x)

# print(x)

# Decorator
def fun1(cal_fun):
	def innerfun1(*args, **kwargs):
		print("inner")
		print(*args)
		return cal_fun(*args, **kwargs)

	return innerfun1

@fun1
def fun2():
	print("fun2")

@fun1
def fun3(msg):
	print(msg)
	print("fun3")

fun3("heyy")