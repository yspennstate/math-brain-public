SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T17:15:44Z.
attacking: the common-plane STAR4 residue; first remove the obsolete third-volume row-marginal escape using the newest marginal-free E3 Fourier theorem, then quantify a coherent scalar cycle inside the remaining 2+2+2 coefficient core without deleting any tail.

# fleet01/B19 — marginal-free E3 closure and coherent common-plane cycle

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / TWO STRUCTURAL GATES SHARPENED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved on the E3-paid branches below; not claimed for the common-plane/heavy-leverage residue or for the full target.

## 1. Fresh control, target and correction ledger


The exact target remains: for arbitrary independent real scalar inputs with densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite `L^infinity` density bound for `X^T A X`, or give a valid counterexample. Continuity is tracked separately.

The live correction state was reread. Nothing below uses post-rotation independence, arbitrary-joint rank-three coarea, positive conditional projection-density moments, law-uniform pointwise quadratic Fourier decay, a fixed-good-minor principle, deletion of a nonzero matrix tail, or replacement of a product-origin grouped bank by an arbitrary bounded joint density.

## 2. Source-pinned incoming common-plane state

The immediate B19 predecessor is

`yspennstate/math-open-problems@97a77b266879a93eb43ad36555ffdec1d981ebe0`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260923T165949Z-fleet01-B19-QFORM-auto11b/REPORT.md`.

It starts from the balanced STAR4 partition

`J=D_1 disjoint_union D_2`, with common third bank `K`,

and physical cross blocks

`C=A[D_1,D_2]`, `N_1=A[D_1,K]`, `N_2=A[D_2,K]`.

The quantitative constants are

`tau=2^-20`,

`rho_*=63(1-tau)^2/16384
       =0.003845207509588222...`,                                (2.1)

`Delta_*=(3/8)rho_*
        =0.0014419528160955833...`,                              (2.2)

and, for both restrictions,

`rho_r=s_1(N_r)s_2(N_r)>=Delta_*`.                               (2.3)

The balanced-cut argument also gives the universal condition number bound

`s_1(N_r)/s_2(N_r)<kappa_0:=sqrt(1288/3)
 =20.72036035722674...`.                                         (2.4)

After the left-plane transverse D3 alternatives have failed, with `P_r` the top-two left singular projections,

`||(I-P_1)C||_F^2<F/64`,
`||C(I-P_2)||_F^2<F/64`,                                         (2.5)

and the grouped self edge

`C_0=P_1 C P_2`                                                   (2.6)

satisfies

`||C_0||_F^2 >=(9/16)F`,                                         (2.7)

where in the strong self-packet branch

`F=0.4537176735697731005/8
  =0.05671470919622164...`.                                      (2.8)

Let `Q_r` be the top-two RIGHT singular projection of `N_r` in the physical `K` bank. The predecessor proved, by applying the designated partner fleet02/B19 to the physical `K` orientation, that

`d_R^2:=||(I-Q_1)Q_2||_F^2`                                     (2.9)

forces the literal physical third volume

`Z_K:=e_3([N_1^T,N_2^T][N_1^T,N_2^T]^T)
     >=(Delta_*^3/kappa_0)d_R^2`.                               (2.10)

In particular, if `d_R^2>=1/64`,

`Z_K >= Z_*:=Delta_*^3/(64 kappa_0)
             =2.260871454155696e-12...`.                         (2.11)

The exact theorem used to obtain (2.10) is the designated partner result

`fleet02/B19`, commit
`9157730c1b552b81f58b3cb6ef604b687962e548`,

`QFORM-OVERLAP-MIXED-EXTERIOR-VOLUME-v1`:
for disjoint physical banks and `N=A[I,K]`, `M=A[I,J]`,

`e_3([M,N][M,N]^T)
 >=(s_1(N)s_2(N))^2 ||(I-P_2)M||_F^2`.                           (2.12)

Equation (2.10) is an actual application of (2.12), not a generic citation: set the partner row bank to `K`, `N=N_1^T`, `M=N_2^T`, and use

`||(I-Q_1)N_2^T||_F^2
 >=s_2(N_2)^2 d_R^2
 >=(Delta_*/kappa_0)d_R^2`.                                      (2.13)

## 3. New peer input: physical E3 no longer has a row-marginal gate

A newer same-hour peer result appeared after the predecessor:

`fleet03/B02`, commit
`d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T170106Z-fleet03-B02-qform-r35/REPORT.md`.

Its theorem `QFORM-CROSS-E3-MARGINALFREE-L1-v1` states that for **every actual original-coordinate physical cross block** `M` with

`Z=e_3(M^T M)>0`,                                                 (3.1)

the full ambient quadratic form, retaining arbitrary same-bank self blocks, outside couplings, affine terms and all signs, has

`||p_Q||_infinity <= C_E3 Z^(-1/6)`,                             (3.2)

`integral_R |phi_Q(t)|dt <=2pi C_E3 Z^(-1/6)`,                   (3.3)

where

`C_E3=3*2^(4/3)*exp(1/3)
    =10.550168831164775...`.                                     (3.4)

Thus the density is continuous and vanishes at infinity. The proof removes the former row-volume marginal gate by a physical one-hub -> two-hub -> three-hub descent; it does not replace grouped variables by arbitrary joint laws.

I use this peer result only at its stated physical-cross-block scope.

## 4. First new payment: right-plane mismatch is now unconditional

### Theorem 4.1 — `QFORM-STAR4-RIGHTPLANE-MISMATCH-MARGINALFREE-v1`

In the common-plane predecessor setup (2.1)-(2.10), if

`d_R^2>=1/64`,                                                    (4.1)

then the **full ambient target law** has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <920.903.`                              (4.2)

### Proof

The designated partner identity applied in (2.10)-(2.13) gives the literal original-coordinate physical cross block

`M_K=A[K,D_1 union D_2]=[N_1^T,N_2^T]`                           (4.3)

with

`e_3(M_K^T M_K)=e_3(M_KM_K^T)>=Z_*`.                            (4.4)

Apply the marginal-free peer theorem (3.2):

`||p_Q||_infinity
 <=C_E3 Z_*^(-1/6)
 =920.9020318006362...<920.903.`                                 (4.5)

Equation (3.3) gives continuity. No third-volume row marginal remains to be checked. QED.

This replaces the predecessor's old split

`D'/D3 paid OR physical row-volume anchor`

by one unconditional E3 payment whenever the fixed mismatch threshold (4.1) holds. In particular, a highly concentrated physical third-volume row is no longer an unpaid branch here.

Exactly the same upgrade applies to the r37 left/right transverse packet. Its fixed lower bound

`Z_3>1.8425438602123219e-9`                                      (4.6)

now yields unconditionally

`boxed: ||p_Q||_infinity <301.317}`                              (4.7)

with continuity, again without any row-marginal alternative.

## 5. The surviving coefficient geometry: a genuine common 2+2+2 triangle

Failure of (4.1) means

`d_R^2<1/64`.                                                     (5.1)

The predecessor then showed

`|det(V_2^T V_1)|>63/64`,                                        (5.2)

where `V_r` are orthonormal frames for `Q_r`. Taking the common `K` plane to be `Q:=Q_1`, define the actual compressed cross maps

`A_12:=P_1 C P_2 : P_2 -> P_1`,
`A_13:=P_1 N_1 Q : Q -> P_1`,
`A_23:=P_2 N_2 Q : Q -> P_2`.                                   (5.3)

Each source/range space is two dimensional and these are deterministic compressions of the **actual** physical coefficient matrix, not new random coordinates. They satisfy

`||A_12||_F^2 >=(9/16)F`,                                       (5.4)

`s_1(A_13)s_2(A_13)>=Delta_*`,                                  (5.5)

`s_1(A_23)s_2(A_23)>(63/64)Delta_*`.                            (5.6)

All nonzero tails of the actual three cross blocks remain present outside (5.3). Equations (5.3)-(5.6) merely identify the core.

## 6. New exact inequality: every such 2+2+2 core contains a coherent scalar cycle

### Theorem 6.1 — `QFORM-COMMONPLANE-COHERENT-CYCLE-ENERGY-v1`

Let `R,S,T` be arbitrary real `2 x 2` matrices. There exist unit vectors

`x,y,z in S^1`                                                   (6.1)

such that

`boxed:
 |x^T R y| |x^T S z| |y^T T z|
 >= ||R||_F ||S||_F ||T||_F /(16 sqrt(2)).
}`                                                                (6.2)

No invertibility, sign, simplicity or genericity assumption is required. If one matrix vanishes the assertion is vacuous; otherwise it gives a nonzero coherent three-cycle.

### Proof

Let `x,y,z` be independent uniform unit vectors on `S^1`. For any `p,q in R^2`, the fourth-moment identity is

`E_x[(x^T p)^2(x^T q)^2]
 = (||p||^2||q||^2+2(p^Tq)^2)/8`.                               (6.3)

For fixed `y,z`, apply (6.3) with `p=Ry`, `q=Sz`:

`E_x[(x^T R y)^2(x^T S z)^2]
 >= ||Ry||^2 ||Sz||^2/8`.                                       (6.4)

Multiply by `(y^T Tz)^2` and average in `y`. With `P=R^TR` and `c=Tz`, the same fourth-moment identity gives

`E_y[(y^T P y)(y^T c)^2]
 = [tr(P)||c||^2+2c^TPc]/8
 >= ||R||_F^2 ||Tz||^2/8`.                                      (6.5)

Therefore

`E_{x,y}[(x^T R y)^2(x^T S z)^2(y^T Tz)^2]
 >= ||R||_F^2 ||Sz||^2||Tz||^2/64`.                             (6.6)

Finally, with `P=S^TS`, `Q=T^TT`,

`E_z[(z^TPz)(z^TQz)]
 =[tr(P)tr(Q)+2tr(PQ)]/8
 >=||S||_F^2||T||_F^2/8`,                                       (6.7)

because `P,Q` are positive semidefinite and `tr(PQ)>=0`. Combining (6.6)-(6.7),

`E[ (x^TRy)^2(x^TSz)^2(y^TTz)^2 ]
 >= ||R||_F^2||S||_F^2||T||_F^2/512`.                           (6.8)

The integrand is nonnegative, so some triple `(x,y,z)` is at least its mean. Taking square roots and `sqrt(512)=16sqrt(2)` proves (6.2). QED.

This is an exact finite-dimensional coefficient inequality. Orthogonal bases are used only in deterministic coefficient spaces; no rotated input coordinates are declared independent.

## 7. Quantitative application to the common-plane STAR survivor

Apply Theorem 6.1 to `(R,S,T)=(A_12,A_13,A_23)`.

For any `2 x 2` matrix `M`,

`||M||_F^2=s_1(M)^2+s_2(M)^2
 >=2s_1(M)s_2(M)`.                                                (7.1)

Hence (5.4)-(5.6) imply unit `x in P_1`, `y in P_2`, `z in Q` with

`|x^T A_12 y| |x^T A_13 z| |y^T A_23 z|
 >= gamma_*`,                                                     (7.2)

where

`gamma_*
 := [sqrt((9/16)F) sqrt(2Delta_*) sqrt(2(63/64)Delta_*)]
       /(16sqrt(2))`
`  = [3 Delta_* sqrt(F) sqrt(63/64)]/(32sqrt(2))`
`  =2.2585799611957883e-5...`.                                   (7.3)

Thus the common-plane survivor cannot hide its third resource by making every scalar cycle vanish. It contains a **quantitatively coherent three-edge cycle** in three disjoint product-origin banks.

The scalar variables

`U=<x,X_{D_1}>`, `V=<y,X_{D_2}>`, `W=<z,X_K>`                    (7.4)

are genuinely independent because their original-coordinate banks are disjoint. Their one-dimensional marginal density caps are universally bounded by the standard product-projection theorem. However, (7.2) by itself does **not** authorize conditioning on the orthogonal complements of these projections, nor does it authorize deleting the remaining cross/self terms. Those would violate the live correction ledger.

For scale only: in the much stronger tail-free rank-one-cycle model to which the completed three-bank scalar theorem applies, the value (7.3) would give

`2(3+log 8) gamma_*^(-1/3)<359.392`.                              (7.5)

Equation (7.5) is **not** asserted for the present ambient survivor. It records that coefficient extraction is no longer the obstruction; the unpaid step is the product-preserving analytic robustness to the rest of the quadratic form.

## 8. Sharpened first essential missing inequality

Before this run the branch list still contained a physical third-volume row-anchor escape. Section 4 removes that escape whenever fixed `E3` currency exists. Section 7 removes the possibility that the common `2+2+2` core has no coherent scalar cycle.

The first local debt on this route is therefore sharper:

`QFORM-COMMONPLANE-COHERENT-CYCLE-WITH-TAIL-LINFINITY-v1`:

> Let three disjoint original-coordinate banks carry the quantitative common-plane core (5.3)-(5.6), equivalently at least the coherent scalar cycle (7.2)-(7.3). Prove a universal `L^infinity` bound for the **actual ambient quadratic form** while retaining every same-bank quadratic term, every complementary cross component and every additional spectral direction; or route the state to a completed physical E3/ridge/pivot receiver. The bound must remain uniform as the complementary cross tails tend to zero and therefore cannot divide by the tail size.

The other explicit local residue is the heavy top-two physical leverage alternative

`max_i ||P_{top2}e_i||^2>1/320`,                                  (8.1)

which the balanced-cut theorem intentionally separated before the common-plane construction. The relative-rank-one STAR4 tube and the other already-recorded global strict-N3 branches also remain outside this local argument.

The important change is that **a D3/E3 row-volume anchor is no longer an independent debt** in the fixed-volume branches: the marginal-free E3 Fourier compiler pays it directly.

## 9. Compact conditional proof graph after this run

A correction-safe conditional assembly now reads:

1. Existing physical-pivot, ruled, semidefinite/definite-pair, exact-null, ridge-window, D/D5 and diffuse-tail theorems pay their exact stated gates.
2. Strict `N3(2^-20)` enters the established STAR/other structural compilation; in the STAR quantitative-rank-two branch `rho>=rho_*`.
3. Selected-volume and carrier arguments isolate either paid diffuse volume, finite-rank carrier, heavy leverage, or the aligned self-packet branch.
4. The balanced physical self cut preserves both bicore legs with product at least `Delta_*` and either produces fixed physical `E3` or a left-aligned `2+2` self edge.
5. **This run + fleet03/B02:** every fixed physical `E3` alternative is paid continuously with no row-marginal gate. In particular, the r37 transverse branch has density `<301.317`, and the right-plane mismatch branch has density `<920.903`.
6. Failure of right-plane mismatch gives one literal common `2+2+2` coefficient core. **This run:** that core necessarily contains a coherent scalar cycle with product strength `>2.2585e-5`.
7. What remains locally is not coefficient extraction but the tail-stable analytic payment in `QFORM-COMMONPLANE-COHERENT-CYCLE-WITH-TAIL-LINFINITY-v1`, together with the separately isolated heavy-leverage branch.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. There are not two independent end-to-end reviews. Global continuity remains open.

## 10. Verification and scope

`CHECKS.py` recomputes the exact source constants and verifies

- `Z_*=2.260871454155696e-12...`;
- the marginal-free mismatch bound `920.9020318006362...`;
- the marginal-free r37 transverse bound `301.31663157073905...`;
- `gamma_*=2.2585799611957883e-5...`;
- the reference tail-free rank-one-cycle value `<359.392`.

The checker terminates `STATUS=PASS`.

All signs are allowed. Repeated singular values are harmless. Degenerate 2x2 edge matrices are covered by Theorem 6.1; the quantitative STAR application is nondegenerate because of (5.5)-(5.6). All input laws remain arbitrary independent scalar laws with density cap one. No moment, smoothness, compact-support, connected-support, Gaussianity, log-concavity or iid assumption is introduced. No nonzero coefficient tail is discarded.
