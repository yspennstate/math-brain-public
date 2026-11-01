#!/usr/bin/env python3
import math

EPS = 1.0/16.0
ADDRESS_C = 19.0/4.0
H13 = -(1.0/3.0)*math.log2(1.0/3.0) -(2.0/3.0)*math.log2(2.0/3.0)
NULL_C = (2.0 + 1.0/math.e)*math.log2(math.e)
ROBUST_C = ADDRESS_C + H13
TOL = 3e-11


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


def entropy(weights):
    s = sum(weights)
    if s <= 0:
        return 0.0
    out = 0.0
    for x in weights:
        if x > 0:
            p = x/s
            out -= p*math.log2(p)
    return out


def tv_to_uniform_subcube(nu, F, allowed_mask):
    m = F.bit_count()
    q = 1.0/(1 << m)
    tv = 0.0
    sub = allowed_mask
    seen = []
    while True:
        seen.append(sub)
        if sub == 0:
            break
        sub = (sub-1) & allowed_mask
    for b in seen:
        target = q if (b & ~F) == 0 else 0.0
        tv += abs(nu.get(b, 0.0)-target)
    return 0.5*tv


def analyze_n(n):
    N = 1 << n
    masks = list(range(N))
    pop = [x.bit_count() for x in masks]
    factorial_log = [math.lgamma(k+1)/math.log(2) for k in range(n+1)]
    functions = 0
    nonconstant = 0
    row_checks = 0
    address_checks = 0
    robust_pairs = 0
    violations = []
    max_null_ratio = 0.0
    max_selector_ratio = 0.0
    max_address_excess = -1e100
    max_robust_excess = -1e100
    max_exception_fraction = 0.0
    min_nonnull_fraction = 1.0

    # Quotient global sign: fix truth[0]=+1.
    for bits in range(1 << (N-1)):
        vals = [1]
        for x in range(1, N):
            vals.append(1 if ((bits >> (x-1)) & 1) == 0 else -1)
        W = fwht(vals)
        mu0 = [(w/N)**2 for w in W]

        # Minimizing-character / folded gauge.
        toggle = 0
        for i in range(n):
            inf = sum(mu0[s] for s in masks if (s >> i) & 1)
            if inf > 0.5 + 1e-14:
                toggle |= 1 << i
        mu = [mu0[s ^ toggle] for s in masks]

        functions += 1
        V = 1.0 - mu[0]
        js = [sum(mu[s] for s in masks if (s >> i) & 1) for i in range(n)]
        I = sum(js)
        if I <= 1e-15:
            continue
        nonconstant += 1

        u = [0.0]*n
        Q = [0.0]*n
        r = [[0.0]*n for _ in range(n)]
        for s, mass in enumerate(mu):
            k = pop[s]
            if k == 0 or mass == 0:
                continue
            invk = 1.0/k
            qshare = factorial_log[k]*invk
            members = [i for i in range(n) if (s >> i) & 1]
            for i in members:
                u[i] += mass*invk
                Q[i] += mass*qshare
            for i in members:
                for j in members:
                    if i != j:
                        r[i][j] += mass*invk

        if abs(sum(u)-V) > 1e-10:
            violations.append(("u_sum", bits, sum(u), V))
        for j in range(n):
            if abs(u[j] + sum(r[j][i] for i in range(n) if i != j) - js[j]) > 1e-10:
                violations.append(("row_sum", bits, j))

        for j in range(n):
            if js[j] > 1e-15:
                L = math.log2(1.0/js[j])
                rhs = 2.0*math.log2(math.e)*js[j]
                if u[j]*L > rhs + TOL:
                    violations.append(("selector", bits, j, u[j]*L, rhs))
                if rhs > 0:
                    max_selector_ratio = max(max_selector_ratio, u[j]*L/rhs)

        nullH = V*entropy(u) if V > 0 else 0.0
        rhs_null = NULL_C*I
        if nullH > rhs_null + TOL:
            violations.append(("null", bits, nullH, rhs_null))
        if rhs_null > 0:
            max_null_ratio = max(max_null_ratio, nullH/rhs_null)

        for j in range(n):
            jj = js[j]
            if jj <= 1e-15:
                continue
            row_checks += 1
            allowed = ((1 << n)-1) ^ (1 << j)
            nu = {}
            for b in masks:
                if (b >> j) & 1:
                    continue
                nu[b] = mu[b | (1 << j)]/jj

            for m in range(1, n):
                if abs((2.0**(-m))-jj) <= EPS*jj + 1e-14:
                    lhs = jj*math.log2(m+1)
                    rhs = Q[j] + ADDRESS_C*jj
                    address_checks += 1
                    ex = lhs-rhs
                    max_address_excess = max(max_address_excess, ex)
                    if ex > TOL:
                        violations.append(("address", bits, j, m, lhs, rhs))

            sub = allowed
            while True:
                if sub.bit_count() >= 1:
                    Fm = sub
                    m = Fm.bit_count()
                    if abs((2.0**(-m))-jj) <= EPS*jj + 1e-14:
                        eps = tv_to_uniform_subcube(nu, Fm, allowed)
                        if eps <= EPS + 1e-12:
                            robust_pairs += 1
                            denom = jj-u[j]
                            e = sum(r[j][i] for i in range(n) if i != j and ((Fm >> i) & 1) == 0)
                            if e > eps*jj + 1e-10:
                                violations.append(("exception_mass", bits, j, Fm, e, eps*jj))
                            lower = (0.25-eps)*jj
                            if denom + 1e-10 < lower:
                                violations.append(("nonnull_mass", bits, j, Fm, denom, lower))
                            max_exception_fraction = max(max_exception_fraction, e/jj)
                            min_nonnull_fraction = min(min_nonnull_fraction, denom/jj)
                            nonnullH = denom*entropy([r[j][i] for i in range(n) if i != j]) if denom > 0 else 0.0
                            exc_weights = [r[j][i] for i in range(n) if i != j and ((Fm >> i) & 1) == 0]
                            excH = e*entropy(exc_weights) if e > 0 else 0.0
                            rhs = Q[j] + ROBUST_C*jj + excH
                            ex = nonnullH-rhs
                            max_robust_excess = max(max_robust_excess, ex)
                            if ex > TOL:
                                violations.append(("robust_code", bits, j, Fm, nonnullH, rhs, e, eps))
                if sub == 0:
                    break
                sub = (sub-1) & allowed

    return {
        "n": n,
        "functions": functions,
        "nonconstant": nonconstant,
        "row_checks": row_checks,
        "address_checks": address_checks,
        "robust_row_F_checks": robust_pairs,
        "violations": violations,
        "max_null_ratio": max_null_ratio,
        "max_selector_ratio": max_selector_ratio,
        "max_address_excess": max_address_excess if address_checks else None,
        "max_robust_excess": max_robust_excess if robust_pairs else None,
        "max_exception_fraction": max_exception_fraction,
        "min_nonnull_fraction": min_nonnull_fraction if robust_pairs else None,
    }


def main():
    print(f"constants NULL_C={NULL_C:.15f} ADDRESS_C={ADDRESS_C:.15f} ROBUST_C={ROBUST_C:.15f}")
    totals = {"functions":0,"nonconstant":0,"row_checks":0,"address_checks":0,"robust_row_F_checks":0,"violations":0}
    global_max_null=0.0
    global_max_selector=0.0
    global_max_addr=-1e100
    global_max_rob=-1e100
    global_max_exc=0.0
    global_min_non=1.0
    for n in range(1,5):
        out=analyze_n(n)
        print(out)
        for k in ["functions","nonconstant","row_checks","address_checks","robust_row_F_checks"]:
            totals[k]+=out[k]
        totals["violations"]+=len(out["violations"])
        global_max_null=max(global_max_null,out["max_null_ratio"])
        global_max_selector=max(global_max_selector,out["max_selector_ratio"])
        if out["max_address_excess"] is not None:
            global_max_addr=max(global_max_addr,out["max_address_excess"])
        if out["max_robust_excess"] is not None:
            global_max_rob=max(global_max_rob,out["max_robust_excess"])
        global_max_exc=max(global_max_exc,out["max_exception_fraction"])
        if out["min_nonnull_fraction"] is not None:
            global_min_non=min(global_min_non,out["min_nonnull_fraction"])
        if out["violations"]:
            print("FIRST VIOLATIONS", out["violations"][:5])
    print("TOTALS",totals)
    print("GLOBAL max_null_ratio",global_max_null)
    print("GLOBAL max_selector_ratio",global_max_selector)
    print("GLOBAL max_address_excess",global_max_addr)
    print("GLOBAL max_robust_excess",global_max_rob)
    print("GLOBAL max_exception_fraction",global_max_exc)
    print("GLOBAL min_nonnull_fraction",global_min_non)
    if totals["violations"]:
        raise SystemExit(1)
    print("PASS")

if __name__=="__main__":
    main()
