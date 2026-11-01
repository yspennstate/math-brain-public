import numpy as np, math
from scipy.integrate import quad
m=1024; theta=2*math.pi/m; delta=math.tan(theta/2)
print(f"m={m}, delta = tan(pi/m) = {delta:.8f}")
def J(c):
    f=lambda u: (1-u)*math.exp(-delta*c*u)*math.cos(c*u)
    v,_=quad(f,0,1,limit=200)
    return v
cs=np.linspace(0.01,40,4000)
Js=np.array([J(c) for c in cs])
print("\nJ(c) = int_0^1 (1-u) e^{-delta c u} cos(cu) du  -- is it MONOTONE in c?")
d=np.diff(Js)
sign_changes=int(np.sum(np.sign(d[:-1])*np.sign(d[1:])<0))
print(f"  sign changes of dJ/dc over c in [0.01,40]: {sign_changes}  -> non-monotone" if sign_changes>0 else "  monotone")
imax=int(np.argmax(Js)); imin=int(np.argmin(Js))
print(f"  J max {Js[imax]:.6f} at c={cs[imax]:.3f};  J min {Js[imin]:.6f} at c={cs[imin]:.3f}")
# find an explicit increasing pair c1<c2 with J(c2) > J(c1) AFTER a decrease (i.e. a genuine rise)
i0=imin
later=[(cs[j],Js[j]) for j in range(i0+1,len(cs))]
best=max(later,key=lambda t:t[1])
dJ=best[1]-Js[i0]
print(f"\n  Explicit rise: J({cs[i0]:.3f}) = {Js[i0]:.6f}  ->  J({best[0]:.3f}) = {best[1]:.6f}   Delta J = +{dJ:.6f}")
print(f"  faster modulation (larger c) gives a LARGER J, hence larger mean workload, if the remainder is dominated.")
print()
print("  Remainder bound: 0 <= R_c <= 27 eps^3/(2(1-3eps)).  The eps^2 term moves by (eps^2/2)|dJ|.")
print("  Need (eps^2/2)|dJ| > 27 eps^3/(2(1-3eps))   <=>   |dJ| > 27 eps/(1-3eps).")
for eps in [1e-2,1e-3,1e-4]:
    need=27*eps/(1-3*eps)
    print(f"    eps={eps:<8} need |dJ| > {need:.6f}   actual |dJ| = {dJ:.6f}   -> {'SUFFICES' if dJ>need else 'not enough'}")
