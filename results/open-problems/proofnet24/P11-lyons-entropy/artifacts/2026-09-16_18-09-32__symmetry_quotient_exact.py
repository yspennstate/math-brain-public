from itertools import permutations
import sympy as sp

MASKS=list(range(1,8)); IDX={m:i for i,m in enumerate(MASKS)}

def atom_exp(**kw):
    v=sp.zeros(8,1)
    for key,val in kw.items(): v[int(key[1:])]=val
    return v

c=[
    atom_exp(p2=1,p4=1,p0=-1,p6=-1),
    atom_exp(p1=1,p4=1,p0=-1,p5=-1),
    atom_exp(p1=1,p2=1,p0=-1,p3=-1),
]
tau=atom_exp(p0=1,p3=1,p5=1,p6=1,p1=-1,p2=-1,p4=-1,p7=-1)

def complement_exp(v):
    w=sp.zeros(8,1)
    for S in range(8): w[7^S]+=v[S]
    return w

# A maps the old seven gradient matrices E_T to the new seven gradient matrices
# for J=I-K, with nonempty masks ordered 1,...,7.
A=sp.zeros(7,7)
for S in MASKS:
    T=7^S
    if T:
        A[IDX[S],IDX[T]]=-1
    else:
        for U in MASKS: A[IDX[S],IDX[U]]=1

assert A*A==sp.eye(7)
assert A.det()==-1
for ci in c: assert complement_exp(ci)==ci+tau
assert complement_exp(tau)==-tau

# Every site permutation induces a unimodular permutation matrix on nonempty atoms.
def permute_mask(mask,perm):
    out=0
    for old in range(3):
        if mask & (1<<old): out |= 1<<perm[old]
    return out

perm_dets=[]
for perm in permutations(range(3)):
    P=sp.zeros(7,7)
    for S in MASKS:
        P[IDX[permute_mask(S,perm)],IDX[S]]=1
    assert P.T*P==sp.eye(7)
    assert abs(P.det())==1
    perm_dets.append(int(P.det()))

print('status=PASS')
print('complement_gradient_matrix_A=')
print(A)
print('det(A)=',A.det())
print('A^2=I:',A*A==sp.eye(7))
print('complement_log_exponents: c_i -> c_i+tau for i=1,2,3; tau -> -tau: PASS')
print('site_permutation_atom_matrices_checked=',len(perm_dets))
print('site_permutation_determinants=',perm_dets)
