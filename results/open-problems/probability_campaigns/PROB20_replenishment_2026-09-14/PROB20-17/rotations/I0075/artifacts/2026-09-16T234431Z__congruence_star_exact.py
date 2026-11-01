#!/usr/bin/env python3
from heapq import heappush, heappop
from functools import total_ordering

BOX = 10
CUTOFF = (9,0)
SEARCH_R2 = 25

def sign_qsqrt2(p,q):
    if p == 0: return (q>0)-(q<0)
    if q == 0: return (p>0)-(p<0)
    if p > 0 and q > 0: return 1
    if p < 0 and q < 0: return -1
    if p > 0 and q < 0:
        c=p*p-2*q*q
        return (c>0)-(c<0)
    c=2*q*q-p*p
    return (c>0)-(c<0)

def alg_lt(x,y):
    return sign_qsqrt2(x[0]-y[0],x[1]-y[1]) < 0

def alg_leq(x,y):
    return sign_qsqrt2(x[0]-y[0],x[1]-y[1]) <= 0

def route_leq_source(A,B,dx,dy):
    # Exact test (A+B sqrt2)^2 <= 2(dx^2+dy^2), A,B >=0.
    R2=dx*dx+dy*dy
    C=2*R2-(A*A+2*B*B)
    return C>=0 and C*C>=8*A*A*B*B

@total_ordering
class HeapItem:
    __slots__=("a","b","v")
    def __init__(self,a,b,v): self.a,self.b,self.v=a,b,v
    def __lt__(self,o):
        s=sign_qsqrt2(self.a-o.a,self.b-o.b)
        return s<0 if s else self.v<o.v
    def __eq__(self,o):
        return (self.a,self.b,self.v)==(o.a,o.b,o.v)

def distances(q,k,src):
    sx,sy=src
    def selected(a,b): return (a+k*b)%q==0
    def inside(v):
        return sx-BOX<=v[0]<=sx+BOX and sy-BOX<=v[1]<=sy+BOX
    def deleted_edge(x1,y1,x2,y2):
        assert abs(x1-x2)+abs(y1-y2)==1
        if y1==y2:
            x,y=min(x1,x2),y1
            return selected(x,y) or selected(x,y-1)
        x,y=x1,min(y1,y2)
        return selected(x,y) or selected(x-1,y)
    def neighbors(v):
        x,y=v
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            w=(x+dx,y+dy)
            if inside(w) and not deleted_edge(x,y,*w):
                yield w,(1,0)
        for a in (x,x-1):
            for b in (y,y-1):
                if selected(a,b):
                    for w in ((a,b),(a+1,b),(a,b+1),(a+1,b+1)):
                        if w!=v and inside(w):
                            # two spokes through the square centre: sqrt(2)
                            yield w,(0,1)
    dist={src:(0,0)}
    pq=[HeapItem(0,0,src)]
    while pq:
        h=heappop(pq)
        v=h.v
        if dist.get(v)!=(h.a,h.b): continue
        if not alg_leq((h.a,h.b),CUTOFF): break
        for w,c in neighbors(v):
            nd=(h.a+c[0],h.b+c[1])
            if w not in dist or alg_lt(nd,dist[w]):
                dist[w]=nd
                heappush(pq,HeapItem(nd[0],nd[1],w))
    return dist

def first_violation(q,k):
    for rho in range(q):
        src=(rho,0)
        dist=distances(q,k,src)
        for R2 in range(1,SEARCH_R2+1):
            for dx in range(-5,6):
                for dy in range(-5,6):
                    if dx*dx+dy*dy != R2: continue
                    t=(src[0]+dx,src[1]+dy)
                    if t not in dist: continue
                    A,B=dist[t]
                    if not route_leq_source(A,B,dx,dy):
                        # Exact finite-box certificate: this shortest route is < 9,
                        # whereas any route leaving the box must first reach Euclidean
                        # distance >= 10 from src, so cannot improve it.
                        assert sign_qsqrt2(9-A,-B)>0
                        return (rho,dx,dy,A,B,R2)
    return None

fails={}
survivors=[]
for q in range(2,9):
    for k in range(1,q):
        w=first_violation(q,k)
        if w is None:
            survivors.append((q,k))
        else:
            fails[(q,k)]=w

# The only non-overlapping one-residue congruence patterns with q<=8
# that survive all exact local tests are the two reflection-equivalent
# period-eight patterns already globally certified elsewhere.
assert survivors == [(8,3),(8,5)]

# In particular every denser member q<8 has an exact source-level failure.
assert len([1 for q in range(2,8) for k in range(1,q) if (q,k) in fails]) == sum(range(1,7))

print("I0075_CONGRUENCE_STAR_LOCAL_OBSTRUCTION_EXACT")
print("family: selected unit squares satisfy a+k*b == 0 mod q, 1<=k<q")
print("edge-sharing: none in this family because k != 0 mod q")
print("q<8: every member has an exact all-pairs stretch violation")
for q in range(2,9):
    for k in range(1,q):
        if (q,k) in fails:
            rho,dx,dy,A,B,R2=fails[(q,k)]
            print("FAIL q=%d k=%d phase=%d d=(%d,%d) shortest=%d+%d*sqrt2 R2=%d" %
                  (q,k,rho,dx,dy,A,B,R2))
        else:
            print("SURVIVES_LOCAL q=%d k=%d" % (q,k))
print("local_survivors=%r" % (survivors,))
print("global_note: q=8,k=3 is globally source-valid by the prior period-eight certificate; k=5 is its reflection")
print("restricted_optimality: among this congruence family, any source-valid member has q>=8; length density for k!=0 is 2-(4-2*sqrt2)/q")
print("ALL_ASSERTIONS_PASSED")
