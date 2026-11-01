"""A078 v1: exact actual-Boolean parity-code checks; no numerical entropy."""
import itertools, json, sys, time
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
COUNT=0
def check(x):
    global COUNT
    COUNT+=1
    assert x
def parity(x): return x.bit_count()&1
def rank(vs):
    piv={}
    for v in vs:
        while v:
            k=v.bit_length()
            if k in piv: v^=piv[k]
            else: piv[k]=v; break
    return len(piv)
def walsh(t):
    a=list(t); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return a
def directional(t):
    return [sum(t[x]!=t[x^v] for x in range(len(t))) for v in range(len(t))]
def minimum(cost,m):
    selected=[]
    for v in sorted(range(1,1<<m),key=lambda v:(cost[v],v)):
        if rank(selected+[v])>len(selected): selected.append(v)
        if len(selected)==m: break
    return sum(cost[v] for v in selected),selected
def lifted(t,cols,shift=0):
    out=[]
    for x in range(1<<len(cols)):
        z=0
        for j,v in enumerate(cols):
            if (x>>j)&1: z^=v
        out.append(t[z]*(-1 if parity(x&shift) else 1))
    return out
def verify_code(t,m,cols,shift):
    N=len(cols); size=1<<N; seedsize=1<<m
    f=lifted(t,cols,shift); a=walsh(t); b=walsh(f)
    want=[0]*size
    for s,w in enumerate(a):
        dest=shift
        for j,v in enumerate(cols): dest^=parity(s&v)<<j
        want[dest]=w*(size//seedsize)
    check(b==want)
    check(sum(w*w for w in b)==size*size)
    dc=directional(t)
    for j,v in enumerate(cols):
        c=dc[v] if not ((shift>>j)&1) else seedsize-dc[v]
        edges=sum(f[x]!=f[x^(1<<j)] for x in range(size))
        check(edges*seedsize==c*size)
    check(sorted(w*w*seedsize*seedsize for w in b if w)==sorted(w*w*size*size for w in a if w))
    fold=[min(c,seedsize-c) for c in dc]
    opt,_=minimum(fold,m)
    check(sum(dc[v] if not ((shift>>j)&1) else seedsize-dc[v] for j,v in enumerate(cols))>=opt)
def main():
    start=time.perf_counter(); pilot='--pilot' in sys.argv
    cases={}; records=[]
    # Exhaustive tables and unordered bases: no output-sign quotient.
    maxm=2 if pilot else 3
    for m in range(1,maxm+1):
        size=1<<m; bases=[b for b in itertools.combinations(range(1,size),m) if rank(b)==m]
        tables=1<<size
        for tab in range(tables):
            t=[-1 if (tab>>x)&1 else 1 for x in range(size)]
            dc=directional(t); fold=[min(c,size-c) for c in dc]
            opt,b=minimum(fold,m)
            check(opt==min(sum(fold[v] for v in q) for q in bases))
            shift=sum((dc[v]>size-dc[v])<<j for j,v in enumerate(b))
            verify_code(t,m,b,shift)
            check(sum(directional(lifted(t,b,shift))[1<<j] for j in range(m))==opt)
        cases['basis_tables_m'+str(m)]=tables
    # All surjective 2-output maps from three physical bits, all modulations.
    m=2; codes=[c for c in itertools.product(range(4),repeat=3) if rank(c)==2]
    limit=2 if pilot else 16
    for tab in range(limit):
        t=[-1 if (tab>>x)&1 else 1 for x in range(4)]
        for cols in codes:
            for shift in range(8): verify_code(t,m,cols,shift)
    cases['rank2_codes']=len(codes); cases['rank2_lifts']=limit*len(codes)*8
    # Systematic 3-bit seeds plus all one-bit parity auxiliaries, all modulation.
    limit=4 if pilot else 256
    for tab in range(limit):
        t=[-1 if (tab>>x)&1 else 1 for x in range(8)]
        for v in range(8):
            for shift in range(16): verify_code(t,3,[1,2,4,v],shift)
    cases['systematic_lifts']=limit*8*16
    # Tensor optimum independently enumerated over every unordered 4D basis.
    bases4=[b for b in itertools.combinations(range(1,16),4) if rank(b)==4]
    lim=2 if pilot else 16
    for ta in range(lim):
        a=[-1 if (ta>>x)&1 else 1 for x in range(4)]; da=directional(a)
        oa,_=minimum([min(c,4-c) for c in da],2)
        for tb in range(lim):
            b=[-1 if (tb>>x)&1 else 1 for x in range(4)]; db=directional(b)
            ob,_=minimum([min(c,4-c) for c in db],2)
            t=[a[x&3]*b[x>>2] for x in range(16)]; dt=directional(t)
            fold=[min(c,16-c) for c in dt]
            check(min(sum(fold[v] for v in q) for q in bases4)==4*(oa+ob))
            for v in range(16):
                check(16-2*dt[v]==(4-2*da[v&3])*(4-2*db[v>>2]))
    cases['tensor_pairs']=lim*lim; cases['unordered_4D_bases']=len(bases4)
    # Concrete complete-simplex padding (full Boolean truth tables).
    for m in range(2,4):
        t=[-1]+[1]*((1<<m)-1); cols=list(range(1,1<<m))
        verify_code(t,m,cols,0)
        d=directional(lifted(t,cols)); check(sum(d[1<<j] for j in range(len(cols)))==2*((1<<m)-1)*(1<<(len(cols)-m)))
    # Exact asymptotic family inputs and basis minima, compressed arithmetic.
    for dims in [(2,),(3,),(4,),(2,2),(2,3),(3,3),(2,2,2)]:
        m=sum(dims); size=1<<m; cost=[]
        for v in range(size):
            rho=F(1); off=0
            for r in dims:
                if (v>>off)&((1<<r)-1): rho*=1-F(4,1<<r)
                off+=r
            cost.append((1-abs(rho))/2)
        opt,b=minimum(cost,m); want=sum(F(2*r,1<<r) for r in dims)
        check(opt==want)
        records.append({'point_defect_tensor_dimensions':dims,'optimized_influence':str(opt),'basis':b})
    result={'helper':'A078-exact-code-v1','mode':'pilot' if pilot else 'full','status':'PASS','assertions':COUNT,'cases':cases,'records':records,'seconds':time.perf_counter()-start,'arithmetic':'integer Walsh/physical edges; Fraction compressed laws; entropy preservation checked by exact probability multiset; no floating entropy'}
    out=ROOT/'out'/('pilot.json' if pilot else 'validation.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
