SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-22T23:32:13Z.
attacking: joint product-space Fourier rearrangement for rank-r two-sided quadratic contamination, followed by overlap-safe scalar-square smoothing.

# account02/B04 r22 — two-sided contamination via joint rank-r Fourier rearrangement

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control observed fresh at revision `2026-09-22.15`; full target remains OPEN. Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`. Execution label: `WITHOUT_VERIFIED_BRAIN` (authenticated private-repository retrieval occurred, but no native learned-memory receiver/ingestion was observed).

## 1. Exact scope and source-pinned inputs

Target: for independent real original coordinates with densities bounded by one and symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal bound for the density of `X^T A X`, or give a valid counterexample. No moment, support, centering, diagonal-basis, post-rotation-independence, arbitrary-joint coarea, or law-uniform one-dimensional pointwise Fresnel-decay assumption is introduced.

Corrections consumed include the live `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, the arbitrary-joint coarea/conditional-projection-moment failures in `CURRENT_RESEARCH.md`, and this slot's preceding `QFORM-HYPERBOLIC-TWOSIDED-HALFRIESZ-UNIFORM-FALSE-v1`. The new argument is a JOINT bilinear Fourier estimate on two original product banks; it is not the refuted scalar quadratic-phase bound.

Two completed sources are used at equation level:

1. account02/B06, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. If `U` has `r` orthonormal columns and `X` is an original-coordinate cap-one product vector, `U^T X` has an `r`-dimensional density bounded by `exp(r/2)`.

2. Named partner account03/B04 r20, `QFORM-SQUARE-RANKR-CLEANBANK-LINF-v1`, `yspennstate/math-open-problems@52dbe47e8a0ed76734162216e4446595bba201d9`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T225115Z-r20/REPORT.md`. For a one-quadratically-clean residual bank with two cross singular values at least `sigma`, it gives

`||p_Q||_infinity <= 5.749943550416816 / sqrt(|a| sigma)`.

The named-partner theorem is applied below to an actual clean-side companion inequality before the new two-sided extension is applied.

## 2. New joint Fourier theorem with arbitrary contamination on BOTH banks

Let `X in R^m` and `Y in R^n` be disjoint original-coordinate product banks, all coordinate densities bounded by one. Let `W` be any further independent original-coordinate vector. Let `B` be a real `m x n` matrix of **exact rank** `r>=2`, with nonzero singular values

`sigma_1,...,sigma_r>0`,  `Delta=product_{j=1}^r sigma_j`.

For arbitrary measurable real functions `F(X,W)` and `G(Y,W)`, define

`H = F(X,W) + G(Y,W) + 2 X^T B Y`.                              (2.1)

Thus both active banks may carry arbitrary self-quadratic leakage, arbitrary linear terms, and arbitrary additional within-bank contamination; after conditioning on `W`, all original X coordinates remain independent of all original Y coordinates.

### Theorem 2.1 — `QFORM-RANKR-TWOSIDED-CONTAMINATION-FOURIER-v1`

For every `r>=2`, `H` is absolutely continuous and

`||p_H||_3 <= [3 e r/(3r-4)]^(2/3) Delta^(-2/(3r)).`            (2.2)

More precisely, conditional on every admissible outside value `W=w`, its characteristic function satisfies the JOINT product-space estimate

`|phi_w(t)| <= min{1, (pi e)^(r/2) Delta^(-1/2) |t|^(-r/2)}.`   (2.3)

For `r>=3`, (2.3) is integrable and yields the stronger direct density bound

`||p_H||_infinity <= e r/(r-2) Delta^(-1/r).`                   (2.4)

At the critical rank `r=2`, (2.2) reads

`||p_H||_3 <= (3e)^(2/3) (sigma_1 sigma_2)^(-1/3).`             (2.5)

#### Proof

Fix `w`; all bounds below are uniform in it. Take a thin SVD

`B = U Sigma V^T`,

where `U,V` have `r` orthonormal columns and `Sigma=diag(sigma_1,...,sigma_r)`. Put

`xi=U^T X`, `eta=V^T Y`.

By the completed weighted affine-fiber theorem, `xi` and `eta` have densities `p_xi,p_eta` satisfying

`||p_xi||_infinity, ||p_eta||_infinity <= exp(r/2)`.             (2.6)

Define complex densities

`a_t(xi)=p_xi(xi) E[exp(it F(X,w)) | U^T X=xi]`,
`b_t(eta)=p_eta(eta) E[exp(it G(Y,w)) | V^T Y=eta]`.             (2.7)

Regular conditional expectations suffice; only their modulus bound is used. Namely

`|a_t|<=p_xi`, `|b_t|<=p_eta`,

so, since the projected densities have total mass one,

`||a_t||_2, ||b_t||_2 <= exp(r/4)`.                              (2.8)

Because the original X and Y banks are independent, (2.1) gives exactly

`phi_w(t)= integral a_t(xi) b_t(eta)
                  exp(2it xi^T Sigma eta) dxi deta`.             (2.9)

Use the Fourier convention

`hat b(k)=integral exp(i k.eta)b(eta)deta`.

Then

`phi_w(t)=integral a_t(xi) hat b_t(2t Sigma xi) dxi`.            (2.10)

Cauchy--Schwarz, the change of variables `k=2t Sigma xi`, and Plancherel give

`|phi_w(t)|
 <= ||a_t||_2 |det(2t Sigma)|^(-1/2) ||hat b_t||_2`
` = ||a_t||_2 (2|t|)^(-r/2) Delta^(-1/2)
     (2pi)^(r/2)||b_t||_2`
` <= (pi e)^(r/2) Delta^(-1/2)|t|^(-r/2)`.                     (2.11)

Together with `|phi_w(t)|<=1`, this proves (2.3). This is a joint rank-r bilinear estimate; it does not assert any law-uniform decay for a single quadratic direction.

Set

`T = pi e Delta^(-1/r)`.                                        (2.12)

The right side of (2.3) equals `min(1,(T/|t|)^(r/2))`. Therefore

`integral_R |phi_w(t)|^(3/2) dt
 <= 2 T [1 + 1/(3r/4-1)]
 = 2 T * 3r/(3r-4).`                                            (2.13)

For the inverse Fourier map `g -> (2pi)^(-1) integral exp(-its)g(t)dt`, Riesz--Thorin between `L^1->L^infinity` and Plancherel gives operator norm `(2pi)^(-2/3)` from `L^(3/2)` to `L^3`. Hence

`||p_(H|w)||_3
 <= (2pi)^(-2/3) [2pi e Delta^(-1/r) 3r/(3r-4)]^(2/3)`
` = [3 e r/(3r-4)]^(2/3) Delta^(-2/(3r))`,                    (2.14)

which is (2.2). The inverse transform defines an `L^3` density; equality of Fourier transforms identifies it with the conditional law. Averaging in `w` and Minkowski preserve the same `L^3` bound.

If `r>=3`, direct integration of (2.3) instead gives

`integral |phi_w(t)|dt <= 2T r/(r-2)`.                           (2.15)

Fourier inversion therefore gives (2.4), uniformly in `w`, and averaging preserves it. QED.

### What this pays

The account03/B04 r20 one-clean-side hypothesis is no longer needed when the physical cross block is taken at its exact rank: arbitrary measurable contamination on BOTH product banks is allowed. At `r>=3` the bilinear packet itself has an `L^infinity` density; at the analytically critical `r=2`, it has the exact `L^3` strength needed for one additional square smoother.

The exact-rank qualification is essential to the proof as stated: discarding extra singular directions after a rotation would condition on dependent projected coordinates and is not authorized. No claim is made that top two singular values alone control an arbitrary higher-rank cross block.

## 3. Critical rank-two square splice with two-sided contamination

Let `Z` be one further original coordinate, independent of `(X,Y,W)`, with density bounded by one. Let `a!=0` and let `m(X,Y,W)` be arbitrary measurable, possibly reusing every active bank variable. Put

`Q = a[Z+m(X,Y,W)]^2 + H`.                                      (3.1)

### Lemma 3.1 — one-sided half-Riesz smoothing from `L^3`

If `h` is a probability density with `||h||_3=L`, then

`sup_t integral_0^infinity h(t-u)u^(-1/2)du
 <= 8*3^(-3/4) L^(3/4)`.                                       (3.2)

The same bound holds with `h(t+u)`.

**Proof.** For `R>0`, Holder gives

`integral_0^R h(t-u)u^(-1/2)du
 <= L (integral_0^R u^(-3/4)du)^(2/3)
 = 4^(2/3)L R^(1/6)`.                                           (3.3)

The tail is at most `R^(-1/2)` by total mass one. Writing `x=R^(1/6)` and minimizing `4^(2/3)L x+x^(-3)` gives (3.2). QED.

Conditional on `(X,Y,W)`, translation of `Z` does not change its density cap, so `a[Z+m]^2` has the one-sided density envelope `|a|^(-1/2)u^(-1/2)`. The sign of `a` selects one of the two one-sided potentials in Lemma 3.1. Combining (2.2) and (3.2) proves:

### Theorem 3.2 — `QFORM-SQUARE-RANKR-TWOSIDED-CONTAMINATION-v1`

For every exact cross rank `r>=2`,

`||p_Q||_infinity
 <= C_r |a|^(-1/2) Delta^(-1/(2r)),`                            (3.4)

where

`C_r = 8*3^(-1/4) sqrt(e r/(3r-4)).`                            (3.5)

At the critical `r=2`,

`C_2 = 8 sqrt(e)/3^(1/4) = 10.022058057366376...`,              (3.6)

hence

`||p_Q||_infinity
 <= 10.022058057366376 |a|^(-1/2)
    (sigma_1 sigma_2)^(-1/4).`                                  (3.7)

If `sigma_1,sigma_2>=sigma`, this is

`||p_Q||_infinity <= 10.022058057366376 / sqrt(|a| sigma)`.     (3.8)

This is the first direct B04 payment of the preceding `QFORM-TWOSIDED-CONTAMINATION-JOINT-SPLICE-v1` debt at the critical two-cross-direction endpoint. The completed square may overlap both contaminated banks; no conditional independence between the square shift and `H` is assumed.

## 4. Named partner applied to an actual inequality, then extended beyond its scope

Let

`H2=(1/sqrt(2))*[[1,1],[1,-1]]`, `B=3H2`,
`u=(1,1)/sqrt(2)`, `q_x=q_y=u/20`, `C=(1/5)H2`.

First set the Y-side self block to zero and consider

`Q_clean = 2[z+q_x^T x+q_y^T y]^2 + x^T Cx + 2x^TBy`.          (4.1)

Both singular values of `B` equal `3`, and the y bank is quadratically clean. The named partner account03/B04 r20 theorem therefore gives the actual all-input-law inequality

`||p_(Q_clean)||_infinity
 <= 5.749943550416816/sqrt(2*3)
 = 2.347404624721380...`.                                       (4.2)

The square shift in (4.1) deliberately overlaps both active banks, which the partner theorem permits.

Now restore genuine contamination on the formerly clean side:

`D=-(3/20)H2`,

`Q_* = 2[z+q_x^T x+q_y^T y]^2
       + x^T Cx + 2x^TBy + y^T D y`.                            (4.3)

The partner clean-side theorem no longer applies, while Theorem 3.2 does. Since `Delta=3*3=9` and `a=2`,

`||p_(Q_*)||_infinity
 <= [8 sqrt(e)/3^(1/4)] / [sqrt(2) 9^(1/4)]`
` = 4 sqrt(2e)/3^(3/4)`
` = 4.091488068849406...`.                                      (4.4)

Thus a completed named-partner inequality has been used as the exact boundary case, and the new result explicitly crosses its first missing two-sided-contamination interface.

## 5. Rigorous genuinely rotated indefinite target certificate

Order the physical coordinates as `(z,x_1,x_2,y_1,y_2)`. Let

`A0 = diag(2, S0)`,  `S0=[[0,B],[B^T,0]]`.                      (5.1)

Since `B=3H2` and `H2` is orthogonal, the singular values of `S0` are all `3`, so

`s_min(A0)=2`.                                                   (5.2)

The difference `E=A_*-A0` consists of the two dense self blocks plus the square-overlap perturbation. Put `q=(q_x,q_y)`. Since

`||C||=1/5`, `||D||=3/20`, `||q||=sqrt(2)/20`,                 (5.3)

and

`||[[0,2q^T],[2q,2qq^T]]||
 <= 2||q||+2||q||^2`,                                           (5.4)

we obtain

`||E|| <= 1/5+3/20+sqrt(2)/10+1/100`
`      = 9/25 + sqrt(2)/10`.                                    (5.5)

Therefore Weyl's singular-value inequality gives

`s_min(A_*) >= 2-(9/25+sqrt(2)/10)`
`            = 41/25-sqrt(2)/10`
`            = 1.498578643762690... > 1`.                       (5.6)

So **all five** eigenvalues of this symmetric matrix have modulus bigger than one. The two negative eigenvalues of `A0` are at `-3`; the same perturbation bound keeps them negative, so `A_*` is indefinite. Every z-to-bank coefficient is nonzero, `B` has no zero physical entry, and both self blocks are dense, so this is genuinely rotated/nonseparable rather than a diagonal disguise.

A finite numerical check (not used in the proof of (5.6)) gives

`spec(A_*) approx (-3.029219322164717, -2.980095424506847,
                    1.984395628022514,  2.980102321162068,
                    3.054816797486987)`.

Thus (4.4) is an explicit universal density estimate for a genuinely rotated indefinite form satisfying the exact target spectral hypothesis.

## 6. First unpaid implication after this run

`QFORM-REGULARIZED-CROSS-RANK-ROUTING-v1` remains. The analytic two-sided-contamination debt is now paid for an **exact** rank-r physical cross packet (`r>=3` directly, `r=2` after one scalar square). The bare hypothesis `s_3(A)>=1` still does not force a cross block whose *entire* nonzero singular spectrum has a uniformly bounded geometric-mean cost; arbitrarily small extra cross singular directions cannot simply be discarded after rotation. The next proof must either:

- derive a product-preserving regularized version of Theorem 2.1 that ignores quantitatively tiny extra singular directions without conditioning on dependent spectral coordinates; or
- route those small directions into an already completed scalar-square/ridge/rank-two/pair-log packet before applying this theorem.

This is a structural/full-target debt, not a failure of the new analytic estimate. Full QFORM remains OPEN; no target counterexample is claimed.

## 7. Exact computation used

The accompanying `CHECK.py` and `CHECK_OUTPUT.txt` reproduce `B^T B=9I`, the exact Weyl perturbation bound, the rigorous `s_min>1` certificate, the numerical spectrum check, the new constant, and the named-partner companion constant. The proof uses the exact Weyl bound, not the floating spectrum.

Privacy/source review for this run's mathematical bundle: changed files are limited to this worker-owned QFORM run directory; no credentials, signed URLs, unrelated private data, scheduler identifiers, machine paths, benchmark material, or public-release instructions are included.
