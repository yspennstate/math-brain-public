"""Exact identities and rational witnesses for X072; decimals are illustrations."""
from pathlib import Path
import json
import sympy as S
import mpmath as mp

R=S.Rational; I=S.I
HERE=Path(__file__).resolve().parent
checks=0
def check(x):
    global checks
    assert x
    checks+=1
def zero(x):
    check(S.simplify(x)==0)
def atoms(K):
    n=K.rows
    return [S.expand((-1)**(n-mask.bit_count())*
            (K-S.diag(*[0 if mask>>j&1 else 1 for j in range(n)])).det())
            for mask in range(1<<n)]
def jets(K,A):
    t=S.Symbol('t',real=True)
    ps=atoms(K+t*A)
    return [[S.simplify(S.diff(p,t,j).subs(t,0)) for p in ps] for j in range(3)]
def grads2(J):
    adj=J.adjugate()
    return [adj-S.eye(2),S.diag(1,0)-adj,S.diag(0,1)-adj,adj]
def strictly_physical(K):
    margins=[]
    for J in (K,S.eye(K.rows)-K):
        for size in range(1,K.rows+1):
            value=S.simplify(J[:size,:size].det())
            check(value>0); margins.append(str(value))
    return margins
def num(x):
    return mp.mpf(str(S.N(x,90)))
def entropy(ps):
    return -sum(num(p)*mp.log(num(p)) for p in ps if p!=0)
def curvature(K,A):
    p,q,r=jets(K,A)
    return sum(num(qi)**2/num(pi)+num(ri)*mp.log(num(pi)) for pi,qi,ri in zip(p,q,r))
def Pswap():
    return S.Matrix([[1,0,0],[0,0,1],[0,1,0]])
P=Pswap()
def sym(K): return (K+P*K*P)/2
def swapmask(mask): return (mask&1)|((mask&2)<<1)|((mask&4)>>1)

# All eight atoms of the arbitrary-lambda channel, symbolically.
a,u,lam,x,y=S.symbols('a u lam x y',real=True)
rr=x+I*y
M=S.Matrix([[a,S.conjugate(rr)],[rr,u]])
K=S.Matrix([[a,S.conjugate(rr)/S.sqrt(2),S.conjugate(rr)/S.sqrt(2)],
            [rr/S.sqrt(2),(u+lam)/2,(u-lam)/2],
            [rr/S.sqrt(2),(u-lam)/2,(u+lam)/2]])
pm=atoms(M)
channel=[[1-lam,0],[lam/2,(1-lam)/2],[lam/2,(1-lam)/2],[0,lam]]
for mask,p in enumerate(atoms(K)):
    pivot=mask&1; leaf=mask>>1
    zero(p-sum(pm[pivot+2*bit]*channel[leaf][bit] for bit in (0,1)))

# Exact refinement probabilities behind (9), including all group weights.
ss=(1-2*lam)/(1-lam); dd=lam/(1-lam)
wg=[(1-lam)/2,(1-lam)/2,lam]
split=[ss/2,ss/2,dd]
for bit in (0,1):
    for g in range(3):
        positive=g+1
        slope=ss if g<2 else S.Integer(1)
        intercept=dd if g<2 else S.Integer(0)
        zero(channel[0][bit]*split[g]-wg[g]*(1-intercept-slope*bit))
        zero(channel[positive][bit]-wg[g]*(intercept+slope*bit))
zero(sum(wg)-1); zero(sum(split)-1)

# Every swap-odd direction has rank at most two and opposite eigenvalues.
d,e,zr,zi=S.symbols('d e zr zi',real=True)
z=zr+I*zi
Odd=S.Matrix([[0,z,-z],[S.conjugate(z),d,I*e],[-S.conjugate(z),-I*e,-d]])
check(P*Odd*P==-Odd)
zero(Odd.det()); zero(S.trace(Odd))
zero(S.trace(Odd*Odd)/2-(d*d+e*e+2*(zr*zr+zi*zi)))

# Corrected conditional gradient identity and full fixed-pivot logarithmic work.
Kgen=S.Matrix([[R(1,5),R(1,10),I/20],[R(1,10),R(3,5),R(1,10)],
               [-I/20,R(1,10),R(4,5)]])
strictly_physical(Kgen)
av=Kgen[0,0]; bv=1-av; C=Kgen[1:,1:]; v=Kgen[1:,0]
Q=v*v.conjugate().T; J1=C-Q/av; J0=C+Q/bv
logs=S.symbols('ell0:8',real=True)
gr1=grads2(J1); gr0=grads2(J0)
G=S.zeros(2); Qg=S.zeros(2)
for mask in range(4):
    G+=-logs[2*mask+1]*gr1[mask]+logs[2*mask]*gr0[mask]
    Qg+=(logs[2*mask]-logs[2*mask+1])*grads2(C)[mask]
ll1=logs[3]+logs[5]-logs[1]-logs[7]
ll0=logs[2]+logs[4]-logs[0]-logs[6]
for val in G+(ll1/av+ll0/bv)*Q.adjugate()-Qg: zero(val)
B=S.Matrix([[R(1,7),(2+I)/13],[(2-I)/13,-R(1,9)]])
wvec=S.Matrix([(1+2*I)/11,(-2+I)/17])
Ag=S.zeros(3); Ag[1:,1:]=B; Ag[1:,0]=wvec; Ag[0,1:]=wvec.conjugate().T
T=wvec*v.conjugate().T+v*wvec.conjugate().T
work=sum(r*l for r,l in zip(jets(Kgen,Ag)[2],logs))
rhs=-2*(av*ll1+bv*ll0)*B.det()-2*(ll0-ll1)*S.trace(B.adjugate()*T)+2*(wvec.conjugate().T*Qg*wvec)[0]
zero(work-rhs)

# Exact parity cancellation for all five even by four odd basis pairs.
Kstar=S.Matrix([[R(2,5),R(1,10),R(1,10)],
                [R(1,10),R(3,5),R(1,5)],
                [R(1,10),R(1,5),R(3,5)]])
strictly_physical(Kstar)
E11=S.diag(1,0,0)
Lc=S.diag(0,1,1)
Lr=S.Matrix([[0,0,0],[0,0,1],[0,1,0]])
Vr=S.Matrix([[0,1,1],[1,0,0],[1,0,0]])
Vi=S.Matrix([[0,I,I],[-I,0,0],[-I,0,0]])
even=[E11,Lc,Lr,Vr,Vi]
odd=[Odd.subs({d:1,e:0,zr:0,zi:0}),Odd.subs({d:0,e:1,zr:0,zi:0}),
     Odd.subs({d:0,e:0,zr:1,zi:0}),Odd.subs({d:0,e:0,zr:0,zi:1})]
pst=atoms(Kstar)
for Aev in even:
    pe,qe,re=jets(Kstar,Aev)
    for Aod in odd:
        po,qo,ro=jets(Kstar,Aod)
        _,_,both=jets(Kstar,Aev+Aod)
        mixed=[S.simplify((zz-xx-yy)/2) for zz,xx,yy in zip(both,re,ro)]
        zero(sum(ee*oo/pp for ee,oo,pp in zip(qe,qo,pst)))
        for mask in range(8): zero(mixed[mask]+mixed[swapmask(mask)])

# Two dense complex, full-rank indefinite endpoint chords.
Qminus=S.Matrix([[0,0,0],[0,R(1,2),-R(1,2)],[0,-R(1,2),R(1,2)]])
Amean=S.Matrix([[0,R(1,20),I/30],[R(1,20),R(1,25),(1+2*I)/40],
                [-I/30,(1-2*I)/40,-R(1,50)]])
Aspect=S.Matrix([[R(1,20),(1+I)/20,-R(1,30)],
                [(1-I)/20,R(1,25),R(1,100)+I/40],
                [-R(1,30),R(1,100)-I/40,-R(1,50)]])
mp.mp.dps=80
examples=[]
for name,A in [('fixed_measured_pivot',Amean),('fixed_spectator_moving_pivot',Aspect)]:
    check(A.det()!=0)
    check(A[:2,:2].det()<0 if name=='fixed_measured_pivot' else A[1:,1:].det()<0)
    zero(A[0,0] if name=='fixed_measured_pivot' else S.trace(Qminus*A))
    check(A[1,0]!=A[2,0])
    endpoints=[Kstar-A,Kstar+A]
    margins=[strictly_physical(V) for V in endpoints]
    avgs=[sym(V) for V in endpoints]
    zero(S.trace((sym(Kstar)-Kstar)**2))
    hmid=entropy(atoms(Kstar)); hend=[entropy(atoms(V)) for V in endpoints]
    havg=[entropy(atoms(V)) for V in avgs]
    fullgap=hmid-sum(hend)/2
    evengap=hmid-sum(havg)/2
    symgaps=[hh-he for hh,he in zip(havg,hend)]
    check(abs(fullgap-evengap-sum(symgaps)/2)<mp.mpf('1e-70'))
    # The signs are consequences of the analytic theorem; these are illustrations.
    examples.append(dict(name=name,direction_determinant=str(S.factor(A.det())),
        endpoint_leading_minors=margins,
        midpoint_gap=str(fullgap),even_gap=str(evengap),
        symmetrization_gaps=[str(t) for t in symgaps],
        negative_hessian_at_midpoint=str(curvature(Kstar,A))))

# Independent numerical display check of the entropy refinement, not a sign proof.
lambda0=R(2,5); active=S.Matrix([[R(2,5),S.sqrt(2)/10],[S.sqrt(2)/10,R(4,5)]])
s0=(1-2*lambda0)/(1-lambda0); d0=lambda0/(1-lambda0)
Sm=S.diag(1,S.sqrt(s0)); Nm=S.diag(0,d0)+Sm*active*Sm
ww=[(1-lambda0)/2,(1-lambda0)/2,lambda0]; ell=[s0/2,s0/2,d0]
refine=entropy(ww)+num(1-lambda0)*entropy(atoms(Nm))+num(lambda0)*entropy(atoms(active))-num((1-lambda0)*(1-active[1,1]))*entropy(ell)
check(abs(refine-entropy(atoms(Kstar)))<mp.mpf('1e-70'))

out=dict(status='PASS',exact_assertions=checks-3,high_precision_identity_checks=3,
         examples=examples,scope='Analytic restricted Bellman theorem; no universal proof or numerical sign certificate.')
(HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
