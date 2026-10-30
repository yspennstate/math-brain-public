from collections import Counter, defaultdict
from fractions import Fraction

n=4
N=1<<n
PTS=range(N)

def bit(x,i): return (x>>i)&1
def gate(x): return bit(x,0)&bit(x,1)
V={x for x in PTS if gate(x)}
U=set(PTS)-V

def xor_all(A):
    z=0
    for x in A: z ^= x
    return z

def fval(F,x): return -1 if x in F else 1

def prod_f(F,B,y=0):
    p=1
    for x in B: p*=fval(F,x^y)
    return p

def zeta(F,A,y=0):
    AU=[x for x in A if x in U]
    AV=[x for x in A if x in V]
    return Fraction(prod_f(F,AV,y)-prod_f(F,AU,y),2)

def nu(F,A,y=0): return Fraction(1-prod_f(F,A,y),2)

def influence(F,i):
    return Fraction(sum(fval(F,x)!=fval(F,x^(1<<i)) for x in PTS),N)

D=[]
for mask in range(1<<N):
    A=tuple(x for x in PTS if (mask>>x)&1)
    if len(A)%2==0 and xor_all(A)==0:
        D.append(A)
REL=[A for A in D if sum(gate(x) for x in A)%2==1]
assert len(D)==2048 and len(REL)==1024
assert Counter(map(len,REL))==Counter({4:64,6:256,8:384,10:256,12:64})
assert all(len([x for x in A if x in U])%2==1 and len([x for x in A if x in V])%2==1 for A in REL)

cases=[("subcube-two-point",{0,4}),("weight-one-four-point",{1,2,4,8})]
print("dual_relations",len(D))
print("gate_separated_relations",len(REL))
print("shell_counts",dict(sorted(Counter(map(len,REL)).items())))

for name,F in cases:
    infl=[influence(F,i) for i in range(n)]
    folded=[min(p,1-p) for p in infl]
    J=sum(folded,Fraction(0))
    for A in REL:
        for y in PTS:
            assert zeta(F,A,y)**2==nu(F,A,y)
    max_ratio=Fraction(0)
    shell=defaultdict(lambda:[Fraction(0) for _ in range(n)])
    checks=0
    for A in REL:
        q=len(A)
        for i in range(n):
            e=Fraction(sum((zeta(F,A,y)-zeta(F,A,y^(1<<i)))**2 for y in PTS),N)
            shell[q][i]+=e
            rhs=2*q*folded[i]
            assert e<=rhs
            if rhs: max_ratio=max(max_ratio,e/rhs)
            checks+=1
    # deterministic cross-term sample; pointwise identity
    sample=REL[:64]
    for A in sample:
        AU=set(A)&U; AV=set(A)&V
        for B in sample:
            BU=set(B)&U; BV=set(B)&V
            for y in PTS:
                lhs=4*zeta(F,A,y)*zeta(F,B,y)
                rhs=(prod_f(F,AV^BV,y)-prod_f(F,AV^BU,y)
                     -prod_f(F,AU^BV,y)+prod_f(F,AU^BU,y))
                assert lhs==rhs
    print(name,"influences",[str(x) for x in infl],"J",str(J))
    print(name,"gradient_checks",checks,"max_bound_ratio",str(max_ratio))
    print(name,"shell_gradient_energy",{q:[str(v) for v in shell[q]] for q in sorted(shell)})
    print(name,"cross_identity_checks",len(sample)*len(sample)*N)

print("status PASS")
