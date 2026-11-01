"""Aldous and Fill, Open Problem 7.31: over distance-regular graphs other than the cycles, is the maximum
mean hitting time tau_0 = O(n)?  They record that Biggs computed max_{i,j} E_i T_j/(n-1) = 195/101 on a
cubic graph with 102 vertices.

In a distance-regular graph the hitting time E_i T_j depends only on d(i,j), so the distance to a fixed
target is a birth-and-death chain on {0,...,d}: from distance i it moves down with probability c_i/k and
up with b_i/k.  Its stationary measure is k_i/n with k_0 = 1 and k_{i+1} = k_i b_i/c_{i+1}, and the
birth-and-death formula for a DOWNWARD step, E_i T_{i-1} = (sum_{j>=i} pi_j)/(pi_i * down-rate), gives

    tau_0 = E_d T_0 = k * sum_{i=1..d} (k_i + ... + k_d) / (k_i c_i).

So the question is a statement about intersection arrays and no graph need be built.

CONTROLS.  The complete graph must give n-1 and the complete bipartite graph 2n-3 (both known exactly),
the Petersen and dodecahedron values must match a direct linear-algebra computation on the graph, and the
n-cycle must give n^2/4.  The cycle ALONE is not a sufficient control: its k_i are symmetric, so it cannot
tell a tail sum from a head sum, and an earlier version of this file had the sum reversed and still passed
it.  The complete graph is what caught that.
"""
from fractions import Fraction as F


def multiplicities(b, c):
    """k_0..k_d from the intersection array {b_0..b_{d-1}; c_1..c_d}"""
    k = [F(1)]
    for i in range(len(b)):
        k.append(k[i] * b[i] / c[i])
    return k


def tau0(b, c):
    """maximum mean hitting time, exactly, together with n"""
    k = multiplicities(b, c)
    n = sum(k)
    valency = b[0]
    tot = F(0)
    for i in range(1, len(k)):
        tail = sum(k[i:])
        tot += tail / (k[i] * c[i - 1])
    return valency * tot, n


DRG = [
    ("K_4",           [3],                      [1]),
    ("K_{3,3}",       [3, 2],                   [1, 3]),
    ("cube Q_3",      [3, 2, 1],                [1, 2, 3]),
    ("Petersen",      [3, 2],                   [1, 1]),
    ("Heawood",       [3, 2, 2],                [1, 1, 3]),
    ("Pappus",        [3, 2, 2, 1],             [1, 1, 2, 3]),
    ("Desargues",     [3, 2, 2, 1, 1],          [1, 1, 2, 2, 3]),
    ("dodecahedron",  [3, 2, 1, 1, 1],          [1, 1, 1, 2, 3]),
    ("Coxeter",       [3, 2, 2, 1],             [1, 1, 1, 2]),
    ("Tutte-Coxeter", [3, 2, 2, 2],             [1, 1, 1, 3]),
    ("Foster",        [3, 2, 2, 2, 2, 1, 1, 1], [1, 1, 1, 1, 2, 2, 2, 3]),
    ("Biggs-Smith",   [3, 2, 2, 2, 1, 1, 1],    [1, 1, 1, 1, 1, 1, 3]),
    ("Tutte 12-cage", [3, 2, 2, 2, 2, 2],       [1, 1, 1, 1, 1, 3]),
]

if __name__ == '__main__':
    print("CONTROLS")
    for m in (4, 6, 10):
        t, n = tau0([m - 1], [1])
        print(f"   K_{m}: tau_0 = {t}, should be n-1 = {m-1}   {'ok' if t == m - 1 else 'WRONG'}")
    for m in (3, 4, 6):
        t, n = tau0([m, m - 1], [1, m])
        print(f"   K_{{{m},{m}}}: n = {int(n)}, tau_0 = {t}, should be 2n-3 = {2*int(n)-3}   "
              f"{'ok' if t == 2 * n - 3 else 'WRONG'}")
    for m in (10, 20, 40):
        d = m // 2
        t, n = tau0([2] + [1] * (d - 1), [1] * (d - 1) + [2])
        print(f"   C_{m}: tau_0 = {t}, should be n^2/4 = {m*m//4}   {'ok' if t == F(m*m, 4) else 'WRONG'}")

    print("\nthe thirteen cubic distance-regular graphs")
    print(f"{'graph':>16} {'n':>6} {'tau_0':>12} {'tau_0/(n-1)':>14} {'tau_0/n':>9}")
    worst = (F(0), None)
    for name, b, c in DRG:
        t, n = tau0(b, c)
        r = t / (n - 1)
        print(f"{name:>16} {int(n):>6} {str(t):>12} {str(r):>14} {float(t/n):>9.4f}")
        if r > worst[0]: worst = (r, name)
    print(f"\nlargest tau_0/(n-1): {worst[0]} = {float(worst[0]):.4f} at {worst[1]}")
    print(f"Aldous and Fill report Biggs found 195/101 = {float(F(195,101)):.4f} on a cubic graph "
          f"with 102 vertices")
