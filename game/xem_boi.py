
def xem_boi(a, b):
    a = a.lower()
    b = b.lower()
    count = 0
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) in a and chr(i) in b:
            count += 1
        if count >= 3:
            result = 'Hop nhau'
        elif 0 < count < 3:
            result = 'Lam ban'
        else:
            result = 'Khong hop'
    return result

if __name__ == '__main__':
    a = input('Nhap ten A: ')
    b = input('Nhap ten B: ')
    result = xem_boi(a, b)
    print(result)