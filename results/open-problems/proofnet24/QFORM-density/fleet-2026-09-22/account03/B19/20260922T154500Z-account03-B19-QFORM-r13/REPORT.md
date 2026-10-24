# account03/B19 — Schur critical-value splice for the one-effective-direction residue

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T154500Z-account03-B19-QFORM-r13`  
**Assignment:** Universal proof assembly  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCHES_PROVED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and inputs

The target remains the unrestricted statement: for arbitrary dimension, arbitrary independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `Q=X^T A X`, or give a target-valid counterexample. Continuity is separate and is **not** proved by the new splice below.

The live correction inbox was respected. No law-uniform scalar Fresnel decay, independence after a spectral rotation, conditional density cap after an aggregate rotation, fiber-supremum closure, or fixed local-minor dichotomy is used.

The previous B19 result, source-pinned at

`yspennstate/math-open-problems@143e97c42cdbccb14fe847efb6abd3f6c3d349dc`

left the one-effective-direction branch with two physical coordinates `p,q` whose diagonal entries have opposite signs and magnitude at least `7/8`, and an outside unit vector `w` with `max_i w_i^2<7/27`, such that the **actual full-matrix compression** to `span(e_p,e_q,w)` has

` s_min > delta_0 := 9/280. `                                                   (1.1)

This run attacks the previously unpaid product-preserving use of (1.1).

The designated partner `account04/B19` completed `QFORM-FINITE-UNION-CORE-v1`, canonical

`yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`.

It proves that the interval-concentration supremum over all independent cap-one densities equals the supremum over bounded finite-union product indicators of measure one. I use it as an actual final transfer: the interval inequalities proved below may be verified on that finite-union core, and then the same constant holds for the full arbitrary-density class. The derivation in fact works directly for arbitrary cap-one factors as well.

## 2. A sharp-enough quarter-kernel for an indefinite physical pivot pair

Let `X,Y` be independent with densities at most one, and let

`B=[[a,c],[c,-b]]`, with `a,b>0`,

`Delta=ab+c^2=|det B|`.

Translations of `X,Y` preserve independence and the density caps. Therefore arbitrary affine terms may be removed by completing the square.

### Lemma 2.1 — indefinite binary quarter-kernel

The quadratic variable

`R=aX^2+2cXY-bY^2`

has a density `h` satisfying, for almost every `s!=0`,

- if `s>0`, `h(s) <= 2 Delta^(-1/4) b^(-1/4) s^(-1/4)`;
- if `s<0`, `h(s) <= 2 Delta^(-1/4) a^(-1/4) |s|^(-1/4)`.

In particular, if `a,b>=m>0`,

` h(s) <= 2 Delta^(-1/4) m^(-1/4) |s|^(-1/4). `                    (2.1)

#### Proof

For `s>0`, complete in `Y`:

`R=(Delta/b)X^2-b(Y-(c/b)X)^2`.

Conditioned on `X=x`, the shifted variable `Y-(c/b)x` still has density cap one. The density of `-bZ^2` at a negative argument `-u` is at most `1/sqrt(bu)`. Hence, with `alpha=Delta/b`,

`h(s) <= b^(-1/2) integral_{alpha x^2>s} f_X(x)(alpha x^2-s)^(-1/2) dx`.

Put `r=sqrt(s/alpha)`. Since

`x^2-r^2 >= 2r(|x|-r)` on `|x|>r`,

and a cap-one density of mass `m_+` on `(r,infinity)` maximizes the decreasing kernel `(x-r)^(-1/2)` by filling the interval adjacent to `r`,

`integral_r^infinity f_X(x)(x-r)^(-1/2)dx <=2 sqrt(m_+)`.

The analogous left-hand mass is `m_-`; `sqrt(m_+)+sqrt(m_-)<=sqrt(2)` because `m_++m_-<=1`. Therefore

`integral_{|x|>r} f_X(x)(x^2-r^2)^(-1/2)dx <=2 r^(-1/2)`.

Substitution gives

`h(s)<=2 b^(-1/2) alpha^(-1/2) r^(-1/2)
     =2 Delta^(-1/4)b^(-1/4)s^(-1/4)`.

For `s<0`, complete instead in `X`:

`R=a(X+(c/a)Y)^2-(Delta/a)Y^2`,

and repeat the same argument with `a,b` interchanged. QED.

The exponent `1/4` is exactly the useful feature: the opposite-sign two-pivot logarithmic singularity is not falsely declared bounded, but a square-root-small-ball third mechanism is enough to integrate it.

## 3. Critical-value splice

Partition the original coordinates into the physical pivot pair `U=(X_p,X_q)` and the remaining original coordinates `Z`. Write the exact matrix block decomposition

`A=[[B,K],[K^T,C]]`,

where in the live branch, after a possible global sign change,

`B=[[a,c],[c,-b]]`, `a,b>=m:=7/8`, and `Delta=ab+c^2>=m^2`.

Since `B` is invertible, define its exact Schur complement

`S=C-K^T B^(-1)K`,                                                        (3.1)

and the **critical-value quadratic form**

`kappa(Z)=Z^T S Z`.

For each fixed `Z=z`, completing the square only in the two original pivot coordinates gives

`Q=(U+B^(-1)Kz)^T B (U+B^(-1)Kz)+kappa(z)`.                         (3.2)

The two shifts in (3.2) are deterministic after conditioning on `z`, so the original `X_p,X_q` remain independent with their original cap-one densities. This avoids every prohibited post-rotation conditional-cap step.

### Theorem 3.1 — `QFORM-CRITICAL-VALUE-QUARTER-SPLICE-v1`

Assume that for some `L<infinity`, uniformly in `t` and `0<r<=1`,

`P(|kappa(Z)-t|<=r) <= L sqrt(r).`                                      (3.3)

Then `Q` has an essentially bounded density and

` ||p_Q||_infinity <= 4 Delta^(-1/4)m^(-1/4) max(1,sqrt(L)). `        (3.4)

#### Proof

By Lemma 2.1 applied conditionally in (3.2), a version of the mixture density satisfies

`p_Q(t) <= 2 Delta^(-1/4)m^(-1/4) E|t-kappa(Z)|^(-1/4).`             (3.5)

Let `D=|t-kappa(Z)|`. Layer cake and (3.3) give

`E D^(-1/4)
 = integral_0^infinity P(D<u^(-4))du
 <=1+integral_1^infinity min(1,L u^(-2))du
 <=2 max(1,sqrt(L)).`

Insert this into (3.5). QED.

Thus the previous mixed coordinate/aggregate problem is converted to a precise product-law obligation on the exact Schur critical value, not on a biased or rotated conditional law.

## 4. The `9/280` compression forces a nontrivial Schur critical value

Let `w` be the outside unit vector from the previous B19 normal form, and compress `A` to `span(e_p,e_q,w)`:

`M=[[B,Kw],[w^T K^T,w^T C w]].`

Its scalar Schur complement with respect to `B` is exactly

`sigma=w^T S w`.                                                          (4.1)

Because `s_min(M)>delta_0=9/280`, the block inverse formula gives

`(M^(-1))_33 = sigma^(-1)`

and therefore

` |sigma| > delta_0. `                                                     (4.2)

This is the first direct transfer from the mixed compression to an exact outside quadratic resource.

## 5. A physical Schur diagonal closes the full branch

### Lemma 5.1 — quadratic one-coordinate concentration

If a one-dimensional cap-one random variable `T` enters a conditional quadratic as

`d T^2+ell T+c`, with `|d|>=eta>0`, then for every center `s` and radius `r>0`,

`P(|dT^2+ell T+c-s|<=r) <= 2 sqrt(2/eta) sqrt(r).`                    (5.1)

Indeed, complete the square. The inverse image of an interval of length `2r` under `d x^2` has total Lebesgue length at most `2 sqrt(2r/|d|)`.

Apply this to `kappa=Z^T S Z`, conditioning every outside coordinate except `Z_i`. If

` |S_ii| >= eta := delta_0/4 = 9/1120, `                               (5.2)

then (3.3) holds with

`L_diag=2 sqrt(2/eta)=2 sqrt(2240/9)<31.553`.                           (5.3)

Since `Delta>=m^2`, (3.4) gives the explicit target-level bound

` ||p_Q||_infinity
 <=4 m^(-3/4) sqrt(L_diag)
 <24.836 <25. `                                                         (5.4)

This statement allows arbitrary signs, arbitrary remaining dimensions, arbitrary outside couplings and arbitrary cap-one input laws. Continuity is not asserted.

By the designated partner `QFORM-FINITE-UNION-CORE-v1`, the same interval inequality (and hence the same `<25` constant) transfers without loss from the finite-union testing core to the entire admissible product-density class. This is the designated-partner result applied to an actual inequality in this run.

## 6. If no Schur diagonal pays, a quantitative original-coordinate cross resource is forced

Assume now that every outside physical diagonal satisfies

`|S_ii|<delta_0/4`.

Write `O=S-diag(S)`. Since `||w||=1`, (4.2) gives

`|w^T O w| > delta_0-delta_0/4 = 3delta_0/4.`                          (6.1)

Choose a random bipartition `T=I disjoint_union J`, independently assigning each index to either side with probability `1/2`. For

`Y(I,J)=2 w_I^T S[I,J] w_J`,

symmetry and zero diagonal give

`E Y = (1/2) w^T O w`.

Hence some deterministic partition satisfies

`|w_I^T S[I,J]w_J| >= |w^TOw|/4 > 3delta_0/16`.                       (6.2)

Since `||w_I|| ||w_J||<=1/2`, (6.2) implies

`boxed( s_1(S[I,J]) > 3delta_0/8 = 27/2240. )`                        (6.3)

The sets `I,J` are disjoint sets of **original** coordinates. Thus no rotated independence is being claimed. Equation (6.3) is an unconditional, dimension-free cross-bank resource forced by the previous `9/280` mixed compression whenever the physical-Schur-diagonal branch does not already close.

This is strictly stronger information than the previous run had: the one-effective-direction residue cannot hide all of its third curvature inside the mixed spectral direction. It must become either a physical Schur curvature coefficient or a quantitatively nonzero original-coordinate Schur cross bank.

## 7. Applying the new ridge theorem to the forced Schur bank

The fresh supporting result `QFORM-RIDGE-DENSITY-v1`, source-pinned at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

applies directly to the exact outside quadratic `kappa=Z^T S Z`: for any disjoint original-coordinate cut `I,J`, put `B_S=S[I,J]`, choose `gamma>0`, and define

`K_gamma=B_S B_S^T(gamma^2 I+B_S B_S^T)^(-1)`,
`theta=tr K_gamma`.

If for some `1<=q<=2`,

`max_i (K_gamma)_ii<=q/2`, `theta>2q`,                                 (7.1)

then `kappa` itself has a bounded continuous density with the explicit ridge bound from that theorem. In particular, if the bound is `M_kappa`, then

`P(|kappa-t|<=r)<=2M_kappa r<=2M_kappa sqrt(r)` for `r<=1`,

so Theorem 3.1 closes `Q` with `L=2M_kappa`.

Therefore the live one-effective branch is now reduced further: if (5.2) fails, a cut satisfying (6.3) exists; if any such cut also satisfies a ridge certificate (7.1), the full branch is paid. The remaining residue must be **low ridge-effective-dimension / high leverage** despite possessing the fixed cross singular resource (6.3).

I do not claim the ridge condition is automatic; the owner controls explicitly record the singleton-plus-two-banks obstruction to a ridge-only proof.

## 8. Exact diffuse-rank-one Schur critical values are completely paid

There is one important endpoint of the low-ridge residue that can already be closed.

Assume, in addition to the live one-effective setup, that the exact Schur complement has the form

`S=D+mu w w^T`,                                                         (8.1)

with `D` diagonal and the same outside unit vector `w`, for which `max_i w_i^2<7/27<1/2`.

### Theorem 8.1 — `QFORM-DIFFUSE-RANK1-SCHUR-SPLICE-v1`

Under (8.1), the full quadratic form `Q` has a universally bounded density. More explicitly, the bound obtained below is `<36`.

#### Proof

From (4.2),

`|mu + sum_i D_ii w_i^2|=|w^T S w|>delta_0`.

If `|mu|<delta_0/2`, then

`|sum_i D_ii w_i^2|>delta_0/2`,

so some `|D_ii|>delta_0/2`. For that index,

`|S_ii|=|D_ii+mu w_i^2|
 > delta_0/2-(delta_0/2)(7/27)
 =10delta_0/27
 >delta_0/4`.

Thus Section 5 closes this case with `<25`.

Assume instead `|mu|>=delta_0/2`. The already-reviewed diffuse-separable-phase proof at

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`

has, before its `r>2` time-integration step, the valid rank-one characteristic estimate for arbitrary coordinate-separable phases:

`|phi_kappa(t)| <= min(1, K |t|^(-1/2))`,
`K <= sqrt(e pi) |mu|^(-1/2)`.                                         (8.2)

Here the diagonal term `sum D_ii Z_i^2` is exactly the allowed separable phase; no independence after projection is invoked.

A self-contained Gaussian smoothing bound converts (8.2) to square-root concentration. On `|kappa-s|<=r`,

`exp(-(kappa-s)^2/(2r^2))>=e^(-1/2)`.

Fourier inversion of the Gaussian gives

`P(|kappa-s|<=r)
 <= C_G K sqrt(r)`,

where

`C_G = e^(1/2) * [2^(1/4) Gamma(1/4)]/sqrt(2 pi)
    =2.835932... <3.`                                                   (8.3)

Thus one may take

`L_rank <3 sqrt(e pi) sqrt(2/delta_0) <65.372`.

The splice (3.4) then gives

`||p_Q||_infinity <35.748<36`.                                         (8.4)

QED.

So the exact diffuse rank-one Schur endpoint is **not** an obstruction. What remains is quantitative nonseparable departure from that endpoint.

## 9. Compact conditional end-to-end architecture after this run

The current proof assembly now has the following source-valid structure.

1. Near-diagonal and definite physical two-plane branches are paid by the preceding B19 results.
2. High stable-rank/diffuse branches and the reviewed separable-phase branch are paid by existing worker/interactive theorems.
3. In the previous `s_2(H)<=1/8` one-effective residue, the physical indefinite pivot pair plus exact Schur complement obeys the quarter-kernel splice of Section 3.
4. The actual mixed compression forces `|w^T S w|>9/280`.
5. A Schur diagonal of magnitude at least `9/1120` closes the full form with density `<25`.
6. Otherwise an original-coordinate outside cut has `s_1(S[I,J])>27/2240`.
7. A ridge-certified version of that cut closes by the fresh ridge theorem plus the splice.
8. The exact diffuse-rank-one Schur endpoint closes with density `<36`.

The full conjecture remains **OPEN** because the complementary `s_2(H)>1/8` extraction is not yet exhaustive, and within the one-effective branch the following quantitative implication is still missing.

## 10. First unpaid implication after the new splice

### `QFORM-SCHUR-CROSS-LOWRIDGE-STABILITY-v1` — OPEN

Under the exact one-effective normal form, assume:

- `|w^T S w|>9/280` and `max w_i^2<7/27`;
- all physical Schur diagonals have magnitude `<9/1120`;
- a forced disjoint original-coordinate cut has `s_1(S[I,J])>27/2240`;
- no available cut satisfies the proved ridge certificate;
- `S` is not of the exact diagonal-plus-`mu ww^T` form already paid in Section 8.

Prove a dimension-free quantitative stability dichotomy: either extract a second independent cross/ridge direction large enough for the completed mixed/ridge mechanisms, or show that `S` is close enough to a diffuse rank-one-plus-diagonal form that a perturbation-stable version of Section 8 survives.

This is narrower than the former generic “mixed aggregate splice.” The key new fact is that the obstruction has been moved entirely into the exact Schur critical-value matrix on the original outside coordinates, with a fixed numerical cross singular resource and no biased induced law.

## 11. Constants/checks and nonclaims

With `delta_0=9/280`, `eta=9/1120`, `m=7/8`:

- forced cross singular threshold: `3 delta_0/8=27/2240=0.01205357...`;
- `L_diag=31.5524255...`;
- full physical-Schur-diagonal splice constant: `24.8353524...<25`;
- Gaussian smoothing constant `C_G=2.83593244...<3`;
- worst displayed exact diffuse-rank-one Schur splice constant: `35.7478034...<36`.

A separate verifier records these arithmetic checks. They are not a proof substitute; the analytic proof is above.

**Not proved:** the full theorem, global continuity, an automatic ridge certificate, or the quantitative low-ridge stability implication. No counterexample to the owner target was found.
