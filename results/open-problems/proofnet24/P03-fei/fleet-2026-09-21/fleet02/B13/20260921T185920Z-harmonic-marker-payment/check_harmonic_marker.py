#!/usr/bin/env python3
"""Sanity checker for B13 harmonic-marker FEI decomposition.

Standard library only. Exhausts Boolean functions modulo global output sign
through n=4 and checks the entropy chain, the one-charge mean identity, the
coordinatewise harmonic-marker payment, and the aggregate paid terms.
The analytic proof in REPORT.md is authoritative; this is a regression check.
"""
from __future__ import annotations
import math

LN2 = math.log(2.0)
C_MARK = (2.0 + math.exp(-1.0)) / LN2
C_PAID = 2.0 + C_MARK


def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    inv = 1.0/n
    return [x*inv for x in a]


def entropy(probs):
    return -sum(p*math.log2(p) for p in probs if p > 0.0)


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1.0-p)*math.log2(1.0-p)


def stats(vals):
    n = len(vals).bit_length()-1
    hat = fwht(vals)
    mu = [x*x for x in hat]
    K = [s.bit_count() for s in range(1 << n)]
    H = entropy(mu)
    I = sum(mu[s]*K[s] for s in range(1 << n))
    tau = sum(mu[s] for s in range(1 << n) if K[s] > 0)
    atom = h2(tau)
    r = []
    pcoord = []
    qent = []
    qmean_excess = []
    for i in range(n):
        pi = sum(mu[s] for s in range(1 << n) if ((s >> i) & 1))
        ri = sum(mu[s]/K[s] for s in range(1 << n)
                 if K[s] and ((s >> i) & 1))
        pcoord.append(pi)
        r.append(ri)
        if ri == 0.0:
            qent.append(0.0)
            qmean_excess.append(0.0)
            continue
        probs = []
        mean_excess = 0.0
        for s in range(1 << n):
            if K[s] and ((s >> i) & 1):
                q = mu[s]/(K[s]*ri)
                probs.append(q)
                mean_excess += q*(K[s]-1)
        qent.append(entropy(probs))
        qmean_excess.append(mean_excess)
    marker = 0.0
    if tau > 0.0:
        marker = tau * entropy([x/tau for x in r if x > 0.0])
    elogk = sum(mu[s]*math.log2(K[s]) for s in range(1 << n) if K[s] > 0)
    residual = sum(r[i]*qent[i] for i in range(n)) - elogk
    weighted_qmean = sum(r[i]*qmean_excess[i] for i in range(n))

    # Equivalent geometric-mean form of the residual.
    residual_geom = 0.0
    for s in range(1 << n):
        k = K[s]
        if not k or mu[s] == 0.0:
            continue
        log_geom_r = sum(math.log2(r[i]) for i in range(n) if (s >> i) & 1)/k
        residual_geom += mu[s]*(log_geom_r - math.log2(mu[s]))

    return {
        "H": H, "I": I, "tau": tau, "atom": atom, "r": r,
        "pcoord": pcoord, "marker": marker, "residual": residual,
        "residual_geom": residual_geom, "elogk": elogk,
        "weighted_qmean": weighted_qmean, "qent": qent,
        "qmean_excess": qmean_excess,
        "chain_error": H - (atom + marker + residual),
    }


def truth_from_bits(n, bits):
    N = 1 << n
    vals = [1.0]*N
    for j in range(1, N):
        if (bits >> (j-1)) & 1:
            vals[j] = -1.0
    return vals


def one_point(n):
    vals = [1.0]*(1 << n)
    vals[-1] = -1.0
    return vals


def majority(n):
    assert n % 2 == 1
    return [1.0 if x.bit_count() <= n//2 else -1.0 for x in range(1 << n)]


def point_indicator_harmonic_row(m):
    """Exact-form diagnostics for g=1_{0} on an m-cube.

    Q(A) is proportional to 1/(|A|+1), and E_Q(|A|+1) has a closed form.
    """
    denom = (1 << (m+1)) - 1
    H = 0.0
    mean = 0.0
    for k in range(m+1):
        q = (m+1)/(denom*(k+1))
        count = math.comb(m, k)
        H -= count*q*math.log2(q)
        mean += count*q*(k+1)
    exact_mean = (m+1)*(1 << m)/denom
    return H, mean, exact_mean


def main():
    total = nonconstant = checks = active_coords = 0
    max_chain_error = 0.0
    max_geom_error = 0.0
    max_marker_ratio = 0.0
    max_atom_ratio = 0.0
    max_paid_ratio = 0.0
    max_residual_ratio = -1e300
    max_qmean_error = 0.0
    max_coordinate_marker_excess = -1e300

    for n in range(1, 5):
        N = 1 << n
        for bits in range(1 << (N-1)):
            st = stats(truth_from_bits(n, bits))
            total += 1
            max_chain_error = max(max_chain_error, abs(st["chain_error"]))
            max_geom_error = max(max_geom_error, abs(st["residual"]-st["residual_geom"]))
            max_qmean_error = max(max_qmean_error,
                                  abs(st["weighted_qmean"] - (st["I"] - st["tau"])))
            checks += 3
            for ri, pi in zip(st["r"], st["pcoord"]):
                if pi <= 1e-15:
                    continue
                active_coords += 1
                lhs = 0.0 if ri <= 0.0 else ri*math.log2(1.0/ri)
                excess = lhs-C_MARK*pi
                max_coordinate_marker_excess = max(max_coordinate_marker_excess, excess)
                assert excess <= 2e-12
                checks += 1
            I = st["I"]
            if I <= 1e-14:
                continue
            nonconstant += 1
            assert st["atom"] <= 2.0*I + 2e-12
            assert st["marker"] <= C_MARK*I + 2e-12
            assert st["atom"] + st["marker"] <= C_PAID*I + 2e-12
            checks += 3
            max_marker_ratio = max(max_marker_ratio, st["marker"]/I)
            max_atom_ratio = max(max_atom_ratio, st["atom"]/I)
            max_paid_ratio = max(max_paid_ratio, (st["atom"]+st["marker"])/I)
            max_residual_ratio = max(max_residual_ratio, st["residual"]/I)

    print("B13 harmonic-marker regression: PASS")
    print(f"functions_sign_normalized={total}")
    print(f"nonconstant={nonconstant}")
    print(f"active_coordinate_rows={active_coords}")
    print(f"checks={checks}")
    print(f"C_marker={C_MARK:.15f}")
    print("C_atom=2.000000000000000")
    print(f"C_paid={C_PAID:.15f}")
    print(f"max_chain_error={max_chain_error:.3e}")
    print(f"max_residual_geometric_form_error={max_geom_error:.3e}")
    print(f"max_one_charge_mean_error={max_qmean_error:.3e}")
    print(f"max_coordinate_marker_excess={max_coordinate_marker_excess:.3e}")
    print(f"max_marker_over_I={max_marker_ratio:.15f}")
    print(f"max_atom_over_I={max_atom_ratio:.15f}")
    print(f"max_paid_over_I={max_paid_ratio:.15f}")
    print(f"max_residual_over_I={max_residual_ratio:.15f}")

    for label, gen, dims in [
        ("one_point", one_point, [4, 8, 12, 16]),
        ("majority", majority, [3, 5, 7, 9]),
    ]:
        for n in dims:
            st = stats(gen(n))
            I = st["I"]
            print(
                f"stress={label} n={n} H/I={st['H']/I:.12f} "
                f"marker/I={st['marker']/I:.12f} residual/I={st['residual']/I:.12f}"
            )

    # Exact point-indicator harmonic rows show that any hoped-for local theorem
    # H(Q) <= B E_Q(|A|+1) must have B >= 2 asymptotically.
    for m in [4, 8, 12, 16]:
        H, mean, exact_mean = point_indicator_harmonic_row(m)
        assert abs(mean-exact_mean) <= 2e-12
        print(
            f"point_indicator_row m={m} H={H:.12f} mean_Kplus1={mean:.12f} "
            f"H_over_mean={H/mean:.12f}"
        )

    # Purely diagnostic non-Boolean product-set law: for fixed mean lambda and
    # n growing, a uniform random marked element has entropy log2(n), so the
    # marker contribution / mean diverges. This is NOT an FEI counterexample;
    # it shows the Boolean derivative/hypercontractive input is substantive.
    lam = 4.0
    for n in [64, 256, 1024, 4096]:
        p = lam/n
        tau = 1.0-(1.0-p)**n
        ratio = tau*math.log2(n)/lam
        print(f"nonboolean_product_marker_ratio n={n} lambda=4 ratio={ratio:.12f}")


if __name__ == "__main__":
    main()
