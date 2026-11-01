import numpy as np
rng=np.random.default_rng(23)
def N_of(a,b,c):
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    M=np.array([[0.,1,0],[1,0,0],[0,0,-2]])
    return G-absL*M, absL, p
print("N = G - |L|M must be PSD.  Which minor is tight?")
m1=1e9;m2=1e9;m3=1e9; w1=w2=w3=None; n=0; bad=0
while n<200000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    t=c*c
    if t>=min(a*b,(1-a)*(1-b))-1e-9: continue
    N,absL,p=N_of(a,b,c)
    if p.min()<=1e-9: continue
    n+=1
    d1=N[0,0]; d2=N[0,0]*N[1,1]-N[0,1]**2; d3=np.linalg.det(N)
    if d1<m1: m1=d1; w1=(a,b,c)
    if d2<m2: m2=d2; w2=(a,b,c)
    if d3<m3: m3=d3; w3=(a,b,c)
    if min(np.linalg.eigvalsh(N))<-1e-9: bad+=1
print(f"  n={n}  points where N is NOT PSD: {bad}")
print(f"  min leading 1x1 minor: {m1:+.6e} at {tuple(round(v,3) for v in w1)}")
print(f"  min leading 2x2 minor: {m2:+.6e} at {tuple(round(v,3) for v in w2)}")
print(f"  min determinant      : {m3:+.6e} at {tuple(round(v,3) for v in w3)}")
print()
print("  det N at c -> 0 (the equality locus): a=b=0.5")
for c in [0.3,0.1,0.03,0.01,0.003,0.001]:
    N,absL,p=N_of(0.5,0.5,c)
    print(f"    c={c:<7} det={np.linalg.det(N):+.6e}  |L|={absL:.3e}  min eig={min(np.linalg.eigvalsh(N)):+.3e}")
