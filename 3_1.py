str_old = str(input("Please input string: "))
str_new = ''
for i in range(len(str_old)):
    symbol = str_old[i]
    count = str_old.count(symbol)
    if not(symbol+str(count) in str_new):
        str_new += symbol
        if count != 1:
            str_new += str(count)
print(str_new)
