SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-22T19:07:33Z.
attacking: the surviving O0 one/two-heavy self-block splice — convert the raw projected exterior bank into an honest physical Schur-complement bank, then pay scalar-pivot and definite-pair subbranches.

# fleet02/B19 — two-heavy raw refinement and Schur-projection inheritance

**Run:** `20260922T190733Z-fleet02-B19-qform-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Fresh owner control at final pre-write refresh:** revision `2026-09-22.13`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL SUBBRANCHES PAID / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction discipline

The target is the unrestricted statement: for arbitrary independent real coordinates `X_i` with one-dimensional densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `Q=X^TAX`, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis, compactness, or post-rotation-independence hypothesis is added.

The full theorem remains **OPEN**. I retain the live corrections: no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no arbitrary-joint rank-three coarea cap; no positive conditional spectral-fiber moment; no worst scalar-conditioned rank-three density supremum; no one-good-minor exhaustion; and no inference of a rank-two physical cut merely from high off-diagonal spectral mass.

The revision-13 owner message contains proposed rank-three/scalar-conditioning deductions which are superseded, as mathematical premises, by the source-backed correction inbox. I use the unchanged target, not those refuted interfaces.

## 2. Source-pinned incoming state

The following completed results are used at their exact scopes.

1. **Full third-compound O0 reduction.** fleet03/B07, `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`, canonical `yspennstate/math-open-problems@987b364e280070b1de6eec307557cc00f489e581`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T163733Z-fleet03-B07-qform-r12/REPORT.md`. In O0 there are disjoint original-coordinate banks `L,R` with `B=A[L,R]` satisfying

`E_3(B):=e_3(BB^T)>=1/256`.                                      (2.1)

2. **Prior fleet02/B19 raw heavy-overlap factorization.** Canonical `yspennstate/math-open-problems@06913a3636bf0add597d8dcf16eca5cd2ccd92a2`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T183530Z-fleet02-B19-qform-r15/REPORT.md`. For any physical row set `H`, raw third-volume mass splits by the exact heavy pattern `T=S intersect H`, and for a fixed pattern

`sum_R det(B_(T union R)B_(T union R)^T)
 =det(B_TB_T^T)e_(3-|T|)(B_C P_T^perp B_C^T)`,                 (2.2)

where `C=L\H` and `P_T^perp` is the orthogonal projection in the right-bank coordinate space onto the complement of the row span of `B_T`.

3. **Current named partner fleet03/B19 r17.** Canonical `yspennstate/math-open-problems@9989e8640c2933ba54cd8de88723ac5c223be3b1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T190100Z-fleet03-B19-QFORM-r17/REPORT.md`. It proves that every O0 state with at least three `3/4`-heavy ridge rows is already paid, with continuous density at most `12 sqrt(e)<19.785`. Together with the completed diffuse-ridge branch, every unpaid O0 state can therefore be reduced to a physical heavy set `H` of size at most two.

4. **Determinant-bank half-Riesz theorem.** fleet03/B03 r17, canonical `yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T175531Z-fleet03-B03-QFORM-r17/REPORT.md`. If a residual physical cross block `N` obeys `E_3(N)=e_3(NN^T)>0`, then unconditionally

`H_(1/2)(R):=sup_y E|R-y|^(-1/2)
 <=9.840655864922019 E_3(N)^(-1/12)`.                           (2.3)

If `E_2(N)>0` and the selected-side range leverage is at most `1/2`, then

`H_(1/2)(R)<=7.673759290384858 E_2(N)^(-1/8)`.                 (2.4)

The same report proves the scalar-pivot transducer: for

`Q=a(X_i+h(Z))^2+R(Z)`, `a!=0`,                                (2.5)

with `X_i` an original coordinate independent of `Z` and density at most one,

`||p_Q||_infinity<=|a|^(-1/2) H_(1/2)(R)`.                     (2.6)

These statements retain arbitrary residual self curvature and do not condition on a rotated spectral vector.

## 3. First new theorem: sharpen the raw factor once the named partner removes three-heavy O0

Let `H` be the full `3/4`-heavy row set in an unpaid O0 state. By the current named partner r17, `|H|<=2`. Put `C=L\H`.

### Theorem 3.1 — `QFORM-O0-TWOHEAVY-RAW-FACTOR-v1`

Under (2.1) and `|H|<=2`, there exist `r in {0,1,2}` and `T subset H`, `|T|=r`, such that `B_T` has full row rank when `r>0` and

`det(B_TB_T^T)e_(3-r)(B_C P_T^perp B_C^T)
 >= 1/[768 binom(2,r)].`                                       (3.1)

Consequently at least one of the following holds:

`R0: e_3(B_CB_C^T)>=1/768;`                                    (3.2)

`R1: ||b_i||^2 e_2(B_C P_i^perp B_C^T)>=1/1536` for some `i in H`; (3.3)

`R2: det(B_TB_T^T)||B_C P_T^perp||_F^2>=1/768` for `T=H`, `|T|=2`. (3.4)

#### Proof

Expand the Gram third compound:

`e_3(BB^T)=sum_{S subset L, |S|=3} det(B_SB_S^T)`.              (3.5)

Every term is nonnegative. Because `|H|<=2`, the possible overlap sizes are only `r=0,1,2`; one of these three bins has mass at least `(1/256)/3=1/768`. For that `r`, split again by the exact pattern `T=S intersect H`. There are at most `binom(2,r)` choices. Thus some `T` carries mass at least the right side of (3.1). The Gram Schur-complement identity gives, term by term,

`det(B_(T union R)B_(T union R)^T)
 =det(B_TB_T^T)det(B_RP_T^perp B_R^T)`,                        (3.6)

and summing over `|R|=3-r` gives (3.1). QED.

This is a direct mathematical application of the **current named partner r17**: its target-level elimination of the three-or-more-heavy branch changes the raw pigeonhole from four overlap bins to three and removes `r=3` from the unpaid tree.

## 4. Second new theorem: projected raw banks survive as honest physical Schur banks

The prior r15 report explicitly warned that the orthogonal row residual `B_C P_T^perp` could not simply be renamed a physical Schur-complement cross block. The missing identity is exact once the selected physical self block is invertible.

### Theorem 4.1 — `QFORM-SCHUR-PROJECTION-INHERITANCE-v1`

Let `T subset L` be a physical row set for which both

`B_TB_T^T` and `D:=A[T,T]` are invertible.                      (4.1)

Let `S` be the Schur complement after completing the square in the original coordinates `T`:

`S=A[T^c,T^c]-A[T^c,T]D^(-1)A[T,T^c]`.                        (4.2)

For any `C subset L\T`, the physical `C x R` cross block of `S` is

`N:=S[C,R]=B_C-A[C,T]D^(-1)B_T`.                               (4.3)

Let

`P_T^perp=I-B_T^T(B_TB_T^T)^(-1)B_T`.                          (4.4)

Then

`boxed(N P_T^perp=B_C P_T^perp).`                              (4.5)

Consequently

`NN^T >= B_C P_T^perp B_C^T`                                  (4.6)

in Loewner order, and for every `k>=1`,

`e_k(NN^T)>=e_k(B_C P_T^perp B_C^T)`.                          (4.7)

#### Proof

Since `B_TP_T^perp=0`, multiplying (4.3) on the right by `P_T^perp` gives (4.5) exactly. Since `P_T^perp` and `P_T=I-P_T^perp` are orthogonal projections,

`NN^T=(NP_T^perp)(NP_T^perp)^T+(NP_T)(NP_T)^T
     >=(B_CP_T^perp)(B_CP_T^perp)^T`,                          (4.8)

which is (4.6). Eigenvalues of positive semidefinite matrices are coordinatewise monotone under Loewner order; elementary symmetric functions of nonnegative eigenvalues are increasing in each coordinate, proving (4.7). QED.

### Corollary 4.2 — the r=1 and r=2 raw packets become physical Schur banks

In `R1`, if the heavy scalar pivot `a=A_ii` is nonzero, its scalar Schur complement has a **physical** cross block `N=S[C,R]` with

`||b_i||^2 e_2(NN^T)>=1/1536`.                                 (4.9)

In `R2`, if the physical two-coordinate self block `D=A[T,T]` is invertible, its Schur complement has

`det(B_TB_T^T)||N||_F^2>=1/768`.                               (4.10)

Thus the previous algebraic mismatch between the raw orthogonal residual and a physical Schur residual is completely removed whenever the selected self block is invertible. The remaining difficulty is quantitative payment of the self block and the surviving bank order, not provenance.

## 5. Third new theorem: R0 plus a scalar pivot either pays immediately or forces an aligned E2 obstruction

The `R0` alternative has third-volume mass completely outside the at-most-two heavy rows. A scalar pivot in a heavy row can change the cross block by a rank-one row-direction shear. The exterior-power effect of that shear has an exact two-term decomposition.

Fix `i in H`, put `a=A_ii`, `b=b_i=B[i,R]`, and assume `a!=0`. Let `M=B_C` and let `N=S[C,R]` be the scalar Schur cross block.

If `b=0`, then `N=M`, so by (3.2), `e_3(NN^T)>=1/768`; this is stronger than the paid threshold below. Assume henceforth `b!=0`, set

`u=b/||b||`, `P=I-uu^T`, `G=MPM^T`, `c=Mu`.                   (5.1)

Then

`MM^T=G+cc^T`.                                                 (5.2)

### Lemma 5.1 — rank-one third-exterior split

For every positive semidefinite `G` and vector `c`,

`e_3(G+cc^T)=e_3(G)+c^T T_2(G)c`,                              (5.3)

where the second Newton transform `T_2(G)` is positive semidefinite and obeys

`0<=T_2(G)<=e_2(G)I`.                                         (5.4)

Hence

`e_3(G+cc^T)<=e_3(G)+||c||^2 e_2(G)`.                          (5.5)

#### Proof

Diagonalize `G` with eigenvalues `lambda_j>=0`. The matrix determinant lemma gives

`det(I+t(G+cc^T))
 =det(I+tG)[1+t c^T(I+tG)^(-1)c]`.                             (5.6)

The coefficient of `t^3` is (5.3). In the eigenbasis of `G`, the eigenvalue of `T_2(G)` in direction `j` is `e_2(lambda_1,...,hat lambda_j,... )`, which lies in `[0,e_2(G)]`. This proves (5.4)-(5.5). QED.

### Theorem 5.2 — `QFORM-R0-SCALAR-PIVOT-EXTERIOR-SPLIT-v1`

Under `R0`, for every heavy scalar pivot `i` with `a=A_ii!=0`, either

`GOOD3: e_3(B_C P_i^perp B_C^T)>=1/1536`,                     (5.7)

or

`ALIGNED2: ||B_Cu||^2 e_2(B_C P_i^perp B_C^T)>=1/1536`,       (5.8)

where `u=b_i/||b_i||` when `b_i!=0`. If `b_i=0`, `GOOD3` holds automatically.

In `GOOD3`, the full parent quadratic form already has the target-level bound

`boxed(||p_Q||_infinity
 <=9.840655864922019 * 1536^(1/12) * |a|^(-1/2)
 <18.137 |a|^(-1/2).)`                                        (5.9)

In particular, any fixed lower bound `|a|>=alpha>0` gives a universal constant `18.137 alpha^(-1/2)` on this branch.

#### Proof

By `R0`, `e_3(MM^T)>=1/768`. Apply (5.5) to (5.2). At least one of the two nonnegative terms `e_3(G)` and `||c||^2e_2(G)` is at least `1/1536`, proving (5.7)-(5.8).

In the `GOOD3` branch, Theorem 4.1 for the scalar pivot gives `NP_i^perp=MP_i^perp`, hence

`e_3(NN^T)>=e_3(G)>=1/1536`.                                  (5.10)

The residual quadratic form therefore satisfies the unconditional fleet03/B03 half-Riesz bound (2.3):

`H_(1/2)(R)<=9.840655864922019 * 1536^(1/12)`.                 (5.11)

Apply the scalar-pivot transducer (2.6) to obtain (5.9). QED.

The alternative (5.8) is the exact obstruction that remains: third-volume mass is concentrated through the pivot row direction while retaining an aggregate transverse two-volume. It is stronger and more explicit than the previous phrase “arbitrary self-block / scale splice.”

## 6. Further target-level payments inside R1 and R2

### 6.1 R1 with a moderate cross row and diffuse Schur range

In `R1`, assume `a=A_ii!=0`, `||b_i||^2<=M`, and the selected-side range leverage of the physical Schur cross block `N=S[C,R]` is at most `1/2`. From (4.9),

`e_2(NN^T)>=1/(1536M)`.                                       (6.1)

Using (2.4) and then (2.6),

`boxed(||p_Q||_infinity
 <=7.673759290384858 (1536M)^(1/8)|a|^(-1/2)
 <19.201 M^(1/8)|a|^(-1/2).)`                                 (6.2)

Thus the R1 debt is confined to a near-zero scalar pivot, a very large physical cross row, or a high-leverage Schur bank; those are precisely the geometries for which the existing grouped/heavy-coordinate mechanisms are designed.

### 6.2 Any definite two-coordinate physical self block is paid directly

Suppose a two-coordinate physical set `T={i,j}` has a definite self block `D=A[T,T]`. Condition on every coordinate outside `T`. The conditional form in the two independent cap-one coordinates `x=X_T` is

`x^TDx+2 ell^T x+c`.                                          (6.3)

Complete the square. Translation of `x` does not change the joint density cap one. For positive definite `D`,

`Leb{x: s<=x^TDx<=s+h} <= pi h/sqrt(det D)`                    (6.4)

for every `s` and `h>0`, because the full ellipsoidal sublevel area is `pi s/sqrt(detD)`; intersecting with any translated support can only decrease the shell measure. Reflection gives the negative-definite case. Averaging the conditional interval inequality therefore yields

`boxed(||p_Q||_infinity<=pi/sqrt(|det D|).)`                    (6.5)

This does not use `R2` at all, so in the two-heavy R2 branch the only genuinely unpaid self-pair geometries are **indefinite or singular/near-singular** physical self blocks. The raw R2 packet then additionally supplies the honest Schur-cross Frobenius currency (4.10) whenever the pair is invertible.

## 7. Compact conditional end-to-end assembly after this run

A correction-safe proof tree now reads as follows.

1. **Low offdiagonal:** the completed fleet03/B19 low-offdiagonal theorem pays `s_2(A-diag A)<=499/1000` with density `<84`.
2. **High offdiagonal:** use the completed third-compound O0/O1/O2/O3 overlap reduction; do not infer a good local minor.
3. **O0 diffuse ridge:** already paid by the completed ridge theorem.
4. **O0 with at least three heavy rows:** paid by the **current named partner fleet03/B19 r17**, with continuous density `<19.785`.
5. **O0 with at most two heavy rows:** Theorem 3.1 gives the sharpened scale-free alternatives R0/R1/R2. Theorem 4.1 converts every invertible-self-block projected residual into an honest physical Schur cross bank with no loss.
6. **R0:** any nonzero scalar heavy pivot is either paid by (5.9), or forces the explicit aligned-two-volume obstruction (5.8).
7. **R1:** a nonzero scalar pivot plus moderate row norm and diffuse Schur range is paid by (6.2); only near-zero pivot / huge-row / high-leverage geometry remains.
8. **R2:** any definite physical self pair is paid by (6.5); only indefinite or singular/near-singular pair geometry remains, now carrying the honest one-direction Schur bank (4.10).
9. **O1/O2/O3:** remain separate aggregate overlap obligations and are not silently folded into O0.

The new step removes one source-valid logical gap from the live synthesis: the projected exterior bank from raw heavy-row factorization **does survive physical Schur completion exactly in the orthogonal directions**. The residual problem is no longer provenance; it is quantitative payment of aligned/near-singular self-block geometry.

## 8. First unpaid implication with exact quantifiers

`QFORM-O0-ALIGNED-NEARSINGULAR-SPLICE-v1` (OPEN):

> There exist universal constants `alpha,M,c>0` such that every surviving O0 state with at most two `3/4`-heavy physical rows, after the paid cases above are removed, admits a product-preserving descent to an already-proved grouped/zero-self/ridge/exact-cross-rank branch. Concretely, one must pay either
>
> (i) the aligned scalar-pivot obstruction
> `||B_Cu||^2 e_2(B_C P_u^perp B_C^T)>=1/1536`
> when every available `GOOD3` scalar branch fails, or
>
> (ii) the R2 state with an indefinite or singular/near-singular physical self pair and
> `det(B_TB_T^T)||S[C,R]||_F^2>=1/768`,
>
> without selecting one reciprocal tiny coordinate minor, conditioning on a rotated spectral vector, or replacing the product law by a biased conditional law.

A quantitatively useful sufficient replacement is to show that either the Schur cross range in (i) has leverage at most `1/2` after a bounded-cardinality grouping, or that the high-leverage alternative itself creates the zero-self / grouped hyperbolic packet. For (ii), one needs one additional grouped direction or a dependence-safe one-cross-direction half-Riesz transducer; a bare single cross direction is below the integrability threshold of the current determinant-bank theorem.

This is strictly narrower than the prior generic “one/two-heavy arbitrary-self-block/scale splice.”

## 9. Status

- `QFORM-O0-TWOHEAVY-RAW-FACTOR-v1`: **PROVED**.
- `QFORM-SCHUR-PROJECTION-INHERITANCE-v1`: **PROVED**.
- `QFORM-R0-SCALAR-PIVOT-EXTERIOR-SPLIT-v1`: **PROVED**, with target-level payment (5.9) on `GOOD3`.
- R1 moderate-row/diffuse-Schur subbranch: **PAID** by (6.2).
- Definite physical two-coordinate self block: **PAID** by (6.5).
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full continuity conclusion: **OPEN**; no new continuity claim is made for the half-Riesz branches unless the cited source explicitly supplies it.
- No numerical experiment is used as a proof. A tiny arithmetic verifier records only the displayed numerical constants; the algebraic identities above are proved symbolically.
