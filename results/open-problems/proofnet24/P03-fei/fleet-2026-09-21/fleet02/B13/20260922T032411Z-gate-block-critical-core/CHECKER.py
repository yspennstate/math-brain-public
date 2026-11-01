from __future__ import annotations
import itertools, math
from decimal import Decimal, getcontext

# Self-check for REPORT.md. The universal identities are proved on the page.

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1.0-x)*math.log2(1.0-x)

def pts(n): return list(itertools.product((0,1), repeat=n))

def prob_x(x, ps):
    r=1.0
    for xi,p in zip(x,ps): r*=p if xi else 1.0-p
    return r

def gamma_test(t): return 2.0*t*(1.0-t)

def biased_stats(vals, ps):
    n=len(ps); xs=pts(n); coeff=[]
    for mask in range(1<<n):
        s=0.0
        for idx,x in enumerate(xs):
            b=1.0
            for i,p in enumerate(ps):
                if (mask>>i)&1: b*=(x[i]-p)/math.sqrt(p*(1.0-p))
            s+=prob_x(x,ps)*vals[idx]*b
        coeff.append(s)
    w=[a*a for a in coeff]
    H=-sum(t*math.log2(t) for t in w if t>1e-300)
    It=[sum(w[m] for m in range(1<<n) if (m>>i)&1) for i in range(n)]
    q=sum(prob_x(x,ps) for idx,x in enumerate(xs) if vals[idx]<0)
    return H,It,q

def D_gate(vals, ps):
    H,It,q=biased_stats(vals,ps); rhs=0.0
    for I,p in zip(It,ps):
        V=4.0*p*(1.0-p)
        rhs+=I/V*(gamma_test(p)+h2(V))
    return rhs-gamma_test(q)-H,H,It,q

def restrict_vals(vals,n,A,z):
    A=tuple(sorted(A)); rem=tuple(i for i in range(n) if i not in A); out=[]
    for xr in pts(len(rem)):
        x=[0]*n
        for i,b in zip(A,z): x[i]=b
        for i,b in zip(rem,xr): x[i]=b
        idx=0
        for b in x: idx=(idx<<1)|b
        out.append(vals[idx])
    return out,rem

def block_identity_error(vals,ps,A):
    n=len(ps); D,H,It,q=D_gate(vals,ps); ED=EH=EG=0.0
    rem=tuple(i for i in range(n) if i not in A)
    for z in pts(len(A)):
        wt=1.0
        for i,b in zip(sorted(A),z):
            p=ps[i]; wt*=p if b else 1.0-p
        child,_=restrict_vals(vals,n,A,z); cps=[ps[i] for i in rem]
        if rem: cD,cH,_,cq=D_gate(child,cps)
        else:
            cH=0.0; cq=1.0 if child[0]<0 else 0.0; cD=-gamma_test(cq)
        ED+=wt*cD; EH+=wt*cH; EG+=wt*gamma_test(cq)
    cost=0.0
    for i in A:
        p=ps[i]; V=4.0*p*(1.0-p)
        cost+=It[i]/V*(gamma_test(p)+h2(V))
    R=cost+EG-gamma_test(q)-(H-EH)
    return D-ED-R

def truth_vals(n,bits): return [-1 if (bits>>i)&1 else 1 for i in range(1<<n)]

def small_gate_checks():
    total=0; maxerr=0.0
    for n,ps in ((2,(1/3,2/5)),(3,(1/3,2/5,3/5))):
        for bits in range(1,(1<<(1<<n))-1):
            vals=truth_vals(n,bits)
            for r in range(1,n):
                for A in itertools.combinations(range(n),r):
                    e=abs(block_identity_error(vals,ps,A)); maxerr=max(maxerr,e); total+=1
    assert maxerr<2e-12
    return total,maxerr

def affine_witness():
    global gamma_test
    old=gamma_test; gamma_test=lambda t:4.0*t*(1.0-t)
    try:
        parity=[1,-1,-1,1]; dictator=[1,1,-1,-1]
        Dp,Hp,_,_=D_gate(parity,(0.5,0.5)); Dd,Hd,_,_=D_gate(dictator,(0.5,0.5))
        assert abs(Dp-1.0)<1e-12 and abs(Dd)<1e-12 and abs(Hp)<1e-12 and abs(Hd)<1e-12
        return Dp,Dd
    finally: gamma_test=old

def g10_arithmetic():
    getcontext().prec=80
    C0=Decimal('6.4548'); Cdag=Decimal('6.521852'); a=Decimal(4)*(Cdag-C0)
    Mup=Decimal('6.52185121301287772365150440023918196647146413881'); assert Cdag>Mup
    Q=Decimal(229)/Decimal(1024)
    rlo=Decimal('25.057083819433480'); rhi=Decimal('25.057083819433481')
    Hlo=Decimal(29)/Decimal(32)+Q*rlo; Hhi=Decimal(29)/Decimal(32)+Q*rhi
    term=a*Decimal(29)/Decimal(1024)
    Drlo=Cdag*Decimal(129)/Decimal(128)-Hhi; Drhi=Cdag*Decimal(129)/Decimal(128)-Hlo
    Blo=Drlo-term; Bhi=Drhi-term
    oldlo=C0*Decimal(129)/Decimal(128)-Hhi; oldhi=C0*Decimal(129)/Decimal(128)-Hlo
    assert Blo==oldlo+a*Q and Bhi==oldhi+a*Q and Blo>Decimal('0.05537')
    return Cdag,a,Mup,Hlo,Hhi,a/Decimal(16),term,Drlo,Drhi,Blo,Bhi

def main():
    count,maxerr=small_gate_checks(); Dp,Dd=affine_witness(); g=g10_arithmetic()
    print('PASS'); print(f'block_identity_checks={count}'); print(f'block_identity_max_abs_error={maxerr:.3e}')
    print(f'affine_witness_D_parity={Dp:.17g}'); print(f'affine_witness_D_dictator={Dd:.17g}')
    names=('Cdag','a','M_upper','H_lo','H_hi','terminal_each','terminal_expected','Droot_lo','Droot_hi','block_lo','block_hi')
    for k,v in zip(names,g): print(f'{k}={v}')

if __name__=='__main__': main()
