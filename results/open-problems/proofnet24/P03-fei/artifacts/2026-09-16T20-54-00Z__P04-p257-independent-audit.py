from fractions import Fraction as F
p=257

def chi(a):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

V=[x for x in range(p) if x not in (0,1) and chi(x)==1 and chi(x-1)==1]
n=len(V)
assert n==63
A=[[0]*n for _ in range(n)]
for i,x in enumerate(V):
    for j in range(i+1,n):
        if chi(x-V[j])==1:
            A[i][j]=A[j][i]=1
deg=[sum(r) for r in A]
assert sum(deg)==1890 and sorted(set(deg))==[28,30,32,34]

# Independent check of the structural identity used to construct the degree-aware dual.
for x,dx in zip(V,deg):
    Sx=sum(chi(t*(t-1)*(t-x)) for t in range(p))
    assert 8*dx==p-15+Sx

c0,c1,c2,c3=F(-123,200),F(-3,100),F(1,100),F(-3,400)
t=F(53,5)
delta=[d-30 for d in deg]
B=[[F(0) for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j or A[i][j]:
            B[i][j]=F(1)
        else:
            u,v=delta[i],delta[j]
            B[i][j]=c0+c1*(u+v)+c2*u*v+c3*(u*u+v*v)
# Theta-dual support conditions.
for i in range(n):
    assert B[i][i]==1
    for j in range(i+1,n):
        if A[i][j]: assert B[i][j]==1

# Exact LDL^T certificate for tI-B \succ 0, with reconstruction.
M=[[(t if i==j else F(0))-B[i][j] for j in range(n)] for i in range(n)]
L=[[F(0) for _ in range(n)] for __ in range(n)]
D=[F(0)]*n
for i in range(n):
    L[i][i]=1
    D[i]=M[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
    assert D[i]>0
    for j in range(i+1,n):
        L[j][i]=(M[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/D[i]
for i in range(n):
    for j in range(n):
        assert sum(L[i][k]*D[k]*L[j][k] for k in range(min(i,j)+1))==M[i][j]

margin=F(4*p,9)-t*t
assert margin==F(419,225)>0
print('P03-AUDIT-P04-I0101-P257-210=PASS')
print(f'p={p} n={n} edges={sum(deg)//2} degree_set={sorted(set(deg))}')
print(f't={t} threshold_square_margin={margin}')
print(f'positive_ldl_pivots={len(D)}')
print(f'min_pivot_exact={min(D)}')
print('EXACT_RECONSTRUCTION=PASS')
