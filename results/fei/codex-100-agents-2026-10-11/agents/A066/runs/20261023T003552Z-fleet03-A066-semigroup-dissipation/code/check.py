from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import sys,json,time
run=Path(__file__).resolve().parents[1]
started=time.perf_counter(); checks=0
def test(v):
    global checks
    checks+=1
    assert v
    assert time.perf_counter()-started<55
def walsh(v):
    a=list(v);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):x,y=a[k],a[k+h];a[k]=x+y;a[k+h]=x-y
        h*=2
    return tuple(Q(x,len(a)) for x in a)
def ln_interval(x):
    z=(x-1)/(x+1)
    v=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(32)),Q(0))
    return v,v+2*z**65/(65*(1-z*z))
l2,h2=ln_interval(Q(2))
@lru_cache(None)
def log2_interval(x):
    k=0;x=Q(x);assert x>0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    lo,hi=ln_interval(x)
    return k+lo/h2,k+hi/l2
@lru_cache(None)
def cost(p,q=None):
    if q is None:q=p
    lo=hi=Q(0)
    for a,b in zip(p,q):
        if a:
            test(b>0);x,y=log2_interval(1/b);lo+=a*x;hi+=a*y
    return lo,hi
def edge(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def spectrum(v):
    a=walsh(v);p=tuple(x*x for x in a);test(sum(p)==1);return a,p
def rounded(v):
    scale=1<<70
    return [str(Q((v[0]*scale).__floor__(),scale)),str(Q((v[1]*scale).__ceil__(),scale))]
rows=[];admit=reject=undetermined=0
mode=sys.argv[1]
roots=[]
for d in range(3 if mode=='pilot' else 4):
    N=1<<d
    for mask in range(1<<(N-1)):
        roots.append((d,'exhaustive',tuple([1]+[1 if mask>>(x-1)&1 else -1 for x in range(1,N)])))
if mode!='pilot':
    for d in [4,5,6]:
        N=1<<d;odd=d if d%2 else d-1
        candidates=[('constant',tuple([1]*N)),('dictator',tuple(1-2*(x&1) for x in range(N))),
          ('parity',tuple(1-2*(x.bit_count()%2) for x in range(N))),
          ('positive_point',tuple(1 if x==0 else -1 for x in range(N))),
          ('negative_point',tuple(-1 if x==N-1 else 1 for x in range(N))),
          ('majority',tuple(1 if (x&((1<<odd)-1)).bit_count()<=odd//2 else -1 for x in range(N))),
          ('quadratic',tuple(1-2*(sum(((x>>(2*k))&1)*((x>>(2*k+1))&1) for k in range(d//2))%2) for x in range(N))),
          ('prescribed',tuple(1 if x==0 or (x*x+3*x+1)%7<3 else -1 for x in range(N)))]
        seen=set()
        for name,b in candidates:
            if b not in seen:roots.append((d,name,b));seen.add(b)
for d,name,b in roots:
    N=len(b);delta=Q(1,N);e=delta/2;R=Q(d+1)*e
    F=tuple(b[x]+((1 if j==0 and z==0 else -1)-1 if x==0 else 0) for x in range(N) for z in range(2) for j in range(2))
    f0=tuple(b[x]+(-2*z if x==0 else 0) for x in range(N) for z in range(2))
    f1=tuple(b[x]-(2 if x==0 else 0) for x in range(N) for z in range(2))
    test(all(v in [-1,1] for v in F+f0+f1));test(tuple(F[2*i] for i in range(2*N))==f0);test(tuple(F[2*i+1] for i in range(2*N))==f1)
    ba,bp=spectrum(b);fa,fp=spectrum(F);a0,p0=spectrum(f0);a1,p1=spectrum(f1)
    test(sum(ba)==1)
    for T in range(N):
        test(fa[4*T]==ba[T]-3*delta/2)
        for U in [1,2,3]:test(fa[4*T+U]==delta/2)
        test(a0[2*T]==ba[T]-delta and a0[2*T+1]==delta)
        test(a1[2*T]==ba[T]-2*delta and a1[2*T+1]==0)
    Ib=sum(i.bit_count()*p for i,p in enumerate(bp))
    I0=sum(i.bit_count()*p for i,p in enumerate(p0));I1=sum(i.bit_count()*p for i,p in enumerate(p1));Ibar=(I0+I1)/2
    If=sum(i.bit_count()*p for i,p in enumerate(fp))
    t=sum(b[1<<i]==-1 for i in range(d))
    test(I0==Ib+delta*(d-2*t)+delta)
    test(I1==Ib+2*delta*(d-2*t))
    test(Ibar==Ib+Q(3,2)*delta*(d-2*t)+delta/2)
    test(Ib>=2*delta*t);test(Ibar>=R)
    test(edge(F,0)==e);test(If-Ibar==e)
    test(sum(edge(F,i) for i in range(d+2))==If)
    test(R-Q(d)*delta/2==e)
    H=cost(fp);H0=cost(p0);H1=cost(p1)
    Hd=(H[0]-(H0[1]+H1[1])/2,H[1]-(H0[0]+H1[0])/2)
    kappa_lo=Q(5,2)+Q(3,2)/h2
    test(Hd[1]<=R/2+kappa_lo*e)
    test(4*Hd[1]<=2*R+19*e)
    B=cost((fp[0],));B0=cost((p0[0],));B1=cost((p1[0],))
    Bd=(B[0]-(B0[1]+B1[1])/2,B[1]-(B0[0]+B1[0])/2)
    A=cost(fp[1:]);A0=cost(p0[1:]);A1=cost(p1[1:])
    heat=(A[0]-(A0[1]+A1[1])/2,A[1]-(A0[0]+A1[0])/2)
    test(max(heat[0],Hd[0]-Bd[1])<=min(heat[1],Hd[1]-Bd[0]))
    Llo=max(Hd[0]-5*e,0);Lhi=max(Hd[1]-5*e,0)
    test(Lhi<=R/2-e/4)
    refrows=[]
    for ref in ['actual','half_uniform']:
        qs=[p0,p1] if ref=='actual' else [tuple((v+Q(1,len(p)))/2 for v in p) for p in [p0,p1]]
        ce0=cost(p0,qs[0]);ce1=cost(p1,qs[1]);CE=((ce0[0]+ce1[0])/2,(ce0[1]+ce1[1])/2)
        test(CE[1]>=(H0[0]+H1[0])/2)
        for K in [4,8]:
            # One old debit, never canceled or re-booked. Both complete CE bills
            # were withheld before defining the original source bank.
            old=Ibar/4;U=(K*Ibar-CE[1]-old,K*Ibar-CE[0]-old)
            threshold=Q(3,2)*R-e/4
            if U[0]>=threshold:
                status='ADMITTED';admit+=1
                test(U[0]>=R)
                test(U[0]-R-Lhi>=0)
                test(Hd[1]<=4*e+e+U[0]-R)
                test(CE[1]+old+R+Lhi<=K*Ibar)
            elif U[1]<threshold:status='NOT_ADMITTED';reject+=1
            else:status='INTERVAL_UNRESOLVED';undetermined+=1
            refrows.append({'reference':ref,'rate':K,'admission':status,'old_debit':str(old),'unused_original_source':rounded(U)})
    rows.append({'d':d,'name':name,'truth_table_mask':str(sum((v==1)<<i for i,v in enumerate(b))),'e':str(e),'R':str(R),'Ibar':str(Ibar),'DeltaH':rounded(Hd),'signed_empty_boundary_bits':rounded(Bd),'two_heat_area_over_ln2':rounded(heat),'profile_minus_Rhalf_over_e':rounded(((Hd[0]-R/2)/e,(Hd[1]-R/2)/e)),'references':refrows})

budget_cases=0;budget_hypotheses=0
if mode!='pilot':
    for E in range(4):
        for reserve in range(E,9):
            for U in range(17):
                for D in range(31):
                    budget_cases+=1
                    if 4*D<=2*reserve+19*E and 4*U>=6*reserve-E:
                        budget_hypotheses+=1;test(U>=reserve);test(D<=5*E+U-reserve);test(max(D-5*E,0)<=U-reserve)
    test(budget_cases==15810)
    # All-width constant-core obstruction: exact spectral histogram, no cube allocation.
    d=18;delta=Q(1,1<<d)
    def point_entropy(n):
        p=Q(1,1<<n);pempty=(1-2*p)**2;tail=(1<<n)-1;mass=4*p*p
        A=cost((pempty,));lo,hi=log2_interval(1/mass)
        return A[0]+tail*mass*lo,A[1]+tail*mass*hi
    h0=point_entropy(d+1);h1=point_entropy(d)
    Ibar=Q(3*d+1,2)*delta
    B=(4*Ibar-(h0[1]+h1[1])/2,4*Ibar-(h0[0]+h1[0])/2)
    test(B[1]<=9*delta);test(B[1]<Q(d+1,2)*delta)
    guard={'d':d,'bank_rate4':rounded(B),'required_R':str(Q(d+1,2)*delta),'status':'SOURCE_ADMISSION_FAILS_EVEN_BEFORE_OLD_DEBIT'}
else:guard=None
out={'status':'PASS','mode':mode,'roots':len(roots),'reference_cases':4*len(roots),'admitted':admit,'not_admitted':reject,'interval_unresolved':undetermined,'integer_budget_domain':budget_cases,'integer_budget_admitted':budget_hypotheses,'exact_assertions':checks,'seconds':time.perf_counter()-started,'constant_core_guard':guard,'rows':rows}
(run/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','constant_core_guard']}))
