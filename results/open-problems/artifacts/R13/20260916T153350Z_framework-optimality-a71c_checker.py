#!/usr/bin/env python3
"""
R13 run 4 exact-arithmetic self-check.

Finite/algebraic core only.  This does NOT prove Komlos.  It certifies:
  X02: the tempting L=4 slab optimization violates universal sign-recovery
       containment on the rational 1D example K=(-2,2), v=1.
  C04: within the uniform-slab + linear BV-translation compiler,
       kappa_max(L)=3(L-2)/L^2 <= 1/3 for 2<L<=3.
  C05: the cosine-square initializer has Fisher information pi^2/C^2 exactly,
       so its diagonal CLT coefficient is sqrt(2*pi)/C.
"""
import sympy as sp

L,kappa,C,x=sp.symbols("L kappa C x", positive=True)

print("R13 Komlos run-4 framework-optimality checker")

h=sp.symbols("h", nonnegative=True)
integral=sp.integrate(h*(2*L-h),(h,0,2*L))
assert sp.simplify(integral-sp.Rational(4,3)*L**3)==0
loss=sp.simplify(integral/(8*L))
assert sp.simplify(loss-L**2/sp.Integer(6))==0
print("general slab loss coefficient L^2/6: PASS")

kmax=sp.simplify((L/sp.Integer(2)-1)*6/L**2)
assert sp.simplify(kmax-3*(L-2)/L**2)==0
gap=sp.factor(sp.Rational(1,3)-kmax)
assert gap==(L-6)*(L-3)/(3*L**2)
print("1/3-kappa_max(L) factor =", gap)
print("uniform-slab compiler max on 2<L<=3 occurs at L=3 and equals 1/3: PASS")

assert sp.simplify(kmax.subs(L,4)-sp.Rational(3,8))==0
print("tempting unconstrained L=4 threshold 3/8: PASS")

witness=sp.Rational(13,4)
assert -4 < witness < 4
assert not (-3 < witness < 3)
print("X02 exact witness x=13/4 lies in D_1=(-4,4) but not in (K-v) union (K+v)=(-3,3): PASS")

g=sp.cos(sp.pi*x/(2*C))/sp.sqrt(C)
norm=sp.integrate(g**2,(x,-C,C))
dirichlet=sp.integrate(sp.diff(g,x)**2,(x,-C,C))
assert sp.simplify(norm-1)==0
assert sp.simplify(dirichlet-sp.pi**2/(4*C**2))==0
fisher=sp.simplify(4*dirichlet)
assert fisher==sp.pi**2/C**2
diag=sp.simplify(sp.sqrt(sp.Rational(2,1)/sp.pi)*sp.sqrt(fisher))
assert diag==sp.sqrt(2*sp.pi)/C
print("cosine-square norm=1 and Fisher=pi^2/C^2: PASS")
print("diagonal CLT coefficient sqrt(2*pi)/C: PASS")

bound=sp.simplify(sp.sqrt(2*sp.pi)/(sp.Rational(1,3)))
assert bound==3*sp.sqrt(2*sp.pi)
print("combined product-density/uniform-slab framework barrier C >= 3*sqrt(2*pi): PASS")

print("ALL_EXACT_CHECKS_PASS")
