from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, sys, time

run = Path(__file__).resolve().parents[1]
start = time.perf_counter()
checks = 0
def check(x):
    global checks
    checks += 1
    assert x
    assert time.perf_counter()-start < 55

@lru_cache(None)
def log2_bounds(x):
    x=Q(x); k=0
    assert x>0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def ln_bounds(y):
        z=(y-1)/(y+1)
        v=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
        return v,v+2*z**65/(65*(1-z*z))
    lo,hi=ln_bounds(x); l2,h2=ln_bounds(Q(2))
    return k+lo/h2,k+hi/l2

def entropy(p):
    lo=hi=Q(0)
    for x in p:
        if not x: continue
        l,h=log2_bounds(1/x); lo+=x*l; hi+=x*h
    return lo,hi

def fwht(v):
    a=list(v); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                x,y=a[k],a[k+step]; a[k]=x+y; a[k+step]=x-y
        step*=2
    return [Q(x,len(a)) for x in a]

def spectrum(v):
    aa=fwht(v); check(sum(x*x for x in aa)==1)
    return aa,[x*x for x in aa]

def edge(v,i):
    return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))

def outward(v):
    unit=1<<70
    return [str(Q((v[0]*unit).__floor__(),unit)),str(Q((v[1]*unit).__ceil__(),unit))]

rows=[]
for m in ([2] if sys.argv[1]=='pilot' else range(2,7)):
    N=1<<(2*m); delta=Q(1,N); s=Q(1,1<<m)
    b=tuple(1-2*((sum(((x>>(2*k))&1)*((x>>(2*k+1))&1) for k in range(m)))%2) for x in range(N))
    # j is bit 0, z is bit 1, data x starts at bit 2.
    F=tuple(b[x]+((1 if j==0 and z==0 else -1)-1 if x==0 else 0)
            for x in range(N) for z in range(2) for j in range(2))
    c=tuple(b[x]-(2 if x==0 and j==1 else 0) for x in range(N) for j in range(2))
    child0=tuple(b[x]+((1-2*z)-1 if x==0 else 0) for x in range(N) for z in range(2))
    child1=tuple(b[x]-(2 if x==0 else 0) for x in range(N) for z in range(2))
    check(all(v in [-1,1] for v in F+c+child0+child1))
    check(tuple(F[2*t] for t in range(2*N))==child0)
    check(tuple(F[2*t+1] for t in range(2*N))==child1)
    ba,bp=spectrum(b); fa,fp=spectrum(F)
    a0,p0=spectrum(child0); a1,p1=spectrum(child1)
    ca,cp=spectrum(c)
    check(sum(x==s for x in ba)==(N+(1<<m))//2)
    check(all(abs(x)==s for x in ba))
    for T in range(N):
        check(fa[4*T]==ba[T]-3*delta/2)
        for U in [1,2,3]:check(fa[4*T+U]==delta/2)
        check(a0[2*T]==ba[T]-delta and a0[2*T+1]==delta)
        check(a1[2*T]==ba[T]-2*delta and a1[2*T+1]==0)
    e=edge(F,0); check(e==delta/2)
    If=sum(Q(S.bit_count())*p for S,p in enumerate(fp))
    Icore=sum(Q(S.bit_count())*p for S,p in enumerate(cp))
    I0=sum(Q(S.bit_count())*p for S,p in enumerate(p0))
    I1=sum(Q(S.bit_count())*p for S,p in enumerate(p1))
    check(If==m+(3*m+1)*delta)
    check(Icore==m+(2*m+1)*delta)
    check(If-(I0+I1)/2==e)
    check(sum(edge(F,i) for i in range(2*m+2))==If)
    H=entropy(fp); H0=entropy(p0); H1=entropy(p1); Hc=entropy(cp)
    D=(H[0]-(H0[1]+H1[1])/2,H[1]-(H0[0]+H1[0])/2)
    check(D[0]>=e*(m+3))
    # G=0 for a one-bit character q throughout. R is carried once.
    R=Q(2*m+1,2)*delta; Rchild0=2*m*delta; Rchild1=Q(0)
    DR=R-(Rchild0+Rchild1)/2
    check(DR==e)
    check(D[0]-DR>=e*(m+2))
    check(D[1]<=e*(3*m+3))
    # Actual terminal source bank: both whole entropy bills are withheld FIRST.
    terminal_lo=(H0[0]+H1[0])/2
    terminal_hi=(H0[1]+H1[1])/2
    bank_lo=4*(I0+I1)/2-terminal_hi
    bank_hi=4*(I0+I1)/2-terminal_lo
    Llo=max(D[0]-4*e-DR,0)
    Lhi=max(D[1]-4*e-DR,0)
    check(bank_lo>=2*m)
    check(Lhi<=delta*(Q(3*m,2)-1))
    check(bank_lo-R-Lhi>=Q(59*m+1,32))
    check(H0[1]<=4*I0 and H1[1]<=4*I1)
    B=entropy([fp[0]]); B0=entropy([p0[0]]); B1=entropy([p1[0]])
    Bd=(B[0]-(B0[1]+B1[1])/2,B[1]-(B0[0]+B1[0])/2)
    check(Bd[1]<0)
    # 2 Delta K / ln(2) is DeltaH minus its signed bit boundary.
    heatbits=(D[0]-Bd[1],D[1]-Bd[0])
    check(heatbits[0]>=e*(m+3))
    rows.append({'m':m,'delta':str(delta),'influence':str(e),'reserve_root':str(R),'reserve_release':str(DR),
                 'entropy_debit_over_influence':outward((D[0]/e,D[1]/e)),
                 'unpaid_after_release_over_influence':outward(((D[0]-DR)/e,(D[1]-DR)/e)),
                 'signed_boundary_over_influence':outward((Bd[0]/e,Bd[1]/e)),
                 'actual_source_slack_rate4':outward((4*Icore-Hc[1],4*Icore-Hc[0])),
                 'full_terminal_entropy':outward(((H0[0]+H1[0])/2,(H0[1]+H1[1])/2)),
                 'root_entropy':outward(H),
                 'root_rate4_slack':outward((4*If-H[1],4*If-H[0]))})
    rows[-1].update({'original_terminal_bank':outward((bank_lo,bank_hi)),
                     'additional_positive_debit':outward((Llo,Lhi)),
                     'unused_after_reserve_booking_and_data_payment':outward((bank_lo-R-Lhi,bank_hi-R-Llo))})

out={'status':'PASS','mode':sys.argv[1],'cases':len(rows),'exact_checks':checks,'elapsed_seconds':time.perf_counter()-start,'rows':rows}
(run/'out'/('CHECK_'+sys.argv[1].upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
