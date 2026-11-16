"""PROVED: exact centered-polynomial inclusion bounds, with integer replay.

If P has integer coefficients and total degree d, translate S^d P((c+y)/S).
All resulting coefficients are integers. On |y_i|<=h_i, an odd-power
monomial has range [-m,m], an all-even monomial has range [0,m].
Adding these ranges gives an inclusion bound. No floating arithmetic is used.
"""
from math import comb
from fractions import Fraction as F


def integer_polynomial(p,divisor=1):
    out={}
    for mon,c in p.terms():
        assert c.denominator==1 and int(c)%divisor==0
        out[mon]=int(c)//divisor
    return out


def translate(poly,c,scale):
    assert len(c)==len(next(iter(poly)))
    degree=max(map(sum,poly))
    out={m:a*scale**(degree-sum(m)) for m,a in poly.items()}
    for i,ci in enumerate(c):
        new={}
        for mon,a in out.items():
            for k in range(mon[i]+1):
                key=mon[:i]+(k,)+mon[i+1:]
                new[key]=new.get(key,0)+a*comb(mon[i],k)*ci**(mon[i]-k)
        out={m:a for m,a in new.items() if a}
    return out,degree


def bound_translated(poly,h):
    dim=len(h)
    powers=[[int(hi)**k for k in range(9)]for hi in h]
    lo=hi=poly.get((0,)*dim,0)
    for mon,a in poly.items():
        if not any(mon): continue
        value=a
        for i,m in enumerate(mon): value*=powers[i][m]
        if any(m%2 for m in mon):
            lo-=abs(value); hi+=abs(value)
        elif value<0: lo+=value
        else: hi+=value
    return lo,hi


def box_bound(poly,box):
    center=[(F(l)+F(h))/2 for l,h in box]
    widths=[(F(h)-F(l))/2 for l,h in box]
    from math import lcm
    scale=lcm(*(v.denominator for v in center+widths))
    c=[int(x*scale)for x in center]
    h=[int(x*scale)for x in widths]
    shifted,d=translate(poly,c,scale)
    lo,hi=bound_translated(shifted,h)
    return F(lo,scale**d),F(hi,scale**d)


def box_analysis(poly,box):
    """Exact inclusion plus discovery-only sensitivity data for subdivision."""
    center=[(F(l)+F(h))/2 for l,h in box]
    widths=[(F(h)-F(l))/2 for l,h in box]
    from math import lcm
    scale=lcm(*(v.denominator for v in center+widths))
    c=[int(x*scale)for x in center]
    h=[int(x*scale)for x in widths]
    tr,d=translate(poly,c,scale)
    lo,hi=bound_translated(tr,h)
    c0=tr.get((0,)*len(h),0)
    powers=[[x**k for k in range(9)]for x in h]
    impact=[0]*len(h)
    for mon,a in tr.items():
        if a>=0 and not any(m%2 for m in mon):continue
        val=abs(a)
        for i,m in enumerate(mon):val*=powers[i][m]
        for i,m in enumerate(mon):impact[i]+=m*val
    return F(lo,scale**d),F(hi,scale**d),c0,lo,impact
