import os #operating system


#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查資料在不在／相對路徑
	print('yeah!找到檔案了!')
	with open('products.csv','r',encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name,price = line.strip().split(',')  #strip去換行 split用逗點切割 
			products.append([name, price])
	print(products)
else:
	print('找不到檔案....')



#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1])

#寫入檔案
with open('products.csv', 'w',encoding='utf-8') as f: #打開檔案寫入/encoding='utf-8'編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+str(p[1]) +'\n') #f.write真正的寫入
