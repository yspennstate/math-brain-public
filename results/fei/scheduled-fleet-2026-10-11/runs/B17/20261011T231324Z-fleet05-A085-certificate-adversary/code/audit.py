"""A085 independent certificate audit. Only writes beneath its own run."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from collections import defaultdict,Counter
from pathlib import Path
from math import prod,comb
import json,time,sys,hashlib
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
TEAM=Path(r'~\brain_workers\FEI100_20261011\agents')
def source(a): return next(p for p in (TEAM/a/'runs').iterdir() if p.is_dir())
START=time.perf_counter(); checks=0
def ck(v):
    global checks
    assert v; checks+=1
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf8')
def guard(limit):
    if time.perf_counter()-START>limit: raise RuntimeError('Frozen runtime exceeded')
S=1<<96; N=28
@lru_cache(None)
def natural_unit(x):
    ck(1<=x<=2)
    z=(x-1)/(x+1); power=z; zz=z*z; lo=0
    for j in range(N):
        t=2*S*power/(2*j+1); lo+=t.numerator//t.denominator; power*=zz
    tail=2*S*power/((2*N+1)*(1-zz))
    return lo,lo+N+(tail.numerator+tail.denominator-1)//tail.denominator
@lru_cache(None)
def log(x):
    ck(x>0)
    a,b=x.numerator,x.denominator; k=a.bit_length()-b.bit_length()
    r=x/(Q(2)**k)
    if r<1: k-=1; r*=2
    ck(1<=r<2)
    if r==1: return Q(k),Q(k)
    l,u=natural_unit(r); dl,du=natural_unit(Q(2)); ck(dl>0)
    # Positive numerator divided BEFORE adding the exact possibly negative k.
    return Q(k)+Q(l,du),Q(k)+Q(u,dl)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def sub(a,b): return add(a,scale(-1,b))
@lru_cache(None)
def entropy(dist):
    ck(sum(dist)==1 and all(x>=0 for x in dist)); ans=(Q(0),Q(0))
    for x in dist:
        if x: ans=add(ans,scale(-x,log(x)))
    return ans
@lru_cache(None)
def spectrum(table,ps):
    # Tensor transform in the basis 1,(x-p); coefficients have no radicals.
    a=list(map(Q,table)); n=len(ps)
    for i,p in enumerate(ps):
        for x in range(1<<n):
            if not x>>i&1:
                u,v=a[x],a[x|(1<<i)]
                a[x]=(1-p)*u+p*v; a[x|(1<<i)]=v-u
    result=tuple(a[s]**2*prod(ps[i]*(1-ps[i]) for i in range(n) if s>>i&1) for s in range(1<<n))
    ck(sum(result)==1 and all(x>=0 for x in result)); return result
def marginal(P,coords):
    return tuple(sum(v for s,v in enumerate(P) if sum(((s>>i)&1)<<j for j,i in enumerate(coords))==t) for t in range(1<<len(coords)))
def defect(table,ps,mask):
    n=len(ps); A=[i for i in range(n) if mask>>i&1]; B=[i for i in range(n) if not mask>>i&1]
    parent=spectrum(table,ps); q=marginal(parent,B); mix=[Q(0)]*len(q); avg=(Q(0),Q(0))
    for z in range(1<<len(A)):
        w=prod(ps[i] if z>>j&1 else 1-ps[i] for j,i in enumerate(A))
        child=tuple(table[sum(((z>>j)&1)<<i for j,i in enumerate(A))+sum(((y>>j)&1)<<i for j,i in enumerate(B))] for y in range(1<<len(B)))
        c=spectrum(child,tuple(ps[i] for i in B)); avg=add(avg,scale(w,entropy(c)))
        for t,v in enumerate(c): mix[t]+=w*v
    ck(tuple(mix)==q)
    delta=(Q(0),Q(0))
    for i in A: delta=add(delta,add(entropy((ps[i],1-ps[i])),log(max(ps[i],1-ps[i]))))
    d=add(add(entropy(parent),scale(-2,entropy(q))),add(avg,delta))
    return d,parent,q,avg
@lru_cache(None)
def factor(x):
    result={}; d=2
    while d*d<=x:
        while x%d==0: result[d]=result.get(d,0)+1; x//=d
        d+=1
    if x>1: result[x]=result.get(x,0)+1
    return result
def zero_defect(table,ps,mask,parent,q):
    logs=defaultdict(Q)
    def ent(dist,c):
        for v in dist:
            if v: logs[v]-=c*v
    ent(parent,1); ent(q,-2)
    A=[i for i in range(3) if mask>>i&1]; B=[i for i in range(3) if not mask>>i&1]
    for z in range(1<<len(A)):
        w=prod(ps[i] if z>>j&1 else 1-ps[i] for j,i in enumerate(A))
        child=tuple(table[sum(((z>>j)&1)<<i for j,i in enumerate(A))+sum(((y>>j)&1)<<i for j,i in enumerate(B))] for y in range(1<<len(B)))
        ent(spectrum(child,tuple(ps[i] for i in B)),w)
    for i in A: ent((ps[i],1-ps[i]),1); logs[max(ps[i],1-ps[i])]+=1
    primes=defaultdict(Q)
    for x,c in logs.items():
        if c:
            for p,e in factor(x.numerator).items(): primes[p]+=c*e
            for p,e in factor(x.denominator).items(): primes[p]-=c*e
    ck(all(c==0 for c in primes.values()))
    return len(primes)
def coverage():
    counts=Counter(); maps=0
    for ms in product((1,2,4,6,7),repeat=3):
        flip=sum(1<<i for i,m in enumerate(ms) if m>4); low=tuple(min(m,8-m) for m in ms)
        for bits in range(256):
            t=tuple(-1 if bits>>x&1 else 1 for x in range(8)); mapped=tuple(t[x^flip] for x in range(8)); sign=mapped[0]
            mapped=tuple(sign*v for v in mapped); code=sum((mapped[x]==-1)<<(x-1) for x in range(1,8))
            ck(0<=code<128 and mapped[0]==1); counts[(low,code)]+=1; maps+=1
    ck(len(counts)==27*128 and sum(counts.values())*6==192000)
    return {'raw_grid':192000,'representatives':len(counts)*6,'table_bias_maps':maps,'orbit_multiplicities':dict(Counter(counts.values()))}
def grid(pilot):
    count=zero=positive=ambiguous=0; minimum=None; minrow=None; zeros=[]
    biases=[(4,4,4)] if pilot else product((1,2,4),repeat=3)
    for ms in biases:
        ps=tuple(Q(m,8) for m in ms)
        for code in range(128):
            table=tuple(1 if x==0 or not code>>(x-1)&1 else -1 for x in range(8))
            for mask in range(1,7):
                d,P,q,avg=defect(table,ps,mask); count+=1
                if d[0]>0:
                    positive+=1
                    if minimum is None or d[0]<minimum: minimum=d[0]; minrow={'code':code,'ms':ms,'mask':mask,'lower':str(d[0]),'upper':str(d[1])}
                elif d==(0,0): zero+=1
                else:
                    ambiguous+=1; ck(d[1]>=0); zero_defect(table,ps,mask,P,q); zero+=1; zeros.append([list(ms),code,mask])
        guard(55 if pilot else 180)
        if not pilot: save('grid_checkpoint.json',{'cases':count,'zeros':zero,'positives':positive,'elapsed':time.perf_counter()-START})
    ck(count==(768 if pilot else 20736)); ck(count==zero+positive)
    original=json.loads((source('A071')/'out/search.json').read_text())
    zorig=json.loads((source('A071')/'out/zero_certificates.json').read_text())
    if not pilot:
        ck(positive==19632 and zero==1104 and ambiguous==600)
        ck({(tuple(ms),c,m) for ms,c,m in zeros}=={(tuple(r['bias_numerators_over_8']),r['code'],r['block_mask']) for r in zorig['certificates']})
        ck(minrow['code']==4 and tuple(minrow['ms'])==(1,1,4) and minrow['mask']==4)
        ck(minimum>Q(5,2048))
    result={'cases':count,'positive':positive,'zero':zero,'resolved_by_prime_identity':ambiguous,'minimum':minrow,'checks':checks,'seconds':time.perf_counter()-START,'independent_transform':True,'independent_log_checker':True}
    save('pilot.json' if pilot else 'grid_audit.json',result); print(json.dumps(result),flush=True)
def interval_value(row,key): return tuple(Q(row[key][side]) for side in ('lower','upper'))
def overlaps(a,b): return max(a[0],b[0])<=min(a[1],b[1])
def contained(inner,outer): return outer[0]<=inner[0]<=inner[1]<=outer[1]
@lru_cache(None)
def fine_log(x):
    # Exact 44-term rational series, tighter than A047's 40-term enclosure.
    ck(x>0); k=x.numerator.bit_length()-x.denominator.bit_length(); r=x/(Q(2)**k)
    if r<1: r*=2; k-=1
    def unit(t):
        z=(t-1)/(t+1); zz=z*z; power=z; total=Q(0)
        for j in range(44): total+=2*power/(2*j+1); power*=zz
        return total,total+2*power/(89*(1-zz))
    a,b=unit(r); dl,du=unit(Q(2))
    return k+a/du,k+b/dl
def finite_reviews():
    global log
    coarse_log=log
    log=fine_log
    # A047 full parent transform, rather than its two-child fiber formula.
    r47=source('A047'); rows=json.loads((r47/'out/results.json').read_text())['finite']; unequal=json.loads((r47/'out/unequal.json').read_text())
    cases={'constant_to_quarter_defect':([1]*4,[-1,1,1,1]),'constant_to_balanced':([1]*4,[-1,-1,1,1]),'dictator_to_balanced_quarter_surgery':([1,-1]*4,[-1,1,1,-1,1,-1,1,-1]),'equal_children':([1,-1],[1,-1]),'opposite_children':([1,-1],[-1,1])}
    reviewed47=[]
    for row in rows:
        g,h=cases[row['label']]; p=Q(row['p']); n=(len(g)).bit_length()-1
        table=tuple(g[x>>1] if not x&1 else h[x>>1] for x in range(2*len(g)))
        ps=(p,)+(Q(1,2),)*n; d,P,q,avg=defect(table,ps,1)
        ck(tuple(Q(x) for x in row['joint'])==P)
        M=sub(entropy(P),entropy(q)); J=sub(entropy(q),avg); debt=sub(J,M)
        for key,val in [('M',M),('J',J),('debt',debt)]: ck(contained(val,interval_value(row,key)))
        if row['label'] in ('constant_to_quarter_defect','dictator_to_balanced_quarter_surgery'): ck(debt[0]>0)
        if row['label']=='opposite_children': ck(debt[1]<0)
        reviewed47.append({'label':row['label'],'p':str(p),'debt_bounds':list(map(str,debt))})
        guard(55)
    for row in unequal:
        p,q=Q(row['p']),Q(row['q']); table=(1,1,1,-1); P=spectrum(table,(p,q)); ck(P==tuple(Q(x) for x in row['spectrum']))
        d,_,marg,avg=defect(table,(p,q),1); debt=sub(sub(entropy(marg),avg),sub(entropy(P),entropy(marg)))
        ck(contained(debt,interval_value(row,'debt'))); ck(debt[0]>0 if p<Q(1,2) else debt[1]<0)
        reviewed47.append({'p':str(p),'q':str(q),'debt_bounds':list(map(str,debt))})
        guard(55)
    # A042 independently sum corrected entropy over compressed spectral atoms.
    log=coarse_log
    entropy.cache_clear()
    original42=json.loads((source('A042')/'out/CHECK_OUTPUT.json').read_text()); reviews42=[]
    ln2=log(Q(2)) # exact log2(2)=1; natural conversion uses independent ln enclosure below.
    l,u=natural_unit(Q(2)); ln2nat=(Q(l,S),Q(u,S))
    def hnat(x):
        bits=entropy((x,1-x)); return bits[0]*ln2nat[0],bits[1]*ln2nat[1]
    def natlog(x):
        a=log(x); corners=[v*w for v in a for w in ln2nat]; return min(corners),max(corners)
    for row in original42['weighted_rational_log_certificates']:
        m=row['m']; q=Q(1,m*m); r=q**m; a=(m-1)*r/(1+(m-1)*r); z=1-a; alpha=a+z*r
        atoms=[(Q(1),(2*alpha-1)**2,0,1),(4*a*z,4*a*z*(1-r)**2,1,1)]
        for k in range(1,m+1):
            W=(4*q*(1-q))**k; v=r*r*((1-q)/q)**k
            atoms += [(W,4*z*z*v,k,comb(m,k)),(4*a*z*W,4*a*z*v,k+1,comb(m,k))]
        ck(sum(P*mul for W,P,k,mul in atoms)==1)
        I=sum(k*P*mul for W,P,k,mul in atoms); V=1-atoms[0][1]; D=I-V; ck(D>0)
        E=(Q(0),Q(0))
        for W,P,k,mul in atoms:
            if k and P: ck(0<P<=W); E=add(E,scale(P*mul,log(W/P)))
        ratio=scale(1/D,E); ck(contained(ratio,tuple(map(Q,row['Hplus_over_deficit_bits']))))
        eta=Q(1,m); t=eta+(1-eta)*q; TC=sub(scale(m,hnat(t)),scale(m-1,hnat(q))); tc=scale(alpha/I,TC)
        ck(contained(tc,tuple(map(Q,row['event_TC_over_I_nats']))))
        I0=4*a*z*(1-r); Il=4*m*z*r*(1-q)
        residual=add(scale(V,natlog(1/V)),add(scale(-I0,natlog((1-r)/(alpha*(1-alpha)))),scale(-Il,natlog(Q(m)/(1-alpha)))))
        credit=scale(1/I,residual); ck(contained(credit,tuple(map(Q,row['unit_pivotal_residual_over_I_nats']))))
        reviews42.append({'m':m,'Hplus_D':list(map(str,ratio)),'TC_I':list(map(str,tc)),'credit_I':list(map(str,credit))})
        guard(55)
    # Exact closed-boundary transform needs contraction. No log(0) is evaluated.
    boundary=[]
    for fixed in (0,1):
        ps=(Q(fixed),Q(1,3)); P=spectrum((1,1,1,-1),ps)
        restricted=(1,1) if fixed==0 else (1,-1); child=spectrum(restricted,(Q(1,3),))
        ck(P[1]==P[3]==0 and marginal(P,[1])==child)
        boundary.append({'fixed_X':fixed,'parent':list(map(str,P)),'contracted':list(map(str,child))})
    # Exact low-dimensional endpoint minimality, not a new all-pair census.
    maxcoeff={}
    for n in (0,1):
        size=1<<n; tabs=[tuple(1 if b>>x&1 else -1 for x in range(size)) for b in range(1<<size)]; best=-10
        for g in tabs:
            G=[Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(g)),size) for s in range(size)]
            for h in tabs:
                H=[Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(h)),size) for s in range(size)]
                Z=sum(v*v for u,v in zip(G,H) if not u); c=Q(sum(u*v for u,v in zip(g,h)),size); coeff=2*Z+2*c-2
                ck(coeff<=0); best=max(best,coeff)
        maxcoeff[str(n)]=str(best)
    save('finite_scope_audit.json',{'A047_cases':len(reviewed47),'A047':reviewed47,'A042_cases':len(reviews42),'A042':reviews42,'deterministic_contractions':boundary,'endpoint_low_dimension_max':maxcoeff,'checks':checks,'seconds':time.perf_counter()-START})
    print(json.dumps({'A047_cases':len(reviewed47),'A042_cases':len(reviews42),'checks':checks,'seconds':time.perf_counter()-START}),flush=True)
def main():
    mode=sys.argv[1]
    for k in (-1075,-100,-1,0,1,100,1075): ck(log(Q(2)**k)==(Q(k),Q(k)))
    ck(entropy((Q(0),Q(1)))==(0,0))
    if mode=='pilot': grid(True)
    elif mode=='grid':
        c=coverage(); save('coverage_audit.json',c); print(json.dumps(c),flush=True); grid(False)
    elif mode=='finite': finite_reviews()
    else: raise ValueError(mode)
if __name__=='__main__': main()
