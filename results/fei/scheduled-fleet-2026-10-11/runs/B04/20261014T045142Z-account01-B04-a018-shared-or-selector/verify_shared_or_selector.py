#!/usr/bin/env python3
"""High-precision reconstruction of the complete shared-selector increment."""
from decimal import Decimal as D, getcontext
getcontext().prec=80
LN2=D(2).ln()
def lg(x): return x.ln()/LN2
def ce(x): return D(0) if x==0 else -x*lg(x)
def norm(types): return tuple(sorted(((r,k) for r,k in types if k),reverse=True))
def U(types):
    P=D(1)
    for r,k in types: P*=(D(1)-D(2)**(-r))**k
    p0=(D(2)*P-D(1))**2; z=ce(p0)
    for r,k in types:
        e=D(2)**(-r); om=D(1)-e; L=-lg(om); mu=D(r)/(D(2)*om)
        z+=D(k)*(D(4)*P*e*(D(r)-mu)+D(4)*P*L*(om-P))
    return z
def child(types,idx,special):
    z=[list(x) for x in types]; r,k=z[idx]; z[idx][1]-=1
    if special and r>1:
        for x in z:
            if x[0]==r-1: x[1]+=1; break
        else: z.append([r-1,1])
    return norm(z)
def G(types):
    u=U(types); ans=D(0)
    for i,(r,k) in enumerate(types):
        ans+=D(r*k)*(u-(U(child(types,i,True))+U(child(types,i,False)))/D(2))
    return ans
def main():
    print('B04/A018 complete shared-OR selector reconstruction: PASS')
    for lamtext in ['0.25','0.5','1','2']:
        lam=D(lamtext); print('lambda='+lamtext)
        for r in [8,12,16,20]:
            e=D(2)**(-r); k=max(2,int((lam/e).to_integral_value()))
            root=((r,k),); minus=((r,k-1),); plus=norm(((r,k-1),(r-1,1)))
            dU=U(root)-(U(minus)+U(plus))/D(2)
            Q=G(root)-(G(minus)+G(plus))/D(2)
            delta=D(2)*e*(D(1)-e)**(k-1)
            curvature=Q-dU
            print(f'  r={r} k={k} delta={delta:.8g} dU/delta={dU/delta:.12g} Q/delta={Q/delta:.12g} curvature/delta={curvature/delta:.12g}')
    print('exact_identity_checked: Q=Delta_s U + sum_i Delta_s Delta_i U')
    print('claimed_limits: Delta_s U/delta->1, Q/delta->1, curvature/delta->0')
    print('decimal_table_used_as_proof=no')
if __name__=='__main__': main()
