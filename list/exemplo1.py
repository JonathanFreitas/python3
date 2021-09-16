print(type([]))

list1 = [1, 2, 3, 4, 5, 6, 7]

list2 = ['S', 'C', 'H', 'O', 'O', 'L']

list3 = []

list4 = list(range(11))

list5 = list('University')

if 8 in list4:
	print('found number 8')
else:
	print('not found number 8')

list6 = [9, 8, 7, 6, 5, 4, 3, 2]
list6.sort()
print(list6)

list7 = list('Geek University')
print(list7.count('e'))

"""
add element in list, using the function append
"""
print(list1)
list1.append(8)
print(list1)
