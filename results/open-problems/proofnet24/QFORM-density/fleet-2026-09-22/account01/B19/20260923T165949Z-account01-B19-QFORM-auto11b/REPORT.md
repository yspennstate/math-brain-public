SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B19, 2026-09-23T16:59:49Z.
attacking: QFORM-2x2x2-PRODUCT-TRIANGLE-OR-HEAVY-ANCHOR-PAYMENT-v1 — spend mismatch of the two K-side rank-two planes by the designated partner's mixed exterior-volume theorem, then isolate a genuinely common-plane 2+2+2 survivor without deleting any tail.

# account01/B19 auto11b — right-plane mismatch elevator for the balanced STAR triangle

Programme: `QFORM-DENSITY-3EIG-20260922`

Status: **ESSENTIAL_STEP_APPLIED / ONE LARGE SUBBRANCH PAID / FULL QFORM OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval and source-pinned handoff are durable transport, not native learned-memory ingestion.

Continuity: proved on the D'/D3-paid branch below; not claimed for the remaining common-plane survivor or for the full target.

## 1. Fresh source graph and corrections


The full conjecture remains OPEN: independent real coordinates with arbitrary probability densities bounded by one; arbitrary real symmetric A with at least three eigenvalues of absolute value at least one; prove one universal finite essential density bound for X^T A X. No moments, iid law, support condition, smoothness, log-concavity or sign restriction is assumed. Continuity is separate.

The live correction inbox was reread before this report. In particular, nothing below uses post-rotation independence, arbitrary-joint coarea, conditional density caps after projection, law-uniform pointwise quadratic Fourier decay, a uniformly good single minor, deletion of a small matrix tail as a random perturbation, or a generic bounded-joint-density replacement for a product-origin grouped bank.

The new interactive grouped-projection theorem at

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`,

was also read. It is compatible supporting mathematics but does not by itself close the small-leak/common-plane survivor because its grouped-hub crossing hypothesis must hold exactly; an arbitrary nonzero hub-complement/light coupling cannot be discarded or reclassified as an internal hub phase.

### Designated partner actually used

The newest completed `account02/B19` result is

`yspennstate/math-open-problems@9157730c1b552b81f58b3cb6ef604b687962e548`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T160847Z-account02-B19-QFORM-r36/REPORT.md`.

Its theorem `QFORM-OVERLAP-MIXED-EXTERIOR-VOLUME-v1` says: for pairwise disjoint ORIGINAL-coordinate banks I,J,K, with

`N=A[I,K]`, `M=A[I,J]`, `C=[M N]`,

if P_2 is a top-two left singular projection of N and `rho=s_1(N)s_2(N)`, then

`e_3(C C^T) >= rho^2 ||(I-P_2)M||_F^2`.                         (1.1)

More precisely it identifies the full nonnegative mixed exterior sum. When the natural third-volume row marginals of the actual cross block are at most `2/3`, its completed D' receiver gives

`||p_Q||_infinity <= (9 sqrt(3)e/2) e_3(CC^T)^(-1/6)`,           (1.2)

with arbitrary self blocks, outside couplings, affine terms and signs retained, and with a continuous `C_0` density.

This report applies (1.1) and (1.2) to a new literal physical orientation, not merely as background.

## 2. Input from the balanced STAR triangle

The quantitative-rank-two STAR4 branch is source-pinned at

`yspennstate/math-open-problems@db5c35db0ea104ee7e38d904c1a759ba46164f49`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T130709Z-account02-B19-QFORM-auto11/REPORT.md`.

For its physical leaf cross block `N=A[J,K]`,

`s_2(N)>s_1(N)/16`,                                               (2.1)

and

`rho=s_1(N)s_2(N)>rho_*`,
`rho_*:=63(1-tau)^2/16384`, `tau=2^-20`,                          (2.2)

so

`rho_*=0.0038452075095882221056...`.                              (2.3)

The newest balanced self-cut compiler is account03/B19 r37,

`yspennstate/math-open-problems@fd9966835d05b404551208f2cf6bfbec1bee65dc`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T160411Z-account03-B19-QFORM-r37/REPORT.md`.

In its diffuse top-two-left-leverage branch it chooses one ORIGINAL-coordinate cut

`J=D_1 disjoint_union D_2`                                      (2.4)

such that the top-two left frame U of the parent N obeys, for

`G_r=U[D_r,:]^T U[D_r,:]`,

`3/8 I_2 <=G_r<=5/8 I_2`, `r=1,2`,                              (2.5)

and the actual restrictions

`N_r:=N[D_r,K]`                                                   (2.6)

satisfy

`rho_r:=s_1(N_r)s_2(N_r) >=Delta_*:=(3/8)rho_*`.                 (2.7)

Numerically

`Delta_*=0.00144195281609558329...`.                              (2.8)

The same r37 cut carries the self-bank packet `C=A[D_1,D_2]`. Its theorem already pays a transverse left-plane component by D3, and otherwise gives top-two left projections `P_1,P_2` for `N_1,N_2` with, at theta=1/64,

`||(I-P_1)C||_F^2<F/64`,
`||C(I-P_2)||_F^2<F/64`,                                         (2.9)

and therefore

`||P_1 C P_2||_F^2 >=(9/16)F`.                                  (2.10)

What r37 did **not** force is alignment of the two different top-two RIGHT singular planes inside the common physical K bank. Without such an alignment the K-side carrier may have dimension four, so the phrase `2+2+2` requires one further gate. The next two sections supply it.

## 3. Condition-number inheritance under the balanced physical cut

### Lemma 3.1 — `QFORM-STAR4-RESTRICTED-BICORE-CONDITION-v1`

Under (2.1), (2.5), let `kappa_r=s_1(N_r)/s_2(N_r)` for the **actual** restricted block including its entire SVD tail. Then

`boxed: kappa_r < kappa_0:=sqrt(1288/3)=20.72036035722674...}`     (3.1)

for `r=1,2`.

Consequently, using (2.7),

`boxed: s_2(N_r)^2 >=Delta_*/kappa_0.}`                           (3.2)

#### Proof

Write the parent SVD as

`N=N^(2)+T`,

where `N^(2)` is its top-two truncation. The right singular spaces of `N^(2)` and `T` are orthogonal, hence after restriction to physical rows `D_r`,

`N_r N_r^T=N^(2)_r (N^(2)_r)^T+T_rT_r^T`.                       (3.3)

The two nonzero squared singular values of `N^(2)_r` are the eigenvalues of

`diag(s_1(N),s_2(N)) G_r diag(s_1(N),s_2(N))`.                   (3.4)

By (2.5),

`lambda_1(N^(2)_r(N^(2)_r)^T) <=(5/8)s_1(N)^2`,                  (3.5)

`lambda_2(N^(2)_r(N^(2)_r)^T) >=(3/8)s_2(N)^2`.                  (3.6)

Also

`||T_r||_op<=||T||_op=s_3(N)<=s_2(N)`.                           (3.7)

Therefore Weyl monotonicity and the triangle inequality for the top eigenvalue give

`s_1(N_r)^2 <=(5/8)s_1(N)^2+s_2(N)^2
             <[(5/8)16^2+1]s_2(N)^2
             =161s_2(N)^2`,                                     (3.8)

while

`s_2(N_r)^2 >=(3/8)s_2(N)^2`.                                   (3.9)

Dividing (3.8) by (3.9) proves (3.1). Since

`rho_r=s_1(N_r)s_2(N_r)<=kappa_0 s_2(N_r)^2`,                    (3.10)

(2.7) gives (3.2). QED.

The point of Lemma 3.1 is that the balanced cut retains not only a singular-product lower bound but also a universal condition number. The nonzero parent tail is kept exactly in (3.3); it is never thrown away.

## 4. Main new theorem: right-plane mismatch creates literal physical third volume

For `r=1,2`, let `Q_r` denote the orthogonal projection in the ORIGINAL physical K-coordinate space onto the top-two RIGHT singular plane of the actual `N_r`. Define

`d_R^2:=||(I-Q_1)Q_2||_F^2`.                                    (4.1)

For two rank-two projections this is symmetric in 1 and 2.

### Theorem 4.1 — `QFORM-TWO-BICORE-RIGHTPLANE-MISMATCH-v1`

Let `N_1,N_2` be two real matrices with the same column-coordinate space K, and suppose

`s_1(N_r)s_2(N_r)>=Delta>0`,
`s_1(N_r)/s_2(N_r)<=kappa`, `r=1,2`.                             (4.2)

Put

`Z_K:=e_3(A[K,D_1 union D_2] A[D_1 union D_2,K])`
`    =e_3([N_1^T,N_2^T][N_1^T,N_2^T]^T)`.                       (4.3)

Then

`boxed: Z_K >=(Delta^3/kappa) d_R^2.}`                           (4.4)

This is an exact deterministic coefficient statement. No input law appears in it.

#### Proof — designated partner applied at the actual inequality

Use account02/B19 r36 Theorem (1.1) with the partner's row bank set equal to the present physical `K`, with

`N_partner=N_1^T`,
`M_partner=N_2^T`.                                                (4.5)

The top-two left singular projection of `N_1^T` is exactly `Q_1`. Hence the partner theorem gives

`Z_K >=rho_1^2 ||(I-Q_1)N_2^T||_F^2`.                           (4.6)

Let `q_{2,1},q_{2,2}` be the first two right singular vectors of `N_2`. Expanding in its full SVD and discarding only nonnegative summands,

`||(I-Q_1)N_2^T||_F^2`
` =sum_a s_a(N_2)^2 ||(I-Q_1)q_{2,a}||^2`
` >=s_2(N_2)^2 sum_(a=1)^2||(I-Q_1)q_{2,a}||^2`
` =s_2(N_2)^2 d_R^2.                                             (4.7)

The condition-number hypothesis gives

`s_2(N_2)^2>=Delta/kappa`.                                       (4.8)

Insert (4.7)-(4.8) and `rho_1>=Delta` into (4.6) to obtain (4.4). QED.

This proof is sign-free and rank-tail-safe: all omitted terms in (4.7) are nonnegative squared contributions, and the partner theorem itself is an exterior-volume identity for the actual physical block.

## 5. Actual STAR4 payment

Apply Theorem 4.1 with

`Delta=Delta_*`,
`kappa=kappa_0`,
`theta_R=1/64`.                                                   (5.1)

If

`d_R^2>=1/64`,                                                    (5.2)

then

`boxed: Z_K >=Delta_*^3/(64 kappa_0)
              >2.260871454155696e-12.}`                          (5.3)

### 5.1 Direct designated-partner D' payment

If the natural squared-third-volume row marginals of this literal physical cross block `A[K,D_1 union D_2]` are all at most `2/3`, the account02/B19 r36 D' receiver (1.2) gives the full ambient law

`boxed: ||p_Q||_infinity <1849.361.}`                            (5.4)

The same Fourier theorem gives a continuous `C_0` density on this branch.

If the `2/3` marginal gate fails, then one actual ORIGINAL K-coordinate has normalized row-volume marginal `>2/3`; equivalently it is incident to more than

`boxed: (2/3)Z_K >1.507247636103797e-12}`                        (5.5)

of the squared physical `3x3` cross-minor mass. This is a genuine physical third-volume anchor, not a selected reciprocal minor.

### 5.2 Stronger constant on the older D3 gate

If in fact every row marginal is at most `1/2`, the completed D3 theorem used in account03/B19 r37 gives the sharper

`boxed: ||p_Q||_infinity <863.481,}`                             (5.6)

again continuously. Failure of that stronger gate yields a row carrying more than

`1.130435727077848e-12`                                          (5.7)

of squared third-volume mass.

The numerical checker in this run recomputes every constant in (5.3)-(5.7) from the exact rational definitions and terminates `QFORM_B19_RIGHTPLANE_CHECK_PASS`.

## 6. The genuinely common-plane survivor

It remains to understand the complementary case

`d_R^2<1/64`.                                                     (6.1)

This case is much narrower than merely saying that both `N_1,N_2` have rank-two bicores.

For rank-two projections,

`||Q_1-Q_2||_F^2=2d_R^2<1/32`,                                  (6.2)

so

`||Q_1-Q_2||_F<0.176776695296637`.                               (6.3)

Let `V_r` be orthonormal two-column frames for `Q_r`, and let the principal angles between `Q_1,Q_2` be `theta_1,theta_2`. Then

`d_R^2=sin^2(theta_1)+sin^2(theta_2)`.                            (6.4)

Therefore

`|det(V_2^T V_1)|=cos(theta_1)cos(theta_2)`
` >=1-d_R^2>63/64`.                                              (6.5)

Let `P_r` be the top-two left singular projection of `N_r`. Since `P_2N_2Q_2` is its exact top-two SVD component, restricting that component to the common plane `Q_1` gives

`s_1(P_2N_2Q_1)s_2(P_2N_2Q_1)`
` =rho_2 |det(V_2^T V_1)|`
` >(63/64)Delta_*`
` =0.00141942230334409... .`                                    (6.6)

At the other leg,

`s_1(P_1N_1Q_1)s_2(P_1N_1Q_1)=rho_1>=Delta_*`.                  (6.7)

Combine (6.6)-(6.7) with the r37 self-edge core (2.10). Every survivor after the two physical third-volume exits now contains one deterministic **common-plane** triangle

`P_1  <---- C_core ----> P_2`,
`  \                         /`
`   \ N_1_core     N_2_core/`
`          Q_1`,

where all three displayed spaces have dimension exactly two,

`||C_core||_F^2>=(9/16)F`,                                       (6.8)

`prod_2(N_1_core)>=Delta_*`,                                     (6.9)

`prod_2(N_2_core)>(63/64)Delta_*`.                              (6.10)

This is the first point at which the previous shorthand `2+2+2` is literally justified on all three vertices. Before the new right-plane gate, the two K-side planes could span four dimensions.

Crucially, (6.8)-(6.10) identify a core; they do **not** license replacing the actual quadratic form by that core. All of the following remain exactly present in the ambient law:

- the small but nonzero components of `C` outside `P_1-P_2`;
- every SVD-tail component of `N_1,N_2`;
- all same-bank quadratic curvature and diagonals;
- all affine terms generated by any legitimate conditioning;
- all outside couplings and every additional eigenvalue of A.

The account04/B19 moving-ridge construction shows why the next step may not compress one bank to an arbitrary bounded joint density: product provenance must remain visible through the analytic payment.

## 7. Compact conditional proof graph after this run

The correction-safe proof assembly is now:

1. Existing pivot, pair, ruled, exact-null, semidefinite, D/D5, spectral-window and diffuse-tail exits pay their stated gates, with continuity only where their Fourier proof supplies it.
2. Strict `N3(2^-20)` reaches STAR4 or another already recorded open global branch. In STAR4, the relative-rank-one tube remains a separate debt; the quantitative-rank-two branch has (2.1)-(2.3).
3. The completed selected-volume and carrier results pay diffuse finite-rank branches and isolate aligned STAR geometry.
4. The r37 balanced cut either exposes physical top-two leverage `>1/320`, or creates a robust three-bank triangle and pays its transverse self packet by D3, leaving left-plane alignment (2.9)-(2.10).
5. **New:** on that aligned triangle, account02/B19 r36 applied with the K bank as the exterior row space pays every fixed right-plane mismatch by a literal physical third-volume block, modulo only its explicit row-marginal anchor.
6. **New:** failure of that payment forces the two K-side rank-two planes to be quantitatively common, with the exact common-plane products (6.9)-(6.10).

Thus the first essential unpaid implication on this route is now

`QFORM-COMMONPLANE-2x2x2-PRODUCT-WITH-TAIL-v1`:

> starting from the exact quantitative common 2+2+2 coefficient core (6.8)-(6.10), pay the **actual** ambient quadratic form while preserving the original-product origin of each physical bank and retaining every nonzero cross/self tail; or route the explicit heavy top-plane leverage / D3 row-volume anchor to an already completed receiver.

This is narrower than `QFORM-2x2x2-PRODUCT-TRIANGLE-OR-HEAVY-ANCHOR-PAYMENT-v1`: a possible four-dimensional K-side union has been removed. The new interactive arbitrary-rank projected-crossing theorem is a plausible receiver for subcases with genuine projected crossing volume, but its exact grouped-hub hypotheses still have to be verified on the survivor rather than inferred from smallness.

The unrestricted QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**. Two independent end-to-end reviews do not exist. Global continuity remains open.

## 8. Scope ledger

- All input laws remain arbitrary independent scalar laws with density cap one.
- No coordinate rotation is applied to the random input and no projected coordinates are called independent.
- Orthogonal singular-vector changes appear only inside deterministic matrix identities.
- All matrix signs, repeated singular values, degeneracies and additional spectrum are allowed.
- The theorem is vacuous only when its displayed singular-product hypotheses fail; those failures belong to other already-recorded branches, not to an illicit division by zero.
- No nonzero SVD tail or small coefficient is deleted.
- The partner's row-marginal gate is kept explicitly; a failed gate is an anchor, not a paid density estimate.
- Essential boundedness and continuity are asserted only on the D'/D3-paid branch.
- Full target status: OPEN.
