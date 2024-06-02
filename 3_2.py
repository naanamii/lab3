str_old = str(input("Please input string: "))
str_new = ''
for i in range(len(str_old)):
    if not str_old[i].isdigit():
        count = ''
        j = i + 1
        while j < len(str_old) and str_old[j].isdigit():
            count += str(str_old[j])
            j += 1
        if count == '': count = 1
        if not (str_old[i] in str_new):
            str_new += (str_old[i]*int(count))
print(str_new)
