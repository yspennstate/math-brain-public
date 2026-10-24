SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T03:20:12Z.
attacking: the uncovered indefinite two-sheet curved integral by testing whether low leverage / one minority pivot / physical cone-cover certificates are exhaustive before aggregate-bank coarea.

# Early substantive checkpoint — a two-sheet hybrid obstruction that aggregate-bank coarea pays

Run `20260923T032012Z-account02-B05-QFORM-29fa25e8`.

Status: `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_QFORM_OPEN`.

The previous B05 checkpoint already transferred the newest-source ruled one-sheet theorem to arbitrary rough cap-one product laws at the interval level. This run does not reprove it. It attacks the opposite two-sheet side and constructs an exact target family showing that three natural physical-coordinate exits are not exhaustive, while the designated partner account03/B05 aggregate-bank theorem gives a uniform bound.

## 1. Source pins actually used

Required newest Claude package:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md` proves the ruled one-sheet estimate for exact rank-three signature `(+,+,-)`:

`ess sup_(t>=0) p_Q(t) <= pi sqrt(2)` when the three eigenvalue magnitudes are at least one.

The designated completed partner theorem is account03/B05 `QFORM-ONE-RANK2-TWO-RANK1-BANK-COAREA-v1`, run `20260922T223741Z-account03-B05-QFORM-r19`, canonical report at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T223741Z-account03-B05-QFORM-r19/REPORT.md`.

For one spectral-rank-two product bank and two spectral-rank-one product banks, with invertible indefinite scalar-bank compression `B`, `kappa=sigma_min(B)`, and aggregate principal-determinant mass `mu`, it proves

`||p_Q||_infinity <= 8*2^(3/4)*sqrt(5)*(kappa*mu)^(-1/4)`.

I also use account01/B06 `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1`, whose exact two-sheet cone-cover cost is a legitimate product-preserving physical-fibre certificate, to test whether that mechanism can be exhaustive.

## 2. Exact target family

Fix an integer `m>=1`. Let `R` have `1+3m` rows in `R^3` as follows:

* one row `r_0=e_1`;
* for each `k=1,...,m`, two mixed rows

  `r_(k,+)=(0,1/sqrt(2m), 1/(2sqrt(m)))`,

  `r_(k,-)=(0,1/sqrt(2m),-1/(2sqrt(m)))`;

* for each `k=1,...,m`, one minority-bank row

  `s_k=(0,0,1/sqrt(2m))`.

The mixed rows contribute

`sum r_(k,+)r_(k,+)^T + r_(k,-)r_(k,-)^T = diag(0,1,(1/2))`,

while the `s_k` rows contribute `diag(0,0,1/2)`. Hence

`R^T R=I_3`.

Take

`Lambda=diag(1,1,-1)`, `A=R Lambda R^T`.

Therefore the nonzero eigenvalues of `A` are exactly `{1,1,-1}` for every `m`; this is an exact target family, not a weakened spectral statement.

The physical diagonals are also exact:

`A_00=1`,

`A_(k,+),(k,+)=A_(k,-),(k,-)=1/(4m)>0`,

`A_(s_k,s_k)=-1/(2m)`.

Thus every physical coordinate of the minority sign has magnitude only `1/(2m)`.

## 3. Three natural two-sheet certificates all lose dimension

First, the full-frame Fresnel/Brascamp-Lieb low-leverage exit does not apply: row `r_0` has leverage one.

Second, every single minority-sign physical pivot is near-null. In the physical-pivot cone compiler, `L=1` and `c_i=1/(2m)`, so its bound scales as

`8 sqrt(pi e) (L/c_i)^2 = 32 sqrt(pi e) m^2`.

Third, even the aggregate curvature-weighted physical cone cover has a necessary `sqrt(m)` cost. Since `Lambda^2=I`, every transverse determinant factor is one, and the product-fibre factors satisfy `M_i>=1`. Evaluate the cone constraint at the strict minority-axis point `z=e_3`. Any admissible nonnegative weights `a_i` must satisfy

`sum_i a_i r_(i3)^2 >= 1`.

The exact cost is at least `sum_i a_i q_i`, `q_i=||r_i||`. For every row seeing `e_3`,

`q_i/r_(i3)^2 >= sqrt(2m)`:

* minority-bank rows have equality `q_i/r_(i3)^2=sqrt(2m)`;
* mixed rows have ratio `2 sqrt(3m)`.

Therefore

`Gamma_-(R,Lambda) >= sqrt(2m)`.

So the valid physical-fibre cone-cover theorem itself necessarily returns a bound growing at least like `sqrt(m)` on this family. This is not a defect in that theorem; it proves that a dimension-free proof cannot rely on this cone-cover currency alone.

The natural shortcut

> `low leverage OR a uniformly non-null minority pivot OR a uniformly bounded physical cone cover`

is therefore **not exhaustive even inside exact rank three**.

## 4. The designated partner theorem pays exactly this family

Partition the coordinates into three disjoint banks:

* `G_1`: all `2m` mixed rows; their spectral span is exactly `span(e_2,e_3)`, so this is a genuine rank-two bank;
* `G_2={r_0}`: a rank-one `e_1` bank;
* `G_3={s_1,...,s_m}`: a diffuse rank-one `e_3` bank.

For the partner notation,

`t_2=e_1`, `t_3=e_3/sqrt(2)`.

The scalar-bank compression is

`B=diag(1,-1/2)`,

so

`D=|det B|=1/2`, `kappa=sigma_min(B)=1/2`.

The aggregate determinant packet is also exact. For a mixed row `r_i` and a minority row `s_k`,

`|det A_{ {i,0,s_k},{i,0,s_k} }|
 = |det Lambda| det(r_i,e_1,s_k)^2
 = 1/(4m^2)`.

There are `2m^2` such triples, hence

`mu=1/2`.

The partner theorem therefore gives, for every choice of independent original-coordinate densities bounded by one,

`||p_Q||_infinity
 <= 8*2^(3/4)*sqrt(5)*(1/4)^(-1/4)
 = 8*2^(5/4)*sqrt(5)
 < 42.547`,

uniformly in `m`.

Combining with the required newest-source ruled theorem sharpens the majority side separately to

`ess sup_(t>=0) p_Q(t) <= pi sqrt(2) < 4.443`.

Thus the increasing-dimensional two-sheet hybrid that defeats all three physical-coordinate currencies above is still uniformly paid once the diffuse minority bank is aggregated **before** reciprocal local-pivot or cone-cover payment.

## 5. Latest partner bridge pinpoints the same lost factor

The newer account03/B05 checkpoint `20260923T024819Z-account03-B05-QFORM-auto11` proves the pair-log `L^p` receiver

`||p_Q||_infinity <= 2^(11/4)(D*kappa)^(-1/4)
                     ||p_R||_p^[p/(4(p-1))]`, `p>=2`,

without requiring independence between the pair translations and residual. Apply that bridge to the obvious physical pair consisting of `r_0` and one minority coordinate. Its principal quadratic pair is `diag(1,-1/(2m))`, so

`D=kappa=1/(2m)`,

and already

`(D*kappa)^(-1/4)=sqrt(2m)`.

Hence even arbitrarily strong residual `L^p` smoothing cannot remove the same `sqrt(m)` physical-pair tax. The aggregate-bank partner theorem removes it by paying the whole determinant packet `mu=1/2` first.

## 6. First unpaid implication

The exact remaining two-sheet obligation is sharpened to

`QFORM-TWOSHEET-AGGREGATE-BANK-OR-NEARISOTROPIC-CLOSURE-v1`:

> From a remaining indefinite/no-pivot exact-rank-three state, either extract a product-coordinate bank partition for which the partner aggregate currency `kappa*mu` is bounded below at universal scale, or prove a curved interval estimate that spends the rank-two bank's embedded third curvature when the scalar-bank compression is singular or near-isotropic (`kappa -> 0`).

The family above proves that neither diffuse leverage, individual minority diagonals, nor the physical cone-cover objective can replace the aggregate-bank step. Conversely, once `kappa*mu` is nondegenerate, the designated partner theorem already closes the two-sheet density uniformly.

Full QFORM remains open. This run changes the proof map by removing a false physical-coordinate exhaustiveness shortcut and localizing the genuinely unpaid convex-side factor to **aggregate-bank extraction versus near-isotropic scalar compression**.

## 7. Computation

`check_twosheet_hybrid.py` verifies `R^T R=I`, the nonzero spectrum `{-1,1,1}`, the exact `sqrt(2m)` cone-cost lower-bound ratio, and the two constants for `m=1,2,3,10,100`. `check_output.txt` records the actual run and ends `PASS`. The computation is regression evidence only; every identity used above has an analytic proof in the text.
