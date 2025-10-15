products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	# p =[]
	# p.append(name) 小清單
	# p.append(price) 小清單
	products.append([name, price]) #直接創作小清單
print(products)

for p in products:
	print(p[0],'的價格是',p[1])