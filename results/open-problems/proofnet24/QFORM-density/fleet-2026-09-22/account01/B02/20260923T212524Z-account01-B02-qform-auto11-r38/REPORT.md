SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T21:25:24Z.
attacking: the rank-at-most-42 carrier + small original-coordinate diagonal + tiny Frobenius-tail endpoint from r37, by a product-preserving random physical cut and the account02/B02 marginal-free E3 Fourier receiver.

# account01/B02 r38 — finite-rank carrier diffuse-or-finite-localized Fourier fork

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate  
Status: **NEW SUPPORTING THEOREM / ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN_NOT_REFUTED**  
Regularity: continuous `C_0` density on the Fourier-L1 branch proved below; full-target continuity remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation-independence, arbitrary-joint coarea, conditional-cap, fiber-supremum, single-good-minor, or small-random-tail deletion is used.


## 1. Source-pinned inputs actually used

### 1.1 Previous B02 endpoint

The preceding run is

`yspennstate/math-open-problems@1084cf8ec8916b7e5b9754cbb7ebad2a4c29cf4b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T210217Z-account01-B02-qform-auto11-r37/REPORT.md`.

Its remaining relative-second-scale strong-cut collar is an exact ORIGINAL-coordinate decomposition

`A = R_42 + D_small + E_0`,                                      (1.1)

where

`rank(R_42) <= 42`,
`D_small` is diagonal in the independent coordinates,
`||D_small||_op < 1/8`,
`||E_0||_F < eps_0 := 0.002987529789725499`,                     (1.2)

and the target hypothesis plus Weyl gives

`s_3(R_42) > gamma_0 := 1 - 1/8 - eps_0
                       = 0.8720124702102745...`.                  (1.3)

No term in (1.1) is probabilistically discarded.

### 1.2 Designated partner account02/B02

The completed partner source used at an actual inequality is

`yspennstate/math-open-problems@aeaba9e3351623ead11450857c2d014b43664aef`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T200844Z-account02-B02-qform-auto11/REPORT.md`.

Its marginal-free physical-third-volume theorem says: for every literal ORIGINAL-coordinate cross block `B=A[J,I]`, if

`Z_3(B)=E_3(B):=e_3(BB^T)>0`,

then, with the completed constant

`C_3=10.345084`,                                                  (1.4)

the full ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= C_3 Z_3(B)^(-1/6)`,                         (1.5)

with `phi_Q in L^1`. The same completed Fourier compiler records the quantitative unweighted bound

`integral_R |phi_Q(t)| dt <= 2 pi C_3 Z_3(B)^(-1/6)`.            (1.6)

Arbitrary same-bank curvature, outside couplings, affine terms and signs remain present. This is the only partner theorem used in the main inequality below.

## 2. Main deterministic/Fourier theorem

### Theorem 2.1 — `QFORM-FINITERANK-CARRIER-DIFFUSE-OR-FINITELOCALIZED-L1-v1`

Suppose, in ORIGINAL coordinates,

`A=D+R+E`,                                                        (2.1)

where

- `D` is diagonal;
- `R=R^T` has rank `r>=3`;
- `s_3(R)>=gamma>0`;
- `||E||_F<=eps`.

Write the exact nonzero spectral factorization

`R=V K V^T`, `V^T V=I_r`,                                       (2.2)

where `K=K^T` is invertible and `s_3(K)=s_3(R)>=gamma`. Let `v_i^T` be row `i` of `V`, and define the carrier leverages

`ell_i=||v_i||_2^2`, so `sum_i ell_i=r`.                         (2.3)

Put

`H={i: ell_i>1/(16r)}`, `L=H^c`.                                (2.4)

Then `|H|<=16r^2`, and at least one of the following alternatives holds.

**(A) Diffuse Fourier-L1 exit.** If

`sigma := (sqrt(3)/8) gamma - eps >0,`                            (2.5)

then there is a literal ORIGINAL-coordinate cut `J|I` for which

`E_3(A[J,I]) >= sigma^6`,                                       (2.6)

and therefore

`boxed: ||p_Q||_infinity <= C_3/sigma`,                          (2.7)

`boxed: integral_R |phi_Q(t)|dt <= 2 pi C_3/sigma`.              (2.8)

In this alternative the density is continuous and vanishes at infinity.

**(B) Finite physical localization.** There is a unit vector `u in R^r` such that the unit carrier-range vector `Vu` satisfies

`boxed: ||(Vu)_H||_2^2 > 1/2`,                                  (2.9)

on a set of at most `16r^2` ORIGINAL coordinates.

The alternatives are exhaustive. In particular, failure of the Fourier exit forces a dimension-independent physical localization certificate for the finite-rank carrier.

### Proof

First, (2.3)-(2.4) give

`|H|/(16r) < sum_{i in H} ell_i <= r`,

so `|H|<16r^2`; the stated weak inequality is a convenient integer relaxation.

Define

`G_L=V_L^T V_L=sum_{i in L} v_i v_i^T`.                          (2.10)

If `lambda_min(G_L)<1/2`, choose a unit eigenvector `u` with

`u^T G_L u<1/2`.

Since `V^TV=I_r`,

`||(Vu)_H||_2^2
 =u^T(V_H^TV_H)u
 =u^T(I_r-G_L)u
 >1/2`,                                                          (2.11)

which is alternative (B).

It remains to assume

`G_L >= (1/2)I_r`.                                                (2.12)

Put every heavy coordinate in the bank `I`. Independently place each light physical coordinate in `J` with probability `1/2`; the remaining light coordinates also go to `I`. Then

`G_J=V_J^TV_J=sum_{j in J}v_jv_j^T`,
`G_I=I_r-G_J`.                                                    (2.13)

Since `E G_J=G_L/2` and the Bernoulli summands are independent and centered after subtraction,

`E ||G_J-G_L/2||_F^2
 = (1/4) sum_{j in L} ||v_jv_j^T||_F^2
 = (1/4) sum_{j in L} ell_j^2
 <= (1/4)(1/(16r)) sum_j ell_j
 = 1/64.`                                                        (2.14)

Hence some actual ORIGINAL-coordinate split satisfies

`||G_J-G_L/2||_op
 <=||G_J-G_L/2||_F
 <=1/8`.                                                         (2.15)

Using (2.12) and `G_L<=I_r`,

`G_J >= (1/8)I_r`,
`G_J <= (5/8)I_r`,
`G_I=I_r-G_J >= (3/8)I_r`.                                      (2.16)

Now consider only the coefficient identity for the carrier crossing:

`B_R:=R[J,I]=V_J K V_I^T`.                                      (2.17)

Because (2.16) makes both Gram matrices invertible, define

`U_J=V_J G_J^(-1/2)`, `U_I=V_I G_I^(-1/2)`.

Both have orthonormal columns and

`B_R=U_J [G_J^(1/2) K G_I^(1/2)] U_I^T`.                        (2.18)

Thus the nonzero singular values of `B_R` are exactly those of the middle square matrix. The standard singular-value product inequality gives

`s_3(B_R)
 >= sqrt(lambda_min G_J) s_3(K) sqrt(lambda_min G_I)
 >= sqrt(1/8) gamma sqrt(3/8)
 = (sqrt(3)/8)gamma.`                                            (2.19)

The full physical cross block is

`B:=A[J,I]=B_R+E[J,I]`,                                         (2.20)

because the ORIGINAL-coordinate diagonal `D` has zero cross block. Crucially, `E` is retained exactly; it is not deleted from the random quadratic form. We use it only through the deterministic Weyl estimate

`||E[J,I]||_op <= ||E||_op <= ||E||_F <=eps`.                    (2.21)

Consequently

`s_3(B)>= (sqrt(3)/8)gamma-eps=sigma`.                           (2.22)

If `sigma>0`, then

`E_3(B)=e_3(BB^T)
 >=s_1(B)^2s_2(B)^2s_3(B)^2
 >=s_3(B)^6
 >=sigma^6`.                                                     (2.23)

This is (2.6). Applying the designated account02/B02 theorem (1.5)-(1.6) to this actual literal cross block gives (2.7)-(2.8). QED.

### Remark: tunable form

The constants above are chosen to make the live r37 application transparent. More generally, for `0<eta<=1`, take

`H_eta={i: ell_i>eta^2/(4r)}`.

Then `|H_eta|<=4r^2/eta^2`. If `lambda_min(V_{L_eta}^TV_{L_eta})<eta`, a unit carrier vector has more than `1-eta` of its squared mass on `H_eta`. Otherwise the same random split has an actual realization with

`G_J >= (eta/4)I_r`,
`G_I >= (1/2-eta/4)I_r`,                                        (2.24)

and hence

`s_3(A[J,I])
 >= gamma sqrt[(eta/4)(1/2-eta/4)]-eps`.                         (2.25)

No probabilistic input-law regularity beyond the eventual partner receiver is used in this deterministic fork.

## 3. Actual application to the r37 rank-at-most-42 collar

Apply Theorem 2.1 to (1.1). Let `r=rank(R_42)<=42`,

`gamma=gamma_0=0.8720124702102745...`,
`eps=eps_0=0.002987529789725499...`.

Then

`sigma_0
 = (sqrt(3)/8)gamma_0-eps_0
 = 0.1858087081150042... >0`.                                   (3.1)

Therefore the r37 endpoint now has the following exhaustive fork.

### 3.1 Fourier-L1 branch

There is an actual original-coordinate cut with

`E_3(A[J,I]) >= sigma_0^6`,                                     (3.2)

so the designated account02/B02 theorem applies at the concrete inequality (3.2) and gives

`boxed: ||p_Q||_infinity < 55.675992`,                           (3.3)

and

`boxed: integral_R |phi_Q(t)|dt < 349.822571`.                   (3.4)

This branch has a continuous `C_0` density.

### 3.2 Only surviving branch

There is a carrier-range unit vector with more than half of its squared Euclidean mass on at most

`16(42)^2 = 28224`                                               (3.5)

literal ORIGINAL coordinates.

Thus the previous fixed-rank carrier obstruction is no longer diffuse in physical coordinates. It has been compressed to a universal finite-coordinate localization obstruction.

## 4. What this does and does not prove

This theorem is useful for the exact target because:

1. the random split is a split of ORIGINAL independent coordinates, not a spectral rotation;
2. the small diagonal remains exactly in `Q` and vanishes only from a cross block for the algebraic reason that it is physically diagonal;
3. the nonzero Frobenius tail remains exactly in `Q`; only deterministic singular-value perturbation is used;
4. no individual cross minor is selected or inverted;
5. the completed account02/B02 result is applied to an actual quantitative `E_3` lower bound.

The full conjecture is **not** proved. Alternative (B) is a structural certificate, not yet a density theorem. In particular, one carrier direction localized on a universal finite coordinate set does not by itself guarantee three large singular values of the corresponding principal block.

The first unpaid B02 interface on this collar is now

`QFORM-RANK42-FINITELOCALIZED-CARRIER-HUB-RECEIVER-v1`:

> Starting with `rank R<=42`, `s_3(R)>0.872`, `||D||op<1/8`, `||E||F<0.002988`, and a carrier-range unit vector carrying more than half its mass on at most 28224 original coordinates, either promote that finite set as a grouped physical hub and obtain a product-preserving Fourier/Riesz receiver for the remaining two smoothing directions, or iterate the leverage split on the orthogonal carrier quotient until three directions are paid. Keep `D` and `E` exactly; do not turn the finite-localization statement into a fictitious good 3x3 principal minor.

No exact-target counterexample to a universal `integral |phi_Q|` bound was found. The target-wide integrated-Fourier criterion remains `OPEN_NOT_REFUTED`; full bounded density and full-target continuity remain OPEN.

## 5. Arithmetic checks

With

`eps_0=0.002987529789725499`,
`gamma_0=1-1/8-eps_0`,

one gets

`gamma_0=0.8720124702102745...`,
`sigma_0=sqrt(3)gamma_0/8-eps_0=0.1858087081150042...`,
`C_3/sigma_0=55.6759912113324...`,
`2pi C_3/sigma_0=349.822569941704...`,
`16*42^2=28224`.

These checks concern constants only; the proof is the exact argument in Section 2.

## 6. Source status


Correction package consumed: live `CORRECTION_INBOX.json` at the same control commit. In particular the proof does not invoke `QFORM-CROSSMINOR-ALONE-FALSE`, post-rotation independence, a conditional-density cap, arbitrary-joint coarea, pointwise van-der-Corput decay, or deletion of a small nonzero quadratic tail.

Repository transport and source retrieval occurred, but native learned-memory ingestion was not verified. Status remains `WITHOUT_VERIFIED_BRAIN`.
