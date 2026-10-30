SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T17:20:04Z.
attacking: the r42 adaptive R1/R2 alignment packets by exact original-coordinate conditioning, then a two-sided Pluecker split that either creates physical E3 smoothing or reduces R2 to the same finite common-plane cycle isolated by the assembly workers.

# fleet03/B08 r43 — adaptive-hub conditioning collapse and two-sided Pluecker/E3 router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T172004Z-fleet03-B08-qform-diffuse-r43`  
Assignment: diffuse eigenvector case  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Final owner control used before publication: revision `2026-09-22.15`, brain main `dbce8d8c240977172f159ddd4c4abaf3cb43d032`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: `NEW EXACT CONDITIONING REDUCTION + NEW TWO-SIDED PLUECKER BISECTION + NEW MARGINAL-FREE E3 PAYMENT / FULL TARGET OPEN`.

The unrestricted QFORM conjecture remains **OPEN**. Global continuity remains open. The new E3-paid branches below have continuous `C_0` densities. Every conditioning step is on original independent coordinates. No moment, bounded-support, connected-support, Gaussian, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, pointwise quadratic-phase decay, coefficient-small random-error deletion, one-good-minor selection, or fiber-supremum argument is used.

## 1. Source-pinned incoming state

The immediate predecessor is

`yspennstate/math-open-problems@d2d64042e84bba8609cd2a27ae2dada21e215c38`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T165737Z-fleet03-B08-qform-diffuse-r42/REPORT.md`.

Its R2 branch starts from two **actual physical hub coordinates** `H`, a light complement `I`, and a physical outside bank `J`. Let

`M=A[H,J]` (a `2 x |J|` matrix),

`B=A[I,J]`,

and let `Pi` project onto `row(M)`. The r42 physical extraction gives

`S:=s_1(M)s_2(M)>L^2/(64 sqrt(2)).`                                (1.1)

On its adaptive-alignment branch,

`B=K M+E`,                                                         (1.2)

where `K` is a physical-row coefficient matrix and the predecessor records `||E||_F<L/8`. The size of `E` will not be used below: after conditioning on `X_I`, the whole `x_I^T E X_J` term is affine in the still-random `J` variables and therefore is retained exactly rather than treated as a small random perturbation.

The R1 branch analogously has one actual hub coordinate `h`, an outside partner vector `w_J` satisfying

`||w_J||_2>sqrt(3/2)L/8`,                                         (1.3)

and an adaptive low-rank description of `A[I,J]`.

Two newer source-pinned results are used.

1. The reviewed grouped projected-crossing bundle is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

2. More importantly for this run, fleet03/B02 subsequently removed the third-volume row-marginal gate:

`yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T170106Z-fleet03-B02-qform-r35/REPORT.md`.

Its theorem `QFORM-CROSS-E3-MARGINALFREE-L1-v1` says that for every **literal original-coordinate physical cross block** `N` with

`Z_3=e_3(NN^T)>0`,                                                (1.4)

the entire ambient quadratic-affine form has a continuous `C_0` density and

`||p_Q||_infinity <= C_E3 Z_3^(-1/6)`,                            (1.5)

where

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775... .`                 (1.6)

Arbitrary same-bank quadratic terms, all outside couplings, affine terms, all signs and arbitrary rank are retained.

The newest assembly peer fleet03/B19 also supplied an exact common-plane cycle identity at commit

`dbfe84527051235b5614ee4edb74754b28eb9dd5`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T170040Z-fleet03-B19-qform-r37/REPORT.md`.

It will be applied only as deterministic coefficient algebra after the new R2 reduction below.

## 2. First essential implication: adaptive alignment disappears under legitimate conditioning

### Lemma 2.1 — `QFORM-ADAPTIVE-HUB-CONDITIONING-COLLAPSE-v1`

Let the original independent coordinates be partitioned as `H disjoint_union I disjoint_union J disjoint_union K0`, with `|H|=k`. Condition on every coordinate in `K0` first, so it suffices to suppress `K0`. Write

`M=A[H,J]`, `B=A[I,J]`.                                           (2.1)

For **any** deterministic matrix `K` of size `|I| x k`, condition on `X_I=x`. Define

`Z=X_H+K^T x`.                                                    (2.2)

Then, conditional on `X_I=x`, the coordinates of `Z` are independent and each has a density bounded by one; `Z` is independent of `X_J`. Moreover the conditional quadratic form can be written exactly as

`Q_x=F_x(Z)+2 Z^T M X_J+R_x(X_J)`,                               (2.3)

where `F_x` is a quadratic-affine polynomial in the `k` hub variables and `R_x` is a quadratic-affine polynomial in the `J` variables **provided that every cross term from `I` to `J` not equal to `KM` is absorbed into the affine part of `R_x`**. Explicitly,

`2 X_H^T M X_J+2x^T B X_J
 =2 Z^T M X_J+2x^T(B-KM)X_J`.                                    (2.4)

The last term is affine in `X_J` because `x` is frozen. Every `H-H`, `H-I`, `I-I`, diagonal and previously conditioned outside term is likewise absorbed into `F_x`, `R_x` or the constant term. No coefficient is discarded.

#### Proof

Conditional on `X_I=x`, (2.2) is a deterministic coordinatewise translation of the original physical hub vector `X_H`, hence preserves independence and every cap-one density. Equation (2.4) is direct expansion. All other assertions are bookkeeping of a quadratic polynomial after an original-coordinate conditioning. QED.

### Consequence for r42

On R2-A choose the `K` from (1.2). The residual `E` contributes the exact affine term `2x^TEX_J`; its coefficient size is irrelevant. Thus the entire adaptive R2 packet reduces, conditionally and without approximation, to the canonical two-physical-hub form

`Q_x=F_x(Z_1,Z_2)+2 Z^T M X_J+R_x(X_J)`                           (2.5)

with (1.1).

On R1-A the same argument reduces the entire adaptive packet to

`Q_x=F_x(Z)+2 Z <w_J,X_J>+R_x(X_J)`                              (2.6)

with (1.3). In particular, the predecessor's extra rank-one channel and its `<L/8` coefficient tail no longer need to be treated as random perturbations after conditioning: they are affine in `X_J`. The remaining R1 analytic obstruction is exactly the canonical **single physical hub with an arbitrary quadratic light remainder**. This is the same one-hub boundary isolated in the current `single_hub_core` continuation; this run does not claim to close it.

A uniform conditional density estimate for (2.3) transfers to the unconditional form: for every Borel set `E0`,

`P(Q in E0)=E[P(Q_x in E0 | X_I)]<=C |E0|`.                      (2.7)

If the conditional representatives are continuous `C_0` and uniformly bounded by `C`, dominated convergence also gives a continuous `C_0` representative after averaging.

## 3. A new two-sided Pluecker bisection lemma

The R2 partner matrix `M` in (2.5) has row rank two. For physical columns `j<k` put

`w_jk=det(M[:,{j,k}])^2`,

`Z=sum_{j<k} w_jk=det(MM^T)=S^2`,                                (3.1)

and define the normalized Pluecker inclusion marginals

`alpha_j=Z^(-1) sum_{k!=j} w_jk`.                                (3.2)

They satisfy `sum_j alpha_j=2`.

### Lemma 3.1 — `QFORM-PLUECKER-TWO-SIDED-BISECTION-v1`

If

`max_j alpha_j<=1/2`,                                             (3.3)

then there is a partition of the **physical columns**

`J=J_1 disjoint_union J_2`                                       (3.4)

such that, writing

`Z_r=det(M_rM_r^T)`, `M_r=M[:,J_r]`,                              (3.5)

one has

`boxed: Z_1 Z_2 >= Z^2/448`,                                     (3.6)

and consequently

`boxed: Z_r>=Z/448,  r=1,2`.                                     (3.7)

Equivalently, if `S_r=s_1(M_r)s_2(M_r)=sqrt(Z_r)`, then

`boxed: S_r>=S/sqrt(448).}`                                      (3.8)

If (3.3) fails, one actual physical column `j` carries more than half of the complete second-exterior mass:

`sum_{k!=j} det(M[:,{j,k}])^2>Z/2`.                              (3.9)

#### Proof of the diffuse case

Normalize `x_e=w_e/Z` on the edges `e={j,k}` of the complete graph on the physical columns. Thus `sum_e x_e=1` and the weighted degree of vertex `j` is `alpha_j`.

Take two independent random edges `E,F` with law `x`. The ordered disjoint-edge mass is

`D=P(E cap F=empty)
 =1-sum_j alpha_j^2+sum_e x_e^2`.                                (3.10)

Indeed `sum_j alpha_j^2` counts the event that the two edges meet, with the event `E=F` counted twice rather than once, so one subtracts `sum_e x_e^2` from the intersection probability.

Put

`delta=1-sum_j alpha_j^2
      =sum_j alpha_j(1/2-alpha_j)>=0`,                            (3.11)

where `sum alpha_j=2` was used. If `delta>=1/28`, then `D>=1/28` immediately.

Assume `delta<1/28` and let

`S0={j: alpha_j>=1/4}`.                                          (3.12)

For `j notin S0`,

`alpha_j(1/2-alpha_j)>=alpha_j/4`,

so

`sum_{j notin S0} alpha_j<=4delta`.                              (3.13)

Every edge not wholly contained in `S0` contributes at least one incidence to the left side of (3.13). Hence the total edge mass internal to `S0` is at least `1-4delta`. Also `|S0|<=8`, since every such vertex has degree at least `1/4` while the total degree is `2`. Therefore Cauchy--Schwarz over at most `binom(8,2)=28` internal edges gives

`sum_e x_e^2 >= (1-4delta)^2/28`.                                (3.14)

Combining (3.10)--(3.14),

`D>=delta+(1-4delta)^2/28>=1/28`,                                (3.15)

because the final expression is increasing for `delta>=0`.

Now color every physical column independently red or blue with probability `1/2`. Let `A` be the normalized Pluecker mass of edges with both endpoints red and `B` the corresponding blue mass. For ordered edges `e,f`, the event that `e` is all-red and `f` all-blue has probability `1/16` exactly when `e` and `f` are disjoint, and probability zero otherwise. Hence

`E[A B]=D/16>=1/448`.                                            (3.16)

Some coloring therefore satisfies `AB>=1/448`. Multiplying by `Z^2` proves (3.6). Since each `Z_r<=Z`, (3.7) follows. QED.

### Numerical scale inherited from r42

From (1.1),

`Z=S^2>L^4/8192`.                                                 (3.17)

Therefore the localized alternative (3.9) gives the explicit original-coordinate certificate

`boxed: sum_{k!=j} det(M[:,{j,k}])^2>L^4/16384.}`                 (3.18)

On the diffuse alternative, both split partners satisfy

`boxed: S_r>L^2/(64 sqrt(896)).}`                                (3.19)

No individual minor was selected or inverted.

## 4. R2 diffuse partner: transverse internal curvature forces physical E3

Assume the diffuse Pluecker branch and use the physical split (3.4). Let

`C=A[J_1,J_2]`,                                                   (4.1)

and let `P_r` be the orthogonal projection in the physical coefficient space `R^{J_r}` onto `row(M_r)`. Define the two transverse internal-crossing sizes

`F_L=||(I-P_1)C||_F`,
`F_R=||C(I-P_2)||_F`.                                             (4.2)

### Lemma 4.1 — exterior injection on either side

For the literal original-coordinate physical cross block

`N_L=A[J_1,H union J_2]=[M_1^T,C]`,                               (4.3)

one has

`boxed: e_3(N_LN_L^T)>=Z_1 F_L^2.}`                              (4.4)

Similarly, for

`N_R=A[J_2,H union J_1]=[M_2^T,C^T]`,                             (4.5)

`boxed: e_3(N_RN_R^T)>=Z_2 F_R^2.}`                              (4.6)

#### Proof

In `N_L`, keep only the three-column minors using both physical hub columns and one column of `C`. For a column `c` of `C`, the Gram determinant of `[M_1^T,c]` is

`det(M_1M_1^T) ||(I-P_1)c||_2^2=Z_1||(I-P_1)c||_2^2`.

Cauchy--Binet and summation over all columns of `C` give (4.4); all omitted three-column minors are nonnegative squared volumes. Equation (4.6) is the transposed argument. QED.

### Theorem 4.2 — `QFORM-R2-TRANSVERSE-E3-OR-COMMONPLANE-v1`

Fix the concrete transverse threshold

`rho=1/16`.                                                       (4.7)

Under the r42 R2 state (1.1), exactly one of the following useful alternatives occurs.

**R2-P (paid transverse E3).** If `F_L>=rho L` or `F_R>=rho L`, then the full ambient quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity<330.175/L.}`                            (4.8)

**R2-C (two-sided common-plane survivor).** If both are smaller than `rho L`, then with

`C_0=P_1 C P_2`, `T=C-C_0`,                                      (4.9)

one has

`boxed: ||T||_F<L/8,}`                                           (4.10)

and the exact common-plane part factors as

`boxed: C_0=M_1^T R M_2}`                                       (4.11)

for the deterministic `2 x 2` matrix

`R=(M_1M_1^T)^(-1) M_1 C M_2^T (M_2M_2^T)^(-1).`                 (4.12)

Both physical hub legs retain the quantitative determinant currency (3.19).

#### Proof of R2-P

Suppose `F_L>=L/16`; the other orientation is identical. From (3.7), (3.17) and (4.4),

`e_3(N_LN_L^T)
 > [L^4/(8192*448)] [L^2/256]
 = L^6/(8192*448*256).`                                          (4.13)

Apply the marginal-free physical E3 theorem (1.5):

`||p_Q||_infinity
 < C_E3 (8192*448*256)^(1/6) L^(-1)
 =330.1749063999598.../L.`                                       (4.14)

The source theorem gives Fourier `L^1`, hence a continuous `C_0` density. Notice that **no projected-crossing row marginal remains** in this payment.

#### Proof of R2-C

The exact decomposition

`C-P_1CP_2=(I-P_1)C+P_1C(I-P_2)`                                 (4.15)

gives

`||T||_F<=F_L+F_R<L/8`,                                          (4.16)

which is (4.10). Formula (4.11) follows by inserting the explicit projections

`P_r=M_r^T(M_rM_r^T)^(-1)M_r`                                    (4.17)

on both sides of `C`. QED.

This is the main r43 advance. The r42 adaptive R2 state is no longer a vague low-rank leakage packet. After a legitimate conditioning collapse, it is routed as follows:

1. a **localized physical partner column** with anchored second-volume `>L^4/16384`; or
2. a **continuous physical-E3 payment `<330.175/L`**; or
3. a **quantitative two-sided common-plane cycle**, with both rank-two partner legs bounded below by (3.19) and every non-common-plane internal crossing retained in a coefficient tail of Frobenius norm `<L/8`.

No coefficient tail is deleted probabilistically.

## 5. Exact finite common-plane algebra and proof-graph merge

In branch R2-C choose orthonormal frames `U_r` for `row(M_r)` and write

`N_r=M_r U_r in R^{2 x 2}`,                                      (5.1)

`D=U_1^T C U_2 in R^{2 x 2}`.                                   (5.2)

Then `N_r` is invertible and

`|det N_r|=S_r>L^2/(64sqrt(896)).`                               (5.3)

The exact compressed cross-only skeleton on the deterministic coefficient spaces

`row(M_1) direct_sum row(M_2) direct_sum R^H`

is

`H_0=[[0,D,N_1^T],
      [D^T,0,N_2^T],
      [N_1,N_2,0]].`                                             (5.4)

Apply the completed fleet03/B19 common-plane algebra to

`C=D`, `N=N_1^T`, `P=N_2^T`.                                    (5.5)

With

`R_cyc=N_1^(-T) D N_2^(-1)`,                                    (5.6)

it gives the actual identities

`boxed: det H_0=det(N_1)^2 det(N_2)^2 det(R_cyc+R_cyc^T),}`       (5.7)

`boxed: rank H_0=4+rank(R_cyc+R_cyc^T).}`                        (5.8)

These are deterministic coefficient identities only. The grouped variables `U_r^TX_{J_r}` are **not** declared to have independent coordinates. The physical tail `T` from (4.10), all same-bank curvature and all other spectrum remain in the real quadratic form.

Thus the r42 diffuse route and the current B19 assembly route now meet the **same finite common-plane cycle geometry**. The next analytic task is not another high-dimensional rank extraction; it is a product-provenance receiver for this cycle that is stable under the retained `<L/8` physical coefficient tail.

## 6. R1 is now identified exactly with the canonical one-hub obstruction

On r42 R1-A, condition on its light complement `I`. Equation (2.4) gives, after a scalar hub translation,

`Q_x=F_x(Z)+2Z<w_J,X_J>+R_x(X_J)`,                               (6.1)

with

`||w_J||>sqrt(3/2)L/8`.                                         (6.2)

All other `I-J` cross terms, including the predecessor's rank-one aligned channel and the coefficient tail, are affine in `X_J` after conditioning and are retained in `R_x`.

Therefore the remaining R1-A problem is **exactly** a strong physical single-hub row against an arbitrary quadratic light remainder. This matches the current `single_hub_core` boundary: arbitrary remainder gives the known borderline one-hub Fourier/small-ball estimates, but a universal `L^infinity` bound in the fully entangled arbitrary-law case is not yet available. This run does not relabel that open one-hub problem as solved.

This identification is useful because it prevents further work on irrelevant rank-one decompositions of `A[I,J]`: once `I` is conditioned, those coefficients are affine data. The only genuinely nonlinear random resources left are the physical hub and the `J-J` quadratic remainder.

## 7. Designated partner fleet04/B08 applied to an actual inequality

The designated partner source is

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

For

`Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`, `R>=3`,            (7.1)

it proves

`boxed: ||p_(Q_(R,L))||_infinity<7.251/L.}`                      (7.2)

This is an actual endpoint on the **localized Pluecker side** of Lemma 3.1. Its partner block is

`M=L diag(R,R^(-1))`,                                             (7.3)

so `Z=det(MM^T)=L^4` and there is only one nonzero two-column Pluecker edge. Hence both physical column marginals are exactly one, maximally violating the diffuse gate (3.3). The new bisection theorem correctly refuses to call this state diffuse; the designated partner theorem pays the canonical extreme directly by (7.2), uniformly as `R^2 -> infinity`.

I do **not** extend (7.2) to every localized-Pluecker R2 state. The general localized branch (3.18) remains for localized-coordinate conditioning/grouped receivers.

## 8. Continuity, signs and correction ledger

The R2-P branch is continuous `C_0` because the marginal-free E3 source supplies a genuine integrable characteristic function. R2-C and R1-A are structural reductions only; no continuity is claimed there. The fleet04/B08 grouped endpoint proves essential boundedness but does not assert continuity.

All signs are allowed. Repeated singular values cause no problem: `P_r` is the orthogonal projection onto the full two-dimensional row space of `M_r`, independent of a singular basis. The Pluecker bisection is carried out on actual physical columns. Orthogonal frames `U_r` appear only after the physical split and only for deterministic coefficient algebra; their projected random coordinates are never declared independent.

The new conditioning lemma is deliberately different from an illegal post-rotation conditioning. We condition on the original coordinates `X_I`; translated physical hubs retain their original product density caps. The residual `x^TEX_J` is an affine term because `x` is fixed, not because `E` is coefficient-small.

## 9. What remains

The unrestricted QFORM conjecture is still **OPEN / NOT DISPROVED**.

The r42 adaptive alignment debt is sharpened to two already-recognizable analytic boundaries:

1. **R1:** canonical single physical hub with arbitrary light quadratic remainder and a strong partner row (6.1)-(6.2).
2. **R2:** localized partner second-volume (3.18), or the quantitative common-plane `2+2+2` cycle (5.4) with both invertible legs bounded below by (5.3) and a retained physical coefficient tail `<L/8`.

The next B08 task should be

`QFORM-R2-COMMONPLANE-TAIL-STABLE-PRODUCT-RECEIVER-v1`:

consume the common-plane cycle using the original product provenance of the three physical banks, while retaining the `<L/8` coefficient tail, arbitrary same-bank curvature and every unused coupling. The exact B19 invariant (5.7)-(5.8) is now available at this B08 endpoint. In parallel, the R1 survivor should use the fleet's canonical single-hub machinery rather than further matrix-rank bookkeeping.

## 10. Regression checks

The companion `CHECKS.py` independently recomputes

`C_E3=10.550168831164775...`,

`C_R2=330.1749063999598...`,

and the designated-partner constant

`C_partner=7.250055108887958...`.

It tests the disjoint-edge identity (3.10) and exhaustively searches every two-coloring for hundreds of random physical `2 x m` matrices satisfying the diffuse Pluecker gate, verifying the analytic target `Z_1Z_2/Z^2>=1/448`. The observed minimum is much larger than the proved constant; this is regression evidence only. It terminates

`QFORM_B08_R43_CHECK_PASS`.
