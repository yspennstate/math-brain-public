# Direct checks of the m=2 claim alpha_2 = (3-sqrt7)/4 under convention (4)-(5):
# (i) at alpha slightly below, the operator a=b=alpha, c=1-alpha has a 2-cycle (non-regular);
# (ii) random search: no QSO with min P > (3-sqrt7)/4 has a fixed point with f'(p) < -1;
# (iii) direct iteration of the example.
import numpy as np
rng=np.random.default_rng(1)
al0=(3-7**0.5)/4
def f_of(a,b,c):
    return np.poly1d([a-2*b+c, 2*b-2*c, c])
def fixed_points(f):
    r=np.roots((f-np.poly1d([1,0])).coeffs)
    return [x.real for x in r if abs(x.imag)<1e-10 and -1e-9<=x.real<=1+1e-9]
def two_cycles(f):
    g=f(f)-np.poly1d([1,0]); h=f-np.poly1d([1,0]); q,_=np.polydiv(g,h)
    return [x.real for x in np.roots(q) if abs(x.imag)<1e-9 and -1e-9<=x.real<=1+1e-9]
for al in [al0-0.01, al0-0.001, al0+0.001, al0+0.01, 0.12, 0.17]:
    f=f_of(al,al,1-al); p=fixed_points(f)[0]
    print(f"alpha={al:.5f} a=b=alpha c=1-alpha: p={p:.5f} f'(p)={f.deriv()(p):+.5f} 2-cycle points={np.round(two_cycles(f),5)}")
# (iii) iterate at alpha = 0.12 (min P = 0.12 > 0.0886) 
al=0.12; f=f_of(al,al,1-al); x=0.3
for _ in range(2000): x=f(x)
orbit=[x]; 
for _ in range(4): x=f(x); orbit.append(x)
print("alpha=0.12 orbit tail:",np.round(orbit,6))
# (ii) random search over all (a,b,c) with min P > al0: worst f'(p)
worst=0; cnt=0
for _ in range(200000):
    a,b,c=rng.uniform(al0,1-al0,3)
    f=f_of(a,b,c)
    for p in fixed_points(f):
        d=f.deriv()(p); worst=min(worst,d); cnt+=len(two_cycles(f))
print("random search (200k) with min P > (3-sqrt7)/4: most negative f'(p) =",worst," two-cycles found:",cnt)
# boundary probe: min P slightly below
worst=0
for _ in range(200000):
    a,b,c=rng.uniform(al0-0.02,1-al0+0.02,3)
    f=f_of(a,b,c); ok=False
    for p in fixed_points(f):
        if f.deriv()(p)<-1: ok=True
    if ok: worst=max(worst,min(a,b,c,1-a,1-b,1-c))
print("random search: largest min P among operators with f'(p)<-1:",worst," target",al0)
