"""Framing-independent check of the Conjecture 4.2 counterexample: simulate the MMPP itself.
m=64 cycle at rate 1, states 0..31 emit Poisson arrivals at rate 0.25.  Measure from the sample path:
  P(T^alpha > t)  = fraction of consecutive inter-arrival gaps exceeding t   (event-stationary)
  P(T^pi > t)     = fraction of uniformly sampled times whose wait to the next arrival exceeds t (time-stationary)
Conjecture 4.2 says the second >= the first for every t.  Matrix prediction at t*=53.0: 0.005276 vs 0.007865."""
import numpy as np
rng = np.random.default_rng(2026)
m, k, L = 64, 32, 0.25
n_hold = 12_000_000                      # holding intervals ~ 187,500 laps ~ 1.5M arrivals
hold = rng.exponential(1.0, n_hold)
ends = np.cumsum(hold); starts = ends - hold
state = np.arange(n_hold) % m
hot = state < k
cnt = np.zeros(n_hold, dtype=np.int64)
cnt[hot] = rng.poisson(L*hold[hot])
idx = np.repeat(np.arange(n_hold), cnt)
arr = starts[idx] + rng.random(idx.size)*hold[idx]
arr.sort()
Ttot = ends[-1]
print(f"arrivals {arr.size}, total time {Ttot:.0f}, empirical intensity {arr.size/Ttot:.5f} (lambda* = {k*L/m})")
gaps = np.diff(arr)
print(f"E[T^alpha] = {gaps.mean():.4f} (theory 8.0), c^2 = {gaps.var()/gaps.mean()**2:.4f} (E0077 says >= 1)")
u = rng.random(2_000_000) * (arr[-1] - arr[0]) + arr[0]
j = np.searchsorted(arr, u, side='right')
wait = arr[j] - u                        # forward recurrence time from a uniform instant
for t in [20.0, 40.0, 50.0, 53.0, 56.0, 60.0]:
    pa = (gaps > t).mean(); pp = (wait > t).mean()
    sa = np.sqrt(pa*(1-pa)/gaps.size); sp = np.sqrt(pp*(1-pp)/wait.size)
    print(f"t={t:5.1f}: P(T^alpha>t)={pa:.5f}+-{sa:.5f}   P(T^pi>t)={pp:.5f}+-{sp:.5f}   pi-alpha = {pp-pa:+.5f}  ({(pp-pa)/np.hypot(sa,sp):+.1f} sigma)")
