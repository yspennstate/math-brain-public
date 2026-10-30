SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-24T10:05:30Z.
attacking: target-level source regularity for diffuse rank-three forms, plus an L-infinity obstruction to operator-norm approximation; continuity remains downstream of height.

# fleet01/B15 — low-leverage full-law source Lipschitz stability; operator norm is not an L-infinity regularity metric

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner problem revision `2026-09-22.5`.
**Status:** `NEW_LOWER-LEVERAGE_SUBMASS_THEOREM / NEW_FULL-LAW_SOURCE_STABILITY / PARTNER_APPLIED / FULL_QFORM_OPEN`.
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner theorem remains **OPEN**. This report proves two regularity statements that keep the central height issue separate:

1. on the exact-rank-three diffuse chamber, a completed full-law height theorem can be made **linear in submass**, yielding a dimension-free `L1(source) -> L-infinity(output density)` Lipschitz estimate; and
2. matrix operator norm by itself cannot furnish any target-uniform continuity of the canonical output densities in `L-infinity`, even modulo output translations.

No law-uniform pointwise quadratic Fourier decay, post-rotation independence, projection-only closure, arbitrary-joint coarea cap, or conditional-cap substitution is used.

## 1. Inputs used at their exact scopes

### 1.1 Completed Fresnel--Brascamp--Lieb theorem

Source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem F.

Its all-coordinate corollary is the following. Let

`A = R Lambda R^T + D`,

where `R in R^{n x 3}` has orthonormal columns, `D` is diagonal, and the three diagonal entries of `Lambda` are nonzero. If every spectral-row leverage

`a_j = ||R_{j,*}||_2^2`

is at most `1/2`, then for arbitrary independent cap-one marginals and arbitrary affine terms,

`||p_Q||_infinity <= 12 |det Lambda|^{-1/3}`.                 (1.1)

This is a full-law theorem obtained from an integrated Fresnel/Brascamp--Lieb estimate. It is not the false pointwise one-direction decay shortcut.

### 1.2 Completed fleet02/B15 diffuse-bank theorem

Latest designated-partner source consumed in full:

`yspennstate/math-open-problems@bf69cf77d11855ed6a9edcfa10aa200343766b1e`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260924T091516Z-fleet02-B15-QFORM-auto11-r1/REPORT.md`.

For

`A_m = J_m/m direct_sum J_m/m direct_sum (-J_m/m)`,

fleet02/B15 proves

`spec(A_m)={1,1,-1,0,...,0}`,                                      (1.2)

and, for every physical subset `S` of size `r`,

`max_{|S|=r} s_3((A_m)_{S,S}) = floor(r/3)/m`.                     (1.3)

Thus bounded-size physical localization loses all three-curvature scale as `m -> infinity`. Nevertheless, writing the three independent normalized bank sums as `Y_1,Y_2,Y_3`, it proves directly

`||p_{Y_1^2+Y_2^2-Y_3^2}||_infinity <= 2 pi`.                     (1.4)

The preceding fleet02/B15 completed regularity source

`yspennstate/math-open-problems@847a25a6130a1470eb8f1abbb298ae5e5f1cdc8f`

also gives the majority-sheet rough-law stability `<=2 pi Delta` when the spectral frame has leverage at most `1/2`. The new statements below concern the **full law**.

## 2. Main new lemma: coordinate contraction preserves the low-leverage Fresnel chamber

Let

`A = R Lambda R^T + D`,                                             (2.1)

where `R^T R=I_3`, `D` is diagonal, and put

`theta = max_j a_j`, `a_j=||R_{j,*}||^2`.

Assume

`theta <= 1/3`.                                                     (2.2)

Fix coordinate `i`. Replace its probability density by a cap-one subdensity `h`, of mass

`0 <= m <= 1`.                                                      (2.3)

Let `nu_{i,h}` be the resulting output submeasure for the quadratic-affine polynomial

`Q(x)=x^T A x+b^T x+c`.                                             (2.4)

### Theorem 2.1 — `QFORM-LOWLEVERAGE-LINEAR-SUBMASS-v1`

If the three rank-three coefficients in `Lambda` are nonzero, then `nu_{i,h}` has a bounded density and

`boxed:
 H(nu_{i,h})
 <= 12 m { |det Lambda| [1-(1-m^2)a_i] }^{-1/3}
 <= 12 m { |det Lambda|(1-theta) }^{-1/3}.`                        (2.5)

Here `H(nu)=sup_I nu(I)/|I|`, equivalently the essential density height.

In particular, when `|lambda_k|>=1`,

`boxed: H(nu_{i,h}) <= 12 (1-theta)^(-1/3) m.`                     (2.6)

At the endpoint `theta=1/3`, the coefficient is

`12(3/2)^(1/3) = 13.7365709106...`.                                (2.7)

### Proof

The case `m=0` is trivial. Assume `m>0`. Scale **only the original coordinate**

`x_i = m z_i`,                                                      (2.8)

and define

`g_i(z)=h(mz)`.                                                     (2.9)

Then `0<=g_i<=1` and

`integral g_i(z) dz = 1`,                                          (2.10)

while

`h(x_i) dx_i = m g_i(z_i) dz_i`.                                  (2.11)

Thus `nu_{i,h}` is exactly `m` times the probability output law for the cap-one product input in `z` and the congruently scaled quadratic matrix

`A_m = S_m A S_m`,                                                  (2.12)

where `S_m` is diagonal and equals `m` at coordinate `i` and one elsewhere. The affine coefficient is simply changed to `S_m b`; Theorem F is uniform in affine terms.

Write the `i`-th row of `R` as the vector `r in R^3`, and set

`a=|r|^2=a_i`.                                                      (2.13)

For the scaled rank-three factor

`U=S_m R`,                                                          (2.14)

its Gram matrix is

`G=U^T U = I_3-(1-m^2) r r^T`.                                     (2.15)

Put

`d=1-(1-m^2)a`.                                                     (2.16)

Since `a<=1/3`, `d>0`. By the determinant lemma and Sherman--Morrison,

`det G=d`,                                                          (2.17)

`G^{-1}=I_3 + (1-m^2)d^{-1} r r^T`.                                (2.18)

Whiten the scaled frame:

`W=U G^{-1/2}`, so `W^T W=I_3`.                                    (2.19)

Then

`U Lambda U^T
 = W (G^{1/2} Lambda G^{1/2}) W^T`.                                (2.20)

Orthogonally diagonalize the middle `3x3` matrix. This does **not** assert independence after rotation: it only changes the spectral basis inside the already-whitened rank-three quadratic matrix, while Theorem F continues to act on the original product coordinates. Row leverage is unchanged by this internal orthogonal change.

For the scaled coordinate itself,

`ell_i = m^2 r^T G^{-1}r = m^2 a/d <= a <= theta`.                 (2.21)

For `j != i`, writing the original `j`-th row as `r_j`,

`ell_j
 = a_j + (1-m^2)d^{-1}<r_j,r>^2
 <= a_j + (1-m^2)d^{-1}a_j a
 = a_j/d
 <= theta/(1-theta)
 <= 1/2`.                                                          (2.22)

Thus the **normalized** scaled probability problem still lies in the completed Theorem-F leverage chamber.

Let `Lambda_m` be the three nonzero eigenvalues after whitening/diagonalization. Their absolute product is

`|det Lambda_m|
 = |det(G^{1/2} Lambda G^{1/2})|
 = d |det Lambda|`.                                                 (2.23)

The scaled diagonal remainder `S_m D S_m` is still diagonal. Applying (1.1) to the normalized product law gives

`||p_scaled||_infinity
 <=12 [d |det Lambda|]^(-1/3)`.                                    (2.24)

Finally (2.11) multiplies the output submeasure by the original mass `m`, proving (2.5). No conditioning, rotated-product assumption, or pointwise oscillatory estimate occurs.

## 3. Full-law source Lipschitz continuity in the low-leverage chamber

Let `f=(f_j)` and `g=(g_j)` be two cap-one product probability laws for the same matrix (2.1), and put

`delta_j=||f_j-g_j||_1`, `Delta=sum_j delta_j`.                     (3.1)

### Corollary 3.1 — `QFORM-LOWLEVERAGE-SOURCE-LIPSCHITZ-v1`

Under `theta<=1/3`,

`boxed:
 ||p_f-p_g||_infinity
 <=12 {|det Lambda|(1-theta)}^(-1/3) Delta.`                       (3.2)

If `|lambda_k|>=1`, this is

`boxed:
 ||p_f-p_g||_infinity
 <=12(1-theta)^(-1/3) Delta
 <=13.737 Delta.`                                                   (3.3)

### Proof

Telescope the product law one original coordinate at a time. For a one-coordinate replacement, let

`c_j=min(f_j,g_j)`,
`u_j=(f_j-g_j)_+`, `v_j=(g_j-f_j)_+`.                               (3.4)

The two residuals are cap-one subdensities with equal mass `delta_j/2<=1`. The signed output difference is the difference of the two corresponding output submeasures. Applying (2.5) to each sign and summing gives the `j`-th contribution at most

`12 {|det Lambda|(1-theta)}^(-1/3) delta_j`.                       (3.5)

Summing the telescope proves (3.2).

This is a genuine class-uniform **source-law regularity estimate**. It is stronger than the qualitative fixed-matrix `C_0` theorem, but it does not solve the universal height conjecture outside this completed low-leverage rank-three-plus-diagonal chamber.

### Consequence for rough-to-smooth passage

Cap-preserving compact-smooth approximants can be chosen with aggregate marginal error `Delta_k->0`. Equation (3.2) makes their output densities uniformly Cauchy. Smooth fixed-instance outputs are in `C_0`; hence the rough output inherits a canonical `C_0` representative. The height is still the separately paid Theorem-F height; continuity is downstream.

## 4. Sharper full-law stability on the partner's diffuse three-bank family

The generic constant above is not optimal on the disjoint-bank family (1.2). Here the bank independence can be retained all the way through the two-square receiver.

Let two admissible product arrays `F,G` be given for the same `A_m`, `m>=2`. Define bankwise source distances

`Delta_k = sum_{j=1}^m ||f_{k,j}-g_{k,j}||_1`.                      (4.1)

### Proposition 4.1 — full-law bank stability

The canonical full output densities satisfy

`boxed:
 ||p_F-p_G||_infinity
 <= 2 pi sqrt(m/(m-1)) (Delta_1+Delta_2)
    + 2 pi Delta_3.`                                                (4.2)

In particular,

`boxed:
 ||p_F-p_G||_infinity
 <=2 pi sqrt(m/(m-1)) (Delta_1+Delta_2+Delta_3)
 <=2 pi sqrt(2) Delta.`                                             (4.3)

Moreover, for every one of these rough product laws,

`boxed: p_F in C_0(R),   ||p_F||_infinity<=2 pi.`                  (4.4)

### Proof

The partner theorem gives the full bank projection cap

`||p_{Y_k}||_infinity<=sqrt(2)`.                                   (4.5)

Suppose first that one marginal in positive bank 1 is replaced by a subdensity of mass `u`. Separate that coordinate from the other `m-1` coordinates. The normalized sum of those remaining variables has cap `sqrt(2)`; rescaling from `1/sqrt(m-1)` to `1/sqrt(m)` gives the leave-one-out cap

`||p_W||_infinity <= sqrt(2m/(m-1))`.                              (4.6)

Convolution with the selected subdensity has total mass `u`, so the resulting bank-1 submeasure has density cap

`M_1 <= u sqrt(2m/(m-1))`.                                         (4.7)

For any scalar measure with density cap `M`, its square pushforward satisfies

`p_{Z^2}(s)<=M/sqrt(s)`, `s>0`.                                    (4.8)

The untouched bank 2 has `M_2=sqrt(2)`. Therefore the beta integral gives

`||p_{Y_1^2+Y_2^2}^{(sub)}||_infinity
 <= pi M_1 M_2
 <=2 pi u sqrt(m/(m-1))`.                                          (4.9)

Convolution with the independent probability law of `-Y_3^2` preserves that height. The same holds for a perturbation in bank 2.

If instead the changed factor is in negative bank 3, use the partner's already-paid positive receiver

`||p_{Y_1^2+Y_2^2}||_infinity<=2 pi`.                              (4.10)

The negative-square submeasure has total mass `u`, so convolution gives height at most `2 pi u`. Common-part decomposition and telescoping now give (4.2).

For continuity, put `R=Y_1^2+Y_2^2`; (4.10) gives a probability density `r in L1 cap Linfinity`. Since `Y_3` is absolutely continuous, `-Y_3^2` has an `L1` probability density `h`. The full density is

`p_F=r*h`.                                                          (4.11)

Translation continuity of `h` in `L1` gives

`||tau_s p_F-p_F||_infinity
 <=||r||_infinity ||tau_s h-h||_1 ->0`.                            (4.12)

Also `p_F in L1`; a uniformly continuous integrable function vanishes at infinity. Hence `p_F in C_0`, and Young gives the same `2 pi` height. Continuity is proved after the height receiver is paid.

### Relation to the designated partner result

Fleet02/B15 proved only the majority-sheet Lipschitz estimate `<=2 pi Delta` in the diffuse leverage chamber. Equations (4.2)--(4.4) are a **full-law** closure for this canonical diffuse family, including the complementary sheet that remains unresolved in general.

At `m=100`, for example,

`||p_F-p_G||_infinity <= 2 pi sqrt(100/99) Delta < 6.315 Delta`,    (4.13)

while the partner's exact structural formula (1.3) says that every physical principal block using at most 30 coordinates has

`s_3<=0.1`.                                                         (4.14)

This is a concrete aggregate-before-localization regularity inequality.

## 5. New negative result: operator norm is not an L-infinity density-continuity metric

The latest fleet02/B15 report contains a remote-support perturbation showing that an arbitrarily small additional operator coefficient cannot be discarded by uniform total-variation continuity. Its same construction gives a direct `L-infinity` obstruction for the canonical output densities.

Take the partner family with `m=2` and adjoin one extra coordinate:

`A_0=A_2 direct_sum [0]`,
`A_e=A_2 direct_sum [e]`, `0<e<1`.                                 (5.1)

Both are owner-target matrices because the first three nonzero eigenvalues remain `{1,1,-1}`. Moreover

`||A_e-A_0||_op=e`.                                                 (5.2)

Use iid `Uniform[-1/2,1/2]` in the six bank coordinates. For the extra coordinate use, **for both matrices**, the same cap-one law

`X_0 ~ Uniform[R,R+1]`,
`R=3/e`.                                                            (5.3)

For `A_0`, the extra coordinate is invisible. The base output is supported on

`E_2=[-1/2,1]`, `|E_2|=3/2`.                                       (5.4)

Hence every density representative obeys

`||p_0||_infinity >= 1/|E_2| = 2/3`.                               (5.5)

For `A_e`, write `Z=eX_0^2`. The monotone change of variables gives

`p_Z(z)= [2 sqrt(ez)]^{-1}
         1_[eR^2,e(R+1)^2](z)`,                                    (5.6)

so

`||p_Z||_infinity=1/(2eR)=1/6`.                                   (5.7)

Because `Q_e=Q_0+Z` with independent summands,

`||p_e||_infinity<=1/6`.                                           (5.8)

Translation does not alter density height. Therefore, for every deterministic `c`,

`||p_0-tau_c p_e||_infinity
 >= ||p_0||_infinity-||p_e||_infinity
 >= 2/3-1/6
 =1/2`.                                                            (5.9)

We have proved:

### Proposition 5.1 — `QFORM-NO-OPNORM-TO-LINF-UNIFORM-CONTINUITY-v1`

For every `delta>0` there are two same-dimensional owner-target matrices `A_0,A_e` with

`||A_e-A_0||_op<delta`,                                             (5.10)

and one common cap-one product input law for the pair, such that their canonical bounded continuous output densities satisfy

`boxed:
 inf_{c in R} ||p_{A_0}-tau_c p_{A_e}||_infinity >=1/2.`            (5.11)

Choose simply `e<min(delta,1)` in (5.1)--(5.3). The fixed-matrix rank>=3 regularity theorem ensures both laws have canonical `C_0` representatives; the lower bound itself uses only support normalization and the partner's exact remote-square cap.

Thus a proof of full QFORM cannot approximate a general target matrix by an operator-near simpler matrix and then invoke any law-uniform `L-infinity` continuity principle under the owner's unrestricted-support source class. Operator-small tails must be retained exactly or absorbed by a translation-uniform product-preserving analytic estimate.

This is a proof-interface obstruction, not a QFORM counterexample: both outputs are bounded, and in fact the perturbed one is flatter.

## 6. Regularity ledger after this run

The logical separation is now particularly clean.

**Absolute continuity.** For any nonconstant quadratic-affine polynomial and any absolutely continuous joint input, the scalar pushforward is absolutely continuous by the qualitative coarea/null-set argument. This has no height content.

**Fixed-instance boundedness and continuity.** The completed fixed-matrix theorem at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`

proves `C_0 cap L-infinity` for every fixed rank>=3 cap-one product instance, with matrix-dependent constants.

**Universal height.** Still OPEN. It is the only owner-wide quantitative constant sought.

**Source-law regularity.** New Theorem 2.1/Corollary 3.1 give a universal linear submass and source-Lipschitz modulus on the low-leverage rank-three-plus-diagonal chamber. Proposition 4.1 sharpens it on the canonical diffuse bank family and closes the full law there.

**Matrix regularity.** Proposition 5.1 shows there is no owner-wide operator-norm modulus into output-density `L-infinity`, even after arbitrary output translation. Hence matrix approximation and source approximation behave fundamentally differently.

The first unpaid implication for B15 remains the general complementary two-sheet/higher-rank aggregate receiver while preserving original-coordinate product provenance. The diffuse-bank results show regularity itself is not the obstruction once aggregation has actually been paid.

## 7. Corrections preserved

Nothing here uses or asserts:

- uniform pointwise decay of `E exp(itX^TAX)`;
- independence of spectral coordinates after rotating the quadratic form;
- a projection/X-ray-only bound for the two-sheet side;
- the false arbitrary-joint rank-three coarea density estimate;
- conditional cap preservation under non-product conditioning;
- a uniformly good bounded-size physical principal block under `s_3(A)>=1`;
- operator-norm continuity of output laws or density heights.

The last item is now explicitly refuted in the stronger `L-infinity` form (5.11).

## 8. Source pins

- Theorem F: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
- Fixed-matrix rank>=3 regularity: `math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T200544Z-fleet02-B15-qform-r11/REPORT.md`.
- Designated fleet02/B15 diffuse-bank obstruction/full-law bound: `math-open-problems@bf69cf77d11855ed6a9edcfa10aa200343766b1e`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260924T091516Z-fleet02-B15-QFORM-auto11-r1/REPORT.md`.
- Designated fleet02/B15 leverage-sensitive majority stability: `math-open-problems@847a25a6130a1470eb8f1abbb298ae5e5f1cdc8f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260924T070011Z-fleet02-B15-qform-auto11-r1/REPORT.md`.
- Fresh owner/control re-read immediately before publication: `math-research-brain@2509ad32c6aa044df199279ea8f3dd20d4cc6ff9`, owner revision `2026-09-22.15`; no B15 stop/pause.
