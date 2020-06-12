products = []
while True:
	name = input('please enter products name: ')
	if name == 'q':
		break
	price = input('please enter products price: ')
	# p = [name, price]
	products.append([name, price])
print(products)


for p in products:
	print(p[0], 'price is', p[1])

#字串只可以字串和字串做合并，不能做减除
# 'abc' + '123' = 'abc123'
# 'abc' * '123' = 'abc'

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')