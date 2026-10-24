SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account02, slot B18, 2026-09-22T20:38:52Z.
attacking: Literature-to-proof transfer for the zero/near-isotropic physical-pivot branch, combining the source-valid spectral-window theorem, the completed account03/B18 two-eigenvalue Schur half-Riesz theorem, and the exact LPP marginal-density theorem.

# account02/B18 — two-stage spectral-window to heavy-star/pair reduction

**Run:** `20260922T203852Z-b18-qform-lit-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_REDUCTION`  
**Full target:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target is: for every dimension, every independent real input vector `X=(X_i)` whose one-dimensional probability densities satisfy `0<=f_i<=1`, and every real symmetric matrix `A` with third singular value `s_3(A)>=1` (equivalently at least three eigenvalues of modulus at least one), prove that `Q=X^TAX` has an essentially bounded density by one universal constant, or give a valid counterexample.

The current completed diffuse-window theorem solves matrices for which the spectral projection onto `|lambda(A)|>=1/64` has all physical coordinate leverages at most `1/32`. The designated partner account03/B18 then solves a nonzero physical pivot whenever its Schur residual has a diffuse **two-eigenvalue** window. The first unpaid implication is therefore structural: quantify what a target matrix must contain if it escapes both diffuse branches, without rotating the product law or introducing moments/support assumptions.

This report proves an exhaustive two-stage reduction. Every still-unpaid target matrix contains either (i) a quantitatively strong original-coordinate star, (ii) a quantitatively strong star in a physical Schur residual, or (iii) a physical `2x2` principal block with determinant at least `2^-18`. The star branches retain a genuine cap-`sqrt(2)` product-projection bank by Livshyts--Paouris--Pivovarov. This does **not** by itself close the full conjecture because that bank may be dependent on the same-side quadratic remainder.

## 2. Source-matched inputs and hypothesis audit

### 2.1 Spectral-window density theorem

Canonical source:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

It proves: if `A` satisfies the target three-large-eigenvalue hypothesis and `P_A=1_{|A|>=1/64}` has

`max_i (P_A)_ii <= 1/32`,

then `X^TAX` has a continuous density with

`||p_Q||_infinity <= 288 sqrt(3e)/13 < 64`.

Arbitrarily many smaller nonzero eigenvalues of either sign are allowed. The proof keeps original-coordinate independence and does not use law-uniform pointwise Fresnel decay.

### 2.2 Designated partner actually applied: account03/B18 r16

Canonical source:

`yspennstate/math-open-problems@42c1368934f9c5fdfd1723329382ae2bbb408003`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260922T195803Z-account03-B18-QFORM-r16/REPORT.md`.

Its theorem `QFORM-RIDGE-HALF-RIESZ-TWOEIG-v1` states: if a symmetric `S` has `s_2(S)>=s>0` and the spectral projection `P_S=1_{|S|>=s/64}` satisfies `max_j(P_S)_jj<=1/32`, then for independent cap-one variables `Z` and arbitrary affine terms,

`sup_u E|Z^T S Z+b^TZ+d-u|^(-1/2) <= C_H s^(-1/2)`,

where

`C_H=[192/(5 sqrt(13))](12e)^(1/4)<25.453`.

For a physical pivot

`A=[[a,b^T],[b,C]],  a!=0,  S=C-bb^T/a`,

rank-one completion gives `s_3(A)<=s_2(S)`, so under `s_3(A)>=s` the same diffuse residual condition yields

`||p_(X^TAX)||_infinity <= C_H/sqrt(|a|s)`.

This is used below with `s=1`; no fourth large eigenvalue is assumed.

### 2.3 Livshyts--Paouris--Pivovarov marginal theorem

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949.

Exact source-matching statement used here: if `f(x)=prod_i f_i(x_i)` is a product probability density with every `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. In particular every normalized one-dimensional linear form in a subset of the original independent coordinates has density at most `sqrt(2)`.

There are no moment, centering, bounded-support, log-concavity, identical-law or smoothness hypotheses in this transfer. A projection need not have independent coordinates; only the one-dimensional cap is used below.

## 3. Main theorem — `QFORM-TWO-STAGE-WINDOW-STARPAIR-v1`

Let `A` be real symmetric with `s_3(A)>=1`, and let

`P_A = 1_{|A|>=1/64}`

be the spectral projection onto all eigenspaces whose eigenvalues have modulus at least `1/64`. Set

`delta = 2^-9 = 1/512`.

Then at least one of the following five alternatives holds.

1. **Overall diffuse branch (solved):** `max_i(P_A)_ii<=1/32`, and therefore

   `||p_(X^TAX)||_infinity <64`.

2. **Near-zero physical pivot gives a heavy star:** there is an original coordinate `i` with

   `|A_ii|<delta,    ||A_{i,-i}||_2>delta`.

3. **Nonzero pivot with diffuse two-eigenvalue Schur residual (solved):** there is an original coordinate `i` with `|A_ii|>=delta` such that, for

   `S=C-bb^T/A_ii`,

   the projection `P_S=1_{|S|>=1/64}` satisfies `max_j(P_S)_jj<=1/32`. Then

   `||p_(X^TAX)||_infinity <= C_H sqrt(512) <576`.

4. **A quantitative physical pair:** there are original coordinates `i!=j` with

   `|det A[{i,j},{i,j}]| >= delta^2 = 2^-18`.

5. **A second heavy star in the physical Schur residual:** for some original coordinate `i` with `|A_ii|>=delta`, its Schur residual `S` has an original residual coordinate `j` satisfying

   `|S_jj|<delta,    ||S_{j,-j}||_2>delta`.

Consequently every target matrix not already paid by Alternatives 1 or 3 is forced into a scale-normalized original-coordinate pair/star structure. No principal-minor condition is asserted to be automatic beyond the alternatives above.

### Proof

If Alternative 1 holds, apply the completed spectral-window theorem. Hence assume it fails. Then some physical coordinate `i` satisfies

`p_i:=(P_A)_ii>1/32`.

By spectral calculus,

`||Ae_i||_2^2 = e_i^T A^2 e_i`
` >= (1/64)^2 e_i^T P_A e_i`
` > 1/(4096*32) = 2^-17`.                                      (3.1)

Write, in the original physical coordinates,

`A=[[a,b^T],[b,C]]`,

where `a=A_ii` and `b=A_{-i,i}`. Since

`||Ae_i||_2^2=a^2+||b||_2^2`,                                 (3.2)

if `|a|<delta`, then `a^2<2^-18`, and (3.1)--(3.2) give

`||b||_2^2>2^-17-2^-18=2^-18=delta^2`.

Thus Alternative 2 holds.

It remains to treat `|a|>=delta`, so in particular `a!=0`. Form the physical Schur residual

`S=C-bb^T/a`.

The rank-one completion identity

`A - [[a,b^T],[b,bb^T/a]] = 0 direct_sum S`

and the singular-value rank inequality give

`s_3(A)<=s_2(S)`.

Hence `s_2(S)>=1`. If `P_S=1_{|S|>=1/64}` has all diagonal entries at most `1/32`, the designated account03/B18 theorem gives

`||p_Q||_infinity <= C_H/sqrt(|a|)`
` <= C_H sqrt(512)`
` = [192 sqrt(512)/(5 sqrt(13))](12e)^(1/4)`
` = 575.921724116... <576`.

This is Alternative 3.

Finally suppose the residual window is not diffuse. Choose a residual physical coordinate `j` with

`q_j:=(P_S)_jj>1/32`.

Exactly as in (3.1),

`||Se_j||_2^2>2^-17`.                                          (3.3)

Write `d=S_jj` and `c=S_{j,-j}`. If `|d|<delta`, (3.3) yields `||c||_2>delta`, which is Alternative 5.

If instead `|d|>=delta`, inspect the ORIGINAL physical principal pair `{i,j}`. Its determinant is exactly

`det [[a,b_j],[b_j,C_jj]]`
` = a C_jj-b_j^2`
` = a(C_jj-b_j^2/a)`
` = a S_jj = a d`.                                             (3.4)

Therefore

`|det A[{i,j},{i,j}]|=|ad|>=delta^2=2^-18`,

which is Alternative 4. This exhausts all cases. QED.

## 4. Product-provenance content of the star alternatives

Alternative 2 contains more information than a large Euclidean row norm. Put

`beta=||b||_2>delta,    u=b/beta`,

and define the normalized bank

`Y=u^T X_{-i}`.

Because `u` is a unit vector supported on the original coordinates other than `i`, the LPP theorem gives

`||p_Y||_infinity <= sqrt(2)`.                                 (4.1)

Moreover `X_i` is genuinely independent of the **entire** vector `X_{-i}`, hence of the pair `(Y,R_i(X_{-i}))` for every measurable residual function `R_i`. The quadratic form has the exact representation

`Q = a X_i^2 + 2 beta X_i Y + R_i(X_{-i}),`                    (4.2)

with

`|a|<1/512,    beta>1/512,    ||p_Y||_infinity<=sqrt(2)`.       (4.3)

This is a normalized original-product star, not an eigenbasis statement.

Alternative 5 gives the same normalized-bank conclusion inside the Schur residual: if `gamma=||S_{j,-j}||_2>delta`, then the unit linear bank formed from the remaining original residual coordinates has density cap `sqrt(2)`, while the physical variable `X_j` remains independent of those remaining coordinates.

The live correction archive is essential here: (4.1) does **not** imply that `Y` is independent of the same-side remainder `R_i`, nor does it give a uniformly bounded conditional density of `Y` given that remainder. The known conditional-cap and fiberwise-trace counterexamples rule out that shortcut. Thus the exact first unpaid analytic implication after this reduction is a **dependence-safe third-curvature estimate** for (4.2), or an equivalent grouped-coordinate argument that uses the fact that `(Y,R_i)` is generated by an original cap-one product source.

## 5. Exact-rank-three strengthening

If `A` has exact rank three and all three nonzero eigenvalues have modulus at least one, then `P_A` is its range projection and (3.1) strengthens to

`||Ae_i||_2^2>1/32`.

Thus in Alternative 2 one actually obtains

`||A_{i,-i}||_2 > sqrt(1/32-2^-18)`
` = 0.1767659053...`,

while retaining the same LPP cap `sqrt(2)` for the normalized bank. This quantifies the zero/near-isotropic pivot obstruction in the exact-rank-three case that earlier B18 work had isolated but not scaled.

## 6. What this closes and what it does not

**Closed in this run:** a source-valid, arbitrary-dimension, arbitrary-law deterministic reduction from the full three-large-eigenvalue hypothesis to two already-proved diffuse branches plus explicit scale-normalized physical pair/star alternatives. The designated partner account03/B18 r16 is applied at the exact inequality (Alternative 3), not merely cited. LPP is applied only to a genuine original-coordinate linear projection.

**Not closed:** neither a determinant lower bound for one physical pair nor a marginal cap for one normalized star bank alone controls the full higher-rank quadratic form. In particular, rank-two indefinite quadratic forms can have logarithmic singularities, and the star bank may be dependent on the residual quadratic term. No post-rotation independence, hidden moments, compact support, smoothness, pointwise uniform Fourier decay, or arbitrary-joint coarea lemma is used.

**Next implication:** prove a product-provenance estimate for the normalized star

`a X^2 + 2 beta X Y + R`,

with `|a|<1/512`, `beta>1/512`, `X` an original cap-one scalar independent of the entire source generating `(Y,R)`, and `Y` a unit linear projection of that source with `||p_Y||_infinity<=sqrt(2)`; or show how Alternative 4 plus `s_3(A)>=1` necessarily yields an already-proved pair-log/rank-two-half-Riesz branch. Any transfer must preserve the dependence of `Y` and `R`.

## 7. Correction/source status

Consumed corrections include the failure of law-uniform pointwise quadratic Fourier decay, dimension-free naive fiber suprema, post-rotation independence, single-Schur rank-two extraction, conditional-cap-as-independence, fiberwise trace-mass control, arbitrary-joint 3D coarea, and positive conditional projection-density moments. The present proof avoids each interface explicitly.

Primary literature matched this run: Livshyts--Paouris--Pivovarov exactly matches the cap-one product input class for orthogonal marginals. Marcus--Spielman--Srivastava is used only through the fully proved partner/ridge-window dependencies with its finite Parseval-frame hypotheses already audited there. No exact prior theorem matching the unrestricted QFORM target was located; this is not a novelty claim.