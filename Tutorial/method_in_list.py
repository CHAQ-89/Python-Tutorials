
s = 'quyetmoihocpython'
print(s.capitalize())
print(s.center(20,'-'))
print(s.count('t', 1, 7))
s1 = s.encode()
print(s1)
print(s1.decode())
print(s.endswith('h', 0, 9))
print(s.find('o', 0, 5))
print(s.index('py'))
s3 = '-'
s4 = '---quyet---'
print(s3.join(s4))
print(s4.rstrip('-'))
print(s4.split('q'))

# Lay 1 ki tu trong chuoi
a = 'quyet'
b = ' '
c = b.join(a).split()
#print(c)
#c.insert(1, 'a')
#print(c)
#print(c[0])
c.sort(reverse = False)
print(c)

# def custom_sort(elem):
# 	return elem[1]
lis = [(1, 2), (5, 7), (7, 100), (4, 4)]
lis.sort()
print(lis)

# Ham an danh

# lam = lambda x, y: x + y
# print(lam(1, 2))

# Ham map
def mutiply(x):
	return x * 2
lis_1 = [1, 2, 3, 4, 5]
result = map(mutiply, lis_1)
# Ham map tra ve result la class 'map'
print(type(result))
# Ep result ve dang 'list'
print(list(result))	

# Ap dung ham an danh 'lambda'

result_1 = map(lambda x: x * x, lis_1)
print(list(result_1))
# map voi 2 list truyen vao

lis_2 = ['quyet', 'hello']
lis_3 = ['hihi','world']
result_2 = map(lambda a, b: a + ' ' + b, lis_2, lis_3)
print(list(result_2))

# ham filter

lis_4 = [i for i in range(1, 19)]
# loc cac ket qua khong chia het cho 2 va chia het cho 2
res = filter(lambda x: x % 2, lis_4)
res_1 = filter(lambda x: x % 2 == 0, lis_4)

print(list(res))
print(list(res_1))