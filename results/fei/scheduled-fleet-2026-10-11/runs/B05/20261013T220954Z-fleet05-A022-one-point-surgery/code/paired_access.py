"""A022 paired access v1: exact signed Walsh / rational prime-log certificates."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
from itertools import combinations
import sys,time,json,hashlib
RUN=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
# Reuse the immutable stage-2 certified logarithm kernel, not its search.
OLD=RUN.parents[0]/'20261011T234607Z-fleet05-A022-one-point-surgery'/'code'/'oddface_surgery.py'
ns={'__file__':str(OLD),'__name__':'kernel'}
exec(OLD.read_text(encoding='utf-8').split('\nmaxima={};')[0],ns)
fwht=ns['fwht']; factors=ns['factors']; canonical=ns['canonical']
expr_interval=ns['expr_interval']; SCALE=ns['SCALE']; LOG_E=ns['LOG_E']
START=time.perf_counter(); LIMIT=60 if MODE=='pilot' else 1800
CHECKS=0; COUNTS=Counter()
def ck(ok):
    global CHECKS
    assert ok
    CHECKS+=1
def guard():
    if time.perf_counter()-START>LIMIT:raise TimeoutError('frozen cap')
def add(*weighted):
    result=Counter()
    for scale,expr in weighted:
        for p,c in expr:result[p]+=scale*c
    return canonical(result)
def interval(expr):
    lo,hi=expr_interval(expr)
    return Q(lo,SCALE),Q(hi,SCALE)
def entropy_masses(masses,den):
    e=Counter()
    for p,j in factors(den):e[p]+=j
    for mass in masses:
        if mass:
            for p,j in factors(mass):e[p]-=Q(mass*j,den)
    ck(sum(masses)==den)
    return canonical(e)
@lru_cache(maxsize=4096)
def stats(f):
    N=len(f);w=fwht(f);n=(N-1).bit_length();den=N*N
    ck(sum(a*a for a in w)==den)
    H=entropy_masses([a*a for a in w],den)
    infs=tuple(Q(sum(w[S]**2 for S in range(N) if (S>>i)&1),den) for i in range(n))
    return H,infs
@lru_cache(maxsize=4096)
def split(f):
    N=len(f);w=fwht(f);den=N*N
    Braw,dnum=ns['packet_expr'](f)
    B=tuple((p,Q(c,den)) for p,c in Braw)
    d=Q(dnum,den)
    g=f[::2];h=f[1::2]
    ck(d==Q(sum(a!=b for a,b in zip(g,h)),len(g)))
    Hp,ip=stats(f);Hg,ig=stats(g);Hh,ih=stats(h)
    mixH=entropy_masses([w[S]**2+w[S+1]**2 for S in range(0,N,2)],den)
    JS=add((1,mixH),(-Q(1,2),Hg),(-Q(1,2),Hh))
    delta=add((1,Hp),(-Q(1,2),Hg),(-Q(1,2),Hh))
    ck(delta==add((1,B),(1,JS)))
    ck(sum(ip)==d+(sum(ig)+sum(ih))/2)
    ck(interval(B)[1]<=4*d)
    ck(interval(JS)[1]<=2*LOG_E[0]*d if d else not JS)
    return B,JS,d
def bent(x,k):
    return -1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2 else 1
@lru_cache(maxsize=6)
def map_vertices(k,r):
    order=list(range(k,k+r))+list(range(0,k,2))+[k+r]+list(range(1,k,2))
    return tuple(sum(((v>>j)&1)<<i for j,i in enumerate(order)) for v in range(1<<len(order)))
def truth(k,r,D):
    defect=set(D);ans=[]
    for v in map_vertices(k,r):
        x=v&((1<<k)-1);z=(v>>k)&((1<<r)-1);y=(v>>(k+r))&1
        ans.append(1 if z else bent(x,k)*(-1 if y and x in defect else 1))
    return tuple(ans)
def char_value(v,A):return -1 if (v&A).bit_count()%2 else 1
def tree(f,k,r,depth=0,a=0,y=None):
    guard();H,infs=stats(f);I=sum(infs)
    if min(f)==max(f) or depth==r+k//2+1:
        if depth==r+k//2+1:
            E=tuple(v for v,t in enumerate(f) if t!=char_value(v,a))
            ck(len(E)<=4 if y else not E)
            COUNTS['sparse_leaves' if E else 'character_leaves']+=1
        else:COUNTS['early_constant_leaves']+=1
        ck(interval(H)[1]<=6*I)
        return Q(0),I,(),H
    B,JS,d=split(f)
    if depth<r:kind='control'
    elif depth<r+k//2:kind='pair'
    else:kind='selector'
    if kind=='pair':ck(d>=Q(1,4))
    if kind in ('control','selector'):ck(interval(B)[1]<3*d if d else not B)
    COUNTS[kind+'_nodes']+=1
    children=[]
    for bit,child in enumerate((f[::2],f[1::2])):
        aa=a|(bit<<(depth-r)) if kind=='pair' else a
        yy=bit if kind=='selector' else y
        children.append(tree(child,k,r,depth+1,aa,yy))
    l,t=children
    removed=d+(l[0]+t[0])/2;terminal=(l[1]+t[1])/2
    delta=add((1,B),(1,JS),(Q(1,2),l[2]),(Q(1,2),t[2]))
    leaf=add((Q(1,2),l[3]),(Q(1,2),t[3]))
    ck(I==removed+terminal);ck(H==add((1,delta),(1,leaf)))
    return removed,terminal,delta,leaf
def patterns(k,mode):
    if k==4:
        return [D for s in range(1,3 if mode=='pilot' else 5) for D in combinations(range(16),s)]
    if k==6:
        return [D for s in (1,2) for D in combinations(range(64),s)]+[(2,4,6),(2,4,6,11),(0,21,42,63)]
    return [(0,),(255,),(0,1),(0,128),(2,4,6),(2,4,6,11),(0,85,170,255)]
case_count=0
with (RUN/'out'/f'{MODE}_CASES.jsonl').open('w',encoding='utf-8') as out:
    for k in ([4] if MODE=='pilot' else [4,6,8]):
        for r in (0,2):
            for D in patterns(k,MODE):
                f=truth(k,r,D);removed,terminal,delta,leaf=tree(f,k,r)
                H,infs=stats(f);rootI=sum(infs)
                ck(interval(H)[1]<=(4+2*LOG_E[0])*rootI)
                # The entropy numerator is exact; intervals certify only comparisons.
                out.write(json.dumps({'k':k,'r':r,'D':D,'I':str(rootI),'I_removed':str(removed),
                    'I_terminal':str(terminal),'H_interval':[str(x) for x in interval(H)],
                    'terminal_H_interval':[str(x) for x in interval(leaf)],'access_bad_credit':'0'})+'\n')
                case_count+=1
            out.flush()
# Exhaust every sparse leaf through m=4, every character, including dense fibers.
leaf_count=0;sets_count=0
for m in range(0,3 if MODE=='pilot' else 5):
    N=1<<m
    for s in range(min(4,N)+1):
        for E in combinations(range(N),s):
            guard();defect=set(E);g=tuple(-1 if v in defect else 1 for v in range(N))
            H,infs=stats(g);sets_count+=1
            for A in range(N):
                I=sum(1-infs[i] if (A>>i)&1 else infs[i] for i in range(m))
                ck(interval(H)[1]<=6*I)
                leaf_count+=1
results={'helper':'paired-access-v1','mode':MODE,'cases':case_count,'leaf_sets':sets_count,
    'leaf_character_cases':leaf_count,'assertions':CHECKS,'kernel_assertions':ns['ASSERTIONS'],
    'counts':dict(COUNTS),'runtime_seconds':time.perf_counter()-START,
    'arithmetic':'integer Walsh; rational coefficients; outward 80-bit prime log2 intervals',
    'interval_kernel_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),
    'all_access_bad_credit':'0','verdict':'PASS'}
(RUN/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
(RUN/'out'/f'{MODE}_LOG_RECEIPTS.json').write_text(json.dumps({'scale':str(SCALE),
    'log_prime_intervals':ns['PRIME_RECEIPTS'],'natural_log2_interval':[str(x) for x in ns['LN2']],
    'proof':'ln y=2 sum_(j=0)^49 z^(2j+1)/(2j+1), z=(y-1)/(y+1); tail<=2z^101/(101(1-z^2)); range reduce y into [1,2].'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(results))
