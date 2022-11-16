def fibonacci(first, second, index, limit):
	sum = first + second
	print(first)
	if index < limit:
		fibonacci(second, sum, index + 1, limit)

elements = int(input("Number of elements: "))
first_element = 1
second_element = 1
fibonacci(first_element, second_element, 1, elements)

