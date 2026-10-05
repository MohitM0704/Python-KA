cost_price = int(input("Enter cost price: "))
sell_price = int(input("Enter sell price: "))

if sell_price > cost_price:
    profit = sell_price - cost_price
    print("Profit: ", profit)

elif cost_price > sell_price:
    loss = cost_price - sell_price
    print("Loss: ", loss)

else:
    print("No profit : No loss")