from fractions import Fraction as F
from collections import Counter
import hashlib, json

P=257
T=F(53,5)
C0,C1,C2,C3=F(-123,200),F(-3,100),F(1,100),F(-3,400)

def chi(a):
    a %= P
    if a == 0:
        return 0
    return 1 if pow(a,(P-1)//2,P)==1 else -1

V=[x for x in range(P) if x not in (0,1) and chi(x)==1 and chi(x-1)==1]
n=len(V)
assert n == (P-5)//4 == 63
idx={x:i for i,x in enumerate(V)}

A=[[0]*n for _ in range(n)]
for i,x in enumerate(V):
    for j in range(i+1,n):
        y=V[j]
        if chi(x-y)==1:
            A[i][j]=A[j][i]=1

deg=[sum(row) for row in A]
assert sum(deg)//2 == 945
assert Counter(deg)==Counter({28:24,30:21,32:12,34:6})
assert sum(deg)==30*n

# Exact elliptic-trace coordinate.
Svals=[]
for x,dx in zip(V,deg):
    sx=sum(chi(t*(t-1)*(t-x)) for t in range(P))
    assert 8*dx == P-15+sx
    Svals.append(sx)
assert sorted(set(Svals))==[-18,-2,14,30]

# Exact S3 action and exceptional orbit.
def r(x): return (1-x)%P
def s(x): return pow(x,-1,P)
Vset=set(V)
for x in V:
    assert r(x) in Vset and s(x) in Vset
for i,x in enumerate(V):
    for j,y in enumerate(V):
        if i==j: continue
        assert A[idx[r(x)]][idx[r(y)]]==A[i][j]
        assert A[idx[s(x)]][idx[s(y)]]==A[i][j]

seen=set()
orbits=[]
for x in V:
    if x in seen: continue
    orb=set()
    frontier=[x]
    while frontier:
        y=frontier.pop()
        if y in orb: continue
        orb.add(y)
        frontier.extend([r(y),s(y)])
    seen |= orb
    orbits.append(tuple(sorted(orb)))
sizes=sorted(map(len,orbits))
assert sizes == [3]+[6]*10
harm=tuple(sorted({2, P-1, pow(2,-1,P)}))
assert harm in orbits
assert [deg[idx[x]] for x in harm]==[30,30,30]
assert P%24==17

# Degree-aware dual and stronger theta-plus sign test.
delta=[d-30 for d in deg]
B=[[F(0) for _ in range(n)] for __ in range(n)]
nonedge_coeffs=Counter()
for i in range(n):
    for j in range(n):
        if i==j or A[i][j]:
            B[i][j]=F(1)
        else:
            u,v=delta[i],delta[j]
            q=C0+C1*(u+v)+C2*u*v+C3*(u*u+v*v)
            B[i][j]=q
            if i<j:
                nonedge_coeffs[q]+=1

assert sum(nonedge_coeffs.values()) == n*(n-1)//2-945 == 1008
assert max(nonedge_coeffs) == F(-103,200) < 0
assert min(nonedge_coeffs) == F(-187,200) < 0

# Independent positive-definiteness proof: scale to integers and apply
# fraction-free Bareiss elimination. Its diagonal pivots are the leading
# principal minors; Sylvester's criterion says all positive => PD.
SCALE=400
Q=[]
for i in range(n):
    row=[]
    for j in range(n):
        m=(T if i==j else F(0))-B[i][j]
        q=m*SCALE
        assert q.denominator==1
        row.append(q.numerator)
    Q.append(row)

M=[row[:] for row in Q]
prev=1
pivots=[]
for k in range(n):
    pivot=M[k][k]
    assert pivot>0, (k,pivot)
    pivots.append(pivot)
    if k==n-1:
        break
    for i in range(k+1,n):
        aik=M[i][k]
        for j in range(k+1,n):
            num=M[i][j]*pivot-aik*M[k][j]
            assert num % prev == 0
            M[i][j]=num//prev
    for i in range(k+1,n):
        M[i][k]=0
    for j in range(k+1,n):
        M[k][j]=0
    prev=pivot
assert len(pivots)==n and all(x>0 for x in pivots)

margin=F(4*P,9)-T*T
assert margin==F(419,225)>0

# Hash deterministic exact objects for compact reproducibility.
adj_bytes=json.dumps(A,separators=(',',':')).encode()
pivot_bytes=json.dumps(pivots,separators=(',',':')).encode()
print("P26-AUDIT-P04-I0101-P257-DEGREE-AWARE-DUAL-61=PASS")
print(f"p={P}")
print(f"n={n}")
print(f"edges={sum(deg)//2}")
print(f"nonedges={sum(nonedge_coeffs.values())}")
print("degree_multiplicities="+repr(sorted(Counter(deg).items())))
print("elliptic_trace_set="+repr(sorted(set(Svals))))
print("s3_orbit_sizes="+repr(sizes))
print("harmonic_orbit="+repr(harm))
print("harmonic_orbit_degrees="+repr([deg[idx[x]] for x in harm]))
print("theta_plus_nonedge_coeff_range="+str(min(nonedge_coeffs))+".."+str(max(nonedge_coeffs)))
print("theta_plus_nonedge_coeff_counts="+repr([(str(k),v) for k,v in sorted(nonedge_coeffs.items())]))
print("THETA_PLUS_SIGN=PASS")
print(f"integer_scale={SCALE}")
print(f"bareiss_positive_leading_minors={len(pivots)}")
print(f"bareiss_first_pivot={pivots[0]}")
print(f"bareiss_final_minor_bitlength={pivots[-1].bit_length()}")
print("bareiss_pivots_sha256="+hashlib.sha256(pivot_bytes).hexdigest())
print("adjacency_sha256="+hashlib.sha256(adj_bytes).hexdigest())
print(f"t={T}")
print(f"threshold_square_margin={margin}")
print("EXACT_INTEGER_PD=PASS")
print("EXACT_RECONSTRUCTION=PASS")
print("END_P26_P257_AUDIT")
