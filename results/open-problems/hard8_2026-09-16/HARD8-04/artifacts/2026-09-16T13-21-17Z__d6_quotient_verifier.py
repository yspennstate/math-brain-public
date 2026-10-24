from math import isqrt

SPECIAL = {
    1: ((0,0,0,1,0,1),(0,0,0,1,1,1),(0,0,1,0,1,1),(0,0,1,0,1,1)),
    2: ((0,0,0,2,1,2),(0,0,2,0,2,2),(1,1,1,1,1,1),(1,1,1,1,1,1)),
    3: ((0,0,1,3,1,3),(0,2,2,1,2,2),(1,1,1,2,2,2),(1,1,2,1,2,2)),
    4: ((0,0,2,3,2,4),(0,2,2,2,2,4),(2,2,2,2,2,2),(2,2,2,2,2,2)),
    6: ((0,1,3,4,3,6),(2,3,3,3,3,4),(2,3,3,4,3,3),(2,3,4,2,4,3)),
    8: ((0,2,4,5,4,8),(3,4,4,4,5,4),(3,4,4,4,5,4),(4,4,4,4,4,4)),
    9: ((0,3,5,5,5,8),(3,4,4,5,5,6),(3,4,5,5,5,5),(4,5,4,5,4,5)),
    11: ((0,4,6,7,6,9),(4,5,6,5,6,7),(5,5,6,5,6,6),(5,5,6,5,6,6)),
    13: ((0,6,7,7,9,9),(5,7,6,7,6,8),(5,7,6,7,7,7),(6,7,6,7,6,7)),
    23: ((9,11,12,7,13,16),(12,13,16,9,11,8),(10,11,13,11,13,11),(10,11,10,15,11,12)),
    25: ((13,10,10,13,15,13),(11,12,9,14,17,12),(12,11,17,12,11,12),(16,8,13,14,14,10)),
    35: ((18,15,26,18,12,15),(17,19,16,16,17,20),(17,14,21,15,20,18),(17,19,19,16,16,18)),
    42: ((21,21,21,25,18,19),(24,20,24,21,19,18),(21,11,24,24,23,23),(23,21,21,21,23,17)),
}

SIMPLE = {
    10:(5,0,0,6), 12:(-1,6,0,6), 14:(-7,0,0,6), 16:(5,6,0,6),
    18:(-1,6,6,6), 22:(5,6,6,6), 24:(-1,0,0,12), 28:(5,0,0,12),
    30:(-1,6,0,12), 34:(5,6,0,12), 36:(-1,6,6,12), 40:(5,6,6,12),
    46:(-13,6,6,6), 48:(17,0,0,0), 52:(5,12,0,12), 54:(17,0,0,6),
    58:(5,0,0,18), 64:(5,6,0,18), 70:(5,6,6,18), 76:(5,12,12,12),
    82:(5,12,0,18),
}

EVEN_FIN = {2,4,6,8,10,12,14,16,18,22,24,28,30,34,36,40,42,46,48,52,54,58,64,70,76,82}
ODD_FIN = {1,3,9,11,13,23,25,35}


def block(N, a):
    assert (N-a) % 6 == 0
    b = (N-a)//6
    return (b+a,b,b,b,b,b)


def qenergy(v, a):
    return sum((v[i]-v[(i+a)%6])**2 for i in range(6))//2


def forbidden_three_square(n):
    if n < 0:
        return True
    if n == 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n % 8 == 7


def three_square(n):
    assert n >= 0 and not forbidden_three_square(n)
    limit = isqrt(n)
    square_root = {i*i:i for i in range(limit+1)}
    for x in range(limit+1):
        rem1 = n-x*x
        for y in range(isqrt(rem1)+1):
            z = square_root.get(rem1-y*y)
            if z is not None:
                return x,y,z
    raise AssertionError(("missing three-square representation", n))


def triangular_three(L):
    ys = three_square(8*L+3)
    assert all(y % 2 == 1 for y in ys)
    xs = tuple((abs(y)-1)//2 for y in ys)
    assert sum(x*(x+1)//2 for x in xs) == L
    return xs


def certificate(s):
    if s in SPECIAL:
        return SPECIAL[s]

    if s in SIMPLE:
        a = SIMPLE[s]
        return (block(3*s-1,a[0]),) + tuple(block(3*s,x) for x in a[1:])

    if s % 2 == 0:
        t = s//2
        if t % 3 == 0:
            u = t//3
            candidates = [(3,u-8),(-3,u-10)]
        elif t % 3 == 1:
            u = (t-1)//3
            candidates = [(-1,u-1),(2,u-3)]
        else:
            u = (t-2)//3
            candidates = [(1,u),(4,u-14)]

        choice = None
        for k,R in candidates:
            if R >= 0 and not forbidden_three_square(R):
                choice = (k,R)
                break
        assert choice is not None, (s,t,candidates)
        k,R = choice
        xs = three_square(R)
        a = (6*k-1,) + tuple(6*x for x in xs)
        return (block(3*s-1,a[0]),) + tuple(block(3*s,x) for x in a[1:])

    t = (s-1)//2
    k = {0:2,1:1,2:0,3:-1,4:-2,5:-3}[t % 6]
    B = 3*k*k+2*k+2
    assert t >= B, (s,t,k,B)
    L = (t-B)//6
    xs = triangular_three(L)
    a = (6*k+2,) + tuple(6*x+3 for x in xs)
    return (block(3*s-1,a[0]),) + tuple(block(3*s,x) for x in a[1:])


def verify(s, cert):
    assert len(cert) == 4
    assert all(len(v) == 6 for v in cert)
    assert sum(cert[0]) == 3*s-1
    assert all(sum(v) == 3*s for v in cert[1:])
    assert all(0 <= x <= s for v in cert for x in v)

    target = 6*s+1
    energy = [sum(qenergy(v,a) for v in cert) for a in (1,2,3)]
    assert energy == [target,target,target], (s,energy,cert)

    autocorr = []
    for a in range(6):
        autocorr.append(sum(sum(v[i]*v[(i+a)%6] for i in range(6)) for v in cert))
    assert autocorr[0] == 6*s*s+4*s+1, (s,autocorr)
    assert autocorr[1:] == [6*s*s-2*s]*5, (s,autocorr)


assert EVEN_FIN == set(SIMPLE) | {2,4,6,8,42}
assert ODD_FIN == {1,3,9,11,13,23,25,35}
assert (EVEN_FIN | ODD_FIN) == (set(SIMPLE) | set(SPECIAL))

for s in sorted(EVEN_FIN | ODD_FIN):
    verify(s, certificate(s))
print("BASE_CERTIFICATES_VERIFIED", len(EVEN_FIN | ODD_FIN))
print("DIRECT_BASE_CERTIFICATES", len(SPECIAL))
print("ONE_EXCEPTION_BASE_CERTIFICATES", len(SIMPLE))

MAX_S = 5000
for s in range(1, MAX_S+1):
    verify(s, certificate(s))
print("D6_QUOTIENT_CERTIFICATES_VERIFIED", MAX_S)
print("FINITE_RANGE", f"s=1..{MAX_S}", f"v=6..{6*MAX_S}")
print("ALL_EXACT_D6_CHECKS_PASSED")
