# a = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

# # Loại bỏ các số 11
# b = [i for i in a if i!=11]

# # Lưu lại các vị trí của số 11
# c = [i for i in range(len(a)) if a[i]==11]   # vị trí của các số 11: 2,6,7,10

# # Sắp xếp lại list đã bỏ 11 theo thứ từ từ bé đến lớn
# b.sort()

# # Dùng phương thức insert của list với các vị trí của số 11 đã lưu
# for j in c:
#     b.insert(j,11)
# print(b)

# Sort voi List Compre

# if __name__ == '__main__':
#     a= []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         a.append([score, name])

#     a.sort()
#     b = [i for i in a if i[0] != a[0][0]]
#     c = [j for j in b if j[0] == b[0][0]]
    
#     c.sort(key=lambda x: x[1])
#     for i in range(len(c)):
#         print(c[i][1])


# SORT VOI DICT

# score_list = {}
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     if score in score_list:
#         score_list[score].append(name)
#     else:
#         score_list[score] = [name]
# print(score_list)
# new_list = []
# for i in score_list:
#     new_list.append([i, score_list[i]])
# print(new_list)
# new_list.sort()
# print(new_list)
# result = new_list[1][1]
# print(result)
# result.sort()
# print (*result, sep = "\n")        

# SORT VOI DICT

d={} #1
for _ in range(int(input())): #2
    Name= input() #3
    Grade= float(input()) #4
    d[Name] = Grade #5
v=d.values()#6
second = sorted(list(set(v)))[1] #7
second_lowest = [] #8
for key,value in d.items():  #9
    if value == second: #10
        second_lowest.append(key) #11
second_lowest.sort() #12
for name in second_lowest: #13
    print(name) #14

# 1) Empty dictionary.

# 2) Range for number of students.

# 3) Accepting name of the student.

# 4) Accepting the grade of the student.

# 5) Assigning name as key and grade as value for the dictionary.

# 6) Obtaining the values of dictionary(all grades of students.

# 7) Remoing duplicte grades by using set data type , changing it to list, sorting in ascending order and taking the second lowest grade.

# 8) Declaring an empty list for storing the name of the students who got the second lowest grade.

# 9) Going through the name and grade of each students by using items() method of dictionary.

# 10) Checking whether the grade is equal to the second lowest grade.

# 11) If yes , append it to the second_lowest list.

# 12) bSorting the name of students in asceding order

# 13) Going through the name of each students who got the second lowes grade.

# 14) Printing each name of students in seperate line.