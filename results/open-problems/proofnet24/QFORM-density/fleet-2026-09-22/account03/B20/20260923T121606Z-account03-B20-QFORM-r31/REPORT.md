# account03/B20 r31 — finite-depth heavy-leverage deletion compiler

Run: `20260923T121606Z-account03-B20-QFORM-r31`

Status: **ESSENTIAL_STEP_APPLIED / EXACT-RANK-THREE HEAVY-LEVERAGE FRONTIER REDUCED / FULL QFORM OPEN**.

## 1. Exact target and source discipline

The owner target remains: for arbitrary finite `n`, independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound on the density of `Q=X^T A X`, or give a valid target counterexample. Full-target continuity is tracked separately.

This report does not rotate the random vector, does not infer independence of spectral coordinates, does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, a conditional density cap as independence, small-coefficient deletion, or a one-good-minor shortcut. Every conditioning step below is on literal original coordinates.

Fresh current global synthesis predecessor: account01/B20, `QFORM-N3-LOWLEVERAGE-ANNULUS-OR-STAR4DIR-COMPILER-v1`, canonical `yspennstate/math-open-problems@0a22623e8aa296bfdb618b8952fbd186c670c55c`. It leaves the arbitrary-extra-spectrum annulus/star-four-direction packet open. The theorem below does not claim to pay that arbitrary-rank packet; it closes a distinct exact-rank-three heavy-leverage recursion that was still feeding the older mixed-range/near-coloop frontier.

Fresh account03/B20 predecessor: r30, canonical `yspennstate/math-open-problems@2c0131b6830892a77a8faaf3521388d3a51e7514`, which reduced the exact-rank-three double-coloop state to a three-packet/mixed-range survivor.

Required completed partner actually applied: account04/B20 `QFORM-MODERATE-HEAVY-ANCHOR-DELETION-v1`, canonical `yspennstate/math-open-problems@1d3bcd6c2a19605a6bdcb3fa572b7f85c19369db`. Its theorem says that for an exact-rank-three Parseval factor `A=RMR^T`, `s_min(M)>=1`, one physical row of leverage `c in (1/2,3/4]`, and all residual deletion-whitened leverages at most `1/2`, the density is continuous and

`||p_Q||_infinity <= 3 e (1-c)^(-1/3) <= 3 e 4^(1/3) < 12.946`.

The determinant-basis receiver used for later deletion stages is account01/B18 `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, canonical `yspennstate/math-open-problems@b42066397eb5ba83a885c6e700e0417a49a1d8ac`. In its natural volume-sampling specialization, for a `3 x m` column matrix `L`, an invertible symmetric `D`, all leverage marginals at most `1/2`, and `G=LL^T`, it gives, uniformly under affine terms,

`||p||_infinity <= 3e (|det D| det G)^(-1/3)`

and an integrable characteristic-function majorant, hence a continuous density.

## 2. Setup: exact-rank-three physical frame

Assume in this section that

`A = R M R^T`,

where the physical rows `r_i in R^3` of `R` satisfy

`R^T R = sum_i r_i r_i^T = I_3`,

and `M` is real symmetric invertible with

`s_min(M)>=1`.

Thus `|det M|>=1`. This is the exact-rank-three subproblem, not the arbitrary-extra-spectrum target.

For a set `S` of already conditioned original coordinates define the residual Gram

`G_S := I_3 - sum_(i in S) r_i r_i^T = sum_(i notin S) r_i r_i^T`.

Whenever `G_S` is positive definite, define the deletion-whitened leverage of a residual original coordinate `i notin S` by

`ell_i(S) := r_i^T G_S^(-1) r_i`.

The whitened residual rows `G_S^(-1/2)r_i` form a Parseval frame, hence

`0 <= ell_i(S) <= 1`,

and their leverages sum to `3`.

If `i notin S` is deleted next, then

`G_(S union {i}) = G_S - r_i r_i^T`,

and the matrix determinant lemma gives the exact identity

`det G_(S union {i}) = det G_S [1-ell_i(S)]`.                 (2.1)

No random variable has been transformed in this identity.

## 3. New theorem — QFORM-EXACTR3-18ANCHOR-DIFFUSE-OR-NEARCOLOOP-v1

For every exact-rank-three factorization above, one of the following alternatives holds.

### (A) Continuous density branch

The full law of `Q=X^TAX` has a continuous density and

`||p_Q||_infinity <= 192 e < 522`.                              (3.1)

### (B) finite physical near-coloop branch

There is a set `S` of at most eighteen **original physical coordinates** and a spectral unit vector `v in R^3` such that

`sum_(i in S) <r_i,v>^2 > 63/64`.                              (3.2)

Equivalently, the selected physical Gram

`T_S := sum_(i in S) r_i r_i^T`

has

`lambda_max(T_S)>63/64`.                                      (3.3)

This theorem is deterministic except for the final application of the existing density receiver in branch (A).

### Proof

Start with `S_0=emptyset`, `G_0=I_3`. At a generic stage `k`, first test whether

`lambda_min(G_k)<1/64`.                                       (3.4)

If so, since `T_k=I-G_k`, an eigenvector `v` for `lambda_min(G_k)` satisfies

`v^T T_k v = 1-v^T G_k v >63/64`,

so (B) holds with the current selected set.

Assume therefore that

`G_k >= (1/64) I_3`.                                          (3.5)

Now inspect the deletion-whitened residual leverages.

#### Diffuse stop

If

`max_(i notin S_k) ell_i(S_k) <=1/2`,                         (3.6)

condition on the literal original variables `X_i`, `i in S_k`. The remaining variables are still independent with their original cap-one densities. The residual conditional form has quadratic matrix

`R_res M R_res^T`

plus an affine term depending on the conditioned values. In account01/B18 take the columns of `L` to be the residual physical rows `r_i`; then

`L L^T = G_k`.

Natural volume sampling has determinant-entropy score `Z=det G_k`, and its coordinate marginals are exactly the quantities `ell_i(S_k)` in (3.6). Therefore, uniformly in all conditioned values,

`||p_(Q | X_(S_k))||_infinity
 <= 3e (|det M| det G_k)^(-1/3)
 <= 3e (det G_k)^(-1/3).`                                    (3.7)

From (3.5),

`det G_k >= (1/64)^3`,

so

`||p_(Q | X_(S_k))||_infinity <=3e*64=192e<522`.              (3.8)

The B18 characteristic-function estimate is uniform in the affine term, so averaging over the conditioned physical variables preserves an integrable Fourier majorant. Hence the **full**, unconditioned law has a continuous density and obeys (3.1).

This is a genuine source-product argument: the conditioning is only on original coordinates; whitening is used only to calculate deterministic frame leverages.

#### Heavy deletion step

If (3.6) fails, choose a residual original coordinate `i_k` with

`c_k:=ell_(i_k)(S_k)>1/2`.                                    (3.9)

Put

`u=G_k^(-1/2)r_(i_k)`, `c_k=|u|^2`, `e=u/sqrt(c_k)`.

Then

`G_(k+1)=G_k^(1/2)(I-u u^T)G_k^(1/2)`.                       (3.10)

If `c_k>63/64`, choose `x=G_k^(-1/2)e`. Since `G_k<=I`, one has `G_k^(-1)>=I`, hence

`x^T x = e^T G_k^(-1)e >=1`,

while

`x^T G_(k+1)x = e^T(I-u u^T)e =1-c_k<1/64`.

Therefore

`lambda_min(G_(k+1))<1/64`,                                  (3.11)

so the next stage is already alternative (B).

It remains to consider a sequence of heavy but non-extreme deletions

`1/2 < c_j <=63/64`.                                         (3.12)

By (2.1), after `m` such deletions,

`det G_m = product_(j=0)^(m-1)(1-c_j) <2^(-m)`.              (3.13)

If eighteen such deletions occur, then

`det G_18 <2^(-18)=(1/64)^3`.

For a positive semidefinite `3 x 3` matrix,

`lambda_min(G_18)^3 <= det G_18`,

hence

`lambda_min(G_18)<1/64`.                                     (3.14)

Thus alternative (B) must occur by the time eighteen original coordinates have been selected. Every diffuse stop before then is paid by (3.8). This proves the theorem. QED.

## 4. Required account04/B20 theorem applied to an actual inequality

The first deletion step directly contains account04/B20's completed scope. If the initial physical heavy row `h` has

`1/2 < c=|r_h|^2 <=3/4`

and all post-deletion whitened residual leverages satisfy

`r_i^T(I-r_h r_h^T)^(-1)r_i <=1/2`,

then the partner theorem gives the sharper branch

`||p_Q||_infinity <=3e(1-c)^(-1/3)
                  <=3e 4^(1/3)
                  =12.9450103021... <12.946`,                (4.1)

with a continuous density. This is an equation-level application of the designated partner result, not a mere citation.

The new eighteen-anchor compiler is needed only when the partner's residual-diffuseness gate repeatedly fails or when a normalized pivot becomes extreme. It does not enlarge the partner theorem's assumptions.

## 5. Consequence for the r30 exact-rank-three mixed-range survivor

The r30 three-packet/mixed-range survivor carries a physical row of leverage greater than `1/2`. Apply the theorem above to its exact-rank-three Parseval representation. Then the entire recursive normalized-heavy-row obstruction has only two outcomes:

1. it is paid by a **continuous** density bound `||p_Q||_infinity<522` (and by `<12.946` in the immediate account04/B20 overlap); or
2. there is a set of at most eighteen original coordinates carrying more than `63/64` of one spectral direction.

Hence the older requirement to immediately pay every genuinely mixed second-heavy row can be replaced by a finite-depth deletion compiler. The surviving exact-rank-three obstruction is now a quantitatively finite near-coloop core, not an unbounded normalized-heavy chain.

This also improves the size of the near-coloop support arising from the earlier r29 bookkeeping in this exact-rank-three route: the new certificate uses at most eighteen physical coordinates. It does not by itself pay the near-coloop core, because concentration in one spectral direction does not imply a uniformly positive three-dimensional finite-core Gram.

## 6. What remains open

The full owner target remains open. In particular:

- `QFORM-EXACTR3-18CORE-NEARCOLOOP-PAYMENT-v1` remains: pay the at-most-eighteen-coordinate physical core in (3.2), retaining arbitrary interactions and the diffuse complement, or splice it into an already-paid ruled/convex/grouped receiver.
- The fresher global arbitrary-rank frontier from account01/B20 remains `QFORM-N3-ANNULUS-OR-STAR4DIR-PAYMENT-v1`; the theorem here does **not** remove arbitrary extra spectrum.
- Full-target continuity remains open. Continuity is proved in branch (A) because the B18 Fourier envelope is integrable, and in the immediate partner branch (4.1).
- A full candidate would still require all signs/degenerate cases and two independent end-to-end reviews.

## 7. Constant check and scope check

Exact arithmetic used above:

`(1/64)^3 = 2^(-18)`;

if eighteen factors satisfy `1-c_j<1/2`, then their product is strictly smaller than `2^(-18)`;

`3e*64 = 192e = 521.910... <522`;

`3e*4^(1/3) = 12.9450103021... <12.946`.

The argument never assumes support connectedness, compact support, moments, Gaussianity, log-concavity, iid inputs, or diagonal independence after rotation. No Monte Carlo or histogram is used.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Authenticated repository reads/writes are not native learned-memory receiver ingestion.
