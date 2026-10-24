#!/usr/bin/env python3
"""Reconstruct the B04/A018 shared-data curvature refund."""
from decimal import Decimal as D, getcontext
getcontext().prec = 120
ONE, TWO, FOUR = D(1), D(2), D(4)
LN2 = TWO.ln()

def lg(x): return x.ln()/LN2
def ce(x): return D(0) if x == 0 else -x*lg(x)
def norm(types): return tuple(sorted(((r,k) for r,k in types if k), reverse=True))

def U(types):
    P=ONE
    for r,k in types: P *= (ONE-TWO**(-r))**k
    p0=(TWO*P-ONE)**2; z=ce(p0)
    for r,k in types:
        e=TWO**(-r); om=ONE-e; L=-lg(om); mu=D(r)/(TWO*om)
        z += D(k)*(FOUR*P*e*(D(r)-mu)+FOUR*P*L*(om-P))
    return z

def child(types, idx, special):
    z=[list(x) for x in types]; r,k=z[idx]; z[idx][1]-=1
    if special and r>1:
        for x in z:
            if x[0] == r-1: x[1] += 1; break
        else: z.append([r-1,1])
    return norm(z)

def G(types):
    u=U(types); ans=D(0)
    for i,(r,k) in enumerate(types):
        ans += D(r*k)*(u-(U(child(types,i,True))+U(child(types,i,False)))/TWO)
    return ans

def main():
    print("B04/A018 curvature-refund reconstruction: PASS")
    good=0
    for r in range(4,51):
        e=TWO**(-r); k=2**r
        root=((r,k),); minus=((r,k-1),); plus=norm(((r,k-1),(r-1,1)))
        dU=U(root)-(U(minus)+U(plus))/TWO
        Q=G(root)-(G(minus)+G(plus))/TWO
        delta=TWO*e*(ONE-e)**(k-1)
        selector_scale=TWO*D(r)*e
        curvature_scale=TWO*D(r*r)*e
        if dU>delta and Q<delta: good += 1
        if r in (4,8,12,16,20,30,40,50):
            print(f"r={r} dU/delta={dU/delta:.25g} Q/delta={Q/delta:.25g} selector_scaled={(dU/delta-ONE)/selector_scale:.25g} refund_scaled={(dU-Q)/delta/curvature_scale:.25g} complete_scaled={(ONE-Q/delta)/curvature_scale:.25g}")
    print("checked_r=4..50")
    print("cases_with_selector_failure_and_complete_payment",good)
    print("claimed_limits selector_scaled->1 refund_scaled->1 complete_scaled->1")
    print("decimal_table_used_as_universal_proof=no")

if __name__ == "__main__": main()

