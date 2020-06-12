# 读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品, 价格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])

# 让使用者输入
products = []
while True:
	name = input('please enter products name: ')
	if name == 'q':
		break
	price = input('please enter products price: ')
	# p = [name, price]
	products.append([name, price])
print(products)

# 印出所有购买记录
for p in products:
	print(p[0], 'price is', p[1])

#字串只可以字串和字串做合并，不能做减除
# 'abc' + '123' = 'abc123'
# 'abc' * '123' = 'abc'


# 写入档案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')