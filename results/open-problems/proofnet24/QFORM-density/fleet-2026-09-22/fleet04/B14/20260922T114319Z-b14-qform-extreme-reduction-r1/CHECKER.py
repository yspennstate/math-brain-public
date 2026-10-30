from fractions import Fraction
from itertools import product, combinations


def dot(g, f):
    return sum(a*b for a, b in zip(g, f))


def bathtub(g, k):
    idx = sorted(range(len(g)), key=lambda i: g[i], reverse=True)[:k]
    return tuple(Fraction(int(i in idx)) for i in range(len(g)))


def grid_densities(m, k, den=4):
    # finite hypersimplex mesh: 0<=f_i<=1 and sum f_i=k
    vals = [Fraction(j, den) for j in range(den+1)]
    for f in product(vals, repeat=m):
        if sum(f) == k:
            yield f


def check_one_coordinate():
    m, k = 6, 3
    kernels = [
        tuple(Fraction((7*i*i + 3*i + s) % 19, 19) for i in range(m))
        for s in range(11)
    ]
    for g in kernels:
        top = dot(g, bathtub(g, k))
        mesh = max(dot(g, f) for f in grid_densities(m, k))
        assert top == mesh


def check_two_coordinate_replacement():
    m, k = 5, 2
    for seed in range(7):
        G = [[Fraction((11*i + 17*j + 5*i*j + seed) % 23, 23)
              for j in range(m)] for i in range(m)]
        f = tuple(Fraction(x, 4) for x in (4, 2, 1, 1, 0))
        h = tuple(Fraction(x, 4) for x in (3, 3, 1, 1, 0))
        assert sum(f) == k and sum(h) == k
        old = sum(G[i][j]*f[i]*h[j] for i in range(m) for j in range(m))
        gi = tuple(sum(G[i][j]*h[j] for j in range(m)) for i in range(m))
        e = bathtub(gi, k)
        mid = sum(G[i][j]*e[i]*h[j] for i in range(m) for j in range(m))
        gj = tuple(sum(G[i][j]*e[i] for i in range(m)) for j in range(m))
        d = bathtub(gj, k)
        new = sum(G[i][j]*e[i]*d[j] for i in range(m) for j in range(m))
        assert old <= mid <= new


def check_product_tv():
    # exact finite analogue of TV(product)<=sum TV(marginals)
    p = [(Fraction(1,2), Fraction(1,2)), (Fraction(1,3), Fraction(2,3))]
    q = [(Fraction(2,3), Fraction(1,3)), (Fraction(1,4), Fraction(3,4))]
    def tv(a,b): return sum(abs(x-y) for x,y in zip(a,b))/2
    P = [p[0][i]*p[1][j] for i,j in product(range(2), repeat=2)]
    Q = [q[0][i]*q[1][j] for i,j in product(range(2), repeat=2)]
    assert tv(P,Q) <= tv(p[0],q[0]) + tv(p[1],q[1])


if __name__ == "__main__":
    check_one_coordinate()
    check_two_coordinate_replacement()
    check_product_tv()
    print("STATUS=PASS")
    print("finite_bathtub_kernels=11")
    print("two_coordinate_kernels=7")
    print("product_tv_exact=PASS")
