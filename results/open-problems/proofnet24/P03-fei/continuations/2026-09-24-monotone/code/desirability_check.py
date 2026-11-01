# Checks the remark of Section 3.2: in G = F_3(Maj_3(w^1), Maj_3(w^2), Maj_3(w^3), z) no leaf is at least as desirable
# as z (so z is maximal), while in F_3 itself every y_j is at least as desirable as z (so z is minimal there).
n, k = 3, 3
ystar = [1] * ((n - 1) // 2) + [0] * ((n + 1) // 2)
def F(y, z):
    return int(sum(y) > n // 2 or (z == 1 and list(y) == ystar))
def G(v):
    y = [int(sum(v[j * k:(j + 1) * k]) > k // 2) for j in range(n)]
    return F(y, v[n * k])
def at_least_as_desirable(fun, nv, a, b):
    """a >= b: fun(x with a=1,b=0) >= fun(x with a=0,b=1) for every x."""
    for x in range(1 << nv):
        v = [(x >> t) & 1 for t in range(nv)]
        u1 = list(v); u1[a], u1[b] = 1, 0
        u2 = list(v); u2[a], u2[b] = 0, 1
        if fun(u1) < fun(u2):
            return False
    return True
Fv = lambda v: F(v[:n], v[n])
print('F_3: y_j >= z for every j:', all(at_least_as_desirable(Fv, n + 1, j, n) for j in range(n)))
print('F_3: z >= y_j for some j :', any(at_least_as_desirable(Fv, n + 1, n, j) for j in range(n)))
nv = n * k + 1
print('G  : some leaf w >= z     :', any(at_least_as_desirable(G, nv, w, n * k) for w in range(n * k)))
print('G  : z >= some leaf w     :', any(at_least_as_desirable(G, nv, n * k, w) for w in range(n * k)))
