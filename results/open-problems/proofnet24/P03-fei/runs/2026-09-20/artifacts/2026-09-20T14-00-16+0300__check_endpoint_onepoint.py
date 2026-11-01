#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import math, random, json, sys

Q = 10**12

def root_floor_scaled(x: int, k: int, Q: int = Q) -> int:
    """Return floor(Q*x^(1/k)), certified by integer powers."""
    assert x >= 1 and k >= 1
    a = x ** (1.0 / k)
    r = int(a * Q)
    target = x * (Q ** k)
    while pow(r, k) > target:
        r -= 1
    while pow(r + 1, k) <= target:
        r += 1
    assert pow(r, k) <= target < pow(r + 1, k)
    return r


def g_upper_frac(n: int, t: int) -> Fraction:
    """Rigorous rational upper bound for scalar g_n(t), t>=1."""
    assert n >= 2 and t >= 1
    m = n - 1
    rpt = root_floor_scaled(2 * t, n)
    r2 = root_floor_scaled(2, n)
    pos = Fraction(2 * t * t * Q, rpt) + Fraction(2 * Q, r2)
    neg = Fraction(0)
    for u in (t + 1, abs(t - 1)):
        if u:
            rr = root_floor_scaled(u, m)
            neg += Fraction(u * u * Q, rr + 1)
    return n * pos - m * neg - (t * t + 1)


def rhs_frac(n: int, t: int) -> Fraction:
    N = 1 << (n - 1)
    return Fraction(3, 1) + Fraction(1 + t * t, N)


def finite_scalar_certificate():
    count = 0
    min_margin = None
    min_arg = None
    per_n = {}
    for n in range(2, 73):
        N = 1 << (n - 1)
        if n <= 16:
            ts = range(1, N, 2)
        else:
            lim = int(math.sqrt(16 * n)) + 2
            ts = [t for t in range(1, lim + 1, 2) if t * t < 16 * n]
        ncount = 0
        nmin = None
        narg = None
        for t in ts:
            up = g_upper_frac(n, t)
            rhs = rhs_frac(n, t)
            margin = rhs - up
            if margin <= 0:
                raise AssertionError(f"scalar certificate failed n={n} t={t}: {margin}")
            count += 1
            ncount += 1
            if min_margin is None or margin < min_margin:
                min_margin, min_arg = margin, (n, t)
            if nmin is None or margin < nmin:
                nmin, narg = margin, t
        per_n[n] = {"count": ncount, "min_margin": float(nmin) if nmin is not None else None, "arg": narg}
    return {
        "count": count,
        "min_margin": float(min_margin),
        "min_arg": min_arg,
        "per_n_selected": {str(n): per_n[n] for n in [2,3,4,5,6,7,8,16,17,32,72]},
    }


def fwht(vals):
    a = [float(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def phi(vals):
    N = len(vals)
    d = N.bit_length()-1
    if d == 0:
        return 0.0
    s = 2.0 - 1.0/d
    c = fwht(vals)
    return d * (sum(abs(x)**s for x in c) - 1.0)


def parent_from_children(g,h):
    out=[]
    for a,b in zip(g,h):
        out.extend([a,b])
    return out


def onepoint_charge(g, point):
    h=list(g); h[point]*=-1
    f=parent_from_children(g,h)
    n=(len(f)).bit_length()-1
    A=phi(f)-0.5*(phi(g)+phi(h))
    delta=1.0/len(g)
    return A,delta


def boolean_sanity():
    exhaustive=0
    max_ratio=-1e100
    max_case=None
    max_violation=-1e100
    for m in range(1,4):
        N=1<<m
        for mask in range(1<<N):
            g=[1 if ((mask>>x)&1) else -1 for x in range(N)]
            for p in range(N):
                A,d=onepoint_charge(g,p)
                ratio=A/d
                exhaustive+=1
                if ratio>max_ratio:
                    max_ratio,max_case=ratio,(m,mask,p)
                max_violation=max(max_violation,A-4*d)
    rng=random.Random(202609201400)
    sampled=0
    for m in range(4,9):
        N=1<<m
        reps=500
        for _ in range(reps):
            g=[1 if rng.getrandbits(1) else -1 for _ in range(N)]
            p=rng.randrange(N)
            A,d=onepoint_charge(g,p)
            ratio=A/d
            sampled+=1
            if ratio>max_ratio:
                max_ratio,max_case=ratio,(m,"sample",p)
            max_violation=max(max_violation,A-4*d)
    return {
        "exhaustive_onepoint_pairs": exhaustive,
        "sampled_onepoint_pairs": sampled,
        "max_charge_over_delta": max_ratio,
        "max_case": max_case,
        "max_violation_of_A_le_4delta": max_violation,
    }


def analytic_constants():
    ln2=math.log(2.0)
    n=17
    F17=2*((n-1)*ln2-math.log(4.0)-0.5*math.log(n))-math.sqrt(n*(n-1))
    n=73
    L=math.log(8*math.sqrt(n))
    deriv_margin=(2*ln2-1)-((L*L+L)/n+1/12)
    B3=13-16*ln2+(9*math.log(6)**2+ln2**2)/n
    return {"middle_endpoint_F17":F17,"small_region_derivative_margin_n73":deriv_margin,"small_region_B3_n73":B3}


def influence_truth(vals, bit):
    N=len(vals)
    return Fraction(sum(1 for x in range(N) if vals[x] != vals[x ^ (1<<bit)]), N)


def total_influence_truth(vals):
    m=len(vals).bit_length()-1
    return sum((influence_truth(vals,k) for k in range(m)), Fraction(0))


def restrict_truth(vals, bit, b):
    n=len(vals).bit_length()-1
    out=[]
    for y in range(1<<(n-1)):
        lo=y & ((1<<bit)-1)
        hi=y >> bit
        x=lo | (b<<bit) | (hi<<(bit+1))
        out.append(vals[x])
    return out


def translate(vals,w):
    return [vals[y^w] for y in range(len(vals))]


def folded(q):
    return min(q, 1-q)


def translation_average_sanity():
    checked=0
    max_formula_error=Fraction(0)
    max_bound_violation=Fraction(-10**9)
    min_exists_slack=None
    for n in range(1,5):
        N=1<<n
        for tailmask in range(1<<(N-1)):
            vals=[1]+[1 if ((tailmask>>(x-1))&1) else -1 for x in range(1,N)]
            for i in range(n):
                g=restrict_truth(vals,i,0); h=restrict_truth(vals,i,1)
                m=n-1; R=1<<m
                a=[]; b=[]
                for k in range(m):
                    a.append(influence_truth(g,k)); b.append(influence_truth(h,k))
                exact=sum((aa+bb-2*aa*bb for aa,bb in zip(a,b)),Fraction(0))
                costs=[]
                for w in range(R):
                    hw=translate(h,w)
                    d=[g[y]*hw[y] for y in range(R)]
                    costs.append(total_influence_truth(d))
                avg=sum(costs,Fraction(0))/R
                err=abs(avg-exact)
                if err>max_formula_error:max_formula_error=err
                Jrest=Fraction(0)
                for aa,bb in zip(a,b):
                    Jrest += folded((aa+bb)/2)
                rhs=2*Jrest
                viol=min(costs)-rhs
                if viol>max_bound_violation:max_bound_violation=viol
                slack=rhs-min(costs)
                if min_exists_slack is None or slack<min_exists_slack:min_exists_slack=slack
                assert avg==exact
                assert min(costs)<=rhs
                checked+=1
    return {"coordinate_cases":checked,"max_formula_error":float(max_formula_error),
            "max_min_cost_minus_2Jrest":float(max_bound_violation),
            "min_exists_slack":float(min_exists_slack)}

def main():
    finite=finite_scalar_certificate()
    sanity=boolean_sanity()
    trans=translation_average_sanity()
    const=analytic_constants()
    assert const["middle_endpoint_F17"]>0
    assert const["small_region_derivative_margin_n73"]>0
    assert const["small_region_B3_n73"]<3
    assert sanity["max_violation_of_A_le_4delta"] < 1e-10
    out={"status":"PASS","finite_scalar_certificate":finite,"boolean_sanity":sanity,"translation_average_sanity":trans,"analytic_constant_sanity":const,
         "notes":[
             "Finite scalar certificate is rigorous rational arithmetic: all irrational nth roots are enclosed by integer-power inequalities at denominator 10^12.",
             "Boolean Walsh checks are floating-point sanity checks only; theorem proof uses the scalar certificate plus analytic regions.",
         ]}
    path=sys.argv[1] if len(sys.argv)>1 else "/tmp/endpoint_onepoint_check.json"
    with open(path,"w") as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
