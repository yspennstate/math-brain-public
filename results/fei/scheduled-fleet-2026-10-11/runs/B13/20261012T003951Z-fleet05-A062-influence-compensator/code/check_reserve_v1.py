"""A062-reserve-v1: integer Boolean spectra and rational log certificates."""
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json,time,hashlib

RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter()
counts=Counter()
def equal(a,b,kind):
    assert a==b,(kind,a,b)
    counts[kind]+=1
def leq(a,b,kind):
    assert a<=b,(kind,str(a),str(b))
    counts[kind]+=1
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def minus(a,b): return (a[0]-b[1],a[1]-b[0])
def mul(a,c):
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def pos(a): return (max(F(0),a[0]),max(F(0),a[1]))
def point(c): return (F(c),F(c))
def ln_series(q):
    z=(q-1)/(q+1)
    assert 0<=z<=F(1,3)
    value=F(0)
    zp=z
    for j in range(48):
        value+=2*zp/(2*j+1)
        zp*=z*z
    error=2*zp/(97*(1-z*z))
    return (value,value+error)
LN2=ln_series(F(2))
@lru_cache(None)
def log2(q):
    if q==1: return point(0)
    exponent=q.numerator.bit_length()-q.denominator.bit_length()
    power=F(2)**exponent
    norm=q/power
    if norm<1:
        exponent-=1
        norm*=2
    assert 1<=norm<=2
    lo,hi=ln_series(norm)
    # All corner quotients: also correct for negative logarithms.
    vals=[lo/LN2[0],lo/LN2[1],hi/LN2[0],hi/LN2[1]]
    return (F(exponent)+min(vals),F(exponent)+max(vals))
@lru_cache(None)
def atom_h(q):
    return point(0) if not q else mul(log2(q),-q)
def entropy(hist):
    out=point(0)
    for q,count in hist.items():
        if q:
            out=plus(out,mul(atom_h(q),count))
    return out
def phi(r,s): return minus(plus(atom_h(r),atom_h(s)),atom_h(r+s))
def psi(mu): return atom_h(mu)
def fwht(values):
    out=list(values)
    h=1
    while h<len(out):
        for block in range(0,len(out),2*h):
            for j in range(block,block+h):
                a,b=out[j],out[j+h]
                out[j],out[j+h]=a+b,a-b
        h*=2
    return out
def b(t):
    return tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(t//2)) for x in range(1<<t))
@lru_cache(None)
def measure(values):
    size=len(values)
    n=size.bit_length()-1
    coeff=[F(w,size) for w in fwht(values)]
    law=[w*w for w in coeff]
    equal(sum(law),F(1),'parseval')
    infl=[sum(law[x] for x in range(size) if (x>>i)&1) for i in range(n)]
    boundary=[F(sum(values[x]!=values[x^(1<<i)] for x in range(size)),size) for i in range(n)]
    equal(infl,boundary,'boundary_walsh')
    return coeff,entropy(Counter(law)),infl
def fmt(a):
    # These decimals are presentation only; fractions supply certificates.
    return {'lower':str(a[0]),'upper':str(a[1]),'display_midpoint':float((a[0]+a[1])/2)}

core_rows=[]
evenQ={0:point(0)}
evenH={0:point(0)}
for t in (2,4,6,8,10,12):
    core=list(b(t)); core[0]=-1; core=tuple(core)
    coeff,h,inf=measure(core)
    equal(inf,[F(1,2)+F(2,2**t)]*t,'edited_influence')
    leq(F(t-2),h[0],'edited_entropy_lower')
    leq(h[1],F(t),'edited_entropy_upper')
    if t==2:
        equal(h,point(0),'base_parity_entropy')
        evenQ[t]=point(0)
        evenH[t]=h
        core_rows.append({'t':t,'even_Q':fmt(point(0))})
        continue
    bt=b(t-2)
    odd=tuple(-1 if x==0 else bt[x>>1] for x in range(1<<(t-1)))
    oc,oh,oi=measure(odd)
    equal(oi[0],F(1,2**(t-2)),'odd_influence')
    od=minus(oh,mul(plus(evenH[t-2],point(t-2)),F(1,2)))
    leq(od[1],F(2),'odd_drop_upper')
    oq=pos(plus(minus(od,point(7*oi[0])),mul(evenQ[t-2],F(1,2))))
    leq(oq[1],F(2),'odd_reserve_upper')
    ed=minus(h,mul(plus(oh,point(t-2)),F(1,2)))
    eq_pre=plus(minus(ed,point(7*inf[0])),mul(oq,F(1,2)))
    leq(eq_pre[1],F(0),'even_reserve_cancel')
    evenQ[t]=point(0)
    evenH[t]=h
    mu=F(sum(x==-1 for x in odd),len(odd))
    equal(mu,F(1- F(1,2**((t-2)//2))+F(1,2**(t-2)),2),'odd_minority')
    leq(oq[1],4*psi(mu)[0],'odd_rarity_domination')
    core_rows.append({'t':t,'D_even':fmt(ed),'D_odd':fmt(od),'odd_Q':fmt(oq),
                      'even_pre_max':fmt(eq_pre),'odd_mu':str(mu),'odd_4psi':fmt(mul(psi(mu),4)),
                      'truth_table_sha256':hashlib.sha256(bytes(x+1 for x in core)).hexdigest()})

def activation_h(coeff,s):
    if s==0:
        return entropy(Counter(w*w for w in coeff))
    p=F(1,2**s)
    a=1-coeff[0]
    hist=Counter()
    hist[(1-p*a)**2]+=1
    hist[(p*a)**2]+=2**s-1
    for w in coeff[1:]: hist[(p*w)**2]+=2**s
    equal(sum(q*n for q,n in hist.items()),F(1),'activation_mass')
    return entropy(hist)

activation_rows=[]
for k in (4,6):
    for edited in (False,True):
        values=list(b(k))
        if edited: values[0]=-1
        coeff,h,inf=measure(tuple(values))
        a=1-coeff[0]
        for s in range(1,9):
            d=F(a,2**s)
            hd=minus(activation_h(coeff,s),mul(activation_h(coeff,s-1),F(1,2)))
            leq(hd[1],7*d,'control_drift_paid')
            be=plus(point(2*d-2*d*d),phi((1-d)**2,d*d))
            leq(be[1],4*d,'control_erasure_paid')
            activation_rows.append({'k':k,'edited':edited,'s':s,'d':str(d),'D':fmt(hd),'B':fmt(be)})

root_rows=[]
for k,r in ((4,8),(6,12),(8,16),(10,20),(12,24)):
    alpha=F(1,2**(k//2)); delta=alpha*alpha; p=F(1,2**r)
    numplus=(2**k+2**(k//2))//2
    numminus=(2**k-2**(k//2))//2
    packets=[(1+p*(alpha-1),1),(p*(alpha-1),2**r-1),
             (p*alpha,(numplus-1)*2**r),(-p*alpha,numminus*2**r)]
    ph,ch0,ch1=Counter(),Counter(),Counter()
    mismatch=F(0)
    for g,num in packets:
        hh=g-2*p*delta
        ph[((g+hh)/2)**2]+=num
        ph[((g-hh)/2)**2]+=num
        ch0[g*g]+=num; ch1[hh*hh]+=num
        mismatch+=num*((g-hh)/2)**2
    for hist in (ph,ch0,ch1): equal(sum(w*num for w,num in hist.items()),F(1),'selector_mass')
    d=p*delta
    equal(mismatch,d,'selector_disagreement')
    D=minus(entropy(ph),mul(plus(entropy(ch0),entropy(ch1)),F(1,2)))
    reserve=pos(minus(D,point(7*d)))
    leq(reserve[1],d*(r+k-F(5,2)),'selector_rational_upper')
    mu=p*(1-alpha+delta)/2
    rarity=psi(mu)
    leq(reserve[1],4*delta*rarity[0],'selector_sharp_rarity_credit')
    leq(reserve[1],rarity[0]/4,'selector_quarter_rarity_credit')
    infl=p*(F(k,2)+(k+1)*delta+r*(1-alpha+delta))
    leq(reserve[1],2*delta*infl,'root_label_budget')
    # A064's physical-rarity drift is much smaller than this actual reserve.
    mudrift=minus(rarity,mul(plus(psi(mu-d/2),psi(mu+d/2)),F(1,2)))
    root_rows.append({'k':k,'r':r,'d':str(d),'mu':str(mu),'I':str(infl),'D':fmt(D),'Qstar':fmt(reserve),
                      'quarter_psi':fmt(mul(rarity,F(1,4))),
                      'rarity_drift_c4':fmt(mul(mudrift,4)),
                      'c4_rarity_local_payment_margin':fmt(minus(point(7*d),minus(D,mul(mudrift,4))))})

elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'helper_version':'A062-reserve-v1','assertions':sum(counts.values()),'counts':dict(counts),
     'failures':0,'runtime_seconds':elapsed,'C':'7','core_states':core_rows,
     'activation_nodes':activation_rows,'selector_roots':root_rows,
     'arithmetic':'Fraction atanh series 48 terms with explicit tail; integer Walsh truth tables'}
(RUN/'out/CERTIFICATES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assertions':sum(counts.values()),'failures':0,'runtime_seconds':elapsed,
                  'roots':[{'k':x['k'],'r':x['r'],'Qstar':x['Qstar']['display_midpoint'],
                           'Qstar_over_I':x['Qstar']['display_midpoint']/float(F(x['I']))} for x in root_rows]},indent=2))
