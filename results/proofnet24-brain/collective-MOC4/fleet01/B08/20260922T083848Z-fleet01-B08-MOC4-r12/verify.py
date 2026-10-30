from fractions import Fraction as F
from itertools import permutations, combinations

U = [
    [F(0),        F(16,25),   F(-48,65),   F(69,325)],
    [F(16,25),    F(-72,125), F(-33,65),   F(-48,1625)],
    [F(-69,325),  F(48,1625), F(-16,65),   F(-1536,1625)],
    [F(48,65),    F(33,65),   F(24,65),    F(-16,65)],
]

def det2(I,J):
    i,k=I; j,l=J
    return U[i][j]*U[k][l]-U[i][l]*U[k][j]

for i in range(4):
    for j in range(4):
        v=sum(U[k][i]*U[k][j] for k in range(4))
        assert v == F(int(i==j))
assert U[0][0] == 0
assert all(U[i][j] != 0 for i in range(4) for j in range(4) if (i,j)!=(0,0))

pairs=list(combinations(range(4),2))
assert all(det2(I,J) != 0 for I in pairs for J in pairs)

def P(i,j):
    return U[i][j]**2

def Q(I,J):
    return det2(I,J)**2

def facet_point():
    return (
        -P(0,1) + P(1,2) - P(2,0) - P(2,1)
        +Q((0,1),(0,1)) + Q((0,2),(0,1)) + Q((0,2),(0,2))
    )

def pind(pi,i,j):
    return F(int(pi[j]==i))

def qind(pi,I,J):
    return F(int({pi[j] for j in J}==set(I)))

def facet_vertex(pi):
    return (
        -pind(pi,0,1) + pind(pi,1,2) - pind(pi,2,0) - pind(pi,2,1)
        +qind(pi,(0,1),(0,1)) + qind(pi,(0,2),(0,1)) + qind(pi,(0,2),(0,2))
    )

allowed=[pi for pi in permutations(range(4)) if pi[0]!=0]
vals=[facet_vertex(pi) for pi in allowed]
assert set(vals)=={F(-1),F(0)}
assert vals.count(F(0))==12 and vals.count(F(-1))==6
gap=facet_point()
assert gap==F(5810112,446265625) and gap>0

coords = [
    ("P",0,1), ("P",0,2), ("P",1,0), ("P",1,1),
    ("P",1,2), ("P",2,0), ("P",2,1), ("P",2,2),
    ("Q",(0,1),(0,1)), ("Q",(0,1),(0,2)),
    ("Q",(0,2),(0,1)), ("Q",(0,2),(0,2)),
]

def endpoint_coords(pi):
    out=[]
    for c in coords:
        if c[0]=="P":
            _,i,j=c
            out.append(pind(pi,i,j))
        else:
            _,I,J=c
            out.append(qind(pi,I,J))
    return out

def rank(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m:
            break
    return r

def affine_rank(points):
    base=points[0]
    return rank([[x-y for x,y in zip(p,base)] for p in points[1:]])

allowed_pts=[endpoint_coords(pi) for pi in allowed]
tight_pts=[endpoint_coords(pi) for pi in allowed if facet_vertex(pi)==0]
assert affine_rank(allowed_pts)==12
assert affine_rank(tight_pts)==11

print("orthogonal_exact=PASS")
print("only_forced_zero_entry=PASS")
print("all_36_two_minors_nonzero=PASS")
print("allowed_vertex_values: zero=12 minus_one=6")
print("joint_polytope_affine_dimension=12")
print("tight_face_affine_dimension=11")
print("facet_gap =", gap)
print("facet_gap_decimal =", float(gap))
print("common_positive_all_compound_law=IMPOSSIBLE")
