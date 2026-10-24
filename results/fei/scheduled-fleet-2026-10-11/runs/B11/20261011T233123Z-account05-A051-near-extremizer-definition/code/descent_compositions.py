"""v1: exact read-once NAND composition census and physical block orbits."""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter, defaultdict
from itertools import product, combinations_with_replacement
from pathlib import Path
import json, time, sys, math

ROOT=Path(__file__).resolve().parent.parent
ASSERTIONS=0
def ck(x):
    global ASSERTIONS
    assert x
    ASSERTIONS+=1
def save(path,obj):
    (ROOT/path).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

# () = literal, tuples of >=2 children = NAND. Polarity on every edge is fixed.
@lru_cache(None)
def size(t):
    if isinstance(t,int): return 0
    if t==(): return 1
    if t[0]=='~': return size(t[1])
    return sum(size(x) for x in t)
def neg(t):
    if isinstance(t,int): return 1-t
    if t and t[0]=='~': return t[1]
    return ('~',t)
def nand(children):
    if 0 in children: return 1
    a=[x for x in children if x!=1]
    if not a: return 0
    if len(a)==1: return neg(a[0])
    return tuple(sorted(a,key=repr))
@lru_cache(None)
def tables(t):
    if isinstance(t,int): return (t,)
    if t==(): return (0,1)
    if t[0]=='~': return tuple(1-x for x in tables(t[1]))
    ts=[tables(x) for x in t]; dims=[size(x) for x in t]
    ans=[]
    for z in range(1<<sum(dims)):
        offset=0; allone=1
        for a,d in zip(ts,dims):
            allone &= a[(z>>offset)&((1<<d)-1)]; offset+=d
        ans.append(1-allone)
    return tuple(ans)
@lru_cache(None)
def factor(v):
    ans={}; p=2
    while p*p<=v:
        while v%p==0: ans[p]=ans.get(p,0)+1; v//=p
        p+=1
    if v>1: ans[v]=ans.get(v,0)+1
    return ans
def add(terms):
    ans=defaultdict(F)
    for scale,d in terms:
        for p,a in d.items(): ans[p]+=scale*a
    return {p:a for p,a in ans.items() if a}
def fwht(a):
    a=list(a); step=1
    while step<len(a):
        for k in range(0,len(a),2*step):
            for j in range(k,k+step):
                u,v=a[j],a[j+step]; a[j],a[j+step]=u+v,u-v
        step*=2
    return a
def spectrum_table(t):
    a=fwht([2*x-1 for x in t]); n=(len(t)-1).bit_length(); den=1<<(2*n)
    ck(sum(x*x for x in a)==den)
    d=defaultdict(int); d[2]=2*n*den
    for v in a:
        if v:
            for p,e in factor(abs(v)).items(): d[p]-=2*v*v*e
    H={p:F(x,den) for p,x in d.items() if x}
    ii=[F(sum(v*v for s,v in enumerate(a) if s>>i&1),den) for i in range(n)]
    edge=[F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]
    ck(ii==edge)
    return H,ii
@lru_cache(None)
def stats(t): return spectrum_table(tables(t))
def restrict(t,values):
    it=iter(values)
    def rec(u):
        if u==():
            x=next(it); return () if x is None else x
        return nand([rec(x) for x in u])
    return rec(t)

@lru_cache(None)
def partitions(n,low=1):
    ans=[]
    for k in range(low,n+1):
        if k==n: ans.append((k,))
        else:
            ans += [(k,)+a for a in partitions(n-k,k)]
    return tuple(ans)
@lru_cache(None)
def trees(n):
    if n==1: return ((),)
    ans=set()
    for parts in partitions(n):
        if len(parts)==1: continue
        groups=[]
        for s,r in sorted(Counter(parts).items()):
            groups.append(list(combinations_with_replacement(trees(s),r)))
        for blocks in product(*groups):
            ans.add(tuple(sorted(sum((list(x) for x in blocks),[]),key=repr)))
    return tuple(sorted(ans,key=repr))

# Each orbit is (canonical selected mask, exact labelled-orbit multiplicity).
@lru_cache(None)
def orbits(t):
    if t==(): return ((0,1),(1,1))
    groups=[]; offsets=[]; offset=0
    for child,r in sorted(Counter(t).items(),key=lambda a:repr(a[0])):
        opts=orbits(child); d=size(child); gg=[]
        for ix in combinations_with_replacement(range(len(opts)),r):
            mask=0; mult=math.factorial(r)
            for count in Counter(ix).values(): mult//=math.factorial(count)
            for j,k in enumerate(ix):
                mask|=opts[k][0]<<(j*d); mult*=opts[k][1]
            gg.append((mask,mult))
        groups.append(gg); offsets.append(offset); offset+=d*r
    ans=[]
    for choices in product(*groups):
        mask=sum(a<<offset for (a,m),offset in zip(choices,offsets))
        mult=math.prod(m for a,m in choices); ans.append((mask,mult))
    ck(sum(m for a,m in ans)==1<<size(t))
    return tuple(ans)

# Rational atanh-series enclosure; no library transcendental approximations.
BITS=110
def ln_reduced(x,K=48):
    z=(x-1)/(x+1); z2=z*z; power=z; ans=F(0)
    for j in range(K): ans+=2*power/(2*j+1); power*=z2
    return ans,ans+2*power/((2*K+1)*(1-z2))
LN2=ln_reduced(F(2))
@lru_cache(None)
def logprime(p):
    k=p.bit_length()-1; lo,hi=ln_reduced(F(p,1<<k))
    a=F(k)+lo/LN2[1]; b=F(k)+hi/LN2[0]
    scale=1<<BITS
    return F(a.numerator*scale//a.denominator,scale),F(-(-b.numerator*scale//b.denominator),scale)
def interval(d):
    lo=hi=F(0)
    for p,c in d.items():
        a,b=logprime(p)
        if c<0: a,b=b,a
        lo+=c*a; hi+=c*b
    return lo,hi
def enc(d): return {str(p):str(a) for p,a in sorted(d.items())}
def ei(v): return [str(x) for x in v]

def evaluate(t,deadline):
    n=size(t); H,ii=stats(t); I=sum(ii); rows=[]
    for mask,mult in orbits(t):
        if not mask or mask==(1<<n)-1: continue
        a=mask.bit_count(); selected=[i for i in range(n) if mask>>i&1]
        counts=Counter()
        for z in range(1<<a):
            vals=[None]*n
            for j,i in enumerate(selected): vals[i]=(z>>j)&1
            counts[restrict(t,vals)]+=1
        avgh=add((F(count,1<<a),stats(u)[0]) for u,count in counts.items())
        avgi=sum(F(count,1<<a)*sum(stats(u)[1]) for u,count in counts.items())
        IA=sum(ii[i] for i in selected); ck(IA+avgi==I)
        L=add([(1,H),(-1,avgh)]); ratio={p:c/IA for p,c in L.items()}
        rows.append({'mask':mask,'orbit_size':mult,'selected_count':a,'I_A':str(IA),'L':enc(L),'ratio':enc(ratio),'interval':ei(interval(ratio))})
        if time.perf_counter()>deadline: raise TimeoutError('Frozen cap reached')
    minupper=min(F(r['interval'][1]) for r in rows)
    candidates=[r for r in rows if F(r['interval'][0])<=minupper]
    ck(all(r['ratio']==candidates[0]['ratio'] for r in candidates))
    # Identical symbolic ratios are exact ties; all others are interval-separated.
    winner=candidates[0]; phi=interval({int(p):F(c) for p,c in winner['ratio'].items()})
    R=interval({p:c/I for p,c in H.items()}); relative=(phi[0]/R[1],phi[1]/R[0])
    ck(sum(r['orbit_size'] for r in rows)==(1<<n)-2)
    return {'n':n,'tree':repr(t),'truth_sha256':__import__('hashlib').sha256(bytes(tables(t))).hexdigest(),'H':enc(H),'I':str(I),'ratio_H_I':ei(R),'phi':ei(phi),'phi_over_H_I':ei(relative),'minimizing_masks':[r['mask'] for r in candidates],'minimizing_block_sizes':sorted(set(r['selected_count'] for r in candidates)),'phi_gt_227_over_50':phi[0]>F(227,50),'block_orbits':len(rows),'labelled_blocks':sum(r['orbit_size'] for r in rows),'all_orbits':rows}

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    start=time.perf_counter(); cap=55 if mode=='pilot' else 1200
    family=[(((),(),()),((),(),())),(((),()),((),()),((),()))] if mode=='pilot' else [t for n in range(6,10) for t in trees(n)]
    result=[]
    for j,t in enumerate(family):
        r=evaluate(t,start+cap); result.append({k:v for k,v in r.items() if k!='all_orbits'})
        save('out/'+mode+'_case_'+str(j).zfill(4)+'.json',r)
        if j%20==0: print('completed',j+1,'of',len(family),flush=True)
        save('out/'+mode+'_SUMMARY.json',{'helper_version':'A051-descent-compositions-v1','case_count':len(family),'completed':j+1,'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-start,'cases':result})
    print(json.dumps({'status':'PASS','mode':mode,'cases':len(family),'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-start,'tree_counts':{n:len(trees(n)) for n in range(6,10)},'above_threshold':sum(r['phi_gt_227_over_50'] for r in result)},indent=2))
if __name__=='__main__': main()
