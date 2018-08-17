def calc_exp(num, exp):
    if exp == 1:
        return str(num)
    else:
        return str(num**exp) + str(calc_exp(num, exp-1))

#print(calc_exp(10, 10))
print(calc_exp(3,3))


