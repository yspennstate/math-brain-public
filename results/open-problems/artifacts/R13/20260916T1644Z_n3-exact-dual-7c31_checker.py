import sympy as sp
import itertools

print("R13 exact n=3 Komlos finite-core checker")

q=sp.sqrt(22)
K=(sp.sqrt(11)+sp.sqrt(2))/3
t=sp.simplify(1/K**2)
t_expected=(13-2*q)/9
assert sp.simplify(t-t_expected)==0
assert sp.N(K,30) > sp.Rational(1576,1000)
assert sp.N(K,30) < sp.Rational(1577,1000)
print("K3 =", sp.simplify(K))
print("t* =", sp.simplify(t))

# Critical 2+1+1 dual certificate.
lam=(4*q-11)/33
mu=(1-lam)/2
assert sp.simplify(lam+2*mu-1)==0
assert bool(lam>0) and bool(mu>0)
d_single=sp.simplify(1/(1/lam+2/mu))
d_pair=sp.simplify(1/(1/mu+1/mu))
D=sp.simplify(2*d_single+d_pair)
assert sp.simplify(D-t)==0

L=sp.symbols('L', positive=True)
Dsym=sp.simplify(2/(1/L+4/(1-L))+(1-L)/4)
der=sp.factor(sp.diff(Dsym,L))
assert sp.simplify(der + (33*L**2+22*L-7)/(4*(3*L+1)**2))==0
assert sp.simplify(33*lam**2+22*lam-7)==0
print("critical dual lambda =", sp.simplify(lam))
print("critical dual D(lambda) =", D)

# Equality construction before scaling.
a=(q-2)/6
b=(8-q)/12
assert sp.simplify(a+2*b-1)==0
assert sp.simplify(2*a*a-t)==0
assert sp.simplify(2*b*b+sp.Rational(1,4)-t)==0

S=[
    sp.Matrix([1,1,1]),
    sp.Matrix([1,-1,-1]),
    sp.Matrix([-1,1,-1]),
    sp.Matrix([-1,-1,1]),
]
M0=sp.Matrix([
    [a,b,b],
    [a,-b,-b],
    [0,sp.Rational(1,2),-sp.Rational(1,2)]
])
M=sp.simplify(K*M0)

# Column norms exactly one.
for j in range(3):
    norm2=sp.simplify(sum(M[i,j]**2 for i in range(3)))
    assert norm2==1

# Every Boolean signing has discrepancy >=K; and one has exactly K.
ratios=[]
for eps in itertools.product([-1,1], repeat=3):
    y=M*sp.Matrix(eps)
    maxsq=max([sp.N(sp.simplify(v**2/K**2),50) for v in y])
    assert maxsq >= 1
    ratios.append((eps,[sp.simplify(v/K) for v in y]))
for eps, vals in ratios:
    sq=[sp.simplify(v**2) for v in vals]
    if all(bool(v<=1) for v in sq) and any(v==1 for v in sq):
        break
else:
    raise AssertionError("no exact minimizing signing")
print("lower-bound matrix M =")
sp.pprint(M)
print("one exact minimizing signing:", eps, vals)

# Exhaustive combinatorial classification of witness partitions/orientations.
def partitions(seq):
    if not seq:
        yield []
        return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield [[first]]+[b[:] for b in rest]
        for i in range(len(rest)):
            new=[b[:] for b in rest]
            new[i]=[first]+new[i]
            yield new

seen=set()
parts=[]
for p in partitions([0,1,2,3]):
    key=tuple(sorted(tuple(sorted(b)) for b in p))
    if key not in seen:
        seen.add(key)
        parts.append([list(b) for b in key])
assert len(parts)==15

def same_oriented_pair(block, signs):
    for i,j in itertools.combinations(block,2):
        if signs[i]==signs[j]:
            return True
    return False

non_easy=[]
for p in parts:
    for sigtuple in itertools.product([-1,1], repeat=4):
        signs=dict(enumerate(sigtuple))
        easy=any(len(b)>=3 for b in p) or any(
            len(b)==2 and same_oriented_pair(b,signs) for b in p
        )
        if not easy:
            sizes=sorted(map(len,p))
            assert sizes in ([1,1,1,1],[1,1,2],[2,2])
            for b in p:
                if len(b)==2:
                    assert signs[b[0]]==-signs[b[1]]
            non_easy.append((tuple(sizes),p,sigtuple))
print("partitions:",len(parts),"non-easy oriented configs:",len(non_easy))

# Tetrahedral pair structure: a pair and its complementary pair differ
# in exactly the same two coordinates.
for i,j in itertools.combinations(range(4),2):
    si=S[i]; sj=S[j]
    same=[r for r in range(3) if si[r]==sj[r]]
    diff=[r for r in range(3) if si[r]!=sj[r]]
    assert len(same)==1 and len(diff)==2
    rem=[k for k in range(4) if k not in (i,j)]
    sk,sl=S[rem[0]],S[rem[1]]
    diff2=[r for r in range(3) if sk[r]!=sl[r]]
    assert diff2==diff
print("tetrahedral pair/complement coordinate structure: PASS")

# Easy lower bounds dominate the critical value.
assert bool(sp.Rational(4,9)>t)
assert bool(sp.Rational(1,2)>t)
assert bool(sp.Integer(1)>t)
print("case lower bounds: singleton 4/9; pair+pair 1/2; same-oriented pair/block>=3 gives 1; critical 2+1+1 gives t*")

# n=2 exact Hadamard lower certificate.
H2=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
for j in range(2):
    assert sp.simplify(sum(H2[i,j]**2 for i in range(2)))==1
for eps in itertools.product([-1,1], repeat=2):
    y=H2*sp.Matrix(eps)
    assert max([sp.simplify(v**2) for v in y])==2
print("n=2 exact Hadamard lower certificate: PASS")

print("ALL_EXACT_CHECKS_PASS")
