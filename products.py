products = []

while True:
    name = input('Please input the product: ')
    if name =='q':
        break
    price = input('Please input the price: ')
    products.append([name, price])
print(products)

for p in products:
    print('The price of', p[0], 'is', p[1])


with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('product, 價錢\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

