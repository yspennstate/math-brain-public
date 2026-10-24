# Numerical diagnostic output

Status: finite floating stress test only; not a proof.

The saved `burst_block_laplace_probe.py` is the repository form of the same combinatorial evaluator executed in this run. The complete `s=k/100`, `k=0,...,100`, sweeps found no ratio above `1` for the following even-layer burst laws:

| n | L | maximum ratio including s=1 |
|---:|---:|---:|
| 12 | 4 | 1.0 |
| 16 | 4 | 1.0 |
| 18 | 6 | 1.0 |
| 24 | 6 | 1.0 |

The equality at `s=1` is tautological. On a separate nontrivial grid excluding `s=1` and zero-mass cells, representative maxima were:

- `(12,4)`: `0.9953428691679338` at `(j,t,a,y,s)=(3,0,0,0,0.99)`;
- `(16,4)`: `0.9951911486649648` at `(5,0,0,0,0.99)`;
- `(18,6)`: `0.9952806122448982` at `(3,0,0,0,0)`;
- `(24,6)`: `0.9951583934781764` at `(5,0,0,0,0.99)`.

Small even-layer instances can fail: `(n,L)=(8,4)` has a ratio `1.020833333333333` already at the `s=0` atom endpoint, with `(j,t,a,y)=(2,0,0,0)`.

The integrated product-profile diagnostic at `n=64` gives

- `V = 1-(63/64)^64 = 0.6350134757560926`;
- `2/ln(64) = 0.48089834696298783`;
- violation gap `0.15411512879310474`.

A separate randomized symmetry-type search found no violation of the full block-Laplace inequality for `(n,L)=(4096,8)` on the tested `s` grid, but this is deliberately not promoted to a theorem. The next mathematical target is an analytic proof or explicit violating block/centre/scale for the logarithmic even-layer family.
