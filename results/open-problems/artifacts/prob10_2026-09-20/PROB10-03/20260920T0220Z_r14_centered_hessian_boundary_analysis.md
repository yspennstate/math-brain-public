Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

# PROB10-03 / R14 — centered-Hessian certification compiler and the `B -> 0` full-lift boundary equation

Status: **PARTIAL / SOURCE OPEN / TWO NEW ANALYTICAL LEMMAS / NO RIGOROUS THRESHOLD ENDPOINT MOVED**.

Frozen model throughout: `M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)`, and `<g_a,sigma> >= -sqrt(N)` for all `a<=M`, with fixed `alpha` and `N->infinity`.

The source metric remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

width `6.48139658710`.

The lower endpoint is the repository-supported Montanari--Zhong--Zhou LP-success theorem after normalization; the upper endpoint is the globally certified one-parameter Stojnic-2013 partial-lift/Gordon bound. The complete second-lift point at `alpha=12.75` remains a candidate until a continuous enclosure is proved.

This run deliberately changes method after two unchanged R14 PROB10 iterations. It does **not** produce another finite-mesh certificate.

## 1. Recovered exact second-full reduction

Use the companion exact reduction with

`q=pD^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`,

`h_B(x)=exp[-B(x-1)_+^2]`,

`f_{p,B}(z)=E_H h_B(sqrt(p)z+sqrt(1-p)H)`,

`I=E_Z log f`, `I_B=partial_B I`, and

`K=E_Z[(partial_z log f)^2]`.

On the complete interior branch,

`D^2=K/[-4p^2B^2I_B]`,

`alpha=-c^2/[4B^2I_B]`,

`gamma=c/(4B)`,

and stationarity at fixed density is equivalent to

`H(p,B)=I-BI_B-4B^2I_B(T_D/c_D)=0`,

`alpha(p,B)=alpha_0`.

The stationary comparison value is

`Psi(p,B)=T+cI/(4B^2I_B)`.

The closed conditional Gaussian kernel from the companion theory report is also retained; no nested Gaussian integral is needed.

## 2. Attack A — falsify the naive whole-box interval route

The preceding R14 report proposed direct interval enclosure of the four entries of

`DF=[[H_p,H_B],[alpha_p,alpha_B]]`

on the weighted box around

`p_c=0.645767064689`, `B_c=4.9292292009`.

I implemented an outward interval-Simpson prototype for the closed one-dimensional Gaussian formulas. At the **single center point**, on `|z|<=9`, with Simpson step `0.0125` and a fourth-derivative remainder enclosure, it returned the compact enclosures

`H in [-8.31900404e-7, 8.31901849e-7]`,

`alpha in [12.74998595516,12.75001404485]`,

`Psi in [0.01519909607,0.01520289087]`,

`H_p in [-0.02581892329,-0.02560675743]`,

`H_B in [0.000435785389,0.000440026977]`,

`alpha_p in [26.83396764,26.83740113]`,

`alpha_B in [-0.888916790,-0.888847730]`.

The earlier companion checker gives exact full-tail value bounds outside `|z|<=9`:

`|tail(I)| <= (85/9)(10/27)^40 < 5.26e-17`,

`|tail(I_B)| <= 19(10/27)^40 < 1.06e-16`,

`tail(K) <= 19000(10/27)^40 < 1.06e-13`.

Inflating the **value** integrals by those exact tail bounds leaves

`H in [-8.31902147e-7,8.31903592e-7]`,

`alpha in [12.74998595513,12.75001404488]`,

`Psi in [0.015199096066,0.015202890869]`.

These are self-checks of the center computation, not an endpoint certificate. In particular, the tail derivatives needed for a full-line Jacobian enclosure were not claimed from the old value-tail estimate.

The important negative result is methodological: applying ordinary rectangular interval arithmetic directly to `(p,B)` over the preceding product box causes the algebraic reconstruction `K/(-4p^2B^2I_B)`, followed by `D,c,alpha,H`, to wrap catastrophically. The same dependency inflation remained visible after shrinking to approximately `|p-p_c|<=1e-4`, `|B-B_c|<=0.004`. Thus the missing proof is **not** merely “use more quadrature nodes.” A centered form that remembers parameter correlations is required.

This is the explicit third-unchanged-run obstruction: naive product intervals destroy the cancellation that makes the two-scalar reduction well-conditioned.

## 3. Attack B — a centered-Hessian contraction theorem

The remedy is to enclose `DF` through point derivatives plus Hessian bounds, rather than reevaluate the full nonlinear reconstruction on one product interval.

Let

`F(p,B)=(H(p,B),alpha(p,B)-12.75)`.

Keep the rational preconditioner

`A=[[-1601/20,-493/12500],[-60418/25,-5789/2500]]`.

Use the smaller weighted box

`Q={|p-p_c|<=1/2000, |B-B_c|<=1/50}`.

### Lemma R14-T03-CENTERED-HESSIAN

Assume `F` is `C^2` on `Q`. Suppose at the center

`H_p in [-259/10000,-255/10000]`,

`H_B in [43/100000,45/100000]`,

`alpha_p in [134/5,269/10]`,

`alpha_B in [-9/10,-22/25]`,

and throughout `Q`

`|H_pp|<=1/5`, `|H_pB|<=1/100`, `|H_BB|<=1/1000`,

`|alpha_pp|<=70`, `|alpha_pB|<=4`, `|alpha_BB|<=1/2`.

Then throughout `Q`

`H_p in [-131/5000,-63/2500]`,

`H_B in [81/200000,19/40000]`,

`alpha_p in [5337/200,5403/200]`,

`alpha_B in [-114/125,-217/250]`.

If also

`|H(p_c,B_c)|<=10^-6`,

`|alpha(p_c,B_c)-12.75|<=2*10^-5`,

then `F` has a unique zero in `Q`.

#### Proof

The first four claims are the mean-value theorem. For example,

`|H_p(p,B)-H_p(p_c,B_c)|`
`<= (1/5)(1/2000)+(1/100)(1/50)=3/10000`,

and similarly for the other three entries.

Let `D0=diag(1/2000,1/50)`. For the resulting rational Jacobian box, every entry of

`D0^{-1}(I-AJ)D0`

is affine in the four interval variables. The induced infinity norm is convex, so its maximum is attained at a box vertex. Exact enumeration of the 16 vertices gives

`q <= 62439/312500 = 0.1998048`.

The worst vertex is

`(-63/2500,19/40000,5403/200,-217/250)`.

The center residual assumption gives exactly

`eta=||D0^{-1}AF(p_c,B_c)||_infinity`
`<=202097/1250000=0.1616776`.

Since

`eta < 1-q = 250061/312500 = 0.8001952`,

the map `x -> x-AF(x)` maps `Q` strictly into itself and is a contraction. Banach's theorem yields a unique fixed point, hence a unique zero of `F` because `A` is invertible. QED.

The gain is quantitative: instead of a direct full-box interval extension of the reconstructed formulas, it is enough to certify four point derivatives and six deliberately loose second-derivative bounds.

### Comparison-value positivity on the same box

Assume in addition

`Psi(p_c,B_c)>=7/500`,

`|Psi_p(p_c,B_c)|<=1`, `|Psi_B(p_c,B_c)|<=1/25`,

and on `Q`

`|Psi_pp|<=2`, `|Psi_pB|<=1/5`, `|Psi_BB|<=1/20`.

Taylor's theorem gives, everywhere on `Q`,

`Psi >= 7/500 - 1/2000 - (1/25)(1/50)`
`       - (1/2)[2(1/2000)^2 + 2(1/5)(1/2000)(1/50) + (1/20)(1/50)^2]`
`     = 50751/4000000`
`     = 0.01268775 >0`.

Therefore the centered-Hessian hypotheses plus the already source-matched complete-second-lift implication would rigorously certify UNSAT at `alpha=12.75`.

**The endpoint is not promoted here:** the six Hessian bounds and the full-line point-derivative enclosures have not yet been proved.

### Numerical-only falsification of the proposed Hessian windows

A separate `260`-node Gauss--Hermite finite-difference scout on a `7 x 7` grid over `Q` produced

`H_pp in [0.11969,0.12027]`,

`H_pB in [-0.00644,-0.00641]`,

`H_BB in [9.27e-5,9.46e-5]`,

`alpha_pp in [56.93,58.05]`,

`alpha_pB in [-2.87,-2.79]`,

`alpha_BB in [0.353,0.364]`,

`Psi_pp in [1.046,1.079]`,

`Psi_pB in [-0.0805,-0.0788]`,

`Psi_BB in [0.0120,0.0124]`.

All lie comfortably within the rational hypotheses above. These are **NUMERICAL_ONLY** diagnostics, not proofs of those bounds.

## 4. Attack C — deform the complete second lift to `B=0`

This is a genuinely different analytical route: instead of certifying the interior `alpha=12.75` root, identify the exact boundary condition from which a complete second-lift branch could bifurcate.

Let

`u(x)=(x-1)_+`,

`Y=sqrt(p)Z+sqrt(1-p)H`,

`r_p(Z)=E[u(Y)|Z]=T_{sqrt(p)}u(Z)`,

and

`mu_1=E[u(G)^2]`.

### Lemma R14-T03-B0-BOUNDARY

Fix `p in (0,1)`. As `B downarrow 0`,

`I_B(p,B) -> -mu_1`,

`K(p,B)/B^2 -> 4p E[r_p(Z)^2]`.

Consequently, any complete-second-lift stationary branch for which

`B->0`, `p->p_0 in (0,1)`, and `D->1`

must satisfy the scalar boundary equation

`E[r_{p_0}(Z)^2]=p_0 mu_1`.                                           (B0)

Moreover `(B0)` has exactly one solution in the open interval `(0,1)`; `p=1` is the separate endpoint solution.

#### Proof of the limits

Condition on `Z=z` and put `V=u(Y)^2`. Since all conditional polynomial moments are Gaussian-integrable,

`E[e^{-BV}|Z=z]=1-B E[V|Z=z]+O(B^2 E[V^2|Z=z])`

with domination sufficient to integrate the expansion and its first `z` derivative. Thus

`I_B(p,B) -> -E V=-mu_1`.

If `m_p(z)=E[V|Z=z]`, then

`partial_z log f_{p,B}(z)=-B m_p'(z)+O(B^2)` in `L^2(dgamma)`.

Differentiating the shifted Gaussian expectation gives

`m_p'(z)=2 sqrt(p) E[u(Y)|Z=z]=2sqrt(p) r_p(z)`.

Hence

`K/B^2 -> E[m_p'(Z)^2]=4pE[r_p(Z)^2]`.

Substituting these limits into the exact reconstruction

`D^2=K/[-4p^2B^2I_B]`

gives

`D^2 -> E[r_p^2]/(p mu_1)`.

Therefore `D->1` forces `(B0)`.

#### Proof of uniqueness of the interior boundary point

Expand `u` in probabilists' Hermites and put

`s_k=(E[u(G)He_k(G)])^2/k! >=0`.

The OU spectral identity gives

`E[r_p(Z)^2]=sum_{k>=0}s_k p^k`,

while

`mu_1=sum_{k>=0}s_k`.

For `0<=p<1`,

`[E r_p^2-p mu_1]/(1-p)`
`=s_0-sum_{k>=2}s_k p(1+p+...+p^{k-2})`.                              (U)

The right side is strictly decreasing because `u` is not affine. At `p=0` it equals `s_0>0`.

As `p↑1`, Gaussian Sobolev/Parseval gives

`sum k s_k=E[u'(G)^2]=P(G>1)=barPhi(1)`,

so the limit of `(U)` is

`mu_1-barPhi(1)`.

For `u=(x-1)_+`, direct truncated-normal integration gives

`mu_1=2barPhi(1)-phi(1)`,

hence

`mu_1-barPhi(1)=barPhi(1)-phi(1)<0`

by the strict Mills inequality `barPhi(1)<phi(1)`. Continuity and strict monotonicity therefore give exactly one zero in `(0,1)`. QED.

A numerical-only `300`-node Gauss--Hermite scout places this boundary point at

`p_* ~= 0.1526513489316`.

That number is not used as a rigorous endpoint or parameter certificate. The analytical value of the lemma is that a perturbative complete-lift continuation from `B=0` is no longer an unconstrained two-parameter search: any interior branch with `D->1` must emanate from the unique scalar OU balance `(B0)`. Whether that boundary branch connects to the source-relevant interior `p~=0.646` branch is still unproved.

## 5. Exact self-check

`20260920T0220Z_r14_centered_hessian_boundary_checker.py` verifies the rational contraction compiler and the rational `Psi` Taylor lower bound exactly with `fractions.Fraction`. Its archived output ends `ALL_SELF_CHECKS_PASS`.

The same executable reports the `B=0` root only under a `NUMERICAL_ONLY` label.

Self-checks are not independent audits.

## 6. What changed and what did not

### Source metric

Before:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

After:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

**No source-level movement.**

### Mechanism movement

1. The naive whole-product-interval version of the `12.75` certificate has a concrete dependency/wrapping obstruction; merely refining quadrature is not the right next action.
2. A complete centered-Hessian theorem replaces that failed obligation by point derivative/residual bounds plus six coarse Hessian bounds, with exact contraction margin
   `0.8001952-0.1616776=0.6385176`.
3. A distinct `B->0` deformation theorem identifies a unique interior OU boundary balance from which any `D->1` second-full branch must start.

## 7. Remaining full-scope gap

The fastest source-moving route now appears to be a **centered Taylor model in `(p,B)`** for the closed one-dimensional Gaussian kernel, not raw interval substitution. To promote `alpha_U=12.75`, one still must prove the point/full-tail derivative bounds and the six Hessian inequalities in Lemma R14-T03-CENTERED-HESSIAN, verify the reconstructed branch stays interior, and then invoke the complete source theorem with `Psi>0`.

The deformation route is independent backup: derive the first nonzero `B` coefficient at the unique boundary solution and determine whether it produces a branch whose `alpha` decreases below the certified partial-lift endpoint. No such connection is claimed here.

Status remains **OPEN / PARTIAL**.
