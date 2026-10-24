from itertools import combinations
from math import sqrt, pi
import sympy as sp

A = sp.Matrix([
    [0,4,4,4,4,4],
    [4,3,2,3,4,5],
    [4,2,6,6,8,10],
    [4,3,6,11,12,15],
    [4,4,8,12,18,20],
    [4,5,10,15,20,27],
])

u = sp.ones(5,1)
R = A[1:,1:]
w = R.inv()*u
s = (u.T*R.inv()*u)[0]
wnorm = (w.T*w)[0]
rq = sp.factor(-16*s/(1+16*wnorm))
assert R.eigenvals() == {sp.Integer(57):1, sp.Integer(2):4}
assert w == sp.Matrix([sp.Rational(7,19),sp.Rational(9,38),sp.Rational(2,19),-sp.Rational(1,38),-sp.Rational(3,19)])
assert s == sp.Rational(10,19)
assert wnorm == sp.Rational(165,722)
assert rq == -sp.Rational(3040,1681)
assert rq < -1

# Every ordered nonempty disjoint physical cut has rank <= 2.
rank_counts = {}
cuts = 0
for r in range(1,7):
    for I in combinations(range(6),r):
        rem = [j for j in range(6) if j not in I]
        for q in range(1,len(rem)+1):
            for J in combinations(rem,q):
                rk = A.extract(I,J).rank()
                rank_counts[rk] = rank_counts.get(rk,0)+1
                cuts += 1
assert cuts == 602
assert rank_counts == {1:392, 2:210}

# Augmented pair volumes z_i=(4,i), i=1,...,5.
z = [(4,i) for i in range(1,6)]
c = {}
for i,j in combinations(range(5),2):
    d = z[i][0]*z[j][1]-z[j][0]*z[i][1]
    c[(i,j)] = d*d
W = sum(c.values())
J1 = sum(cp*cq for P,cp in c.items() for Q,cq in c.items() if set(P).isdisjoint(Q))
assert W == 800
assert J1 == 158720

Z = sp.Matrix(z)
G = Z.T*Z
assert G == sp.Matrix([[80,60],[60,55]])
assert G.det() == 800
lev = []
for i in range(5):
    row = sp.Matrix([[4,i+1]])
    lev.append(sp.factor((row*G.inv()*row.T)[0]))
assert lev == [sp.Rational(3,5),sp.Rational(3,10),sp.Rational(1,5),sp.Rational(3,10),sp.Rational(3,5)]

# Exact KKT optimizer under all pair-row marginal caps <=1/2.
t = sp.sqrt(6)/4
Zbase = sp.simplify(6+28*t+16*t*t)
assert Zbase == 12+7*sp.sqrt(6)
assert sp.simplify((14*t+16*t*t)/Zbase) == sp.Rational(1,2)
alpha2 = sp.simplify((5+10*t)/Zbase)
alpha3 = sp.simplify((2+8*t)/Zbase)
assert alpha2 < sp.Rational(1,2) and alpha3 < sp.Rational(1,2)
Gopt = sp.simplify(16*Zbase/t)
assert Gopt == 448+128*sp.sqrt(6)

# Exact localized J2 packet enumeration.
triples = list(combinations(range(6),3))
J2 = {}
for H in combinations(range(6),2):
    total = 0
    for I in triples:
        for J in triples:
            if set(I).intersection(J) == set(H):
                d = A.extract(I,J).det()
                total += d*d
    J2[H] = sp.simplify(total)
best_H,max_J2 = max(J2.items(), key=lambda kv:int(kv[1]))
assert best_H == (4,5)
assert max_J2 == 262304

C0 = 3*2**(4/3)
new_opt = C0*float(Gopt)**(-1/3)
new_J = C0*J1**(-1/6)
pinned_A = 3*sqrt(pi)
partner = 88.25355476673130*float(max_J2)**(-1/6)

# Pure localized-J1 family m=144.
J1_pure = sp.Rational(71,72)**2
J2_pure = sp.Rational(71,72**3)
P3_pure = sp.Rational(1,72**2)
assert J1_pure > sp.Rational(1,144)
assert J2_pure < sp.Rational(1,144)
assert P3_pure < sp.Rational(1,4)
assert sp.Rational(1,144) < sp.Rational(1,64)

print('QFORM_B04_R22_WEIGHTED_J1_CHECK_PASS')
print('rayleigh=', rq, float(rq))
print('cut_rank_counts=', rank_counts)
print('W=', W, 'J1=', J1)
print('natural_leverage=', lev)
print('t=', t, 'Gopt=', Gopt, float(Gopt))
print('remaining_marginals=', alpha2, float(alpha2), alpha3, float(alpha3))
print('new_bound_opt=', new_opt)
print('new_bound_Jonly=', new_J)
print('pinned_Theorem_A=', pinned_A)
print('max_J2=', best_H, max_J2, 'partner_r53=', partner)
print('pure_J1=', J1_pure, float(J1_pure))
print('pure_J2star=', J2_pure, float(J2_pure))
print('pure_P3=', P3_pure, float(P3_pure))
