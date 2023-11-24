def larger_root(p, q):
    ll = list()
    dis = p ** 2 - 4 * q
    cor1 = (-p - (dis ** 0.5)) / 2
    ll.append(cor1)
    cor2 = (-p + (dis ** 0.5)) / 2
    ll.append(cor2)
    ll.sort()
    return ll[0]


def smaller_root(p, q):
    ll = list()
    dis = p ** 2 - 4 * q
    cor1 = (-p - (dis ** 0.5)) / 2
    ll.append(cor1)
    cor2 = (-p + (dis ** 0.5)) / 2
    ll.append(cor2)
    ll.sort()
    return ll[1]


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    p = float(input())
    q = float(input())
    print(p ** 2 - 4 * q)
    print(larger_root(p, q), smaller_root(p, q))

main()