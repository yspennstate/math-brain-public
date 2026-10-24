Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0336 — exact two-bin prefix conservation, min-cost-flow reduction, and Gaussian innovation homogenization

Worker: `R7-05`  
Native task ID: `6aabe805f32881919992996e1c5cfad6`  
Canonical target: `P0336`  
Source: Eustasio del Barrio, Alberto González-Sanz, Jean-Michel Loubes, David Rodríguez-Vítores, *Distributional Limit Theory for Optimal Transport*, arXiv:2505.19104v2 (13 July 2026), Problem 4.  
Status: **OPEN / PARTIAL**.  
Frozen metric: `SEL_ID = 0` before and after this artifact.

## 1. Recovery objective after STUCK1

The preceding STUCK1 diagnosis isolated the first source-faithful missing step: after the universal common-slope tangent energy has been removed, derive the first **discrete, kernel-dependent** correction of the empirical assignment. The selected recovery action was to solve as much as possible of the two-horizontal-bin empirical model while retaining genuine vertical order statistics and the global permutation constraint.

This run uses exactly the assigned methods:

- **B12 — find what is conserved:** derive exact marked prefix-flux identities in the two-bin model;
- **B19 — make it an algorithm:** give an exact min-cost-flow/sensitivity representation of the horizontal contingency statistic;
- **B30 — one scale at a time:** analyze a macroscopic block and then a mesoscopic Gaussian-innovation decomposition.

The main new conclusion is two-sided.

1. A single macroscopic block has a genuinely random first residual preference: the pure monotone-versus-crossed cost difference converges to a nondegenerate difference of two Cramér–von Mises functionals. Thus the previously suggested deterministic `J(kappa)=int (b-a)^(-1) d kappa` cannot be justified by simply replacing the source-faithful residual by its expectation.
2. After conditioning out coarse prefix information and splitting Brownian bridge fluctuations into many independent interval innovations, the same local bias **does** self-average: for `K` equal blocks the innovation-level monotone-minus-crossed residual has mean `-1/(18K)`, variance `17/(810 K^3)`, and `K` times that residual converges in `L^2` to `-1/18`.

This identifies a much sharper possible selector mechanism: deterministic strict-Monge selection can only emerge after coarse marked flux has been handled pathwise and the remaining local innovations are averaged across a diverging number of mesoscopic blocks.

## 2. The exact two-bin model

Use horizontal source marks `a in {0,1}` and target marks `b in {2,3}`. For a matched pair with vertical coordinates `(s,t)`, let

`D_ab = b-a in {1,2,3}`

and write the Euclidean excess over the horizontal baseline as

`e_D(t-s) = sqrt(D^2+(t-s)^2)-D`.

Because the sum of the horizontal gaps is matching-independent, minimizing Euclidean assignment cost is equivalent to minimizing the sum of the `e_D` terms.

Let

- `N_0,N_1` be the source horizontal counts,
- `M_2,M_3` be the target horizontal counts,
- `N_ab` the number of matched edges of horizontal cell `(a,b)`.

Then the entire horizontal contingency matrix is determined by the single integer

`k := N_02`:

`N_02 = k`,

`N_03 = N_0-k`,

`N_12 = M_2-k`,

`N_13 = N_1-M_2+k`.

The exact feasible range is

`max(0,N_0+M_2-n) <= k <= min(N_0,M_2)`.

Thus in the two-bin model the horizontal-selection variable really is one scalar integer. In the balanced population normalization `N_0=N_1=M_2=M_3=n/2`, the normalized statistic is `p_n=k/n`, with the monotone extreme at `1/2` and the crossed extreme at `0`.

## 3. B12 — exact marked prefix conservation

Fix a vertical cut `y`. For each horizontal cell `(a,b)`, define

`A_ab(y) = # { matched edges (a,s)->(b,t) with s <= y }`,

`B_ab(y) = # { matched edges (a,s)->(b,t) with t <= y }`,

and the signed vertical flux

`F_ab(y) = A_ab(y)-B_ab(y)`.

Also let

`S_a(y) = # { source points of type a with vertical coordinate <= y }`,

`T_b(y) = # { target points of type b with vertical coordinate <= y }`.

### Proposition 3.1 — exact prefix identities

For every perfect matching and every cut `y`,

`A_02+A_03 = S_0`,

`A_12+A_13 = S_1`,

`B_02+B_12 = T_2`,

`B_03+B_13 = T_3`,

and therefore

`F_02+F_03+F_12+F_13 = (S_0+S_1)-(T_2+T_3)`.

Moreover the two marked discrepancies satisfy

`S_0-T_2 = F_02 + A_03-B_12`,

`S_1-T_3 = F_13 + A_12-B_03`.

#### Proof

The first four identities simply partition the source or target endpoints below the cut by the horizontal cell of their matched edge. Subtracting the target identities from the source identities gives the total signed flux formula. For the first marked identity,

`S_0-T_2 = (A_02+A_03)-(B_02+B_12) = F_02 + A_03-B_12`.

The second is identical with the labels interchanged. `QED`.

These formulas are the exact discrete conservation law that the smooth tangent problem compresses. In particular, cross-cell assignments act as a control that can absorb horizontal-mark prefix imbalance before the remaining discrepancy is carried as vertical flux inside a diagonal cell.

### Corollary 3.2 — cross-mass lower bound for suppressing a marked flux

In the balanced case, put `r=N_03=N_12`. Since `0<=A_03(y),B_12(y)<=r`,

`|S_0(y)-T_2(y)-F_02(y)| <= r`

for every `y`. Hence

`r >= sup_y ( |S_0(y)-T_2(y)| - |F_02(y)| )`.

Thus any construction that tries to make the diagonal-cell flux `F_02` much smaller than the raw marked empirical discrepancy must open a corresponding number of crossed horizontal edges. This makes precise why an endpoint limiting kernel may nevertheless require `O(sqrt(n))` off-kernel edges at tangent scale.

The analogous statement holds for the `(1,3)` cell.

## 4. Blockwise monotonicity, but failure of global vertical Monge order

For a fixed horizontal cell `(a,b)`, define

`c_D(s,t)=sqrt(D^2+(t-s)^2)`.

Then

`partial_s partial_t c_D(s,t) = - D^2/(D^2+(t-s)^2)^(3/2) < 0`.

Therefore for `s_1<s_2` and `t_1<t_2`,

`c_D(s_1,t_1)+c_D(s_2,t_2) < c_D(s_1,t_2)+c_D(s_2,t_1)`.

So, **after the membership of endpoints in a horizontal cell has been fixed, the unique optimal matching inside that cell is the order-preserving vertical matching.** Every global optimum may therefore be chosen blockwise order-preserving.

However a naive dynamic program based on a single global vertical order is invalid: the whole two-bin cost matrix is not globally Monge because the horizontal gap changes with the source/target marks.

A simple exact witness uses sources

`x_1=(0,0)`, `x_2=(1,1/4)`

and targets, in increasing vertical order,

`y_1=(2,1/2)`, `y_2=(2,1)`.

The vertically order-preserving pairing has cost

`sqrt(17)/2 + 5/4`,

whereas the crossed pairing has cost

`sqrt(5) + sqrt(17)/4`.

Numerically these are `3.3115528128...` and `3.2668443839...`, so the crossed pairing is strictly cheaper. Thus any exact DP must retain horizontal mark state; a one-dimensional prefix recurrence that silently assumes global Monge structure is unsound.

## 5. B19 — exact min-cost-flow and sensitivity representation of `p_n`

Let the actual source points be `X_i=(A_i,S_i)` and targets `Y_j=(B_j,T_j)`. Build the standard bipartite integral min-cost-flow network:

- source node `s` to each source observation `i`, capacity `1`, cost `0`;
- every source observation `i` to every target observation `j`, capacity `1`, cost

  `c_ij = sqrt((B_j-A_i)^2+(T_j-S_i)^2)`;

- every target observation `j` to sink `t`, capacity `1`, cost `0`;
- send total flow `n`.

Integral capacities make every optimum an integral perfect matching. Since the sample coordinates are continuous, the empirical assignment is generically unique, so the horizontal count `k_n=N_02` is well-defined almost surely.

To expose `k_n` directly, add a scalar penalty `theta` to every `(0,2)` edge and define

`Phi_n(theta) = min_sigma [ sum_i c_{i,sigma(i)} + theta N_02(sigma) ]`.

This is the minimum of finitely many affine functions of `theta`, hence is concave and piecewise affine. At every differentiability point,

`Phi_n'(theta) = N_02(sigma_theta)`

for the unique optimal penalized matching `sigma_theta`. In particular, when the unpenalized optimum is unique,

`Phi_n'(0) = k_n`,

and

`p_n = Phi_n'(0)/n`.

This is an exact sensitivity representation of the selection statistic. It turns the two-bin selection problem into the behavior at zero penalty of a random concave assignment value function.

Combining this with blockwise monotonicity gives an equivalent structural description: first select, for each of the four horizontal cells, source and target subsequences whose cell counts obey the single contingency parameter `k`; then match the selected subsequences in increasing vertical order inside each cell. The nontrivial global problem is the selection of those four interlocking subsequences.

## 6. B30, scale 1 — one macroscopic balanced block has random sign

The preceding run's Gaussian `2x2` microcell suggested the deterministic expected functional `J(kappa)=int (b-a)^(-1) d kappa`. The first test is whether that expected preference survives in a source-faithful empirical order-statistic block.

Consider the balanced surrogate with exactly `m` source points on each horizontal line `0,1` and exactly `m` target points on each horizontal line `2,3`. Their vertical coordinates are four independent iid `Uniform[0,1]` samples. Let

- `M` be the pure monotone horizontal contingency: `0->2` and `1->3`;
- `C` be the pure crossed contingency: `0->3` and `1->2`.

Inside each occupied horizontal cell use the vertically order-preserving matching, which is exactly optimal for that fixed contingency by Section 4. Let `R_M^(m),R_C^(m)` be the **total Euclidean excesses** over the horizontal baseline.

### Theorem 6.1 — nondegenerate Brownian residual comparison

As `m -> infinity`,

`R_M^(m)-R_C^(m)  =>  Delta`,

where

`Delta = (1/2) I_+ - (5/6) I_-`,

and `I_+,I_-` are independent copies of

`I = int_0^1 B(u)^2 du`

for a standard Brownian bridge `B`.

Consequently

`E[Delta] = -1/18`,

`Var(Delta) = 17/810`,

`P(Delta<0) > 1/2`,

and

`P(Delta>0) > 0`.

Thus the monotone pure plan wins more often than the crossed pure plan and has lower expected residual, but the sign does **not** self-average in one macroscopic block.

#### Proof

Let `U_a,(1)<=...<=U_a,(m)` and `V_b,(1)<=...<=V_b,(m)` denote the four independent uniform order-statistic samples. For fixed `D in {1,2,3}`,

`e_D(h)=h^2/(2D)+O(h^4)`

uniformly for `|h|<=1`. Uniform empirical-quantile convergence gives

`max_r |U_a,(r)-V_b,(r)| -> 0`

in probability, while the expected sum of squared order-statistic differences is bounded. Hence

`sum_r |U_a,(r)-V_b,(r)|^4 <= (max_r |U_a,(r)-V_b,(r)|^2) sum_r |U_a,(r)-V_b,(r)|^2 -> 0`

in probability. Therefore the quartic Taylor remainder disappears in the total excess.

The uniform quantile-process CLT yields jointly, for four independent standard Brownian bridges `B_0,B_1,B_2,B_3`,

`sum_r (V_b,(r)-U_a,(r))^2  =>  int_0^1 (B_a-B_b)^2 du`.

Thus

`R_M^(m) => Q_M := (1/4) int(B_0-B_2)^2 + (1/4) int(B_1-B_3)^2`,

`R_C^(m) => Q_C := (1/6) int(B_0-B_3)^2 + (1/2) int(B_1-B_2)^2`.

At each vertical parameter `u`, the quadratic form `Q_M-Q_C` in the four Gaussian coordinates has exactly the same constant coefficient matrix as the canonical Gaussian microcell from the preceding run. Its nonzero eigenvalues are `1/2` and `-5/6`. Applying the same fixed orthogonal transform simultaneously to the four independent Brownian bridges produces two independent standard Brownian bridges `B_+,B_-` in the nonzero eigendirections. Therefore

`Q_M-Q_C = (1/2) int B_+^2 - (5/6) int B_-^2`,

which is the stated law.

The Karhunen–Loeve expansion gives

`I = sum_{r>=1} Z_r^2/(pi^2 r^2)`.

Hence `E[I]=1/6` and `Var(I)=1/45`. Independence gives

`E[Delta]=(1/2-5/6)/6=-1/18`,

`Var(Delta)=(1/4+25/36)/45=17/810`.

Since `I_+,I_-` are iid continuous positive nondegenerate random variables,

`P(Delta<0)=P(I_+/I_-<5/3)>P(I_+<I_-)=1/2`,

while `P(Delta>0)>0` because the ratio has nontrivial support above `5/3`. `QED`.

### Corollary 6.2 — the expectation-level `J` bias is not by itself a pathwise selector

For one macroscopic block the expected strict-Monge preference and its random fluctuation live at the **same** order. In particular, replacing the true residual by its expectation loses a nonvanishing random term. The candidate `J` functional therefore cannot be justified by a one-block law-of-large-numbers argument.

This does not refute translation as the source-level limiting plan, because a neighborhood of a limiting kernel is allowed to use `o(n)` off-kernel edges; the previous tangent theorem shows that `O(sqrt(n))` such edges can already change the order-`1/n` energy. The pure endpoint comparison is a diagnostic, not a closure argument.

## 7. B30, scale 2 — Gaussian bridge innovations self-average across many blocks

The one-block randomness suggests conditioning on coarse prefix information before looking for a deterministic local bias.

Let `B_0,B_1,B_2,B_3` be four independent standard Brownian bridges on `[0,1]`. Partition `[0,1]` into `K` equal intervals

`I_q=[(q-1)/K,q/K]`.

Condition on all four bridge values at the `K+1` partition points. On each interval, subtract the linear interpolation between the two endpoint values. The residual processes

`beta_{a,q}`

are, conditionally and unconditionally, independent across `q` and `a`, and each is a Brownian bridge on an interval of length `ell=1/K`. Thus

`beta_{a,q}((q-1)ell+ell u) =_d sqrt(ell) * B_{a,q}(u)`

with independent standard bridges `B_{a,q}`.

Define the **innovation-only** monotone and crossed residuals

`G_M(K) = sum_q [ (1/4) int_{I_q}(beta_0-beta_2)^2 + (1/4) int_{I_q}(beta_1-beta_3)^2 ]`,

`G_C(K) = sum_q [ (1/6) int_{I_q}(beta_0-beta_3)^2 + (1/2) int_{I_q}(beta_1-beta_2)^2 ]`.

### Theorem 7.1 — exact innovation homogenization

For iid copies `Delta_1,...,Delta_K` of the random variable in Theorem 6.1,

`G_M(K)-G_C(K) =_d K^(-2) sum_{q=1}^K Delta_q`.

Therefore

`E[G_M(K)-G_C(K)] = -1/(18K)`,

`Var(G_M(K)-G_C(K)) = 17/(810 K^3)`,

and

`K [G_M(K)-G_C(K)] -> -1/18`

in `L^2` as `K->infinity`.

#### Proof

On an interval of length `ell`, the innovation has amplitude `sqrt(ell)` and the integration variable contributes another factor `ell`. Hence every quadratic bridge integral is exactly `ell^2=K^(-2)` times the corresponding unit-interval integral. The four bridge innovations in different intervals are independent. Thus each block contributes an independent copy of `K^(-2) Delta`, proving the distributional identity. The mean and variance follow from Theorem 6.1:

`K * K^(-2) * (-1/18) = -1/(18K)`,

`K * K^(-4) * (17/810) = 17/(810 K^3)`.

Finally

`E[( K(G_M-G_C)+1/18 )^2] = K^2 * 17/(810 K^3) = 17/(810K) -> 0`.

`QED`.

### Interpretation

This calculation exhibits exactly the homogenization mechanism that was missing from the one-block comparison. Once coarse prefix data are frozen, the genuinely local Brownian-bridge innovations average across many blocks. Their random fluctuation is smaller than their strict-Monge mean by a factor `K^(-1/2)`.

For the monotone-versus-crossed pair this innovation-level correction therefore becomes deterministic after multiplying by `K`. The sign is the same as the candidate `J` functional: monotone/translation is favored.

What is **not** yet proved is that the actual discrete empirical assignment, after the exact coarse marked flux from Section 3 is optimized, has an innovation residual asymptotic to `G_K` uniformly over horizontal contingency states.

## 8. What this run changes in the P0336 strategy

The earlier candidate statement “the first discrete correction is deterministic `J(kappa)`” was too crude. The correct picture now has three levels.

1. **Macroscopic tangent level:** universal and kernel-blind, as proved in the preceding runs.
2. **One macroscopic residual block:** kernel-sensitive but genuinely random; the expected `J` preference is not pathwise.
3. **Many conditioned mesoscopic innovations:** the same strict-Monge preference self-averages deterministically, with an exact signal-to-noise improvement of order `sqrt(K)`.

Thus a plausible source-level proof must first condition/control the coarse marked prefix flux and only then homogenize the local innovations. Averaging before the coarse conservation law is enforced is invalid.

## 9. Exact remaining blocker

A decisive theorem would choose a scale `K=K_n` with

`K_n -> infinity`,

`K_n=o(n)`,

and prove a source-faithful expansion, uniformly over horizontal kernels or the one-parameter two-bin contingency states,

`empirical residual = universal coarse-flux term + innovation term + error`,

where the error is `o_P(1/K_n)` after the natural total-excess normalization, and where the innovation term converges to the Gaussian block functional of Section 7 (or another explicitly identified local functional).

The exact min-cost-flow representation in Section 5 supplies the discrete object whose coarse conditioning must be analyzed. The prefix identities in Section 3 identify the conservation variables. The Gaussian calculation in Section 7 identifies what has to emerge after those variables are frozen.

Until this bridge is proved, neither translation nor any random alternative is established for the source problem.

## 10. Next attack

The next ordinary run should not repeat `B12/B19/B30`. The most useful nonrepeating triple is:

- **B14 — FIND THE GROUP ACTING:** exploit the exact two-bin involutions and mark-exchange symmetries to reduce the conditioned local effective functional to one scalar contingency variable;
- **B13 — FIND WHAT ONLY INCREASES:** search for a monotone reduced-cost / uncrossing functional along the penalty path `theta -> Phi_n(theta)` that forces the optimal contingency toward the monotone endpoint after coarse flux is frozen;
- **B29 — ADD THE POINTS AT INFINITY:** analyze the boundary tangent cones `p=0` and `p=1/2` together with interior `p`, so an eventual effective functional cannot hide a different boundary scaling.

The fixed metric remains `SEL_ID=0`. This is substantive recovery progress but not source closure.