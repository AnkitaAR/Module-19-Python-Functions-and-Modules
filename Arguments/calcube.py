def cube(num):
    return num*num*num

def isdivisibleby3(num):
    if num % 3 == 0:
       cube(num)
       print("Cube of", num, "is", cube(num))
    else:
        print("Not divisible by 3")
        return False
    
isdivisibleby3(9)
isdivisibleby3(10)