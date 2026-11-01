"""A cleaner form of the maximum-hitting-time identity for distance-regular graphs, and what it says
about Aldous and Fill's Open Problem 7.31.

From tau_0 = k * sum_i (k_i + ... + k_d)/(k_i c_i), put u_i = k/(k_i c_i) and T_i = k_i + ... + k_d.  Then
tau_0/n = sum_i u_i (T_i/n), and since k_{i+1} c_{i+1} = k_i b_i,

    u_1 = 1,      u_{i+1} = u_i * (c_i / b_i),      so      u_i = prod_{j<i} (c_j / b_j).

So

    tau_0 / n  =  sum_{i=1..d}  (T_i/n) * prod_{j<i} (c_j/b_j)   <=   sum_{i=1..d} prod_{j<i} (c_j/b_j).

The first term is exactly T_1/n = (n-1)/n, which is the universal lower bound again.  For the n-cycle
every ratio c_j/b_j is 1/1, so every u_i is 1 and the sum has d terms: that is precisely why the cycles
are excluded.  For every other distance-regular graph the question is whether those products are summable.
"""
from fractions import Fraction as F
from drg_hitting import tau0, multiplicities, DRG


def expansion(b, c):
    k = multiplicities(b, c)
    n = sum(k)
    d = len(b)
    u = [F(1)]
    for i in range(1, d):
        u.append(u[-1] * F(c[i - 1]) / F(b[i]))     # ratio is c_i/b_i: c[i-1] is c_i and b[i] is b_i
    T = [sum(k[i:]) for i in range(1, d + 1)]
    tot = sum(u[i] * T[i] for i in range(d))
    return tot / n, sum(u), [float(x) for x in u]


if __name__ == '__main__':
    print("check: the expansion must reproduce tau_0/n exactly, and sum u_i bounds it")
    print(f"{'graph':>16} {'tau_0/n':>10} {'expansion':>11} {'sum u_i':>9} {'agree':>6}")
    for name, b, c in DRG:
        t, n = tau0(b, c)
        e, su, u = expansion(b, c)
        print(f"{name:>16} {float(t/n):>10.4f} {float(e):>11.4f} {float(su):>9.4f} "
              f"{'yes' if e == t / n else 'NO':>6}")

    print("\nthe cycles, where the products do not decay (every c_j/b_j is 1):")
    for m in (10, 20, 40):
        d = m // 2
        b = [2] + [1] * (d - 1); c = [1] * (d - 1) + [2]
        e, su, u = expansion(b, c)
        print(f"   C_{m}: tau_0/n = {float(e):.3f}, sum u_i = {float(su):.1f}, "
              f"first few u_i = {[round(x,3) for x in u[:5]]}")

    print("\nclassical families, where they do decay:")
    def hamming(d, q): return [(d - i) * (q - 1) for i in range(d)], [i + 1 for i in range(d)]
    def johnson(N, K):
        d = min(K, N - K)
        return [(K - i) * (N - K - i) for i in range(d)], [(i + 1) ** 2 for i in range(d)]
    for nm, (b, c) in (("H(12,2)", hamming(12, 2)), ("H(12,4)", hamming(12, 4)),
                       ("J(30,15)", johnson(30, 15)), ("J(40,8)", johnson(40, 8))):
        e, su, u = expansion(b, c)
        print(f"   {nm:>9}: tau_0/n = {float(e):.4f}, sum u_i = {float(su):.4f}, "
              f"u_2 = {u[1]:.4g}, u_3 = {u[2]:.4g}")
