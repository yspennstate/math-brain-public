"""How large can sum_i prod_{j<i} (c_j/b_j) be over feasible intersection arrays?

That sum bounds tau_0/n, so Aldous and Fill's Open Problem 7.31 follows for any class where it is bounded.
The cycles, which the problem excludes, have every ratio equal to 1 and the sum equal to 2d.
"""
from fractions import Fraction as F
import sys
from drg_feasible import enumerate_arrays
from drg_hitting import multiplicities

def sum_u(b, c):
    u = [F(1)]
    for i in range(1, len(b)):
        u.append(u[-1] * F(c[i - 1]) / F(b[i]))
    return sum(u), u

if __name__ == '__main__':
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    print(f"{'k':>3} {'d':>3} {'feasible':>9} {'max sum u_i':>12} {'at array':>40}")
    grand = (0.0, None)
    for k in range(3, kmax + 1):
        for d in range(1, dmax + 1):
            res = enumerate_arrays(k, d)
            if not res: continue
            best = (0.0, None)
            for r, n, b, c in res:
                s, u = sum_u(list(b), list(c))
                if float(s) > best[0]: best = (float(s), (b, c, n))
            b, c, n = best[1]
            print(f"{k:>3} {d:>3} {len(res):>9} {best[0]:>12.4f}   "
                  f"{{{','.join(map(str,b))};{','.join(map(str,c))}}}", flush=True)
            if best[0] > grand[0]: grand = (best[0], best[1])
    print(f"\nlargest sum u_i over feasible arrays of valency 3..{kmax}, diameter to {dmax}: {grand[0]:.4f}")
    b, c, n = grand[1]
    print(f"   n = {n}, array {{{','.join(map(str,b))};{','.join(map(str,c))}}}")
