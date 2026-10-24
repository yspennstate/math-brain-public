import numpy as np
rng=np.random.default_rng(3)
a=1.0; R0=1/(np.sqrt(2)*a); T=1.0; S=(np.exp(2*T)-1)/2
def P_hit(x, npaths, nsteps):
    ds=S/nsteps; sd=np.sqrt(ds)
    B=np.zeros((npaths,4)); B[:,0]=R0; m=np.full(npaths,R0*R0)
    for k in range(nsteps):
        B+=rng.normal(0,sd,size=(npaths,4)); m=np.minimum(m,(B*B).sum(1))
    return float(np.mean(m<=x*x))
print("Question: is the fall in P/x^2 real, or does my discrete path jump over the ball?")
print("A step moves the BM about sqrt(ds). If sqrt(ds) is not << x, hits get missed.")
print(f"{'x':>6} {'nsteps':>7} {'sqrt(ds)':>9} {'sqrt(ds)/x':>11} {'P(inf<=x)':>10} {'P/x^2':>7}")
for x in [0.20, 0.10]:
    for nsteps in [750, 3000, 12000]:
        ds=S/nsteps
        p=P_hit(x, 20000, nsteps)
        print(f"{x:>6.2f} {nsteps:>7} {np.sqrt(ds):>9.4f} {np.sqrt(ds)/x:>11.3f} {p:>10.5f} {p/(x*x):>7.3f}")
print("\nexact infinite-horizon limit of P/x^2 as x->0 is 1/R0^2 =", round(1/R0**2,4))
