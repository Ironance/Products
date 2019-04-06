#read the file
products = [['product', 'price']]
with open('products.csv', 'r') as f:
    for line in f:
        name, price = line.strip().split(',')
        if name != 'product':
            products.append([name,price])

print(products)

while True:
    name = input('Please input the product: ')
    if name =='q':
        break
    price = input('Please input the price: ')
    products.append([name, price])
print(products)

for p in products:
    if p[0] != 'product':
        print('The price of', p[0], 'is', p[1])


with open('products.csv', 'w', encoding='utf-8') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

