"""A046 review v3: independent probability tables and formal prime-log entropy."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, time, hashlib, itertools, runpy
ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def factors(n):
    ans={}; d=2
    while d*d<=n:
        while n%d==0: ans[d]=ans.get(d,0)+1; n//=d
        d+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans
def plus(*terms):
    out={}
    for c,a in terms:
        for k,v in a.items(): out[k]=out.get(k,Q(0))+c*v
    return {k:v for k,v in out.items() if v}
@lru_cache(None)
def H(law):
    assert sum(law)==1
    out={}
    for p in law:
        if p:
            for n,s in [(p.numerator,-1),(p.denominator,1)]:
                for k,v in factors(n).items(): out[k]=out.get(k,Q(0))+s*p*v
    return {k:v for k,v in out.items() if v}
def law(f,ps):
    out=[Q(0),Q(0)]
    for x,y in enumerate(f):
        w=Q(1)
        for i,p in enumerate(ps): w*=p if x>>i&1 else 1-p
        out[y<0]+=w
    return tuple(out)
@lru_cache(None)
def spectrum(f,ps):
    ans=[]
    for s in range(len(f)):
        a=Q(0); den=Q(1)
        for i,p in enumerate(ps):
            if s>>i&1: den*=p*(1-p)
        for x,y in enumerate(f):
            w=Q(y)
            for i,p in enumerate(ps):
                bit=x>>i&1; w*=p if bit else 1-p
                if s>>i&1: w*=bit-p
            a+=w
        ans.append(a*a/den)
    assert sum(ans)==1
    return tuple(ans)
def child(f,i,b):
    return tuple(f[x] for x in range(len(f)) if (x>>i&1)==b)
@lru_cache(None)
def trees(n):
    return (None,)+tuple((i,a,b) for i in range(n) for a in trees(n-1) for b in trees(n-1)) if n else (None,)
@lru_cache(None)
def ledger(f,ps,t):
    hf=H(spectrum(f,ps)); hy=H(law(f,ps))
    if t is None: return hf,hy,{}, {},{},{}
    i,t0,t1=t; p=ps[i]; rest=ps[:i]+ps[i+1:]
    g,h=child(f,i,0),child(f,i,1)
    sg,sh=spectrum(g,rest),spectrum(h,rest)
    mix=tuple((1-p)*a+p*b for a,b in zip(sg,sh))
    hc=plus((1-p,H(sg)),(p,H(sh)))
    M=plus((1,hf),(-1,H(mix))); J=plus((1,H(mix)),(-1,hc))
    # Physical joint outcome/output law; compute conditioning directly.
    gy,hyc=law(g,rest),law(h,rest)
    joint=tuple((1-p)*z for z in gy)+tuple(p*z for z in hyc)
    c=plus((1,H(joint)),(-1,hy))
    a,b=ledger(g,rest,t0),ledger(h,rest,t1)
    leafF=plus((1-p,a[0]),(p,b[0])); leafY=plus((1-p,a[1]),(p,b[1]))
    MT=plus((1,M),(1-p,a[2]),(p,b[2])); JT=plus((1,J),(1-p,a[3]),(p,b[3]))
    tr=plus((1,H((1-p,p))),(1-p,a[4]),(p,b[4]))
    cond=plus((1,c),(1-p,a[5]),(p,b[5]))
    return leafF,leafY,MT,JT,tr,cond
def coherent(f,order):
    """Full joint root set/transcript by kernels, no information-chain assumption."""
    n=len(order); root=spectrum(f,(Q(1,2),)*n); joint={}; paths={}
    def rec(g,labels,s,weight,path):
        if not labels:
            joint[s,path]=weight; paths[path]=g[0]; return
        orig=order[len(path)]; i=labels.index(orig)
        rest=labels[:i]+labels[i+1:]
        cg,ch=child(g,i,0),child(g,i,1)
        sg=spectrum(cg,(Q(1,2),)*len(rest)); sh=spectrum(ch,(Q(1,2),)*len(rest))
        rem=sum(((s>>j)&1)<<k for k,j in enumerate(rest))
        q=(sg[rem]+sh[rem])/2
        if not weight: return
        assert q>0
        for b,cc,sp in [(0,cg,sg),(1,ch,sh)]:
            w=weight*sp[rem]/(2*q)
            if w: rec(cc,rest,s,w,path+(b,))
    for s,w in enumerate(root):
        if w: rec(f,tuple(range(n)),s,w,())
    marg={}; sy={}
    for (s,path),w in joint.items():
        marg[path]=marg.get(path,Q(0))+w
        key=s,paths[path]; sy[key]=sy.get(key,Q(0))+w
    assert all(w==Q(1,2**n) for w in marg.values())
    MI=plus((1,H(root)),(1,H(tuple(marg.values()))),(-1,H(tuple(joint.values()))))
    got=ledger(f,(Q(1,2),)*n,fulltree(order))[3]
    assert MI==got
    diff=plus((1,MI),(-1,H(law(f,(Q(1,2),)*n))))
    return diff,MI
def fulltree(order):
    if not order: return None
    i=order[0]; rem=tuple(x-(x>i) for x in order[1:]); t=fulltree(rem)
    return i,t,t
def main():
    start=time.perf_counter(); count=0; jointcount=0
    for n in range(4):
        biases=list(itertools.product((Q(1,4),Q(1,2),Q(3,4)),repeat=n)) if n<=2 else [(Q(1,2),)*n]
        for bits in range(2**(2**n)):
            f=tuple(-1 if bits>>x&1 else 1 for x in range(2**n))
            for ps in biases:
                policies=trees(n) if n<=2 else tuple(fulltree(order[:cut]) for order in itertools.permutations(range(n)) for cut in range(n+1))
                for t in policies:
                    lf,ly,M,J,tr,cond=ledger(f,ps,t)
                    hf=H(spectrum(f,ps)); hy=H(law(f,ps))
                    assert hf==plus((1,lf),(1,M),(1,J))
                    assert plus((1,tr),(-1,cond))==plus((1,hy),(-1,ly))
                    # Exact terminal-inclusive A050 ledger, substitute S=.5 H(Pi)-J+M.
                    S=plus((Q(1,2),tr),(-1,J),(1,M))
                    rhs=plus((1,lf),(2,M),(Q(1,2),cond),(Q(1,2),hy),(-Q(1,2),ly),(-1,S))
                    assert hf==rhs; count+=1
            for order in (itertools.permutations(range(n)) if n<=2 else [(0,1,2)]):
                coherent(f,order); jointcount+=1
            ledger.cache_clear()
            if time.perf_counter()-start>55:
                (ROOT/'out'/'PILOT_STOP.json').write_text(json.dumps({'status':'BUDGET_STOP','cases':count,'direct_joint':jointcount,'seconds':time.perf_counter()-start})+'\n')
                raise SystemExit('Budget stop; no full census claim')
    # Independent certified signs for the two opposite compatibility witnesses.
    helper=runpy.run_path(str(ROOT.parent.parent/'20261011T214251Z-account05-A046-current-candidate-intake'/'code'/'exact_check.py')) if False else runpy.run_path(str(ROOT.parent/'20261011T214251Z-account05-A046-current-candidate-intake'/'code'/'exact_check.py'))
    log=helper['log2']; fmt=helper['outward']
    def interval(a):
        lo=hi=Q(0)
        for p,c in a.items():
            x,y=log(Q(p)); lo+=c*(x if c>=0 else y); hi+=c*(y if c>=0 else x)
        return lo,hi
    witnesses=[]
    for f,order,name in [((1,-1),(0,),'one-bit character'),((1,1,1,-1),(0,1),'two-bit AND')]:
        diff,mi=coherent(f,order); bounds=interval(diff)
        assert bounds[1]<0 if name.startswith('one') else bounds[0]>0
        witnesses.append({'name':name,'truth_table':f,'order':order,'difference_prime_log':{str(k):str(v) for k,v in diff.items()},'difference_interval_bits':fmt(bounds),'rational_interval':[str(x) for x in bounds]})
    out={'status':'PASS','tree_function_bias_cases':count,'direct_coherent_joint_cases':jointcount,'assertions':3*count+jointcount+2,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction and formal prime-log equality; rational 24-term logarithm sign intervals','witnesses':witnesses}
    (ROOT/'out'/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
