from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(a,b):
    global checks
    checks+=1
    assert a==b,(a,b)
ZERO=(F(0),F(0))
def plus(*xs):return (sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0)))
def times(x,a):return (x[0]*a,x[1]*a) if a>=0 else (x[1]*a,x[0]*a)
def sub(x,y):return plus(x,times(y,-1))
def round_iv(x,bits=80):
    d=1<<bits
    return F((x[0]*d).__floor__(),d),F((x[1]*d).__ceil__(),d)
def ln_range(q):
    z=(q-1)/(q+1);s=F(0);term=z
    for j in range(32):s+=term/F(2*j+1);term*=z*z
    tail=2*abs(z)**65/(65*(1-z*z))
    return (2*s,2*s+tail) if z>=0 else (2*s-tail,2*s)
LN2=ln_range(F(2))
@lru_cache(None)
def log2(q):
    assert q>0
    if q==1:return ZERO
    e=q.numerator.bit_length()-q.denominator.bit_length()
    y=q/F(2)**e
    if y<1:y*=2;e-=1
    if y>=2:y/=2;e+=1
    check(F(1)<=y<2,True)
    z=ln_range(y)
    return round_iv((F(e)+z[0]/LN2[1],F(e)+z[1]/LN2[0]))
def entropy_pairs(items):
    return plus(*(times(log2(p),-multiplicity*p) for p,multiplicity in items if p))
def phi(a,b):
    if not a or not b:return ZERO
    return plus(times(log2((a+b)/a),a),times(log2((a+b)/b),b))
def kl_items(items):
    return plus(*(times(log2(p/q),w) for p,q,w in items if w))
def display(x):
    from decimal import Decimal,localcontext
    x=round_iv(x)
    with localcontext() as c:
        c.prec=28
        dec=[str(Decimal(t.numerator)/Decimal(t.denominator)) for t in x]
    return dict(lower=str(x[0]),upper=str(x[1]),display=dec)
def overlap(x,y):check(max(x[0],y[0])<=min(x[1],y[1]),True)

def activation_ref(c,z0,r):
    z=z0;zs=[z0];records=[]
    for s in range(1,r+1):
        u=F(1,1<<s);d=u*c;q0=1-2*d+2*d*d
        a=(1-d)**2;bb=d*d;active=(1-2*d)**2
        bcost=plus(phi(a,bb),(1-q0,1-q0))
        kcost=kl_items([(F(1,2*q0),F(1,1+z),F(1,2)),(active/(2*q0),z/(1+z),active/2)])
        r0=(1+z)/2;w=bb/q0*r0;z=a/q0*r0
        records.append(dict(s=s,u=u,q0=q0,B=bcost,K=kcost,w=w,z=z))
        zs.append(z)
    return zs,records

def core(k,mode):
    delta=F(1,1<<k);e=F(1,1<<(k//2));mu=e-delta
    counts={1:((1<<k)+(1<<(k//2)))//2,-1:((1<<k)-(1<<(k//2)))//2}
    q={s:delta-2*s*delta*e+2*delta*delta for s in counts}
    shifted={s:(s*e-2*delta)**2 for s in counts}
    avgHb=times(plus((F(k),F(k)),entropy_pairs([(shifted[s],counts[s]) for s in counts])),F(1,2))
    B=plus(*(times(phi((s*e-delta)**2,delta*delta),counts[s]) for s in counts))
    Hq=entropy_pairs([(q[s],counts[s]) for s in counts])
    J=sub(Hq,avgHb)
    if mode=='exact':
        z0=mu*mu;K=ZERO;leafKL=ZERO;leafCE=avgHb
    else:
        z0=delta*mu*mu/q[1];K=J;leafKL=sub((F(k),F(k)),avgHb);leafCE=(F(k),F(k))
    Hh=plus(B,Hq)
    return dict(delta=delta,e=e,mu=mu,counts=counts,q=q,shifted=shifted,z0=z0,B=B,J=J,K=K,leafKL=leafKL,leafCE=leafCE,Hh=Hh,avgHb=avgHb)

def calculate(k,mode):
    r=2*k;p=F(1,1<<r);h=core(k,mode);mu=h['mu'];c=1-mu;delta=h['delta']
    zs,records=activation_ref(c,h['z0'],r)
    B=times(h['B'],p);K=times(h['K'],p)
    for row in records:
        B=plus(B,times(row['B'],p/row['u']))
        K=plus(K,times(row['K'],p/row['u']))
    Iremoved=p*(r*c+delta);Iterminal=p*(F(k,2)+k*delta);Iroot=Iremoved+Iterminal
    # Independent explicit root KL over vacuum, pure controls and nonempty core.
    vacuum=(1-p*c)**2
    rootKL=times(log2(vacuum/zs[-1]),vacuum)
    mass=zs[-1]
    for j in range(r):
        s=r-j;row=records[s-1]
        prob=p*p*c*c;ref=row['w']/F(4)**j;mult=1<<j
        rootKL=plus(rootKL,times(log2(prob/ref),mult*prob))
        mass+=mult*ref
    coreKLnonempty=ZERO
    for sign,count in h['counts'].items():
        coeff=count*h['q'][sign]-(mu*mu if sign==1 else 0)
        ratio=F(1) if mode=='exact' else h['q'][sign]/delta
        coreKLnonempty=plus(coreKLnonempty,times(log2(ratio),coeff))
    rootKL=plus(rootKL,times(coreKLnonempty,p))
    mass+=p*(1-h['z0'])
    check(mass,F(1))
    terminalKL=times(h['leafKL'],p)
    overlap(rootKL,sub(terminalKL,K))
    rootH=entropy_pairs([(vacuum,1),(p*p*c*c,(1<<r)-1)])
    for sign,count in h['counts'].items():
        multiplicity=count-(1 if sign==1 else 0)
        rootH=plus(rootH,entropy_pairs([(p*p*(sign*h['e']-delta)**2,(1<<r)*multiplicity)]))
    rootH=plus(rootH,entropy_pairs([(p*p*delta*delta,(1<<r)*(1<<k))]))
    Jtree=sub(sub(rootH,times(h['avgHb'],p)),B)
    rootCE=plus(rootH,rootKL)
    overlap(rootCE,plus(sub(B,K),Jtree,times(h['leafCE'],p)))
    # All-even-k credit cap follows from chi-square bound.
    cap=times((1/LN2[1],1/LN2[0]),8*p*delta*(1-delta))
    check(K[0]>=-F(1,1<<65),True)
    check(K[1]<=terminalKL[1]+F(1,1<<65),True)
    check(K[1]<=cap[1],True)
    residual=sub(B,K)
    check(B[1]/Iremoved<F(3),True)
    check(rootCE[1]/Iroot<3+2/LN2[0],True)
    result=dict(k=k,r=r,reference=mode,I_removed=str(Iremoved),I_terminal=str(Iterminal),I_root=str(Iroot),erasure_over_removed=display(times(B,1/Iremoved)),posterior_credit_over_removed=display(times(K,1/Iremoved)),residual_over_removed=display(times(residual,1/Iremoved)),channel_over_removed=display(times(Jtree,1/Iremoved)),root_entropy_over_influence=display(times(rootH,1/Iroot)),root_CE_over_influence=display(times(rootCE,1/Iroot)),terminal_KL_over_removed=display(times(terminalKL,1/Iremoved)),chi_square_credit_cap_over_removed=display(times(cap,1/Iremoved)),root_KL=display(rootKL),root_reference_empty_mass=str(zs[-1]),nodes=[dict(s=row['s'],physical_reach=str(p/row['u']),B=display(row['B']),kappa=display(row['K']),reference_empty_mass=str(row['z'])) for row in records],selector_B=display(h['B']),selector_J=display(h['J']),selector_kappa=display(h['K']))
    return result,h,zs,records

def walsh(values):
    a=values[:];stride=1
    while stride<len(a):
        for base in range(0,len(a),2*stride):
            for j in range(stride):
                x,y=a[base+j],a[base+j+stride];a[base+j]=x+y;a[base+j+stride]=x-y
        stride*=2
    return [F(x,len(a)) for x in a]
def bent_values(k):return [-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2 else 1 for x in range(1<<k)]
def direct_check(k):
    r=2*k;vals=bent_values(k);flipped=vals[:];flipped[0]*=-1
    av,bv=walsh(vals),walsh(flipped);delta=F(1,1<<k);p=F(1,1<<r)
    check(all(x*x==delta for x in av),True)
    check(bv,[x-2*delta for x in av])
    # Residual index has selector first, then k data bits.
    hvals=[(flipped if (x&1) else vals)[x>>1] for x in range(1<<(k+1))]
    ah=walsh(hvals);mu=ah[0];c=1-mu
    qcore=[]
    for s in range(len(ah)):
        t=s>>1;mix=(av[t]**2+bv[t]**2)/2
        qcore.append(delta*ah[s]**2/mix)
    for mode in ['exact','uniform']:
        result,h,zs,records=calculate(k,mode)
        refcore=[a*a for a in ah] if mode=='exact' else qcore
        qold=refcore
        for remaining in range(1,r+1):
            # Direct Walsh spectrum of the actual active suffix Boolean table.
            n=remaining+k+1;cube=[hvals[x>>remaining] if (x&((1<<remaining)-1))==0 else 1 for x in range(1<<n)]
            a=walsh(cube);qnew=[]
            for index in range(1<<n):
                t=index>>1;mix=a[2*t]**2+a[2*t+1]**2
                check(mix>0,True)
                refmix=(qold[t]+(1 if t==0 else 0))/2
                qnew.append(a[index]**2/mix*refmix)
            check(sum(qnew),F(1));check(qnew[0],zs[remaining])
            qold=qnew
        # Compare every root reference atom to the compressed closed expression.
        for index,Q in enumerate(qold):
            U=index&((1<<r)-1);V=index>>r
            if V:expected=p*p*refcore[V]
            elif not U:expected=zs[-1]
            else:
                j=U.bit_length()-1;s=r-j
                expected=records[s-1]['w']/F(4)**j
            check(Q,expected)
        if mode=='uniform':
            # Direct physical edge count of total/removed/terminal influences.
            total=F(0)
            for i in range(n):total+=F(sum(cube[x]!=cube[x^(1<<i)] for x in range(1<<n)),1<<n)
            check(total,F(result['I_root']))
    return dict(k=k,dimension=r+k+1,root_atoms=1<<(r+k+1),method='Integer Walsh reconstruction and atomwise Fraction reference comparison')

start=time.perf_counter();pilot='--pilot' in sys.argv
ks=[2] if pilot else [2,4,6,8]
results=[]
for k in ks:
    for mode in ['exact','uniform']:
        result,_,_,_=calculate(k,mode);results.append(result)
direct=[direct_check(k) for k in ([2] if pilot else [2,4])]
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out=dict(helper_version='A097-bent-reference-v2',case_count=len(results),exact_assertions=checks,failures=0,runtime_seconds=elapsed,logarithm_certificate='32-term rational atanh series; dyadic range reduction and outward 2^-80 rounding',direct_validation=direct,results=results)
(ROOT/'out').mkdir(exist_ok=True)
name='PILOT.json' if pilot else 'RESULTS.json'
(ROOT/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(case_count=len(results),exact_assertions=checks,failures=0,runtime_seconds=elapsed,ratios=[dict(k=x['k'],reference=x['reference'],B=x['erasure_over_removed']['display'],K=x['posterior_credit_over_removed']['display'],residual=x['residual_over_removed']['display']) for x in results]),indent=2))
