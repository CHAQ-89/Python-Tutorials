""" 
SO SÁNH PHẦN TỬ TRONG NHIỀU LIST
Nhập vào 2 list số nguyên, so sánh các phần tử của 2 list theo cặp thứ tự index
 """


def compareTriplets(a, b):
    c = 0
    d = 0
    result = []
    for i, j in zip(a, b):
        if i > j:
            c += 1
        elif i < j:
            d += 1
    result.extend([c, d])
    return result


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = compareTriplets(a, b)
    print(result)
