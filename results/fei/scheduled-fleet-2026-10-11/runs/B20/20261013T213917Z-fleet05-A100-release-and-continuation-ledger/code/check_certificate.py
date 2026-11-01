from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, sys
RUN=Path(__file__).resolve().parents[1]; START=time.perf_counter(); CHECKS=0
def check(c,name):
    global CHECKS
    assert c,name
    CHECKS+=1
    if time.perf_counter()-START>60: raise RuntimeError('Frozen runtime cap reached')
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(a,s): return (a[0]*s,a[1]*s) if s>=0 else (a[1]*s,a[0]*s)
def sub(a,b): return add(a,scale(b,-1))
def iv(x): return (F(x),F(x))
def pack(x):
    # Compact outward reporting leaves all sign decisions in exact Fraction arithmetic.
    grid=1<<100
    lo=(x[0].numerator*grid)//x[0].denominator
    hi=-((-x[1].numerator*grid)//x[1].denominator)
    return {'lower':str(F(lo,grid)),'upper':str(F(hi,grid))}
def ln_series(y):
    z=(y-1)/(y+1); z2=z*z; term=z; result=F(0)
    for j in range(24): result+=2*term/(2*j+1); term*=z2
    return result,result+2*term/(49*(1-z2))
LN2=ln_series(F(2))
@lru_cache(None)
def log2(x):
    x=F(x); assert x>0
    power=0
    while x<1: x*=2; power-=1
    while x>=2: x/=2; power+=1
    lo,hi=ln_series(x)
    return power+lo/LN2[1],power+hi/LN2[0]
def entropy(masses):
    result=iv(0)
    for m,count in masses.items():
        if m: result=add(result,scale(log2(m),-count*m))
    return result
def phi(a,b): return sub(entropy({a:1,b:1}) if a!=b else entropy({a:2}),entropy({a+b:1}))
def divergence(p,q):
    result=iv(0)
    for a,b in zip(p,q):
        if a: result=add(result,scale(log2(a/b),a))
    return result
def walsh(vals):
    out=list(vals); step=1
    while step<len(out):
        for start in range(0,len(out),2*step):
            for j in range(start,start+step):
                a,b=out[j],out[j+step]; out[j],out[j+step]=a+b,a-b
        step*=2
    return [F(x,len(out)) for x in out]
def influences(vals,n):
    return [F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals)) for i in range(n)]
def bent_vals(k): return [(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k)]
def root_vals(k,r):
    b=bent_vals(k); return [1 if x>>(k+1) else b[x&((1<<k)-1)]-2*int(((x>>k)&1)==1 and (x&((1<<k)-1))==0) for x in range(1<<(k+1+r))]
domain=[2] if '--pilot' in sys.argv else [2,4,6,8]
source=json.loads(Path(r'~\brain_workers\FEI100_20261011\agents\A097\runs\20261012T005449Z-fleet05-A097-cross-route-transfer\out\RESULTS.json').read_text(encoding='utf-8-sig'))
rows=[]
for k in domain:
    r=2*k; delta=F(1,1<<k); activation=F(1,1<<r); e=F(1,1<<(k//2)); mu=e-delta; c=1-mu
    b=bent_vals(k); bp=b.copy(); bp[0]*=-1
    a=walsh(b); ap=walsh(bp)
    check(all(x*x==delta for x in a),'bent flat spectrum')
    check(sum(x>0 for x in a)==((1<<k)+(1<<(k//2)))//2,'positive sign multiplicity')
    check(all(y==x-2*delta for x,y in zip(a,ap)),'actual zero-point surgery')
    check(sum(influences(b,k))==F(k,2),'b influence')
    check(sum(influences(bp,k))==F(k,2)+2*k*delta,'point-flipped b influence')
    check(sum((x*x-delta)**2/delta for x in ap)==16*delta*(1-delta),'all-k chi-square formula')
    h=b+bp; ah=walsh(h); ph=[x*x for x in ah]
    check(sum(ph)==1,'actual selector spectrum normalization')
    q=[ph[t]+ph[t+(1<<k)] for t in range(1<<k)]
    bs=iv(0); hbprime=entropy({m:sum(x*x==m for x in ap) for m in set(x*x for x in ap)})
    js=sub(entropy({m:q.count(m) for m in set(q)}),scale(add(iv(k),hbprime),F(1,2)))
    for t in range(1<<k): bs=add(bs,phi(ph[t],ph[t+(1<<k)]))
    im=activation*(r*c+delta); it=activation*(F(k,2)+k*delta)
    check(im>0 and it>0,'positive separated budgets')
    if k in [2,4]:
        v=root_vals(k,r); av=walsh(v); n=k+1+r
        for index,coeff in enumerate(av):
            core=index&((1<<(k+1))-1); controls=index>>(k+1)
            predicted=activation*ah[core] if core else (1-activation*c if not controls else -activation*c)
            check(coeff==predicted,'root direct integer-Walsh activation coefficient')
        phys=influences(v,n)
        check(sum(phys)==im+it,'root physical total influence')
        check(sum(phys[k:])==im,'control plus selector physical influence')
    for mode in ['exact','uniform']:
        qh=ph[:] if mode=='exact' else [delta*ph[t]/q[t&((1<<k)-1)] for t in range(1<<(k+1))]
        check(sum(qh)==1,'complete seed-compatible core reference')
        z=qh[0]; credit=iv(0) if mode=='exact' else js; bsum=bs
        w_by_s={}
        for s in range(1,r+1):
            u=F(1,1<<s); d=u*c; vac=(1-d)**2; tail=d*d; marginal=vac+tail
            B=add(phi(vac,tail),iv(1-marginal))
            bsum=add(bsum,scale(B,1/u))
            childvac=(1-2*d)**2
            kp=[1/(2*marginal),childvac/(2*marginal)]; kq=[1/(1+z),z/(1+z)]
            check(sum(kp)==1 and sum(kq)==1,'physical/reference posterior normalization')
            kap=scale(divergence(kp,kq),marginal)
            if mode=='exact': check(kp==kq,'exact leaf references force zero credit')
            credit=add(credit,scale(kap,1/u))
            w_by_s[s]=tail/marginal*(1+z)/2
            z=vac/marginal*(1+z)/2
        bt=scale(bsum,activation); kt=scale(credit,activation)
        brate=scale(bt,1/im); krate=scale(kt,1/im); residual=scale(sub(bt,kt),1/im)
        check(brate[1]<3,'finite B_tree/I_removed<3')
        leafslack=iv(0) if mode=='exact' else scale(sub(iv(k),hbprime),activation/2)
        rootdiv=scale(log2((1-activation*c)**2/z),(1-activation*c)**2)
        qmass=z
        for j in range(r):
            true=activation**2*c*c; ref=F(1,4**j)*w_by_s[r-j]; count=1<<j
            rootdiv=add(rootdiv,scale(log2(true/ref),count*true)); qmass+=count*ref
        for atom in range(1,len(ph)):
            if ph[atom]: rootdiv=add(rootdiv,scale(log2(ph[atom]/qh[atom]),activation*ph[atom]))
        qmass+=activation*(1-qh[0])
        check(qmass==1,'independently grouped complete root reference')
        discrepancy=sub(add(rootdiv,kt),leafslack)
        check(discrepancy[0]<=0<=discrepancy[1],'KL telescope interval consistency, not equality proof')
        source_row=next(x for x in source['results'] if x['k']==k and x['reference']==mode)
        for label,bounds in [('erasure_over_removed',brate),('posterior_credit_over_removed',krate),('residual_over_removed',residual)]:
            src=source_row[label]; lo,hi=F(src['lower']),F(src['upper'])
            check(max(lo,bounds[0])<=min(hi,bounds[1]),'independent enclosure intersects source '+label)
        # A coarser rational credit ceiling does not need a floating ln2.
        cap=8*delta*(1-delta)/( (r*c+delta)*LN2[0])
        check(krate[1]<=cap,'terminal chi-square credit ceiling')
        rows.append({'k':k,'reference':mode,'I_removed':str(im),'I_terminal':str(it),'B_over_removed':pack(brate),'credit_over_removed':pack(krate),'residual_over_removed':pack(residual),'terminal_slack':pack(leafslack),'root_KL':pack(rootdiv),'KL_identity_discrepancy_enclosure':pack(discrepancy),'credit_upper_bound':str(cap)})
# Actual two-bit Boolean witness to the false A021 v1 remainder sign.
activation_dictator=[1,1,1,-1]; aa=walsh(activation_dictator)
check(all(x*x==F(1,4) for x in aa),'A021 two-bit actual flat law')
check(sum(influences(activation_dictator,2))==1,'A021 physical influence')
check(LN2[0]>F(56,81),'strict cubic ln2 certificate')
rem=(F(1,2)-F(1,4)/LN2[0],F(1,2)-F(1,4)/LN2[1])
check(rem[0]>F(31,224),'A021 positive remainder R>31/224')
result={'helper_version':'A100-independent-certificate-v1','frozen_case_count':len(rows),'assertions_passed':CHECKS,'failed':0,'runtime_seconds':time.perf_counter()-START,'logarithms':'24-term exact rational atanh series after dyadic range reduction','rows':rows,'A021_actual_Boolean_witness':{'truth_table':activation_dictator,'squared_spectrum':['1/4']*4,'H_exact':'2','I_exact':'1','q':'1/2','R_formula':'1/2-1/(4 ln2)','R_certified':pack(rem),'strict_lower_bound':'31/224'},'limits':'Finite logarithmic consistency is not an all-k identity proof; all-k B/chi-square/credit statements are reconstructed analytically in REVIEW.md.'}
name='PILOT.json' if '--pilot' in sys.argv else 'INDEPENDENT_CERTIFICATE.json'
(RUN/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','A021_actual_Boolean_witness']},indent=2))
