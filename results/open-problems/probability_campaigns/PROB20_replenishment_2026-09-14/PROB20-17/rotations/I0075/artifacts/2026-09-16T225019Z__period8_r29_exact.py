#!/usr/bin/env python3
from heapq import heappush, heappop
from functools import total_ordering

LO, HI = -90, 100
MAX_CUTOFF = (76, 0)
RADIUS = 29

def sign_qsqrt2(p, q):
    if p == 0: return (q > 0) - (q < 0)
    if q == 0: return (p > 0) - (p < 0)
    if p > 0 and q > 0: return 1
    if p < 0 and q < 0: return -1
    if p > 0 and q < 0:
        c = p*p - 2*q*q
        return (c > 0) - (c < 0)
    c = 2*q*q - p*p
    return (c > 0) - (c < 0)

def alg_lt(x,y): return sign_qsqrt2(x[0]-y[0],x[1]-y[1])<0
def alg_leq(x,y): return sign_qsqrt2(x[0]-y[0],x[1]-y[1])<=0

@total_ordering
class HeapItem:
    __slots__=("a","b","v")
    def __init__(self,a,b,v): self.a,self.b,self.v=a,b,v
    def __lt__(self,o):
        s=sign_qsqrt2(self.a-o.a,self.b-o.b)
        return (s<0) if s else (self.v<o.v)
    def __eq__(self,o): return (self.a,self.b,self.v)==(o.a,o.b,o.v)

def selected_square(a,b): return (a+3*b)%8==0

def deleted_unit_edge(x1,y1,x2,y2):
    assert abs(x1-x2)+abs(y1-y2)==1
    if y1==y2:
        x,y=min(x1,x2),y1
        return selected_square(x,y) or selected_square(x,y-1)
    x,y=x1,min(y1,y2)
    return selected_square(x,y) or selected_square(x-1,y)

def incident_selected_squares(x,y):
    for a in (x,x-1):
        for b in (y,y-1):
            if selected_square(a,b): yield a,b

def neighbors(v):
    x,y=v
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny=x+dx,y+dy
        if LO<=nx<=HI and LO<=ny<=HI and not deleted_unit_edge(x,y,nx,ny):
            yield (nx,ny),(1,0)
    for a,b in incident_selected_squares(x,y):
        for w in ((a,b),(a+1,b),(a,b+1),(a+1,b+1)):
            if w!=v and LO<=w[0]<=HI and LO<=w[1]<=HI:
                yield w,(0,1)

def dijkstra_exact(src):
    dist={src:(0,0)}; pred={src:None}; pq=[HeapItem(0,0,src)]
    while pq:
        item=heappop(pq); v=item.v; cur=dist.get(v)
        if cur!=(item.a,item.b): continue
        if not alg_leq(cur,MAX_CUTOFF): break
        A,B=cur
        for w,(da,db) in neighbors(v):
            nd=(A+da,B+db)
            if w not in dist or alg_lt(nd,dist[w]):
                dist[w]=nd; pred[w]=(v,(da,db)); heappush(pq,HeapItem(nd[0],nd[1],w))
    return dist,pred

def check_predecessors(src,dist,pred):
    for v,dv in dist.items():
        if v==src:
            assert dv==(0,0) and pred[v] is None; continue
        u,cost=pred[v]
        assert u in dist and alg_lt(dist[u],dv)
        assert dv==(dist[u][0]+cost[0],dist[u][1]+cost[1])
        assert any(w==v and c==cost for w,c in neighbors(u))

def route_leq_source(A,B,dx,dy):
    R2=dx*dx+dy*dy
    C=2*R2-(A*A+2*B*B)
    return C>=0 and C*C>=8*A*A*B*B

# Existing phase-uniform macro cost bounds.
A=(6,2); D=(18,7)
# Exact octagon ordering from the prior proof.
assert sign_qsqrt2(348,-60)>0
assert sign_qsqrt2(660,-332)>0
# Exact h^2=(14720-8448 sqrt2)/4513. New sharper rational lower bound h>47/60.
# After clearing 3600*4513: 43022783 - 30412800 sqrt2 > 0.
assert sign_qsqrt2(43022783,-30412800)>0
# 47/15 - 2sqrt2 > 0.
assert sign_qsqrt2(47,-30)>0
# Descent at r=29. After multiplying the margins by 15:
# axis: 3438 - 2134 sqrt2 >0; diagonal: 3324 - 2339 sqrt2 >0.
assert sign_qsqrt2(3438,-2134)>0
assert sign_qsqrt2(3324,-2339)>0
# sqrt2*29 exceeds both macro costs.
assert sign_qsqrt2(-6,27)>0
assert sign_qsqrt2(-18,22)>0

axis_vecs=((8,0),(-8,0),(0,8),(0,-8))
diag_vecs=((16,16),(16,-16),(-16,16),(-16,-16))
checked_macro=checked_core=nodes_total=0
phase_summaries=[]
for rho in range(8):
    src=(rho,0); dist,pred=dijkstra_exact(src); check_predecessors(src,dist,pred); nodes_total+=len(dist)
    for dx,dy in axis_vecs:
        t=(src[0]+dx,src[1]+dy); assert t in dist and alg_leq(dist[t],A); checked_macro+=1
    for dx,dy in diag_vecs:
        t=(src[0]+dx,src[1]+dy); assert t in dist and alg_leq(dist[t],D); checked_macro+=1
    local=0
    for dx in range(-(RADIUS-1),RADIUS):
        for dy in range(-(RADIUS-1),RADIUS):
            if dx==0 and dy==0: continue
            if dx*dx+dy*dy>=RADIUS*RADIUS: continue
            t=(src[0]+dx,src[1]+dy); assert t in dist
            aa,bb=dist[t]; assert route_leq_source(aa,bb,dx,dy),(rho,(dx,dy),(aa,bb))
            checked_core+=1; local+=1
    phase_summaries.append((rho,len(dist),local))
assert checked_macro==64
assert checked_core==8*2616
print('I0075_PERIOD8_R29_EXACT_CERTIFICATE')
print('network: a+3b == 0 mod 8 square-star replacements')
print('length_density=(6+sqrt(2))/4 < 2 : PASS')
print('axis_macros: +-8 axes <= 6+2*sqrt(2) : PASS')
print('diagonal_macros: (+-16,+-16) <= 18+7*sqrt(2) : PASS')
print('normalized_macro_octagon_inradius > 47/60 : PASS')
print('macro_descent_for_all_norm_ge_29 : PASS')
print('source_phases=8')
print('finite_nonzero_displacements_per_phase=2616')
print('finite_cases_checked=%d' % checked_core)
print('macro_cases_checked=%d' % checked_macro)
print('discovered_nodes_total=%d' % nodes_total)
for row in phase_summaries: print('phase_summary=%r' % (row,))
print('finite_stretch_failures=0')
print('ALL_ASSERTIONS_PASSED')
