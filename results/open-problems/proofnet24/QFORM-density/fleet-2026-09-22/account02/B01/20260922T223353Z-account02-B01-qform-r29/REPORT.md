# QFORM account02/B01 r29 — two-slope zero-pair closure and the nonzero-edge discontinuity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T223353Z-account02-B01-qform-r29`  
Assignment: `Oscillatory replacement`  
Status: `ESSENTIAL_STEP_APPLIED / EXPLICIT_INTERMEDIATE_FALSIFIER / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Target and source boundary

The target is unchanged: for every `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a target-valid counterexample.

Fresh startup control was `yspennstate/math-research-brain@82521c4e42d1f353c9ee1aaa5e4b61d7097ad8f3`; the prepublication refresh was `3f72c7506277515478cac4df56974a31e9f829e1`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no B01 stop. The live corrections consumed include the false law-uniform pointwise Fresnel decay, false post-rotation independence, false arbitrary-joint rank-three coarea estimate, false positive conditional-projection-height moment, and the existing fixed-minor/fiber-supremum obstructions.

The mandatory phase-aligned-density refutation remains in force: for any nonzero `s` and small `delta`, a cap-one density supported on a measure-one subset of `{x:dist(sx^2,2pi Z)<=delta}` has `Re E exp(i sX^2)>=cos(delta)`. Nothing below uses pointwise `|s|^{-1/2}` decay.

The named partner actually used is account03/B01 r18, canonical source

`yspennstate/math-open-problems@7acff3e983f6e6a3ede04ecbaf8405a3ce4ee8e2:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T202731Z-r18/REPORT.md`.

Its theorem used below is: if `X` is independent of `(U,R)`, `f_X<=1`, and `||p_U||_infinity<=M`, then for every finite `p>1`,

`||p_(2XU+R)||_p <= p M^(1-1/p)`.                         (1.1)

In particular at `p=3`, with `M=1`, the bound is `3`. The partner also proves that one zero bilinear row alone necessarily has an `ell log(1/ell)` small-ball / `log T` signed-Fejer loss. The new theorem below shows exactly how a second *jointly anti-concentrated* slope kills that logarithm without normalizing a conditional density.

## 2. New theorem: two zero physical rows give a bounded density

### Theorem 2.1 — `QFORM-ZERO-PAIR-TWO-SLOPE-LINF-v1`

Let `X,Y` be independent real random variables with probability densities bounded by `L_X,L_Y`, respectively. Let `(U,V,R)` be an arbitrary random vector independent of `(X,Y)`. No independence between `U,V,R` is assumed. Suppose `(U,V)` has a joint density `rho` with

`||rho||_infinity <= M < infinity`.                           (2.1)

Put

`T=2XU+2YV+R`.                                                 (2.2)

Then for every interval `I`,

`P(T in I) <= 2 sqrt(M L_X L_Y) |I|`,                         (2.3)

and hence `T` has a density satisfying

`boxed: ||p_T||_infinity <= 2 sqrt(M L_X L_Y).`               (2.4)

The result is distributional; it does not take absolute values of a pointwise quadratic-phase transform and does not require a conditional density cap for `U|V` or `V|U`.

### Proof

Condition on `(U,V,R)=(u,v,r)`. For `u,v` not both zero, `2uX+2vY+r` is a convolution of two scaled input laws. Therefore its conditional density has essential supremum at most

`k(u,v)=min( L_X/(2|u|), L_Y/(2|v|) )`,                      (2.5)

with the usual `+infinity` interpretation when one denominator is zero. Since `(U,V)` has a density, the point `(0,0)` has zero probability.

Thus for an interval `I` of length `ell`,

`P(T in I) <= ell int rho(u,v) k(u,v) du dv`.                 (2.6)

For `lambda>0`, the Lebesgue area of the superlevel set is exactly

`|{(u,v): k(u,v)>lambda}|`
` = (L_X L_Y)/lambda^2`.                                      (2.7)

Hence, under a probability density bounded by `M`,

`P_rho(k>lambda) <= min(1, M L_X L_Y/lambda^2)`.              (2.8)

Layer cake gives

`int rho k`
` <= int_0^infinity min(1, M L_X L_Y/lambda^2) dlambda`
` = 2 sqrt(M L_X L_Y)`.                                      (2.9)

This proves (2.3). An interval domination `mu(I)<=C|I|` extends to open sets by countable disjoint interval decomposition and then to Borel sets by regularity, so the law is absolutely continuous with Radon--Nikodym derivative at most `C`. This proves (2.4). QED.

### Why this is the correct replacement for the one-row logarithm

The account03/B01 r18 theorem shows that one exact-zero row has the sharp product example `2XU` with a logarithmically unbounded density. Theorem 2.1 spends a second physical coordinate *before any conditional normalization*: the relevant singular kernel is `1/max(|u|,|v|)`, which is locally integrable in two dimensions. Thus the logarithm disappears for geometric, not pointwise-Fourier, reasons.

Equivalently, using the already-proved signed-Fejer interface, (2.4) implies

`sup_(T0>0,y) D_(T0) law(T)(y) <= 2 sqrt(M L_X L_Y)`.         (2.10)

So the second slope upgrades the partner's unavoidable one-row `log T` growth to a uniform averaged-frequency bound.

## 3. Full-matrix physical certificate

### Corollary 3.1 — `QFORM-ZERO-PHYSICAL-PAIR-CROSSMINOR-v1`

Let `Q=X^T A X` under the full product-density hypotheses. Suppose four distinct original-coordinate indices `i,j,k,l` satisfy

`A_ii=A_jj=A_ij=0`                                            (3.1)

and

`Delta = |A_ik A_jl - A_il A_jk| > 0`.                        (3.2)

Then, with every other coefficient and coupling of `A` arbitrary,

`boxed: ||p_Q||_infinity <= 2 Delta^(-1/2).`                  (3.3)

### Proof

Write

`U=sum_(r notin {i,j}) A_ir X_r`,
`V=sum_(r notin {i,j}) A_jr X_r`,                             (3.4)

and put all remaining terms into `R`. Because the physical `2x2` pair in (3.1) is zero,

`Q=2X_i U+2X_j V+R`,                                         (3.5)

and `(X_i,X_j)` is independent of `(U,V,R)`.

Condition on all outside coordinates except `X_k,X_l`. The map `(X_k,X_l)->(U,V)` is affine with Jacobian determinant of magnitude `Delta`. Since the source density of `(X_k,X_l)` is at most one, the conditional density of `(U,V)` is at most `Delta^(-1)`. Averaging over the other outside coordinates preserves that cap. Theorem 2.1 with `L_X=L_Y=1` and `M=Delta^(-1)` gives (3.3). QED.

This is an ambient full-matrix theorem. It does not require the residual matrix to split, have small norm, have fixed rank, or be independent of `(U,V)`.

## 4. The exponent `Delta^(-1/2)` is the natural local scaling

Let `m>=1`, set `alpha=m^(-1/2)`, and take four independent cap-one inputs. Consider

`Q_m=2 alpha (X_1 X_3+X_2 X_4)`.                              (4.1)

The selected zero pair is `(1,2)` and its transverse minor is `Delta=alpha^2=1/m`; the joint slope density cap is `M=m`. Scaling gives

`Q_m=alpha Q_1`,                                              (4.2)

so `||p_(Q_m)||_infinity=alpha^(-1)||p_(Q_1)||_infinity` whenever the latter is finite.

To verify finiteness using the named partner rather than a new duplicate argument, apply account03/B01 r18 at `p=2` separately to `2X_1X_3` and `2X_2X_4`; each density has `L^2` norm at most `2`, and the two terms are independent. Young/Cauchy--Schwarz then gives `||p_(Q_1)||_infinity<=4`. Also `p_(Q_1)(0)>0` because it is the integral of the product of two nonzero symmetric `L^2` densities. Therefore the `sqrt(M)=Delta^(-1/2)` dependence in Theorem 2.1 / Corollary 3.1 cannot in general be improved to a smaller power using only this local gate currency.

## 5. Exact falsifier: any nonzero mutual edge destroys the two-slope theorem

The zero-pair hypothesis is not perturbatively removable under the same assumptions.

Fix `0<epsilon<=1/2` and take iid

`X_1,X_2,X_3,X_4 ~ Uniform[-1/2,1/2]`.                        (5.1)

Define

`Q_epsilon`
` =2 epsilon X_1X_2+2X_1X_3+2X_2X_4+2 epsilon^(-1)X_3X_4`
` =2 (X_1+X_4/epsilon)(epsilon X_2+X_3)`.                    (5.2)

For the physical pair `(1,2)`, both diagonals are still zero, the mutual edge is only `A_12=epsilon`, and the two outside slopes are exactly

`U=X_3`, `V=X_4`,                                             (5.3)

so their joint density cap is `M=1` and the same transverse minor is

`Delta=|A_13 A_24-A_14 A_23|=1`.                             (5.4)

Nevertheless `Q_epsilon` has an unbounded density.

Indeed set

`A=X_1+X_4/epsilon`, `B=epsilon X_2+X_3`.                     (5.5)

The variables `A,B` are independent. For `epsilon<=1/2`, the density `h_A` equals `epsilon` on `[-1/2,1/2]`, while `h_B` equals `1` on `[-1/4,1/4]`. Therefore, for `0<|t|<1/8`, the product-density formula and restriction to `a in [2|t|,1/2]` give

`p_(Q_epsilon)(t)`
` >= int_(2|t|)^(1/2) epsilon * 1 * (da/(2a))`
` = (epsilon/2) log(1/(4|t|)) -> infinity`.                  (5.6)

Thus there is no theorem of the form `||p_Q||_infinity<=F(M,Delta)` obtained by merely allowing an arbitrary nonzero `A_ij` while keeping the exact same two-slope hypotheses. The obstruction persists for arbitrarily small `epsilon`, with `M=Delta=1` fixed; a compensating residual coupling `A_34=epsilon^(-1)` aligns the rank-two product singularity.

The matrix in (5.2) has only two nonzero eigenvalues. Reorder the variables into the two independent groups `{1,4}` and `{2,3}`. The cross block is

`C_epsilon=[[epsilon,1],[1,epsilon^(-1)]]`,                  (5.7)

which has rank one and unique singular value `epsilon+epsilon^(-1)`. Hence the spectrum is

`{epsilon+epsilon^(-1), -(epsilon+epsilon^(-1)), 0,0}`.      (5.8)

So (5.2) is **not** a counterexample to QFORM. It is a sharp source-valid falsifier of the tempting near-zero-edge continuation, and it identifies exactly where a third spectral direction must be spent.

## 6. Applying the partner result: a third square uniformly cures the falsifier family

The preceding rank-two logarithm becomes a target-valid, uniformly bounded family as soon as an independent third large square is added.

### Theorem 6.1 — `QFORM-ALIGNED-PRODUCT-PLUS-THIRD-SQUARE-v1`

Let `0<epsilon<=1`, `|d|>=1`, and let `X_1,...,X_5` be **arbitrary independent** real random variables with densities bounded by one. Put

`T_epsilon`
` =2 epsilon X_1X_2+2X_1X_3+2X_2X_4+2 epsilon^(-1)X_3X_4+dX_5^2`. (6.1)

Then

`boxed: ||p_(T_epsilon)||_infinity`
` <= 2^(7/2) epsilon^(1/2) |d|^(-1/2)`
` <= 2^(7/2) < 11.314.`                                      (6.2)

The coefficient matrix has eigenvalues

`{epsilon+epsilon^(-1), -(epsilon+epsilon^(-1)), d,0,0}`,     (6.3)

so this is a genuine full-target subfamily with three eigenvalues of modulus at least one.

### Proof

Define the disjoint-bank aggregates

`A'=epsilon X_1+X_4`, `B'=epsilon X_2+X_3`.                   (6.4)

They are independent. Each has density cap at most one, because convolution with the unscaled cap-one coordinate `X_4` or `X_3` cannot increase the `L^infinity` norm. The rank-two part factors as

`Q_epsilon=(2/epsilon) A'B'`.                                (6.5)

Set `S=2A'B'`. Apply the named partner account03/B01 r18 theorem (1.1) with `X=A'`, `U=B'`, `R=0`, `M=1`, and `p=3`:

`||p_S||_3 <=3`.                                              (6.6)

For `Z=epsilon^(-1)S`, scaling gives

`||p_Z||_3 <=3 epsilon^(2/3)`.                               (6.7)

It remains to average the logarithmic rank-two law against the third square. For any probability density `p` with `||p||_3=N`, Holder on `|x|<=r` and probability mass on `|x|>r` give

`int p(t-x)|x|^(-1/2) dx`
` <=4N r^(1/6)+r^(-1/2)`.                                    (6.8)

Optimizing at `r^(1/6)=(3/(4N))^(1/4)` yields the elementary half-Riesz estimate

`sup_t int p(t-x)|x|^(-1/2) dx`
` <=2^(7/2) 3^(-3/4) N^(3/4)`.                              (6.9)

The density of `dX_5^2` is bounded by

`|d|^(-1/2)|y|^(-1/2)` on its sign half-line.                 (6.10)

Convolution of (6.7) with (6.10), followed by (6.9), therefore gives

`||p_(T_epsilon)||_infinity`
` <= |d|^(-1/2) 2^(7/2) 3^(-3/4)
      (3 epsilon^(2/3))^(3/4)`
` = 2^(7/2) epsilon^(1/2)|d|^(-1/2)`.                        (6.11)

This proves (6.2). The spectrum statement follows from (5.7): the rank-one cross block has singular value `epsilon+epsilon^(-1)`, and the independent fifth coordinate contributes eigenvalue `d`. QED.

### Interpretation

The same aligned product that defeats every bounded-density claim with only two large eigenvalues is uniformly regularized by one independent physical square. This is an exact, source-valid model of the programme's `why three` principle: the third gate is spent *after* the rank-two logarithm is retained, not by pretending the logarithm never formed.

## 7. What is paid and what remains unpaid

Paid in this run:

1. a new dependence-safe, unnormalized two-slope theorem that turns two exact zero physical rows into a true `L^infinity` density bound;
2. an ambient full-matrix cross-minor certificate `2 Delta^(-1/2)` with arbitrary residual couplings;
3. a sharp construction showing the exact-zero condition is discontinuous: any nonzero mutual edge can recover the rank-two logarithm while leaving the two-slope cap and transverse minor fixed;
4. a direct quantitative application of account03/B01 r18 showing that an independent third square uniformly cures this aligned-log family under all target input quantifiers.

First unpaid implication after this run:

`QFORM-THIRD-DIRECTION-BEFORE-NONZERO-EDGE-v1`.

In the general near-singular physical-pair / three-bank overlap branch, one cannot first perturb the zero-pair theorem across `A_ij!=0` using only a two-slope density cap: family (5.2) forbids it. The next universal step must identify and spend a *genuine third spectral/product-preserving resource* before the compensating residual coupling can align the product singularity. Equivalently, the three-bank overlap synthesis needs a quantitative third-direction currency of the **total** matrix, not only a fixed transverse `2x2` slope minor.

This is consistent with the r27 leakage-safe overlap identity and the r18 one-row logarithmic endpoint. It changes the mechanism from `improve the two-row gate perturbatively` to `insert the third gate before the nonzero-edge product singularity` while keeping the full QFORM target unchanged.

Full QFORM remains OPEN. No full-proof claim is made, and two end-to-end reviews do not exist.
