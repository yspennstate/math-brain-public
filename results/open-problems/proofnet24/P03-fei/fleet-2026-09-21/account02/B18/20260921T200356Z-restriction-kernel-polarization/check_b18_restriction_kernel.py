#!/usr/bin/env python3
import math
import numpy as np

LN2 = math.log(2.0)

def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -(t*math.log(t)+(1.0-t)*math.log(1.0-t))/LN2

def S(x,y):
    q=x*x+y*y
    if q == 0.0: return 0.0
    return q*h2(y*y/q)

def P(x,y):
    q=x*x+y*y
    if q == 0.0: return 0.0
    t=y*y/q
    return q*(1.0-h2(0.5+math.sqrt(max(0.0,t*(1.0-t)))))

def G(x,y): return S(x,y)+P(x,y)
def M(x,y): return min(x*x,y*y)

def F(x):
    return 0.0 if x == 0.0 else x*x*math.log(abs(x))

def K4(v,w):
    a,b=v; c,d=w
    x=a-b; u=a+b; y=c-d; z=c+d
    return (F(x-y)+F(x+y)-F(x-z)-F(x+z)
            -F(u-y)-F(u+y)+F(u-z)+F(u+z))/16.0

max_diag=0.0
for a in np.linspace(-1.0,1.0,21):
    for b in np.linspace(-1.0,1.0,21):
        if a == 0.0 and b == 0.0:
            continue
        max_diag=max(max_diag,abs(K4((a,b),(a,b))-LN2*G(a,b)/4.0))

xs=np.exp(np.linspace(-8.0,0.0,14))
mins={}
for name,kernel in [
    ("S",S),
    ("P",P),
    ("G",G),
    ("phase_dom",lambda x,y:(2.0/LN2)*M(x,y)-P(x,y)),
]:
    A=np.array([[kernel(float(x),float(y)) for y in xs] for x in xs])
    mins[name]=float(np.linalg.eigvalsh(A)[0])

rng=np.random.default_rng(123)
max_pol=0.0
tests=0
for m in (3,5,8):
    for _ in range(100):
        alpha=rng.normal(size=m)
        alpha-=alpha.mean()
        ap=rng.uniform(-0.5,0.5,size=m)
        am=rng.uniform(-0.5,0.5,size=m)
        U=ap+am
        V=ap-am
        lhs=sum(alpha[i]*alpha[j]*K4((ap[i],am[i]),(ap[j],am[j]))
                for i in range(m) for j in range(m))
        rhs=(LN2/16.0)*sum(
            alpha[i]*alpha[j]*(G(V[i],V[j])-G(V[i],U[j])
                               -G(U[i],V[j])+G(U[i],U[j]))
            for i in range(m) for j in range(m))
        max_pol=max(max_pol,abs(lhs-rhs))
        tests+=1

print("PASS")
print(f"diag_grid_max_abs_error={max_diag:.17g}")
print(f"polarization_tests={tests}")
print(f"polarization_max_abs_error={max_pol:.17g}")
for name in ("S","P","G","phase_dom"):
    print(f"{name}_log_grid_min_eigenvalue={mins[name]:.17g}")
