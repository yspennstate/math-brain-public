from functools import lru_cache
from fractions import Fraction
from itertools import combinations

N = 9
COVERS = [(0,2),(0,3),(0,4),(1,4),(2,5),(3,6),(4,7),(4,8),(5,8),(6,8)]
CHAINS = [(0,3,6),(1,4,7),(2,5,8)]

def closure(edges):
    r=[[False]*N for _ in range(N)]
    for a,b in edges: r[a][b]=True
    for k in range(N):
        for i in range(N):
            if r[i][k]:
                for j in range(N):
                    if r[k][j]: r[i][j]=True
    assert not any(r[i][i] for i in range(N))
    return {(i,j) for i in range(N) for j in range(N) if r[i][j]}

REL=closure(COVERS)
PRED=[0]*N
for a,b in REL: PRED[b] |= 1<<a
FULL=(1<<N)-1

@lru_cache(None)
def A(mask):
    # number of ideal paths from 0 to mask; 0 if mask is not an ideal
    if mask==0: return 1
    total=0
    for x in range(N):
        if mask>>x & 1:
            prev=mask ^ (1<<x)
            if PRED[x] & ~prev == 0:
                total += A(prev)
    return total

@lru_cache(None)
def B(mask):
    if mask==FULL: return 1
    total=0
    for x in range(N):
        if not (mask>>x & 1) and PRED[x] & ~mask == 0:
            total += B(mask | (1<<x))
    return total

E=B(0)
assert E==420
assert A(FULL)==E

def incomparable(x,y): return (x,y) not in REL and (y,x) not in REL

def pair_count(x,y):
    assert incomparable(x,y)
    rel2=closure(set(REL)|{(x,y)})
    pred=[0]*N
    for a,b in rel2: pred[b] |= 1<<a
    @lru_cache(None)
    def d(mask):
        if mask==FULL: return 1
        return sum(d(mask|1<<z) for z in range(N)
                   if not(mask>>z&1) and pred[z]&~mask==0)
    return d(0)

def width():
    w=0
    for mask in range(1<<N):
        xs=[i for i in range(N) if mask>>i&1]
        if all(incomparable(a,b) for a,b in combinations(xs,2)):
            w=max(w,len(xs))
    return w

def incomparability_connected():
    adj=[set() for _ in range(N)]
    for i,j in combinations(range(N),2):
        if incomparable(i,j):
            adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]-seen:
            seen.add(v); stack.append(v)
    return len(seen)==N

def extrema():
    mins={x for x in range(N) if all((y,x) not in REL for y in range(N))}
    maxs={x for x in range(N) if all((x,y) not in REL for y in range(N))}
    return mins,maxs

def chain_of(x):
    for i,C in enumerate(CHAINS):
        if x in C: return i
    raise AssertionError

def flux(x,b):
    C=CHAINS[b]
    out=[0]*(len(C)+1)
    for mask in range(1<<N):
        if mask>>x & 1: continue
        if PRED[x] & ~mask: continue
        a=A(mask)
        if not a: continue
        nxt=mask | (1<<x)
        bb=B(nxt)
        if not bb: continue
        t=sum(1 for y in C if mask>>y&1)
        out[t] += a*bb
    assert sum(out)==E
    return out

assert width()==3
assert incomparability_connected()
mins,maxs=extrema()
assert mins=={0,1}
assert maxs=={7,8}

pairs=[]
for x,y in combinations(range(N),2):
    if incomparable(x,y):
        c=pair_count(x,y)
        p=Fraction(c,E)
        bal=min(p,1-p)
        pairs.append((x,y,c,E-c,p,bal))

best=max(p[-1] for p in pairs)
assert best==Fraction(1,2)
assert any((x,y)==(2,3) and p==Fraction(1,2) for x,y,_,_,p,_ in pairs)
assert any((x,y)==(5,6) and p==Fraction(1,2) for x,y,_,_,p,_ in pairs)

extbest=max(bal for x,y,_,_,_,bal in pairs if x in mins|maxs or y in mins|maxs)
assert extbest==Fraction(43,140)
assert extbest < Fraction(1,3)

flux_rows=[]
for x in range(N):
    for b,C in enumerate(CHAINS):
        if b==chain_of(x): continue
        inc=[y for y in C if incomparable(x,y)]
        if not inc: continue
        w=flux(x,b)
        flux_rows.append((x,b,tuple(w),max(w),Fraction(max(w),E),tuple(inc)))

min_heavy=min(row[4] for row in flux_rows)
assert min_heavy==Fraction(11,30)
assert min_heavy>Fraction(1,3)
assert [row for row in flux_rows if row[4]==min_heavy] == [
    (4,0,(0,133,154,133),154,Fraction(11,30),(3,6)),
    (4,2,(133,154,133,0),154,Fraction(11,30),(2,5)),
]

print('POS3_B19_IDEAL_DP_CERTIFICATE_PASS')
print('extensions',E)
print('width',width(),'inc_connected',incomparability_connected(),'mins',sorted(mins),'maxs',sorted(maxs))
print('best_balance',best,'extremal_endpoint_best',extbest)
print('balanced_pairs',[(x,y,str(p)) for x,y,_,_,p,bal in pairs if bal>=Fraction(1,3)])
print('min_relevant_max_flux_fraction',min_heavy,'threshold',Fraction(1,3))
print('pair_table')
for row in pairs: print(row)
print('flux_table')
for row in flux_rows: print(row)
