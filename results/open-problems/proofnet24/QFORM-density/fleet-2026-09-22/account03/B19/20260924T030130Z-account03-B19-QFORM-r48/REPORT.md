SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T03:01:30Z.
attacking: the strong physical rank-two crossing with arbitrary same-bank curvature — promote any transverse physical same-bank row to a literal third cross direction and localize the unpaid survivor to at most six heavy coordinates plus adaptively rank-two-aligned self curvature.

# account03/B19 r48 — physical row promotion for the ultra-thin rank-two carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW TARGET-LEVEL PAYMENT + STRUCTURAL FUNNEL / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not authenticated native brain-receiver ingestion.  
Continuity: the positive physical-`E3` branch below has a continuous `C_0` density by the cited marginal-free Fourier receiver. The surviving alignment statement is deterministic only. Full-target continuity remains **OPEN**.

All random coordinates below are literal ORIGINAL product coordinates. No random-coordinate rotation is used to claim independence. There is no Gaussian, log-concave, moment, compact-support, connected-support, iid, arbitrary-joint-coarea, fiber-supremum, or law-uniform pointwise oscillatory-decay assumption. No nonzero coefficient tail is deleted as a probabilistically small perturbation.

## 1. Fresh proof graph and current frontier


The immediate inherited source is account03/B19 r47:

`yspennstate/math-open-problems@1a64d8ce29d893fd99b9af8dac5a63e359a9cc08`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T020346Z-account03-B19-QFORM-r47/REPORT.md`.

One of its still-unpaid literal physical-crossing branches consists of disjoint ORIGINAL-coordinate banks `R,C` with

`N=A[R,C]`,

`dist_F(N,rank<=2)<tau`, `tau=2^-16`,                              (1.1)

`sigma_2(N)>=1/64`,                                                (1.2)

and

`sigma_1(N)sigma_2(N)>gamma_0`,                                   (1.3)

where

`gamma_0=28159/(4194304 sqrt(2))
        =0.00474725242887306...`.                                  (1.4)

The full matrix may have arbitrary within-`R`, within-`C`, and outside curvature and every nonzero crossing tail remains present.

The fresh account02/B19 result

`yspennstate/math-open-problems@cddd95e8f2034382419d488197e0eb08cb506543`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260924T025057Z-account02-B19-QFORM-auto11b/REPORT.md`

proves the pure-bilinear rank-two subcase

`Q_0=2X_R^T N X_C + independent addend`

by

`||p_Q0||_infinity <=2 sqrt(pi) [sigma_1(N)sigma_2(N)]^-1/2`,      (1.5)

hence the r47 scale gives `<51.44981`. It also exhibits a target-valid exact Schur-cancellation family showing that raw `E2` need not survive a scalar pair completion. Thus the first real debt is the SAME rank-two physical crossing with arbitrary internal curvature on the same source banks.

The analytic receiver used below is account03/B04 r42,

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T215155Z-account03-B04-QFORM-auto11-r42/REPORT.md`.

For every literal disjoint ORIGINAL-coordinate physical cross block `K`, with

`E_3(K)=e_3(KK^T)>0`,

it proves for the full ambient quadratic-plus-affine law

`||p_Q||_infinity <= C_E3 E_3(K)^(-1/6)`,                         (1.6)

where

`C_E3=8.4530212255281768747...`,                                  (1.7)

and the density is continuous and vanishes at infinity. Arbitrary same-bank quadratic terms, outside couplings, affine terms, signs and extra spectrum are retained.

## 2. New exact promotion inequality

Let `R,J` be disjoint physical coordinate sets. Let

`M=A[R,J]`

and let `j` be one further physical coordinate disjoint from `R union J`. Put

`d=A[j,J]`.

Let `s_1(M)>=s_2(M)>=...` be the singular values of `M`, and let `V_2(M)` be any top-two right singular subspace when `s_2(M)>0`. Define

`F=dist(d,V_2(M))`.                                                (2.1)

Form the literal physical cross block

`K=A[R union {j},J]=[M;d]`.                                       (2.2)

### Theorem 2.1 — `QFORM-PHYSICAL-R2-PROMOTED-ROW-E3-v1`

If `s_2(M)>0`, then

`boxed: E_3(K) >= [s_1(M)s_2(M)]^2 F^2.`                          (2.3)

Consequently the exact target law satisfies

`boxed: ||p_Q||_infinity
 <= C_E3 [s_1(M)s_2(M)]^(-1/3) F^(-1/3)}`                         (2.4)

whenever `F>0`, and this branch has a continuous `C_0` density.

#### Proof

Take an SVD of the deterministic coefficient matrix only,

`M=U Sigma V^T`.

Apply the block-row orthogonal transformation `diag(U^T,1)` to the coefficient matrix `[M;d]`. This changes neither singular values nor `E_3`; it does not transform random variables. The first two transformed rows are

`s_1 v_1^T`, `s_2 v_2^T`.

Their exterior product with `d` has squared norm

`||s_1 v_1 wedge s_2 v_2 wedge d||^2
 =s_1^2 s_2^2 ||P_(span(v_1,v_2)^perp)d||^2
 =s_1^2 s_2^2 F^2`.                                               (2.5)

By Cauchy--Binet, `E_3(K)` is the sum of squared norms of all three-row exterior products (equivalently all squared physical `3x3` minors after summing columns). The nonnegative summand (2.5) is therefore bounded above by `E_3(K)`, proving (2.3). Equation (2.4) is the direct application of (1.6). QED.

This theorem is insensitive to signs and to repeated singular values. If `s_1=s_2`, choose any orthonormal basis of the top two-dimensional singular subspace; (2.3) is valid for that choice. Degenerate `s_2=0` is outside the claimed rank-two gate and is handled elsewhere in the proof graph.

## 3. Robust deletion of one light coordinate from an ultra-thin rank-two crossing

Return to the live `N=A[R,C]` satisfying (1.1)--(1.3). Let

`N_2=s_1 u_1v_1^T+s_2u_2v_2^T`,
`E=N-N_2`,

so

`||E||_F<tau=2^-16`.                                               (3.1)

For every physical `j in C`, define the top-two coordinate leverage

`ell_j=v_1(j)^2+v_2(j)^2`.                                        (3.2)

Then

`sum_(j in C) ell_j=2`,                                           (3.3)

so there are at most three coordinates with `ell_j>1/2`.

Call all other coordinates **light**. Fix a light `j`, put `J=C\{j}`, and let

`M_j=A[R,J]`.

Deleting coordinate `j` from the exact rank-two part gives

`N_2^{(j)}=N_2 P_J`.

If `z=(v_1(j),v_2(j))^T`, then on the left singular two-plane its Gram matrix is

`Sigma (I_2-zz^T) Sigma`.                                         (3.4)

Since `||z||^2=ell_j<=1/2`,

`I_2-zz^T >= (1-ell_j)I_2 >= (1/2)I_2`.                           (3.5)

Hence, writing `a_j>=b_j>0` for the two nonzero singular values of `N_2^{(j)`,

`b_j>=s_2/sqrt(2)>=1/(64 sqrt(2))`,                               (3.6)

and the determinant identity gives the sharper product formula

`a_j b_j=s_1s_2 sqrt(1-ell_j)>=gamma_0/sqrt(2)`.                  (3.7)

The deleted tail obeys

`||M_j-N_2^{(j)}||_op <=||E||_F<tau`.                             (3.8)

Weyl's singular-value inequality therefore yields

`s_1(M_j)s_2(M_j)
 >=(a_j-tau)(b_j-tau)
 >=a_jb_j(1-delta)^2`,                                            (3.9)

where

`delta=tau/(1/(64sqrt(2)))=64sqrt(2) 2^-16
      =0.0013810679320049757...`.                                 (3.10)

Combining (3.7)--(3.10), every light coordinate obeys the uniform physical rank-two lower bound

`boxed: s_1(M_j)s_2(M_j)>Gamma_0}`,                               (3.11)

with

`Gamma_0=(gamma_0/sqrt(2))(1-delta)^2
        =0.0033475488096756326...`.                               (3.12)

No dimension enters this estimate.

## 4. Same-bank curvature is either paid or physically aligned

For light `j in C`, define the literal same-bank row into the remaining coordinates

`d_j=A[j,J]`,                                                     (4.1)

and let

`F_j=dist(d_j,V_2(M_j))`,                                        (4.2)

where `V_2(M_j)` is a top-two right singular subspace of the **actual** deleted cross block `M_j`.

The literal row bank `R union {j}` and column bank `J` are disjoint original-coordinate sets, so Theorem 2.1 applies without any provenance loss:

`E_3(A[R union {j},J])
 >=Gamma_0^2 F_j^2`.                                              (4.3)

Take the fixed physical threshold

`f_0=2^-12`.                                                       (4.4)

If some light coordinate satisfies `F_j>=f_0`, then (1.6) and (4.3) give the **full ambient law**

`||p_Q||_infinity
 <=C_E3 (Gamma_0^2 f_0^2)^(-1/6)
 =904.1135320...<905.`                                            (4.5)

The density is continuous and vanishes at infinity.

Therefore every still-unpaid strong-rank-two r47 state satisfies

`boxed: for every j in C with ell_j<=1/2,
 dist(A[j,C\{j}],V_2(A[R,C\{j}]))<2^-12.}`                        (4.6)

Only at most three coordinates of `C` can escape (4.6).

Transpose the entire construction. Define the analogous top-two **left** leverage on `R`. Its sum is also two, so at most three coordinates of `R` have leverage `>1/2`. For every remaining `i in R`, apply Theorem 2.1 to the literal cross block with row bank `C union {i}` and column bank `R\{i}`. Thus an unpaid state also satisfies

`boxed: for every light i in R,
 dist(A[i,R\{i}],V_2(A[C,R\{i}]))<2^-12.}`                        (4.7)

where the displayed `V_2` is understood in the corresponding coefficient space after transposition.

### Corollary 4.1 — `QFORM-STRONGR2-INTERNAL-CURVATURE-HEAVY6-FUNNEL-v1`

The live r47 strong physical rank-two branch is now exhausted by:

1. a paid continuous-density physical-`E3` exit with `||p_Q||_infinity<905`; or
2. an unpaid survivor having at most three high-top-two-leverage physical coordinates on each bank, while every other physical same-bank row lies within `2^-12` of the adaptive two-dimensional right/left singular plane obtained after deleting that coordinate.

Thus arbitrary internal curvature can no longer remain freely transverse across a diffuse collection of physical coordinates in the strong-rank-two chamber.

### Important limitation

Do **not** sum the `<2^-12` row errors over all light coordinates and call the whole same-bank matrix a dimension-free small perturbation. Such a Frobenius sum can grow with dimension, and the input laws have no moment assumptions. Also, the adaptive planes `V_2(M_j)` vary with `j`. The next step must aggregate those alignments before any supremum/fiber operation or use the at-most-six heavy coordinates as literal hubs. This is precisely where the remaining product structure must be spent.

## 5. Compact conditional full-proof assembly after this run

The current proof graph supports the following conditional closure statement.

* Principal-minimal same-constant descent removes reducible extra threshold spectrum.
* Existing diagonal/pivot/pair, grouped-crossing, ridge/window, physical-`E3`, cross-null-curvature and singular-pair compilers pay their stated branches without rotating independence or discarding nonzero tails.
* r47 sends its large-leaf-curvature chamber either to physical `E3`, to a fixed-strength ultra-thin physical rank-two crossing (the branch treated here), or to the giant near-rank-one frontier.
* Fresh account02/B19 pays the pure-bilinear subcase of the strong-rank-two branch by `<51.44981` and proves that stronger post-Schur `E2/E3` forcing is impossible in general.
* The present run pays every strong-rank-two state with a transverse light same-bank row by `<905`; the only same-bank survivor has the heavy-six/adaptive-alignment structure (4.6)--(4.7).

Hence the first essential missing implication on this route is now

`QFORM-HEAVY6-ADAPTIVE-R2-SELF-CURVATURE-PAYMENT-v1`:

> pay the strong physical rank-two crossing when all but at most three coordinates per bank have same-bank rows within `2^-12` of their deleted-cross top-two singular planes, retaining the genuine nonzero rank-two tail and arbitrary outside couplings; or route it to an already-paid grouped-hub, scalar/pair, physical-volume, cross-null-curvature, ridge/window, or principal-block exit.

The giant near-rank-one and rank-<=9 carrier frontiers remain separate debts. Thus this run is a genuine narrowing of the first strong-rank-two debt, not a full theorem.

## 6. Designated partner account04/B19 applied at an actual inequality

The designated partner source remains

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`,

theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`.

In its exact residual-diffuse rank-three null-coloop normal form, and **only** there, for `0<D_res<=1` and the partner normalization `|det M|>=1`,

`||p_Q||_infinity<34 sqrt(log(e/D_res))`,                          (6.1)

with continuous density. Therefore the concrete gate

`2^-24<=D_res<=1`                                                  (6.2)

gives

`boxed: ||p_Q||_infinity
 <34 sqrt(log(e 2^24))
 =142.7819154...<143.`                                             (6.3)

This is an actual equation-level application of the completed designated-partner theorem. No claim is made that the heavy-six adaptive-rank-two survivor automatically has the partner's exact-null-coloop form, and no near-null interpolation is inferred.

## 7. Rigorous computation checks

A finite diagnostic checker (not a proof substitute) tested Theorem 2.1 on 3,000 random noncommuting rectangular matrices and random symmetric same-bank blocks. The minimum observed ratio

`E3([M;d]) / ([s1(M)s2(M)]^2 dist(d,V2(M))^2)`

was `0.9999999999999941`; there were zero violations, with maximum normalized numerical deficit `1.95e-15`.

A separate 5,000-instance test constructed matrices with `s_2>=1/64` and Frobenius rank-two tail at most `2^-16`; for every top-two-leverage-light deleted coordinate it checked (3.9)--(3.12). There were zero violations and minimum observed actual-product / claimed-lower-bound ratio `1.0003054`.

The exact constants used above are

`gamma_0=0.00474725242887306...`,
`delta=0.0013810679320049757...`,
`Gamma_0=0.0033475488096756326...`,
`C_E3(Gamma_0^2 2^-24)^(-1/6)=904.1135320...`,

and the designated-partner gate (6.3) is `142.7819154...`.

## 8. Status

The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. This run proves a target-level payment and a physical structural funnel in the strong-rank-two chamber, but does not pay the final adaptive-alignment/heavy-six survivor, the giant near-rank-one branch, or the remaining rank-<=9 carrier.

No scheduler state, task identity, enabled/paused state, notification, email, permission, installation, public-release, paid-call, remote workflow, or cross-account authentication state is changed by this report.
