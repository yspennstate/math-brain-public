#!/usr/bin/env python3
"""
T04 repair-menu certificate.

Majority assignment in proper iid random 3-SAT:
P,N iid Pois(mu), mu=3 alpha/2, Z=min(P,N), M=max(P,N),
q=EZ/(2mu).  A variable reached through a false occurrence has Palm
weight Z/EZ and break count B|P,N ~ Bin(M,q^2).

Depth-d repairability:
p_0=P(B=0); p_{d+1}=E[(2p_d-p_d^2)^B].
Writing y_d=1-p_d and r1=EB=mu*q/2 gives
  y_{d+1}=E[1-(1-q^2 y_d^2)^M] <= r1 y_d^2.
Hence if c=r1*y_0<1,
  y_d <= c^(2^d)/r1,
and an unsatisfied root clause (3 iid false-Palm candidates) has
no depth-d repair tree with probability <= y_d^3.

For the greedy min-break repair tree, nonroot offspring is
Y2=min(B1,B2), root offspring Y3=min(B1,B2,B3).
Thus r2=EY2=sum_t P(B>=t)^2 and r3=EY3=sum_t P(B>=t)^3.
If r2<1, expected tree size is 1+r3/(1-r2).

All finite Poisson sums use mpmath.iv.  The omitted size-biased mass and
tail moments are covered by Chernoff bounds as in the predecessor
majority-repair certificate.
"""
import mpmath as mp
mp.iv.dps = 60
iv = mp.iv

def certify(alpha_string, K=55):
    alpha = iv.mpf(alpha_string)
    mu = iv.mpf("1.5") * alpha

    pois = [iv.exp(-mu)]
    for k in range(K):
        pois.append(pois[-1] * mu / (k + 1))

    ez0 = iv.mpf("0")
    pairs = []
    for p in range(K + 1):
        for n in range(K + 1):
            z = min(p, n)
            if not z:
                continue
            m = max(p, n)
            wz = pois[p] * pois[n] * z
            ez0 += wz
            pairs.append((wz, m))

    # Poisson Chernoff tail P(Pois(mu)>=K).
    ch = iv.exp(-mu) * (iv.exp(iv.mpf("1")) * mu / K) ** K
    delta_z = 2 * mu * ch  # omitted E[Z] mass

    ez_lo = ez0.a
    ez_hi = (ez0 + delta_z).b
    mu_lo, mu_hi = mu.a, mu.b
    q_lo = ez_lo / (2 * mu_hi)
    q_hi = ez_hi / (2 * mu_lo)
    q = iv.mpf([q_lo, q_hi])
    r = q * q

    # Rigorous lower bound on p0=P_F(B=0): omitted numerator mass is >=0.
    num0 = iv.mpf("0")
    for wz, m in pairs:
        num0 += wz * (1 - r) ** m
    p0_lo = num0.a / ez_hi
    y0_hi = 1 - p0_lo

    r1 = mu * q / 2
    r1_hi = r1.b
    c_hi = r1_hi * y0_hi

    # Binomial survival tails for the truncated Palm mixture.
    tails_by_m = {}
    for m in range(K + 1):
        tails = [iv.mpf("0")] * (K + 1)
        if m:
            pmf = [iv.mpf("0")] * (m + 1)
            pmf[0] = (1 - r) ** m
            ratio = r / (1 - r)
            for k in range(m):
                pmf[k + 1] = pmf[k] * (m - k) / (k + 1) * ratio
            s = iv.mpf("0")
            for k in range(m, 0, -1):
                s += pmf[k]
                tails[k] = s
        tails_by_m[m] = tails

    r2_up = iv.mpf("0")
    r3_up = iv.mpf("0")
    for t in range(1, K + 1):
        num = iv.mpf("0")
        for wz, m in pairs:
            if m >= t:
                num += wz * tails_by_m[m][t]
        T_up = (num.b + delta_z.b) / ez_lo
        r2_up += T_up * T_up
        r3_up += T_up * T_up * T_up

    # For t>K, T_t^j <= T_t and sum_{t>K}T_t <=
    # E_F[B 1_{M>K}] <= delta_pm/EZ0.
    delta_pm = 2 * mu_hi * mu_hi * ch.b
    tail = delta_pm / ez_lo
    r2_up += tail
    r3_up += tail

    unsat = alpha * q * q * q
    root_size_up = 1 + r3_up / (1 - r2_up)
    load_up = unsat * root_size_up

    return {
        "q_lo": q_lo, "q_hi": q_hi,
        "p0_lo": p0_lo, "y0_hi": y0_hi,
        "r1_hi": r1_hi, "c_hi": c_hi,
        "r2_up": r2_up.b, "r3_up": r3_up.b,
        "unsat_up": unsat.b,
        "root_size_up": root_size_up.b,
        "load_up": load_up.b,
        "ch": ch.b, "delta_z": delta_z.b, "delta_pm": delta_pm,
    }

def sf(x):
    return float(x.mid)

def print_one(a):
    s = certify(a)
    print(f"alpha={a}")
    print("  q in [%.15f, %.15f]" % (sf(s["q_lo"]), sf(s["q_hi"])))
    print("  p0_false_Palm >= %.15f" % sf(s["p0_lo"]))
    print("  r1 <= %.15f" % sf(s["r1_hi"]))
    print("  c=r1*(1-p0) <= %.15f" % sf(s["c_hi"]))
    print("  quadratic_menu_certificate =", bool(s["c_hi"] < iv.mpf("1")))
    print("  r2 <= %.15f ; r3 <= %.15f" % (sf(s["r2_up"]), sf(s["r3_up"])))
    print("  E[root_tree_size] <= %.15f" % sf(s["root_size_up"]))
    print("  majority_unsat_density <= %.15f" % sf(s["unsat_up"]))
    print("  independent_tree_variable_load <= %.15f" % sf(s["load_up"]))
    print("  load_slack_certificate =", bool(s["load_up"] < iv.mpf("1")))
    print("  poisson_tail <= %.3e ; omitted_Z <= %.3e ; omitted_Bmoment <= %.3e"
          % (sf(s["ch"]), sf(s["delta_z"]), sf(s["delta_pm"])))
    if s["c_hi"] < iv.mpf("1"):
        r1 = s["r1_hi"]
        c = s["c_hi"]
        for d in range(0, 6):
            if d == 0:
                y = s["y0_hi"]
            else:
                y = c ** (2 ** d) / r1
            rf = y ** 3
            print("  depth=%d: variable_no_tree <= %.3e ; root_no_tree <= %.3e"
                  % (d, sf(y), sf(rf)))
    print()

if __name__ == "__main__":
    print("T04 REPAIR-MENU DOUBLE-EXPONENTIAL / LOAD-SLACK CERTIFICATE")
    print("K=55, mpmath.iv.dps=60")
    for a in ("3.52", "3.6", "4.0", "4.3911", "4.4898"):
        print_one(a)
