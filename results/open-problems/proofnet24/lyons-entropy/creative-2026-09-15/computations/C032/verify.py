"""C032: exact algebra plus numerical verification of proved sharp inequalities.
Run from the campaign root: python computations/C032/verify.py
No floating-point search is used to prove a theorem in C032.md.
"""
from pathlib import Path
import json, math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import brentq

OUT=Path(__file__).parent
mp.mp.dps=70
z=mp.findroot(lambda z:z*mp.tanh(z)-1,mp.mpf('1.2'))
vstar=z*z-1
rstar=(1-1/z)/2

# Rational certificates for the elementary coarse bounds in the obstruction.
S10=sum(sp.Rational(12,5)**j/sp.factorial(j) for j in range(11))
assert S10>11
assert sp.Rational(68,75)>sp.Rational(22,25)

K=sp.Matrix([[sp.Rational(9,10),sp.Rational(1,5)],[sp.Rational(1,5),sp.Rational(1,10)]])
A=sp.Matrix([[2,-sp.Rational(3,2)],[-sp.Rational(3,2),-2]])
t=sp.symbols('t',real=True)

def atom(K,mask):
    n=K.rows
    return sp.det(sp.Matrix.hstack(*[(K if (mask>>j)&1 else sp.eye(n)-K)[:,j] for j in range(n)]))
polys=[sp.expand(atom(K+t*A,m)) for m in range(4)]
p=[q.subs(t,0) for q in polys]
p1=[sp.diff(q,t).subs(t,0) for q in polys]
p2=[sp.diff(q,t,2).subs(t,0) for q in polys]
assert p==[sp.Rational(1,20),sp.Rational(17,20),sp.Rational(1,20),sp.Rational(1,20)]
assert p1==[-1,3,-1,-1]
assert p2==[-sp.Rational(25,2),sp.Rational(25,2),sp.Rational(25,2),-sp.Rational(25,2)]
gM=sp.simplify(sum(a*a/b for a,b in zip(p1,p)))
assert gM==sp.Rational(1200,17)
assert K.det()==sp.Rational(1,20)
assert (sp.eye(2)-K).det()==sp.Rational(1,20)
assert A.det()==-sp.Rational(25,4)
ob_H1=-3*mp.log(17)
ob_H2=-mp.mpf(1200)/17-mp.mpf(25)/2*mp.log(17)
ob_power_upper=-sp.Rational(1200,17)-sp.Rational(100,3)+sp.Rational(16200,169)
assert ob_power_upper<0
assert sum(sp.Rational(3)**j/sp.factorial(j) for j in range(6))>17

# A four-mode complex example; T_eta matches all determinant polynomials exactly.
I=sp.I
K4=sp.Matrix([
    [sp.Rational(2,5),sp.Rational(1,10),I/20,sp.Rational(1,30)],
    [sp.Rational(1,10),sp.Rational(3,5),sp.Rational(1,40),(1+I)/50],
    [-I/20,sp.Rational(1,40),sp.Rational(9,20),-sp.Rational(1,25)],
    [sp.Rational(1,30),(1-I)/50,-sp.Rational(1,25),sp.Rational(11,20)]
])
D4=sp.diag(*[sp.Rational(j,5) for j in range(1,5)])
# Componentwise |x+iy| <= |x|+|y| makes strict diagonal dominance rational.
row_bounds=[sum(abs(sp.re(K4[i,j]))+abs(sp.im(K4[i,j])) for j in range(4) if j!=i) for i in range(4)]
assert all(row_bounds[i]<min(K4[i,i],1-K4[i,i]) for i in range(4))
assert K4*D4 != D4*K4
eta=sp.symbols('eta',real=True)
base=sp.Matrix([atom(K4,m) for m in range(16)])
ref=[D4[j,j] for j in range(4)]
replaced=base
for j in range(4):
    R=sp.zeros(16,16)
    for x in range(16):
        for y in range(16):
            if x & ~(1<<j) == y & ~(1<<j):
                R[x,y]=ref[j] if (x>>j)&1 else 1-ref[j]
    replaced=eta*replaced+(1-eta)*R*replaced
atom_coeffs=[]
for mask in range(16):
    q=sp.expand(atom(D4+eta*(K4-D4),mask))
    assert sp.expand(q-replaced[mask])==0
    atom_coeffs.append([str(sp.expand(q).coeff(eta,j)) for j in range(5)])
assert sum(base)==1 and all(a>0 for a in base)
(OUT/'exact_atoms.json').write_text(json.dumps({'order':'mask 0 to 15; bit i means site i+1 occupied','K':[[str(x) for x in K4.row(i)] for i in range(4)],'D':list(map(str,ref)),'coefficient_order':'eta^0 through eta^4','atoms':atom_coeffs},indent=2))

def entropy_sp(q):
    return -sum(mp.mpf(str(x))*mp.log(mp.mpf(str(x))) for x in q if x)
H0=entropy_sp([sp.prod(ref[j] if (m>>j)&1 else 1-ref[j] for j in range(4)) for m in range(16)])
Hend=entropy_sp(base)
Hmid=entropy_sp([q.subs(eta,sp.Rational(1,2)) for q in replaced])
c4=4*vstar
linear=(H0+Hend)/2
power_bound=c4*mp.log((mp.exp(H0/c4)+mp.exp(Hend/c4))/2)
assert Hmid>power_bound>linear

# Numerical checks on arbitrary (not necessarily DPP) binary laws.
def replace(p,d,i):
    out=np.empty_like(p)
    for m in range(len(p)):
        q=p[m&~(1<<i)]+p[m|(1<<i)]
        out[m]=q*(d[i] if (m>>i)&1 else 1-d[i])
    return out

def metrics(p,d,eta):
    n=len(d)
    V=lambda q:sum((q-replace(q,d,i) for i in range(n)),np.zeros_like(q))
    p1=V(p)/eta;p2=(V(V(p))-V(p))/eta**2
    H=-p@np.log(p);H1=-p1@np.log(p);H2=-sum(p1*p1/p)-p2@np.log(p)
    chi=sum(sum((p-replace(p,d,i))**2/p) for i in range(n))
    B=0
    for i in range(n):
        for m in range(len(p)):
            if (m>>i)&1:continue
            q=p[m]+p[m|(1<<i)];r=p[m|(1<<i)]/q
            B+=q*r*(1-r)*math.log(r/(1-r))**2
    return H,H1,H2,chi,B

rng=np.random.default_rng(3203)
rows=[];min_curv=math.inf;min_stam=math.inf;max_identity=0
for n in range(1,7):
    for k in range(12):
        inp=rng.dirichlet(np.ones(1<<n)*.5)
        d=rng.uniform(.05,.95,n)
        eta0=float(rng.uniform(.1,.95))
        pp=inp.copy()
        for i in range(n):pp=eta0*pp+(1-eta0)*replace(pp,d,i)
        H,H1,H2,chi,B=metrics(pp,d,eta0)
        assert -eta0**2*H2>=chi-1e-10
        assert eta0**2*H1**2<=B*chi+1e-10
        assert B<=n*float(vstar)+1e-12
        power_slack=-H2-H1**2/(n*float(vstar))
        assert power_slack>-1e-10
        min_curv=min(min_curv,power_slack)
        # For uniform reference, reciprocal Stam with an additional noise step.
        du=np.full(n,.5);pu=inp.copy()
        for i in range(n):pu=eta0*pu+(1-eta0)*replace(pu,du,i)
        _,Hu,_,_,_=metrics(pu,du,eta0)
        I0=-eta0*Hu
        theta=.61;pnext=pu.copy()
        for i in range(n):pnext=theta*pnext+(1-theta)*replace(pnext,du,i)
        _,Hv,_,_,_=metrics(pnext,du,eta0*theta)
        I1=-eta0*theta*Hv
        if I0>1e-10 and I1>1e-12:
            slack=1/I1-1/(theta*I0)-(1/theta-1)/(n*float(vstar))
            assert slack>-1e-8;min_stam=min(min_stam,slack)

# Sharpness at iid Bernoulli p*: compare exponents below, at, above the optimum.
logit=mp.log((1-rstar)/rstar)
sharp={}
for scale in [mp.mpf('.99'),mp.mpf(1),mp.mpf('1.01')]:
    # E=e^{scale*h/vstar}; report E''/(E*scale/vstar).
    sharp[str(scale)]=str(-1/(rstar*(1-rstar))+(scale/vstar)*logit**2)
assert mp.mpf(sharp['0.99'])<0 and abs(mp.mpf(sharp['1.0']))<mp.mpf('1e-60') and mp.mpf(sharp['1.01'])>0

results={
    'status':'PASS',
    'constant':{'z_star':str(z),'r_star':str(rstar),'v_star':str(vstar),'max_exponent_per_normalized_entropy':str(1/vstar),'v_star_upper_bound':'11/25','exponential_partial_sum_minus_11':str(S10-11)},
    'first_fisher_obstruction':{'K':[[str(x) for x in K.row(i)] for i in range(2)],'A':[[str(x) for x in A.row(i)] for i in range(2)],'p':list(map(str,p)),'p1':list(map(str,p1)),'p2':list(map(str,p2)),'gM':str(gM),'entropy_slope':'-3 log 17','entropy_hessian':'-1200/17-(25/2) log 17','ratio':'(51/400) log(17)^2','ratio_decimal':str(mp.mpf(51)/400*mp.log(17)**2),'two_mode_constant':str(2*vstar),'proved_ratio_lower_bound':'68/75','power_curvature_bracket':str(ob_H2+ob_H1**2/(2*vstar)),'power_curvature_rational_upper_bound':str(ob_power_upper)},
    'four_mode_example':{'rational_row_bounds':list(map(str,row_bounds)),'exact_atom_comparisons':16,'H_D':str(H0),'H_K':str(Hend),'H_midpoint':str(Hmid),'Shannon_chord':str(linear),'sharp_power_lower_bound':str(power_bound),'improvement_over_Shannon_chord':str(power_bound-linear)},
    'replacement_numerical_checks':{'seed':3203,'laws':72,'dimensions':'1 to 6','min_power_curvature_slack':min_curv,'min_reciprocal_Stam_slack':min_stam},
    'sharpness_curvature_brackets':sharp,
    'scope':'Exact symbolic checks and rational bounds support the analytic proof. Numerical checks are corroboration only.'
}
(OUT/'results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
