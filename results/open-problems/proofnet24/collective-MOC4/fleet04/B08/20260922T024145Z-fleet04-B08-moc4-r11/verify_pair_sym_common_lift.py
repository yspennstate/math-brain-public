from fractions import Fraction as F
from itertools import permutations

U = [
    [F(0), F(3,5), F(16,25), F(-12,25)],
    [F(-69,325), F(-192,325), F(48,65), F(16,65)],
    [F(48,65), F(16,65), F(69,325), F(192,325)],
    [F(16,25), F(-12,25), F(0), F(-3,5)],
]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
assert all(dot(U[i],U[j]) == F(int(i==j)) for i in range(4) for j in range(4))

r,s,p,q = 0,1,2,3
a = [U[p][j]**2 for j in range(4)]
b = [U[q][j]**2 for j in range(4)]
def qminor(j,k): return (U[p][j]*U[q][k]-U[p][k]*U[q][j])**2

edges = [(0,1),(0,2),(0,3),(1,0),(1,2),(1,3),(2,0),(2,1),(2,3),(3,0),(3,1),(3,2)]
vals = [
    F(14524416,66015625), F(0), F(1651968,5078125),
    F(2781184,66015625), F(0), F(1218816,66015625),
    F(1218816,66015625), F(685584,66015625), F(42849,2640625),
    F(36864,105625), F(0), F(0),
]
t = dict(zip(edges, vals))
assert all(v >= 0 for v in t.values())
for j in range(4):
    assert sum(t.get((j,k),F(0)) for k in range(4) if k != j) == a[j]
    assert sum(t.get((k,j),F(0)) for k in range(4) if k != j) == b[j]
for j in range(4):
    for k in range(j+1,4):
        assert t[(j,k)] + t[(k,j)] == qminor(j,k)

PERMS = list(permutations(range(4)))
lam = {sigma:F(0) for sigma in PERMS}
for (j,k),w in t.items():
    rem = [c for c in range(4) if c not in (j,k)]
    sigma1=[None]*4; sigma2=[None]*4
    sigma1[p]=j; sigma1[q]=k; sigma1[r]=rem[0]; sigma1[s]=rem[1]
    sigma2[p]=j; sigma2[q]=k; sigma2[r]=rem[1]; sigma2[s]=rem[0]
    lam[tuple(sigma1)] += w/2
    lam[tuple(sigma2)] += w/2
assert all(w >= 0 for w in lam.values())
assert sum(lam.values()) == 1

P = [[U[i][j]**2 for j in range(4)] for i in range(4)]
Us = [row[:] for row in U]
Us[r],Us[s] = Us[s],Us[r]
Ps = [[Us[i][j]**2 for j in range(4)] for i in range(4)]
Pbar = [[(P[i][j]+Ps[i][j])/2 for j in range(4)] for i in range(4)]
Plam = [[F(0) for _ in range(4)] for _ in range(4)]
for sigma,w in lam.items():
    for i,j in enumerate(sigma): Plam[i][j] += w
assert Plam == Pbar

PAIRS = [(0,1),(0,2),(0,3)]
ALL = set(range(4))
def det2(M,rows,cols):
    i,k=rows; j,l=cols
    return M[i][j]*M[k][l]-M[i][l]*M[k][j]
def R_of(M):
    R=[[F(0) for _ in range(3)] for _ in range(3)]
    for aa,S in enumerate(PAIRS):
        for bb,T in enumerate(PAIRS):
            Tc=tuple(sorted(ALL-set(T)))
            R[aa][bb] = det2(M,S,T)**2 + det2(M,S,Tc)**2
    return R
R=R_of(U); Rs=R_of(Us)
Rbar=[[(R[i][j]+Rs[i][j])/2 for j in range(3)] for i in range(3)]
pairclass={}
for idx,S in enumerate(PAIRS):
    pairclass[frozenset(S)] = idx
    pairclass[frozenset(ALL-set(S))] = idx
Rlam=[[F(0) for _ in range(3)] for _ in range(3)]
for sigma,w in lam.items():
    for aa,S in enumerate(PAIRS):
        bb=pairclass[frozenset(sigma[i] for i in S)]
        Rlam[aa][bb] += w
assert Rlam == Rbar

HSGN = [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
def D_from_P(P):
    return [[sum(F(HSGN[aa+1][i]*HSGN[bb+1][j],4)*P[i][j]
                 for i in range(4) for j in range(4))
             for bb in range(3)] for aa in range(3)]
D=D_from_P(P); Ds=D_from_P(Ps)
Dbar=[[(D[i][j]+Ds[i][j])/2 for j in range(3)] for i in range(3)]
Dlam=[[F(0) for _ in range(3)] for _ in range(3)]
for sigma,w in lam.items():
    Pm=[[F(0) for _ in range(4)] for _ in range(4)]
    for i,j in enumerate(sigma): Pm[i][j]=1
    Sm=D_from_P(Pm)
    for i in range(3):
        for j in range(3): Dlam[i][j]+=w*Sm[i][j]
assert Dlam == Dbar

print('PASS MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1')
print('lambda_support =', sum(w>0 for w in lam.values()))
print('Pbar_match =', Plam == Pbar)
print('Rbar_match =', Rlam == Rbar)
print('Dbar_match =', Dlam == Dbar)
print('Rbar =')
for row in Rbar: print(' ', [str(x) for x in row])
