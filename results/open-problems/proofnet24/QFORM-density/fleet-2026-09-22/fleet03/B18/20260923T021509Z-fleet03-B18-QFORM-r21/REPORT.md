SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T02:15:09Z.
attacking: a literature-to-proof transfer for an exact-null rank-one source bank coupled to a rank-two product-projection bank, then a dependence-safe Schur-pivot splice using fleet04/B18.

# fleet03/B18 — exact-null rank1+rank2 grouped transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T021509Z-fleet03-B18-QFORM-r21`  
**Status:** `PROVED SUPPORTING TARGET-LEVEL BRANCH / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The target remains the unrestricted statement for arbitrary finite dimension, arbitrary independent original-coordinate inputs with probability densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussianity, smoothness, connected-support, or post-rotation independence assumption is added. Continuity is tracked separately.

Fresh owner control was revision `2026-09-22.15`. The live correction set was consumed before this derivation. In particular, this proof does not use arbitrary-joint rank-three coarea, positive moments of conditional projection-density suprema, conditional-cap-as-independence, a fixed good physical minor/cross cut, or law-uniform pointwise quadratic-phase decay.

The structural input applied below is fleet03/B19 r22, `QFORM-O3-ONE-RANK1-TWO-RANK2-ROUTING-v1`, which isolates a rank-one source bank and a rank-two source bank with an exact grouped determinant currency. The designated fleet04/B18 input applied in Section 5 is `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`.

## 2. Primary literature audit

The external theorem used positively is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949. If a product density has one-dimensional factors bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. There are no moment, support, centering, iid, log-concavity, or smoothness assumptions.

I also checked the current Kwan--Sauermann quadratic Littlewood--Offord theorem (Compositio Math. 161 (2025), published online 2026). Its theorem controls point probabilities for robustly dependent quadratic polynomials, with an arbitrary-distribution extension. It is not an `O(epsilon)` interval small-ball theorem and therefore does not by itself imply an `L^infinity` density bound under the present continuous cap-one hypotheses. I do not use it as a density theorem.

No exact published theorem located in this focused source check matches all quantifiers of the owner's unrestricted target.

## 3. New grouped theorem

Work in an exact-rank-three spectral representation

`A = R M R^T`, `R^T R = I_3`,

with `M=M^T` invertible. Let `H` and `G` be disjoint banks of original coordinates. Denote their spectral row vectors by `r_i in R^3`, and suppose

`S_H := sum_(h in H) r_h r_h^T = lambda v v^T`,

where `lambda>0`, `|v|=1`, while

`S_G := sum_(i in G) r_i r_i^T`

has rank two. Put `P=I-vv^T` and

`d := det( (P S_G P)|_(v^perp) )`.

Assume

`t := v^T M v = 0`, `d>0`.

Define the grouped determinant currency

`D := |det M| lambda d`.

### Theorem `QFORM-NULL-RANK1-PLUS-RANK2-GROUPED-v1`

For arbitrary independent cap-one original-coordinate inputs, after conditioning on all coordinates outside `H union G`, the resulting conditional quadratic polynomial has a continuous density satisfying, uniformly in every outside conditioning value,

`||p||_infinity <= 12 D^(-1/3).`                                      (3.1)

Consequently the full quadratic form has a continuous density with the same bound.

### Proof

Because `S_H` has rank one, write `r_h=c_h v` with `sum_h c_h^2=lambda`, and define

`Z = lambda^(-1/2) sum_(h in H) c_h X_h`.

The coefficient vector of this linear form is normalized. LPP in dimension one gives

`||p_Z||_infinity <= sqrt(2)`.

Set `X_0=sqrt(2) Z`; then `||p_(X_0)||_infinity<=1`.

For the rank-two bank, take a thin factorization of its coefficient map

`L_G = W U^T`, `U^T U=I_2`, `W W^T=S_G`.

Then

`Y=U^T X_G`

is an actual two-dimensional orthogonal marginal of the original product source, so LPP gives the joint cap

`||p_Y||_infinity <= 2`.

The banks are disjoint, hence `X_0` is genuinely independent of the whole vector `Y`; no independence is asserted between the two coordinates of `Y`.

The active three-dimensional spectral map is

`L_0=[ sqrt(lambda/2) v, W ]`.

Its quadratic coefficient matrix in `(X_0,Y)` is

`K_0=L_0^T M L_0`.

The scalar pivot is exactly zero:

`(K_0)_(11)=(lambda/2) v^T M v=0`.

Moreover

`det K_0 = det M * det(L_0)^2`.

Since `S_G` has rank two, determinant expansion in the rank-one direction gives

`det(L_0)^2 = det( (lambda/2)vv^T + S_G ) = (lambda/2)d`.

Thus

`|det K_0| = D/2`.                                                   (3.2)

Conditioning outside `H union G` creates only affine and constant terms in `(X_0,Y)`. The completed affine zero-pivot `1+2` theorem (the affine completion of `QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`) applies to a cap-one scalar independent of a two-dimensional vector with joint density cap `M_2`; it gives

`||p||_infinity <= 6 M_2^(2/3) |det K_0|^(-1/3)`

and continuity. Using `M_2<=2` and (3.2),

`6 * 2^(2/3) * (D/2)^(-1/3)
 =6 * 2^(2/3) * 2^(1/3) D^(-1/3)
 =12 D^(-1/3)`.

This proves (3.1). The bound is uniform in the outside conditioning. Averaging the conditional densities preserves the bound, and dominated convergence against the uniform bound preserves continuity. QED.

## 4. Actual application to the live fleet03/B19 O3 packet

Fleet03/B19 r22 proves, in its one-rank-one/two-rank-two O3 chamber, the exact currencies

`D_j=|det M| lambda d_j`,

and a mixed packet `mu>=1/512`. On a grouped determinant exit,

`D_j>=mu/4`,

hence

`D_j>=1/2048`.

Its existing near-null theorem pays the region `|t|<=d_j/2` by a more general projection-product estimate. In the exact-null subcase `t=0`, Theorem (3.1) instead gives the substantially sharper source-valid estimate

`||p_Q||_infinity <=12 * 2048^(1/3)
                   =96 * 2^(2/3)
                   =152.390500988947... .`                          (4.1)

The density is continuous. This is a genuine target-level subbranch: B19 works in an exact-rank-three target core with `s_min(M)>=1`, retains arbitrary cap-one laws, and obtains the packet by disjoint original-coordinate banks. No single favorable physical triple is selected.

### Explicit target-valid family

Take

`M=[[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `{1,-1,1}`. Let the rank-one bank have frame sum `(1/2)e_1e_1^T`; let a disjoint four-coordinate rank-two bank have frame sum `(1/2)e_2e_2^T+(1/2)e_3e_3^T`; use any disjoint residual bank completing the total frame to `I_3`. For example the rank-two bank may use four mixed transverse rows of equal norm `1/2` at the four `45-degree` directions in the `(e_2,e_3)` plane, so its two projected coordinates need not be independent.

Here `lambda=1/2`, `d=1/4`, `|det M|=1`, hence `D=1/8`. The theorem gives

`||p_Q||_infinity <=24`,                                           (4.2)

continuously, for every admissible product input law. Because the total frame is Parseval, the full physical matrix has nonzero spectrum exactly `{1,-1,1}`.

## 5. Required designated-partner splice: fleet04/B18

Now add a genuine nonzero physical Schur pivot. Write a full form after completing that physical coordinate as

`Q = a V^2 + R`, `a!=0`,

where the shifted pivot variable `V` may depend on the residual variables but retains conditional density cap one, and suppose the Schur residual `R` satisfies Theorem (3.1) with currency `D`. The completed fleet04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` applies precisely in this dependence-safe situation and gives

`||p_Q||_infinity <=2 sqrt( ||p_R||_infinity / |a| )`.

Substituting (3.1),

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(3) |a|^(-1/2) D^(-1/6).`                              (5.1)

This is the required actual inequality using the designated partner result. For example, on the B19 packet scale `D>=1/2048` and a pivot `|a|>=1`,

`||p_Q||_infinity
 <=4 sqrt(3) 2048^(1/6)
 =24.6893095074728... .`                                         (5.2)

The fleet04 square-smoothing theorem establishes essential boundedness; I do not promote continuity through this final wrapper without a separate continuity statement for that theorem.

## 6. Literature non-transfer note

The recent Kwan--Sauermann quadratic Littlewood--Offord theorem is powerful but addresses point concentration under robust dependence. For continuously distributed inputs every single point already has probability zero, while the present target requires the scale-sensitive statement

`sup_t P(Q in [t,t+epsilon]) <= C epsilon`

for every `epsilon>0`. No step in their stated point-probability theorem supplies this linear-in-`epsilon` modulus under only density caps, so it is not an exact prior solution of QFORM.

## 7. Remaining implication

This run closes the **exact-null** portion of the rank-one-bank/rank-two-bank grouped determinant exit, and supplies its dependence-safe scalar-Schur wrapper. It does not pay a merely small but nonzero `t=v^T Mv`; replacing `t` by zero perturbatively is not authorized and would conflict with the live small-curvature corrections. The remaining local task is therefore a genuine interpolation between the exact-null estimate above and the existing nonzero rank-one-bank Schur theorem, or a structural routing of that strip to the completed near-null projection-product branch.

It also does not provide the missing global compiler from `s_3(A)>=1` to one of the already-paid product-preserving packets. Arbitrary extra spectrum remains a separate interaction unless a qualifying Schur residual is produced.

**Full QFORM: OPEN / NOT PROVED.**  
**Continuity:** proved for Theorem (3.1) and the exact-rank-three O3 application; not claimed for the fleet04 square-smoothing wrapper or the unrestricted target.

## 8. Source pins

- LPP: Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), 877--889.
- Affine zero-pivot theorem: `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T222028Z-fleet01-B13-qform-auto11/REPORT.md`.
- Designated partner square smoothing: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.
- Live structural packet: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T020435Z-fleet03-B19-QFORM-r22/REPORT.md`.
- Kwan--Sauermann: DOI `10.1112/S0010437X25102789`.
