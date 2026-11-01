import math
from scipy.optimize import brentq
import numpy as np
a=math.log(10.0)
def K(s,R): return 1.0/(2.0*(math.cosh(s)-math.cos(R)))
def F(u,R): return 0.5*(K(u-a,R)+K(u+a,R))
def Rof(t):  # solve R/sin R = t/10 on (0,pi)
    f=lambda R: R/math.sin(R)-t/10.0
    return brentq(f,1e-9,math.pi-1e-12,xtol=1e-15,rtol=1e-15)
print(f"nu = (delta_{{1/10}} + delta_{{10}})/2 ; Lemma 4.1(3): log-unimodal <=> (sin R/R)*Int = 1/t has <=2 roots")
print(f"{'t':>10} {'R':>9} {'RHS=R/(t sinR)':>15} {'F(0)':>9} {'F(a)':>9} {'#roots of F=RHS':>16}")
for t in [5*math.pi+1e-6, 16, 20, 50, 200, 1000, 100000]:
    R=Rof(t); rhs=R/(t*math.sin(R))
    us=np.linspace(-12,12,240001); vals=np.array([F(u,R) for u in us])-rhs
    roots=int(np.sum(np.sign(vals[:-1])*np.sign(vals[1:])<0))
    print(f"{t:>10.4f} {R:>9.6f} {rhs:>15.10f} {F(0,R):>9.6f} {F(a,R):>9.6f} {roots:>16}")
# the two structural bounds, over the whole admissible range R in [pi/2, pi)
Rs=np.linspace(math.pi/2, math.pi-1e-9, 20001)
f0=np.array([F(0,R) for R in Rs]); fa=np.array([F(a,R) for R in Rs])
print(f"\nover all R in [pi/2,pi):  max F(0) = {f0.max():.6f}  (must be < 0.1)   min F(a) = {fa.min():.6f}  (must be > 0.1)")
print(f"cosh(log 10) = {math.cosh(a):.4f}  -> F(0) <= 1/(2*(cosh a - 0)) = {1/(2*math.cosh(a)):.6f} = 10/101")
