def calculatetotalbillamt(bill,tip_perc):
    tip_amount = bill * (tip_perc / 100)
    total_bill = bill + tip_amount
    return total_bill

print("Total bill amount is: ", calculatetotalbillamt(100, 15))