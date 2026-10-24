SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T19:56:12Z.
attacking: stabilize a diffuse strong rank-three carrier against a weak fourth carrier by aggregate physical three-volume smoothing, or force strong original-coordinate localization without deleting the weak mode.

# account02/B09 r20 — weak-fourth-mode stability before localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING THEOREM + TARGET-VALID PAYMENT / FULL QFORM OPEN**

The unrestricted conjecture remains OPEN. The result below removes one specific defect in the preceding finite-carrier fork: a rank-four carrier can have a physically localized fourth direction whose eigenvalue tends to zero, so a localization certificate for the full four-frame need not locate one of the three spectral directions that actually pay the owner's hypothesis. The theorem below proves that this vanishing fourth mode cannot by itself obstruct aggregate physical three-volume smoothing. Either the strong three-dimensional carrier is itself localized, or the full form is paid uniformly through the fourth-mode collapse.

No random source variable is rotated. The only rotations below diagonalize a deterministic finite-dimensional carrier. No moment, support, log-concavity, iid, or post-rotation-independence hypothesis is introduced. No small quadratic random term is deleted. Continuity is asserted only in branches with an integrable characteristic-function envelope.

## 1. Fresh sources and exact scopes

Fresh owner control remained `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`, with no stop or B09 reassignment observed before publication.

The required historical source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. I apply its completed Theorem H to an actual source-coordinate star in Section 7. The pinned counterexample search contains no valid counterexample to full QFORM.

The newest completed designated account03/B09 source consumed here is r39, canonical report

`yspennstate/math-open-problems@4b076c614a1e1b826433acf811adcffc29e8f05d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T184804Z-account03-B09-QFORM-r39/REPORT.md`,

with late-source reconciliation at `af81ace54b10d45b8284185c92e89df38b92063c`. Its surviving new theorem is `QFORM-R4-CARRIER-DIFFUSE-OR-256-LOCALIZED-v1`. The analytic receiver used below is its proved aggregate physical-cross estimate:

if `B=A[J,I]` is a literal original-coordinate cross block,

`Z_3(B)=e_3(BB^T)`,

and all size-three row-volume marginals satisfy `alpha_j<=1/2`, then

`||p_Q||_infinity <= 6 sqrt(2e) Z_3(B)^(-1/6)`,                 (1.1)

with a continuous density and the same coefficient in the interval estimate. Arbitrary same-side quadratic blocks remain inside the phase. For a rank-three cross block, the row-volume marginal is exactly the leverage in its physical row range.

The preceding account02/B09 r19 theorem gave, for a general diagonal plus rank-three/rank-four carrier, either an aggregate payment or finite localization of some carrier direction. The missing issue was that the localized direction could be only a spectrally negligible fourth mode. This run addresses precisely that issue.

## 2. Strong-three plus weak-four decomposition

Let

`A = D + R K R^T + mu w w^T`,                                  (2.1)

where

- `D` is diagonal in the ORIGINAL independent coordinates;
- `R in R^(n x 3)`, `R^T R=I_3`;
- `K=K^T` is invertible with `s_3(K)>=gamma>0`;
- `w` is a unit vector orthogonal to `range(R)`;
- `mu` is real.

Every symmetric rank-four carrier with third singular value at least `gamma` can be put in this form by diagonalizing only its deterministic four-dimensional coefficient matrix and taking the three eigenmodes of largest absolute value as `R K R^T`. This is not a random-coordinate rotation.

Write the physical row of `R` at coordinate `i` as `r_i^T` and set

`a_i=||r_i||_2^2`, `sum_i a_i=3`.                               (2.2)

The fourth direction `w` may be arbitrarily concentrated and may create dense same-side physical coefficients through `mu w w^T`.

## 3. Main theorem — weak fourth mode cannot fake the hard localized branch

### Theorem `QFORM-STRONG3-WEAK4-ROBUST-CROSS-v1`

Assume (2.1). Put

`kappa_0 = sqrt(7)/192 = 0.013779954745128...`.                 (3.1)

If

`|mu| <= kappa_0 gamma`,                                        (3.2)

then at least one of the following holds.

**(A) uniform aggregate bilinear payment.** The law of `X^TAX` has a continuous density and

`boxed:
 ||p_(X^TAX)||_infinity
 <= C_0 gamma^(-1),
 C_0 = [96 sqrt(2e)/sqrt(7)] (8/7)^(1/3)
     = 88.453516030135... .`                                    (3.3)

Consequently, for every interval `L`,

`boxed: P{X^TAX in L} <= C_0 gamma^(-1)|L|.}`                   (3.4)

**(B) genuinely strong physical localization.** There are at most `576` ORIGINAL coordinates `H` and a unit vector `u in R^3` such that

`boxed: ||(Ru)_H||_2^2 > 3/4.}`                                 (3.5)

Thus failure of the paid branch cannot be blamed solely on a localized fourth carrier direction whose eigenvalue is vanishing.

### Proof

Set

`delta=1/192`,
`H={i:a_i>delta}`, `L=H^c`.                                     (3.6)

Since `sum_i a_i=3`,

`|H| delta <3`, hence `|H|<=576`.                               (3.7)

Let

`G_L=R_L^T R_L`.                                                 (3.8)

If `lambda_min(G_L)<1/4`, choose a unit `u` realizing that Rayleigh quotient. Because `R^TR=I_3`,

`||(Ru)_H||_2^2
 =1-u^T G_Lu
 >3/4`,                                                           (3.9)

which is alternative (B).

Assume henceforth

`G_L >= I_3/4`.                                                  (3.10)

Randomly place each coordinate of `L` into a row bank `J` with probability `1/2`, independently, and put every coordinate of `H` into the complementary bank `I`. Define

`G_J=R_J^T R_J`, `G_I=R_I^T R_I=I_3-G_J`.                       (3.11)

The Bernoulli fluctuations are centered and independent, so

`E ||G_J-G_L/2||_F^2
 =(1/4) sum_(j in L) ||r_j r_j^T||_F^2
 =(1/4) sum_(j in L) a_j^2
 <=(delta/4) sum_j a_j
 <=1/256`.                                                       (3.12)

Therefore one literal original-coordinate split satisfies

`||G_J-G_L/2||op <=1/16`.                                      (3.13)

Using (3.10) and `G_L<=I_3`,

`G_J>=I_3/16`,
`G_I>=7I_3/16`.                                                  (3.14)

Consider first the strong-three physical cross block

`B_0=R_J K R_I^T`.                                               (3.15)

The two restricted frames have positive Gram matrices, so `B_0` has rank three and

`s_3(B_0)
 >= sqrt(lambda_min G_J) s_3(K) sqrt(lambda_min G_I)
 >= (sqrt(7)/16) gamma
 =: c gamma`.                                                    (3.16)

For `j in J`, the rank-three row-volume marginal equals the range leverage and hence

`alpha_j(B_0)
 = r_j^T G_J^(-1) r_j
 <=16 a_j
 <=1/12`.                                                        (3.17)

Now restore the complete weak fourth mode. Its cross contribution is the rank-one matrix

`E=mu w_J w_I^T`,                                                (3.18)

so

`||E||op
 =|mu| ||w_J||_2 ||w_I||_2
 <=|mu|/2`.                                                      (3.19)

Put `B=B_0+E`, which is the FULL physical cross block of `A` for this cut because the diagonal `D` has no cross entries.

Let the three nonzero singular values of `B_0` be

`sigma_1>=sigma_2>=sigma_3>0`.                                  (3.20)

The key point is that a rank-one update is affine at exterior degree three. In singular coordinates write

`B_0=sum_(a=1)^3 sigma_a u_a v_a^T`,
`E=x y^T`.                                                       (3.21)

Any exterior-cube term containing `E` twice vanishes because its two output vectors are parallel to `x`. Thus

`wedge^3 B = wedge^3 B_0 + T`,                                  (3.22)

where `T` is the sum of the three terms selecting `E` and two singular rank-one summands of `B_0`. Consequently

`||T||HS
 <=||E||op (sigma_1 sigma_2+sigma_1 sigma_3+sigma_2 sigma_3)
 <=3 ||E||op sigma_1 sigma_2`.                                  (3.23)

Since

`||wedge^3 B_0||HS=sigma_1 sigma_2 sigma_3`,                    (3.24)

we obtain

`theta:=||T||HS/||wedge^3 B_0||HS
 <=3||E||op/sigma_3
 <=3|mu|/(2 c gamma)`.                                          (3.25)

Under (3.2), using `c=sqrt(7)/16`,

`theta<=1/8`.                                                    (3.26)

Write

`Z_0=||wedge^3 B_0||HS^2`, `Z=Z_3(B)=||wedge^3 B||HS^2`.        (3.27)

The triangle inequality and (3.16) give

`sqrt(Z)
 >=(1-theta)sqrt(Z_0)
 >=(7/8)(c gamma)^3`.                                            (3.28)

It remains to retain the volume-marginal gate after adding `E`. Let `P_j` be the orthogonal projection in the output exterior space onto basis row triples containing the physical row `j`. For `B_0`,

`||P_j wedge^3 B_0||HS^2=alpha_j(B_0) Z_0`.                     (3.29)

Hence, by (3.17), (3.23), and (3.26),

`alpha_j(B)
 =||P_j wedge^3 B||HS^2/Z
 <=[(sqrt(1/12)+1/8)/(7/8)]^2
 =0.223512969119... <1/2`.                                      (3.30)

The completed account03/B09 aggregate physical-cross receiver (1.1) therefore applies to the FULL matrix `B`, not to `B_0` with the weak mode deleted. From (3.28),

`Z^(-1/6)
 <=(8/7)^(1/3)(c gamma)^(-1)`.                                  (3.31)

Substituting `c=sqrt(7)/16` in (1.1) gives exactly (3.3). Its characteristic-function majorant is integrable, proving continuity, and (3.4) follows by integrating the density. QED.

### Mechanism point

The weak mode is spent at the exterior-volume level before the reciprocal `Z_3^(-1/6)` is taken. The estimate is uniform as `mu->0`; no factor `|mu|^{-a}` appears. This is the relevant stability feature for the rank-four-to-rank-three transition.

## 4. Corollary for the r38/r39 diagonal-plus-rank-four carrier

Suppose an exact dual-zero-aggregate rank-two hub/star survivor has, as in account03/B09 r38,

`A=D_0+S`, `rank S<=4`,                                         (4.1)

and suppose a deterministic spectral step gives

`s_3(S)>=gamma>0`.                                               (4.2)

For example, r38 gives `gamma>=1-tau` when `s_3(A)>=1` and `||D_0||op<=tau<1`.

If `rank S=4`, diagonalize its four-dimensional coefficient matrix and call the fourth singular/eigenvalue magnitude `|mu|=s_4(S)`. Then:

- if `s_4(S)<=kappa_0 gamma`, Theorem 3 says either the form is paid by (3.3), or a direction in the THREE-dimensional strong spectral carrier is `>3/4` localized on at most 576 physical coordinates;
- if `s_4(S)>kappa_0 gamma`, then all four carrier singular values are at least `kappa_0 gamma`, so any subsequent full-carrier localization is not a spectrally negligible fourth-mode artifact.

Thus the remaining exact-carrier localization branch can no longer hide exclusively in a vanishing fourth direction. The still-unpaid work is to route a genuinely strong finite localization, or a uniformly rank-four localized carrier, through a physical pivot/hub/projected-crossing receiver while retaining arbitrary diagonal curvature. The nonzero r38 residual `E` is still separate and is not deleted by this theorem.

## 5. Actual target-valid family paid uniformly through a weak dense fourth mode

Let `m=1024` and let `z_0,z_1,z_2,z_3` be four orthonormal flat Walsh vectors on an `m`-coordinate source bank `I`. Add one literal physical hub coordinate `h`. Extend `z_1,z_2,z_3` by zero at `h` and put

`R=[z_1,z_2,z_3]`,
`K=diag(1,1,-1)`,
`w=(sqrt(3)/2)e_h+(1/2)z_0`.                                    (5.1)

Then `R^TR=I_3`, `w` is unit and orthogonal to `range(R)`. For

`A_mu=R K R^T+mu w w^T`,                                        (5.2)

the nonzero spectrum is exactly

`{1,1,-1,mu}`.                                                   (5.3)

Hence the owner's three-large-eigenvalue hypothesis holds for every `mu`, including `mu->0`.

The full four-frame is strongly localized: its physical leverage at the hub is `3/4`. By contrast, the strong three-frame has hub leverage zero and leaf leverage `3/1024<1/192`, so its heavy set in the proof of Theorem 3 is empty. Therefore for every admissible independent cap-one product law and every

`|mu|<=sqrt(7)/192`,                                             (5.4)

Theorem 3 gives the genuine target inequality

`boxed: ||p_(X^T A_mu X)||_infinity <88.454,}`                  (5.5)

and

`boxed: P{X^T A_mu X in L}<88.454 |L|.}`                        (5.6)

The weak fourth term is not a diagonal perturbation. In source coordinates,

`mu(w^T X)^2
 =mu[(3/4)X_h^2
     +(sqrt(3)/2) X_h <z_0,X_I>
     +(1/4)<z_0,X_I>^2]`.                                      (5.7)

Thus the theorem retains simultaneously a physical hub coupling and a dense same-side leaf square. The bound stays uniform as `mu` vanishes. Treating the weak term by a rank-four Fresnel product would instead introduce a reciprocal power of `|mu|`; deleting it would be invalid for arbitrary unbounded cap-one inputs.

This family is therefore a concrete source-coordinate payment of the weak-mode localization loophole, not merely a structural statement.

## 6. Source-valid limitation of the new theorem

The threshold (3.2) is a sufficient stability scale, not a claim that the fourth mode must be small in the full problem. If `|mu|` is larger, the theorem only says the fourth mode is no longer spectrally negligible relative to the third strong scale. A finite physical localization of a uniformly rank-four carrier is still analytically unpaid in full generality.

Likewise, the theorem does not treat the quantitative r38 decomposition

`A=D_0+S+E_res`

by dropping `E_res`. Small Frobenius/operator norm of `E_res` is not a small random quadratic perturbation under arbitrary unbounded cap-one laws. That live correction remains binding.

## 7. Required pinned mixed-hub theorem applied to an actual source-coordinate star

I also apply the completed Theorem H from the required `e5f71d79...` source directly, in a branch with no probability squaring.

Take two literal physical hubs `a,b` and an `m`-coordinate leaf bank, with `m` a Walsh size at least eight. Choose flat orthonormal leaf vectors `c_1,c_2,v` and consider

`Q_star
 =2X_a<c_1,Y>
  +2X_b<c_2,Y>
  +<v,Y>^2`.                                                     (7.1)

The active matrix on the coefficient directions `{e_a,c_1,e_b,c_2,v}` has spectrum

`{1,-1,1,-1,1}`,                                                 (7.2)

so this is an exact target instance. Its mixed source-coordinate rows are

`rho_i=(v_i,(c_1)_i,(c_2)_i)`,                                  (7.3)

with

`sum_i rho_i rho_i^T=I_3`,
`||rho_i||_2^2=3/m<=1/2`.                                       (7.4)

Theorem H with two hubs and one same-side square therefore gives directly

`|phi_Q(t)|<=8 pi^(5/2)|t|^(-5/2)`.                             (7.5)

There is no Weyl-differencing square here. Integrating the actual envelope,

`(1/(2pi)) integral_R min(1,8pi^(5/2)|t|^(-5/2)) dt
 =(5/3)2^(6/5)`,                                                 (7.6)

so

`boxed:
 ||p_Q||_infinity
 <=(5/3)2^(6/5)
 =3.828994516656... ,}`                                         (7.7)

and hence

`boxed: P{Q_star in L}<=3.829 |L|.}`                            (7.8)

The dense same-side leaf square remains in the original source bank. The three leaf projections are never declared independent. The estimate is already linear in interval length, with no square-root small-ball conversion.

## 8. Updated first unpaid B09 implication

The preceding debt

`QFORM-R4-CARRIER-STRONG-LOCALIZED-HUB-OR-RESIDUAL-CROSSING-v1`

is sharpened to

`QFORM-STRONG-CARRIER-LOCALIZATION-OR-RETAINED-RESIDUAL-RECEIVER-v1`:

1. In the exact diagonal-plus-rank-at-most-four carrier endpoint, the vanishing-fourth-mode loophole is now paid. Route either a `>3/4` localization of a genuinely strong top-three carrier direction on at most 576 ORIGINAL coordinates, or a uniformly rank-four localized carrier, into a physical scalar/pair/hub or projected-crossing theorem while retaining the diagonal twist.
2. Separately, for r38's nonzero retained residual, compile that residual into a literal cross packet or prove a phase-sensitive receiver that keeps it in the oscillatory integral. Do not infer probabilistic smallness from matrix norm.

The full target remains OPEN. Full-target continuity remains OPEN. No valid counterexample was found.

## 9. Numerical constants checked

The exact constants used above are

`c=sqrt(7)/16=0.1653594569415369...`,
`kappa_0=sqrt(7)/192=0.0137799547451281...`,
`alpha_max=0.2235129691193947...`,
`C_0=88.45351603013505...`,
`C_star=(5/3)2^(6/5)=3.828994516656783...`.

These are arithmetic checks only; the proof is the analytic argument above.
