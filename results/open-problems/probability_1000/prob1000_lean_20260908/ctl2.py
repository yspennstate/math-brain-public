import math, numpy as np
US=np.linspace(-30,30,60001); R_GRID=np.linspace(1e-3, math.pi-1e-3, 300)
def maxroots(nu,t):
    r=np.exp(US); best=0
    for R in R_GRID:
        Th=np.zeros_like(r); c=math.cos(R)
        for (x,w) in nu: Th += w*(r*x)/(1.0+r*r*x*x-2.0*r*x*c)
        Th *= math.sin(R)/R
        v=Th-1.0/t
        n=int(np.sum(np.sign(v[:-1])*np.sign(v[1:])<0))
        best=max(best,n)
    return best
print("POSITIVE CONTROL - Theorem 4.4 (PROVED): cond holds and t>=D  =>  log-unimodal  =>  at most 2 roots")
for (al,be) in [(1.0,1.1),(1.0,1.2),(1.0,1.3)]:
    lhs=be**4-3*al**4; rhs=2*al**3*be
    D=2*be**2*(al+be)**2*math.pi/math.sqrt(4*al**6*be**2-(3*al**4-be**4)**2)
    nu=[(al,0.5),(be,0.5)]
    print(f"  a={al} b={be}: {lhs:.3f}<{rhs:.3f}={lhs<rhs}  D={D:.2f} | max roots t=1.01D: {maxroots(nu,1.01*D)}  t=10D: {maxroots(nu,10*D)}")
print("\nNEGATIVE CONTROL - same code, same nu shape, t BELOW the theorem's D (log-unimodality not guaranteed):")
nu=[(1.0,0.5),(1.3,0.5)]
D=2*1.3**2*(2.3)**2*math.pi/math.sqrt(4*1.3**2-(3-1.3**4)**2)
for t in [0.2*D,0.5*D]: print(f"  a=1 b=1.3 t={t:.2f} (<D={D:.2f}): max roots {maxroots(nu,t)}")
print("\nTHE CANDIDATE - nu=(delta_0.1+delta_10)/2 on [1/10,10], Thm 4.4 hypothesis fails:")
nu=[(0.1,0.5),(10.0,0.5)]
for t in [5*math.pi+0.01, 20, 100, 1000, 10**5, 10**7]:
    print(f"  t={t:>11.2f}: max roots {maxroots(nu,t)}   (>2 => NOT log-unimodal)")
