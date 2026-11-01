import numpy as np
for al in [0.08,0.10,0.12,0.15,0.17]:
    a=b=al; c=1-al
    A=a-2*b+c; B=2*b-2*c
    r=[x.real for x in np.roots([A,B-1,c]) if abs(x.imag)<1e-12 and 0<=x.real<=1]; p=r[0]
    x=0.3
    for _ in range(4000): x=a*x*x+2*b*x*(1-x)+c*(1-x)**2
    x2=a*x*x+2*b*x*(1-x)+c*(1-x)**2
    print(f"alpha={al}: a=b={al}, c={c:.2f}, fixed point p={p:.5f}, f'(p)={2*A*p+B:+.4f}, orbit tail {x:.5f} -> {x2:.5f}")
