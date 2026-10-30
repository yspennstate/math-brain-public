#!/usr/bin/env python3
"""Exact sanity checks for B15 stop-loss / increasing-convex valuation order.

This checker is finite evidence only. The theorem in REPORT.md is analytic and
uses the proved all-cost valuation-tail majorization theorem.
"""
from collections import defaultdict
import json

def fwht(a):
    a = list(a)
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def v2(z):
    z = abs(int(z))
    assert z
    return (z & -z).bit_length() - 1

def analyze(vals):
    N = len(vals)
    n = N.bit_length() - 1
    den = N*N
    W = fwht(vals)

    packets = defaultdict(list)
    for s, w in enumerate(W):
        if w:
            packets[abs(w)].append((s, 1 if w > 0 else -1))

    rows = []
    for mag, entries in packets.items():
        eps = [0]*N
        for s, sign in entries:
            eps[s] = sign
        V = fwht(eps)
        r = min(v2(x) for x in V if x)
        mass_num = len(entries)*mag*mag
        rows.append((r, mass_num))

    assert sum(m for _, m in rows) == den

    qnums = []
    for i in range(n):
        jnum = sum(w*w for s, w in enumerate(W) if (s >> i) & 1)
        qnums.append(min(jnum, den-jnum))
    qdesc = sorted(qnums, reverse=True)

    # Stop-loss tails and packet-mass tails.
    stoploss = []
    for m in range(1, n+1):
        lhs = sum(mass*max(0, r-m+1) for r, mass in rows)
        rhs = 2*sum(qdesc[m-1:])
        assert lhs <= rhs, ("stoploss", n, m, lhs, rhs, rows, qdesc)
        mass_tail = sum(mass for r, mass in rows if r >= m)
        assert mass_tail <= rhs, ("mass_tail", n, m, mass_tail, rhs)
        stoploss.append((m, lhs, rhs, mass_tail))

    # Consequences for increasing convex test functions.
    # phi(r)=r^2, increments 2k-1.
    lhs2 = sum(mass*r*r for r, mass in rows)
    rhs2 = 2*sum((2*(k+1)-1)*qdesc[k] for k in range(n))
    assert lhs2 <= rhs2, ("quadratic", n, lhs2, rhs2)

    # phi(r)=2^r-1.
    lhse1 = sum(mass*((1 << r)-1) for r, mass in rows)
    rhse1 = 2*sum((1 << k)*qdesc[k] for k in range(n))
    assert lhse1 <= rhse1, ("exp1", n, lhse1, rhse1)

    # phi(r)=4^r-1: increments are 3*4^(k-1), hence factor 6 after tail payment.
    lhse2 = sum(mass*((4**r)-1) for r, mass in rows)
    rhse2 = 6*sum((4**k)*qdesc[k] for k in range(n))
    assert lhse2 <= rhse2, ("exp2", n, lhse2, rhse2)

    return {
        "n": n,
        "packet_count": len(rows),
        "max_r": max((r for r, _ in rows), default=0),
        "stoploss_checks": len(stoploss),
        "quadratic_check": True,
        "exp_base2_check": True,
        "exp_base4_check": True,
    }

def truth_table(mask, n):
    N = 1 << n
    return [1 if (mask >> x) & 1 else -1 for x in range(N)]

def main():
    totals = {
        "boolean_functions": 0,
        "stoploss_checks": 0,
        "quadratic_checks": 0,
        "exp_base2_checks": 0,
        "exp_base4_checks": 0,
        "max_packet_r_seen": 0,
    }
    by_n = {}
    for n in range(1, 5):
        cases = 1 << (1 << n)
        local_max_r = 0
        for mask in range(cases):
            rec = analyze(truth_table(mask, n))
            totals["boolean_functions"] += 1
            totals["stoploss_checks"] += rec["stoploss_checks"]
            totals["quadratic_checks"] += 1
            totals["exp_base2_checks"] += 1
            totals["exp_base4_checks"] += 1
            local_max_r = max(local_max_r, rec["max_r"])
        totals["max_packet_r_seen"] = max(totals["max_packet_r_seen"], local_max_r)
        by_n[str(n)] = {"functions": cases, "max_packet_r_seen": local_max_r}

    print(json.dumps({
        "status": "PASS",
        "scope": "exhaustive Boolean functions in dimensions 1 through 4; finite sanity check only",
        "by_dimension": by_n,
        "totals": totals,
        "checked_consequences": [
            "E[(r-m+1)_+] <= 2 sum_{k=m}^n q_k^down for every m",
            "Pr(r>=m) <= same RHS for every m",
            "E[r^2] <= 2 sum_k (2k-1) q_k^down",
            "E[2^r-1] <= 2 sum_k 2^(k-1) q_k^down",
            "E[4^r-1] <= 6 sum_k 4^(k-1) q_k^down",
        ],
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
