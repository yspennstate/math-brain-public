"""Exact six-site Fourier arithmetic and diamond/exchange-flow indexing."""
from fractions import Fraction as F
from itertools import combinations, permutations

E = tuple(range(6))
LEVELS = [list(combinations(E, k)) for k in (2, 3, 4)]
SETS = sum(LEVELS, [])
SIX = {s: i for i, s in enumerate(SETS)}
AB = [(A, B) for A in LEVELS[0]
      for B in combinations([i for i in E if i not in A], 2)]
AIX = {ab: i for i, ab in enumerate(AB)}
D = [[0] * 90 for _ in SETS]
for j, (A, B) in enumerate(AB):
    J = tuple(i for i in E if i not in A + B)
    T = tuple(i for i in E if i not in B)
    for X, sign in [(A, 1), (T, 1)] + [(tuple(sorted(A + (i,))), -1) for i in J]:
        D[SIX[X]][j] = sign

# Elements a+b*eta of Q(eta), eta^2=-3.
def add(p, q): return (p[0] + q[0], p[1] + q[1])
def neg(p): return (-p[0], -p[1])
def mul(p, q): return (p[0]*q[0]-3*p[1]*q[1], p[0]*q[1]+p[1]*q[0])
def conj(p): return (p[0], -p[1])
def norm(p): return p[0]*p[0]+3*p[1]*p[1]
def power(p, n):
    out = (F(1), F(0))
    for _ in range(n): out = mul(out, p)
    return out
ZETA = (F(1, 2), F(1, 2))
FOURIER = [[power(ZETA, i*j) for j in E] for i in E]

def field_det(M):
    out = (F(0), F(0))
    for p in permutations(range(len(M))):
        v = (F(1), F(0))
        for i, j in enumerate(p): v = mul(v, M[i][j])
        if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2:
            v = neg(v)
        out = add(out, v)
    return out

def minor(rows, cols):
    return field_det([[FOURIER[i][j] for j in cols] for i in rows])

def probability_coefficients(rows, cols):
    """Coefficients of 1,x,y,z for the (0,3) SU(2) row rotation.

    x=cos(2 theta), y=sin(2 theta)cos(phi),
    z=sqrt(3)sin(2 theta)sin(phi).
    """
    scale = F(6) ** len(rows)
    A = minor(rows, cols)
    selected = tuple(i for i in (0, 3) if i in rows)
    if len(selected) != 1:
        return (norm(A)/scale, F(0), F(0), F(0))
    which = selected[0]
    replacement = tuple(3-which if i == which else i for i in rows)
    B = minor(replacement, cols)
    cross = mul(A, conj(B))
    return ((norm(A)+norm(B))/(2*scale),
            (norm(A)-norm(B))/(2*scale),
            cross[0]*(1 if which == 0 else -1)/scale,
            cross[1]/scale)

def contrast_coefficients():
    rows = []
    for X in SETS:
        if len(X) == 2:
            value = probability_coefficients(X, (0, 1))
        elif len(X) == 3:
            a = probability_coefficients(X, (0, 1, 2))
            b = probability_coefficients(X, (0, 1, 3))
            value = tuple(-u-v for u, v in zip(a, b))
        else:
            value = probability_coefficients(X, (0, 1, 2, 3))
        rows.append(value)
    return rows

def matvec(M, v): return [sum(a*b for a, b in zip(row, v)) for row in M]
def at(C, point): return [r[0]+sum(a*b for a, b in zip(r[1:], point)) for r in C]

def right_inverse_numerators():
    beta = {(2,0,0):1788, (1,1,0):-702, (1,0,1):378,
            (0,2,0):588, (0,1,1):-222, (0,0,2):228}
    gamma = {(2,1,0):-1222, (2,0,1):838, (1,2,0):838,
             (1,1,1):-357, (1,0,2):338, (0,2,1):338, (0,1,2):-122}
    out = []
    for A, B in AB:
        J = tuple(i for i in E if i not in A+B)
        row = []
        for X in SETS:
            count = tuple(len(set(X) & set(V)) for V in (A, J, B))
            if len(X) == 2: value = beta[count]
            elif len(X) == 3: value = gamma[count]
            else: value = beta[(2-count[2], 2-count[1], 2-count[0])]
            row.append(value)
        out.append(row)
    return out

def exchange_flows():
    flows, labels = [], []
    for h in E:
        for e in E:
            if h == e: continue
            for triple in combinations([i for i in E if i not in (h,e)], 3):
                f = [0] * 90
                for k in range(3):
                    a, b = triple[k], triple[(k+1) % 3]
                    f[AIX[(tuple(sorted((h,a))), tuple(sorted((e,b))))]] += 1
                    f[AIX[(tuple(sorted((h,b))), tuple(sorted((e,a))))]] -= 1
                flows.append(f); labels.append((h,e)+triple)
    return flows, labels

SIGMA = (0,2,1,3,5,4)  # x sign flip
TAU = (0,5,4,3,2,1)    # z sign flip
IDENTITY = E

def act_sets(v, perm=IDENTITY, swap=False):
    out = [F(0)]*50
    for X, value in zip(SETS, v):
        Y = tuple(sorted(perm[i] for i in X))
        if swap: Y = tuple(i for i in E if i not in Y)
        out[SIX[Y]] = value
    return out

def act_weights(v, perm=IDENTITY, swap=False):
    out = [F(0)]*90
    for (A,B), value in zip(AB, v):
        A = tuple(sorted(perm[i] for i in A)); B = tuple(sorted(perm[i] for i in B))
        if swap: A,B = B,A
        out[AIX[(A,B)]] = value
    return out

def sign_action(v, sx, sy, sz):
    if sx == -1: v = act_weights(v, SIGMA)
    if sy == -1: v = act_weights(v, swap=True)
    if sz == -1: v = act_weights(v, TAU)
    return v

def solve(M, b):
    aug = [list(map(F, row))+[F(v)] for row,v in zip(M,b)]
    n = len(b)
    for j in range(n):
        p = next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[p] = aug[p],aug[j]
        v = aug[j][j]; aug[j] = [a/v for a in aug[j]]
        for i in range(n):
            if i == j: continue
            a = aug[i][j]
            if a: aug[i] = [u-a*v for u,v in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]
