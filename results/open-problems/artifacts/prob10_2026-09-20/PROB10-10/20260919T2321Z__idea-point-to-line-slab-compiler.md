# PROB10-10 idea before code — random-endpoint slab compiler

The old R08 fixed-corner block test pays a reset cost: every block is forced from `(0,0)` to `(m,m)`. The new mechanism removes that reset while preserving the eventual diagonal direction.

Fix `m>=1`. Let

`H_k = {x in Z^2 : x_1+x_2=2mk}`.

Starting at `X_0=0`, in slab `k` use only northeast-oriented edges and choose the minimum-passage path from `X_k` to **any** vertex of `H_{k+1}`. Let its cost be `tau_k` and endpoint be

`X_{k+1}=X_k+(m+D_k,m-D_k)`,  `D_k in {-m,...,m}`.

Because successive slabs use disjoint edge levels and the environment is iid, the pairs `(tau_k,D_k)` are iid after translation. Reflection across the diagonal gives `D_k =_d -D_k`, hence `E D_k=0`. Therefore the random endpoint has no linear transverse drift:

`X_n=(mn+S_n,mn-S_n)`,  `S_n=sum_{k<n}D_k`,  `S_n/n -> 0`.

The concatenated path has cost `sum tau_k`, so this already suggests

`mu(1,1) <= q_m/m`,  where `q_m=E tau_0`.

There is also an explicit finite-to-infinite expectation correction. From `X_n` to `(mn,mn)`, correct one unit of transverse offset by a two-edge zig-zag lying entirely between levels `H_n` and `H_n+1`: north-west if `S_n>0`, east-south if `S_n<0`. These future-level edges are fresh conditional on the past. Thus the connector has conditional expected cost exactly `2|S_n|`. Since `|D_k|<=m` and `E D_k=0`,

`E|S_n| <= sqrt(E S_n^2) <= m sqrt(n)`.

Hence

`E T(0,nm(1,1)) <= n q_m + 2m sqrt(n)`,                       (A)

and therefore

`E T(0,nm(1,1))/(nm) <= q_m/m + 2/sqrt(n)`.                 (B)

Passing to the standard L1 time-constant limit yields the claimed compiler.

This is genuinely different from the retired R08 routes: it does not tensorize local detours, does not demand pointwise finite strictness, and does not reset to a deterministic corner after each block. The dependence inside a block is kept exactly; only disjoint slabs are independent.

## Counterexample/negation checks before coding

1. **Could the adaptive endpoint drift linearly and change the direction?** No: the endpoint displacement `D_k` is bounded and its law is reflection-symmetric. SLLN gives `S_n/n->0`.
2. **Could random translation destroy block independence?** No: `X_k` is measurable from lower-level edges, while slab `k` uses edges whose lower `x_1+x_2` level is in `[2mk,2m(k+1)-1]`; these edge sets are disjoint across `k`, and iid translation invariance gives the same conditional law.
3. **Could the endpoint correction reuse revealed edges and invalidate the expected `2|S_n|` cost?** Use the two-step zig-zag only on edges crossing levels `2mn` and `2mn+1`, which no previous oriented slab used. Conditional on `S_n`, those edges are fresh iid `Exp(1)`.

## Three materially different approaches compared this run

- **Dependence-controlled block optimization (selected):** the random-endpoint slab compiler above. It gives a complete finite-to-infinite inequality with an explicit `2/sqrt(n)` error and a finite exact quantity `q_m` to optimize.
- **Busemann/HJB variational comparison:** Krishnan's exact time-constant variational formula and Busemann/corrector language could in principle separate the diagonal support value from the axis support value. The present obstruction is source-level: no explicit stationary corrector/cocycle for iid Exp(1) is known that gives a strict directional defect without importing unproved curvature/differentiability. No claim is made from this route this run.
- **Overlap-controlled directed-path second moment:** for threshold `a=0.60048`, a single length-`2m` directed path has a Gamma lower-tail exponent below the binary path entropy, so the expected number of fast paths grows exponentially. The missing step is a rigorous overlap kernel controlling reconverging lattice paths; a tree-style second moment would be false because paths can split and rejoin. This remains a plausible future attack, but it is not used to certify the current theorem.

## Planned finite exact test

For `m=1,2,3`, compute `q_m` exactly from the exponential-memoryless infection recursion on the finite northeast triangle before level `2m`. This tests the mechanism without claiming that finite values close strict convexity. The source metric remains `Delta_12>=0` unless a certified `q_m/m` combines with a verified axis lower bound to produce a positive defect.
