from itertools import product
from math import comb
from collections import defaultdict, deque
import heapq

N=285
NDIR=1093
D2=180690
D3=-2502870


def types_no110():
    out=[]
    for a in range(67,110):
        for b in range(a,110):
            c=N-a-b
            if b<=c<=109:
                out.append((a,b,c))
    return out


T=types_no110()
assert len(T)==169


def q2(t): return sum((x-95)**2 for x in t)
def q3(t): return sum((x-95)**3 for x in t)
def cat(t):
    r=[x%3 for x in t]
    return ("eq",r[0]) if len(set(r))==1 else ("dist",None)


CATS=[("eq",0),("eq",1),("eq",2),("dist",None)]


# Exact projective value counts for canonical quadratic forms over F_3.
def qform_counts(dim, rank, delta=1):
    diag=(([1]*(rank-1)+[delta]) if rank else [])+[0]*(dim-rank)
    cnt=[0,0,0]
    for u in product(range(3), repeat=dim):
        if not any(u):
            continue
        v=sum(d*x*x for d,x in zip(diag,u))%3
        cnt[v]+=1
    assert all(x%2==0 for x in cnt)
    return tuple(x//2 for x in cnt)


def possible_a_counts(dim):
    out=set()
    for rank in range(dim+1):
        deltas=[1] if rank==0 else [1,2]
        for delta in deltas:
            z,o,t=qform_counts(dim,rank,delta)
            # a=-Q: Q=1 maps to a=2 and Q=2 maps to a=1.
            out.add((z,t,o))
    return sorted(out)


P7=possible_a_counts(7)
P6=possible_a_counts(6)
assert P7==sorted({
 (121,486,486),(283,405,405),(337,378,378),(364,0,729),
 (364,243,486),(364,324,405),(364,351,378),(364,378,351),
 (364,405,324),(364,486,243),(364,729,0),(391,351,351),
 (445,324,324),(607,243,243),(1093,0,0)})
assert P6==sorted({
 (40,162,162),(94,135,135),(112,126,126),(121,0,243),
 (121,81,162),(121,108,135),(121,135,108),(121,162,81),
 (121,243,0),(130,117,117),(148,108,108),(202,81,81),
 (364,0,0)})


# Pointwise supporting inequalities on the 169 no-110 direction types.
NORMALS=[(183,13),(183,14),(27,2)]
mins={}
for A,B in NORMALS:
    mins[(A,B)]={}
    for c in CATS:
        vals=[A*q2(t)+B*q3(t) for t in T if cat(t)==c]
        assert vals
        mins[(A,B)][c]=min(vals)

assert mins[(183,13)]=={("eq",0):1020,("eq",1):1176,("eq",2):0,("dist",None):366}
assert mins[(183,14)]=={("eq",0):1014,("eq",1):-15288,("eq",2):0,("dist",None):-6186}
assert mins[(27,2)]=={("eq",0):150,("eq",1):-1176,("eq",2):0,("dist",None):54}


def separated(counts, normal):
    A,B=normal
    target=A*D2+B*D3
    lower=sum(counts.get(c,0)*mins[normal][c] for c in CATS)
    return target < lower, target, lower


# If S=0, every direction is equal-residue and its common residue is -Q(u).
# Every possible 7D quadratic-form value distribution is impossible.
s0_certificate={}
for tup in P7:
    counts={("eq",0):tup[0],("eq",1):tup[1],("eq",2):tup[2],("dist",None):0}
    wins=[]
    for normal in [(183,13),(183,14)]:
        ok,target,lower=separated(counts,normal)
        if ok: wins.append((normal,target,lower))
    assert wins, ("S=0 tuple survived",tup)
    s0_certificate[tup]=wins[0]


# If S!=0, exactly 729 directions are distinct-residue; the 364 equal-residue
# directions lie in H=S^perp and are governed by Q restricted to a 6D space.
EXC=(40,162,162)
sn_certificate={}
for tup in P6:
    if tup==EXC:
        continue
    counts={("eq",0):tup[0],("eq",1):tup[1],("eq",2):tup[2],("dist",None):729}
    wins=[]
    for normal in [(27,2),(183,13)]:
        ok,target,lower=separated(counts,normal)
        if ok: wins.append((normal,target,lower))
    assert wins, ("S!=0 tuple survived",tup)
    sn_certificate[tup]=wins[0]


# Exceptional case: Q|_H is rank-2 anisotropic, with residue counts (40,162,162).
# Two exact slack budgets follow from the two supporting normals.
exc_counts={("eq",0):40,("eq",1):162,("eq",2):162,("dist",None):729}
def lower_sum(normal):
    return sum(exc_counts[c]*mins[normal][c] for c in CATS)

P_B=(27*D2+2*D3-lower_sum((27,2)))//18
R_B=(183*D2+13*D3-lower_sum((183,13)))//18
assert (P_B,R_B)==(1002,1713)
assert 27*D2+2*D3-lower_sum((27,2))==18*P_B
assert 183*D2+13*D3-lower_sum((183,13))==18*R_B


# Convert each type to nonnegative exact slack coordinates (p,r).
# Equal-residue types contribute 3p,3r to the divided-by-18 budgets;
# distinct-residue types contribute p,r.
options=defaultdict(list)
for t in T:
    c=cat(t); Q2=q2(t); Q3=q3(t)
    if c==("eq",0):
        assert (Q2-6)%18==0 and (Q3+6)%54==0
        a=(Q2-6)//18; b=(Q3+6)//54
        p=9*a+2*b; r=61*a+13*b; w=3
    elif c==("eq",1):
        assert (Q2-6)%18==0 and (Q3-6)%54==0
        a=(Q2-6)//18; b=(Q3-6)//54
        p=25+9*a+2*b; r=61*a+13*b; w=3
    elif c==("eq",2):
        assert Q2%18==0 and Q3%54==0
        a=Q2//18; b=Q3//54
        p=9*a+2*b; r=61*a+13*b; w=3
    else:
        assert (Q2-2)%6==0 and Q3%18==0
        a=(Q2-2)//6; b=Q3//18
        p=9*a+2*b; r=61*a+13*b; w=1
    assert p>=0 and r>=0
    options[c].append((w*p,w*r,a,t))


# Every category has a zero-slack filler, so dropping the finite category-count
# caps gives a relaxation. If even this relaxation has A0<=9, so does the true problem.
for c in CATS:
    assert any(P==0 and R==0 for P,R,a,t in options[c])


def dedup(c, objective=False):
    d={}
    for P,R,a,t in options[c]:
        if P==0 and R==0:
            continue
        if P>P_B or R>R_B:
            continue
        key=(P,R)
        val=a if objective else 0
        if key not in d or val>d[key]:
            d[key]=val
    return [(P,R,v) for (P,R),v in d.items()]


# Exact unbounded knapsack for eq0, maximizing A0=sum a.
eq0_opts=dedup(("eq",0),True)
best={(0,0):0}
heap=[(0,0,0)] # (P+R,P,R)
done=set()
while heap:
    _,P,R=heapq.heappop(heap)
    if (P,R) in done:
        continue
    done.add((P,R))
    v=best[(P,R)]
    for dP,dR,da in eq0_opts:
        nP,nR=P+dP,R+dR
        if nP<=P_B and nR<=R_B:
            nv=v+da
            if nv>best.get((nP,nR),-1):
                best[(nP,nR)]=nv
                heapq.heappush(heap,(nP+nR,nP,nR))


# Exact reachability for the relaxed union of the other three categories.
rest=[]
for c in [("eq",1),("eq",2),("dist",None)]:
    rest.extend(dedup(c,False))
reach={(0,0)}
dq=deque([(0,0)])
while dq:
    P,R=dq.popleft()
    for dP,dR,_ in rest:
        nP,nR=P+dP,R+dR
        if nP<=P_B and nR<=R_B and (nP,nR) not in reach:
            reach.add((nP,nR))
            dq.append((nP,nR))

A0max=-1
best_state=None
for (P,R),a0 in best.items():
    if (P_B-P,R_B-R) in reach and a0>A0max:
        A0max=a0
        best_state=(P,R)
assert A0max==9, (A0max,best_state)


# For the 40 residue-0 directions, q2=6+18a.
Q2U_max=40*6+18*A0max
assert Q2U_max==402


# Geometric collision lower bound on the same 40 directions:
# their rank-2 anisotropic zero set is a 4D radical U.
# Projection to U^* has 81 fibers. Convexity at total 285 gives
# 42 fibers of size 4 and 39 of size 3 in the minimum-collision distribution.
P0_min=42*comb(4,2)+39*comb(3,2)
assert P0_min==369
EU_min=13*comb(N,2)+27*P0_min
assert EU_min==536073
baseline_EU=40*13395
Q2U_min=2*(EU_min-baseline_EU)
assert baseline_EU==535800
assert Q2U_min==546
assert Q2U_max < Q2U_min


print("PASS R15 I0124 exact no-110 285-cap obstruction")
print(f"types={len(T)}; D2={D2}; D3={D3}")
print(f"quadratic_projective_count_cases: dim7={len(P7)} all_S0_eliminated; dim6={len(P6)}")
print(f"unique_surviving_Snonzero_residue_case={EXC}")
print(f"slack_budgets=(P,R)=({P_B},{R_B}); relaxed_exact_DP_A0max={A0max}")
print(f"residue0_q2_upper={Q2U_max}; quotient_collision_q2_lower={Q2U_min}")
print("CONCLUSION: any 285-cap in AG(7,3) must have an affine hyperplane slice of size at least 110")
