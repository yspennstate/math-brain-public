from fractions import Fraction
from itertools import combinations

N=11
COVERS=[
    (0,1),(0,5),(1,2),(1,6),(1,10),(2,3),
    (4,1),(4,5),(5,3),(5,6),(6,7),
    (8,9),(9,5),(9,10),(10,3),(10,7)
]
CHAINS=[(0,1,2,3),(4,5,6,7),(8,9,10)]

def transitive_closure(edges):
    lt=[[False]*N for _ in range(N)]
    for a,b in edges: lt[a][b]=True
    for k in range(N):
        for i in range(N):
            if lt[i][k]:
                for j in range(N):
                    if lt[k][j]: lt[i][j]=True
    assert all(not lt[i][i] for i in range(N))
    return lt

lt=transitive_closure(COVERS)
def comp(a,b): return lt[a][b] or lt[b][a]
def inc(a,b): return a!=b and not comp(a,b)
def preds_with(L,x): return {i for i in range(N) if L[i][x]}
def succs_with(L,x): return {i for i in range(N) if L[x][i]}
def preds(x): return preds_with(lt,x)
def succs(x): return succs_with(lt,x)

# Designated 3-chain cover; exact width is three.
assert sorted(x for c in CHAINS for x in c)==list(range(N))
for c in CHAINS:
    for i in range(len(c)-1): assert lt[c[i]][c[i+1]]
assert all(inc(a,b) for a,b in combinations((0,4,8),2))
for four in combinations(range(N),4):
    assert not all(inc(a,b) for a,b in combinations(four,2))

# Uniform enumeration of every linear extension.
predmask=[]
for v in range(N):
    m=0
    for u in range(N):
        if lt[u][v]: m|=1<<u
    predmask.append(m)
extensions=[]
def rec(mask, seq):
    if len(seq)==N:
        extensions.append(tuple(seq)); return
    for v in range(N):
        if mask>>v&1: continue
        if predmask[v] & ~mask: continue
        rec(mask|1<<v, seq+[v])
rec(0,[])
E=len(extensions)
assert E==932
positions=[]
for L in extensions:
    p=[0]*N
    for i,v in enumerate(L): p[v]=i
    positions.append(p)
def count_event(fn): return sum(1 for p in positions if fn(p))

# Every incomparable-pair probability.
counts={}
for a,b in combinations(range(N),2):
    if inc(a,b):
        counts[(a,b)]=count_event(lambda p,a=a,b=b:p[a]<p[b])
expected={
(0,4):466,(0,8):417,(0,9):736,(1,5):740,(1,8):98,(1,9):344,
(2,5):300,(2,6):616,(2,7):848,(2,8):16,(2,9):80,(2,10):464,
(3,6):164,(3,7):506,(4,8):417,(4,9):736,(5,10):662,(6,10):284
}
assert counts==expected

# Incomparability graph is connected.
seen={0}; stack=[0]
while stack:
    v=stack.pop()
    for w in range(N):
        if w not in seen and inc(v,w):
            seen.add(w);stack.append(w)
assert len(seen)==N

# Record, rather than hide, the non-prime limitation of this local selector adversary.
def relation(z,m):
    return -1 if lt[z][m] else (1 if lt[m][z] else 0)
modules=[]
for mask in range(1,(1<<N)-1):
    S=[i for i in range(N) if mask>>i&1]
    if len(S)==1: continue
    ok=True
    for z in range(N):
        if z in S: continue
        if len({relation(z,m) for m in S})>1:
            ok=False; break
    if ok: modules.append(tuple(S))
assert modules==[(0,4),(8,9)]

# Lead crossed-neighborhood selector, first endpoint x=5,y=10.
x,y=5,10
D=preds(y)-preds(x)
U=succs(x)-succs(y)
assert D=={1} and U=={6}
Nxy=count_event(lambda p:p[x]<p[y])
alpha=count_event(lambda p:p[x]<p[1])
beta=count_event(lambda p:p[6]<p[y])
eta=count_event(lambda p:p[x]<p[1] and p[6]<p[y])
assert (Nxy,alpha,beta,eta)==(662,192,284,84)
assert 2*Nxy-E==alpha+beta-eta==392
assert E < 6*alpha < 2*E and E < 6*beta < 2*E
assert 3*Nxy>2*E and beta>alpha

# Greedy largest canonical fringe event therefore chooses upper fringe:
# minority event 6<10, majority endpoint 10<6.
x2,y2=10,6
N2=count_event(lambda p:p[x2]<p[y2])
D2=preds(y2)-preds(x2)
U2=succs(x2)-succs(y2)
assert D2=={5} and U2=={3}
alpha2=count_event(lambda p:p[x2]<p[5])
beta2=count_event(lambda p:p[3]<p[y2])
eta2=count_event(lambda p:p[x2]<p[5] and p[3]<p[y2])
assert (N2,alpha2,beta2,eta2)==(648,270,164,70)
assert 2*N2-E==alpha2+beta2-eta2==364
assert E < 6*alpha2 < 2*E and E < 6*beta2 < 2*E
assert 3*N2>2*E and alpha2>beta2

# The next greedy largest fringe is the lower event 10<5,
# whose complementary majority endpoint is exactly 5<10: a 2-cycle.
assert E-alpha2==Nxy

# Apply account03/B10's exact two-child conditioning identity to the
# complementary majority-late larger-predecessor orientation.
# Step 1 labels (a,b,d)=(10,5,1).
gamma1=count_event(lambda p:p[1]<p[5])
minority1=count_event(lambda p:p[10]<p[5])
assert (gamma1,minority1)==(740,270)
plus1=transitive_closure(COVERS+[(1,5)])
assert preds_with(plus1,10)==preds_with(plus1,5)
assert Fraction(minority1,gamma1)==Fraction(27,74)
assert Fraction(1,3)<=Fraction(minority1,gamma1)<=Fraction(2,3)
assert Fraction(minority1,E)==Fraction(gamma1,E)*Fraction(minority1,gamma1)

# Step 2 labels (a,b,d)=(6,10,5).
gamma2=count_event(lambda p:p[5]<p[10])
minority2=count_event(lambda p:p[6]<p[10])
assert (gamma2,minority2)==(662,284)
plus2=transitive_closure(COVERS+[(5,10)])
assert preds_with(plus2,6)==preds_with(plus2,10)
assert Fraction(minority2,gamma2)==Fraction(142,331)
assert Fraction(1,3)<=Fraction(minority2,gamma2)<=Fraction(2,3)
assert Fraction(minority2,E)==Fraction(gamma2,E)*Fraction(minority2,gamma2)

print("POS3_GREEDY_FRINGE_2CYCLE_PASS")
print("n",N,"E",E,"width",3,"width_witness",(0,4,8))
print("chains",CHAINS)
print("covers",COVERS)
print("incomparability_connected",True)
print("proper_autonomous_modules",modules)
print("incomparable_pairs",len(counts))
for (a,b),c in sorted(counts.items()):
    f=Fraction(c,E)
    print("pair",a,b,"count",c,"prob",f,"balanced",Fraction(1,3)<=f<=Fraction(2,3))
print("step1 endpoint",(5,10),"prob",Fraction(Nxy,E),
      "D",sorted(D),"U",sorted(U),
      "alpha",Fraction(alpha,E),"beta",Fraction(beta,E),
      "eta",Fraction(eta,E),"union",Fraction(alpha+beta-eta,E))
print("step1 greedy_max upper ->",(10,6),"majority_prob",Fraction(E-beta,E))
print("step2 endpoint",(10,6),"prob",Fraction(N2,E),
      "D",sorted(D2),"U",sorted(U2),
      "alpha",Fraction(alpha2,E),"beta",Fraction(beta2,E),
      "eta",Fraction(eta2,E),"union",Fraction(alpha2+beta2-eta2,E))
print("step2 greedy_max lower ->",(5,10),"majority_prob",Fraction(E-alpha2,E))
print("greedy_cycle",(5,10),"->",(10,6),"->",(5,10))
print("conditioning_step1 gamma",Fraction(gamma1,E),
      "equal_pred_child_prob_10_lt_5",Fraction(minority1,gamma1),
      "original_prob_10_lt_5",Fraction(minority1,E))
print("conditioning_step2 gamma",Fraction(gamma2,E),
      "equal_pred_child_prob_6_lt_10",Fraction(minority2,gamma2),
      "original_prob_6_lt_10",Fraction(minority2,E))
print("ORDINAL_PADDING: for all s,t>=0, C_s + P + C_t preserves these 18 incomparable-pair probabilities and has 3-chain cover lengths (4+s+t,4,3).")
