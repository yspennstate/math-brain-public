# account02/B10 — near-null physical hub: cross-curvature compression identity and a target-valid obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMA / LOCAL_ROUTE_COUNTEREXAMPLE / FULL_QFORM_OPEN`.

## First unpaid implication

`QFORM-TWOSHEET-NEARNULL-WEAKCURVATURE-INTERPOLATION-v1`:

In the exact-rank-three heavy physical-hub state, account03/B10 r24 now pays the entire **exact-null** endpoint. The source ruled theorem pays the one-sheet side for every indefinite rank-three target. What remains is therefore genuinely the **nonzero near-null two-sheet collar**. The algebra below shows that this collar has only one new degenerating curvature scalar: the determinant of the compression of the spectral matrix to `(Mr)^perp`, exactly

`a det(M) / ||Mr||^2`, where `a=r^T M r`.

A proof must interpolate through that scalar without treating a small coefficient as a small random perturbation and without declaring spectral projections independent.

## Setup

Write the exact-rank-three target as

`A = U M U^T`, `U^T U = I_3`,

where `M` is real symmetric and all three eigenvalues obey `|lambda|>=1`. Thus `sigma_min(M)>=1` and `D:=|det M|>=1`.

Let a physical row be

`u_0 = sqrt(h) r`, `||r||=1`,

with `h>55/64` in the surviving heavy-hub branch. Put

`a = r^T M r`, `k = M r`, `kappa = ||k||`.

Then `kappa>=1`. If `|a|<1`, `M` cannot be definite, because a definite target with `|lambda|>=1` has `|r^T M r|>=1` for every unit `r`. Hence the near-null collar is automatically an indefinite-signature problem.

No probabilistic operation below rotates the input. The spectral coordinates are used only for deterministic matrix identities; all density statements are invoked back on the original product coordinates.

## 1. The ruled side is already paid

Assume inertia `(2,1)` and write the spectral eigenvalues as `lambda_1,lambda_2,-mu`, all at least one in magnitude. The completed ruled theorem in the required source record gives, for every `s>=0`,

`p_Q(s) <= (lambda_1 lambda_2 mu)^(-1/2)
             integral_0^(2pi) [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta
          <= pi sqrt(2)`.

For inertia `(1,2)`, the same statement applies after replacing `Q` by `-Q`, so the corresponding one-sheet side is `s<=0`.

Thus the near-null work must not re-prove this side. The only level-set geometry still relevant here is the opposite, two-sheet side.

## 2. Cross-curvature compression identity

Let `v=k/kappa`, and let `E` be any `3 x 2` matrix with orthonormal columns spanning `v^perp`. Define the two-dimensional compression

`C = E^T M E`.

### Lemma (`QFORM-NEARNULL-CROSSCURVATURE-IDENTITY-v1`)

`det C = a det(M) / kappa^2`.

Moreover one eigenvalue of `C` has absolute value at least one. Consequently, if `theta_strong` denotes such an eigenvalue and `theta_weak` the other one, then

`|theta_strong| >= 1`,

`|theta_weak| = |a| D / (kappa^2 |theta_strong|) <= |a| D / kappa^2`.

### Proof

For any invertible symmetric `3 x 3` matrix and unit vector `v`, the determinant of the compression to `v^perp` is the corresponding cofactor:

`det(E^T M E) = det(M) v^T M^(-1) v`.

Here `v=k/kappa` and `k=Mr`, so

`v^T M^(-1) v = k^T M^(-1) k / kappa^2
                 = r^T M r / kappa^2
                 = a/kappa^2`.

This gives the determinant identity.

For inertia `(2,1)`, order the eigenvalues `lambda_1>=lambda_2>=1>0>lambda_3`. Cauchy interlacing for the two-dimensional compression gives

`lambda_1 >= theta_1 >= lambda_2 >= theta_2 >= lambda_3`,

hence `theta_1>=1`. For inertia `(1,2)`, apply the same argument to `-M`; one compressed eigenvalue is at most `-1`. The formula for the other eigenvalue follows from the determinant identity. QED.

A second elementary but useful identity is

`||P_(r^perp) M r||^2 = kappa^2-a^2 >= 1-a^2`.

Thus for `|a|<=1/8` the hub-to-transverse cross coupling is at least `sqrt(63/64)`. The collar is not a weak-star regime: it is a **strong cross coupling plus one weak compressed curvature** regime.

## 3. The designated partner retires the exact-null debt

The latest designated partner account03/B10 r24 proves `QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1`: if `a=0`, the physical hub has leverage `h`, every complementary transverse leverage is at most `1/2`, and `D=|det M|`, then

`||p_Q||_infinity <= 3*2^(4/3) (hD)^(-1/3)`.

In the inherited concentrated branch `h>55/64`, `D>=1`, this is

`||p_Q||_infinity < 7.952`.

Therefore the previous account02/B10 punctured-union exact-null debt is obsolete: the complete exact-null survivor is already paid. The present run does not repeat that proof.

For `a!=0`, the already reviewed physical-pivot theorem gives the real inequality

`||p_Q||_infinity <= 128 [h |A_00| D]^(-1/4)
                       = 128 [h^2 |a| D]^(-1/4)`.

So every fixed `|a|>=delta>0` is paid, but this estimate diverges like `delta^(-1/4)` and therefore does not interpolate to the partner's finite exact-null endpoint.

## 4. Target-valid family showing the weak curvature can really vanish

Fix `h=7/8`. For `0<eps<=1/8`, put

`c_eps = sqrt(1+eps)`,

`M_eps = [[eps,c_eps,0],[c_eps,0,0],[0,0,1]]`.

The `2 x 2` block has eigenvalues `1+eps` and `-1`, so

`spectrum(M_eps)={1+eps,1,-1}`.

For any integer `m>=2`, make a Parseval physical frame from the rows

- `sqrt(h)e_1`;
- `sqrt(1-h)e_1`;
- `m` copies of `e_2/sqrt(m)`;
- `m` copies of `e_3/sqrt(m)`.

Then `U^T U=I_3`, so `A_(eps,m)=U M_eps U^T` has the same three nonzero eigenvalues and is an exact target matrix. Every nonhub transverse leverage is `0` or `1/m<=1/2`.

For `r=e_1`,

`a=eps`, `k=(eps,c_eps,0)`, `kappa^2=1+eps+eps^2`.

An orthonormal basis of `k^perp` is

`w=(c_eps,-eps,0)/kappa`, `e_3`.

In that basis the compression is diagonal with eigenvalues

`1`,

`theta_eps = - eps(1+eps)/(1+eps+eps^2)`.

Thus the strong compressed curvature stays exactly one while the other curvature tends to zero linearly with the near-null pivot. This is not an artifact of estimates; it is the exact compression.

The same family also defeats a return to one local physical certificate. Its largest scalar pivot is at most

`max((7/8)eps,1/m)`;

its largest principal-pair determinant is at most

`(7/8)(1+eps)/m`;

and every nonsingular principal triple uses one `e_1`, one `e_2`, and one `e_3` row, so its determinant magnitude is at most

`(7/8)(1+eps)/m^2`.

Taking, for example, `m=ceil(1/eps)` sends all three local certificate scales to zero while the target spectrum stays `{1+eps,1,-1}`.

This is a counterexample only to a proposed **uniform local-certificate/second-compressed-curvature** bridge, not to QFORM.

## 5. The obstruction family itself is uniformly safe by source-valid bank aggregation

The construction has three disjoint original-coordinate banks. Set

`Z_1=sqrt(h)X_0+sqrt(1-h)X_1`,

`Z_2=m^(-1/2) sum_(j=1)^m Y_j`,

`Z_3=m^(-1/2) sum_(j=1)^m W_j`.

The three variables are independent because their source-coordinate banks are disjoint. Each is a norm-one linear projection of a product density with one-dimensional marginals bounded by one, hence has density at most `sqrt(2)`. Therefore `V_j=sqrt(2) Z_j` are independent and have densities at most one, while

`Q = Z^T M_eps Z = (1/2) V^T M_eps V`.

The completed three-coordinate theorem in the required source record applies to the matrix `M_eps/2`, whose smallest eigenvalue magnitude is `1/2`, and yields the actual uniform bound

`||p_Q||_infinity <= 12 sqrt(pi) < 21.270`.

So the family is a clean structural obstruction with no density blow-up.

Independently, the ruled theorem above gives the sharper one-sheet statement `p_Q(s)<=pi sqrt(2)` for every `s>=0` in this `(2,1)` family.

## 6. What is now genuinely left

The exact-null endpoint is paid by account03/B10 r24; every fixed nonzero pivot is paid by the physical-pivot/half-Riesz theorem; and the one-sheet side is paid by the source ruled theorem. The surviving piece is therefore sharply identified:

> For an indefinite exact-rank-three target with a heavy original physical row `sqrt(h)r`, `h>55/64`, complementary transverse leverage at most `1/2`, and `0<|a|=|r^TMr|<<1`, prove a **uniform two-sheet-side bound** through the transition where the compression to `(Mr)^perp` has one strong curvature and determinant `a det(M)/||Mr||^2` tending to zero.

The proof must use the strong star `||P_(r^perp)Mr||>=sqrt(1-a^2)` jointly with the strong compressed curvature. A method that asks the second compressed curvature, a single physical pivot, a single physical pair, or a single physical triple to stay uniformly nonzero is false by the explicit family above. A method that deletes the `a(r dot U^T X)^2` term as a small random perturbation is also invalid under the source class because supports and moments are unrestricted.

This is `QFORM-TWOSHEET-NEARNULL-WEAKCURVATURE-INTERPOLATION-v1`.

## Source pins actually used

- Required interactive source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md` Theorems A and C, together with the companion `RESULTS.md` / `FOURIER_ROUTE_REPORT.md` record.
- Designated partner: account03/B10 r24, brain handoff `20260923T114517Z-account03-B10-QFORM-r24.md`, canonical mathematics `yspennstate/math-open-problems@c0d7e6eb88886ee1f78a5eef0f80d9b220139e45`.

Execution remained `WITHOUT_VERIFIED_BRAIN`. Continuity is not claimed for the new collar reduction.
