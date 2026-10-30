SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-24T04:00:14Z.
attacking: QFORM-HEAVY6-ADAPTIVE-R2-SELF-CURVATURE-PAYMENT-v1 by converting the varying deleted-cross two-planes into a single physical two-plane and a quantitatively diffuse residual.

# fleet03/B19 r49 — adaptive rank-two alignment to common four-latent carrier + diffuse residual

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW STRUCTURAL COMPILER / FIRST ESSENTIAL R48 GAP NARROWED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native brain ingestion.  
Continuity: this run proves deterministic coefficient structure only. It does not establish continuity on the new survivor. Full-target continuity remains **OPEN**.

All coordinates below are literal ORIGINAL coordinates. No random variable is rotated. No Gaussian, log-concave, moment, compact-support, connected-support, iid, arbitrary-joint-coarea, fiber-supremum, or law-uniform pointwise oscillatory-decay hypothesis is used. Every nonzero coefficient tail remains in the actual quadratic form.

## 1. Source-pinned frontier


The immediate inherited frontier is fleet03/B19 r48:

`yspennstate/math-open-problems@2d483191e9a6edbc28549de90441cbeb631eca71`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260924T030130Z-fleet03-B19-QFORM-r48/REPORT.md`.

It supplies disjoint original-coordinate banks `R,C` and a literal cross block

`N=A[R,C]`

satisfying

`dist_F(N,rank<=2)<tau`, `tau=2^-16`,                            (1.1)

`sigma_2(N)>=1/64`,                                               (1.2)

and, after the completed physical-`E3` exit is excluded, the following adaptive same-bank alignment. Let

`N_2=sigma_1 u_1v_1^T+sigma_2u_2v_2^T`

be the top-two SVD truncation of `N`, and write `V=(v_1,v_2)` as the `|C| x 2` right singular frame. If

`ell_j=||V_{j,*}||_2^2<=1/2`,                                    (1.3)

then, with `J=C\{j}` and `M_j=N[:,J]`, r48 proves

`dist(A[j,J], V_2(M_j))<f_0`, `f_0=2^-12`,                       (1.4)

where `V_2(M_j)` is an ACTUAL top-two right singular subspace of the deleted physical block. Since `sum_j ell_j=2`, at most three coordinates of `C` fail (1.3). The transposed statement holds on `R`.

The problem left by r48 was that the planes in (1.4) depend on `j`; summing row errors against different planes is invalid. The present run removes that adaptivity whenever the light physical rows of the fixed SVD plane contain one quantitatively transverse pair.

A fresh completed fleet03/B08 result is also used as proof-graph context:

`yspennstate/math-open-problems@ec4f970f5cdd3f31a8e913474fbee5172fd7b603`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260924T032039Z-fleet03-B08-qform-diffuse-r49/REPORT.md`.

Its exact deletion theorem says

`s_3(A[-i,-i]) >= (1-p_i)s_3(A)-s_4(A)`,                          (1.5)

so loss of a diffuse physical child third direction creates a fourth parent spectral direction rather than a terminal obstruction. This supports the final router below but is not used as a premise in the algebraic lemmas.

## 2. Deleted actual planes are uniformly close to the fixed SVD plane

Fix a light `j in C`, `ell_j<=1/2`. Let `V^{(j)}` denote `V` with row `j` removed, and let

`S_j=range(V^{(j)}) subset R^J`.                                  (2.1)

The deleted rank-two approximant is

`N_2^{(j)}=U Sigma (V^{(j)})^T`.                                  (2.2)

Since

`(V^{(j)})^T V^{(j)}=I_2-v_jv_j^T >=(1-ell_j)I_2 >=(1/2)I_2`,   (2.3)

its smaller nonzero singular value obeys

`sigma_2(N_2^{(j)})>=sigma_2(N)/sqrt(2)>=b_0`,                    (2.4)

where

`b_0=1/(64 sqrt(2))`.                                             (2.5)

Also

`||M_j-N_2^{(j)}||_op<=||N-N_2||_F<tau`.                         (2.6)

### Lemma 2.1 — exact rank-two subspace transport

Let `W_j=V_2(M_j)`. Then

`||P_{S_j^perp}P_{W_j}||_op <= theta_0`,                          (2.7)

with

`theta_0=tau/(b_0-tau)=0.0013829779184588303...`.                 (2.8)

#### Proof

Take a thin SVD

`M_j W_j=U_j Sigma_j`, `M_j^T U_j=W_j Sigma_j`.

Because `range((N_2^{(j)})^T)=S_j`,

`P_{S_j^perp}(N_2^{(j)})^T=0`.

Therefore

`P_{S_j^perp}W_j=P_{S_j^perp}(M_j-N_2^{(j)})^T U_j Sigma_j^{-1}`.

By Weyl and (2.4)-(2.6),

`sigma_2(M_j)>=b_0-tau>0`,

which proves (2.7). No singular-value gap between the first two directions is needed and repeated top singular values cause no problem. QED.

Now put

`d_j=A[j,C\{j}]`.                                                 (2.9)

If `||d_j||_2<=R_0`, where

`R_0=1/64`,                                                        (2.10)

then (1.4) and Lemma 2.1 imply

`dist(d_j,S_j) <= epsilon_0`,                                     (2.11)

where

`epsilon_0=f_0+theta_0(R_0+f_0)
          =0.00026608729606929297...`.                            (2.12)

Indeed choose `w in W_j` with `||d_j-w||<f_0`; then

`dist(d_j,S_j)<=f_0+theta_0||w||<=f_0+theta_0(R_0+f_0)`.

Thus the adaptive planes have been replaced by the row-deleted restrictions of ONE fixed physical coefficient plane `range(V)`, unless a light coordinate already supplies the explicit original-coordinate self-star witness

`||A[j,C\{j}]||_2>1/64`.                                         (2.13)

## 3. Symmetry forces all fixed-plane column coefficients to come from one symmetric 2x2 form

The next lemma is independent of QFORM and may be useful elsewhere.

### Lemma 3.1 — `QFORM-TWOANCHOR-COMMONPLANE-RIGIDITY-v1`

Let `D=D^T` be an `m x m` real matrix, and let `V in R^{m x 2}` have orthonormal columns. Let `L` be a set of physical indices. Assume that for every `j in L` there is a vector `c_j in R^2` such that

`||D[L\{j},j]-V[L\{j},:] c_j||_2 <= epsilon`.                    (3.1)

Suppose there are two distinct anchors `a,b in L` with

`kappa=|det(v_a,v_b)|>0`,                                        (3.2)

where `v_j=V_{j,*}^T`. Then there exists a symmetric `2x2` matrix `B` such that, after absorbing the diagonal, the light-light residual

`E_L=P_L(D-diag(q)-VBV^T)P_L`                                    (3.3)

has zero diagonal and obeys

`max_{j in L} ||E_L e_j||_2 <= epsilon(1+5/kappa)`.               (3.4)

If `H=L^c` has cardinality `h`, there is an exact decomposition

`D=diag(q)+K+E_L`,                                                (3.5)

with

`rank K<=2+2h`.                                                   (3.6)

#### Proof

Define the linear map `T:R^2->R^2` by

`T v_a=c_a`, `T v_b=c_b`.                                        (3.7)

From (3.1) and symmetry of `D`,

`|v_b^T c_a-v_a^T c_b|<=2epsilon`.                               (3.8)

Let `K_0=(T-T^T)/2`. Every real `2x2` skew matrix is `omega J`, and

`v_b^T(T-T^T)v_a=2 v_b^T K_0v_a`.

Hence, using (3.2),

`||K_0||_op<=epsilon/kappa`.                                      (3.9)

For `j notin {a,b}`, symmetry and (3.1) give

`|v_a^T(c_j-T^T v_j)|<=2epsilon`,
`|v_b^T(c_j-T^T v_j)|<=2epsilon`.                                (3.10)

The `2x2` matrix with rows `v_a^T,v_b^T` has determinant magnitude `kappa` and Frobenius norm at most `sqrt(2)`, so its inverse operator norm is at most `sqrt(2)/kappa`. Therefore (3.10) yields

`||c_j-T^T v_j||_2<=4epsilon/kappa`.                              (3.11)

Set

`B=(T+T^T)/2`.                                                    (3.12)

Combining (3.9) and (3.11),

`||c_j-Bv_j||_2<=5epsilon/kappa`                                 (3.13)

for non-anchor `j`; for the anchors the sharper bound `epsilon/kappa` follows directly from (3.7),(3.9). Since `V` is an isometry on coefficient space, replacing each `Vc_j` by `VBv_j` costs at most the right side of (3.13). Together with (3.1) this gives (3.4).

Choose

`q_j=D_jj-v_j^T Bv_j`                                            (3.14)

for all `j`. Then `R=D-diag(q)-VBV^T` is symmetric and zero-diagonal. Put `E_L=P_LRP_L`. The remainder `R_H=R-E_L` is supported on rows or columns touching `H`. Write

`R_H=P_HR+(I-P_H)RP_H`;                                          (3.15)

each term has rank at most `h`, hence `rank R_H<=2h`. Taking `K=VBV^T+R_H` proves (3.5)-(3.6). QED.

The important point is that symmetry converts many unrelated coefficient vectors `c_j` into one symmetric two-dimensional quadratic form. This is exactly the mechanism missing from the row-by-row r48 statement.

## 4. Row-small symmetric residuals have diffuse high-spectrum projections

### Lemma 4.1 — `QFORM-ROWSMALL-IMPLIES-SPECTRAL-DIFFUSE-v1`

Let `E=E^T` and assume

`max_j ||Ee_j||_2<=eta`.                                         (4.1)

For `s>0`, let `P_s` be the spectral projection of `E` onto eigenvalues with absolute value at least `s`. Then

`max_j (P_s)_{jj} <= eta^2/s^2`.                                 (4.2)

#### Proof

Functional calculus gives

`E^2 >= s^2 P_s`.

Taking the `j`th diagonal entry,

`s^2(P_s)_{jj}<=(E^2)_{jj}=||Ee_j||_2^2<=eta^2`. QED.

This is a deterministic leverage statement. It does not say `E` is small in operator or Frobenius norm; in high dimension `E` may have large spectral directions, but any such directions are physically diffuse.

## 5. Live one-bank compiler at the r48 constants

Let `C_light` be the r48 light coordinates, so at most three coordinates of `C` lie outside it. Assume the following two gates hold:

1. no light self-star witness (2.13), i.e.

`||A[j,C\{j}]||_2<=1/64` for every `j in C_light`;                (5.1)

2. there are light anchors `a,b` with

`|det(v_a,v_b)|>=kappa_0`, `kappa_0=1/64`.                       (5.2)

Equations (2.11)-(2.12) give the hypotheses of Lemma 3.1 with `epsilon=epsilon_0`. Hence the self block

`D_C=A[C,C]`

admits

`D_C=diag(q_C)+K_C+E_C`,                                         (5.3)

where

`rank K_C<=8`                                                     (5.4)

because there are at most three heavy coordinates, and

`max_j ||E_Ce_j||_2 <= eta_0`,                                   (5.5)

with

`eta_0=epsilon_0(1+5/kappa_0)
     =0.08541402203824304...`.                                   (5.6)

Applying Lemma 4.1 at `s=1/2` gives

`max_j (P_{|E_C|>=1/2})_{jj}
 <=(2eta_0)^2
 =0.029182220642997872...
 <1/32`.                                                          (5.7)

This is the first dimension-free common-plane conclusion for the r48 adaptive survivor: any still-unpaid bank satisfying (5.1),(5.2) consists of a coordinate-separable diagonal, an at-most-rank-eight carrier, and a residual whose target-scale spectral projection is already below the live diffuse leverage threshold.

### Theorem 5.1 — `QFORM-ADAPTIVE-R2-TO-COMMONPLANE-DIFFUSE-RESIDUAL-v1`

For the r48 strong physical rank-two survivor on one bank, at least one of the following holds:

- an explicit original-coordinate light self-star has norm `>1/64`;
- every light-light Pluecker anchor pair has `|det(v_a,v_b)|<1/64`;
- the exact decomposition (5.3)-(5.7) holds.

No coefficient is deleted in any branch.

The second alternative is a genuine remaining geometry rather than a failure of the proof: a highly diffuse two-plane can have all individual Pluecker coordinates tiny while their squared aggregate is one. It must be aggregated rather than converted into one good minor.

## 6. Bilateral consequence: four latent directions + at most six physical hubs

Apply Theorem 5.1 also to the transposed r48 statement on bank `R`. In the branch where both banks satisfy the row-norm and anchor-area gates, let

`N_2=U Sigma V^T`, `||N-N_2||_F<tau`.                             (6.1)

On the active block `R union C`, the aligned parts of both self blocks and the rank-two crossing combine into ONE four-dimensional latent carrier:

`K_lat = W H_4 W^T`,                                             (6.2)

where

`W=diag(U,V)` has four orthonormal columns and

`H_4=[[B_R,Sigma],[Sigma,B_C]]`.                                 (6.3)

Thus

`rank K_lat<=4`.                                                  (6.4)

The deviations touching the at-most-three heavy physical coordinates on each bank contribute rank at most `2*3+2*3=12`. Consequently the whole structured nonseparable carrier on `R union C` has rank at most

`4+12=16`.                                                        (6.5)

The exact active block can therefore be written

`A[R union C,R union C]
 =diag(q)+K_16+(E_R direct_sum E_C)+T_cross`,                     (6.6)

where

`rank K_16<=16`,                                                  (6.7)

`||T_cross||_F<sqrt(2) 2^-16`,                                   (6.8)

and each residual `E_R,E_C` satisfies the high-spectrum physical leverage bound (5.7). The cross tail `T_cross` is the genuine retained `N-N_2` term; it is not discarded as random noise. Coefficients coupling `R union C` to coordinates outside this active block remain completely untouched.

Thus the r48 “heavy six + adaptive planes” frontier has been replaced, in the transverse-anchor/no-large-star branch, by the much more rigid object

> coordinate-separable diagonal + one four-latent quadratic carrier + interactions supported on at most six literal physical hubs + two spectrally diffuse residual self blocks + the original `2^-16` cross tail.

This is a structural reduction, not yet a density theorem.

## 7. Fresh other-account receiver now available

The fresh fleet01/B01 r12 theorem at

`yspennstate/math-open-problems@5a750c5b1188ea297a92c01b9692de5d87ab7f4c`

proves a sign-free two-physical-pivot density receiver. If a literal pair

`P=[[a,c],[c,b]]`

has `a!=0`, `det P!=0`, and the full matrix has `s_3(A)>=s`, then

`||p_Q||_infinity <=27.265324466 |a|^(-1/10)|det P|^(-2/5)s^(-1/10)`.  (7.1)

For example, at the concrete target-scale gate

`|a|>=1/64`, `|det P|>=2^-12`, `s>=1`,                           (7.2)

this gives

`||p_Q||_infinity<1151.258`.                                     (7.3)

This receiver is therefore available if the finite physical-hub part of (6.6) exposes such a pair. The present run does not claim that (7.2) is forced by (6.6); aggregate tiny pair currency remains a real issue.

## 8. Designated partner fleet04/B19 applied at an actual inequality

The completed designated partner theorem is

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`,

`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`.

In its exact residual-diffuse rank-three null-coloop normal form, for `0<D_res<=1` and `|det M|>=1`,

`||p_Q||_infinity<34 sqrt(log(e/D_res))`,                         (8.1)

with a continuous `C_0` density. Therefore, strictly inside that proved scope,

`2^-32<=D_res<=1`                                                 (8.2)

implies the concrete inequality

`||p_Q||_infinity
 <34 sqrt(log(e 2^32))
 =163.6975885...<164`.                                            (8.3)

The partner's newer r3 counterexample to generic `L^3 + 1/2`-Holder interpolation is retained as a hard boundary: neither the diffuse residual in (6.6) nor any Frostman estimate may be converted to `L^infinity` by abstract interpolation alone. The next payment must keep the residual coupled to the four-latent / physical-hub resource.

## 9. Compact conditional proof assembly after r49

The current proof tree can now be stated more sharply.

1. Principal-minimal same-constant descent removes any proper original-coordinate principal block that already carries three target eigenvalues.
2. Existing diagonal, principal-triple, physical-`E3`, ridge/window, pair-log, half-Riesz, grouped-square, null-coloop and physical-pair receivers pay their exact branches without post-rotation independence or discarded tails.
3. r47-r48 reduce a major singular-pair/large-leaf-curvature chamber to either a physical-`E3` payment, a giant near-rank-one crossing, or the strong ultra-thin rank-two crossing with adaptive self-curvature.
4. The present run eliminates the varying-plane ambiguity in that strong-rank-two branch whenever a light Pluecker anchor pair has area at least `1/64` and no light self-star exceeds `1/64`: it yields (6.6), with high-spectrum residual leverage `<1/32`.
5. A failure of those hypotheses is itself now explicit: either a physical self-star `>1/64`, or a two-plane whose every light-light Pluecker coordinate is `<1/64` and hence requires aggregate rather than one-minor payment.

Accordingly the first essential implication on this route is now

`QFORM-4LATENT-6PHYSICAL-DIFFUSE-RESIDUAL-COUPLED-PAYMENT-v1`:

> pay (6.6) while retaining the two diffuse self residuals and the genuine nonzero cross tail, or prove that it forces an already-paid physical pair/star/grouped/ridge/physical-volume gate. The proof must preserve the coupling between the diffuse residual and the finite latent/hub carrier; generic interpolation is invalid.

Parallel debts remain the giant near-rank-one crossing, the small-Pluecker aggregate branch, the explicit `>1/64` aligned self-star branch, and the previously identified low-rank carrier / extra-spectrum interactions. This report does not rename any of them as solved.

## 10. Quantifiers, signs, degeneracies, continuity

The new deterministic lemmas are sign-free and tolerate repeated singular/eigenvalues. Exact zero determinants are never divided by: Lemma 3.1 branches explicitly on the existence of a nonzero anchor area `kappa`, and the no-anchor branch is retained. Every probabilistic receiver cited above keeps arbitrary independent input laws with densities bounded by one and arbitrary affine terms in its stated scope. No moments or support regularity are assumed.

Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full universal continuous-density conclusion: **OPEN**.  
New r49 result: deterministic structural compiler only; no new continuity claim.
