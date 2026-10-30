# fleet01/B13 — leverage collision and three-row near-isotropic forcing

**Run:** `B13-20260922T153208Z-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / RANK-THREE LEVERAGE-COLLISION AND ISOTROPIC-COLLAR FORCING / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full owner conjecture remains **OPEN / NOT PROVED**. Everything proved here concerns the exact-rank-three spectral core. Arbitrary additional spectral directions remain a separate interaction debt except in already completed scoped branches.

## 1. Source state and exact dependencies

Fresh owner control was read from `yspennstate/math-research-brain` at commit `7ec7c2b5b2005b6c0edc6248c4dda1bdae8fc978`, and refreshed before publication; the active programme remained `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`. The full target is: for independent real coordinates with probability densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `X^T A X`, or give a valid counterexample.

The live corrections used here exclude law-uniform pointwise quadratic oscillatory decay, post-rotation independence, fiber-supremum closure, one-cross-minor closure, conditional-cap substitutes for independence, bounded-diameter/fixed-fragment localization, and single-Schur-rank-two extraction.

The completed assigned-partner result actually consumed is `fleet02/B13`:

`yspennstate/math-open-problems@93bed74b07afe996a4aa08eaeb88f35060653134`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T152225Z-fleet02-B13-productset-7f3c9a/REPORT.md`.

It proves exact residual pair-incidence identities in the nested-heavy rank-three branch and the quantitative conclusion used in Section 4 below. Its earlier exact bang-bang theorem is

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`:
for every measurable `0<=K<=1`, the supremum of `int K prod_i f_i` over `0<=f_i<=1`, `int f_i=1`, equals the supremum over `f_i=1_{E_i}`, `|E_i|=1`; bounded finite interval unions are dense. This will be applied to the actual slab inequality in Section 3.

Two additional proved dependencies are used exactly at their stated scopes:

1. fleet01/B13 disjoint exterior theorem, source `yspennstate/math-open-problems@0b5cf04790e5927df0efed8811a2a1295006e141`: for exact rank three, with ordered disjoint Pluecker mass `D0`,
   `||p_Q||_infinity <= 12 D0^(-1/6)` under `|lambda_j|>=1`.
2. fleet03/B05 universal rank-two half-Riesz/Schur theorem, source `yspennstate/math-open-problems@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409`: for an exact-rank-three frame row of leverage `ell_i=||r_i||^2` and physical pivot `pi_i=A_ii`,
   `||p_Q||_infinity <= C2 (|pi_i| ell_i |det Lambda|)^(-1/4)` whenever `pi_i!=0`, where `C2=16*2^(3/4)`.

No status in those reports is promoted beyond its proved scope.

## 2. New exact leverage-collision identity

Let

`A=R Lambda R^T`, `R^T R=I_3`,

with rows `r_i in R^3`, and put

`ell_i=||r_i||^2`.

For each physical triple `I`, let

`w_I=det(R_I)^2`.

Cauchy--Binet gives `sum_I w_I=1`. Define

`D0=sum_{I cap J=empty} w_I w_J`,

where the sum is over ordered pairs of triples.

### Lemma 2.1 — exact one-coordinate basis incidence

For every physical coordinate `i`,

`boxed(sum_{I: i in I} w_I = ell_i)`.                         (2.1)

#### Proof

Scale row `r_i` of `R` by `sqrt(t)`, leaving every other row unchanged. Cauchy--Binet gives

`det(R_t^T R_t)`
` = sum_{I: i notin I} w_I + t sum_{I: i in I} w_I`.          (2.2)

But

`R_t^T R_t=I_3+(t-1) r_i^T r_i`,

so the rank-one determinant lemma gives

`det(R_t^T R_t)=1+(t-1)ell_i`.                               (2.3)

Comparing the coefficient of `t` proves (2.1). QED.

### Theorem 2.2 — leverage collision lower bound

`boxed(D0 >= 1-sum_i ell_i^2 >= 1-3 ell_max)`,                (2.4)

where `ell_max=max_i ell_i`.

#### Proof

Regard `I,J` as independent random spectral basis triples with law `P(I)=w_I`. Then `D0=P(I cap J=empty)`. By the union bound and (2.1),

`1-D0=P(I cap J nonempty)`
` <= sum_i P(i in I and i in J)`
` = sum_i ell_i^2`.                                         (2.5)

Also `sum_i ell_i=tr(R^TR)=3`, hence

`sum_i ell_i^2 <= ell_max sum_i ell_i =3 ell_max`.           (2.6)

This proves (2.4). QED.

This is strictly stronger than the previous elementary bound obtained from `det(I-S_I)` whenever the latter was estimated only by `ell_max`; it directly measures the collision probability of two random spectral bases.

## 3. Immediate target-level rank-three branch

Combining Theorem 2.2 with the completed disjoint-exterior theorem yields:

### Corollary 3.1

If an exact-rank-three spectral frame satisfies `ell_max<1/3`, then

`boxed(||p_Q||_infinity <= 12 (1-3 ell_max)^(-1/6))`.        (3.1)

In particular, if `ell_max<=1/4`,

`D0>=1/4`

and

`boxed(||p_Q||_infinity <= 12*2^(1/3) <15.120)`.             (3.2)

This is an arbitrary-law statement, not a uniform-input statement.

To apply the assigned partner's extremal-law result to the actual geometric inequality, let `J` be any interval and let `E_i` be arbitrary measurable sets of measure one. Taking `X_i` with density `1_{E_i}`, (3.2) gives

`|{x in prod_i E_i: x^T A x in J}| <= 12*2^(1/3) |J|`       (3.3)

whenever `ell_max<=1/4`. The partner's exact bang-bang theorem then lifts (3.3), with no loss, to every independent input law satisfying `0<=f_i<=1` and `int f_i=1`.

Thus the rank-three diffuse branch can be closed by the aggregate basis-collision statistic without selecting any local inverse-conditioned minor.

## 4. Applying the latest fleet02/B13 pair-incidence theorem

Now enter the nested-heavy coordinates of the assigned partner. Let

`r_i=sqrt(c)e1`, with `c>1/2`,

`r_j=rho e1+sqrt(h)e2`, with `h>1/2`,

and for residual indices `k`,

`r_k=a_k e1+b_k e2+z_k e3`.

Set

`B=1-h`,
`s=h+rho^2=||r_j||^2<=1`,
`beta=rho^2+h(1-c)`,
`Delta=(1-c)(1-h)-rho^2`,

and let

`n=(sqrt(h)e1-rho e2)/sqrt(s)`,
`u_k=<r_k,n>`,
`U=sum_k u_k^2=beta/s`,
`d_*=max_k z_k^2`.

The partner theorem defines `alpha=cB` and proves, when `alpha beta>0`, that with

`eps=d_*+D0/(4 alpha beta)`,
`theta=h Delta/(B beta)`,                                  (4.1)

there exists a residual physical coordinate `k` satisfying

`b_k^2/B >= 1/2-eps`,                                      (4.2)

`u_k^2/U >= (sqrt(max(0,1/2-eps))-sqrt(2 theta))_+^2`,     (4.3)

and always `z_k^2<=d_*`.

The point of the next calculation is to turn that asymptotic statement into a fixed quantitative collar.

### Theorem 4.1 — quantitative three-row collar away from leverage one

Fix `0<eta<1/2`. Assume

`1/2<c<=1-eta`, `1/2<h<=1-eta`,                             (4.4)

and

`d_*<=1/16`, `D0<=eta^2/64`, `Delta<=eta^2/256`.            (4.5)

Then there exists a residual physical coordinate `k` such that

`boxed(b_k^2 >= 27 eta/64 > eta/4)`,                        (4.6)

`boxed(u_k^2 >= eta/8)`,                                    (4.7)

and

`boxed(z_k^2<=1/16)`.                                       (4.8)

In particular its leverage obeys

`boxed(ell_k=||r_k||^2 > eta/4)`,                           (4.9)

and it is quantitatively separated, in the heavy spectral plane, from both the first heavy line and the second heavy line.

#### Proof

From (4.4),

`B=1-h>=eta`,

`beta=rho^2+h(1-c)>=eta/2`,

and since `c>1/2`,

`alpha beta=(cB)beta >= eta^2/4`.                           (4.10)

Therefore

`eps <=1/16 + (eta^2/64)/(eta^2)=5/64`.                    (4.11)

Also `h<=1`, while `B beta>=eta^2/2`, hence

`theta<=2 Delta/eta^2<=1/128`.                              (4.12)

Equation (4.2) now gives

`b_k^2/B >= 1/2-5/64=27/64`,

and `B>=eta` proves (4.6).

For (4.3),

`sqrt(1/2-eps)>=sqrt(27/64)=3sqrt(3)/8`,

while

`sqrt(2theta)<=1/8`.

Thus

`u_k^2/U >= ((3sqrt(3)-1)/8)^2`
`            =(28-6sqrt(3))/64`
`            >1/4`.                                        (4.13)

Since `s<=1`, `U=beta/s>=beta>=eta/2`, yielding (4.7). Equation (4.8) is immediate from the definition of `d_*`; (4.9) follows from (4.6). QED.

The two lower bounds are geometrically distinct: `|b_k|` is a lower bound on the component away from the first heavy line `Re1`, while `|u_k|` is the component in the heavy plane perpendicular to `r_j`. Thus the new row cannot collapse onto either old heavy line.

## 5. New isotropic-pivot forcing

Let

`M=||p_Q||_infinity`

for an exact-rank-three example with finite density norm. The completed universal rank-two half-Riesz/Schur theorem gives, for every physical coordinate `t`,

`boxed(|A_tt| ell_t |det Lambda| <= C2^4/M^4 = 2^19/M^4)`,   (5.1)

where (5.1) is automatic if `A_tt=0` and otherwise is just the fourth power of the cited density inequality.

Apply this to the three rows in Theorem 4.1. Since `ell_i=c>1/2` and `ell_j=s>=h>1/2`,

`boxed(|A_ii| |det Lambda| < 2^20/M^4)`,                    (5.2)

`boxed(|A_jj| |det Lambda| < 2^20/M^4)`.                    (5.3)

For the third row, (4.9) yields

`boxed(|A_kk| |det Lambda| < 2^21/(eta M^4))`.              (5.4)

Hence any unbounded-density sequence in this non-boundary nested-heavy chamber forces **three macroscopic, mutually separated physical spectral rows to become simultaneously near-isotropic for the quadratic form** in the determinant-normalized sense (5.2)--(5.4).

This is stronger than merely saying `d_*`, `Delta`, and `D0` tend to zero: it also controls the actual quadratic pivots on the three concentrated source coordinates.

## 6. Asymptotic terminal geometry for the nested-heavy obstruction

Combine the previous completed results:

- fleet03/B13 proves that any unbounded nested-heavy exact-rank-three sequence must satisfy `d_*->0` and `Delta->0`;
- the completed fleet01/B13 disjoint-exterior theorem forces `D0->0` as well;
- the assigned partner fleet02/B13 proves that if `alpha beta->0`, then after a subsequence either `c->1` or `h->1`;
- if neither `c` nor `h` tends to one, pass to a subsequence on which both are at most `1-eta` for some fixed `eta>0`, and Theorem 4.1 applies eventually.

Therefore every putative unbounded nested-heavy rank-three sequence has a subsequence in one of only two source-valid terminal geometries:

1. **Leverage-one boundary:** a physical coordinate has spectral leverage tending one (`c->1`, or `h->1`, which also forces `rho->0` and hence `||r_j||^2->1`).
2. **Three-row near-isotropic collar:** there are three original physical rows with leverage bounded below by positive constants, the third is quantitatively separated from the first two heavy directions while its transverse coefficient tends to zero, and
   `|A_tt det Lambda|->0`
   on all three rows; simultaneously the last transverse spectral direction remains distributed over residual coordinates because `sum z_k^2=1` and `d_*->0`.

The second alternative is the genuinely unresolved geometry. It is now a specific product-preserving configuration, not an arbitrary overlap-heavy frame.

## 7. Exact change in the unpaid implication

**Old unpaid implication:** `QFORM-RANK3-THREE-COORDINATE-COLLAR-CLOSURE-v1` — control a rank-three frame merely from the fact that one spectral direction has most of its mass on three coordinates.

**New proved information:** the diffuse side has the sharp collision bound (2.4), and in the nested-heavy collar any unbounded sequence away from leverage one must force a third physically distinct macroscopic row *and* simultaneous determinant-normalized pivot collapse on all three concentrated rows.

The new first unpaid implication is therefore:

> **`QFORM-RANK3-THREE-ISOTROPIC-ROWS-DIFFUSE-TRANSVERSE-v1` (OPEN).** Prove a universal slab/density bound for the source-valid geometry of three macroscopic original-coordinate rows, mutually separated in the heavy spectral plane, whose physical diagonal quadratic pivots are all small in determinant scale, while the remaining transverse spectral direction is diffuse across the other independent coordinates; or construct a genuine cap-one product-law counterexample.

A promising next attack is to aggregate the diffuse transverse bank before conditioning and combine it with a hyperbolic-square or half-Riesz mechanism on the three near-isotropic rows. One must not rotate the independent input coordinates or replace the residual projection by an arbitrary bounded joint density.

After exact rank three is closed, arbitrary additional spectral directions still require a source-valid interaction theorem. Nothing here deletes them.

## 8. Status

- Full QFORM: **OPEN / NOT PROVED**.
- New exact theorem: `D0 >= 1-sum ell_i^2 >=1-3 ell_max`.
- New target-level rank-three branch: `ell_max<=1/4` gives `||p_Q||_infinity<=12*2^(1/3)<15.120` for every admissible product law.
- Latest assigned partner `fleet02/B13@93bed74...` was used in the quantitative derivation (4.1)--(4.13), not merely cited.
- New asymptotic forcing: away from leverage one, an unbounded nested-heavy sequence must exhibit three macroscopic separated physical rows with determinant-normalized pivots tending to zero plus a diffuse transverse bank.
- No continuity claim is made here beyond scopes where imported results separately provide it.
