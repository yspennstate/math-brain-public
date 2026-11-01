# fleet01/B16 — HLS bridge for a nonisotropic residual-heavy spectral row

**Run:** `20260922T150815Z-qform-B16-a01-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source discipline

The target remains: for every dimension, every independent real coordinates `X_i` with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has a density with one universal finite `L^infinity` bound. Continuity is tracked separately.

Fresh control was read from `yspennstate/math-research-brain` revision `2026-09-22.5`; the final correction refresh used brain commit `6f936daa3a621399391c87e126511bdaccddfac7`, correction blob `2ee621225465e603dfd118f6bd86b1ddc853f40e`. In particular, this report does not use law-uniform pointwise Fresnel decay, independence after spectral rotation, a uniform normalized complement-fiber trace bound, receiver-only conditional density caps, one tiny physical minor, or the absolute phase-Wiener interface.

The assigned partner result actually applied is fleet02/B16 run `20260922T133220Z-fleet02-B16-QFORM-auto11`, canonical report `yspennstate/math-open-problems@8cde0cb226c8e10766142441c05878d19a28a623:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T133220Z-fleet02-B16-QFORM-auto11/REPORT.md`, blob `739d8884ff98ab8ec101800a5e133aeb3de0555a`. It proves that authentic product-source complement fibers can have logarithmically unbounded normalized indefinite traces, while the full product law remains bounded if the original-coordinate aggregation is performed before the curved trace. Its equation (8.1), derived from the completed fleet03/B16 theorem, gives for an exact rank-three physical pivot with residual two-frame leverage at most `1/2`

`||p_Q||_infinity <= 4 sqrt(3e) (ell |det Lambda| |a|)^(-1/4)`.        (1.1)

The new argument below covers a complementary residual-heavy collar while obeying the partner correction: an original physical coordinate stays independent until after the nonlinear trace, and the transverse bank is aggregated before any square singularity is paid.

## 2. A dependence-safe fractional-square smoothing lemma

### Lemma 2.1 (`QFORM-DEPENDENT-SQUARE-HLS-L65-v1`)

Let `V` be a real random variable with density at most one and independent of a sigma-field `G`. Let `D,m` be real `G`-measurable random variables, and suppose `D` has a density `p_D in L^(6/5)(R)`. For `c!=0`, put

`Y = D + c(V+m)^2`.

Then `Y` is absolutely continuous and

`||p_Y||_3 <= C_HLS |c|^(-1/2) ||p_D||_(6/5)`,                     (2.1)

where `C_HLS<infinity` is any valid one-dimensional Hardy--Littlewood--Sobolev constant for the fractional kernel `|x|^(-1/2): L^(6/5)->L^3`.

### Proof

Condition on `D=r`. Because `V` is independent of the whole sigma-field `G`, the conditional law of `V+m` given `D=r` is a mixture of translates of the law of `V`; therefore it has density at most one. Consequently the conditional density `k_r` of `c(V+m)^2` obeys the pointwise bound

`k_r(w) <= |c|^(-1/2) |w|^(-1/2) 1_{cw>0}`                         (2.2)

for a.e. `w!=0`. Indeed the two inverse branches contribute at most `1/(2 sqrt(|c w|))` each.

Thus

`p_Y(y) <= |c|^(-1/2) int p_D(r) |y-r|^(-1/2) dr`.                 (2.3)

The one-dimensional Hardy--Littlewood--Sobolev inequality with fractional order `1/2` maps `L^(6/5)` to `L^3`, giving (2.1). No conditional independence between `D` and the shift `m` is used. QED.

This is the same dependence-safe principle needed in the QFORM programme: the only independence retained is the genuine original-coordinate independence of `V` from `G`.

## 3. An explicit L^(6/5) bound for a square of a capped linear bank

### Lemma 3.1 (`QFORM-SQUARE-L65-CAP-v1`)

Let `L` have a probability density bounded by `H`. Then for every `d!=0`, `dL^2` has an `L^(6/5)` density satisfying

`||p_{dL^2}||_(6/5)
 <= (15/2)^(5/6) H^(1/3) |d|^(-1/6)`.                              (3.1)

### Proof

It is enough to take `d=1`. If `r` is the density of `L^2`, then for `y>0`

`r(y)=[g(sqrt y)+g(-sqrt y)]/(2 sqrt y) <= H/sqrt y`,              (3.2)

and `int r=1`. Hence for every `s>0`

`|{r>s}| <= min(s^(-1),H^2 s^(-2))`.                               (3.3)

Using layer cake with `p=6/5` and splitting at `s=H^2`,

`int r^(6/5)
 <= (6/5)[ int_0^(H^2) s^(-4/5) ds
            + H^2 int_(H^2)^infinity s^(-9/5) ds ]
 = (15/2) H^(2/5)`.                                                (3.4)

Taking the `5/6` power gives the claim for `d=1`. Scaling by `d` contributes `|d|^(1/(6/5)-1)=|d|^(-1/6)`. QED.

## 4. Residual-heavy nonisotropic theorem

Let `W` be an `N x 2` Parseval frame, `W^T W=I_2`, arising from the residual spectral plane after one physical rank-three pivot. Choose a physical residual row `w_j` of leverage

`h=||w_j||^2>1/2`.

Choose an orthonormal residual spectral basis `(e_1,e_2)` with `w_j=sqrt(h)e_1`. For `k!=j`, write

`w_k=(t_k,l_k)`.

Parseval gives the exact identities

`sum_{k!=j} t_k^2=1-h`,  `sum_{k!=j} l_k^2=1`,  `sum_{k!=j} t_k l_k=0`.   (4.1)

Let

`X=X_j`, `T=sum_{k!=j} t_k X_k`, `L=sum_{k!=j} l_k X_k`.

Then the two projected residual coordinates are `(sqrt(h)X+T,L)`. Let the invertible residual quadratic coefficient be

`B=[[beta,gamma],[gamma,delta]]`.

Assume `beta!=0`. Completing the square in the genuine independent physical coordinate `X` gives the exact identity

`(sqrt(h)X+T,L) B (sqrt(h)X+T,L)^T`
` = beta h (X+m)^2 + (det B/beta)L^2`,                              (4.2)

where

`m=[T+(gamma/beta)L]/sqrt(h)`                                      (4.3)

is measurable with respect to all coordinates other than `X`.

The actual bounded-density projection theorem, applied to the normalized one-dimensional bank `L` (equivalently by adding an independent unit-density dummy coordinate to make a two-dimensional orthogonal projection), gives

`||p_L||_infinity <=2`.                                             (4.4)

Lemma 3.1 therefore gives

`||p_((detB/beta)L^2)||_(6/5)
 <= (15/2)^(5/6) 2^(1/3)
    |det B|^(-1/6)|beta|^(1/6)`.                                   (4.5)

Applying Lemma 2.1 to (4.2), with `c=beta h`, yields:

### Theorem 4.1 (`QFORM-RESIDUAL-HEAVY-NONISOTROPIC-HLS-v1`)

For every residual-heavy row as above with `beta!=0`, the residual quadratic has an `L^3` density and

`||p_D||_3
 <= C_* h^(-1/2)|beta|^(-1/3)|det B|^(-1/6)`,                    (4.6)

where

`C_* = C_HLS (15/2)^(5/6) 2^(1/3)`.                                (4.7)

No independence between the residual projected coordinates `T,L` is assumed. The bank `L` is aggregated while its original-coordinate product provenance is still available, before the curved square trace is estimated.

### Dimensionless collar

If for some `eta>0`

`|beta| >= eta sqrt(|det B|)`,                                     (4.8)

then

`||p_D||_3 <= sqrt(2) C_* eta^(-1/3)|det B|^(-1/3)`,               (4.9)

because `h>1/2`.

Thus the nonisotropic heavy-row branch has exactly the determinant homogeneity needed for the existing outer-square smoother whenever its normalized residual Rayleigh coefficient is bounded away from zero.

## 5. Exact-rank-three consequence and actual partner application

Now let

`A=R Lambda R^T`, `R^T R=I_3`,

have exact rank three and invertible symmetric `Lambda`, with its three eigenvalues of modulus at least one. Choose an original physical pivot row `v=r_i`, and set

`ell=||v||^2`, `a=v^T Lambda v=A_ii`.

Assume `a!=0`. The exact Schur identity for the residual `2 x 2` coefficient is

`|det B|=ell |det Lambda|/|a|`.                                    (5.1)

There are now two product-preserving branches.

1. **Residual diffuse.** If every residual row leverage is at most `1/2`, apply the assigned-partner fleet02/B16 inequality (1.1):

`||p_Q||_infinity <=4 sqrt(3e)(ell |det Lambda| |a|)^(-1/4)`.       (5.2)

2. **Residual heavy and quantitatively nonisotropic.** If a residual row has `h>1/2` and, in its normalized direction, (4.8) holds, apply (4.9). The already completed dependence-safe outer `L^3 -> L^infinity` square smoothing theorem gives

`||p_Q||_infinity
 <=4 |a|^(-1/2)||p_D||_3^(3/4)`
` <= C_hyb eta^(-1/4)(ell |det Lambda| |a|)^(-1/4)`,               (5.3)

where

`C_hyb=4 (sqrt(2) C_*)^(3/4)<infinity`.                            (5.4)

The determinant cancellation in (5.3) is exact:

`|a|^(-1/2)|det B|^(-1/4)
 =(ell |det Lambda| |a|)^(-1/4)`.                                  (5.5)

The exactly isotropic endpoint `beta=0` is already covered by `QFORM-RANK3-RESIDUAL-ISOTROPIC-HEAVY-v1` from fleet01/B10; the theorem above supplies the punctured nonisotropic collar away from that endpoint.

This is a genuine application of the assigned partner result: the diffuse residual branch is closed by the exact fleet02/B16 inequality (5.2), while the present theorem closes the complementary residual-heavy region satisfying (4.8). The two arguments share the same determinant-scale outer invariant and both preserve original-coordinate product aggregation before the nonlinear trace.

## 6. What this changes

The partner counterexample proved that normalized complement-fiber trace control is impossible even for authentic product sources. The present proof avoids that interface entirely. It never freezes the complement and asks for a uniform trace/mass ratio. Instead:

- one genuine physical coordinate remains independent through the square smoothing;
- the transverse bank `L` is aggregated using the projection theorem before tracing;
- dependence among all other residual variables is permitted;
- the final estimate is stated in invariant Schur determinant units.

Consequently, in an exact-rank-three sequence with the outer scale `ell |det Lambda| |a|` bounded below, an unbounded-density sequence cannot stay in the residual-diffuse branch, cannot stay at the exact residual-isotropic heavy endpoint, and cannot have a residual-heavy row with

`|beta|/sqrt(|det B|) >= eta`

for any fixed `eta>0`. Any surviving nested-heavy sequence must enter the **punctured residual light-cone regime**

`0 < |beta|/sqrt(|det B|) ->0`,                                    (6.1)

or else the outer physical pivot itself must approach its light cone so that the outer invariant degenerates.

This complements the separate rank-three structural reductions that force final-bank diffuseness and covariance saturation in any putative bad nested-heavy sequence. The new theorem pays a quantitative nonisotropic collar rather than another finite principal-minor branch.

## 7. Status and next unpaid implication

**Proved here:**

- `QFORM-DEPENDENT-SQUARE-HLS-L65-v1`;
- `QFORM-SQUARE-L65-CAP-v1`;
- `QFORM-RESIDUAL-HEAVY-NONISOTROPIC-HLS-v1`;
- the exact-rank-three hybrid implication (5.2)--(5.3), combining the assigned fleet02/B16 diffuse-residual result with the new heavy-row collar.

**Not proved:** the full owner conjecture. The first remaining projection-product implication is the **uniform transition through the residual light cone**, i.e. obtain a determinant-level `L^3` estimate when a heavy residual row has `|beta|/sqrt(|det B|)->0` without replacing the product law by a fiberwise trace cap. The exact endpoint `beta=0` is paid, and every fixed punctured collar `|beta|>=eta sqrt(|detB|)` is paid here, but a uniform estimate connecting them is still missing. A second independent debt is stability under arbitrary additional spectral components beyond exact rank three.

Continuity is not proved by the present `L^p` argument and remains separate.

**Full QFORM conjecture: OPEN / NOT PROVED.**
