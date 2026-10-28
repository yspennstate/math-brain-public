SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T09:29:31Z.
attacking: QFORM-DIFFUSE-RESIDUAL-THIRD-DIRECTION-COUPLING-v2 — extract a target-scale physical third direction or a quantitatively spectral-diffuse remainder from the retained r49/r52 residual and couple it to the BL-compatible rank-two light skeleton without discarding the cross tail.

# account03/B19 r55 — deleted-self-column third-compound promotion and rank-four common-plane collapse

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT COMPILER / PARTNER MECHANISM APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native authenticated brain ingestion.

Continuity: the physical-`E3` exit below has a continuous `C_0` density. The complementary structural collar is deterministic only; full-target continuity remains **OPEN**.

Every set below is a set of literal ORIGINAL coordinates. Orthogonal changes of basis are used only inside deterministic coefficient-space determinant identities; no rotated random coordinates are declared independent. All input laws remain arbitrary independent real laws with densities bounded by one. No Gaussianity, moments, log-concavity, compact/connected support, iid assumption, arbitrary-joint coarea bound, fiber-supremum bound, or law-uniform pointwise oscillatory decay is used. No nonzero coefficient tail is dropped.

## 1. Source-pinned live frontier


The immediate robust crossing is account03/B19 r51:

`yspennstate/math-open-problems@bcb36a7573a7e9f23f1ea78792e0b72bc8bb0d9c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T060028Z-account03-B19-QFORM-r51/REPORT.md`.

It supplies an actual literal light-light cross block

`M=A[R,C]`

with a rank-two approximant `M_0` satisfying

`||M-M_0||_F<tau`, `tau=2^-16`,                                  (1.1)

`s_2(M)>sigma_*`, `sigma_*=4089/458752=0.008913312639508928...`, (1.2)

and the left/right rank-two coefficient planes of `M_0` have normalized physical row leverage at most `1/2`. The same source retains the entire nonzero tail `M-M_0` in the actual law.

The earlier common-plane rigidity lemma is account03/B19 r49:

`yspennstate/math-open-problems@35b71af9bbf9feb9542681486f190155c71ff247`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T040014Z-account03-B19-QFORM-r49/REPORT.md`, Lemma 3.1.

The designated partner input actually used is account04/B19 r4:

`yspennstate/math-open-problems@332842522b31419442774a27cfb21cd15e19d1b0`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260924T071532Z-account04-B19-QFORM-r4/REPORT.md`,

`QFORM-DOUBLEANCHOR-AGGREGATE-THIRDARM-v1`.

Its determinant engine is the exact Cauchy--Binet identity

`E_3([u v W]) >= det Gram(u,v) ||P_{span(u,v)^perp}W||_F^2`,      (1.3)

and it couples this to the completed marginal-free physical-`E3` receiver

`||p_Q||_infinity <= 6^(4/3) E_3(B)^(-1/6)`,                     (1.4)

with continuous `C_0` density for a literal physical cross block `B`, retaining arbitrary same-bank terms and outside couplings. The present run applies that engine to the live r51 crossing after a determinant-only orthogonalization of its high-cardinality physical column bank. This is not a probabilistic rotation.

Fresh account01/B19 r55 was also read before this write. Its scalar-pivot positive-tetrad theorem already pays the nonzero-pivot aggregate-`W_2` scope, so this run does not duplicate that scope; it attacks the pivot-free robust-crossing/self-curvature interface instead.

## 2. Top-two physical planes of the actual crossing remain diffuse

Let `P_0` be the left range projection of the rank-two approximant `M_0`. By r51,

`max_i (P_0)_{ii} <=1/2`.                                        (2.1)

Let `P` be the top-two left singular projection of the ACTUAL `M`. Since `M_0` has

`s_2(M_0)>=1/112`

and (1.1) holds, Weyl gives (1.2). Let `U` be an orthonormal basis of `range(P)` and `Sigma_hat` the top-two singular-value diagonal of `M`. If `Q_0=I-P_0`, the singular-vector equation gives exactly

`Q_0 U Sigma_hat = Q_0 (M-M_0) V`,                               (2.2)

for the corresponding two right singular vectors `V`. Therefore

`||Q_0 U||_op <= tau/s_2(M) < tau/sigma_* = 7/4089`.             (2.3)

The two subspaces have equal dimension, so the standard principal-angle identity gives

`||P-P_0||_op <= theta`, `theta=7/4089=0.0017119100024455857...` (2.4)

and hence every physical leverage of the ACTUAL top-two plane satisfies

`ell_i=P_ii <=1/2+theta`.                                        (2.5)

Put

`c_0=1/2-theta=4075/8178=0.4982880899975544...`.                 (2.6)

The identical statement holds for the actual top-two RIGHT singular plane of `M`.

This step is important: all subsequent promoted blocks use the actual `M`, not its rank-two truncation.

## 3. New theorem: a deleted same-bank column promotes the crossing to physical E3

### Theorem 3.1 — `QFORM-DELETED-SELF-COLUMN-PROMOTES-R2-TO-E3-v1`

Fix `j in R`, put `S=R\{j}`, and define the literal deleted self-column

`d_j=A[S,j]`.                                                     (3.1)

Let `U_S` be the restriction to `S` of an orthonormal top-two left singular frame `U` of the actual `M`, and put

`rho_j=dist(d_j,range(U_S))`.                                     (3.2)

Then the literal physical cross block

`B_j=A[S,C union {j}]=[M[S,C]  d_j]`                              (3.3)

satisfies

`boxed: E_3(B_j) >= s_1(M)^2 s_2(M)^2 (1-ell_j) rho_j^2.`         (3.4)

In particular, in the r51 robust branch,

`boxed: E_3(B_j) > c_0 sigma_*^4 rho_j^2.`                        (3.5)

The transpose statement holds for every `j in C`.

#### Proof

Extend the top-two right singular vectors of the ACTUAL `M` to an orthogonal basis of the coefficient space `R^C`. Right multiplication of the matrix in (3.3) by the corresponding block-orthogonal matrix preserves all singular values and hence preserves `E_3=e_3(B_jB_j^T)`. This is only a coefficient calculation; no random variable is transformed.

In that coefficient representation the first two columns of `M[S,C]` are

`s_1(M) u_1[S]`, `s_2(M) u_2[S]`.                               (3.6)

The part of the third-compound energy using precisely those two columns and the appended physical column `d_j` is, by Cauchy--Binet / the Gram determinant identity,

`s_1(M)^2 s_2(M)^2 det(U_S^T U_S) rho_j^2`.                      (3.7)

Since `U^TU=I_2` and the deleted row is `u_j^T`,

`U_S^T U_S=I_2-u_j u_j^T`,

so by the matrix determinant lemma

`det(U_S^T U_S)=1-||u_j||^2=1-ell_j`.                            (3.8)

All other third-minor squares are nonnegative, proving (3.4). Equations (1.2), (2.5)-(2.6) prove (3.5). QED.

This is the high-cardinality/deleted-coordinate version of the partner r4 double-anchor determinant mechanism. The partner's aggregation idea is used before any reciprocal payment, but the terminal receiver is applied to the unrotated literal physical block (3.3).

## 4. Actual numerical E3 payment

Choose the fixed gate

`delta=2^-16`.                                                    (4.1)

If any `j` on either live bank satisfies `rho_j>=delta`, then (3.5) gives

`E_3(B_j)
 > c_0 sigma_*^4 delta^2
 =7.3228005464646e-19`.                                           (4.2)

Applying the completed physical-`E3` receiver (1.4) to this ACTUAL literal block gives

`boxed: ||p_Q||_infinity < 11483.885 <11484,`                     (4.3)

and the density is continuous `C_0`.

Every coefficient outside the block, every same-bank quadratic term, every sign, every affine term induced by conditioning, and all extra spectrum are retained by the source receiver.

Thus any unpaid r51 robust state must satisfy, simultaneously on both banks,

`boxed: rho_j<2^-16 for every physical deleted self-column j.`    (4.4)

This is stronger than the earlier adaptive-plane collar: it is alignment to the fixed ACTUAL top-two singular plane and requires no a priori small self-star norm.

## 5. Anchor-rich survivor collapses directly to rank four

Assume (4.4) on bank `R`, and assume the actual left two-plane has two literal physical anchor rows `a,b` with

`kappa=|det(u_a,u_b)|>=1/64`.                                    (5.1)

For each `j`, (4.4) gives a coefficient vector `c_j in R^2` with

`||A[R\{j},j]-U[R\{j},:]c_j||_2<delta`.                          (5.2)

Apply the r49 symmetry/common-plane rigidity lemma with no exceptional coordinates. For completeness, its mechanism is: define the unique map `T` carrying the two anchor rows to `c_a,c_b`; symmetry of `A[R,R]` makes the skew part of `T` at most `delta/kappa`; testing every other `c_j-T^Tu_j` against the two anchor rows costs at most `4delta/kappa`; symmetrizing `T` therefore produces one symmetric `2x2` matrix `B_R` with total column error at most `delta(1+5/kappa)` after the physical diagonal is absorbed.

Consequently

`A[R,R]=diag(q_R)+U B_R U^T+E_R`,                                (5.3)

with

`max_j ||E_R e_j||_2 < eta`,

`eta=delta(1+5*64)=321/65536=0.0048980712890625.`                 (5.4)

No heavy-coordinate correction is needed: the carrier on this bank is rank at most two.

The same conclusion holds on `C` if its actual right singular plane contains an anchor pair of area at least `1/64`.

By the elementary spectral-projection inequality `E_R^2 >= s^2 P_s`, the spectral projection of `E_R` onto `|lambda|>=s` obeys

`(P_s)_{jj} <= ||E_R e_j||_2^2/s^2`.                             (5.5)

At `s=1/2`,

`boxed:
 max_j (P_|E_R|>=1/2)_{jj}
 <4 eta^2
 =103041/1073741824
 =9.596440941095352e-5.`                                         (5.6)

This is over three hundred times smaller than the live `1/32` ridge-window leverage threshold. The same holds for `E_C`.

Now let

`M=U Sigma V^T+F`                                                 (5.7)

be the ACTUAL top-two SVD truncation plus tail. Because the inherited rank-two approximant is within `tau`, the best-rank-two property gives

`||F||_F<tau=2^-16`.                                              (5.8)

If both banks satisfy the anchor gate (5.1), the whole active block has the exact form

`boxed:
 A[R union C,R union C]
 =diag(q)+W H_4 W^T+(E_R direct_sum E_C)+T_cross,`                (5.9)

where

`W=diag(U,V)`, `W^TW=I_4`,

`H_4=[[B_R,Sigma],[Sigma,B_C]]`,                                  (5.10)

and

`||T_cross||_F=sqrt(2)||F||_F<sqrt(2)2^-16
 =2.1579186437577746e-5.`                                        (5.11)

Thus the earlier r49 rank-16 finite carrier is replaced, on this robust anchor-rich branch, by an exact **rank-four** latent carrier, two row-small spectrally ultra-diffuse self residuals, and the genuine retained nonzero cross tail. No six-heavy-coordinate term remains.

### Theorem 5.1 — `QFORM-R51-E3-OR-RANK4-ULTRADIFFUSE-COLLAR-v1`

In the r51 BL-compatible robust crossing branch, at least one of the following holds:

1. a literal physical deleted-self-column promotion satisfies (4.2), so the full law is paid continuously by (4.3);
2. on at least one side, every available physical anchor pair has area `<1/64` (the explicit small-Pluecker aggregate branch);
3. the exact rank-four carrier decomposition (5.9)-(5.11) holds, with the residual leverage estimate (5.6) on both sides.

No coefficient is removed in any branch.

## 6. Compact conditional proof assembly after r55

The source-valid end-to-end map is now narrower.

1. Principal-minimal same-constant descent, diagonal control, physical-pair/pair-log, grouped-square, ridge/window, scalar-pivot aggregate-tetrad, physical-`E3`, rank-two fractional, null-coloop, and hub-plus-square receivers terminate only their exact proved branches.
2. r47-r51 reduce a major overlap/singular-pair chamber to a robust actual rank-two crossing or explicit finite physical-star alternatives. The robust crossing has `s_2>sigma_*` and a rank-two approximant tail `<2^-16`.
3. The present theorem attacks the arbitrary same-bank curvature directly. Any deleted same-bank column with `2^-16` transverse mass creates a literal physical `E3` block and is terminal by `<11484`.
4. If no such column exists and both actual singular planes have a physical Pluecker anchor `>=1/64`, symmetry collapses all same-bank curvature to the rank-four exact skeleton (5.9) plus ultra-diffuse residuals and the retained tail. This removes the former rank-16/six-heavy-coordinate overhead in this branch.
5. If an anchor is absent, the remaining obstruction is explicitly aggregate: the relevant two-plane has all physical Pluecker coordinates `<1/64`. No single-minor extraction is asserted.

The first essential missing implication on this route is therefore

`QFORM-RANK4-ULTRADIFFUSE-RESIDUAL-PLUS-RETAINED-TAIL-ENDPOINT-v1`:

> pay (5.9) using the two residual high-spectrum projections with leverage `<9.6e-5` together with the four-latent carrier, or force an already-paid ridge, hub-plus-square, finite-carrier, scalar-pivot, physical-pair, or physical-`E3` exit. The `2^-16` cross tail must remain in the proof. Separately, pay the small-Pluecker aggregate branch without selecting one reciprocal tiny minor.

The latest account04/B19 r5 terminal is available whenever the finite carrier genuinely exposes its exact zero-self-side packet; its source explicitly forbids treating a small nonzero replacement as zero. This report therefore does not use that terminal outside its exact packet.

## 7. Quantifiers and status

The new theorem is sign-free and tolerates repeated singular/eigenvalues. Exact rank drops are branched on rather than divided by. All probabilistic receivers invoked are full-ambient in their stated scope and preserve arbitrary independent cap-one input laws and arbitrary affine terms. No moment or support regularity is assumed.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

Full continuous-density conclusion: **OPEN**.

New continuous branch: the physical-`E3` exit (4.3) only. The rank-four collar is structural and carries no continuity claim by itself.
