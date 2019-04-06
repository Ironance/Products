#read the file
products = []
with open('products.csv', 'r') as f:
    for line in f:
        if 'product,price' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name,price])
print(products)

#user input
while True:
    name = input('Please input the product: ')
    if name =='q':
        break
    price = input('Please input the price: ')
    products.append([name, price])
print(products)

#print the log
for p in products:
    print('The price of', p[0], 'is', p[1])

#write into file
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('product, price\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

