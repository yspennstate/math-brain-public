"""Exact self-checks for X021; run from the campaign root."""
import json
from pathlib import Path
import sympy as s

checks = 0

def equal(a, b=0):
    global checks
    difference = s.expand_log(s.expand(a-b), force=True)
    if isinstance(difference, s.MatrixBase):
        assert all(s.simplify(x)==0 for x in difference), (a, b, difference)
    else:
        assert s.simplify(difference) == 0, (a, b, difference)
    checks += 1

def positive(a):
    global checks
    assert bool(a > 0), a
    checks += 1

def atoms(K):
    n = K.rows
    C = s.eye(n)-K
    return [s.simplify(s.Matrix.hstack(*[K[:,j] if mask>>j&1 else C[:,j] for j in range(n)]).det()) for mask in range(1<<n)]

def atom_derivatives(K, A):
    t = s.symbols('t', real=True)
    p = atoms(K+t*A)
    return ([s.simplify(q.subs(t,0)) for q in p],
            [s.simplify(s.diff(q,t).subs(t,0)) for q in p],
            [s.simplify(s.diff(q,t,2).subs(t,0)) for q in p])

# The exact square-root-free version of the endpoint identity.
a,b,c,d,e,f,g,h,u,v,r,q=s.symbols('a b c d e f g h u v r q', real=True)
P=s.Matrix([[a,c+s.I*d],[c-s.I*d,b]])
Q=s.Matrix([[e,g+s.I*h],[g-s.I*h,f]])
E=s.Matrix([[u,r+s.I*q],[r-s.I*q,v]])
L=P+Q; T=P-Q
endpoint=s.trace(P*E)**2+s.trace(Q*E)**2
remainder=s.trace(L*E*L*E)-s.trace(L*E)**2/2+s.trace(T*E)**2/2
equal(endpoint-2*L.det()*E.det(), remainder)

# Small exact example in Section 4.
ones=s.ones(3)
K=s.eye(3)/2+s.I*s.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])/4
A=3*ones-7*s.eye(3)
B=21*ones-14*s.eye(3)
equal(A.adjugate(),B)
for F in [K,s.eye(3)-K]:
    for n in [1,2,3]: positive(F[:n,:n].det())
for v in [s.ones(3,1),s.Matrix([1,-1,0]),s.Matrix([1,0,-1])]:
    lam=49 if v==s.ones(3,1) else -14
    equal(B*v,lam*v)
p,dp,ddp=atom_derivatives(K,A)
expected_p=[s.Rational(1,32) if mask in [0,7] else s.Rational(5,32) for mask in range(8)]
for x,y in zip(p,expected_p):equal(x,y)
expected_score=[108 if mask==0 else -108 if mask==7 else 4 if mask.bit_count()==1 else -4 for mask in range(8)]
for mask in range(8):equal(dp[mask]/p[mask],expected_score[mask])
FI=s.simplify(sum(dp[i]**2/p[i] for i in range(8)))
equal(FI,744)
D=s.simplify(sum(A[k,k]**2/(K[k,k]*(1-K[k,k])) for k in range(3)))
equal(D,192)
M=s.log(5)*s.eye(3)
equal(s.trace(M*B),21*s.log(5))
equal(-sum(ddp[i]*s.log(p[i]) for i in range(8)),42*s.log(5))
endpoint_total=0
N=s.zeros(3)
for k in range(3):
    R=[j for j in range(3) if j!=k]
    a=K[k,k]; d=A[k,k]
    vv=K.extract(R,[k]); ww=A.extract(R,[k]); F=A.extract(R,R)
    branch_FI=0
    branch_endpoint=0
    for present in [0,1]:
        pi=a if present else 1-a
        rr=a-(1-present)
        g=K[:,k] if present else (s.eye(3)-K)[:,k]
        equal((g.conjugate().T*B*g)[0],0)
        J=K.extract(R,R)-vv*vv.conjugate().T/rr
        E=F-(ww*vv.conjugate().T+vv*ww.conjugate().T)/rr+d*vv*vv.conjugate().T/rr**2
        equal(E.det(),0)
        equal(s.trace(E),-10)
        conditional_p,conditional_dp,_=atom_derivatives(J,E)
        conditional_scores=[]
        for rmask in range(4):
            full_mask=(present<<k)+sum(((rmask>>l)&1)<<j for l,j in enumerate(R))
            pivot_score=d/a if present else -d/(1-a)
            equal(conditional_p[rmask],p[full_mask]/pi)
            score=dp[full_mask]/p[full_mask]-pivot_score
            equal(conditional_dp[rmask]/conditional_p[rmask],score)
            conditional_scores.append(score)
        x,y,z,w=conditional_p
        equal(y*z/(x*w),5)
        omega=s.simplify(2+(y+z)/s.sqrt(x*w))
        equal(omega,2+2*s.sqrt(5))
        P=J.adjugate()/s.sqrt(w)
        Q=(s.eye(2)-J).adjugate()/s.sqrt(x)
        L=P+Q;T=P-Q
        fend=s.simplify(s.trace(P*E)**2+s.trace(Q*E)**2)
        equal(fend,670)
        rho=s.simplify(s.trace(L*E*L*E)-s.trace(L*E)**2/2+s.trace(T*E)**2/2)
        equal(rho,fend-2*omega*E.det())
        branch_endpoint+=pi*fend
        branch_FI+=pi*sum(conditional_dp[j]**2/conditional_p[j] for j in range(4))
        N+=omega/pi*g*g.conjugate().T
    equal(branch_endpoint,670)
    equal(branch_FI,680)
    equal(d**2/(a*(1-a))+branch_FI,FI)
    endpoint_total+=branch_endpoint
equal(endpoint_total,2010)
equal(s.trace(N*B),0)
equal(-(D+2*s.trace((N-3*M)*B)+endpoint_total)/3,-734+42*s.log(5))
positive(s.Rational(124,81)-s.Rational(32,21))

# Second rational, non-balanced example in Section 5.
Ku=s.Matrix([[s.Rational(1,5),s.Rational(1,10),s.I/20],
             [s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],
             [-s.I/20,s.Rational(1,10),s.Rational(4,5)]])
Bu=s.Matrix([[88,203-1552*s.I,-1552+122*s.I],
             [203+1552*s.I,122,-325-1552*s.I],
             [-1552-122*s.I,-325+1552*s.I,88]])/1552
for F in [Ku,s.eye(3)-Ku]:
    for n in [1,2,3]:positive(F[:n,:n].det())
for F in [Ku,s.eye(3)-Ku]:
    for k in range(3):
        g=F[:,k]
        equal((g.conjugate().T*Bu*g)[0],0)
for k in range(3):positive(Bu[k,k])
equal(Bu.det(),s.Rational(874502161,467288576))
e2=s.simplify((s.trace(Bu)**2-s.trace(Bu*Bu))/2)
equal(e2,-s.Rational(37931,12416))
positive(Bu.det());positive(-e2)
equal(s.trace(Ku*Bu),s.trace(Bu)/2)
Au=Bu.adjugate()
equal(Au.adjugate(),Bu.det()*Bu)
pu=atoms(Ku)
ratios=[]
for k in range(3):
    R=[j for j in range(3) if j!=k]
    r0,r1=[1<<j for j in R]
    row=[]
    for present in [0,1]:
        shift=present<<k
        ratio=s.simplify(pu[shift+r0]*pu[shift+r1]/(pu[shift]*pu[shift+r0+r1]))
        positive(ratio-1)
        row.append(ratio)
    ratios.append(row)
expected_ratios=[[s.Rational(209,159),s.Rational(219,169)],
                 [s.Rational(4369,3869),s.Rational(39321,35321)],
                 [s.Rational(209,159),s.Rational(219,169)]]
for row,expected in zip(ratios,expected_ratios):
    for x,y in zip(row,expected):equal(x,y)
assert ratios[0][1]!=ratios[0][0]
checks+=1

out={
    'status':'PASS', 'exact_assertions':checks,
    'small_example':{
        'K':str(K),'A':str(A),'adj_A':str(B),
        'atom_masses':[str(v) for v in p],
        'atom_scores':[str(v) for v in expected_score],
        'fisher':str(FI),'marginal_D':str(D),'endpoint_fisher':str(endpoint_total),
        'six_conditional_determinants':'all zero exactly',
        'old_curvature_upper_bound':'-64+42*log(5)>0',
        'new_curvature_upper_bound':'-734+42*log(5)<0',
        'actual_curvature':'-744+42*log(5)'},
    'unbalanced_example':{
        'K':str(Ku),'B':str(Bu),'det_B':str(Bu.det()),'e2_B':str(e2),
        'conditional_odds':[[str(v) for v in row] for row in ratios],
        'six_null_forms':'all zero exactly',
        'trace_MB':'strictly positive by positive B diagonals and conditional log ratios'},
    'scope':'Exact identities and finite examples; no universal endpoint comparison or unrestricted entropy concavity asserted.'}
path=Path(__file__).with_name('certificate.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
