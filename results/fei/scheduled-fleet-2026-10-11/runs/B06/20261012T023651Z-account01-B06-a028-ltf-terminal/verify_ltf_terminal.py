#!/usr/bin/env python3
"""Deterministic checks for the A028 LTF-terminal stopping theorem."""

from fractions import Fraction
from itertools import product
from math import log2, log, pi, e


def fwht(values):
    a = [Fraction(v) for v in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    n = len(a)
    return [x / n for x in a]


def entropy(coeffs):
    ans = 0.0
    for a in coeffs:
        p = float(a*a)
        if p:
            ans -= p*log2(p)
    return ans


def influence(coeffs):
    return sum((i.bit_count())*(a*a) for i, a in enumerate(coeffs))


def odd_mass(coeffs):
    return sum(a*a for i, a in enumerate(coeffs) if i.bit_count() & 1)


def point_defect(m):
    return [-1] + [1]*((1 << m)-1)


def ltf_table(weights, threshold=0):
    out=[]
    for x in product((-1,1), repeat=len(weights)):
        s=sum(w*y for w,y in zip(weights,x))-threshold
        out.append(1 if s >= 0 else -1)
    return out


def modulate(g, h):
    """g on n bits, h on m bits; common modulation of every g input."""
    n=(len(g)).bit_length()-1
    m=(len(h)).bit_length()-1
    out=[]
    xs=list(product((-1,1), repeat=n))
    zs=list(product((-1,1), repeat=m))
    index={x:i for i,x in enumerate(xs)}
    for x in xs:
        for zi,z in enumerate(zs):
            hz=h[zi]
            out.append(g[index[tuple(hz*y for y in x)]])
    return out


def main():
    assertions=0
    failures=[]
    # Exact Fourier formulas and the strict path constant.
    for m in range(1, 41):
        q=fwht(point_defect(m)) if m <= 12 else None
        N=1 << m
        r=Fraction(2,N)
        I=Fraction(m)*r
        if q is not None:
            assertions += 3
            if q[0] != 1-r: failures.append(("empty",m))
            if any(abs(a) != r for a in q[1:]): failures.append(("nonempty",m))
            if influence(q) != I: failures.append(("influence",m))
        a2=(1-float(r))**2
        H=0.0 if a2 == 0.0 else -a2*log2(a2)
        H += float(r*(2-r))*(2*m-2)
        assertions += 1
        if not H < 4*float(I): failures.append(("constant4",m,H/float(I)))

    # One-step identity over several genuine LTF bases and point defects.
    bases=[([1],0),([1,1,1],0),([1,2,3],1),([3,-2,1],-1)]
    max_residual=0.0
    cases=0
    for weights,threshold in bases:
        g=ltf_table(weights,threshold)
        cg=fwht(g)
        for m in (1,2,3):
            h=point_defect(m)
            ch=fwht(h)
            F=modulate(g,h)
            cF=fwht(F)
            P=odd_mass(cg)
            hres=abs(entropy(cF)-(entropy(cg)+float(P)*entropy(ch)))
            ires=abs(float(influence(cF))-
                     (float(influence(cg))+float(P*influence(ch))))
            max_residual=max(max_residual,hres,ires)
            assertions += 3
            cases += 1
            if hres > 1e-11: failures.append(("H-telescope",weights,m,hres))
            if ires > 1e-12: failures.append(("I-telescope",weights,m,ires))
            # Every fixed-z branch is an input sign flip of g, hence same spectrum.
            n=len(weights)
            xs=list(product((-1,1),repeat=n))
            for hz in (-1,1):
                branch=[g[xs.index(tuple(hz*y for y in x))] for x in xs]
                cb=fwht(branch)
                if sorted(a*a for a in cb) != sorted(a*a for a in cg):
                    failures.append(("branch-spectrum",weights,m,hz))

    # Two-level exact telescope checks (fresh blocks, no reused influence).
    two_level_cases=0
    for dims in ((1,1),(1,2),(2,1),(2,2)):
        f=ltf_table([1,1,1],0)
        cf=fwht(f)
        H_pred=entropy(cf)
        I_pred=influence(cf)
        for m in dims:
            q=point_defect(m)
            cq=fwht(q)
            P=odd_mass(cf)
            H_pred += float(P)*entropy(cq)
            I_pred += P*influence(cq)
            f=modulate(f,q)
            cf=fwht(f)
        hres=abs(entropy(cf)-H_pred)
        ires=abs(float(influence(cf))-float(I_pred))
        max_residual=max(max_residual,hres,ires)
        assertions += 2
        two_level_cases += 1
        if hres > 1e-11: failures.append(("H-two-level",dims,hres))
        if ires > 1e-12: failures.append(("I-two-level",dims,ires))

    C=log2(4+e)+2*log2(e*pi)
    assertions += 1
    if not (C < 8.937 and C > 4): failures.append(("C_LTF",C))

    print("A028 LTF-terminal deterministic verification")
    print(f"point-defect dimensions: 40 (exact FWHT through 12)")
    print(f"one-step LTF/modulator cases: {cases}")
    print(f"two-level hierarchy cases: {two_level_cases}")
    print(f"assertions: {assertions}")
    print(f"failures: {len(failures)}")
    print(f"maximum floating telescope residual: {max_residual:.3e}")
    print(f"C_LTF: {C:.12f}")
    print("random seed: none")
    if failures:
        for item in failures[:20]: print("FAIL",item)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
