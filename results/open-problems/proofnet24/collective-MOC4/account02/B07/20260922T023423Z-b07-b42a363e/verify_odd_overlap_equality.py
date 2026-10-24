from fractions import Fraction as F
from collections import defaultdict

# Exact algebraic certificate for MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1.
# Variables t0,t1,t2 are formal nonnegative masses with t0+t1+t2=1.
# A polynomial is a dict exponent-triple -> rational coefficient.

def mon(i,j):
    e=[0,0,0]
    e[i]+=1; e[j]+=1
    return tuple(e)

def normalize(p):
    return {k:v for k,v in p.items() if v}

def target_channels():
    out={}
    for i in range(3):
        j,k=[r for r in range(3) if r!=i]
        out[(i,i,'-')]={mon(i,i):F(1)}
        out[(i,i,'+')]={mon(j,j):F(1), mon(j,k):F(2), mon(k,k):F(1)}
    for i in range(3):
        for j in range(3):
            if i!=j:
                out[(i,j,'+')]={mon(i,j):F(1)}
                out[(i,j,'-')]={mon(i,j):F(1)}
    return out

# E_ij are the nine odd block-monomial colored matchings.
# If i=j: identity with exactly row i colored minus.
# If i!=j: transposition (ij), row i->j plus, row j->i minus, fixed row plus.
atoms=[]
acc=defaultdict(lambda: defaultdict(F))
for i in range(3):
    for j in range(3):
        if i==j:
            perm=[0,1,2]
            signs=['+','+','+']
            signs[i]='-'
        else:
            perm=[0,1,2]
            perm[i]=j; perm[j]=i
            signs=['+','+','+']
            signs[j]='-'
        assert sum(s=='-' for s in signs)%2==1
        atoms.append((i,j,tuple(perm),tuple(signs)))
        for r in range(3):
            acc[(r,perm[r],signs[r])][mon(i,j)] += F(1)

target=target_channels()
assert set(acc)==set(target)
for key in target:
    assert normalize(acc[key])==target[key], (key,normalize(acc[key]),target[key])

# A concrete exact mass vector independently checks normalization and channel values.
t=[F(2,11),F(3,11),F(6,11)]
assert sum(t)==1
weights={(i,j):t[i]*t[j] for i in range(3) for j in range(3)}
assert sum(weights.values())==1
q=defaultdict(F)
for i,j,perm,signs in atoms:
    w=weights[i,j]
    for r in range(3):
        q[(r,perm[r],signs[r])] += w

def eval_poly(p):
    ans=F(0)
    for exp,c in p.items():
        z=c
        for i,e in enumerate(exp):
            z*=t[i]**e
        ans+=z
    return ans

for key,p in target.items():
    assert q[key]==eval_poly(p), (key,q[key],eval_poly(p))

# Arbitrary exact support weights: verify the reflection q-objective equals
# the convex combination of the nine odd endpoint objectives.
wp=[[F(2*i-3*j+5,7) for j in range(3)] for i in range(3)]
wm=[[F(5*i+j-4,9) for j in range(3)] for i in range(3)]
Q_ref=sum((wp[i][j] if s=='+' else wm[i][j])*v
          for (i,j,s),v in q.items())
Q_mix=F(0)
for i,j,perm,signs in atoms:
    score=sum(wp[r][perm[r]] if signs[r]=='+' else wm[r][perm[r]]
              for r in range(3))
    Q_mix += weights[(i,j)]*score
assert Q_ref==Q_mix

# Exact stability identity for the equality collar:
# choose an orientation-reversing reflection H and an orientation-preserving
# rotation Rot in a +1 plane. R=H Rot still has det=-1.
def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return sum(A[i][i] for i in range(len(A)))
def frob2(A,B):
    return sum((A[i][j]-B[i][j])**2
               for i in range(len(A)) for j in range(len(A[0])))

H=eye(6); H[0][0]=F(-1)
Rot=eye(6)
c,s=F(3,5),F(4,5)
Rot[1][1]=c; Rot[2][2]=c
Rot[1][2]=-s; Rot[2][1]=s
R=mm(H,Rot)
delta=F(4-tr(R),2)
assert tr(R)==F(16,5)
assert delta==F(2,5)
assert frob2(R,H)==F(8,5)==4*delta

print("PASS MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1 exact certificate")
print("odd_atoms =", len(atoms))
print("sample_t =", [str(x) for x in t])
print("sample_weight_sum =", sum(weights.values()))
print("sample_support_objective =", Q_ref)
print("sample_mixture_objective =", Q_mix)
print("stability_trace =", tr(R))
print("stability_delta =", delta)
print("stability_distance_squared =", frob2(R,H))
print("stability_4delta =", 4*delta)
