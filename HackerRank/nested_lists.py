if __name__ == '__main__':
    student = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name] = score
    v = student.values()
    print(list(set(v)))
    second = sorted(list(set(v)))[1]
    print(second)
    sco_sorted = []
    for key, value in student.items():
        if value == second:
            sco_sorted.append(key)
    sco_sorted.sort()
    print(sco_sorted)
    for name_ in sco_sorted:
        print(name_)
   
    #     student.append([name, score])
    # student.sort()
    # print(student)
    
    # n = []
    # sco = []
    # for a in student:
    #     for b in a:
    #         n.append(a[0])
    #         sco.append(a[1])
    #         break
    # print(n)
    # print(sco)
    
    # sco_1 = filter(lambda x: x > min(sco), sco)
    # sco_1 = list(sco_1)
    # # print(sco_1)
    # sco_2 = [i for i in sco_1 if i == min(sco_1)]
    # print(sco_2)
    # for x,y in zip(n, sco):
    #     print(x,y)

