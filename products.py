products = []
while True:
	name = input('please enter products name: ')
	if name == 'q':
		break
	price = input('please enter products price: ')
	# p = [name, price]
	products.append([name, price])
print(products)

