r"""Optimal online value of the prophet secretary instance I(k, m) of the paper.

Instance I(k, m): k prizes worth 1 with probability q each; m items worth B1 = b1 k q with probability p1/m each;
m items worth B2 = b2 k q with probability p2/m each; one item worth A = a k q with probability 1.  The items arrive
in uniformly random order and the gambler knows every law.  The optimal value satisfies
V(S) = (1/|S|) sum_{i in S} E max(X_i, V(S - i)),  V(empty) = 0.

usage
  python ps_check.py brute k m        full DP over all 2^n subsets of items and the count DP, both in floats
  python ps_check.py float k m        count DP in floats
  python ps_check.py iv k m prec      count DP in interval arithmetic (mpmath.iv, prec bits); prints an enclosure
                                      of V / E max
The environment variable PS_Q overrides q (default 1e-9).
"""
import json
import os
import sys
import time

PAR = ("0.823", "1.28233", "0.2065", "1.38487", "0.17698")   # a, b1, p1, b2, p2
QS = os.environ.get("PS_Q", "1e-9")


def items(k, m, num):
    a, b1, p1, b2, p2 = (num(s) for s in PAR)
    q = num(QS)
    out = [(num(1), q)] * k
    out += [(b1 * k * q, p1 / m)] * m
    out += [(b2 * k * q, p2 / m)] * m
    out += [(a * k * q, num(1))]
    return out


def emax(its):
    """E max of independent variables equal to v with probability p and to 0 otherwise."""
    its = sorted(its, key=lambda t: -t[0])
    surv, e = 1, 0
    for v, p in its:
        e += surv * p * v
        surv *= 1 - p
    return e


def brute(k, m):
    its = items(k, m, float)
    n = len(its)
    V = [0.0] * (1 << n)
    for S in range(1, 1 << n):
        t, c, x = 0.0, 0, S
        while x:
            low = x & -x
            i = low.bit_length() - 1
            v = V[S ^ low]
            val, p = its[i]
            t += p * max(val, v) + (1 - p) * v
            c += 1
            x ^= low
        V[S] = t / c
    return V[-1], emax(its)


def count_dp(k, m, num, mx):
    """V over states (j prizes, l1 and l2 medium items of each kind, s sure items left)."""
    a, b1, p1, b2, p2 = (num(s) for s in PAR)
    q = num(QS)
    one, zero = num(1), num(0)
    A, B1, B2 = a * k * q, b1 * k * q, b2 * k * q
    r1, r2 = p1 / m, p2 / m
    prev = None
    for j in range(k + 1):
        cur = {}
        for s in (0, 1):
            for l1 in range(m + 1):
                for l2 in range(m + 1):
                    n = j + l1 + l2 + s
                    if n == 0:
                        cur[s, l1, l2] = zero
                        continue
                    t = zero
                    if s:
                        t = t + mx(A, cur[0, l1, l2])
                    if l2:
                        v = cur[s, l1, l2 - 1]
                        t = t + l2 * (r2 * mx(B2, v) + (one - r2) * v)
                    if l1:
                        v = cur[s, l1 - 1, l2]
                        t = t + l1 * (r1 * mx(B1, v) + (one - r1) * v)
                    if j:
                        v = prev[s, l1, l2]
                        t = t + j * (q * mx(one, v) + (one - q) * v)
                    cur[s, l1, l2] = t / n
        prev = cur
    return prev[1, m, m], emax(items(k, m, num))


def main():
    mode, k, m = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    t0 = time.time()
    if mode == "brute":
        vb, eb = brute(k, m)
        vs, es = count_dp(k, m, float, max)
        print(json.dumps({"k": k, "m": m, "q": QS, "subset_dp": vb / eb, "count_dp": vs / es,
                          "diff": vb / eb - vs / es, "sec": round(time.time() - t0, 1)}))
    elif mode == "float":
        v, e = count_dp(k, m, float, max)
        print(json.dumps({"k": k, "m": m, "q": QS, "ratio": v / e, "sec": round(time.time() - t0, 1)}))
    elif mode == "iv":
        from mpmath import iv
        iv.prec = int(sys.argv[4])

        def ivmax(x, y):
            return iv.mpf([max(x.a, y.a), max(x.b, y.b)])
        v, e = count_dp(k, m, iv.mpf, ivmax)
        print(json.dumps({"k": k, "m": m, "q": QS, "prec": iv.prec, "V": [str(v.a), str(v.b)],
                          "Emax": [str(e.a), str(e.b)], "ratio_lo": str(v.a / e.b), "ratio_hi": str(v.b / e.a),
                          "sec": round(time.time() - t0, 1)}))


main()
