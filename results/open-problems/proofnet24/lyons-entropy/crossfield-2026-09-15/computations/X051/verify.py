"""Deterministic exact verification of X051 count jets; decimals only diagnostics."""
import itertools, math, json
import sympy as s
import numpy as np
from pathlib import Path
R=s.Rational

def Q(n,j,k):
    if j>n: return s.S.Zero
    return sum((-1)**(j-a)*s.binomial(k,a)*s.binomial(n-k,j-a) for a in range(j+1))/s.binomial(n,j)

def atom_jets(K,A):
    n=K.rows
    out={}
    for mask in range(1<<n):
        J=[i for i in range(n) if mask>>i&1]
        M=K-s.diag(*[0 if i in J else 1 for i in range(n)])
        prob=(-1)**(n-len(J))*M.det()
        B=M.inv()*A
        first=s.factor(prob*s.trace(B))
        second=s.factor(prob*(s.trace(B)**2-s.trace(B*B)))
        out[mask]=(prob,first,second)
    return out

def count_jets(jets,p,q):
    out={(k,l):[s.S.Zero]*3 for k in range(p+1) for l in range(q+1)}
    for mask,j in jets.items():
        k=sum(bool(mask>>i&1) for i in range(p)); l=sum(bool(mask>>(p+i)&1) for i in range(q))
        for a in range(3):out[k,l][a]+=j[a]
    return out

def block_invariants(U):
    p=U.rows; one=s.ones(p,1); active=(one.T*U*one)[0]/p
    tr=s.trace(U); tr2=s.trace(U*U); u2=(one.T*U*U*one)[0]/p
    return tr,active,tr-active,tr2,s.factor(tr2-2*u2+active**2)

def logcoeffs(p,q,r):
    names=['alpha','beta','gamma','delta','epsilon','zeta']
    vals=np.zeros(6)
    data=[]
    for k in range(p+1):
      for l in range(q+1):
        pi=math.comb(p,k)*math.comb(q,l)/2**(p+q)
        X=float(Q(p,1,k)); Y=float(Q(q,1,l)); A2=float(Q(p,2,k)); B2=float(Q(q,2,l))
        F=1-r*X*Y
        feats=np.array([A2,B2,X*Y,float(Q(p,3,k))*Y,X*float(Q(q,3,l)),A2*B2])
        vals-=pi*np.log(F)*feats
        data.append((pi,F,X,Y,A2,B2))
    return dict(zip(names,vals)),data

assertions=0
p,q=2,3; n=p+q; z=R(1,20); r=4*p*q*z*z
K=s.eye(n)/2
for i in range(p):
 for j in range(p,n):K[i,j]=K[j,i]=z
U=s.Matrix([[R(2,7),R(1,9)+s.I/11],[R(1,9)-s.I/11,R(-1,5)]])
V=s.Matrix([[R(1,8),s.I/12,R(1,13)],[ -s.I/12,R(-2,9),R(1,14)+s.I/15],[R(1,13),R(1,14)-s.I/15,R(1,10)]])
E=s.Matrix([[R(1,6)+s.I/17,R(1,7),-s.I/19],[R(-1,8),R(1,9)+s.I/23,R(1,10)]])
W=s.diag(U,V); C=s.zeros(n)
C[:p,p:]=E; C[p:,:p]=E.conjugate().T
TU,a,d,u2,d2=block_invariants(U); TV,b,e,v2,e2=block_invariants(V)
Pa=s.eye(p)-s.ones(p)/p; Pb=s.eye(q)-s.ones(q)/q
Ed=Pa*E*Pb; ed2=s.trace(Ed*Ed.conjugate().T); normE=s.trace(E*E.conjugate().T)
countW=count_jets(atom_jets(K,W),p,q)
countC=count_jets(atom_jets(K,C),p,q)
for k in range(p+1):
 for l in range(q+1):
    pi=s.binomial(p,k)*s.binomial(q,l)/2**n
    X,Y=Q(p,1,k),Q(q,1,l); A2,B2=Q(p,2,k),Q(q,2,l)
    base=pi*(1-r*X*Y)
    fw=2*(TU*X+TV*Y-r*d*A2*Y-r*e*X*B2)
    sw=4*((TU**2-u2)*A2+(TV**2-v2)*B2+2*TU*TV*X*Y)-4*r*((d**2-d2)*Q(p,3,k)*Y+(e**2-e2)*X*Q(q,3,l)+2*d*e*A2*B2)
    fc=-8*z*s.re(sum(E))*X*Y
    sc=-8*normE*X*Y+8*r*ed2*A2*B2
    for actual,want in zip(countW[k,l],[base,pi*fw,pi*sw]):
        assert s.simplify(actual-want)==0;assertions+=1
    for actual,want in zip(countC[k,l],[base,pi*fc,pi*sc]):
        assert s.simplify(actual-want)==0;assertions+=1
assert s.simplify(sum(v[0] for v in countW.values())-1)==0;assertions+=1
for j in (1,2):assert s.simplify(sum(v[j] for v in countW.values()))==0;assertions+=1
# Touching conditional Fisher cancellation, computed directly for a mixed direction.
jets=atom_jets(K,W+C); counts=count_jets(jets,p,q)
atomFI=sum(float(s.re(v[1]**2/v[0])) for v in jets.values())
countFI=sum(float(s.re(v[1]**2/v[0])) for v in counts.values())
atomH=-sum(float(s.re(v[1]**2/v[0]))+float(s.re(v[2]))*math.log(float(s.re(v[0]))) for v in jets.values())
countH=-sum(float(s.re(v[1]**2/v[0]))+float(s.re(v[2]))*math.log(float(s.re(v[0]))/(math.comb(p,k)*math.comb(q,l))) for (k,l),v in counts.items())
assert abs((countH-atomH)-(atomFI-countFI))<1e-11;assertions+=1
# The exact physical symmetrization formula at unequal means.
a0,b0=R(2,5),R(3,7); K2=K.copy()
for i in range(n):K2[i,i]=a0 if i<p else b0
for mask,(prob,_,_) in atom_jets(K2,s.zeros(n)).items():
 k=sum(bool(mask>>i&1) for i in range(p));l=sum(bool(mask>>(p+i)&1) for i in range(q))
 want=a0**k*(1-a0)**(p-k)*b0**l*(1-b0)**(q-l)*(1-p*q*z*z*(k-p*a0)*(l-q*b0)/(p*q*a0*(1-a0)*b0*(1-b0)))
 assert s.simplify(prob-want)==0;assertions+=1
# Deterministic coefficient / remaining four-scalar diagnostics; these do not prove signs.
diag=[]
for p,q,r0 in [(2,3,.2),(3,4,.6),(4,5,.95),(2,8,.99)]:
 c,data=logcoeffs(p,q,r0);aa,bb,g,dd,ee,zz=[c[x] for x in ['alpha','beta','gamma','delta','epsilon','zeta']]
 def quad(t):
  a,d,b,e=t; I=sum(pi*(2*((a+d)*X+(b+e)*Y-r0*d*A2*Y-r0*e*X*B2))**2/F for pi,F,X,Y,A2,B2 in data)
  return I-8*aa*a*d-4*(p-2)/(p-1)*(aa-r0*dd)*d*d-8*bb*b*e-4*(q-2)/(q-1)*(bb-r0*ee)*e*e-8*g*(a+d)*(b+e)+8*r0*zz*d*e
 M=np.zeros((4,4));B=np.eye(4)
 for i in range(4):M[i,i]=quad(B[i])
 for i in range(4):
  for j in range(i):M[i,j]=M[j,i]=(quad(B[i]+B[j])-M[i,i]-M[j,j])/2
 diag.append({'p':p,'q':q,'rho':r0,'coefficients':c,'remaining_form_eigenvalues':np.linalg.eigvalsh(M).tolist()})
result={'status':'PASS','exact_assertions':assertions-1,'floating_touching_identity_assertions':1,'touching_error':abs((countH-atomH)-(atomFI-countFI)),'diagnostics':diag}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
