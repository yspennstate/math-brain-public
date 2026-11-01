# R11 / I0054 — pre-code idea: quenched random logit shuffles

Timestamp: 2026-09-20T05:38:26Z

This file records the mathematical route **before checker code**.

## New route

Use the conserved CTCS logit measure from U066, but randomize the interval exchange **once for the whole finite tree**, not independently at each proposal. This creates a genuinely different quenched-random-environment hierarchy: conditional on the environment it is a Markov branching paintbox compiler, but after averaging over the one persistent environment the finite tree is generally not Markov branching and different clades are correlated through the common hidden permutation.

Methods used this run:

- **#9 RANDOMIZE:** choose one global random cell permutation `pi_N` and keep it for the whole tree;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** retain leaf exchangeability but deliberately break annealed branching independence / exponential holding times through shared quenched disorder;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** formulate the construction as a random interval-exchange / quenched-environment compiler, using the same kind of quenched-to-annealed uniformity familiar from random environments. Generic random environments and interval exchanges are classical; no novelty is claimed for those ingredients.

## Proposed theorem U067 — growing quenched logit-shuffle compiler

Fix `L>0`. For each `N`, let `M_N>=1` and partition `[0,L)` into equal cells

`I_r=[r h_N,(r+1)h_N)`, `h_N=L/M_N`, `0<=r<M_N`.

Choose one uniform random permutation `pi_N` of `{0,...,M_N-1}` and keep it fixed for the entire `N`-leaf hierarchy. Define the interval exchange

`S_{N,pi}(r h_N+u)=pi(r) h_N+u` for `0<=u<h_N`,

and set `S_{N,pi}(y)=y` outside `[0,L)`.

At harmonic mark `s=1,...,N-1`, with `x_s=s/N`, use the usual clock

`lambda_{N,s}=N/[2s(N-s)] = 1/[2N x_s(1-x_s)]`,

but color every label in the active clade iid red with probability

`p_{N,s,pi}=sigma(S_{N,pi}(logit x_s))`,

where `sigma(y)=e^y/(1+e^y)`. Split iff both colors occur. Conditional on `pi_N`, all clocks/colors of descendants are otherwise fresh.

For a specified unordered `i|j` split, define

`F_{N,pi;i,j}(x) = [tau_{N,pi}(x)^i(1-tau) ^j + tau^j(1-tau)^i]/[2x(1-x)]`.

Because `S_{N,pi}` is Lebesgue-measure preserving in logit coordinates,

`int_0^1 F_{N,pi;i,j}(x) dx = B(i,j)`

**for every permutation pi and every N**.

The key finite-grid point is uniform bounded variation. The map is smooth on each of `M_N` cells and identity off the fixed compact interval. Smooth variation over all cells is bounded by a constant depending only on `(i,j,L)`; there are `M_N-1` jumps, each uniformly bounded because the compact logistic image stays away from 0 and 1. Hence

`TV(F_{N,pi;i,j}) <= C_{i,j,L}(1+M_N)`

uniformly in `pi`. The rectangle-rule discrepancy then gives

`|q_{N,pi}(i,j)-B(i,j)| <= C_{i,j,L}(1+M_N)/N`.

Therefore if

`M_N/N -> 0`,

then for each fixed visible `k`, conditional generator convergence to CTCS is uniform in the quenched environment. Common uniformization gives

`sup_pi || Law(Pi_{N,pi}^{[k]}|_[0,T]) - Law(CTCS^{[k]}|_[0,T]) ||_TV -> 0`.

Averaging over the single global `pi_N` preserves the same bound. Hence the annealed quenched-shuffle hierarchy has the full CTCS(infinity) projective limit. The proposed concrete model C085 takes

`L=2 log 2`, `M_N=max(2,floor(sqrt(N)))` (capped by N if needed), and `pi_N` uniform once per tree.

The important qualitative distinction from C084/U066 is that C084 uses a deterministic fixed interval exchange. C085 uses a random permutation chosen once and shared by all clades for the entire tree, creating persistent cross-clade dependence in the annealed finite tree law.

## Exact N=4 witness plan

For C085 at `N=4`, `M_4=2`, so the environment is uniform on two permutations:

1. identity on `[0,2 log 2)`;
2. the C084 swap of `[0,log2)` and `[log2,2log2)`.

At `N=4`, the harmonic clocks are `(2/3,1/2,2/3)`.

Identity environment biases are `(1/4,1/2,3/4)`, giving exact specified rates

`q_id(1,3)=7/32`, `q_id(2,2)=5/32`, total root rate `Lambda_id=43/32`.

Swap environment biases are `(1/4,2/3,3/5)`, giving the already independently derived C084 values

`q_swap(1,3)=722693/3240000`,
`q_swap(2,2)=560707/3240000`,
`Lambda_swap=4572893/3240000`.

These total rates are unequal. Conditional on the one global environment, the root holding time is exponential with the corresponding rate, so annealed survival is

`P(T_root>t)=1/2 exp(-Lambda_id t)+1/2 exp(-Lambda_swap t)`.

This is not exponential because `Lambda_id != Lambda_swap`. More algebraically, if `a=1/Lambda_id` and `b=1/Lambda_swap`, then

`E[T^2]-2 E[T]^2 = (a-b)^2/2 >0`.

Every deterministic leaf relabeling and positive global time rescaling of source CTCS(4) preserves the property “root holding time is exponential” (and the scale-free equality `E[T^2]=2E[T]^2`). Thus C085 is not equivalent to the source. It is also not equivalent to deterministic C084/U066 compilers, whose finite root holding times are exponential.

## What must be checked before promotion

1. Exact source/current-literature/ownership/audit state remains unchanged: I0054 is still R11 `PENDING_ADMISSION`; no current-package P26 + second OTHER audit pair found.
2. Prove the uniform total-variation bound carefully from bounded variation of `F`.
3. Exact-arithmetic checker for the N=4 identity/swap environments, root rates, and non-exponential moment invariant; small-N direct split-rate checks for several permutations; exact beta-integral invariance for representative cell permutations using symbolic/rational odds transforms where possible.
4. Keep status author-side only; self-check is not an independent audit.
