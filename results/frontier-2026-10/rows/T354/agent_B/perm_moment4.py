# T354: exact second and fourth moments of a linear permutation statistic (agent B, 20 Oct 2026).
# S = sum_q a_q z_pi(q), pi uniform on S_n, with sum a = sum z = 0. E S^k is a sum over set partitions tau of the k factors:
# (distinct-index sum of a^|B| over blocks) * (distinct-index sum of z^|B|) / (n)_|tau|, and a distinct-index sum is the
# Moebius sum over partitions of the blocks of products of power sums. Power sums with p1 = 0. Brute force check at n = 5, 6.
import itertools, math, random
import sympy as sp
from fractions import Fraction

def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p

def distinct_sum(exps, P):
    # sum over distinct i_1..i_k of prod x_{i_j}^{e_j}, in power sums P[e] (P[1] = 0)
    tot = 0
    for sig in set_partitions(list(range(len(exps)))):
        mu = 1
        term = 1
        for C in sig:
            mu *= (-1) ** (len(C) - 1) * math.factorial(len(C) - 1)
            term *= P[sum(exps[j] for j in C)]
        tot += mu * term
    return tot

def moment(k, n, A, Zp):
    tot = 0
    for tau in set_partitions(list(range(k))):
        exps = [len(B) for B in tau]
        ff = 1
        for i in range(len(tau)):
            ff *= (n - i)
        tot += distinct_sum(exps, A) * distinct_sum(exps, Zp) / ff
    return tot

n = sp.Symbol("n", positive=True)
A = {e: sp.Symbol("A%d" % e) for e in range(2, 5)}; A[1] = 0
Z = {e: sp.Symbol("P%d" % e) for e in range(2, 5)}; Z[1] = 0
M2 = sp.factor(sp.simplify(moment(2, n, A, Z)))
M4 = sp.simplify(moment(4, n, A, Z))
M3 = sp.factor(sp.simplify(moment(3, n, A, Z)))
print("E S^3 =", M3)
print("E S^2 =", M2)
print("E S^4 =", sp.collect(sp.expand(sp.numer(sp.together(M4))), [A[2] ** 2, A[4], A[3]]), "/", sp.factor(sp.denom(sp.together(M4))))

# brute force
random.seed(1)
for nn in (5, 6):
    a = [Fraction(random.randint(-5, 5)) for _ in range(nn)]; a = [x - sum(a) / nn for x in a]
    z = [Fraction(random.randint(-5, 5)) for _ in range(nn)]; z = [x - sum(z) / nn for x in z]
    for k in (2, 3, 4):
        bf = Fraction(0)
        for p in itertools.permutations(range(nn)):
            bf += sum(a[q] * z[p[q]] for q in range(nn)) ** k
        bf /= math.factorial(nn)
        Av = {e: sum(x ** e for x in a) for e in range(1, 5)}; Zv = {e: sum(x ** e for x in z) for e in range(1, 5)}
        Av[1] = 0; Zv[1] = 0
        val = moment(k, nn, Av, Zv)
        print("n", nn, "k", k, "brute", float(bf), "formula", float(val), "equal", bf == val)

# the bound: with P2 = n s2, P4 = n m4, |P3| <= sqrt(P2 P4), A3^2 <= A2 A4, worst-case ratio of E S^4 to (s2^2 A2^2 + m4 A4)
s2, m4 = sp.symbols("s2 m4", positive=True)
expr = M4.subs({Z[2]: n * s2, Z[4]: n * m4})
print("E S^4 with P2 = n s2, P4 = n m4:", sp.simplify(sp.expand(expr)))
