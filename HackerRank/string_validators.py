
def myfunct(s, k):
    s = s.upper()
    s1 = list(s)
    n = int(len(s1)/k)
    for i in range(len(s1)):
        # print(i)
        if i == n:
            n += i + 1
            s1.insert(i, '@')
    s1 = ''.join(s1)
    s1 = s1.split('@')
    #s1 = ','.join(s1)
    # print(s1)
    s2 = ''
    for j in range(n):
        t = s1[j]
        print(t)

        for a in t:
            if a not in s2:
                s2 += a
    # a = list(set(j))
    # b = ''.join(a)
    # print(b)
    print(s2)


if __name__ == '__main__':
    s = input()
    k = int(input())
    myfunct(s, k)


# S, N = input(), int(input())
# for part in zip(*[iter(S)] * N):
#     d = dict()
#     print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

# s = input()
# k = int(input())
# num_subsegments = int(len(s) / k)

# for index in range(num_subsegments):
#     # Subsegment string
#     t = s[index * k : (index + 1) * k]
#     print(t)
#     # Subsequence string having distinct characters
#     u = ""

#     # If a character is not already in 'u', append
#     for c in t:
#         if c not in u:
#             u += c

#     # Print final converted string
#     print(u)
