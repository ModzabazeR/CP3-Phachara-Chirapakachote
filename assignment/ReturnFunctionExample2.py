def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result


print(vatCalculate(float(input("Enter total price : "))), "THB")
