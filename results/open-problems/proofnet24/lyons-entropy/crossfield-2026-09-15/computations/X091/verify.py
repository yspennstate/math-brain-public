#!/usr/bin/env python3
"""Exact checks for X091's independent-phase square bouquet theorem.

No numerical observation is used in the proof. Run from the campaign root.
"""
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

mp.mp.dps = 70
R = sp.Rational
checks = 0


def eq(a, b):
    global checks
    assert sp.cancel(a - b) == 0, sp.factor(a - b)
    checks += 1


def forms(a, b):
    c, d, e = a*a+b*b, (a-b)**2, (a+b)**2
    return {
        (1, 1): ((1-c)/4, sp.diag(2-d, 2-e)/(2*(1-c))),
        (-1, -1): ((1+c)/4, sp.diag(2+d, 2+e)/(2*(1+c))),
        (1, -1): ((1-a*a+b*b)/4,
                  sp.diag(d, e)/(2*(1-a*a+b*b))),
        (-1, 1): ((1+a*a-b*b)/4,
                  sp.diag(d, e)/(2*(1+a*a-b*b))),
    }


a, b, x, y = sp.symbols('a b x y', real=True)
v = sp.Matrix([x, y])
z = x + sp.I*y
row = sp.Matrix([[z, 0, sp.conjugate(z)]])
C = sp.Matrix([[0,a,0],[a,0,b],[0,b,0]])
F = forms(a,b)
eq(sum(w for w,M in F.values()), 1)
for sl,sv,sr in product((-1,1), repeat=3):
    Q = sp.diag(sl,sv,sr)+C
    typ = (sl*sv,sr*sv)
    w, M = F[typ]
    eq(sl*sv*sr*Q.det()/8, w/2)
    sig = sv*(-1 if typ == (-1,-1) else 1)
    actual = (row*Q.adjugate()*sp.conjugate(row.T))[0]/(2*Q.det())
    expected = sig*(v.T*M*v)[0]
    eq(actual, expected)

# Closed quartic formula for equal reservoir legs.
Qequal = 2*sum(w*(v.T*M*v)[0]**2 for w,M in forms(a,a).values())
eq(Qequal, x**4/(1-4*a**4)+2*x*x*y*y+(1+4*a**4)*y**4)


def kernel(legs, coords):
    n = 1+3*len(legs)
    J = sp.zeros(n)
    for j, ((a,b),(x,y)) in enumerate(zip(legs,coords)):
        l,m,r = 1+3*j,2+3*j,3+3*j
        z = x+sp.I*y
        for u,vv,val in [(l,m,a),(m,r,b),(0,l,z),(0,r,sp.conjugate(z))]:
            J[u,vv],J[vv,u] = val,sp.conjugate(val)
    return (sp.eye(n)+J)/2


def atom(K, signs):
    Q = K-sp.diag(*[(1-s)//2 for s in signs])
    return sp.factor(sp.prod(signs)*Q.det(method='domain-ge'))


def conditional_data(legs, coords, tangent=None):
    """(exterior probability, Z, Z', Z'', Rs, Bs, sigma, types)."""
    m = len(legs)
    for types in product(*[list(forms(*ab)) for ab in legs]):
        weights, Rs, Ls, Bs = [], [], [], []
        for j, typ in enumerate(types):
            w, M = forms(*legs[j])[typ]
            vv = sp.Matrix(coords[j])
            uu = sp.Matrix(tangent[j] if tangent else (0,0))
            weights.append(w)
            Rs.append((vv.T*M*vv)[0])
            Ls.append(2*(vv.T*M*uu)[0])
            Bs.append((uu.T*M*uu)[0])
        for sigma in product((-1,1), repeat=m):
            z0 = sum(s*r for s,r in zip(sigma,Rs))
            z1 = sum(s*r for s,r in zip(sigma,Ls))
            z2 = 2*sum(s*r for s,r in zip(sigma,Bs))
            yield sp.prod(weights)/2**m,z0,z1,z2,Rs,Bs,sigma,types


def exterior_signs(sigma, types):
    out=[]
    for sig,typ in zip(sigma,types):
        sv=sig*(-1 if typ==(-1,-1) else 1)
        out += [typ[0]*sv,sv,typ[1]*sv]
    return out


def quartic(legs,coords):
    return sp.factor(2*sum(w*(sp.Matrix(v).T*M*sp.Matrix(v))[0]**2
                          for ab,v in zip(legs,coords)
                          for w,M in forms(*ab).values()))


def margin(legs,coords):
    return sp.factor(1-2*sum((sp.Matrix(v).T*forms(*ab)[(1,1)][1]
                             *sp.Matrix(v))[0] for ab,v in zip(legs,coords)))


legs=[(R(3,5),R(3,5)), (R(1,2),R(1,2))]
start=[(R(1,5),R(1,4)),(R(1,4),R(1,10))]
end=[(R(1,10),R(3,10)),(R(3,10),R(1,5))]
tangent=[tuple(q-p for p,q in zip(v,w)) for v,w in zip(start,end)]
mid=[tuple((p+q)/2 for p,q in zip(v,w)) for v,w in zip(start,end)]
K=kernel(legs,start)
Kt=kernel(legs,[[p+q for p,q in zip(v,u)] for v,u in zip(start,tangent)])
Km=kernel(legs,[[p-q for p,q in zip(v,u)] for v,u in zip(start,tangent)])
assert margin(legs,start)>0 and margin(legs,end)>0
for J in [K,sp.eye(7)-K]:
    for n in range(1,8):
        assert J[:n,:n].det(method='domain-ge')>0
        checks += 1

# All 128 atom second jets from signed full 7x7 determinants.
atoms=[]
for weight,z0,z1,z2,Rs,Bs,sigma,types in conditional_data(legs,start,tangent):
    for s0 in (-1,1):
        signs=[s0]+exterior_signs(sigma,types)
        p0=weight*(R(1,2)-s0*z0)
        p1=-s0*weight*z1
        p2=-s0*weight*z2
        eq(atom(K,signs),p0)
        eq(atom(Kt,signs),p0+p1+p2/2)
        eq(atom(Km,signs),p0-p1+p2/2)
        assert p0>0
        atoms.append((p0,p1,p2))
eq(sum(p for p,_,_ in atoms),1)
eq(sum(p for _,p,_ in atoms),0)
eq(sum(p for _,_,p in atoms),0)


def mpr(q):
    return mp.mpf(str(sp.N(q,75)))


def phi1(u):
    return mp.log((mp.mpf('.5')+u)/(mp.mpf('.5')-u))


def curvature_check(legs,v,u):
    info=mp.mpf(0)
    acc=mp.mpf(0)
    paired=mp.mpf(0)
    rem=mp.mpf(0)
    for w,z0,z1,z2,Rs,Bs,sigma,types in conditional_data(legs,v,u):
        ww,zz,zz1,zz2=map(mpr,(w,z0,z1,z2))
        info += ww*zz1**2/(mp.mpf('.25')-zz**2)
        acc += ww*zz2*phi1(zz)
        rem += ww*(1/(mp.mpf('.25')-zz**2)-4)*zz1**2
        for j,(rr,bb,sg) in enumerate(zip(Rs,Bs,sigma)):
            Rj,Bj,Sj=map(mpr,(rr,bb,z0-sg*rr))
            delta=phi1(Sj+Rj)-phi1(Sj-Rj)
            # Full-sign averaging is same as averaging the other signs.
            paired += ww*Bj*delta
            rem += ww*Bj*(delta-8*Rj)
    tt=sp.symbols('t',real=True)
    qt=quartic(legs,[[p+tt*q for p,q in zip(vv,uu)] for vv,uu in zip(v,u)])
    q2=mpr(sp.diff(qt,tt,2).subs(tt,0))
    assert abs(acc-paired)<mp.mpf('1e-65')
    assert abs(info+acc-q2-rem)<mp.mpf('1e-65')
    assert info>=0 and paired>=0 and rem>=0
    return dict(Fisher=mp.nstr(info,35), logarithmic_acceleration=mp.nstr(acc,35),
                minus_H_second=mp.nstr(info+acc,35),
                quartic_second=mp.nstr(q2,35),
                positive_remainder=mp.nstr(rem,35))


curve=curvature_check(legs,start,tangent)
actual_fisher=sum(mpr(p1)**2/mpr(p0) for p0,p1,p2 in atoms)
actual_acc=sum(mpr(p2)*mp.log(mpr(p0)) for p0,p1,p2 in atoms)
assert abs(actual_fisher-mp.mpf(curve['Fisher']))<mp.mpf('1e-32')
assert abs(actual_acc-mp.mpf(curve['logarithmic_acceleration']))<mp.mpf('1e-32')

# Independent unequal-path-leg witness checks all conditional formulas and
# a full phase-and-radius motion, without the equal-leg simplification.
unequal_legs=[(R(3,5),R(1,2)),(R(1,3),R(2,3))]
unequal_v=[(R(1,5),R(1,4)),(R(1,5),R(3,20))]
unequal_u=[(R(-1,7),R(1,9)),(R(1,8),R(-1,10))]
assert margin(unequal_legs,unequal_v)>0
unequal_curve=curvature_check(unequal_legs,unequal_v,unequal_u)


def entropy_at(coords):
    total=mp.mpf(0)
    for w,z0,*_ in conditional_data(legs,coords):
        for s in (-1,1):
            p=mpr(w*(R(1,2)-s*z0))
            total -= p*mp.log(p)
    return total


jensen=entropy_at(mid)-(entropy_at(start)+entropy_at(end))/2
quartic_gap=sp.factor((quartic(legs,start)+quartic(legs,end))/2-quartic(legs,mid))
assert jensen>mpr(quartic_gap)>0

# The same magnitudes with all phases removed violate contraction, exactly.
unsigned_margin=sp.factor(1-2*sum((xx*xx+yy*yy)/(1-2*aa*aa)
                              for (aa,bb),(xx,yy) in zip(legs,start)))
assert unsigned_margin<0

# Exclude the old positive-real simple-cycle odds certificate at this base.
L=K*(sp.eye(7)-K).inv()
violations=[]
for i,j,k in combinations(range(7),3):
    v=sp.factor(sp.re(-L[i,j]*L[j,k]*L[k,i]))
    if v<0:
        violations.append({'triangle':[i,j,k],'Re_negative_odds_product':str(v)})
assert violations

result={
    'status':'PASS', 'exact_assertions':checks,
    'all_full_atom_second_jets_checked':len(atoms),
    'reservoir_normalized_legs':[[str(x) for x in p] for p in legs],
    'start_xy':[[str(x) for x in p] for p in start],
    'end_xy':[[str(x) for x in p] for p in end],
    'start_schur_margin':str(margin(legs,start)),
    'end_schur_margin':str(margin(legs,end)),
    'unsigned_start_schur_margin':str(unsigned_margin),
    'midpoint_entropy_gap':mp.nstr(jensen,40),
    'exact_quartic_gap':str(quartic_gap),
    'curvature':curve,
    'unequal_leg_curvature':unequal_curve,
    'first_C071_violation':violations[0],
}
out=Path(__file__).with_name('results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
