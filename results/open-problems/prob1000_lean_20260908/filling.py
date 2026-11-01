import numpy as np
# The lemma: theta ergodic measure-preserving on (E,P); Q = f P with f>=0, int f dP = 1.
# Then there is an a.s. finite N >= 0 with law(theta^N Z) = Q for Z ~ P.
# Test the exact construction on a finite ergodic system: E = Z/n, theta = +1, P uniform.
def filling(f, nmax=20000):
    n=len(f); P=np.ones(n)/n
    # densities wrt P; L h = h o theta^{-1}  (shift the array forward)
    a=np.ones(n); b=f.copy()
    law=np.zeros(n); mass=[]
    for k in range(nmax):
        m=np.minimum(a,b)
        law += m*P                 # mass accepted at stage k, as a measure
        mass.append((m*P).sum())
        b = b - m
        a = np.roll(a - m, 1)      # L(a-m): push forward by theta
        if b.sum()*1.0/n < 1e-15 and (a*P).sum() < 1e-15: break
    return law, np.array(mass), k+1
rng=np.random.default_rng(0)
print(f"{'n':>4} {'stages':>7} {'total accepted':>15} {'max |law - f P|':>17} {'E[N]':>9}")
for n in [5, 7, 12, 60]:
    for trial in range(2):
        w=rng.random(n)+0.02; f=w/ w.mean()      # density wrt uniform P: mean(f)=1
        f=f/ (f.mean())
        law,mass,stages=filling(f)
        target=f*np.ones(n)/n
        EN=float((mass*np.arange(len(mass))).sum())
        print(f"{n:>4} {stages:>7} {mass.sum():>15.12f} {np.abs(law-target).max():>17.3e} {EN:>9.4f}")
print()
print("Negative control - a NON-ergodic theta (shift by 2 on an even cycle) with f supported on the odd class:")
def filling_step2(f, nmax=20000):
    n=len(f); P=np.ones(n)/n
    a=np.ones(n); b=f.copy(); mass=[]
    for k in range(nmax):
        m=np.minimum(a,b); mass.append((m*P).sum())
        b=b-m; a=np.roll(a-m,2)
        if b.sum()/n<1e-15: break
    return np.array(mass), b
f=np.zeros(6); f[1]=f[3]=f[5]=2.0      # supported on odds, mean 1
mass,bleft=filling_step2(f)
print(f"  total accepted mass = {mass.sum():.6f}  (1.0 would mean success)   leftover b mass = {bleft.mean():.6f}")
print("  -> ergodicity is doing real work in the lemma, not decoration.")
