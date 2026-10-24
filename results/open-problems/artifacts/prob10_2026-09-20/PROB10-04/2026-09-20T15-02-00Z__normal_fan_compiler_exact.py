from math import gcd, exp, log
from itertools import combinations
from functools import reduce

M=23

def prim(v):
    v=tuple(int(x) for x in v)
    if v==(0,0,0):
        return None
    g=reduce(gcd,(abs(x) for x in v if x))
    v=tuple(x//g for x in v)
    for x in v:
        if x:
            if x<0: v=tuple(-y for y in v)
            break
    return v

def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])

def noncol(u,v):
    return cross(u,v)!=(0,0,0)

VW={prim((0,1,-1))}
for i in range(1,M+1):
    for j in range(1,i+1):
        VW.add(prim((i,-j,0)))
        VW.add(prim((i,-1,1-j)))

VR=set()
for u,v in combinations(sorted(VW),2):
    r=prim(cross(u,v))
    if r is not None: VR.add(r)

def var_face_rank(xi):
    A,B,C=xi
    basis=None
    if B==C:
        basis=(0,1,-1)
    for i in range(1,M+1):
        for j in range(1,i+1):
            if B>=C:
                fs=B*j
                d=(-i,j,0)
            else:
                fs=B+(j-1)*C
                d=(-i,1,j-1)
            if A*i==fs:
                if basis is None:
                    basis=d
                elif noncol(basis,d):
                    return 2
    return 1 if basis is not None else 0

vboth=vplus=vminus=vnone=0
VFAC=[]
for r in VR:
    p=(var_face_rank(r)==2)
    nr=tuple(-x for x in r)
    m=(var_face_rank(nr)==2)
    if p: VFAC.append(r)
    if m: VFAC.append(nr)
    if p and m: vboth+=1
    elif p: vplus+=1
    elif m: vminus+=1
    else: vnone+=1

endpoint_checks=0
for A in range(-4,5):
  for B in range(-4,5):
    for C in range(-4,5):
      if (A,B,C)==(0,0,0): continue
      for i in range(1,M+1):
        for j in range(1,i+1):
          brute=max(B*k+C*(j-k) for k in range(1,j+1))
          closed=B*j if B>=C else B+(j-1)*C
          assert brute==closed
          endpoint_checks+=1

def clause_states(K):
    out=[]
    for ps in range(4):
        for ns in range(4-ps):
            for pu in range(4-ps-ns):
                nu=3-ps-ns-pu
                if ps+ns<1 or ps+pu!=K: continue
                ns1=ns if ps+ns==1 else 0
                ns2=0 if ps+ns==1 else ns
                out.append((ps,ns1,ns2))
    return out
CST=[clause_states(k) for k in range(4)]
assert sum(map(len,CST))==16

CW=set()
for states in CST:
    for s,t in combinations(states,2):
        w=prim(tuple(s[k]-t[k] for k in range(3)))
        if w is not None: CW.add(w)

CR=set()
for u,v in combinations(sorted(CW),2):
    r=prim(cross(u,v))
    if r is not None: CR.add(r)

def clause_face_rank(xi):
    A,B,C=xi
    basis=None
    for states in CST:
        scores=[A*x+B*y+C*z for x,y,z in states]
        mx=max(scores)
        tied=[s for s,q in zip(states,scores) if q==mx]
        if len(tied)>1:
            b=tied[0]
            for t in tied[1:]:
                d=tuple(t[k]-b[k] for k in range(3))
                if d==(0,0,0): continue
                if basis is None: basis=d
                elif noncol(basis,d): return 2
    return 1 if basis is not None else 0

cboth=cplus=cminus=cnone=0
CFAC=[]
for r in CR:
    p=(clause_face_rank(r)==2)
    nr=tuple(-x for x in r)
    m=(clause_face_rank(nr)==2)
    if p: CFAC.append(r)
    if m: CFAC.append(nr)
    if p and m: cboth+=1
    elif p: cplus+=1
    elif m: cminus+=1
    else: cnone+=1

assert len(VFAC)==len(set(VFAC))
assert len(CFAC)==len(set(CFAC))

# Direct face-tilt identity / leakage micro-check.
S=[(0,0),(1,0),(0,1),(1,1)]
weights=[1.0,2.0,3.0,5.0]
xi=(1,0)
eta=(0.17,-0.23)
t=3.25
scores=[xi[0]*s[0]+xi[1]*s[1] for s in S]
h=max(scores)
face=[k for k,q in enumerate(scores) if q==h]
outside=[k for k,q in enumerate(scores) if q<h]
Delta=min(h-scores[k] for k in outside)
AF=log(sum(weights[k]*exp(eta[0]*S[k][0]+eta[1]*S[k][1]) for k in face))
R0=(sum(weights[k]*exp(eta[0]*S[k][0]+eta[1]*S[k][1]) for k in outside)/
    sum(weights[k]*exp(eta[0]*S[k][0]+eta[1]*S[k][1]) for k in face))
Rt=(sum(weights[k]*exp(eta[0]*S[k][0]+eta[1]*S[k][1])*exp(-t*(h-scores[k])) for k in outside)/
    sum(weights[k]*exp(eta[0]*S[k][0]+eta[1]*S[k][1]) for k in face))
A=log(sum(weights[k]*exp((t*xi[0]+eta[0])*S[k][0]+(t*xi[1]+eta[1])*S[k][1]) for k in range(len(S))))
identity_error=abs(A-(t*h+AF+log(1+Rt)))
assert identity_error<1e-12
assert Rt <= R0*exp(-t*Delta)*(1+1e-14)

print("PROB10_04_NORMAL_FAN_COMPILER_EXACT_CHECK")
print("M =",M)
print("VARIABLE_PRIMITIVE_WALLS =",len(VW))
print("VARIABLE_CANDIDATE_UNORIENTED_RAYS =",len(VR))
print("VARIABLE_FACET_ORIENTED_NORMALS =",len(VFAC))
print("VARIABLE_RAY_LINES_BOTH_ORIENTATIONS_FACETS =",vboth)
print("VARIABLE_RAY_LINES_PLUS_ONLY_FACET =",vplus)
print("VARIABLE_RAY_LINES_MINUS_ONLY_FACET =",vminus)
print("VARIABLE_RAY_LINES_NO_FACET =",vnone)
print("CLAUSE_PRIMITIVE_WALLS =",len(CW))
print("CLAUSE_CANDIDATE_UNORIENTED_RAYS =",len(CR))
print("CLAUSE_FACET_ORIENTED_NORMALS =",len(CFAC))
print("CLAUSE_RAY_LINES_BOTH_ORIENTATIONS_FACETS =",cboth)
print("CLAUSE_RAY_LINES_PLUS_ONLY_FACET =",cplus)
print("CLAUSE_RAY_LINES_MINUS_ONLY_FACET =",cminus)
print("CLAUSE_RAY_LINES_NO_FACET =",cnone)
print("COPY_SIMPLEX_FACETS = 5")
print("FULL_COMPONENT_FACET_INEQUALITIES_BEFORE_INTERSECTION_REDUNDANCY =",len(VFAC)+len(CFAC)+5)
print("ENDPOINT_MAXIMIZER_EXHAUSTIVE_INTEGER_CHECKS =",endpoint_checks)
print("FACE_TILT_TOY_DELTA =",Delta)
print("FACE_TILT_IDENTITY_ERROR =",format(identity_error,'.3e'))
print("ALL_EXACT_NORMAL_FAN_CHECKS_PASS = True")