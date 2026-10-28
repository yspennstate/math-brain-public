SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-23T20:07:34Z.
attacking: QFORM-R2-COLLAR-PHYSICAL-PIVOT-DEFECT-AREA-v1 — convert the finite-core near-rank-two collar into exact physical-pivot defect identities, pay any large defect circuit, and localize the unpaid self-curvature to a small bad physical bank.

# account03/B19 r41 — physical-pivot defect-area compiler for the finite-core rank-two collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **NEW SUPPORTING THEOREM + NEW LIVE PAYMENT + SHARPER STRUCTURAL SURVIVOR / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Full-target continuity: **OPEN**. The new defect-area payment proves essential boundedness; no continuity upgrade is claimed for it.

## 1. Source boundary and corrections


The proof below never rotates the original coordinates and then declares them independent. All conditioning is on ORIGINAL coordinates. It uses no moment, support, log-concavity, connected-support, Gaussian, or compactness hypothesis. It does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint 3D coarea, conditional projection-density cap, fiber-supremum argument, or deletion of a small nonzero coefficient as a small random perturbation.

The latest account04/B19 moving-ridge barrier is treated as a correction boundary: an arbitrary joint density cap is not substituted for original-product provenance.

Pinned mathematical inputs actually used:

1. account03/B19 r38, `QFORM-R2-PHYSICAL-TWOROW-TRANSVERSE-COMPILER-v1`:
   `yspennstate/math-open-problems@f09b670173440c4c511985c9a89baf38f97e82c1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T183023Z-account03-B19-QFORM-r38/REPORT.md`.
2. account03/B19 r40, `QFORM-TWOSIDED-SCHUR-2PLUS1-PRODUCTBANK-v1`:
   `yspennstate/math-open-problems@a314c39c5734ecd0845867d597f10f77189b6575`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T192751Z-account03-B19-QFORM-r40/REPORT.md`.
3. designated partner account04/B19 r2, residual-diffuse exact-null-coloop theorem:
   `yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.
4. designated partner account04/B19 r4 moving-ridge joint-cap barrier:
   `yspennstate/math-open-problems@ac55b70485c4108c7073a75365127e00be3bc097`.

## 2. Inherited finite-core collar, now with a maximal physical pair

The r38 finite-core state has disjoint ORIGINAL-coordinate banks `H,L=H^c`, with

`m=|H|<=124`,
`C=A[H,L]`,
`s_1(C)s_2(C)>1/480`,
`s_3(C)<1/64`.                                                     (2.1)

Choose `T={1,2} subset H` to maximize the physical row-pair area

`area(c_i,c_j)=sqrt(det(C[{i,j},L] C[{i,j},L]^T))`,              (2.2)

where `c_i=A[i,L]`. Put

`M=C[T,L]`,
`S=sqrt(det(MM^T))`.                                              (2.3)

Cauchy--Binet, exactly as in r38, gives

`S> S_0:=1/(480 sqrt(7626))
   =2.3856699607287348e-5`.                                       (2.4)

Because r38's transverse payment applies to any such selected physical pair, the still-unpaid collar satisfies, for this maximal pair as well,

`rho:=||C[H\T,L](I-Pi)||_F<1/64`,                               (2.5)

where `Pi` is orthogonal projection in coefficient space onto `row(M)`.

For each `i in H`, define the unique coefficient vector `p_i in R^2` by

`Pi c_i = p_i^T M`,                                               (2.6)

and write the orthogonal residual

`z_i=(I-Pi)c_i`.                                                  (2.7)

Thus `p_1=e_1`, `p_2=e_2`, `z_1=z_2=0`, and

`sum_(i in H\T)||z_i||^2=rho^2<1/4096`.                         (2.8)

The maximality of `T` supplies an important exact coefficient bound. Orthogonal projection cannot increase two-volume, so for every `i,j in H`,

`S |det(p_i,p_j)|
 = area(Pi c_i, Pi c_j)
 <= area(c_i,c_j)
 <= S`.                                                           (2.9)

Hence

`boxed: |det(p_i,p_j)|<=1 for every i,j in H.}`                  (2.10)

In particular, because `p_1=e_1` and `p_2=e_2`,

`|p_{i1}|<=1, |p_{i2}|<=1`.                                      (2.11)

No exact-rank-two assumption is used here; the nonzero transverse tail (2.5) is retained.

## 3. Latent rank-two self completion and the defect circuits

Write

`B=A[H,H]`,
`B_0=A[T,T]`,                                                     (3.1)

and let `P` be the `m x 2` matrix whose `i`th row is `p_i^T`. Define the latent rank-two self completion and its exact physical defect by

`B_lat=P B_0 P^T`,
`E=B-B_lat`.                                                      (3.2)

Because the first two rows of `P` are the standard basis and `B_0=B[T,T]`,

`E[T,T]=0`.                                                       (3.3)

For distinct physical indices `i,j,k in H`, with

`a_i=B_ii !=0`,                                                   (3.4)

define the scalar defect circuit

`F_{i;jk}
 := E_ii det(p_j,p_k)
    -E_{ki} det(p_j,p_i)
    -E_{ji} det(p_i,p_k)`.                                       (3.5)

These are not invented coordinates: every index is a literal original coordinate.

## 4. Main theorem — every large defect circuit is an actual density exit

### Theorem 4.1 — `QFORM-PHYSICAL-PIVOT-DEFECT-AREA-v1`

In the setup of Sections 2-3, for every distinct `i,j,k in H` with `a_i!=0`, if `F_{i;jk}!=0`, the full ambient quadratic law has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= K S^(-1/4) |a_i F_{i;jk}|^(-1/4),`                           (4.1)

where

`K=3*2^(1/3)*sqrt(6)*2^(1/4)
  =11.010263449046631...`.                                       (4.2)

All signs are allowed. The complete transverse cross tail `z_i,z_j,z_k`, arbitrary self curvature on both banks, arbitrary outside affine terms produced by conditioning, and all extra spectrum are retained.

### Proof

Condition on every ORIGINAL coordinate in `H\{i,j,k}`. The remaining pivot `X_i`, physical pair `(X_j,X_k)`, and product receiver bank `X_L` are mutually independent. Their one- and two-dimensional source density caps are one.

Complete the pivot square in `X_i` exactly as in account03/B19 r40. The Schur-corrected physical `2 x |L|` cross matrix is

`D_{i;jk}
 = [c_j;c_k]
   -a_i^(-1)[B_{ji};B_{ki}] c_i`.                                (4.3)

Project its two rows orthogonally onto `row(M)`. By (2.6) the projected coefficient rows are

`u_j=p_j-a_i^(-1)B_{ji}p_i`,
`u_k=p_k-a_i^(-1)B_{ki}p_i`.                                     (4.4)

For any two row vectors, orthogonal projection cannot increase their exterior two-volume. Therefore, writing

`Delta_{i;jk}=s_1(D_{i;jk})s_2(D_{i;jk})`,                       (4.5)

one has

`Delta_{i;jk}
 >= S |det(u_j,u_k)|`.                                            (4.6)

The key identity is

`a_i det(u_j,u_k)=F_{i;jk}`.                                     (4.7)

To verify it, expand the left side:

`a_i det(p_j,p_k)
 -B_{ki}det(p_j,p_i)
 -B_{ji}det(p_i,p_k)`.                                            (4.8)

Substitute `B=P B_0 P^T+E`. The entire latent contribution vanishes by the two-dimensional vector identity

`det(p_j,p_k)p_i
 -det(p_i,p_k)p_j
 -det(p_j,p_i)p_k=0`,                                             (4.9)

followed by taking the scalar product with `B_0 p_i`. The remainder is exactly (3.5), proving (4.7).

Combining (4.6)-(4.7),

`Delta_{i;jk}
 >= S |F_{i;jk}|/|a_i|`.                                         (4.10)

Now apply the completed r40 theorem `QFORM-TWOSIDED-SCHUR-2PLUS1-PRODUCTBANK-v1` to the actual conditioned pivot/pair/receiver equation. With `M_X=M_U=1`, that theorem gives

`||p_Q||_infinity
 <= [3*2^(1/3)*sqrt(6)] 2^(1/4)
    |a_i|^(-1/2) Delta_{i;jk}^(-1/4)`.                            (4.11)

Insert (4.10):

`|a_i|^(-1/2) Delta^(-1/4)
 <= S^(-1/4)|a_i F_{i;jk}|^(-1/4)`,                              (4.12)

which is (4.1). The bound is uniform in the conditioned values, so averaging recovers the full law. QED.

**Regularity.** The invoked r40 theorem proves essential boundedness. This argument does not claim a continuous representative.

## 5. Live quantitative payment

Fix the universal circuit threshold

`gamma=2^(-25)=2.9802322387695312e-8`.                            (5.1)

If there exist distinct physical `i,j,k in H` with

`|a_i F_{i;jk}|>=gamma`,                                         (5.2)

then (2.4) and Theorem 4.1 give

`||p_Q||_infinity
 <K S_0^(-1/4) gamma^(-1/4)
 =11990.370228314221...`.                                         (5.3)

Thus

`boxed: ||p_Q||_infinity<11991}`                                  (5.4)

on this entire branch, with no sign restriction and with the nonzero `rho<1/64` tail still present.

Consequently every unpaid collar state obeys the simultaneous family

`boxed:
 |a_i F_{i;jk}|<2^(-25)
 for every distinct i,j,k in H with a_i!=0.}`                     (5.5)

This is substantially stronger than r40's single-pivot scalar cancellation: it constrains every physical scalar pivot against every physical pair.

## 6. New structural compiler — all substantial cross-visible columns become latent

Set

`a_0=delta_0=1/64`.                                               (6.1)

There are now three honest branches.

1. The density exit (5.4) occurs.
2. At least one coordinate of the maximizing base pair has small diagonal,
   `min(|A_11|,|A_22|)<a_0`; this is the separate base-small-pivot chamber and is not silently discarded.
3. Otherwise both base diagonals have magnitude at least `a_0`, and the following localization holds.

Assume branch 3 and failure of (5.2). Define the cross-visible substantial-diagonal set

`G={i in H\T:
      |A_ii|>=a_0 and
      max(|p_{i1}|,|p_{i2}|)>=delta_0}`,                           (6.2)

and the bad physical bank

`B_bad=(H\T)\G`.                                                  (6.3)

Every index in `B_bad` satisfies at least one explicit physical defect condition:

`|A_ii|<1/64`

or

`max(|p_{i1}|,|p_{i2}|)<1/64`.                                   (6.4)

Put

`e_0=gamma/a_0=2^(-19)`,                                         (6.5)

and

`eta=5 e_0/delta_0=5/8192=0.0006103515625`.                      (6.6)

### 6.1 Base-to-all defect columns are tiny

Take any `i in H\T`. Using pivot `1` with pair `(2,i)` in (3.5), and `E[T,T]=0`,

`F_{1;2i}=E_{i1}`.                                                (6.7)

Likewise

`F_{2;1i}=-E_{i2}`.                                               (6.8)

Since `|A_11|,|A_22|>=a_0`, failure of the gate (5.2) gives

`|E_{i1}|<e_0`,
`|E_{i2}|<e_0`                                                     (6.9)

for every physical `i`, including bad rows.

### 6.2 Active diagonals are tiny defects

For `i in G`, use pivot `i` and pair `(1,2)`. Since `det(p_1,p_2)=1`, (3.5) becomes

`F_{i;12}
 =E_ii-p_{i1}E_{1i}-p_{i2}E_{2i}`.                               (6.10)

Because `|A_ii|>=a_0`, failure of (5.2), together with (2.11) and (6.9), yields

`|F_{i;12}|<e_0`,
`|E_ii|<3e_0`.                                                     (6.11)

### 6.3 Every active defect column is uniformly tiny

Fix `i in G` and arbitrary `l in H\{i}`. If `|p_{i2}|>=delta_0`, use pivot `i` and pair `(1,l)`:

`F_{i;1l}
 =p_{l2}E_ii
  -p_{i2}E_{li}
  -det(p_i,p_l)E_{1i}`.                                          (6.12)

By (2.10)-(2.11), (6.9), (6.11), and `|F_{i;1l}|<e_0`,

`|p_{i2}E_{li}|<5e_0`,                                           (6.13)

hence

`|E_{li}|<eta`.                                                    (6.14)

If instead `|p_{i1}|>=delta_0`, the identical argument with pair `(2,l)` gives the same conclusion. The basis-row cases are already covered by the stronger estimate (6.9).

Thus

`boxed:
 |E_{li}|<eta
 for every i in G and every l in H.}`                             (6.15)

### 6.4 Operator localization to the bad bank

Let `E_bad` be the symmetric matrix equal to `E` on `B_bad x B_bad` and zero elsewhere. Then `R_E:=E-E_bad` has no bad-bad entries; every row in `G` has all non-base entries bounded by `eta` and its two base entries bounded by `e_0`; every bad row has only its `G` and base entries left; every base row has all non-base entries bounded by `e_0`.

Since `m<=124`, the maximum absolute row sum is at most

`122 eta+2 e_0
 =0.07446670532226562...`.                                        (6.16)

Because `R_E` is symmetric,

`boxed:
 ||E-E_bad||_op<0.074467<0.075.}`                                 (6.17)

This is a deterministic matrix statement, not a probabilistic perturbation claim.

## 7. Full coefficient structure after the compiler

Let

`Z=C-PM`,                                                         (7.1)

where the first two rows of `Z` are zero. By the live collar,

`||Z||_op<=||Z||_F=rho<1/64`.                                    (7.2)

Define the structured symmetric matrix, in the `H|L` ordering,

`A_* = [[P B_0 P^T+E_bad,  P M],
        [M^T P^T,          A[L,L]]].`                             (7.3)

Then

`A-A_*
 = [[E-E_bad, Z],
    [Z^T,       0]].`                                             (7.4)

The off-diagonal symmetric block has operator norm `||Z||_op`, hence (6.17), (7.2) give

`boxed:
 ||A-A_*||_op
 <0.074466706+1/64
 =0.09009170532226562...<0.091.}`                                 (7.5)

Therefore the original spectral resource survives in the structured carrier:

`s_3(A_*)
 >=s_3(A)-||A-A_*||_op
 >0.909`.                                                         (7.6)

This use of the coefficient approximation is legitimate Weyl/singular-value bookkeeping only. **No step treats `X^T(A-A_*)X` as a small random perturbation**; that would be invalid without moment/support assumptions.

The structural content of `A_*` is sharp: outside the bad physical bank, every `H`-side interaction factors through the two latent coefficient columns `P`. More precisely, if `u in R^H` obeys

`P^T u=0`

and

`u|_(B_bad)=0`,                                                    (7.7)

then

`A_* (u,0_L)=0`.                                                  (7.8)

Thus all still-unexplained `H`-side curvature is carried by only two latent directions plus the explicit bad physical bank (6.4). This is the new survivor passed to the next mechanism.

## 8. Designated partner account04/B19 applied to an actual inequality

The completed account04/B19 r2 theorem states, in its exact residual-diffuse exact-rank-three null-coloop normal form with `0<D_res<=1` and `|det M|>=1`,

`||p_Q||_infinity<34 sqrt(log(e/D_res))`,                          (8.1)

with a continuous density.

On the concrete source-valid interval

`2^(-12)<=D_res<=1`,                                              (8.2)

this gives the actual inequality

`||p_Q||_infinity
 <34 sqrt(log(4096 e))
 =103.7850552282339...<104.`                                      (8.3)

I do not infer that the new bad bank (6.4) automatically satisfies the partner's residual-diffuse exact-null-coloop hypotheses. Equation (8.3) is used only on the true intersection with that completed scope.

The partner's newer r4 result is also consumed as a negative interface: there exist unit-joint-density dependent triples for which a moving-ridge quadratic has arbitrarily large output density, so the bad bank cannot be replaced by an arbitrary joint density with the same cap. Original-product provenance must remain visible in the successor argument.

## 9. Compact updated proof assembly and first missing implication

The finite-core rank-two branch now has the following correction-safe chain.

1. r38 pays `rho>=1/64` continuously by `<743` and leaves the Frobenius collar (2.5).
2. r40 pays any noncancelled scalar Schur pivot in that collar and also pays large exact cross-null curvature at `rho=0`.
3. **This run pays every large physical defect circuit anywhere in the collar by `<11991`, without setting `rho=0`.**
4. If both maximizing-pair diagonals are substantial and all defect circuits fail the payment, then the entire coefficient matrix is within operator distance `<0.091` of the explicit latent-two-plus-bad-bank matrix `A_*`, while `s_3(A_*)>0.909`.
5. The only uncontrolled `H`-side self block in `A_*` is supported on physical rows satisfying `|A_ii|<1/64` or projected cross coefficient `<1/64`.

The unrestricted theorem is still **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity is still **OPEN**.

The first essential missing implication is now the sharper

`QFORM-LATENT2-PLUS-SMALLPIVOT-OR-CROSSNEARNULL-BADBANK-v1`:

> Pay the structured carrier (7.3)-(7.8), or route it quantitatively to an already-paid grouped/rank-one/two-source/null-coloop branch, using the original-product laws on the bad physical bank. The branch where one maximizing base diagonal has magnitude `<1/64` is part of this same debt. No arbitrary-joint reduction or coefficient-to-random perturbation is allowed.

This replaces the previous generic simultaneous-Schur-cancellation description by an explicit operator-stable coefficient normal form with all uncontrolled self curvature physically localized.

## 10. Verification

`CHECK.py` and `CHECK_OUTPUT.txt` in this immutable run directory verify the constants and 4000 random noncommuting instances of the exact algebraic identity and projected-area lower bound. The largest algebra residual observed was `4.930917e-13`; no area inequality violation occurred. The numerical check is a regression check only; the proof is the exact derivation above.

Privacy/write review: changed files contain only pure mathematical statements, public repository commit identifiers, and nonsecret run metadata. No credentials, personal archives, financial/company/client material, notification settings, or external account data are present. No installation, paid call, public release, scheduler mutation, email, or notification change was made.
