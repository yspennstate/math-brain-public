from collections import deque
from itertools import product

# Exact finite graph self-check for the combinatorial core of the fixed-height one-sided cut process.
# No floating point, no randomness.


def vertices(R,H):
    V=[]
    for x in range(-R,R+1):
      for y in range(-R,R+1):
        for z in range(0,H+1):
          V.append((x,y,z))
    return V


def neighbors(v, allowed):
    x,y,z=v
    for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        w=(x+dx,y+dy,z+dz)
        if w in allowed:
            yield w


def reachable(start, top, allowed, removed_edges):
    q=deque(start)
    seen=set(start)
    while q:
        v=q.popleft()
        if v in top:
            return True
        for w in neighbors(v,allowed):
            e=tuple(sorted((v,w)))
            if e in removed_edges or w in seen:
                continue
            seen.add(w); q.append(w)
    return False


def test_case(R,H,a,b,r):
    slab=set(vertices(R,H))
    # Source is the discretized set just below A; add those vertices and crossing edges.
    src={(x,y,-1) for x in range(a+1) for y in range(b+1)}
    allowed=slab|src
    top={(x,y,H) for x in range(-R,R+1) for y in range(-R,R+1)}

    # Graph distance from source in the induced graph.
    q=deque(src)
    dist={s:0 for s in src}
    while q:
        v=q.popleft()
        for w in neighbors(v,allowed):
            if w not in dist:
                dist[w]=dist[v]+1; q.append(w)

    shells=[]
    # use radii 1,3,5,... to ensure distinct boundary levels and enough top separation
    for j in range(r):
        rad=1+2*j
        E=set()
        for v,dv in dist.items():
            if dv<=rad:
                for w in neighbors(v,allowed):
                    if dist.get(w,10**9)>rad:
                        E.add(tuple(sorted((v,w))))
        assert E, (R,H,a,b,r,rad)
        assert not reachable(src,top,allowed,E), (R,H,a,b,r,rad,'shell failed')
        shells.append(E)
    for i in range(len(shells)):
        for j in range(i):
            assert shells[i].isdisjoint(shells[j]), (R,H,a,b,r,i,j,'shell overlap')

    # Subadditivity combinatorial core: split source A into x-columns and use independently valid cuts.
    if a>=1:
        src1={(x,y,-1) for x in range(0,a//2+1) for y in range(b+1)}
        src2=src-src1
        for S in (src1,src2):
            if not S: continue
            q=deque(S); dd={s:0 for s in S}
            while q:
                v=q.popleft()
                for w in neighbors(v,allowed):
                    if w not in dd:
                        dd[w]=dd[v]+1; q.append(w)
            rad=1
            E=set()
            for v,dv in dd.items():
                if dv<=rad:
                    for w in neighbors(v,allowed):
                        if dd.get(w,10**9)>rad:
                            E.add(tuple(sorted((v,w))))
            if S is src1: E1=E
            else: E2=E
        if src2:
            assert not reachable(src,top,allowed,E1|E2), (R,H,a,b,'union cut failed')
    return tuple(len(E) for E in shells)

cases=0
sizes=[]
for R in (3,4,5):
  for H in (8,10,12):
    for a,b in ((0,0),(1,0),(1,1),(2,1)):
      for r in (1,2,3):
        if 1+2*(r-1)+1 >= H:
            continue
        # keep base comfortably away from horizontal finite truncation boundary
        if a>R-2 or b>R-2:
            continue
        sizes.append(test_case(R,H,a,b,r)); cases+=1
print('RESULT PASS')
print('CASES',cases)
print('SHELL_SIZE_RANGE',min(min(s) for s in sizes),max(max(s) for s in sizes))
print('NO_FLOATING_POINT true')
print('LIMITATION finite-box combinatorial self-check only; theorem is proved analytically in report')
