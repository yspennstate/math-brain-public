from pathlib import Path
from fractions import Fraction as Q
import importlib.util, json, time, argparse, itertools

RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parents[0]/'20261011T234442Z-account05-A002-hardness-preserving-transformations'/'code/check.py'
spec=importlib.util.spec_from_file_location('old_exact',OLD)
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
assertions=0
deadline=None
def ck(v):
    global assertions
    if deadline is not None and time.perf_counter()>deadline:raise TimeoutError('Frozen 60-second runtime exceeded')
    assertions+=1
    assert v, assertions
def shift(p,c):return {v^c:x for v,x in p.items()}
def mix(p,q):return {v:(p.get(v,Q(0))+q.get(v,Q(0)))/2 for v in p.keys()|q.keys()}
def signs(n,mask):return [1 if mask>>x&1 else -1 for x in range(1<<n)]
def psign(v):return -1 if v.bit_count()%2 else 1
def fixture(vals,k,m,tags):
    N=1<<m;kmask=(1<<k)-1;nm=k+2*m
    a=M.fwht(vals);p=M.probabilities(a);h=M.H(p);b=M.B(p,k);di=M.inf(p,k)
    truth=[]
    for u in range(1<<nm):
        x=u&kmask;aa=(u>>k)&(N-1);bb=u>>(k+m)
        truth.append(vals[x]*psign(aa&bb)*psign(tags[bb]&x))
    direct=M.fwht(truth);expected={}
    for s in range(N):
        for tt in range(N):
            for v,amp in a.items():expected[(v^tags[s])|(s<<k)|(tt<<(k+m))]=Q(psign(s&tt),N)*amp
    ck(direct==expected)
    pp=M.probabilities(direct);bv=M.Bvec(pp,nm);dd=M.inf(pp,nm)
    ck(sum(pp.values())==1)
    ck(M.H(pp)==M.add((1,h),(1,((2,Q(2*m)),))))
    for i in range(k):
        theta=Q(sum(c>>i&1 for c in tags),N)
        ck(dd[i]==di[i]+theta*(1-2*di[i]));ck(bv[i]==M.Bvec(p,k)[i])
    jterms=[];different=False
    for j in range(m):
        pieces=[]
        for s in range(N):
            if s>>j&1:continue
            p0=shift(p,tags[s]);p1=shift(p,tags[s|(1<<j)])
            js=M.add((1,M.H(mix(p0,p1))),(-1,h))
            ck((js==())==(p0==p1))
            different|=p0!=p1
            pieces.append((Q(2,N),js))
        jj=M.add(*pieces);jterms.append(jj)
        ck(bv[k+j]==M.add((1,((2,Q(1)),)),(-1,jj)))
        ck(bv[k+m+j]==((2,Q(1)),))
        ck(dd[k+j]==Q(1,2) and dd[k+m+j]==Q(1,2))
    J=M.add(*[(1,x) for x in jterms])
    bb=M.add((1,b),(1,((2,Q(2*m)),)),(-1,J))
    ck(M.B(pp,nm)==bb)
    ck(M.add((1,M.H(pp)),(-1,bb))==M.add((1,h),(-1,b),(1,J)))
    ck((J==())== (not different))
    # Independent physical-edge influence verification.
    for i in range(nm):
        physical=Q(sum(truth[u]!=truth[u^(1<<i)] for u in range(1<<nm)),1<<nm)
        ck(physical==dd[i])
    return J,sum(dd)
def run(pilot):
    global deadline
    deadline=time.perf_counter()+60
    start=time.perf_counter();counts={'basis':0,'all_small_maps':0,'balanced_tensors':0,'canonical_tensors':0}
    nmax=2 if pilot else 3
    for n in range(1,nmax+1):
        m=(n).bit_length();N=1<<m
        for mask in range(1<<(1<<n)):
            vals=signs(n,mask);fixture(vals,n,m,[1<<i for i in range(n)]+[0]*(N-n));counts['basis']+=1
    for n in [1,2]:
        for mask in range(1<<(1<<n)):
            for tags in itertools.product(range(1<<n),repeat=2):
                fixture(signs(n,mask),n,1,tags);counts['all_small_maps']+=1
    if not pilot:
        for mask in range(16):
            vals=signs(2,mask);a=M.fwht(vals);p=M.probabilities(a);di=M.inf(p,2)
            canonical_mask=sum(1<<i for i,d in enumerate(di) if d>Q(1,2))
            canon=[v*psign(x&canonical_mask) for x,v in enumerate(vals)]
            for t in [1,2]:
                for parity in [0,1]:
                    k=2*t+parity;m=k.bit_length();N=1<<m;g=[]
                    for x in range(1<<k):
                        val=1
                        for q in range(t):val*=(canon if not parity else vals)[(x>>(2*q))&3]
                        if parity:val*=psign(x>>(2*t))
                        g.append(val)
                    J,If=fixture(g,k,m,[1<<i for i in range(k)]+[0]*(N-k))
                    counts['balanced_tensors' if parity else 'canonical_tensors']+=1
                    gp=M.probabilities(M.fwht(g))
                    ck(M.H(gp)==M.add((t,M.H(p))))
                    ck(M.B(gp,k)==M.add((t,M.B(p,2))))
                    if not parity:
                        Istar=sum(min(d,1-d) for d in di)
                        ck(If>=t*Istar+m)
    result={'helper_version':'A002-correlated-tag-v2','pilot':pilot,'fixture_counts':counts,'fixture_executions':sum(counts.values()),'exact_assertions':assertions,'failures':0,'seconds':time.perf_counter()-start,'max_dimension':6 if pilot else 11,'arithmetic':'integer signed FWHT; Fraction masses, influence, physical edges; formal prime-log entropy identities','observed_process_memory':'not measured; frozen estimate below 100 MB'}
    (RUN/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');run(ap.parse_args().pilot)
