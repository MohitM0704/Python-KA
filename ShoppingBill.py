
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Main program
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculate individual amounts
electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

# Calculate total, discount, and final bill
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

# Display the bill
print("Electronics after GST: ₹{:.2f}".format(electronics))
print("Fashion after GST: ₹{:.2f}".format(fashion))
print("Food after GST: ₹{:.2f}".format(food))
print("--------------------------------")
print("Total after GST: ₹{:.2f}".format(total))
print("Discount (20%): ₹{:.2f}".format(discount))
print("Final payable amount: ₹{:.2f}".format(final_amount))
