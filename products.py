import os

#read the file
def read_file(filename):
    products = []
    if os.path.isfile(filename):  #check if the file is exist
        print('File is found!')
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if 'product,price' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name,price])
        print(products)
    else:
        print('File is not found ...')
    return products

#user input
def user_input(products):
    while True:
        name = input('Please input the product: ')
        if name =='q':
            break
        price = input('Please input the price: ')
        products.append([name, price])
    print(products)
    return products

#print the log
def print_products(products):
    for p in products:
        print('The price of', p[0], 'is', p[1])

#write into file
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('product,price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)

