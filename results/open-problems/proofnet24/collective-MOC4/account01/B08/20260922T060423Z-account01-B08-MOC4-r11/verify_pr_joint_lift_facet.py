from fractions import Fraction as F
from itertools import permutations, combinations

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def det2(A,i1,i2,j1,j2):
    return A[i1][j1]*A[i2][j2]-A[i1][j2]*A[i2][j1]

def det4(A):
    tot=F(0)
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=F(-1 if inv%2 else 1)
        for i in range(4):
            term*=A[i][p[i]]
        tot+=term
    return tot

def givens(i,j,t):
    c=(1-t*t)/(1+t*t)
    s=2*t/(1+t*t)
    G=eye(4)
    G[i][i]=c; G[j][j]=c
    G[i][j]=s; G[j][i]=-s
    return G

seq=[
    (1,2,F(-4,5)),
    (0,2,F(4,5)),
    (1,3,F(1,4)),
    (1,2,F(1,2)),
    (0,3,F(1,2)),
]
U=eye(4)
for i,j,t in seq:
    U=matmul(givens(i,j,t),U)

expected=[
    [F(27,205), F(69792,142885), F(14168,28577), F(12,17)],
    [F(-32,41), F(8217,28577), F(-68292,142885), F(24,85)],
    [F(-24,41), F(-756,28577), F(102531,142885), F(-32,85)],
    [F(-36,205), F(-117656,142885), F(2976,28577), F(9,17)],
]
assert U==expected
assert matmul(U,transpose(U))==eye(4)
assert det4(U)==1
assert all(x != 0 for row in U for x in row)

pair_list=list(combinations(range(4),2))
mins=[]
for I in pair_list:
    for J in pair_list:
        m=det2(U,I[0],I[1],J[0],J[1])
        assert m != 0
        mins.append(abs(m))
assert min(mins)==F(648,28577)

P=[[U[i][j]*U[i][j] for j in range(4)] for i in range(4)]
pairings=[
    [(0,1),(2,3)],
    [(0,2),(1,3)],
    [(0,3),(1,2)],
]
R=[[F(0) for _ in range(3)] for __ in range(3)]
for a,GI in enumerate(pairings):
    for b,GJ in enumerate(pairings):
        s=F(0)
        for I in GI:
            for J in GJ:
                m=det2(U,I[0],I[1],J[0],J[1])
                s += m*m
        R[a][b]=s/2

S=P[0][0]+P[1][3]+P[2][1]+P[3][2]
T=(R[0][0]-R[0][1])+(R[1][1]-R[1][2])+(R[2][2]-R[2][0])
gap=T-3*S
assert S==F(2217495897,20416123225)
assert T==F(212971450419,510403080625)
assert gap==F(46659258144,510403080625)
assert gap>0

# quotient action on the three complementary-pair partitions
cls={}
for a,parts in enumerate(pairings):
    for I in parts:
        cls[frozenset(I)]=a

def quotient(p):
    out=[]
    for parts in pairings:
        I=parts[0]
        image=frozenset(p[j] for j in I)
        out.append(cls[image])
    return tuple(out)

tau=(0,2,3,1)
def endpoint_ST(p):
    S0=sum(p[j]==tau[j] for j in range(4))
    rho=quotient(p)
    # R_{a,b}=1 iff rho(b)=a
    def rr(a,b):
        return F(int(rho[b]==a))
    T0=(rr(0,0)-rr(0,1))+(rr(1,1)-rr(1,2))+(rr(2,2)-rr(2,0))
    return F(S0),T0

values={}
tight=[]
vertices=[]
for p in permutations(range(4)):
    s,t=endpoint_ST(p)
    val=t-3*s
    values[val]=values.get(val,0)+1
    assert val<=0
    if val==0:
        tight.append(p)
    rho=quotient(p)
    v=[]
    for i in range(4):
        for j in range(4):
            v.append(F(int(p[j]==i)))
    for a in range(3):
        for b in range(3):
            v.append(F(int(rho[b]==a)))
    vertices.append(v)
assert values=={F(0):13,F(-6):10,F(-12):1}
assert len(tight)==13

def rank(M):
    M=[row[:] for row in M]
    if not M:
        return 0
    m,n=len(M),len(M[0])
    r=c=0
    while r<m and c<n:
        piv=next((i for i in range(r,m) if M[i][c]),None)
        if piv is None:
            c+=1
            continue
        M[r],M[piv]=M[piv],M[r]
        q=M[r][c]
        M[r]=[x/q for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]:
                q=M[i][c]
                M[i]=[M[i][j]-q*M[r][j] for j in range(n)]
        r+=1; c+=1
    return r

affine_rank=rank([[vertices[k][j]-vertices[0][j] for j in range(25)] for k in range(1,24)])
tight_idx=[k for k,p in enumerate(permutations(range(4))) if endpoint_ST(p)[1]-3*endpoint_ST(p)[0]==0]
tight_vec=[vertices[k] for k in tight_idx]
facet_rank=rank([[tight_vec[k][j]-tight_vec[0][j] for j in range(25)] for k in range(1,len(tight_vec))])
assert affine_rank==13
assert facet_rank==12

# Exact left-right relabeling orbit of the facet on the 24 joint vertices.
# If the endpoint permutation is transformed by p -> l p r^{-1}, the pulled-back
# facet signature is F(l^{-1} p r). Distinct signatures are distinct facets on
# the joint (P,R) polytope.
def compose(p,q):
    return tuple(p[q[i]] for i in range(4))

def invperm(p):
    out=[0]*4
    for i,x in enumerate(p):
        out[x]=i
    return tuple(out)

def base_facet_value(p):
    s,t=endpoint_ST(p)
    return t-3*s

perms4=list(permutations(range(4)))
facet_orbit={}
for left in perms4:
    ileft=invperm(left)
    for right in perms4:
        signature=tuple(base_facet_value(compose(compose(ileft,p),right)) for p in perms4)
        facet_orbit.setdefault(signature,(left,right))
assert len(facet_orbit)==48
for signature in facet_orbit:
    assert signature.count(F(0))==13
    assert signature.count(F(-6))==10
    assert signature.count(F(-12))==1

print("PASS")
print("detU",det4(U))
print("min_abs_entry",min(abs(x) for row in U for x in row))
print("min_abs_2x2_minor",min(mins))
print("endpoint_facet_values", {str(k):v for k,v in sorted(values.items(), key=lambda kv: kv[0])})
print("joint_polytope_affine_dimension",affine_rank)
print("tight_face_affine_dimension",facet_rank)
print("left_right_facet_orbit_size",len(facet_orbit))
print("S",S,float(S))
print("T",T,float(T))
print("T_minus_3S",gap,float(gap))
