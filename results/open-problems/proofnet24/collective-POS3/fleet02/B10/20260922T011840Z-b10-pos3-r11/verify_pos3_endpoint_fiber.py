rels = [(0,2),(0,3),(0,4),(1,4),(1,5),(2,5),(3,6),(3,7),(4,7),(4,8),(5,8),(6,8)]
V = tuple(range(9))

lt = set(rels)
changed = True
while changed:
    changed = False
    for a,b in list(lt):
        for c,d in list(lt):
            if b == c and (a,d) not in lt:
                lt.add((a,d)); changed = True

pred = {v:set() for v in V}
succ = {v:set() for v in V}
for a,b in lt:
    pred[b].add(a); succ[a].add(b)

def linear_extensions(vertices):
    vertices = tuple(vertices)
    P = {v: pred[v] & set(vertices) for v in vertices}
    out = []
    def rec(prefix, rem):
        if not rem:
            out.append(tuple(prefix)); return
        mins = sorted(v for v in rem if not (P[v] & rem))
        for v in mins:
            rec(prefix+[v], rem-{v})
    rec([], set(vertices))
    return out

L = linear_extensions(V)
E = len(L)

def count_before(x,y, exts=L):
    return sum(1 for e in exts if e.index(x) < e.index(y))

x,y = 0,1
Nxy_total = count_before(x,y)
Nyx_total = E-Nxy_total
R = tuple(v for v in V if v not in (x,y))
taus = linear_extensions(R)

def legal_interval(z,tau):
    m=len(tau)
    pos={v:i+1 for i,v in enumerate(tau)}
    lo=max([pos[p] for p in pred[z] if p in pos], default=0)
    hi=min([pos[s]-1 for s in succ[z] if s in pos], default=m)
    return lo,hi

def fiber_counts(tau):
    ax,bx=legal_interval(x,tau)
    ay,by=legal_interval(y,tau)
    nxy=nyx=0
    for i in range(ax,bx+1):
        for j in range(ay,by+1):
            if i < j:
                nxy += 1
            elif i > j:
                nyx += 1
            else:
                # Same deleted-word gap gives two completions, one in each order.
                nxy += 1
                nyx += 1
    return (ax,bx),(ay,by),nxy,nyx

sumxy=sumyx=0
viol=[]
for tau in taus:
    Ix,Iy,nxy,nyx=fiber_counts(tau)
    sumxy += nxy; sumyx += nyx
    if nxy > 2*nyx:
        ax,bx=Ix; ay,by=Iy
        n=bx-ax+1
        Ltail=ax-ay
        Rtail=by-bx
        viol.append((tau,Ix,Iy,nxy,nyx,Ltail,Rtail,n))

print("POS3_B10_ENDPOINT_FIBER_CHECK")
print("linear_extensions", E)
print("pair_0_1", Nxy_total, Nyx_total, f"{Nxy_total}/{E}")
print("deleted_fibers", len(taus))
print("fiber_sums", sumxy, sumyx)
print("violating_fibers_Nxy_gt_2Nyx", len(viol))
tau,Ix,Iy,nxy,nyx,Ltail,Rtail,n = viol[0]
print("first_violating_tau", tau)
print("Ix", Ix, "Iy", Iy, "Nxy", nxy, "Nyx", nyx)
print("L", Ltail, "R", Rtail, "n", n)
print("corridor_lhs_rhs_twice", 2*Rtail, 4*Ltail+n+1)
assert E == 349
assert (Nxy_total,Nyx_total)==(244,105)
assert (sumxy,sumyx)==(244,105)
assert len(viol)==45
assert Ix==(0,0) and Iy==(0,2) and (nxy,nyx)==(3,1)
assert 2*Rtail > 4*Ltail+n+1
print("POS3_B10_ENDPOINT_FIBER_CHECK_PASS")
