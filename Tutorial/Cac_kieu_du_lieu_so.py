
#SO THUC

#Khai bao bien f va gan cho f gia tri la 10 chia 3
f = 10/3
#In bien f ra man hinh
print(f)
#In kieu du lieu cua bien f
print(type(f))
print("---------------------------")

#SO DECIMAL

#Lay toan bo noi dung cua thu vien decimal
from decimal import*

#Ham lay so chu so phan nguyen va thap phan
#Co the dung hoac khong vi ham 'Decimal' mac dinh lay 30 so sau phan thap phan'
getcontext().prec = 30

#Khai bao 1 bien dec va gan cho no gia tri dat trong ham 'Decimal'
dec = Decimal(10)/3
print(dec)
print(type(dec))
print("-----------------------------")

# PHAN SO

#Lay noi dung cua thu vien fractions
from fractions import*
#Ham Fraction() voi 3 la tu so, 6 la mau so
frac = Fraction(3,6)
print(frac)
print(type(frac))
print("------------------------------")

#SO PHUC

#Ham 'complex()' la ham so thuc
c = complex(3,4)
print(c)
#in ra phan thuc
print(c.real)
#in ra phan ao
print(c.imag)
print("------------------------------")

#BIEU THUC TOAN HOC CUA DU LIEU SO

#Phep tinh lay phan thuong nguyen
a = 3//4
print(a)
#Phep tinh lay phan du
b = 3%4
print(b)
#Luy thua 4 cua 3
c = 3**4
print(c)