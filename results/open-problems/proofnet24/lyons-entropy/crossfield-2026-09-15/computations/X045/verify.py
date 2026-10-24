"""Direct, deterministic checks for the X045 two-triangle theorem.

The theorem is analytic. These checks reproduce its atom algebra and concrete
examples; no finite sample is used as a substitute for a universal sign.
"""
from pathlib import Path
import itertools
import json
import sympy as S
import mpmath as mp

mp.mp.dps = 70
OUT = Path(__file__).resolve().parent
a, u, v, t = S.symbols('a u v t', real=True)
I = S.I
H = S.Matrix([[0,I*a,u,v],[-I*a,0,-v,u],
              [u,-v,0,0],[v,u,0,0]])
K = (S.eye(4)+H)/2
C = S.Matrix([[u,v],[-v,u]])
x, y, s, d, c = u*u, v*v, u*u+v*v, u*u-v*v, a*a
q = [(1+s)**2-c,(1-s)**2-c,1+s*s+c+2*d,
     1+s*s+c-2*d,1-s*s+c,1-s*s-c]
counts = {'exact_assertions':0}

def eq(z):
    assert S.simplify(z) == 0, z
    counts['exact_assertions'] += 1

def atom(M, bits):
    absent = [1-b for b in bits]
    return S.expand((-1)**sum(absent)*(M-S.diag(*absent)).det())

eq((C*C.T-s*S.eye(2)).norm()**2)
A = K[:2,:2]
B = K[:2,2:]
bits4 = list(itertools.product((0,1), repeat=4))
atoms = {bits:atom(K,bits) for bits in bits4}
eq(sum(atoms.values())-1)
for leaves in itertools.product((0,1),repeat=2):
    Q = S.eye(2)/2-S.diag(*[1-b for b in leaves])
    M = S.simplify(A-B*Q.inv()*B.T)
    signs = [2*b-1 for b in leaves]
    expected = A-(signs[0]*C[:,0]*C[:,0].T+
                  signs[1]*C[:,1]*C[:,1].T)/2
    for entry in M-expected:
        eq(entry)
    for core in itertools.product((0,1),repeat=2):
        eq(atoms[core+leaves]-atom(M,core)/4)
    eq(sum(atoms[core+leaves] for core in itertools.product((0,1),repeat=2))-S.Rational(1,4))

# The six densities have multiplicities 2,2,2,2,4,4 among the sixteen atoms.
polys = [S.expand(z/16) for z in q]
mult = [0]*6
for p in atoms.values():
    matches = [j for j,z in enumerate(polys) if S.expand(p-z)==0]
    assert len(matches)==1
    counts['exact_assertions'] += 1
    mult[matches[0]] += 1
assert mult == [2,2,2,2,4,4]
counts['exact_assertions'] += 1

# Conditioning on the shared edge creates a nonzero exterior cross entry.
N = S.eye(2)/2-B.T*A.inv()*B
eq(N[0,1]-I*a*s/(2*(1-a*a)))

# Exact determinant-ratio and axis hyperbolic identities.
ss, dd, cc = S.symbols('ss dd cc', real=True)
r_plus = cc/(1+ss)**2
r_minus = cc/(1-ss)**2
qp = [(1+ss)**2-cc,(1-ss)**2-cc,
      1+ss*ss+cc+2*dd,1+ss*ss+cc-2*dd,
      1-ss*ss+cc,1-ss*ss-cc]
ratio = S.prod(qp[:4])/(qp[4]*qp[5])**2
axis_ratio = (1-r_plus*r_plus)*(1-r_minus*r_minus)/(1-r_plus*r_minus)**2
eq(ratio.subs(dd,ss)-axis_ratio)
eq(axis_ratio-(1-((r_minus-r_plus)/(1-r_plus*r_minus))**2))
axis_Gx_ratio = (((1+ss)**2-cc)*((1-ss)**2+cc)/
                (((1+ss)**2+cc)*((1-ss)**2-cc)))
eq(axis_Gx_ratio-(1-r_plus)*(1+r_minus)/((1+r_plus)*(1-r_minus)))

# Formal coefficient checks for the full strength-Hessian identity (10).
alpha, beta = S.symbols('alpha beta', real=True)
vel = [S.diff(z,ss)*alpha+S.diff(z,dd)*beta for z in qp]
acc = [S.diff(z,ss,2)*alpha**2+2*S.diff(z,ss,dd)*alpha*beta+
       S.diff(z,dd,2)*beta**2 for z in qp]
for j, z in enumerate(acc):
    eq(z-(2 if j<4 else -2)*alpha**2)
fisher = sum(m*z*z/q0 for m,z,q0 in zip([1,1,1,1,2,2],vel,qp))/8
fisher_expected = (alpha**2*((1+ss)**2/qp[0]+(1-ss)**2/qp[1])/2+
                  ((ss*alpha+beta)**2/qp[2]+(ss*alpha-beta)**2/qp[3])/2+
                  ss**2*alpha**2*(1/qp[4]+1/qp[5]))
eq(fisher-fisher_expected)

def num(z):
    return mp.mpf(str(S.N(z,75)))

def entropy(prob):
    return -sum(p*mp.log(p) for p in prob if p)

# Both endpoints are strong-coupling strict diamonds. All four cross edges move.
p0 = {a:S.Rational(1,3),u:S.Rational(3,5),v:S.Rational(2,5)}
p1 = {a:S.Rational(1,3),u:S.Rational(2,5),v:S.Rational(3,5)}
hu, hv = p1[u]-p0[u], p1[v]-p0[v]
for pt in (p0,p1):
    margin = 1-abs(pt[a])-s.subs(pt)
    assert margin > 0
    counts['exact_assertions'] += 1
assert p0[u]*p1[v]-p1[u]*p0[v] != 0
counts['exact_assertions'] += 1
direction = K.diff(u)*hu+K.diff(v)*hv
eq(direction.det()-(hu*hu+hv*hv)**2/16)

curvature_checks=[]
maxerr=mp.mpf('0')
for theta in [S.Rational(0),S.Rational(1,4),S.Rational(1,2),
              S.Rational(3,4),S.Rational(1)]:
    pt={a:p0[a],u:p0[u]+theta*hu,v:p0[v]+theta*hv}
    pp=[num(z.subs(pt)) for z in atoms.values()]
    dp=[num((hu*S.diff(z,u)+hv*S.diff(z,v)).subs(pt)) for z in atoms.values()]
    d2p=[num((hu*hu*S.diff(z,u,2)+2*hu*hv*S.diff(z,u,v)+
              hv*hv*S.diff(z,v,2)).subs(pt)) for z in atoms.values()]
    minus_H2=sum(dz*dz/z+ddz*mp.log(z) for z,dz,ddz in zip(pp,dp,d2p))
    qn=[num(z.subs(pt)) for z in q]
    qdot=[num((hu*S.diff(z,u)+hv*S.diff(z,v)).subs(pt)) for z in q]
    qddot=[num((hu*hu*S.diff(z,u,2)+2*hu*hv*S.diff(z,u,v)+
                hv*hv*S.diff(z,v,2)).subs(pt)) for z in q]
    full_lift=sum(m*(dz*dz/z+ddz*mp.log(z))/16
                  for m,z,dz,ddz in zip(mult,qn,qdot,qddot))
    e=abs(minus_H2-full_lift)
    maxerr=max(maxerr,e)
    assert e < mp.mpf('1e-60')
    quartic_curvature=num((3*u*u*hu*hu+3*v*v*hv*hv).subs(pt))
    assert minus_H2 >= quartic_curvature
    curvature_checks.append({'t':str(theta),'minus_H_second':str(minus_H2),
                             'quartic_lower_bound':str(quartic_curvature)})

# An exact physical point has a negative separate determinant coefficient.
aa, ss0, dd0 = S.Rational(1,2), S.Rational(1,5), S.Rational(9,50)
bad_ratio = S.factor(ratio.subs({ss:ss0,dd:dd0,cc:aa*aa}))
assert 0 < bad_ratio < 1
counts['exact_assertions'] += 1
bad_fisher=S.factor(fisher_expected.subs({ss:ss0,dd:dd0,cc:aa*aa,alpha:1,beta:0}))
bad_hessian=num(bad_fisher)+mp.log(num(bad_ratio))/4
assert bad_hessian > mp.mpf('0.5')

probs0=[num(z.subs(p0)) for z in atoms.values()]
probs1=[num(z.subs(p1)) for z in atoms.values()]
pm={a:p0[a],u:(p0[u]+p1[u])/2,v:(p0[v]+p1[v])/2}
probsm=[num(z.subs(pm)) for z in atoms.values()]
gap=entropy(probsm)-(entropy(probs0)+entropy(probs1))/2
quartic=S.factor(((p0[u]**4+p0[v]**4+p1[u]**4+p1[v]**4)/2-
                  pm[u]**4-pm[v]**4)/4)
assert gap > num(quartic) > 0
counts['exact_assertions'] += 1

# Direct conditional mutual information: ordinary clique subtraction is strict.
pc = {b:num(z.subs(p0)) for b,z in atoms.items()}
cmi=mp.mpf('0')
for core in itertools.product((0,1),repeat=2):
    table=[[pc[core+(j,k)] for k in (0,1)] for j in (0,1)]
    tot=sum(sum(row) for row in table)
    rows=[sum(row) for row in table]
    cols=[sum(table[j][k] for j in (0,1)) for k in (0,1)]
    cmi += sum(table[j][k]*mp.log(table[j][k]*tot/(rows[j]*cols[k]))
               for j in (0,1) for k in (0,1))
assert cmi > 0
counts['exact_assertions'] += 1

result={**counts,'six_atom_multiplicities':mult,
        'sample_kernel_feasibility_margin':str(1-S.Rational(1,3)-S.Rational(13,25)),
        'midpoint_entropy_gap':str(gap),'proved_quartic_gap':str(quartic),
        'sample_conditional_mutual_information':str(cmi),
        'negative_determinant_ratio':str(bad_ratio),
        'negative_correction_strength_fisher':str(bad_fisher),
        'negative_correction_full_strength_curvature':str(bad_hessian),
        'max_curvature_identity_error':str(maxerr),
        'curvatures':curvature_checks}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
