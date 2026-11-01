SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T18:51:49Z.
attacking: source-valid validation of the new revision-.12 localized branch and the claimed localized-versus-CLT exhaustion.

# Final control revision 2026-09-22.12 addendum

The owner control advanced from revision 2026-09-22.11 to 2026-09-22.12 after the main r15 report and immutable receipt were written. The new message states that a uniformly nondegenerate original-coordinate 3x3 principal block is a solved localized regime and suggests that failure of such a block leaves only a delocalized/CLT regime. The current shared state still records the arbitrary-joint rank-three coarea lemma as false, so this addendum re-proves the localized statement from source-valid completed theorems and then tests the claimed exhaustion.

Status: the localized principal-triple theorem is PROVED below with an explicit constant. The stronger implication "no uniformly good principal triple => pure CLT/diffuse spectral geometry" is NOT established and is false under the natural leverage interpretation; a known hybrid family is an exact obstruction. Full QFORM remains OPEN.

## 1. Source-valid localized principal-triple theorem

### Theorem QFORM-LOCALIZED-PRINCIPAL-TRIPLE-v1

Let A be any real symmetric matrix and let I be three ORIGINAL coordinate indices. Suppose the physical principal block

B=A[I,I]

is invertible and every eigenvalue of B has magnitude at least c>0. Let the coordinates X_j be independent with densities bounded by one. Then, allowing arbitrary coefficients and couplings outside I,

||p_(X^T A X)||_infinity < 182/c.                              (1.1)

This proves essential boundedness in the localized regime. Continuity is not asserted by this argument.

### Proof

Condition on all original coordinates outside I. The three coordinates X_I remain independent with their original density caps. All outside terms become a deterministic constant plus an arbitrary linear term in X_I. Thus it is enough to prove a bound uniform over affine perturbations of the three-variable quadratic form.

Scale B=c B0. Then s_min(B0)>=1 and

X_I^T B X_I + ell^T X_I
 = c [X_I^T B0 X_I + (ell/c)^T X_I].                           (1.2)

So it is enough to prove the c=1 statement and then divide the density bound by c.

Assume henceforth s_min(B)>=1. Then |det B|>=1 and

||B||_F^2 = sum_{j=1}^3 lambda_j(B)^2 >=3.                    (1.3)

We split into two exhaustive physical-coordinate cases.

#### Case A: a physical diagonal is not small

Suppose |B_ii|>=1/4 for some i. Apply the completed orientation-free exact-rank-three scalar-pivot theorem `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1` from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a 3x3 block the spectral frame V is an orthogonal 3x3 matrix, hence every physical row has leverage c_i=1. The theorem, including arbitrary affine terms/outside couplings, gives

||p_Q||_infinity
 <=128 [|B_ii| |det B|]^(-1/4)
 <=128 (1/4)^(-1/4)
 =128 sqrt2
 <182.                                                         (1.4)

#### Case B: every physical diagonal is small

Assume |B_11|,|B_22|,|B_33|<1/4. From (1.3),

2 sum_{i<j} B_ij^2
 =||B||_F^2-sum_i B_ii^2
 >3-3/16
 =45/16.                                                       (1.5)

Hence some off-diagonal entry b=B_ij satisfies

b^2>=(45/16)/6=15/32.                                        (1.6)

For the corresponding physical pair

E=[[a,b],[b,d]],

we have |a|,|d|<1/4. Therefore

D:=|det E|=b^2-ad >= b^2-|ad| >15/32-1/16=13/32,             (1.7)

and E is indefinite. Comparing E with [[0,b],[b,0]], Weyl's singular-value inequality gives

kappa:=sigma_min(E)
 >=|b|-max(|a|,|d|)
 >sqrt(15/32)-1/4
 =0.4346531968... .                                           (1.8)

Now apply the completed exact-rank-three pair-log theorem from

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its scale parameter is s=1 here, and it allows arbitrary affine terms and arbitrary outside couplings. Thus

||p_Q||_infinity
 <=8 sqrt5 (D kappa)^(-1/4)
 <8 sqrt5 [(13/32)(sqrt(15/32)-1/4)]^(-1/4)
 =27.5956689369...
 <28.                                                          (1.9)

Cases A and B prove the c=1 bound <182. Rescaling (1.2) proves (1.1). QED.

This validates the localized principal-triple branch without using the refuted arbitrary-joint coarea lemma.

## 2. The proposed "only CLT remains" exhaustion is not yet valid

The known exact-rank-three family

A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)               (2.1)

has nonzero spectrum {1,1,-1}. This family is already recorded in the live correction event `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` from fleet02/B03, canonical source

`yspennstate/math-open-problems@24fc7b37c60f77b399936faa7f280296a7ce8c8c:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T131240Z-b03-qform-auto11/REPORT.md`.

It gives a direct test of the new revision-.12 structural slogan.

Every nonsingular 3x3 principal block must choose the singleton coordinate and one coordinate from each m-block. Such a block is exactly

diag(1,1/m,-1/m),                                             (2.2)

so its least singular value is 1/m. Every other 3x3 principal block is singular. Thus there is no dimension-independent localized principal triple.

However the high-spectral projection is

P = [1] direct_sum (J_m/m) direct_sum (J_m/m),                 (2.3)

and P_11=1. Equivalently, one large eigenvector is exactly the physical coordinate e_1; it is maximally localized, not delocalized. Hence

"all physical 3x3 principal blocks are near-singular"

DOES NOT imply

"all three large eigenvectors are spread / the high spectral projection has small coordinate leverage / the three-dimensional spectral vector is a pure CLT regime."  (2.4)

This does not refute QFORM: the same family is uniformly controlled by completed grouped-bank aggregation. It refutes only the proposed exhaustion of the remaining geometry by a pure diffuse/CLT case.

## 3. Corrected structural picture after revision .12

The source-valid decomposition currently has at least three regimes:

1. **Localized principal triple:** now proved by Theorem 1 with explicit bound <182/c.
2. **Truly diffuse spectral window:** the completed ridge-window theorem gives a continuous density <64 when the projection onto |lambda|>=1/64 has maximum coordinate leverage <=1/32, allowing arbitrary smaller nonseparable spectrum.
3. **Hybrid heavy/grouped geometry:** absence of a good 3x3 principal block can coexist with one or more highly localized spectral directions, as (2.1) shows. These cases require bank/group aggregation, nested-heavy, pair-log, weighted-affine-fiber, or a new exhaustive hybrid reduction; a pure CLT statement is insufficient.

Therefore the revision-.12 instruction to focus on the remaining delocalized/local-limit mechanism is useful as a route for regime 2, but it is not yet a proved exhaustive reduction of the full target. Any complete proof still needs a theorem that pays regime 3 uniformly (and remains stable under arbitrary additional spectrum), or a broader local-limit theorem that genuinely includes these hybrid configurations.

Full QFORM remains OPEN. The new localized theorem is source-valid and can be used immediately by the fleet.
