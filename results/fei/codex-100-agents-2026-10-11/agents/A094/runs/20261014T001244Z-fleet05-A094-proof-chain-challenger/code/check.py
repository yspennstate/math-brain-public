from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, sys, time
RUN=Path(__file__).resolve().parents[1]
checks=0
def ck(value):
    global checks
    assert value
    checks+=1
@lru_cache(None)
def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(a,b,scale=F(1)):
    out=a.copy()
    for p,x in b.items():
        out[p]=out.get(p,F(0))+scale*x
        if not out[p]:del out[p]
    return out
def lograt(q):
    q=F(q); return add(factor(q.numerator),factor(q.denominator),F(-1))
def ce(p,q):
    ans={}
    for t,x in p.items():
        if x:ans=add(ans,lograt(q[t]),-x)
    return ans
def ent(p):return ce(p,p)
def kl(p,q):return add(ce(p,q),ent(p),F(-1))
@lru_cache(None)
def ln_bounds(n):
    e=n.bit_length()-1; x=F(n,2**e); z=(x-1)/(x+1)
    s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0))
    rem=2*z**73/(73*(1-z*z))
    if n==2:
        z=F(1,3);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0));rem=2*z**73/(73*(1-z*z));return s,s+rem
    l,u=ln_bounds(2)
    return s+e*l,s+rem+e*u
def interval(v):
    lo=hi=F(0)
    for p,a in v.items():
        l,u=ln_bounds(p)
        lo+=a*(l if a>=0 else u);hi+=a*(u if a>=0 else l)
    return lo,hi
def upper_zero(v):return interval(v)[1]<=0
def fw(values):
    a=list(values);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(h):u,v=a[j+k],a[j+k+h];a[j+k],a[j+k+h]=u+v,u-v
        h*=2
    return {j:F(x,len(a)) for j,x in enumerate(a)}
def influences(values):
    n=(len(values)-1).bit_length()
    return [F(sum(values[x]!=values[x^(1<<j)] for x in range(len(values))),len(values)) for j in range(n)]
def tables(n):
    return [[1 if t>>x&1 else -1 for x in range(1<<n)] for t in range(1<<(1<<n))]
def embed_coeff(c,positions):
    return {sum(1<<positions[j] for j in range(len(positions)) if t>>j&1):a for t,a in c.items()}
def reference(p,variant):
    if variant==0:return p.copy()
    if variant==1:return {t:F(1,len(p)) for t in p}
    # Different from author's increasing-index weights: coordinate-size product law.
    n=(len(p)-1).bit_length();return {t:F(2**t.bit_count(),3**n) for t in p}
def calibrate(p,r,C):
    mass=sum(p.get(t,F(0)) for t in C);den=sum(x for t,x in r.items() if t not in C)
    return {t:p[t] if t in C else (r[t]*(1-mass)/den if den else F(0)) for t in p}
def root_values(g,h,shared):
    ng=(len(g)-1).bit_length();nh=(len(h)-1).bit_length();nd=ng+nh-shared
    out=[]
    for x in range(1<<(nd+1)):
        gi=x&((1<<ng)-1)
        hi=((x>>ng)<<shared)&((1<<nh)-1)
        if shared:hi|=x&1
        out.append(h[hi] if x>>nd&1 else g[gi])
    return out,ng,nh,nd
def one_pair(g,h,shared):
    values,ng,nh,nd=root_values(g,h,shared); ac=fw(g);bc=fw(h)
    positions_g=list(range(ng));positions_h=([0] if shared else [])+list(range(ng,nd))
    a=embed_coeff(ac,positions_g);b=embed_coeff(bc,positions_h)
    p={t:x*x for t,x in ac.items()};q={t:x*x for t,x in bc.items()}
    allT=set(a)|set(b); marginal={t:(a.get(t,0)**2+b.get(t,0)**2)/2 for t in allT}
    true={}
    for t in allT:
        true[t]=(a.get(t,0)+b.get(t,0))**2/4
        true[t|(1<<nd)]=(a.get(t,0)-b.get(t,0))**2/4
    full=fw(values);ck(all(full[t]**2==true.get(t,0) for t in full));ck(sum(true.values())==1)
    ig=influences(g);ih=influences(h);root_i=influences(values)
    C=[0,1] if shared else [0]
    dot=sum(a.get(t,0)*b.get(t,0) for t in C); d=(1-dot)/2
    ck(root_i[-1]==d);ck(sum(root_i)==(sum(ig)+sum(ih))/2+d)
    # Each actual physical data account, including the shared bit, separately.
    for j in range(nd):
        expect=F(0)
        if j in positions_g:expect+=ig[positions_g.index(j)]/2
        if j in positions_h:expect+=ih[positions_h.index(j)]/2
        ck(root_i[j]==expect)
    delta=add(ent(true),add(ent(p),ent(q)),F(-1,2))
    bound=add(delta,{2:2*d},F(-1)); ck(interval(bound)[1]<=4*d)
    # Source critical collision estimate checked as an exact rational inequality.
    ck(sum(abs(a.get(t,0)**2-b.get(t,0)**2) for t in C)<=4*d)
    if shared:
        ck(sum(abs(a.get(t,0)) for t in C)<=1);ck(sum(abs(b.get(t,0)) for t in C)<=1)
    for variant in range(3):
        rg=reference(p,variant);rh=reference(q,(variant+1)%3)
        cg=calibrate(p,rg,C);ch=calibrate(q,rh,C)
        ck(sum(cg.values())==sum(ch.values())==1)
        # Exact categorical calibration identity, not a numerical comparison.
        cats_p={j:p[t] for j,t in enumerate(C)};cats_r={j:rg[t] for j,t in enumerate(C)}
        cats_p[len(C)]=1-sum(cats_p.values());cats_r[len(C)]=1-sum(cats_r.values())
        ck(add(add(ce(p,rg),ce(p,cg),F(-1)),kl(cats_p,cats_r),F(-1))=={})
        eg=embed_coeff(cg,positions_g);eh=embed_coeff(ch,positions_h)
        ref={}
        for t in allT:
            r=(eg.get(t,0)+eh.get(t,0))/2;m=marginal[t]
            if m:
                ref[t]=r*true[t]/m;ref[t|(1<<nd)]=r*true[t|(1<<nd)]/m
                if true[t]:ck(ref[t]>0)
                if true[t|(1<<nd)]:ck(ref[t|(1<<nd)]>0)
            else:ref[t]=r;ref[t|(1<<nd)]=F(0)
        ck(sum(ref.values())==1)
        avgD=add(kl(p,cg),kl(q,ch));ck(add(kl(true,ref),avgD,F(-1,2))=={})
        avgC=add(ce(p,cg),ce(q,ch));ck(add(add(ce(true,ref),avgC,F(-1,2)),delta,F(-1))=={})
        ck(sum(eg.get(t,0)+eh.get(t,0) for t in allT)==2)
def run_pairs(mode):
    count=0
    domains=[(2,2,0)] if mode=='disjoint' else [(2,2,1),(3,2,1)]
    for ng,nh,s in domains:
        gt=tables(ng)
        if mode=='shared' and ng==3:gt=[gt[t] for t in [0,1,3,15,23,85,105,255]]
        for g in gt:
            for h in tables(nh):one_pair(g,h,s);count+=1
    return {'Boolean_pairs':count,'reference_cases':3*count}
def bent(k):return [(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k)]
def run_boundary():
    rows=[]
    for k in [4,6,8,10,12]:
        delta=F(1,2**k);e=F(1,2**(k//2));n=2**k
        plus=(n+2**(k//2))//2;minus=n-plus
        hg={};hh={};hf={};B={}
        for sign,count in [(1,plus),(-1,minus)]:
            a=(sign*e-delta)**2;b=delta**2;m=a+b
            hg=add(hg,lograt(delta),-F(count)*delta)
            hh=add(hh,lograt((sign*e-2*delta)**2),-count*(sign*e-2*delta)**2)
            hf=add(hf,lograt(a),-count*a);hf=add(hf,lograt(b),-count*b)
            B=add(B,lograt(a/m),-count*a);B=add(B,lograt(b/m),-count*b)
        D=add(hf,add(hg,hh),F(-1,2))
        lower=add({2:F(k)},lograt(F(16,9)),F(-1))
        ck(upper_zero(add(lower,B,-1/delta)))
        ck(upper_zero(add(B,D,F(-1))))
        ck(plus+minus==n);ck((e-delta)**2>=F(9,16)*delta)
        I=F(k,2)+(k+1)*delta
        ck(I>0);ck(F(k+1)/I<F(5,2))
        if k in [4,6]:
            g=bent(k);h=g.copy();h[0]=-1
            ac=fw(g);bc=fw(h)
            ck(sum(x==e for x in ac.values())==plus)
            ck(all(abs(x)==e and bc[t]==x-2*delta for t,x in ac.items()))
            ig=influences(g);ih=influences(h)
            ck(ig==[F(1,2)]*k);ck(ih==[F(1,2)+2*delta]*k)
            root=[g[x] if z==0 else h[x] for z in range(2) for x in range(n)]
            ck(ent({t:x*x for t,x in fw(root).items()})==hf)
            ck(sum(influences(root))==I)
            # Both children balanced by a single SAME fresh physical character.
            gt=g+[-v for v in g];ht=h+[-v for v in h]
            rt=root+[-v for v in root]
            ck(sum(gt)==sum(ht)==sum(rt)==0)
            ck(ent({t:x*x for t,x in fw(rt).items()})==hf)
            ck(influences(rt)[k]==delta);ck(sum(influences(rt))==I+1)
            ck(F(k+1)/(I+1)<2)
        rows.append({'k':k,'selector_influence':str(delta),'root_influence':str(I),'balanced_root_influence':str(I+1),'lower_Delta_over_selector':f'{k}-log2(16/9)','Delta_prime_log':{str(p):str(v) for p,v in D.items()}})
    return {'parameters':rows,'actual_large_truth_table_enumeration':False}
def run_tensor():
    cases=0
    for k,nq in [(4,2),(6,1)]:
        g=bent(k);h=g.copy();h[0]=-1
        root=g+h;nr=k+1
        pr={t:x*x for t,x in fw(root).items()}
        pg={t:x*x for t,x in fw(g).items()};ph={t:x*x for t,x in fw(h).items()}
        D=add(ent(pr),add(ent(pg),ent(ph)),F(-1,2))
        for qv in tables(nq):
            pq={t:x*x for t,x in fw(qv).items()}
            actual=[a*b for a in qv for b in root]
            law={t:x*x for t,x in fw(actual).items()}
            product={s|(t<<nr):a*b for s,a in pr.items() for t,b in pq.items()}
            ck(law==product);ck(sum(influences(actual))==sum(influences(qv))+sum(influences(root)))
            ck(influences(actual)[k]==F(1,2**k))
            ck(add(ent(law),add(ent(pq),ent(pr)),F(-1))=={})
            gq=[a*b for a in qv for b in g];hq=[a*b for a in qv for b in h]
            pgq={t:x*x for t,x in fw(gq).items()};phq={t:x*x for t,x in fw(hq).items()}
            ck(add(add(ent(law),add(ent(pgq),ent(phq)),F(-1,2)),D,F(-1))=={})
            for variant in range(3):
                rq=reference(pq,variant);rr=reference(pr,(variant+1)%3)
                output={s|(t<<nr):a*b for s,a in rr.items() for t,b in rq.items()}
                ck(sum(output.values())==1)
                ck(add(ce(law,output),add(ce(pq,rq),ce(pr,rr)),F(-1))=={})
                ck(add(kl(law,output),add(kl(pq,rq),kl(pr,rr)),F(-1))=={})
            cases+=1
    return {'Boolean_core_embeddings':cases,'reference_product_cases':3*cases}
if __name__=='__main__':
    mode=sys.argv[1];start=time.perf_counter()
    result=run_boundary() if mode=='boundary' else run_tensor() if mode=='tensor' else run_pairs(mode)
    result.update(status='PASS',assertions=checks,runtime_seconds=time.perf_counter()-start,mode=mode,arithmetic='Fraction + exact prime-log identities + outward rational log bounds')
    (RUN/'out'/f'{mode.upper()}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
