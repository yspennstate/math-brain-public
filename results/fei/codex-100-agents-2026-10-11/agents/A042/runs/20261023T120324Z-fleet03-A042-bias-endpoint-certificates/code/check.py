import argparse, json, math, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); CHECKS=0
def ck(value):
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(CHECKS)
    if time.perf_counter()-START>55: raise RuntimeError('frozen 55-second limit exceeded')
def cell(t):
    j=0
    while t<=F(1,2): t*=2; j+=1
    return j
@lru_cache(None)
def factors(n):
    result={}; d=2
    while d*d<=n:
        while n%d==0: result[d]=result.get(d,0)+1; n//=d
        d+=1
    if n>1: result[n]=result.get(n,0)+1
    return result
def logadd(expr,x,weight):
    if not weight: return
    ck(x>0)
    for p,e in factors(x.numerator).items(): expr[p]=expr.get(p,F(0))+e*weight
    for p,e in factors(x.denominator).items(): expr[p]=expr.get(p,F(0))-e*weight
def plus(*terms):
    expr={}
    for other,weight in terms:
        for p,v in other.items(): expr[p]=expr.get(p,F(0))+weight*v
    return {p:v for p,v in expr.items() if v}
def ln4(weight): return {2:2*weight} if weight else {}
def spectrum(table,p):
    # Separable physical mean/half-difference transform, O(n 2^n).
    coeff=list(map(F,table)); n=len(p)
    for i,pi in enumerate(p):
        stride=1<<i
        for s in range(1<<n):
            if s&stride: continue
            lo,hi=coeff[s],coeff[s+stride]
            coeff[s]=(1-pi)*lo+pi*hi; coeff[s+stride]=(hi-lo)/2
    sp={}
    for s,c in enumerate(coeff):
        v=F(1)
        for i,pi in enumerate(p):
            if s>>i&1: v*=4*pi*(1-pi)
        j=cell(abs(c)) if c else None
        sp[s]={'c':c,'P':v*c*c,'W':v*F(1,4**j) if c else F(0),'j':j}
    ck(sum(z['P'] for z in sp.values())==1)
    return sp
def stats(sp):
    values={'V':F(0),'I':F(0),'A':F(0),'M':F(0),'Z1':F(0),'Zh':F(0),'J1':F(0),'Jh':F(0),'R':F(0)}
    E1={}; Lh={}
    for s,z in sp.items():
        if not s: continue
        d=s.bit_count(); P=z['P']
        values['V']+=P; values['I']+=d*P; values['R']+=max(0,d-2)*P
        values['A' if d==1 else 'M']+=P
        values['Z1' if d==1 else 'Zh']+=z['W']
        if P:
            values['J1' if d==1 else 'Jh']+=P*z['j']
            if d==1: logadd(E1,abs(z['c']),-2*P)
            else: logadd(Lh,2**z['j']*abs(z['c']),-2*P)
    values.update(E1=plus((E1,1)),Lh=plus((Lh,1)))
    values['L1']=plus((E1,1),(ln4(values['J1']),-1))
    return values
def paid_reference(sp,st):
    M,Z=st['M'],st['Zh']
    return {s:(z['P'] if s.bit_count()<=1 else M*z['W']/Z if M else F(0)) for s,z in sp.items()}
def KL(sp,Q):
    value={}
    for s,z in sp.items():
        if z['P']: logadd(value,z['P']/Q[s],z['P'])
    return plus((value,1))
def normalizer(st):
    value={}
    if st['M']: logadd(value,st['Zh']/st['M'],st['M'])
    return plus((value,1))
def check_case(table,p,k):
    sp=spectrum(table,p); st=stats(sp); e=F(1,2**k)
    root=spectrum(tuple(1 if not x&1 else table[x>>1] for x in range(2*len(table))),(e,)+p)
    rt=stats(root); V,A,M=st['V'],st['A'],st['M']; a=(1-sp[0]['c'])/2
    ck(rt['I']-rt['V']==e*(st['I']-V)+e*(1-e)*V)
    carry=rt['Jh']-e*st['Jh']-e*(1-e)*V
    ck(carry==e*(1-e)*st['J1']+e*e*k*M); ck(carry>=0)
    ck(rt['M']==e*M+e*(1-e)*A)
    ck(rt['Zh']==e*st['Zh']+e*(1-e)*st['Z1'])
    ck(rt['Lh']==plus((st['Lh'],e),(st['L1'],e*(1-e))))
    if not V:
        ck(rt['M']==carry==0); ck(rt['I']==rt['V']); return
    # Full spectrum/cell check independently of the high-sector aggregation.
    for T,z in sp.items():
        if not T: continue
        for bit in (0,1):
            zz=root[2*T+bit]
            ck(zz['c']==z['c']*(F(1,2) if bit else e))
            if z['P']: ck(zz['j']==z['j']+(1 if bit else k))
    fullcarry=sum(z['P']*z['j'] for s,z in root.items() if s and z['P'])-e*(st['J1']+st['Jh'])
    ja=cell(a)
    outer_full=e*(1-e)*(V+4*a*a*ja)+e*e*k*V
    ck(fullcarry==outer_full)
    outer=spectrum((1,-1,1,1),(e,1-a)); ot=stats(outer)
    ck(ot['Jh']==e*(1-e)*V); ck(ot['Lh']=={})
    left=plus((ln4(carry),1),(rt['E1'],1),(rt['Lh'],1))
    right=plus((ot['E1'],1),(st['E1'],e),(st['Lh'],e))
    ck(left==right)
    # Exact complete reference, including low atoms. Compare full ordinary KL.
    qs=paid_reference(sp,st); qf=paid_reference(root,rt)
    qt={0:root[0]['P'],1:root[1]['P']}
    for T,z in sp.items():
        if not T: continue
        qt[2*T]=e*e*qs[T]; qt[2*T+1]=e*(1-e)*qs[T]
    ck(sum(qf.values())==sum(qt.values())==1)
    for s,z in root.items():
        if s.bit_count()<=1: ck(qf[s]==qt[s]==z['P'])
        if z['P']: ck(qf[s]>0 and qt[s]>0)
    kg,kf,kt=KL(sp,qs),KL(root,qf),KL(root,qt)
    ck(kt==plus((kg,e)))
    ck(plus((kf,1),(kg,-e))==plus((normalizer(rt),1),(normalizer(st),-e),(st['L1'],-e*(1-e))))
    # Directly verify individual physical pivotal influence in majority controls below.
    return st,rt,carry
def cases(pilot):
    laws={1:((F(1,2),),(F(1,3),)),2:((F(1,2),F(1,2)),(F(1,3),F(2,5))),3:((F(1,2),)*3,)}
    if pilot:
        for mask in range(16): yield tuple(1 if mask>>s&1 else -1 for s in range(4)),laws[2][0],1,None
        return
    for n in (1,2,3):
        for p in laws[n]:
            for mask in range(1<<(1<<n)):
                table=tuple(1 if mask>>s&1 else -1 for s in range(1<<n))
                for k in (1,2,4,10): yield table,p,k,None
    for n in (3,5,7,9):
        table=tuple(1 if s.bit_count()>n//2 else -1 for s in range(1<<n))
        for k in (1,2,4,10): yield table,(F(1,2),)*n,k,n
def majority_induction():
    for m in range(256):
        ck((2*m+1)**2*(4*m+5)-(2*m+2)**2*(4*m+1)==1)
        ck(4*(m+1)**3-(2*m+1)**2*(m+2)==3*m+2)
    fixtures=[]
    for r in range(1,7):
        m=4**r-1; p=F(math.comb(2*m,m),4**m); A=(2*m+1)*p*p; j=cell(p)
        ck(F(1,4*m+1)<=p*p<=F(1,m+1)); ck(A>F(1,2)); ck(j>=r)
        # Exact coefficients in units ln4, no transcendental comparison.
        endpoint_ratio=A*j
        fair_ratio=A*j+(1-A)
        ck(endpoint_ratio>F(r,2)); ck(fair_ratio>F(r,2))
        fixtures.append({'r':r,'m':m,'n':2*m+1,'j_singleton':j,'endpoint_carry_over_outer_deficit_ln4':{'numerator_bits':endpoint_ratio.numerator.bit_length(),'denominator_bits':endpoint_ratio.denominator.bit_length()},'certified_lower_bound':'r*ln2 (strict)','physical_majority':True})
    return fixtures
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); parser.add_argument('--majority',action='store_true'); args=parser.parse_args()
    if args.majority:
        fixtures=majority_induction(); total=len(fixtures); dest='MAJORITY.json'
    else:
        total=0; fixtures=[]
        for table,p,k,n in cases(args.pilot):
            result=check_case(table,p,k); total+=1
            if n:
                st,rt,carry=result; m=(n-1)//2; pm=F(math.comb(2*m,m),4**m)
                ck(st['A']==n*pm*pm); ck(st['I']==n*pm); ck(st['V']==1)
                ck(carry/(F(1,2**k)*(1-F(1,2**k)))>=st['J1'])
        dest='PILOT.json' if args.pilot else 'CHECKS.json'
    result={'status':'PASS','cases':total,'exact_assertions':CHECKS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'Fraction physical transform and canonical prime-log identities','fixtures':fixtures}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/dest).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='fixtures'}))
