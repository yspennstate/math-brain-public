import math
def h2(x):
    if x<=0 or x>=1: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)
def F(a,b):
    return h2(math.sin(a)**2)+h2(math.sin(a-b)**2)
def U(p, N=20000):
    b=math.asin(math.sqrt(p))
    # fundamental domain alpha in [b/2, b/2+pi/4]; scan
    best=1e9; besta=None
    for k in range(N+1):
        a=b/2+ (math.pi/4)*k/N
        v=F(a,b)
        if v<best: best=v; besta=a
    # refine
    lo=max(b/2,besta-math.pi/(4*N)); hi=min(b/2+math.pi/4,besta+math.pi/(4*N))
    for it in range(100):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if F(m1,b)<F(m2,b): hi=m2
        else: lo=m1
    a=(lo+hi)/2
    return min(best,F(a,b)), a, b
def Delta(p): return h2(p)+math.log2(max(p,1-p))
print("p, tau*=h2-U, Delta/2, ratio tau*/Delta, argmin alpha/beta, (Delta/2-tau)/p, tau/(p log2 1/p)")
for p in [1e-8,1e-6,1e-4,1e-3,0.01,0.03,0.05,0.1,0.15,0.2,0.25,0.28,0.3,0.31,0.32,0.35,0.4,0.45,0.48,0.49,0.499,0.4999]:
    u,a,b=U(p)
    t=h2(p)-u
    D=Delta(p)
    print(f"{p:.6g} {t:.6e} {D/2:.6e} {t/D:.6f} {a/b:.5f} {(D/2-t)/p:.5f} {t/(p*math.log2(1/p)):.5f}")
