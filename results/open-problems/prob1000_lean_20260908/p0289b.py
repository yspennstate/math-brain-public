import numpy as np, math
from scipy.integrate import quad
m=1024; theta=2*math.pi/m; delta=math.tan(theta/2)
def J(c):
    v,_=quad(lambda u:(1-u)*math.exp(-delta*c*u)*math.cos(c*u),0,1,limit=300)
    return v
cs=np.linspace(0.01,30,6000); Js=np.array([J(c) for c in cs])
# largest upward excursion: max over i<j of J(j)-J(i)
runmin=np.minimum.accumulate(Js)
gains=Js-runmin
k=int(np.argmax(gains)); dJ=gains[k]
i=int(np.argmin(Js[:k+1]))
print(f"Largest upward excursion of J:  J({cs[i]:.4f}) = {Js[i]:.6f}  ->  J({cs[k]:.4f}) = {Js[k]:.6f}")
print(f"  Delta J = +{dJ:.6f}   (c INCREASES, i.e. FASTER modulation, and J rises)")
print()
print("Condition for this to survive the remainder:  |dJ| > 27 eps/(1-3 eps)")
for eps in [1e-3,1e-4,3e-5,1e-5,1e-6]:
    need=27*eps/(1-3*eps)
    ok = dJ>need
    print(f"  eps={eps:<9} need > {need:.8f}   have {dJ:.8f}   {'SUFFICES' if ok else 'no'}")
eps=1e-5
need=27*eps/(1-3*eps)
print()
print(f"Take eps = {eps}.  Then rho = eps*M = {3*eps} << 1, the expansion is valid, and")
print(f"  w(c2) - w(c1) >= (eps^2/2)*dJ - 27 eps^3/(2(1-3eps)) = {(eps**2/2)*dJ - 27*eps**3/(2*(1-3*eps)):.6e} > 0")
print(f"  with c1={cs[i]:.4f} < c2={cs[k]:.4f}.  Faster modulation gives STRICTLY larger mean stationary workload.")
