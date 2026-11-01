try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
# Lemma S: for a density f <= 1, g(s,tau) = int f(x) e^{i s x^2 + i tau x} dx satisfies
#   int int |g|^6 ds dtau = (2 pi)^2 int int m^2 <= 4 pi^3 / sqrt(3) = 71.61...
# m = density of (X1+X2+X3, X1^2+X2^2+X3^2). Check by direct quadrature (FFT in tau for each s), plus the s-tail.
import numpy as np, time
bound = 4*np.pi**3/np.sqrt(3)
def run(name, xgrid, f, S, ns, P):
    dx = xgrid[1]-xgrid[0]
    ss = np.linspace(-S, S, ns); ds = ss[1]-ss[0]
    tot = 0.0; t0=time.time()
    dtau = 2*np.pi/(P*dx)
    for s in ss:
        h = f*np.exp(1j*s*xgrid**2)
        G = np.fft.fft(h, n=P)*dx      # |G_k| = |g(s, tau_k)| up to a phase (translation of x does not matter)
        tot += (np.abs(G)**6).sum()*dtau*ds
    # tail |s|>S: int dtau |g|^6 ~ int f(x)^6 ... stationary phase: |g|^2 ~ (pi/|s|) f(x0)^2, dtau = 2|s| dx0
    tail = 2*np.pi**3*(f**3).sum()*dx*2/S     # 2 sides: int_S^inf 2 pi^3 (int f^3)/s^2 ds * 2
    print(f"{name:28s} int|g|^6 (|s|<{S}) = {tot:8.3f}  + tail ~{tail:6.3f}  total ~{tot+tail:8.3f}   bound {bound:.3f}   ({time.time()-t0:.0f}s)", flush=True)
# 1. uniform on [0,1]
x = np.linspace(0,1,4096,endpoint=False)+0.5/4096; f = np.ones_like(x)
run("uniform[0,1]", x, f, 300, 3001, 1<<16)
# 2. two intervals of length 1/2, far apart
x = np.linspace(0,12,24576,endpoint=False)+0.5/2048; f = ((x<0.5)|((x>11.5)&(x<12))).astype(float)
run("two halves at distance 11.5", x, f, 60, 1201, 1<<17)
# 3. bumpy: 10 bumps of width 0.1 at random positions in [0,20]
rng=np.random.default_rng(1); pos=np.sort(rng.uniform(0,19.9,10))
x = np.linspace(0,20,40960,endpoint=False)+0.5/2048; f=np.zeros_like(x)
for p in pos: f[(x>=p)&(x<p+0.1)] = 1.0
f *= 1.0/(f.sum()*(x[1]-x[0]))   # renormalise mass 1 (density still <= 1 up to grid error)
print("  max f =", f.max().round(4))
run("bumpy 10 x 0.1 in [0,20]", x, f, 40, 801, 1<<17)
