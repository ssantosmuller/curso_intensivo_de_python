numbers = list(range(1,10))
print(numbers)

for number in numbers:
    if number == 1:
        print(number,"st",end=" ")
    elif number == 2:
        print(number,"nd",end=" ")
    elif number == 3:
        print(number,"rd",end=" ")
    else:
        print(number,"th",end=" ")