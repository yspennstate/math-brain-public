from itertools import combinations, product
from fractions import Fraction
from collections import defaultdict

ONE_THIRD = Fraction(1,3)
TWO_THIRDS = Fraction(2,3)

def transitive_closure(n, mask):
    R = [[False]*n for _ in range(n)]
    bit = 0
    for i in range(n):
        for j in range(i+1,n):
            if (mask >> bit) & 1:
                R[i][j] = True
            bit += 1
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    return tuple(tuple(row) for row in R)

def width(R):
    n=len(R); ans=0
    for m in range(1<<n):
        if m.bit_count() <= ans:
            continue
        xs=[i for i in range(n) if (m>>i)&1]
        if all(not R[i][j] and not R[j][i] for i,j in combinations(xs,2)):
            ans=len(xs)
    return ans

def cover_edges(R):
    n=len(R)
    return [(i,j) for i in range(n) for j in range(n)
            if R[i][j] and not any(R[i][k] and R[k][j]
                                   for k in range(n) if k not in (i,j))]

def linear_extensions(R):
    n=len(R)
    pred=[sum(1<<j for j in range(n) if R[j][i]) for i in range(n)]
    out=[]
    def rec(mask, seq):
        if len(seq)==n:
            out.append(tuple(seq)); return
        for i in range(n):
            if not ((mask>>i)&1) and (pred[i] & ~mask)==0:
                rec(mask | (1<<i), seq+(i,))
    rec(0,())
    return out

def saturated_paths(R,d,z):
    adj=defaultdict(list)
    for u,v in cover_edges(R):
        adj[u].append(v)
    out=[]
    def rec(u,path):
        if u==z:
            out.append(path); return
        for v in adj[u]:
            if v==z or R[v][z]:
                rec(v,path+(v,))
    rec(d,(d,))
    return out

def analyze(R,L,d,a,b,z,path):
    n=len(R); E=len(L)
    pos=[]
    count=[[0]*n for _ in range(n)]
    for seq in L:
        q=[0]*n
        for k,x in enumerate(seq): q[x]=k
        pos.append(q)
        for x in range(n):
            for y in range(n):
                if x!=y and q[x]<q[y]:
                    count[x][y]+=1
    P=lambda x,y: Fraction(count[x][y],E)
    cov=set(cover_edges(R))
    if (d,a) not in cov or (b,z) not in cov or not R[d][z]:
        return None
    if any((R[a][b],R[b][a],R[d][b],R[b][d],R[a][z],R[z][a])):
        return None
    if not (P(a,b)<ONE_THIRD and P(d,b)>TWO_THIRDS and P(a,z)>TWO_THIRDS):
        return None
    def star(x,y):
        if R[x][y]: return True
        if R[y][x]: return False
        return P(x,y)>TWO_THIRDS
    if not (star(d,b) and star(b,a) and star(a,z)):
        return None
    for c in path[1:-1]:
        for x in (a,b):
            if not (R[x][c] or R[c][x]):
                px=P(x,c)
                if ONE_THIRD <= px <= TWO_THIRDS:
                    return None
        if star(a,c) and star(c,b):
            return None
    if any(star(b,c) and star(c,a) for c in path[1:-1]):
        return ("span_descent", None)
    good=[]
    for l,u in zip(path,path[1:]):
        pb=Fraction(sum(q[l]<q[b]<q[u] for q in pos),E)
        pa=Fraction(sum(q[l]<q[a]<q[u] for q in pos),E)
        if pb>ONE_THIRD and pa>ONE_THIRD:
            good.append((l,u,pb,pa))
    return ("common_cover", good)

stats={}
failures=[]
min_mass=None
for n in range(4,7):
    closures={transitive_closure(n,m) for m in range(1<<(n*(n-1)//2))}
    w3=qual=desc=funnel=0
    for R in closures:
        if width(R)>3:
            continue
        w3 += 1
        L=linear_extensions(R)
        for d,a,b,z in product(range(n), repeat=4):
            if len({d,a,b,z})<4 or not R[d][z]:
                continue
            for path in saturated_paths(R,d,z):
                ans=analyze(R,L,d,a,b,z,path)
                if ans is None:
                    continue
                qual += 1
                if ans[0]=="span_descent":
                    desc += 1
                else:
                    if not ans[1]:
                        failures.append((n,d,a,b,z,path,len(L)))
                    else:
                        funnel += 1
                        for _,_,pb,pa in ans[1]:
                            m=min(pb,pa)
                            min_mass=m if min_mass is None or m<min_mass else min_mass
    stats[n]=(len(closures),w3,qual,desc,funnel)

print("stats",stats)
print("failures",len(failures))
print("minimum_verified_common_cover_mass",min_mass)
if failures:
    raise SystemExit("FAIL")
print("POS3_COMMON_COVER_FUNNEL_CHECK_PASS")
