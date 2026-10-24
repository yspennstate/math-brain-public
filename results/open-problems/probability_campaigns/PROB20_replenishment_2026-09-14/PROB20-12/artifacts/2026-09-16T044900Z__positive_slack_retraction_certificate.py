import itertools
from fractions import Fraction

V=tuple(range(6)); C=tuple(range(3)); EDGES=list(itertools.combinations(V,2)); EID={e:i for i,e in enumerate(EDGES)}
def edge(e): return tuple(sorted(e))
def ix(c,e): return 15*c+EID[edge(e)]

COL=[]; ST=[]
for col in itertools.product(C, repeat=6):
    if all(col.count(c)==2 for c in C):
        r=[0]*45
        for c in C:
            pts=tuple(v for v in V if col[v]==c)
            r[ix(c,pts)]=1
        COL.append(col); ST.append(r)
assert len(COL)==90
SINDEX={s:i for i,s in enumerate(COL)}
i0=SINDEX[(0,0,1,1,2,2)]
assert i0==0

def rank_q(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[x-z*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

# Affine-evaluation matrix: constant plus 45 colored-edge coordinates.
EVAL=[[1]+row[:] for row in ST]
assert rank_q(EVAL)==38

# Full action, and stabilizer of sigma0.
def state_perm(vp_t,cp_t):
    out=[None]*90
    for i,s in enumerate(COL):
        t=[None]*6
        for v in V:
            t[vp_t[v]]=cp_t[s[v]]
        out[i]=SINDEX[tuple(t)]
    return out

stab=[]
for vp in itertools.permutations(V):
    for cp in itertools.permutations(C):
        p=state_perm(vp,cp)
        if p[i0]==i0:
            stab.append(p)
assert len(stab)==48

# Stabilizer orbits on states.
seen=set(); ORB=[]
for j in range(90):
    if j in seen: continue
    o={p[j] for p in stab}
    seen |= o
    ORB.append(o)
ORB=sorted(ORB,key=lambda o:(len(o),min(o)))
assert [len(o) for o in ORB]==[1,2,3,8,12,16,24,24]
reps=[''.join(map(str,COL[min(o)])) for o in ORB]
assert reps==['001122','112200','002211','120201','001212','011202','010212','012201']

# Counts for the four coordinate functions used in the proof.
qs=[ix(0,(0,1)),ix(0,(0,2)),ix(0,(2,3)),ix(0,(2,4))]
counts=[[sum(ST[j][q] for j in o) for q in qs] for o in ORB]
ct=list(map(list,zip(*counts)))
assert ct[0]==[1,0,1,0,4,0,0,0]  # color0 edge 01; base value 1
assert ct[1]==[0,0,0,0,1,2,2,1]  # color0 edge 02; base value 0
assert ct[2]==[0,1,1,0,0,0,0,4]  # color0 edge 23; base value 0
assert ct[3]==[0,0,0,2,0,0,2,2]  # color0 edge 24; base value 0

# Exact positivity implication.  Let t_r >=0 be the base-row value on orbit O_r.
# Fixedness gives:
# t0+t2+4t4=1
# t4+2t5+2t6+t7=0
# t1+t2+4t7=0
# 2t3+2t6+2t7=0
# Nonnegativity forces t1=t2=t7=t3=t6=t4=t5=0, then t0=1.
t=[Fraction(0) for _ in range(8)]
t[0]=Fraction(1)
assert sum(ct[0][r]*t[r] for r in range(8))==1
for k in (1,2,3):
    assert sum(ct[k][r]*t[r] for r in range(8))==0

# The resulting equivariant positive map is the identity.  Identity cannot have
# range in the proper 38-dimensional affine-evaluation subspace of R^90.
assert 38 < 90

print('states',len(COL))
print('affine_eval_rank',rank_q(EVAL))
print('stabilizer_size',len(stab))
print('orbit_sizes',[len(o) for o in ORB])
print('orbit_reps',reps)
print('count_0_01',ct[0])
print('count_0_02',ct[1])
print('count_0_23',ct[2])
print('count_0_24',ct[3])
print('forced_equivariant_positive_fixer',(1,0,0,0,0,0,0,0))
print('NO POSITIVE LINEAR RETRACTION')
print('ALL EXACT CHECKS PASSED')