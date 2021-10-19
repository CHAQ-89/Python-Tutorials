from functools import reduce


def main():

    n = int(input())
    d = {}
    for _ in range(n):
        name, *line = input().split()
        score = list(map(float, line))
        d[name] = score
    query_name = input()
    print(d)
    print(query_name)
    value_list = []
    for key, value in d.items():
        if key == query_name:
            value_list.extend(value)

    print(value_list)

    print(format(reduce(lambda a, b: a+b, value_list) / len(value_list), '.2f'))


if __name__ == '__main__':
    main()
