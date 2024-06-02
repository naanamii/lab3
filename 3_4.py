array = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
dictionary = {i:array.count(i) for i in array}
print(*list(dictionary.values()))
