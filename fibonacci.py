elements = int(input("Number of elements: "))
first_element = 1
second_element = 1

for i in range(0, elements):
	sum = first_element + second_element
	print(first_element)
	first_element = second_element
	second_element = sum
