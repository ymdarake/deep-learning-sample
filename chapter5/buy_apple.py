import layer_naive as lay

apple_unit_price = 100
apple_count = 2
tax = 1.1

mul_apple_layer = lay.MullLayer()
mul_tax_layer = lay.MullLayer()

# forward
price = mul_apple_layer.forward(apple_unit_price, apple_count)
tax_included_price = mul_tax_layer.forward(price, tax)

print(tax_included_price)

# backward
d_price = 1
d_apple_price, d_tax = mul_tax_layer.backward(d_price)
d_apple_unit_price, d_apple_num = mul_apple_layer.backward(d_apple_price)

print(d_apple_unit_price, d_apple_num, d_tax)
