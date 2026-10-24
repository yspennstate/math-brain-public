#!/usr/bin/env python3
"""Finite numerical checks of the report's analytic theorems; not a proof certificate."""
import json
import math
import random
from decimal import Decimal, localcontext
from functools import lru_cache
from pathlib import Path

TOL = 2e-9
metrics = {"functions": 0, "local_checks": 0, "tree_checks": 0,
           "max_signed_identity_error": 0.0, "max_js_split_error": 0.0,
           "max_six_term_identity_error": 0.0, "max_tree_identity_error": 0.0,
           "minimum_phase_refund_margin": 0.0,
           "maximum_credit_generation_fraction_of_phase": 0.0}

def entropy(p):
    return -sum(x * math.log2(x) for x in p if x > 0)

def h(p):
    p = min(1.0, max(0.0, p))
    return entropy((p, 1-p))

def kl(p, q):
    result = 0.0
    for x, y in zip(p, q):
        if x > 1e-15:
            if y <= 0:
                raise AssertionError(("KL support mismatch", x, y, p, q))
            result += x * math.log2(x/y)
    return result

def berkl(p, q):
    p = min(1.0, max(0.0, p)); q = min(1.0, max(0.0, q))
    return kl((p, 1-p), (q, 1-q))

def js(p, q, w=.5):
    mix = [(1-w)*x+w*y for x, y in zip(p, q)]
    return entropy(mix)-(1-w)*entropy(p)-w*entropy(q)

def phase_j(t):
    return 1-h(.5+math.sqrt(max(0.0, t*(1-t))))

def walsh(values):
    a = list(values); width = 1
    while width < len(a):
        for start in range(0, len(a), 2*width):
            for i in range(start, start+width):
                u, v = a[i], a[i+width]
                a[i], a[i+width] = u+v, u-v
        width *= 2
    return a

def projection(P, n):
    """P on masks including an empty zero; returns exact moment I-projection numerically."""
    r = [sum(P[k] for k in range(1, len(P)) if k >> i & 1) for i in range(n)]
    mu = sum(r)
    if mu <= 1+1e-12:
        q = [0.0]*len(P)
        for i, x in enumerate(r): q[1 << i] = x
        return q
    if any(x >= 1-1e-14 for x in r):
        zeta = 1.0
    else:
        lo, hi = 0.0, 1.0
        for _ in range(90):
            mid = (lo+hi)/2
            # (1-product(1-mid*r_i))/mid is evaluated without cancellation.
            g = -math.expm1(sum(math.log1p(-mid*x) for x in r))/mid - 1
            if g > 0: lo = mid
            else: hi = mid
        zeta = (lo+hi)/2
    t = [min(1.0, max(0.0, zeta*x)) for x in r]
    q = [0.0]*len(P)
    for mask in range(1, len(P)):
        q[mask] = math.prod(t[i] if mask >> i & 1 else 1-t[i] for i in range(n))
    total = sum(q)
    assert total > 0
    return [x/total for x in q]

@lru_cache(maxsize=30000)
def state(values):
    n = (len(values)-1).bit_length()
    raw = walsh(values)
    U = [(x/len(values))**2 for x in raw]
    v = sum(U[1:])
    I = [sum(U[k] for k in range(len(U)) if k >> i & 1) for i in range(n)]
    P = [x/v if v else 0.0 for x in U]; P[0] = 0.0
    Q = projection(P, n) if v else [0.0]*len(U)
    credit = v*kl(P,Q) if v else 0.0
    phase = sum(phase_j(x) for x in I)
    return {"n": n, "U": U, "v": v, "P": P, "Q": Q, "I": I,
            "C": credit, "phase": phase, "H": entropy(U)}

def restrict(values, i, b):
    return tuple(value for k, value in enumerate(values) if ((k >> i) & 1) == b)

def delete_bit(mask, i):
    return (mask & ((1 << i)-1)) | ((mask >> (i+1)) << i)

def close(name, error):
    metrics[name] = max(metrics[name], abs(error))
    assert abs(error) < TOL, (name, error)

def local(values, i):
    f = state(values)
    child_values = (restrict(values, i, 0), restrict(values, i, 1))
    a, b = (state(x) for x in child_values)
    xi = f["C"]-.5*(a["C"]+b["C"])
    js_full = js(a["U"], b["U"])
    phase_drop = f["phase"]-.5*(a["phase"]+b["phase"])
    refund = phase_drop-js_full
    terms = [0.0]*4
    M = .5*(a["v"]+b["v"])
    js_nonempty = 0.0
    variance_js = js((a["v"],1-a["v"]), (b["v"],1-b["v"]))
    if M > 0:
        weights = (.5*a["v"]/M, .5*b["v"]/M)
        Pmix = [weights[0]*x+weights[1]*y for x,y in zip(a["P"],b["P"])]
        qs = [0.0]*len(Pmix)
        numerator_theta = 0.0
        for mask, mass in enumerate(f["Q"]):
            residual = delete_bit(mask, i)
            if residual:
                qs[residual] += mass
                if mask >> i & 1: numerator_theta += mass
        qm = sum(qs)
        assert qm > 0
        qs = [x/qm for x in qs]
        theta = numerator_theta/qm
        singleton = f["U"][1 << i]
        sigma = f["Q"][1 << i]
        rho = (f["I"][i]-singleton)/M
        terms[0] = f["v"]*berkl(singleton/f["v"], sigma)
        terms[1] = M*berkl(rho, theta)
        cond_entropy = 0.0
        for oldmask in range(1, len(Pmix)):
            # Insert a zero selector bit into the residual mask.
            mask0 = (oldmask & ((1 << i)-1)) | ((oldmask >> i) << (i+1))
            m0, m1 = f["U"][mask0], f["U"][mask0 | (1 << i)]
            if m0+m1: cond_entropy += (m0+m1)*h(m1/(m0+m1))
        terms[2] = M*h(rho)-cond_entropy
        terms[3] = M*sum(w*kl(c["Q"],qs) for w,c in zip(weights,(a,b)) if w)
        js_nonempty = M*(entropy(Pmix)-sum(w*entropy(c["P"]) for w,c in zip(weights,(a,b))))
    close("max_signed_identity_error", xi-(sum(terms)-js_nonempty))
    close("max_js_split_error", js_full-(variance_js+js_nonempty))
    six = sum(terms)+variance_js+refund
    close("max_six_term_identity_error", xi+phase_drop-six)
    assert min(terms+[variance_js,refund]) >= -TOL
    assert max(0,-xi) <= js_nonempty+TOL <= js_full+2*TOL
    d = f["I"][i]
    var_packet = 0.0
    raw0, raw1 = walsh(child_values[0]), walsh(child_values[1])
    for u0,u1 in zip(raw0,raw1):
        u0 /= len(raw0); u1 /= len(raw1)
        e = (u0*u0+u1*u1)/2
        if e:
            posterior = (u0-u1)**2/(4*e)
            var_packet += e*(posterior-d)**2
    variation = sum((x-y)**2 for x,y in zip(a["I"],b["I"]))
    lower = 2/(3*math.log(2))*var_packet+1/(6*math.log(2))*variation
    metrics["minimum_phase_refund_margin"] = min(metrics["minimum_phase_refund_margin"], refund-lower)
    assert refund+TOL >= lower
    metrics["local_checks"] += 1
    return child_values, {"N": max(0,-xi), "positive": max(0,xi),
                          "Q": js_full, "refund": refund, "six": six, "I": d}

def tree(values):
    n = (len(values)-1).bit_length()
    if n == 0: return {k:0.0 for k in ("N","positive","Q","refund","six","I")}
    # Genuine deterministic adaptive selection: subsequent indices depend on child values.
    i = abs(sum((k+1)*x for k,x in enumerate(values))) % n
    children, totals = local(values,i)
    for child in children:
        below = tree(child)
        for k in totals: totals[k] += .5*below[k]
    return totals

def check_function(values, do_tree=True):
    f = state(values)
    for i in range(f["n"]): local(values,i)
    if do_tree:
        t = tree(values)
        close("max_tree_identity_error", t["positive"]-t["N"]-f["C"])
        close("max_tree_identity_error", t["Q"]+t["refund"]-f["phase"])
        close("max_tree_identity_error", t["six"]-f["C"]-f["phase"])
        close("max_tree_identity_error", t["I"]-sum(f["I"]))
        assert t["N"] <= f["phase"]-t["refund"]+TOL
        if f["phase"] > 1e-12:
            metrics["maximum_credit_generation_fraction_of_phase"] = max(
                metrics["maximum_credit_generation_fraction_of_phase"], t["N"]/f["phase"])
        metrics["tree_checks"] += 1
    metrics["functions"] += 1

def reserve_check():
    with localcontext() as ctx:
        ctx.prec = 160
        c, lam = Decimal(7), Decimal("0.1")
        log2 = Decimal(2).ln()
        def a_norm(m):
            if m == 0: return Decimal(0)
            p = Decimal(2)**(1-m)
            if m == 1: return c
            hm = -(1-p)**2*2*(1-p).ln()/log2+(2*p-p*p)*(2*m-2)
            hp = -p*p.ln()/log2-(1-p)*(1-p).ln()/log2
            return c*m-(1-lam)*hm/p-lam*m*hp/p
        n = 100
        values = [a_norm(m) for m in range(n+1)]
        gaps = [values[n]-values[r] for r in range(n)]
        assert max(gaps) < 0
        # This directly checks all old-only blocks; the y-containing statement
        # is analytic and explicitly conditional on the potential's AND validity.
        return {"center":str(c),"lambda":str(lam),"old_dimension":n,
                "decimal_precision":ctx.prec,"root_augmented_defect_divided_by_p":str(values[n]),
                "largest_normalized_old_block_drift":str(max(gaps)),
                "all_old_only_root_blocks_strictly_fail":True,
                "y_containing_blocks":"analytic under stated AND-child admissibility; no unchosen potential tested"}

def main():
    for n in range(4):
        for code in range(1 << (1 << n)):
            values = tuple(-1 if code >> k & 1 else 1 for k in range(1 << n))
            check_function(values)
    rng = random.Random(20260922)
    for n, count in ((4,700),(5,180),(6,30)):
        for _ in range(count):
            check_function(tuple(rng.choice((-1,1)) for _ in range(1 << n)))
        # Constants, all characters, one-point defects, and their suspensions.
        for mask in range(1 << n):
            check_function(tuple(-1 if (k & mask).bit_count()%2 else 1 for k in range(1 << n)), False)
        check_function(tuple(-1 if k == 0 else 1 for k in range(1 << n)))
        check_function(tuple((-1 if k & 1 else 1)*(-1 if k >> 1 == 0 else 1) for k in range(1 << n)))
    def majority3(bits):
        return 1 if sum(1 if bits >> i & 1 else -1 for i in range(3)) > 0 else -1
    recursive_majority2 = tuple(1 if sum(majority3(k >> (3*j)) for j in range(3)) > 0 else -1
                                for k in range(1 << 9))
    check_function(recursive_majority2)
    rm = state(recursive_majority2)
    assert abs(rm["H"]-5) < TOL
    assert abs(sum(rm["I"])-2.25) < TOL
    assert all(abs(x-.25) < TOL for x in rm["I"])
    metrics["recursive_majority_depth2"] = {"entropy":rm["H"],"influence":sum(rm["I"]),
                                            "credit":rm["C"],"truth_table_checked":True}
    metrics["reserve_obstruction"] = reserve_check()
    metrics["status"] = "PASS"
    metrics["scope"] = "Numerical finite checks of genuine Boolean spectra; analytic proofs are in REPORT.md."
    out = Path(__file__).with_name("CHECK_RESULTS.json")
    out.write_text(json.dumps(metrics,indent=2)+"\n")
    print(json.dumps(metrics,indent=2))

if __name__ == "__main__": main()
