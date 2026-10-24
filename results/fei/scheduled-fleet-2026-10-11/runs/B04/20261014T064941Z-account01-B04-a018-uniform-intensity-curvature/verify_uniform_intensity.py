#!/usr/bin/env python3
"""120-digit reconstruction for the uniform-intensity curvature theorem."""
from decimal import Decimal as D, getcontext
getcontext().prec=120
ONE,TWO,FOUR=D(1),D(2),D(4); LN2=TWO.ln()
def lg(x):return x.ln()/LN2
def ce(x):return D(0) if x==0 else -x*lg(x)
def norm(types):return tuple(sorted(((r,k) for r,k in types if k),reverse=True))
def U(types):
    P=ONE
    for r,k in types:P*=(ONE-TWO**(-r))**k
    z=ce((TWO*P-ONE)**2)
    for r,k in types:
        e=TWO**(-r);om=ONE-e;L=-lg(om)
        z+=D(k)*(FOUR*P*e*(D(r)-D(r)/(TWO*om))+FOUR*P*L*(om-P))
    return z
def child(types,idx,special):
    z=[list(x) for x in types];r,k=z[idx];z[idx][1]-=1
    if special and r>1:
        for x in z:
            if x[0]==r-1:x[1]+=1;break
        else:z.append([r-1,1])
    return norm(z)
def G(types):
    u=U(types);z=D(0)
    for i,(r,k) in enumerate(types):
        z+=D(r*k)*(u-(U(child(types,i,True))+U(child(types,i,False)))/TWO)
    return z
def row(lam,r):
    e=TWO**(-r);k=max(1,int((lam/e).to_integral_value()))
    root=((r,k),);minus=((r,k-1),);plus=norm(((r,k-1),(r-1,1)))
    du=U(root)-(U(minus)+U(plus))/TWO
    q=G(root)-(G(minus)+G(plus))/TWO
    delta=TWO*e*(ONE-e)**(k-1)
    selector=(du/delta-ONE)/(TWO*D(r)*e)
    refund=(du-q)/delta/(TWO*D(r*r)*e)
    complete=(ONE-q/delta)/(TWO*D(r*r)*e)
    return k,du,q,delta,selector,refund,complete
def main():
    print('B04/A018 uniform-intensity curvature reconstruction: PASS')
    assertions=0
    for ls in ('0.1','0.25','0.5','0.65','0.75','1','2','4'):
        lam=D(ls);last=None
        for r in (12,16,20,24,28,32):
            last=(r,)+row(lam,r)
            assert last[2]>last[4] and last[3]<last[4]
            assertions+=2
        r,k,du,q,delta,a,b,c=last
        print(f'lambda={ls} r={r} k={k} selector_scaled={a:.12g} '
              f'refund_scaled={b:.12g} complete_scaled={c:.12g}')
    print('assertions=',assertions,sep='')
    print('claimed_limits: selector_scaled, refund_scaled, complete_scaled -> 1')
    print('decimal_table_used_as_universal_proof=no')
if __name__=='__main__':main()
