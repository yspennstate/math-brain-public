# Independent numeric checks for P0289 (Q1 lane, 2026-09-12)
import math
from mpmath import mp, mpf, quad, cos, exp, tan, pi
mp.dps = 30
# 1. two-arrival interaction integral: arrivals at -(y+d) and -y, unit service.
def V(arr):  # Reich sup formula, arr = list of ages >=0
    ages = sorted(arr)
    best = 0.0
    # sup over u of N(-u,0]-u ; candidates u = age_i + 0 (just past) -> N counts ages <= age_i ... use u -> age_i^+
    for i,a in enumerate(ages):
        best = max(best, (i+1) - a)
    return best
def interaction(y,d):
    return V([y+d,y]) - V([y+d]) - V([y])
for d in [0.0,0.25,0.5,0.9]:
    # integrate over y in [0, 3] numerically (interaction vanishes beyond 2-d)
    n=200000; h=3.0/n
    s=sum(interaction((k+0.5)*h,d) for k in range(n))*h
    print("d=%.2f  int interaction dy = %.6f   expect 1-d = %.6f"%(d,s,1-d))
# 2. J(c) = int_0^1 (1-u) e^{-delta c u} cos(cu) du, delta = tan(pi/1024)
m=1024; delta = tan(pi/m)
J = lambda c: quad(lambda u:(1-u)*exp(-delta*c*u)*cos(c*u),[0,1])
I0 = lambda c: (1-cos(c))/c**2
for c in [2*pi,3*pi,mpf('6.294'),mpf('8.9785')]:
    print("c=%.4f J=%.8f I0=%.8f |J-I0|=%.2e bound dc/6=%.2e"%(c,J(c),I0(c),abs(J(c)-I0(c)),delta*c/6))
print("delta=",delta, " pi/512=",pi/512)
half = (J(3*pi)-J(2*pi))/2
print("half*(J(3pi)-J(2pi)) =",half, " rational lower bound 137/46080 =",mpf(137)/46080)
eps=mpf('1e-4'); rem = 27*eps/(2*(1-3*eps))
print("remainder/eps^2 bound =",rem," 1/700=",mpf(1)/700)
print("margin/eps^2 >=",half-rem," file's 2491/1612800=",mpf(2491)/1612800)
# 3. sign-derivative criterion: dPsi/dc = c^-3 int_0^c (2v-c) R(v) dv with R=(1/2)e^{-delta v}cos v
dPsi = lambda c: quad(lambda v:(2*v-c)*mpf(0.5)*exp(-delta*v)*cos(v),[0,c])/c**3
for c in [1,2,3,pi,2*pi,2.5*pi,3*pi,7,8,9]:
    print("c=%.4f dPsi/dc=%.6e"%(c,dPsi(c)))
# check identity Psi(c) = (1/c^2) int_0^c (c-v)R(v)dv  equals  int_0^1 (1-u) R(cu) du
c=mpf('7.3')
A = quad(lambda v:(c-v)*mpf(0.5)*exp(-delta*v)*cos(v),[0,c])/c**2
B = quad(lambda u:(1-u)*mpf(0.5)*exp(-delta*c*u)*cos(c*u),[0,1])
print("identity check",A,B)
