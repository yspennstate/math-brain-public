SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T08:00:10Z.
attacking: whole-active mass restoration—extend the physical-pair/Schur-bank branch through arbitrary original-coordinate diagonal bank curvature without normalizing fragments or paying support/moment taxes.

# QFORM-DIAGONAL-TWISTED-SCHUR-BANK-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account02/B14`  
Run: `20260923T080010Z-account02-B14-QFORM-r31`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM + SHARP MECHANISM OBSTRUCTION; FULL QFORM OPEN; full-target continuity OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and change

The predecessor account03/B14 r30 theorem pays an invertible indefinite ORIGINAL-coordinate pair whenever, after completing that pair, a disjoint bank has **exact rank-one** quadratic curvature. Its explicit remaining debt was higher-rank same-bank Schur curvature.

This report pays the first nontrivial higher-rank extension: the Schur bank may contain an **arbitrary original-coordinate diagonal quadratic form plus one collective rank-one square**. No diagonal coefficient is assumed small, same-sign, or bounded. The collective square may be spread over arbitrarily many original coordinates. The bound is uniform in every conditioning-generated affine term, every raw pair-to-bank coupling, outside dimension/coupling, arbitrary translations, fragmented/unbounded supports, and all moments.

The analytic input is the completed Fresnel–Brascamp–Lieb rank-one mechanism from the required Claude source. A new capped-Hoelder optimisation removes its leverage <=1/2 restriction at the exact price forced by a two-coordinate cancellation example. A Gaussian smoothing argument turns the resulting |t|^{-1/2} characteristic-function envelope into the square-root small-ball hypothesis required by the completed partner pair-log theorem.

## 2. Source-pinned inputs actually used

### 2.1 Required Claude source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The relevant proved facts are in `RESULTS.md` and `FOURIER_ROUTE_REPORT.md`:

1. for any complex `g` with `|g|<=f`, where `f` is a cap-one probability density, and every `p>=2`,

   `integral |g_hat|^p <= 4 pi / sqrt(p)`;                         (2.1)

2. Fresnel linearisation of a collective square followed by product factorisation; in the rank-one case, if `a` is unit and `max_i a_i^2<=1/2`, then arbitrary diagonal quadratic and affine twists give

   `|phi(t)| <= 2 sqrt(pi) |lambda t|^(-1/2)`.                  (2.2)

The source explicitly keeps affine terms and original-coordinate product structure. Its `COUNTEREXAMPLE_SEARCH.md` reports no target counterexample and separately confirms that localization to one physical 3x3 block is not the remaining general mechanism.

### 2.2 Designated partner account03/B14 r30

Canonical proof:
`yspennstate/math-open-problems@f762fa44abe357031aa4020eb614478ab47588e3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T073732Z-account03-B14-QFORM-r30/REPORT.md`.

For an invertible indefinite physical pair block `B`, with

`Delta=|det B|`, `kappa=sigma_min(B)`,

after exact pair completion the source pair-log theorem gives

`||p_Q||_infinity <= 4 sqrt(2H) (Delta kappa)^(-1/4)`          (2.3)

whenever the completed scalar remainder satisfies

`sup_s P(|R-s|<rho) <= H sqrt(rho)` for every rho>0.           (2.4)

Crucially, the pair translations may depend arbitrarily on the same bank variables generating `R`. This is what permits arbitrary raw pair-to-bank coupling without a false independence step.

## 3. A new rank-one separable Fourier lemma with optimal heavy-leverage exponent

Let `V_1,...,V_m` be independent real variables with probability densities bounded by one. Let `a in R^m` be unit and put

`c_i=a_i^2`, `c=max_i c_i`.

For `0<c<1` define

`eta(c)=1`,                                                     (3.1)

when `c<=1/2`, and

`eta(c)=[4c(1-c)]^(-1/4)`                                     (3.2)

when `1/2<c<1`.

### Theorem 3.1 — `QFORM-RANK1-SEPARABLE-HEAVY-LEVERAGE-v1`

For every nonzero real `lambda` and arbitrary measurable real one-coordinate phases `u_i`, the random variable

`R=lambda(a^T V)^2 + sum_i u_i(V_i)`                           (3.3)

satisfies

`boxed( |phi_R(t)| <= 2 sqrt(pi) eta(c) |lambda t|^(-1/2) )`  (3.4)

for every `t!=0`.

This contains arbitrary diagonal quadratic coefficients, arbitrary affine coefficients, and arbitrary coordinatewise translations. No support or moment hypothesis occurs.

### Proof

Fix `t!=0` and put

`g_i(x)=exp(i t u_i(x)) f_i(x)`, so `|g_i|=f_i`.               (3.5)

Rank-one Fresnel linearisation, exactly as in the proved Claude Theorem F, gives

`|phi_R(t)|`
` <= (4 pi |lambda t|)^(-1/2)`
`    integral_R prod_i |g_i_hat(a_i y)| dy`.                  (3.6)

Choose numbers `q_i` with

`0<=q_i<=1/2`, `sum_i q_i=1`, and `q_i=0` if `a_i=0`.          (3.7)

For positive `q_i`, apply Holder with exponent `p_i=1/q_i>=2`; indices with `q_i=0` are discarded using `|g_i_hat|<=1`. By (2.1),

`integral prod_i |g_i_hat(a_i y)| dy`
` <= prod_i [ |a_i|^(-1) integral |g_i_hat(s)|^(1/q_i) ds ]^(q_i)`
` <= 4 pi prod_i ( sqrt(q_i)/|a_i| )^(q_i)`
` = 4 pi exp{ (1/2) sum_i q_i log(q_i/c_i) }`.                 (3.8)

Thus the only issue is the finite-dimensional entropy minimisation

`min D(q||c)` subject to `q_i<=1/2`, `sum q_i=1`.              (3.9)

If `c<=1/2`, take `q_i=c_i`, so the minimum is zero.

If `c=c_h>1/2`, `h` is unique. The constrained entropy minimiser is

`q_h=1/2`,
`q_i=c_i/[2(1-c)]` for `i!=h`.                                (3.10)

Indeed the non-heavy coordinates are proportional to `c_i` by the Lagrange equations, and `q_i<=1/2` because each `c_i<=1-c`. Its relative entropy is

`D(q||c)`
` = (1/2) log(1/(2c)) + (1/2) log(1/[2(1-c)])`
` = (1/2) log(1/[4c(1-c)]).                                  (3.11)

Therefore the exponential factor in (3.8) is exactly `eta(c)`. Substitution into (3.6) proves (3.4). QED.

At `c=1` no finite assertion of this type is possible for arbitrary separable twists: the single-coordinate phase can cancel the collective square identically.

## 4. Fourier half-decay to square-root small ball, uniformly in translations

### Lemma 4.1 — `QFORM-FOURIER-HALF-SMALLBALL-v1`

If a real random variable `Y` satisfies

`|phi_Y(t)| <= K |t|^(-1/2)` for `t!=0`,                      (4.1)

then for every centre `s` and every `rho>0`,

`boxed( P(|Y-s|<=rho) <= c_G K sqrt(rho) )`,                  (4.2)

where

`c_G = 2^(1/4) Gamma(1/4) sqrt(2 pi e)/(2 pi)`
`    = 2.835932441509... .`                                   (4.3)

No density of `Y` is assumed.

### Proof

Let `G_rho` be an independent centred Gaussian of variance `rho^2`, with density `gamma_rho`. On `|Y-s|<=rho`,

`gamma_rho(s-Y) >= exp(-1/2)/(sqrt(2 pi) rho)`.                (4.4)

Hence

`P(|Y-s|<=rho) <= sqrt(2 pi e) rho p_(Y+G_rho)(s)`.           (4.5)

The Gaussian-smoothed law has an integrable characteristic function, so Fourier inversion and (4.1) give

`p_(Y+G_rho)(s)`
` <= (2 pi)^(-1) K integral_R |t|^(-1/2) exp(-rho^2 t^2/2) dt`
` = (2 pi)^(-1) K 2^(1/4) Gamma(1/4) rho^(-1/2).`             (4.6)

Combining (4.5)-(4.6) proves (4.2). QED.

Combining Theorem 3.1 and Lemma 4.1 gives

`boxed( sup_s P(|R-s|<=rho)`
` <= C0 eta(c) |lambda|^(-1/2) sqrt(rho) )`,                  (4.7)

where

`C0=2^(3/4) sqrt(e) Gamma(1/4)`
`  =10.053118753722... .`                                     (4.8)

This is a whole-bank estimate: no bank coordinate is conditioned on, fragmented, recentered separately, or normalized.

## 5. The diagonal-twisted Schur-bank theorem

Partition the ORIGINAL independent coordinates as

`X=(U,V,Z)`, with `U in R^2`.                                  (5.1)

Allow the full affine form

`F(X)=X^T A X + ell^T X + c0`.                                (5.2)

Let `B=A_UU` be invertible indefinite. Writing `W=(V,Z)` and `C=A_(U,W)`, define the exact Schur complement

`S=A_(W,W)-C^T B^(-1) C`.                                    (5.3)

Assume the bank principal block has the form

`S_VV = D + lambda a a^T`,                                   (5.4)

where `D` is an arbitrary diagonal matrix in the ORIGINAL `V` coordinates, `||a||_2=1`, `|lambda|>=s>0`, and

`c=max_i a_i^2<1`.                                            (5.5)

No conditions are put on `S_VZ`, `S_ZZ`, the raw pair-to-bank block, or any affine coefficient.

### Theorem 5.1 — `QFORM-DIAGONAL-TWISTED-SCHUR-BANK-v1`

Under (5.1)-(5.5), every cap-one independent product input has an essentially bounded output density and

`boxed( ||p_F||_infinity`
` <= C_* eta(c)^(1/2)`
`    [ |det B| sigma_min(B) s ]^(-1/4) )`,                    (5.6)

with

`C_* = 4 sqrt(2 C0)`
`    =17.935991751757... .`                                   (5.7)

In particular, if `c<=1/2`,

`||p_F||_infinity <= 17.936 [|det B| sigma_min(B) s]^(-1/4).` (5.8)

For `1/2<c<1`, the only additional factor is

`eta(c)^(1/2)=[4c(1-c)]^(-1/8)`.                              (5.9)

### Proof

Use the exact completion identity from partner r30. For fixed outside original coordinates `Z=z`,

`F=(U+B^(-1)g(V,z))^T B (U+B^(-1)g(V,z)) + R_z(V)`,          (5.10)

where the pair translation may depend arbitrarily on `V`, and

`R_z(V)=V^T(D+lambda aa^T)V+b(z)^T V+d(z)`.                  (5.11)

The original `V_i` remain independent cap-one variables because only `Z` was conditioned. Apply (4.7), taking the diagonal quadratic and affine pieces in (5.11) as separable phases. Uniformly in `z`, centre `w` and `rho`,

`P(|R_z-w|<=rho | Z=z)`
` <= C0 eta(c) s^(-1/2) sqrt(rho).`                           (5.12)

Thus (2.4) holds with

`H=C0 eta(c)/sqrt(s)`.                                        (5.13)

Apply the completed partner pair-log inequality (2.3), whose scope explicitly allows the `V`-dependent pair translation in (5.10):

`||p_(F|Z=z)||_infinity`
` <= 4 sqrt(2 C0 eta(c)/sqrt(s))`
`       [|det B| sigma_min(B)]^(-1/4)`,                       (5.14)

which is (5.6). The right side is independent of `z`; averaging conditional laws preserves the interval bound and hence the same essential density constant. QED.

This applies the designated partner r30 to an actual new inequality: its exact-rank-one small-ball input is replaced by (5.12), obtained from Claude's whole-bank Fresnel estimate before reciprocal pair payment.

## 6. Heavy-leverage dependence is genuinely necessary under arbitrary diagonal twists

The blow-up of `eta(c)` as `c->1` is not merely an artefact of the capped-Hoelder proof.

Take `m=2`,

`a=(sqrt(c),sqrt(1-c))`, `1/2<c<1`,                           (6.1)

and choose the diagonal twist

`D=-lambda diag(c,1-c)`.                                      (6.2)

Then

`lambda(a^T V)^2+V^T D V`
` = 2 lambda sqrt(c(1-c)) V_1 V_2`.                           (6.3)

Let `V_1,V_2` be independent uniform variables on `[-1/2,1/2]`; these are legal cap-one laws. Put

`rho_max=|lambda| sqrt(c(1-c))/2`.                             (6.4)

Since `|2 lambda sqrt(c(1-c))V_1V_2|<=rho_max` surely,

`P(|R|<=rho_max)=1`.                                          (6.5)

Therefore any uniform square-root concentration estimate

`P(|R-s|<=rho)<=H sqrt(rho)`                                  (6.6)

valid for all diagonal twists must have

`boxed( H >= sqrt(2) |lambda|^(-1/2)[c(1-c)]^(-1/4). )`       (6.7)

Our upper bound (4.7) has precisely the same power `[c(1-c)]^(-1/4)`; only the absolute constant differs. At the endpoint `c=1`, choosing `D=-lambda` makes the quadratic part vanish entirely, so no square-root small-ball estimate can be deduced from the collective-square coefficient alone.

This is a source-valid obstruction to a leverage-free **separable-twist small-ball interface**, not a counterexample to QFORM. It explains why the exact-rank-one partner theorem can be leverage-free while the arbitrary-diagonal extension cannot be: the diagonal twist can cancel the heavy self-square and leave only a weak bilinear interaction.

## 7. Target-valid diffuse stress with nonzero pair-bank coupling and diagonal curvature

Start with partner r30's diffuse coupled family. Let

`a_N=N^(-1/2)(1,...,1)`,
`B=[[0,2],[2,0]]`,
`lambda=2`,
`C_V=[(3/2)a_N^T ; 0]`.                                      (7.1)

Because `C_V^T B^(-1)C_V=0`, choose the raw bank block

`A_VV=2 a_N a_N^T + D_N`,                                    (7.2)

where `D_N` is **any diagonal matrix with ||D_N||op<=1/20**. Then the Schur bank is exactly (7.2), so Theorem 5.1 applies with `c=1/N<=1/2` for `N>=2`, `Delta=4`, `kappa=2`, `s=2`. Hence

`boxed( ||p_Q||_infinity <= C_*/2 < 8.969 )`                  (7.3)

for every `N>=2`, every such diagonal twist, and every cap-one product law.

This family remains inside the exact three-large-eigenvalue target. With `D_N=0`, the active three-dimensional matrix is

`M=[[0,2,3/2],[2,0,0],[3/2,0,2]]`,                            (7.4)

whose characteristic polynomial is

`p(x)=4x^3-8x^2-25x+32`.                                     (7.5)

One has

`p(-3)<0<p(-2)`, `p(11/10)=18/125>0>p(111/100)`, and `p(3)<0<p(4)`,

so its three eigenvalues have moduli respectively greater than `2`, `11/10`, and `3`. Adding the bank-diagonal perturbation `D_N` has operator norm at most `1/20`; Weyl's inequality leaves three eigenvalues with moduli greater than `1`. Thus (7.3) is a genuine target-level branch with:

- individual collective-square coefficients `2/N ->0`;
- individual raw pair-bank couplings `(3/2)/sqrt(N) ->0`;
- arbitrary signs and placements of the diagonal bank twist up to `1/20`;
- no restrictions on translations, fragment geometry, support diameter or moments.

The point is aggregate-before-inversion: Fresnel/Hölder pays the whole bank square and its diagonal twists before the pair-log reciprocal singularity is charged.

## 8. Localization/mixture content

The proof itself never truncates or normalizes an active bank. This is stronger than a bounded-support reduction: (3.4), (4.7) and (5.12) hold directly for arbitrary cap-one product laws and are uniform in every affine parameter generated by outside conditioning.

Consequently all localization that is actually used is zero-tax:

1. condition only on disjoint outside ORIGINAL coordinates `Z`; this preserves independence and the cap on the active `(U,V)` factors;
2. the outside realization changes only affine terms and constants in the bank after the quadratic Schur block is fixed;
3. Theorem 3.1 is uniform over those affine/separable twists;
4. average the final conditional interval bound over `Z`.

Arbitrary translations are free because `X=Y+h` changes only the affine vector while leaving `A`, `B`, the Schur complement quadratic block, `lambda`, `a`, `c`, and `D` unchanged. Fragment count, fragment separation, unbounded support and moments never enter any inequality.

By contrast, conditioning on or normalizing active fragments before (3.8) would destroy the cap-one input to the `L^p` lemma and reintroduce the previously proved fragmentation tax. The safe order is therefore: **whole active bank Fourier aggregation -> square-root small ball -> reciprocal pair payment -> outside averaging/localization**.

## 9. Remaining unpaid implication

The exact next debt is

`QFORM-NONSEPARABLE-SCHUR-CURVATURE-OR-VOLUME-EXIT-v1`:

for a surviving no-pivot/N3 configuration, after any useful physical-pair completion, either

1. expose a Schur bank whose nonseparable part has a whole-law D'/D5/near-diffuse volume certificate before active fragmentation;
2. decompose the Schur bank as diagonal plus a collective low-rank part with a quantitative capped-leverage entropy cost of the type above; or
3. use a different ridge/hub/positive-copy exit that aggregates same-bank curvature before reciprocal payment.

The present argument does **not** control an arbitrary dense higher-rank `S_VV`; nor does the bare condition `s_3(A)>=1` force a uniformly good physical indefinite pair. Full QFORM therefore remains OPEN / NOT PROVED / NOT DISPROVED. Continuity for the unrestricted target remains separate.

## 10. Constants and checks

`Gamma(1/4)=3.62560990822...`

`c_G=2.835932441509...`

`C0=10.053118753722...`

`C_*=17.935991751757...`

`C_*/2=8.967995875879...`.

The entropy minimiser (3.10), the Gaussian integral in (4.6), and the target stress eigenvalue margins were checked algebraically/numerically during the run. These checks are diagnostics only; the proof is analytic.

No hidden moment/support/log-concavity/identical-law/rotation-independence assumption is used. No full-target continuity claim is made.
