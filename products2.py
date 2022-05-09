import os #operationg system 載入作業系統

#讀取檔案
products = []
if os.path.isfile('products2.csv'): #檢查檔案在不在
    print('找到檔案了')
    with open('products2.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            s = line.strip().split(',')
            name = s[0]
            price = s[1]
            products.append([s[0] ,s[1]])
    print(products)
else:
    print('找不到檔案....')

#讓使用者輸入
while True :
    name =  input('請輸入商品名稱:')
    if name == 'q':
    	break
    price = input('請輸入商品價格:')
    price =int(price)
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是' ,p[1])

#寫入檔案
with open('products2.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')