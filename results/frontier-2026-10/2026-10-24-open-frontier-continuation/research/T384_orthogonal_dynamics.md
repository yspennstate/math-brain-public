# T384: standard-coordinate inputs and stable ReLU dynamics

**Theorem (one layer, fixed `k=d`, all deterministic labels).** Fix `0<α<2`, `k=d<∞`, inputs `x_j=e_j∈R^d`, and any deterministic `y∈R^k`. Initialize all first-layer coordinates `U_{ij}(0)` and second-layer weights `W_i(0)` independently as nondegenerate symmetric standard `α`-stable variables. At width `m`, set

`c_m=(m log m)^(−1/α)`, `η_m=(log m)^(2/α)`, `β_m=η_m c_m=m^(−1/α)(log m)^(1/α)`,

`f_j(t)=c_m Σ_i W_i(t)(U_{ij}(t))_+`, `r(t)=y−f(t)`.

Use squared loss `||r||²/2` and the **explicit absorbing-at-zero ReLU solution selection**: once a coordinate `U_{ij}` reaches zero, it remains zero. (Unlike the scalar model, its shared `W_i` may later reverse because of other examples; specifying the solution selection prevents Carathéodory delayed reactivation.) Define

`A_{j,m}(t)=m^(−2/α) Σ_i W_i(t)² 1_{U_{ij}(t)>0}`,

`C_{jℓ,m}(t)=m^(−2/α) Σ_i (U_{ij}(t))_+(U_{iℓ}(t))_+`,

`K_m(t)=diag(A_{1,m}(t),…,A_{k,m}(t))+C_m(t)`.

Let `σ_{j,m}=sgn(r_j(0))`, choosing either `+1` or `−1` when `r_j(0)=0`, and set the *width-dependent selected diagonal*

`P_{j,m}=m^(−2/α)Σ_i W_i(0)² 1_{U_{ij}(0)>0, σ_{j,m}W_i(0)>0}`,

`Q_{j,m}=P_{j,m}+C_{jj,m}(0)`, `Q_m=diag(Q_{1,m},…,Q_{k,m})`.

For every fixed `T<∞` and `0<δ≤T`,

`sup_{0≤t≤T} ||r(t)−exp(−tQ_m)r(0)||₂ →_P 0`,                  (1)

`sup_{δ≤t≤T} ||K_m(t)−Q_m||op →_P 0`,                         (2)

and `sup_{t≤T}||C_m(t)−C_m(0)||op→_P0`. In particular the first-layer matrix is **exactly diagonal** for orthogonal inputs and its positive-time diagonal approaches `P_{j,m}`. The output is a continuous path and (1) is a `C([0,T];R^k)` uniform-distance comparison to a width-dependent random path. The kernels can jump at gate hits; (2) means uniform distance to the random constant `Q_m` on `[δ,T]`, which can be embedded in `D([δ,T])`, and asserts no continuous-kernel-path limit. No joint initialization weak limit is needed for (1)–(2). All results are under the iid initialization for each width; `Q_m` itself need not converge in probability on a shared coupling of widths.

## 1. Exact coupled equations and global motion bound

Away from the finitely many gate hits, gradient flow gives

`U'_{ij}=β_m W_i r_j 1_{U_{ij}>0}`, `W'_i=β_m Σ_j r_j(U_{ij})_+`,

`r'=−K_m r`, `d||r||²/dt=−2rᵀK_mr≤0`.                         (3)

The matrix formula follows from orthogonality: first-layer parameter gradients for distinct `e_j` occupy distinct coordinates, so their kernel cross terms vanish; the `C` block comes from shared output weights. The network output is continuous across gate hits and (3) holds in integral form. Put `R_m=||r(0)||₂`, and

`S_m=m^(−2/α)Σ_i[W_i(0)²+Σ_jU_{ij}(0)²]`.

Both are tight: the paper's marginal stable output limit gives tight `r(0)` for fixed `k,y`, and the normalized sum of finitely many `α/2`-tail squared variables is tight since `α/2<1`. By (3), `||r(t)||≤R_m`. For `z_i(t)=(W_i(t),(U_{i1}(t))_+,…,(U_{ik}(t))_+)`, the active-coordinate ODE is `z_i'=β_m M_i(t)z_i`, where `M_i` is a symmetric star matrix of operator norm at most `||r(t)||≤R_m`; absorbed coordinates contribute zero. Grönwall and integration give, for `b_m=β_mR_mT`, uniformly for `t≤T`,

`||z_i(t)||≤e^{b_m}||z_i(0)||`,

`||z_i(t)−z_i(0)||≤b_m e^{b_m}||z_i(0)||`.                    (4)

In particular `b_m=o_P(1)`. With `g(b)=2be^b+b²e^{2b}`, applying `|x²−y²|≤2|y||x−y|+|x−y|²` and summing (4) yields

`sup_{t≤T}m^(−2/α)Σ_i|W_i(t)²−W_i(0)²|≤g(b_m)S_m=o_P(1)`. (5)

Writing `U_+(t)` for the `m×k` positive-part matrix, the Gram identity and (4) also yield

`sup_{t≤T}||C_m(t)−C_m(0)||op≤(e^{b_m}+1)b_m e^{b_m}S_m=o_P(1)`. (6)

Finally `0≼K_m(t)` and `||K_m(t)||op≤e^{2b_m}S_m`; the last bound sums the squared `z_i` norms and does not assume that individual stable weights are bounded. On an event `S_m≤K`, `R_m≤R` with fixed `K,R`, it is at most `2K` for all large `m`.

## 2. Off-diagonal second-layer terms vanish

For `j≠ℓ`, the initial summands `(U_{ij})_+(U_{iℓ})_+` are products of independent stable coordinates. Choose a number

`α/2<p<min{α,1}`,

which exists for every `0<α<2`. Then their `p`-th moments are finite. Since `p<1` and all summands are nonnegative, `(Σ_iZ_i)^p≤Σ_i Z_i^p`, so Markov gives for each `ε>0`

`P(C_{jℓ,m}(0)>ε)≤ε^(−p)m^(1−2p/α)E[(U_+V_+)^p]→0`. (7)

There are only finitely many entries. Combining (6)–(7), if `E_m(t)=C_m(t)−diag C_m(t)`, then

`ζ_m:=sup_{t≤T}||E_m(t)||op→_P0`.                           (8)

This covers `α≤1` without invoking a nonexistent first moment. For `α>1`, the elementary finite-mean calculation `E C_{jℓ,m}(0)=O(m^(1−2/α))` gives the same conclusion.

## 3. Coordinate signs despite off-diagonal forcing

Let `D_{j,m}(t)=A_{j,m}(t)+C_{jj,m}(t)≥0`. Variation of constants in (3) is exact:

`r_j(t)=r_j(0)e^(−∫_0^tD_{j,m})
          −∫_0^t e^(−∫_s^tD_{j,m})[E_m(s)r(s)]_j ds`.       (9)

On `G_m(c,R,K)={||r(0)||≤R,S_m≤K, min_j|r_j(0)|≥c}`, the first term has magnitude at least `c e^(−2KT)` for large `m`, while the second is at most `RTζ_m`. Thus whenever `RTζ_m≤(c/2)e^(−2KT)`, **every** `r_j(t)` has its initial sign and

`|r_j(t)|≥(c/2)e^(−2KT)` for all `t≤T`.                       (10)

For a single coordinate satisfying `|r_j(0)|≥c`, exactly the same argument gives (10) for that coordinate without requiring any other residual coordinate to be bounded away from zero. This localized version is needed to prove the output assertion (1) without an anti-concentration assumption. The full-kernel assertion (2) will use marginal stable atomlessness to make `G_m` high probability as `c↓0`.

## 4. Large output-weight signs and removal of opposing gates

On `S_m≤K`, (4) implies `max_i||z_i(0)||≤m^(1/α)√K` and

`max_i|W_i(t)−W_i(0)|≤b_m e^{b_m}m^(1/α)√K` for all `t≤T`.

Hence for every fixed `ε>0`, on `S_m≤K,R_m≤R`, all initialized weights with `|W_i(0)|≥εm^(1/α)` keep their sign and have `|W_i(t)|≥|W_i(0)|/2` for large `m`. Fix a coordinate `j` with `|r_j(0)|≥c`. Under (10), a large, initially active **supporting** neuron `σ_{j,m}W_i(0)>0` stays active. A large **opposing** one `σ_{j,m}W_i(0)<0` that remains active through time `δ` must satisfy, by integrating its negative active-side velocity,

`U_{ij}(0)≥d ε(log m)^(1/α)`, `d=δc e^(−2KT)/4>0`.       (11)

The union bound for (11) is unconditional; the good event is used only to derive its necessity. Independence of initialized `W_i` and `U_{ij}` and stable tails give

`P(∃i: |W_i(0)|≥εm^(1/α), U_{ij}(0)≥dε(log m)^(1/α))`

`≤m·O_ε(m^(−1))·O_{d,ε}((log m)^(−1))→0`.                 (12)

This includes initially opposing large neurons with `|W_i(0)|≤U_{ij}(0)`, which would not hit under a fixed-sign scalar hyperbolic orbit: their survival forces the large `U_{ij}(0)` in (11). Small initialized output weights have vanishing normalized square mass as the cutoff shrinks:

`Z_{m,ε}=m^(−2/α)Σ_iW_i(0)²1_{|W_i(0)|<εm^(1/α)}`,

`sup_{m large}E Z_{m,ε}≤C_α ε^(2−α)`.                     (13)

More explicitly, on the fixed-bound good event and outside the exceptional union event in (12), every large-weight gate at times `t∈[δ,T]` equals its initial supporting-gate indicator. At any such time,

`|A_{j,m}(t)−P_{j,m}|≤g(b_m)S_m+2Z_{m,ε}`.                 (13a)

Indeed the first term replaces each moved `W_i(t)²` by `W_i(0)²`, and the remaining indicator disagreement is supported on initially small weights, each of the two selected sums costing at most `Z_{m,ε}`. Equations (5), (12), (13), and (13a), plus monotonicity of absorption, imply for each such coordinate `j`

`sup_{δ≤t≤T}|A_{j,m}(t)−P_{j,m}|→_P0`                 (14)

on the fixed-bound good event, by first sending `m→∞` for fixed `ε` and then `ε↓0`. The argument does not assume an exact hyperbolic orbit for `U_{ij}`: `W_i(t)` is shared and changes, but its **large initial sign** is stable by (4). The normalized movement of all `W_i²` is already bounded in (5).

## 5. Kernel convergence and output near zero residuals

When all `|r_j(0)|≥c`, (6), (8), and (14) imply `sup_{δ≤t≤T}||K_m(t)−Q_m||op→_P0` on `S_m≤K,R_m≤R`. The paper's marginal output limit at each normalized `e_j` is a nondegenerate continuous `α`-stable law, so for each deterministic `y_j`,

`lim_{c↓0}limsup_{m→∞}P(min_j|r_j(0)|<c)=0`.

Tightness of `R_m,S_m` removes their cutoffs and proves (2), without requiring a **joint** law of `F_m` and `Q_m`.

For (1), keep `c>0` fixed and call `j` *good* if `|r_j(0)|≥c`, *small* otherwise. On `S_m≤K,R_m≤R`, each good coordinate has sign preservation by (9)–(10), whether or not some other coordinate is small, and its `D_{j,m}(t)` approaches `Q_{j,m}` on `[δ,T]` by (6), (14). Since `D_{j,m},Q_{j,m}≤2K` for large `m`, its scalar variation formula yields

`sup_{t≤T}|r_j(t)−r_j(0)e^(−Q_{j,m}t)|`

`≤R[3Kδ+T sup_{δ≤t≤T}|D_{j,m}(t)−Q_{j,m}|]+RTζ_m`.   (15)

For a small coordinate, (9) gives `sup_{t≤T}|r_j(t)|≤c+RTζ_m`, while `|r_j(0)e^(−Q_{j,m}t)|≤c`, so its difference is at most `2c+RTζ_m` regardless of its gate pattern. With `k` fixed, (15) and the small-coordinate bound, then `m→∞`, `δ↓0`, `c↓0`, and tightness cutoffs `R,K→∞`, prove (1) **without** using atomlessness near zero. The sign selected at an exact zero can be arbitrary in (1).

## Limits and boundary

At `t=0`, `K_m(0)=diag(A_{j,m}(0))+C_m(0)`, with first-layer `A_{j,m}(0)` containing **both** supporting and opposing initial weights. At every fixed positive time, only the supporting extreme first-layer weights remain at leading order, while `C_m(t)` stays near its initial diagonal. Thus (2) is an initial-boundary-layer statement, not a global frozen-initial-kernel theorem. The theorem requires the **standard coordinate inputs** `x_j=e_j` in the very basis whose hidden-layer entries are iid stable. It does **not** extend by rotating to arbitrary orthogonal inputs: iid non-Gaussian stable coordinates are not rotationally invariant, and a single extreme hidden coordinate can contribute to multiple rotated projections and hence a nonzero off-diagonal `H^(2)`. General fixed inputs, efficient training, and deep networks are not addressed.

The complementary joint initialization result in `T384_orthogonal_initialization.md` supplies `(f_m(0),Q_m)⇒(F,Q)`, where independent primitive limits consist of an output vector `F`, positive-stable first-coordinate energies `C_j`, and a marked Poisson process `N`; nevertheless the assembled `Q` vector generally **depends on** the sign pattern of `y−F`. Combining that result with (1)–(2), for each `T` and `δ>0`,

`(f_m|_[0,T],K_m|_[δ,T]) ⇒ (t↦y−(y−F)⊙exp(−tQ), t↦diag Q)`

in `C([0,T];R^k)×D([δ,T];R^{k×k})`. The second component has a constant positive-time path. The joint law is specified by equations (7)–(8) of the initialization note; one cannot replace it by independent `F` and `Q` vectors when `k≥2`.
