products = []

while True:
    name = input('Please input the product: ')
    if name =='q':
        break
    price = input('Please input the price: ')
    # # p = []
    # # p.append(name)
    # # p.append(price)
    # p = [name, price]
    products.append([name, price])
print(products)

products[0][0]