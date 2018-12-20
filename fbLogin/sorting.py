# Bubble sort

def bubble_sort(arr):
	change = True
	while change:
		change = False
		for j in range(1, len(arr)):
			if arr[j-1] > arr[j] :
				temp = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp
				change = True
	return arr

def bubbleSort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break

    return arr


# selection sort

def selection_sort(arr):
	for i in range(len(arr)):
		change = False
		min_index = i
		for j in range(i+1, len(arr)):
			if arr[min_index] > arr[j]:
				min_index = j
				change = True
		if change :
			arr[i], arr[min_index] = arr[min_index], arr[i]

	return arr


# insertion sort

def insertion_sort(arr):
	for i in range(1, len(arr)):
		insertion_index = 0
		change = False
		for j in range(0, i):
			if arr[j] > arr[i] :
				insertion_index = j
				change = True
				break

		if change :
			arr[i], arr[insertion_index] = arr[insertion_index], arr[i]
	return arr

x = [10, 89, -1, 3, 25]
# bubble complexity : o(n2)
# data = bubbleSort(x)
# data = bubble_sort(x)

# selection complexity : Oo(n2)
# data = selection_sort(x)

# insertion complexity : o(n2)
data = insertion_sort(x)

print(data)