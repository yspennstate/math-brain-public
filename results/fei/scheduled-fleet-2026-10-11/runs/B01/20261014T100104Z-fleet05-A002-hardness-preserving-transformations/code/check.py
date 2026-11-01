import sys,json,time,hashlib,argparse
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
sys.dont_write_bytecode=True
import arithmetic as M
import rows as T
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--nmax',type=int,choices=[3,4],required=True);args=ap.parse_args()
start=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1
    if time.perf_counter()-start>55:raise TimeoutError('frozen cap')
    assert x,checks
def walsh(v):return [int(a*len(v)) for a in dense(M.fwht(v),len(v))]
def dense(a,N):return [a.get(s,Q(0)) for s in range(N)]
def child(v,i,b):return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2))
@lru_cache(maxsize=4096)
def hpattern(weights,N):return T.Hweights(weights,N*N)
@lru_cache(maxsize=512)
def Hchild(v):return hpattern(tuple(sorted(x*x for x in walsh(v))),len(v))
def measure(v):
    w=walsh(v);N=len(v);n=N.bit_length()-1
    return w,hpattern(tuple(sorted(x*x for x in w)),N),[Q(sum(x*x for s,x in enumerate(w) if s>>i&1),N*N) for i in range(n)]
def sub(a,b):return M.add((1,a),(-1,b))
@lru_cache(maxsize=8192)
def positive(expr):
    if not expr:return True
    return T.interval(expr)[0]>=0
def pair(v,i,j,w,h,ds,reconstruct):
    n=len(v).bit_length()-1
    hi=M.add(*[(Q(1,2),Hchild(child(v,i,b))) for b in (0,1)])
    hj=M.add(*[(Q(1,2),Hchild(child(v,j,b))) for b in (0,1)])
    hij=M.add(*[(Q(1,4),Hchild(child(child(v,j,b),i,a))) for a in (0,1) for b in (0,1)])
    omega=M.add((1,hi),(1,hj),(-1,h),(-1,hij))
    ck(positive(M.add((1,omega),(1,((2,2*(ds[i]+ds[j])),)))))
    if reconstruct:
        terms=[]
        for s in range(1<<n):
            if s>>i&1 or s>>j&1:continue
            a=[w[s],w[s|(1<<i)],w[s|(1<<j)],w[s|(1<<i)|(1<<j)]]
            q=Q(sum(x*x for x in a),len(v)**2)
            om,d=T.row(tuple(a));terms.append((q,om))
        ck(M.add(*terms)==omega)
    return omega
spec={'helper_version':'Boolean-pair-interaction-exact-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'all labelled Boolean tables n1..nmax plus fixed n5 real-row realization','domain':list(range(1,args.nmax+1)),'case_count':sum(1<<(1<<n) for n in range(1,args.nmax+1)),'symmetry':'none','arithmetic':'integer Walsh/Fraction/formal prime-log; rigorously outward logarithms','memory_estimate_MB':120,'max_runtime_seconds':55,'row_identity_domain':'all n<=3 plus fixed n5 fixture'}
(R/f'out/EXACT_SPEC_n{args.nmax}.json').write_text(json.dumps(spec,indent=2)+'\n')
tables=pairs=equalities=0
for n in range(1,args.nmax+1):
    for mask in range(1<<(1<<n)):
        v=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));w,h,ds=measure(v);tables+=1
        ck(sum(x*x for x in w)==len(v)**2)
        for i in range(n):
            for j in range(i+1,n):
                om=pair(v,i,j,w,h,ds,n<=3);pairs+=1
                if not M.add((1,om),(1,((2,2*(ds[i]+ds[j])),))):equalities+=1
# Physical four-slice negative counts6,1,2,1 on three outside bits.
counts=[6,1,2,1]
v=tuple(-1 if x>>2<counts[x&3] else 1 for x in range(32))
w,h,ds=measure(v);ck([w[s] for s in range(4)]==[12,-12,-8,-8])
omega=pair(v,0,1,w,h,ds,True)
om,d=T.row((3,-3,-2,-2));margin=M.add((1,om),(1,((2,2*d),)))
ck(T.interval(margin)[1]<0)
q=Q(13,32);other=sub(M.add((1,omega),(1,((2,2*(ds[0]+ds[1])),)) ),M.add((q,margin)))
ck(T.interval(other)[0]>0)
out={'status':'PASS','tables':tables,'pairs':pairs,'equality_pairs_including_irrelevant':equalities,'checks':checks,'seconds':time.perf_counter()-start,'fixture':{'n':5,'negative_counts':counts,'row_amplitudes':['3/8','-3/8','-1/4','-1/4'],'row_mass':str(q),'row_margin':[(p,str(c)) for p,c in margin],'whole_omega':[(p,str(c)) for p,c in omega],'whole_pair_influence':str(ds[0]+ds[1]),'remaining_rows_margin':[(p,str(c)) for p,c in other]}}
(R/f'out/EXACT_n{args.nmax}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
