"""Exact finite checks for X066; no random sampling and no universal sign inference."""
from itertools import product
from pathlib import Path
import json
import sympy as s

R = s.Rational
I = s.I
checks = 0

def check(test, label):
    global checks
    assert bool(test), label
    checks += 1

def eq(a, b, label):
    if isinstance(a, s.MatrixBase):
        check(all(s.simplify(v) == 0 for v in a-b), label)
    else:
        check(s.simplify(a-b) == 0, label)

def atom(K, bits):
    n = K.rows
    eye = s.eye(n)
    C = s.Matrix.hstack(*[(K if bits[j] else eye-K)[:, j] for j in range(n)])
    return s.simplify(C.det(method='domain-ge'))

def law(J, V, M):
    K = s.simplify(J+V*M*V.adjoint())
    return {bits: atom(K, bits) for bits in product((0, 1), repeat=K.rows)}

def effects(J, V):
    bases = [s.zeros(2), s.eye(2), s.diag(1, 0), s.diag(0, 1),
             s.Matrix([[R(1,2), R(1,2)], [R(1,2), R(1,2)]]),
             s.Matrix([[R(1,2), I/2], [-I/2, R(1,2)]])]
    laws = [law(J, V, M) for M in bases]
    out = {}
    for bits in laws[0]:
        alpha, gamma, b1, b2, br, bi = [p[bits] for p in laws]
        z = s.simplify(br-(b1+b2)/2+I*(bi-(b1+b2)/2))
        B = s.Matrix([[b1, z], [s.conjugate(z), b2]])
        out[bits] = (alpha, B, gamma)
        eq(B.det(), alpha*gamma, 'local determinant')
        check(alpha >= 0 and gamma >= 0 and b1 >= 0 and b2 >= 0,
              'effect positivity with determinant')
    eq(sum(a for a,B,g in out.values()), 1, 'sum alpha')
    eq(sum(g for a,B,g in out.values()), 1, 'sum gamma')
    eq(sum((B for a,B,g in out.values()), s.zeros(2)), s.eye(2), 'sum B')
    return out

def from_effect(effect, M):
    alpha, B, gamma = effect
    return s.simplify(alpha*(s.eye(2)-M).det()
                      +s.trace(B*(M-M.det()*s.eye(2)))+gamma*M.det())

def verify_global(E):
    coeff = {}
    for y, (a,B,g) in E.items():
        for z, (aa,BB,gg) in E.items():
            key = tuple(i+j for i,j in zip(y,z))
            coeff[key] = coeff.get(key, 0)+B[0,0]*BB[1,1]-B[0,1]*BB[1,0]-a*gg
    for key, val in coeff.items():
        eq(val, 0, 'global polynomial coefficient '+str(key))
    for y, (a,B,g) in E.items():
        for i, bit in enumerate(y):
            if not bit:
                z = list(y); z[i] = 1
                aa, BB, gg = E[tuple(z)]
                eq(s.trace(B.adjugate()*BB), a*gg+aa*g, 'edge compatibility')
                if a and aa:
                    eq((B/a-BB/aa).det(), 0, 'rank-one odds edge')

def verify_probabilities(J, V, E):
    M = s.Matrix([[R(1,3), (1+2*I)/20], [(1-2*I)/20, R(2,5)]])
    A = s.Matrix([[R(1,11), (2-I)/31], [(2+I)/31, -R(1,13)]])
    eq(A, A.adjoint(), 'Hermitian complex direction')
    vals = {t:law(J,V,M+t*A) for t in (-2,-1,0,1,2)}
    for y in E:
        a,B,g = E[y]
        for t in vals:
            eq(vals[t][y], from_effect(E[y], M+t*A), 'direct atom vs effect')
        c = a+g-s.trace(B)
        eq(vals[1][y]-2*vals[0][y]+vals[-1][y], 2*A.det()*c, 'exact acceleration')
        eq(vals[2][y]-3*vals[1][y]+3*vals[0][y]-vals[-1][y], 0, 'degree at most two')

def reflection(v):
    v = s.Matrix(v)
    return s.eye(len(v))-2*v*v.T/(v.T*v)[0]

# Dense, genuinely complex coherent environment; all four modes are present.
Q = reflection([1,2,3,4])*s.diag(1,I,(3+4*I)/5,1)*reflection([1,1,1,1])
eq(Q.adjoint()*Q, s.eye(4), 'dense unitary')
W, V = Q[:,:2], Q[:,2:]
J = s.simplify(W*s.diag(R(1,3),R(2,5))*W.adjoint())
eq(J*V,s.zeros(4,2),'environment annihilates active plane')
E = effects(J,V)
verify_global(E)
verify_probabilities(J,V,E)
check(any(s.simplify((B*C-C*B).norm()) != 0
          for _,B,_ in E.values() for _,C,_ in E.values()), 'noncommuting dense effects')
check(any(s.im(B[0,1]) != 0 for _,B,_ in E.values()), 'complex dense effects')
singular_effects = sum(a == 0 for a,B,g in E.values())
check(singular_effects > 0, 'singular C_y covered')

# Two disjoint coherent reservoirs: exact commuting classification instance.
U = s.Matrix([[R(3,5),0], [R(4,5),0], [0,R(5,13)], [0,R(12,13)]])
Wc = s.Matrix([[-R(4,5),0], [R(3,5),0], [0,-R(12,13)], [0,R(5,13)]])
Jc = Wc*s.diag(R(1,3),R(2,5))*Wc.T
Ec = effects(Jc,U)
verify_global(Ec)
verify_probabilities(Jc,U,Ec)
check(all(B[0,1] == 0 for _,B,_ in Ec.values()), 'all effects diagonal')

def local_channel(lam, u):
    u1,u2 = u
    return [
        {(0,0):1-lam, (1,0):lam*u2*u2, (0,1):lam*u1*u1, (1,1):0},
        {(0,0):0, (1,0):(1-lam)*u1*u1, (0,1):(1-lam)*u2*u2, (1,1):lam},
    ]
C1 = local_channel(R(1,3),(R(3,5),R(4,5)))
C2 = local_channel(R(2,5),(R(5,13),R(12,13)))
for y,(a,B,g) in Ec.items():
    z1,z2 = y[:2],y[2:]
    eq(a,C1[0][z1]*C2[0][z2],'alpha product')
    eq(B[0,0],C1[1][z1]*C2[0][z2],'b1 product')
    eq(B[1,1],C1[0][z1]*C2[1][z2],'b2 product')
    eq(g,C1[1][z1]*C2[1][z2],'gamma product')

# The bad local-only POVM and a rational strict lower bound for its curvature.
vac=(R(1,64),s.zeros(2),s.Integer(0))
bad=[vac]*64+[(0,s.diag(1,0),0),(0,s.diag(0,1),0),(0,s.zeros(2),1)]
for a,B,g in bad:
    eq(B.det(),a*g,'cloned effect determinant')
eq(sum(a for a,B,g in bad),1,'cloned alpha normalization')
eq(sum(g for a,B,g in bad),1,'cloned gamma normalization')
eq(sum((B for a,B,g in bad),s.zeros(2)),s.eye(2),'cloned B normalization')
log2_lower=2*(R(1,3)+R(1,81))
check(-8+12*log2_lower > 0,'positive curvature by exact logarithm lower bound')

tau1=sum(abs(C1[1][y]-C1[0][y]) for y in C1[0])/2
tau2=sum(abs(C2[1][y]-C2[0][y]) for y in C2[0])/2
out={
    'exact_assertions':checks,
    'dense_zero_alpha_effects':int(singular_effects),
    'dense_outcomes':len(E),
    'commuting_outcomes':len(Ec),
    'channel_total_variations':[str(tau1),str(tau2)],
    'definite_curvature_coefficient':str(8*tau1*tau2),
    'abstract_bad_curvature_lower_bound':str(-8+12*log2_lower),
    'abstract_bad_curvature_decimal':str(s.N(-8+12*s.log(2),30)),
}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
