from itertools import combinations

def closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for i,j in edges: R[i][j]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]: R[i][j]=True
    return tuple(tuple(row) for row in R)

def inc(R,i,j):
    return i!=j and not R[i][j] and not R[j][i]

def width3(R):
    n=len(R)
    return not any(all(inc(R,i,j) for i,j in combinations(Q,2))
                   for Q in combinations(range(n),4))

def cover(R,x,y):
    return R[x][y] and not any(z not in (x,y) and R[x][z] and R[z][y]
                               for z in range(len(R)))

def linext(R):
    n=len(R)
    pm=[sum(1<<j for j in range(n) if R[j][i]) for i in range(n)]
    ans=[]
    def rec(mask,L):
        if len(L)==n:
            ans.append(tuple(L)); return
        for v in range(n):
            if not (mask>>v)&1 and pm[v]&~mask==0:
                rec(mask|(1<<v),L+[v])
    rec(0,[])
    return ans

def extrema(R,x,a,y):
    n=len(R)
    DL=[v for v in range(n) if v not in (x,a) and R[v][a] and inc(R,v,x)]
    TL=[v for v in DL if not any(v!=w and R[v][w] for w in DL)]
    SL=[v for v in range(n) if v not in (x,a) and R[x][v] and inc(R,v,a)]
    UL=[v for v in SL if not any(v!=w and R[w][v] for w in SL)]
    SR=[v for v in range(n) if v not in (a,y) and R[a][v] and inc(R,v,y)]
    UR=[v for v in SR if not any(v!=w and R[w][v] for w in SR)]
    DR=[v for v in range(n) if v not in (a,y) and R[v][y] and inc(R,v,a)]
    TR=[v for v in DR if not any(v!=w and R[v][w] for w in DR)]
    return set(TL),set(UL),set(UR),set(TR)

def swap_valid(R,L,u,v):
    M=list(L); pu=M.index(u); pv=M.index(v)
    M[pu],M[pv]=M[pv],M[pu]
    pos={z:i for i,z in enumerate(M)}
    n=len(R)
    return all((not R[i][j]) or pos[i]<pos[j] for i in range(n) for j in range(n))

total_bad_L=total_bad_R=0
for n in range(2,7):
    pairs=list(combinations(range(n),2))
    posets={}
    for mask in range(1<<len(pairs)):
        R=closure(n,[pairs[i] for i in range(len(pairs)) if (mask>>i)&1])
        posets[R]=None
    kept=states=badL=badR=0
    for R in posets:
        if not width3(R): continue
        kept+=1
        E=linext(R)
        for x in range(n):
            for y in range(n):
                if not cover(R,x,y): continue
                for a in range(n):
                    if a in (x,y) or not inc(R,a,x) or not inc(R,a,y): continue
                    H=[L for L in E if L.index(x)<L.index(a)<L.index(y)]
                    if not H: continue
                    TL,UL,UR,TR=extrema(R,x,a,y)
                    assert y in UL and x in TR
                    assert len(TL)<=2 and len(UL)<=2 and len(UR)<=2 and len(TR)<=2
                    CL=TL | (UL-{y})
                    CR=UR | (TR-{x})
                    assert len(CL)<=3 and len(CR)<=3
                    assert all(cover(R,t,a) for t in TL)
                    assert all(cover(R,x,s) for s in UL)
                    assert all(cover(R,a,u) for u in UR)
                    assert all(cover(R,t,y) for t in TR)
                    for L in H:
                        pos={v:i for i,v in enumerate(L)}
                        bL=not swap_valid(R,L,x,a)
                        bR=not swap_valid(R,L,a,y)
                        wL=any(pos[x]<pos[v]<pos[a] for v in CL)
                        wR=any(pos[a]<pos[v]<pos[y] for v in CR)
                        assert bL==wL
                        assert bR==wR
                        badL+=int(bL); badR+=int(bR)
                    states+=1
    total_bad_L+=badL; total_bad_R+=badR
    print("n",n,"distinct_natural_posets",len(posets),
          "width_le_3",kept,"cover_middle_states",states,
          "bad_left_extensions",badL,"bad_right_extensions",badR)
print("total_bad_left_extensions",total_bad_L)
print("total_bad_right_extensions",total_bad_R)
print("POS3_CANONICAL_ACTIVE_BLOCKER_COMPRESSION_PASS")
