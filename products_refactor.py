# 检查文件在不在里面;
import os #载入作业系统 operating system

# 读取档案
def read_file(filename):
	products = [] #一定要存在的
	with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if '商品, 价格' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
	return products

# 让使用者输入
def user_input(products):
	while True:
		name = input('please enter products name: ')
		if name == 'q':
			break
		price = input('please enter products price: ')
		# p = [name, price]
		products.append([name, price])
	print(products)
	return products

# 印出所有购买记录
def print_products(products):
	for p in products:
		print(p[0], 'price is', p[1])

# 写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品, 价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

# 执行
def main_function():
	filename = 'products.csv'
	if os.path.isfile(filename): #检查档案在不在
		print('yeah! find it!')
		products = read_file(filename)
	else:
			print('cannot find it...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

# 呼叫执行
main_function()


#字串只可以字串和字串做合并，不能做减除
# 'abc' + '123' = 'abc123'
# 'abc' * '123' = 'abc'
