import itertools
import sympy as sp

n = sp.symbols('n', integer=True, positive=True)
r = n - 5

# Schur-complement derivation of the two rooted-forest minors.
# Ordinary-vertex block D = n I_r - J_r, so
# D^{-1} = n^{-1}I_r + (5n)^{-1}J_r because n-r=5.
At = sp.Matrix([
    [-1, n-2, -1],
    [-1, -1, n-2],
    [ 0, -1, -1],
])
As = sp.Matrix([
    [ 0, n-2, -1],
    [ 0, -1, n-2],
    [ 0, -1, -1],
])
scalar = sp.simplify(r / 5)  # 1^T D^{-1} 1
St = sp.simplify(At - scalar * sp.ones(3))
Ss = sp.simplify(As - scalar * sp.ones(3))

det_St = sp.factor(St.det())
det_Ss = sp.factor(Ss.det())
assert sp.simplify(det_St + (n-1)*(n**2-4*n+5)/5) == 0
assert sp.simplify(det_Ss + (n-5)*(n-1)**2/5) == 0

# det(D)=5*n^(r-1). Absolute determinants of the nonsymmetric all-minors:
Ft = sp.factor((n-1)*n**(n-6)*(n**2-4*n+5))
Fs = sp.factor((n-1)**2*(n-5)*n**(n-6))
gap = sp.factor(Ft-Fs)
assert sp.simplify(gap - 2*(n-1)*n**(n-5)) == 0


def laplacian(N, missing):
    L = sp.zeros(N)
    missing = {tuple(sorted(e)) for e in missing}
    for i in range(N):
        for j in range(i+1,N):
            if (i,j) not in missing:
                L[i,i] += 1
                L[j,j] += 1
                L[i,j] -= 1
                L[j,i] -= 1
    return L

# Direct all-minors verification for n=8,...,12.
Xmissing={(0,1),(0,2),(0,3),(0,4),(1,4)}  # st,su,sv,sw,tw
for N in range(8,13):
    L=laplacian(N,Xmissing)
    rows=[i for i in range(N) if i not in {0,1}]
    cols_t=[j for j in range(N) if j not in {0,4}]
    cols_s=[j for j in range(N) if j not in {1,4}]
    ft=abs(int(L.extract(rows,cols_t).det()))
    fs=abs(int(L.extract(rows,cols_s).det()))
    expected_t=(N-1)*(N**(N-6))*(N*N-4*N+5)
    expected_s=((N-1)**2)*(N-5)*(N**(N-6))
    expected_gap=2*(N-1)*(N**(N-5))
    assert ft==expected_t
    assert fs==expected_s
    assert ft-fs==expected_gap
    print(f'all-minors n={N}: Ft={ft}, Fs={fs}, gap={ft-fs}')

# Independent exact brute-force coefficient check at the first source-new scale n=8.
def split_coeff(N, missing, k):
    missing={tuple(sorted(e)) for e in missing}
    edges=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in missing]
    total=0
    for chosen in itertools.combinations(edges,k):
        parent=list(range(N))
        def find(a):
            while parent[a]!=a:
                parent[a]=parent[parent[a]]
                a=parent[a]
            return a
        def union(a,b):
            ra,rb=find(a),find(b)
            if ra!=rb: parent[rb]=ra
        for a,b in chosen:
            union(a,b)
        roots={find(i) for i in range(N)}
        if len(roots)==2 and find(0)!=find(1):
            total += 1
    return total

N=8
A_missing={(0,1),(0,2),(0,3),(0,4)}             # st,su,sv,sw
B_missing={(0,1),(0,2),(0,3),(1,4)}             # st,su,sv,tw
for k in (N-2,N-1):
    ca=split_coeff(N,A_missing,k)
    cb=split_coeff(N,B_missing,k)
    print(f'bruteforce n=8 k={k}: star={ca}, tie={cb}, gap={ca-cb}')
    if k==N-2:
        assert ca==cb
    else:
        assert ca-cb==2*(N-1)*(N**(N-5))

print('det(S_t) =', det_St)
print('det(S_s) =', det_Ss)
print('symbolic gap =', gap)
print('PASS: unique leading-coefficient tie is broken at N_(n-1):')
print('      N_(n-1)(star)-N_(n-1)(tie)=2(n-1)n^(n-5)>0 for all n>=8.')
