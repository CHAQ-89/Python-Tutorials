# Cong chuoi~ co them esscape squence \n
s = "Hello World!"
s1 = "\nI'm CHAQ"
s2 = s + s1
print(s2)
print("--------------------")

"""Chuoi~ tran`: them 'r' truoc chuoi~ 
 ta se dc 1 chuoi~ tran`"""
print(r"Toi la \nguoi Viet Nam")
print("----------------------")

# Kiem tra ky tu co nam trong chuoi~ hay khong
# Cac ky tu se duowc dem' tu 0 toi' n - 1
s3 = "Hello World!"
s4 = "\nI'm CHAQ"
# Toan' tu? 'in' se tra ve ket qua la TRUE or FALSE
s5 = s3 in s4
print(s5)
print("------------------------")

s6 = "Hello World!"
# Lay ra 1 ki tu trong chuoi
s7 = s6[0]
print(s7)
# Lay vi tri cuoi cung trong chuoi
print(s6[len(s6) - 1])
# Cat chuoi
print(s6[0:6])
""" Thay doi ky tu trong chuoi, 
 voi 1 la vi tri cua ky tu can thay the"""
s8 = s6.replace("o","0",1)
print(s8)
""" Cat chuoi~ = toan tu? 'None'
 Neu None o vi tri tiep theo thi chuoi 
 se duoc cat tu trai qua phai """
print(s6[3:None])

# Neu None o vi tri dau tien se tinh la vi tri 0
print(s6[None:3])

""" Cat theo buoc nhay voi 0: vi tri bat dau, 
 7: vi tri ket thuc, 2: buoc nhay"""
print(s6[0:7:2])


