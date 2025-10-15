products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = int(input('請輸入商品價格：'))
	# p =[]
	# p.append(name) 小清單
	# p.append(price) 小清單
	products.append([name, price]) #直接創作小清單
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

with open('products.csv', 'w',encoding='utf-8') as f: #打開檔案寫入/encoding='utf-8'編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+str(p[1]) +'\n') #f.write真正的寫入
