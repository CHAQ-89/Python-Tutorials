
'''
USE LAMBDA

'''
'''
Use Lambda (or List Comprehsion) for map, filter and reduce fuction
'''
# list_1 = ['quyet', 'khoai', 'giang']
# print(list(map(lambda x: x.title(), list_1)))

'''
Use List Comprehesion
'''
# new_list = [i.title() for i in list_1]
# print(new_list)

'''
For Filter function
'''
#list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda x: x % 2 == 0, list_2)))
'''
Use List Comprehesion
'''
# new_list = [x for x in list_2 if x % 2 == 0]
# print(new_list)
'''
For Reduce function
"Lambda function in reduce() takes 2 arguments"
'''
# from functools import reduce
# list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(reduce(lambda a, b: a + b, list_3))
# print(reduce(lambda a, b: a if a > b else b, list_3))

