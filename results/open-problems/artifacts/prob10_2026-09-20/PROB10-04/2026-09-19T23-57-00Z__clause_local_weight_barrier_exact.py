#!/usr/bin/env python3
import sympy as sp

q,u,v,w,t = sp.symbols("q u v w t", positive=True, real=True)

states = [
    ((1,1), q/2),
    ((0,0), q/2),
    ((1,0), (1-q)/2),
    ((0,1), (1-q)/2),
]

def wt(k):
    return {0:sp.Integer(0),1:u,2:v,3:w}[k]

g = sp.Integer(0)
for (a1,p1) in states:
    for (a2,p2) in states:
        for (a3,p3) in states:
            ns = a1[0]+a2[0]+a3[0]
            nt = a1[1]+a2[1]+a3[1]
            g += p1*p2*p3*wt(ns)*wt(nt)
g = sp.expand(g)

A = (3*u+3*v+w)/8
g_half = sp.factor(g.subs(q, sp.Rational(1,2)))
dg_half = sp.factor(sp.diff(g,q).subs(q, sp.Rational(1,2)))
g_one = sp.factor(g.subs(q, 1))

assert sp.simplify(g_half - A**2) == 0
assert sp.simplify(dg_half - 3*(u-v-w)**2/32) == 0
assert sp.simplify(g_one - (3*u**2+3*v**2+w**2)/8) == 0

# Stationarity requires u=v+w.  Write t=v/w and scale w=1.
R1 = sp.factor((g_one/A**2).subs({u:v+w, v:t*w}))
R1 = sp.factor(sp.simplify(R1))
target = 4*(3*t**2+3*t+2)/(3*t+2)**2
assert sp.simplify(R1-target) == 0

dR = sp.factor(sp.diff(R1,t))
assert sp.simplify(dR - 12*(t-2)/(3*t+2)**3) == 0
Rmin = sp.simplify(R1.subs(t,2))
assert Rmin == sp.Rational(5,4)

alpha_barrier = sp.log(2)/sp.log(sp.Rational(5,4))
print("g(1/2)-A^2 =", sp.factor(g_half-A**2))
print("g'(1/2) =", dg_half)
print("stationarity iff u=v+w (positive weights)")
print("g(1) =", g_one)
print("R1(t) =", R1)
print("R1'(t) =", dR)
print("R1 minimum at t=2 =", Rmin)
print("alpha_diagonal_max = log(2)/log(5/4) =", sp.N(alpha_barrier, 18))
print("compare 3.52: barrier < 3.52 =", bool(sp.N(alpha_barrier,50) < sp.Rational(352,100)))
print("ALL_EXACT_CHECKS_PASS = True")
