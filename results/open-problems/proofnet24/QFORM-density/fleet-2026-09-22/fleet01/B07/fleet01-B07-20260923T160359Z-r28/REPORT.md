SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T16:03:59Z.
attacking: the genuine rank-two physical-cross tube by exterior-square factorization of the complete E2 determinant law; recover a dimension-free macroscopic coordinate minor when both top-two singular planes are heavy, without counting minors or paying a reciprocal pivot.

# fleet01/B07 r28 — rank-two tube => approximately product Plucker determinant law

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `fleet01-B07-20260923T160359Z-r28`  
Owner control observed before publication: revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **ESSENTIAL STEP APPLIED / MECHANISM CHANGED TO EXTERIOR-SQUARE FACTORIZATION / PARTNER RESULT APPLIED / FULL QFORM OPEN**.

The unrestricted theorem is not claimed. All probabilistic conditioning remains in ORIGINAL independent coordinates. Singular vectors below are used only to prove deterministic coefficient identities; the probability law is never rotated. No Gaussian, moment, log-concavity, compact-support, connected-support, diagonal-basis, pointwise van-der-Corput, arbitrary-joint coarea, fiber-sup, or one-tiny-minor reciprocal assumption is used.

## 1. Sources actually consumed

Fresh `math-research-brain` main was resolved and the owner/control files, programme manifest, current research, claims, live correction inbox, memory protocol, and `fleet01/B07` assignment were read. The full conjecture and the global continuity conclusion remain OPEN.

The immediately preceding B07 state is `yspennstate/math-open-problems@f03bb7505dc80819aae237e34f516c801e15c6d8`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T150507Z-r27/REPORT.md`.

The completed designated-partner result actually applied here is fleet02/B07's star/E2 compiler, source-pinned by brain commit `24f75537c3e283f33de7c532409d3404b04daa67`, canonical mathematics `yspennstate/math-open-problems@5ff9d960bffec400a9d6db422401e4c4df98ce6d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T150720Z-fleet02-B07-qform/REPORT.md`. Its exact consequence used below is

`dist_F(K, rank<=2) <= (2 G_*/S^2)^(1/4)`                         (1.1)

for the partner's physical block `M=[[s^T,r^T],[C,K]]`, where `S=||s||_2>0` and `G_*` is the complete star-supported anchored third-compound packet.

For the optional high-tail payment after a new macroscopic edge is produced, I also use the already-completed fleet02/B07 theorem `QFORM-PAIRTAIL-CURVATURE-RECEIVER-v1`, canonical source `yspennstate/math-open-problems@3e36370502df5afeb00457b74d05cdbfd87168b0`, which gives

`||p_Q||_inf <= 26.00795742 Delta^(-2/5) kappa^(-1/10) T_2(D)^(-1/20)` (1.2)

for an actual ORIGINAL-coordinate invertible indefinite principal pair with `Delta=|det B|`, `kappa=sigma_min(B)`, and a disjoint physical far cross block `D` before pair completion.

## 2. Exterior-square determinant law

Let `K` be any real `m x n` physical cross block with singular values

`sigma_1 >= sigma_2 >= sigma_3 >= ... >=0`,

and assume `sigma_2>0`. Put

`E = ||K||_F^2 = sum_j sigma_j^2`,
`Omega = E_2(K) = sum_{i<j} sigma_i^2 sigma_j^2`,
`P = sigma_1^2 sigma_2^2`,
`delta = Omega-P`,
`T_2 = sum_{j>=3} sigma_j^2 = dist_F(K,rank<=2)^2`.                 (2.1)

Index the rows of the second compound `C_2(K)=wedge^2 K` by physical row pairs `R` and its columns by physical column pairs `C`. Thus

`C_2(K)_(R,C) = det K[R,C]`,
`||C_2(K)||_F^2 = Omega`.                                           (2.2)

Define the complete E2 determinant-square probability law

`W(R,C)=det K[R,C]^2/Omega`.                                       (2.3)

Let `K_2=sigma_1 u_1 v_1^T + sigma_2 u_2 v_2^T` be the best rank-two SVD truncation. This use of singular vectors is deterministic only. Its second compound has rank one:

`C_2(K_2)=sigma_1 sigma_2 (u_1 wedge u_2)(v_1 wedge v_2)^T`.         (2.4)

Define the Plucker pair laws

`mu(R)=det U_2[R]^2`, `nu(C)=det V_2[C]^2`,                         (2.5)

where `U_2=[u_1,u_2]`, `V_2=[v_1,v_2]`. Cauchy--Binet gives `sum_R mu(R)=sum_C nu(C)=1`. Hence the determinant law of `K_2` is exactly the PRODUCT law

`W_0(R,C)=mu(R) nu(C)`.                                             (2.6)

This exact product structure is the mechanism change in this run.

## 3. Near rank two implies near-product determinant weights

### Theorem 3.1 — `QFORM-RANK2-TUBE-PLUCKER-TV-v1`

With the notation above,

`boxed: delta <= E T_2.`                                            (3.1)

Moreover, with `rho=delta/Omega in [0,1)`, the total-variation distance of the physical determinant law from the product Plucker law satisfies

`boxed:
 TV(W,W_0)
 <= 1/2 sqrt(rho)(1+sqrt(1-rho)) + rho/2
 <= sqrt(rho)+rho/2.`                                               (3.2)

Consequently

`boxed:
 TV(W,W_0) <= sqrt(chi)+chi/2,`                                     (3.3)

whenever `chi>=E T_2/Omega` and `chi<=1`.

#### Proof of (3.1)

Write `lambda_j=sigma_j^2`. Then

`delta = (lambda_1+lambda_2)T_2 + e_2(lambda_3,lambda_4,...)`.

Since `e_2(tail)<=T_2^2/2<=T_2^2`,

`delta <= (lambda_1+lambda_2+T_2)T_2 = E T_2`.

#### Proof of (3.2)

In the singular-vector exterior bases,

`C_2(K)=sum_(i<j) sigma_i sigma_j (u_i wedge u_j)(v_i wedge v_j)^T`.

The summands are orthogonal in Hilbert--Schmidt norm. Hence, with `D=C_2(K)` and `D_0=C_2(K_2)`,

`||D-D_0||_F^2=delta`, `||D||_F^2=Omega`, `||D_0||_F^2=P=Omega-delta`. (3.4)

Now

`sum_(R,C) |D_(R,C)^2-D0_(R,C)^2|
 <= ||D-D_0||_F ||D+D_0||_F
 <= sqrt(delta)(sqrt(Omega)+sqrt(P)).`                              (3.5)

Also the normalization change contributes exactly

`sum D0^2 |1/Omega-1/P| = delta/Omega`.                              (3.6)

Dividing (3.5) by `Omega`, adding (3.6), and then dividing the L1 distance by two gives the first bound in (3.2). The second uses `sqrt(1-rho)<=1`. QED.

No dimension or number of minors appears.

## 4. Heavy top-two singular planes force one macroscopic physical minor

The physical-coordinate inclusion marginal of row coordinate `i` under `mu` is exactly

`ell_i = ||U_2[i,*]||_2^2`,                                        (4.1)

because the event that a random Plucker row pair contains `i` has total squared wedge weight equal to the diagonal of the rank-two projection `U_2 U_2^T`. Similarly the column inclusion marginal under `nu` is

`m_j = ||V_2[j,*]||_2^2`.                                          (4.2)

### Theorem 4.1 — `QFORM-NEARRANK2-DOUBLEHEAVY-MACROMINOR-v1`

Fix `h in (1/2,1)`. Suppose there are distinct physical rows `i_1,i_2` and distinct physical columns `j_1,j_2` such that

`ell_i1, ell_i2, m_j1, m_j2 >= h`.                                 (4.3)

Then

`boxed:
 det K[{i_1,i_2},{j_1,j_2}]^2
 >= Omega * [(2h-1)^2 - TV(W,W_0)]_+.`                              (4.4)

#### Proof

Under the row-pair law `mu`, the intersection of the events `i_1 in R` and `i_2 in R` is the single pair `R={i_1,i_2}`. Hence Bonferroni gives

`mu({i_1,i_2}) >= ell_i1+ell_i2-1 >=2h-1`.                          (4.5)

Likewise `nu({j_1,j_2})>=2h-1`. The product law therefore puts mass at least `(2h-1)^2` on that single physical minor. Any event probability changes by at most total variation, proving (4.4). QED.

At the useful threshold `h=3/4`, define

`rho_0 = 9/4-sqrt(5) = 0.013932022500210...`.                        (4.6)

This is the exact positive solution of

`sqrt(rho_0)+rho_0/2=1/8`.                                         (4.7)

Therefore if `rho<=rho_0` and both top-two singular planes have two physical coordinates of leverage at least `3/4`, then

`boxed:
 det K[{i_1,i_2},{j_1,j_2}]^2 >= Omega/8.`                          (4.8)

This is a DIMENSION-FREE macroscopic coordinate minor. It carries at least `12.5%` of the entire E2 determinant currency. No counting over `binom(m,2)binom(n,2)` minors is used.

Since a `2x2` matrix all of whose entries have magnitude at most `b` has determinant magnitude at most `2b^2`, (4.8) also yields a physical edge

`boxed: |K_ij| >= 2^(-5/4) Omega^(1/4) = 0.420448... Omega^(1/4).`    (4.9)

## 5. Actual application of the completed fleet02/B07 partner result

Apply Theorem 3.1 to the partner's physical far block `K`. Its completed star/E2 compiler (1.1) gives

`T_2(K) <= (2G_*/S^2)^(1/2)`.                                      (5.1)

Therefore

`rho = [E_2(K)-sigma_1^2 sigma_2^2]/Omega
 <= (E/Omega) sqrt(2G_*/S^2)`.                                     (5.2)

Define the dimensionless quantity

`chi_* := (E/Omega) sqrt(2G_*/S^2)`.                                (5.3)

Then the partner result plus the new theorem gives the explicit determinant-law conclusion

`boxed: TV(W,W_0) <= sqrt(chi_*)+chi_*/2` whenever chi_*<=1.        (5.4)

In particular, if

`boxed:
 G_* <= [rho_0^2/2] * S^2 Omega^2/E^2,`                             (5.5)

then `chi_*<=rho_0`. Thus, on the partner's low-third-volume survivor, if both top-two singular planes of `K` contain two physical coordinates of leverage at least `3/4`, one actual physical `2x2` minor obeys

`boxed: |det K[R_*,C_*]|^2 >= Omega/8`,                             (5.6)

and hence one physical edge obeys (4.9).

Equivalently, if the double-heavy geometry holds but every physical `2x2` minor has squared determinant `<Omega/8`, then the partner's star-supported third-volume packet must satisfy the quantitative lower bound

`boxed:
 G_* > [rho_0^2/2] S^2 Omega^2/E^2.`                               (5.7)

Thus the partner's formerly generic `rank-two tube` is split again without reciprocal pivots:

* a regenerated third-compound packet at the explicit scale (5.7); or
* a determinant law close to a product of two physical Plucker laws; and in the double-heavy/double-heavy face, a macroscopic coordinate minor (5.6).

This is the required actual application of the completed designated-partner result to a new inequality.

## 6. Optional immediate payment after the new macroscopic edge

The selected edge in (4.9) is an actual original-coordinate coefficient of the symmetric ambient Schur matrix. Let

`b := A_rs`, `|b|>=2^(-5/4) Omega^(1/4)`.                            (6.1)

Its actual symmetric principal pair is

`B=[[A_rr,b],[b,A_ss]]`.

As in the earlier B07 pair compiler, either

`max(|A_rr|,|A_ss|)>=|b|/2`,                                        (6.2)

or the pair is invertible indefinite with

`Delta=|det B|>=3b^2/4`, `kappa=sigma_min(B)>=|b|/2`.                (6.3)

In the latter branch, apply the completed fleet02/B07 pair-tail receiver (1.2). If an allowed disjoint far physical cross block `D` satisfies

`T_2(D)>=tau b^2`,                                                   (6.4)

then

`||p_Q||_inf
 <=31.274095 tau^(-1/20) |b|^(-1)
 <=74.383 tau^(-1/20) Omega^(-1/4).`                                (6.5)

This proves essential boundedness in that precise branch while retaining arbitrary same-bank curvature, affine terms, outside couplings and extra spectrum. Continuity is NOT promoted because the cited pair-tail theorem does not claim it at this scope.

If (6.4) fails, the true nonzero tail is retained:

`T_2(D)<tau b^2`.                                                    (6.6)

Thus no small quadratic perturbation is deleted.

## 7. What remains after this run

The new first B07 debt is

`QFORM-PLUCKER-ONEHUB-OR-MACROEDGE-RANK2-STABILITY-v1`.

For the genuine rank-two-tube survivor, the determinant law is now quantitatively close to a product of row and column Plucker laws whenever the star-supported E3 packet is small. The double-heavy/double-heavy product face produces a macroscopic coordinate minor and then either a large physical diagonal, a pair-tail payment, or an even tighter rank-two far tube. The remaining product-law faces have at most one `>3/4` leverage coordinate on at least one of the two top singular planes; they should be attacked by the existing E2-to-E1 shadow / mixed-order half-Riesz machinery rather than by another individual-minor search.

A second explicit obligation is the already-known `large physical diagonal` branch after (6.2). No claim is made that a large diagonal alone pays arbitrary same-bank curvature.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. The owner-requested global continuous-density upgrade remains separately OPEN.

## 8. Deterministic regression check

A deterministic NumPy regression was run locally with seed `20260923` on 1,200 generic rectangular Gaussian coefficient matrices and 1,000 targeted near-rank-two matrices whose top-two left and right singular planes are physically double-heavy. It checked (3.1), (3.2), and the `h=3/4`, `rho<=rho_0` macroscopic-minor implication. Result:

`generic_cases=1200`
`targeted_macro_cases=1000`
`violations=0`
`min_targeted_macro_ratio=0.9708928220658307`
`rho_0=0.013932022500210195`
`STATUS=PASS`

These finite checks are regression evidence only. The proof is the analytic argument above.
