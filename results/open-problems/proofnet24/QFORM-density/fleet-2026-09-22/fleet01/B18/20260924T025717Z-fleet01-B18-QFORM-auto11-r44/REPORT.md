# fleet01/B18 r44 — LPP definite active-plane transfer and a retained-rank-two survivor closure

**Run:** `20260924T025717Z-fleet01-B18-QFORM-auto11-r44`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer  
**Partner:** fleet02/B18  
**Status:** `PROVED_SUPPORTING_TARGET_VALID_FAMILY_CLOSURE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope

The owner target remains open: for arbitrary independent real original-coordinate inputs with probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`. Continuity is tracked separately.

This run proves a source-valid two-dimensional active-plane receiver, then uses it on a literal target-valid family inside the latest fleet02/B18 zero-self stable-rank-one / small-fifth-volume survivor. It does **not** delete a small nonzero crossing direction, does not assert independence after rotation, and does not use an arbitrary-joint coarea theorem or a conditional-density-cap-as-independence shortcut.

The elementary definite-shell estimate below was already present in fleet work for a pair of ORIGINAL coordinates (for example fleet03/B12 and fleet02/B12). The contribution here is the exact Livshyts--Paouris--Pivovarov lift from an original pair to an arbitrary two-dimensional orthogonal projection of an entire product source bank, and its application to the partner's retained low-cross-rank survivor. I do not infer literature novelty from the targeted search.

## 2. Primary theorems and hypothesis matching

### 2.1 Livshyts--Paouris--Pivovarov

Source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949, Theorem 1.1.

If

`f(y)=prod_i f_i(y_i)`, `||f_i||_1=1`, `||f_i||_infinity<=1`,

and `E` is a `k`-dimensional subspace, then the orthogonal marginal on `E` has density bounded by `2^(k/2)` (indeed by the sharper minimum in their theorem). For `k=2`,

`||p_(P_E Y)||_infinity <= 2`.                                      (2.1)

This matches the owner source class literally. There is no iid, moment, bounded-support, centering, symmetry, smoothness, or log-concavity hypothesis. I use (2.1) only as a JOINT DENSITY CAP for the projected pair; I never promote it to independence of the two projected coordinates.

### 2.2 Rudelson--Vershynin

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, IMRN 2015, Theorems 1.1--1.2, also applies to independent coordinates with bounded densities. It gives bounded densities for orthogonal projections and the sharp one-dimensional constant `sqrt(2)`. The LPP theorem is the sharper source for the two-dimensional marginal used here.

### 2.3 A quadratic-form regularity theorem that does not match the target

Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, studies iid inputs whose common law is representable as a sufficiently smooth function of a Gaussian field (with additional normalization in its flagship limit theorem). That hypothesis is substantially narrower than arbitrary non-iid cap-one densities, so I do not use it to infer the owner theorem.

## 3. Definite active-plane receiver

### Theorem 3.1 — `QFORM-LPP-DEFINITE-ACTIVE-PLANE-v1`

Let `Y=(Y_1,...,Y_m)` have independent probability densities bounded by one. Let `U` be an `m x 2` matrix with orthonormal columns and put

`Z=U^T Y in R^2`.

Let `R` be any random element independent of the whole source bank `Y`. Let `H=H^T` be a deterministic definite invertible `2 x 2` matrix, and let `a(R) in R^2`, `c(R) in R` be arbitrary measurable functions. Then

`T = Z^T H Z + a(R)^T Z + c(R)`

has an essentially bounded density satisfying

`boxed( ||p_T||_infinity <= 2*pi / sqrt(|det H|) ).`                (3.1)

If `Z` consists of two ORIGINAL coordinates themselves, the constant `2*pi` improves to `pi`.

### Proof

LPP gives a joint density `p_Z` with

`||p_Z||_infinity <= 2`.                                           (3.2)

Fix `R=r`. Completing the square gives, for a deterministic center `z_r`,

`Z^T H Z + a(r)^T Z + c(r)
 = (Z-z_r)^T H (Z-z_r) + c_r`.

Multiplying by `-1` if necessary, assume `H>0`. If `I` is any interval of length `delta`, then the preimage

`{z : (z-z_r)^T H (z-z_r)+c_r in I}`

is an elliptical annulus (or a truncated inner shell at the minimum). Its area is at most

`pi*delta / sqrt(det H)`.                                          (3.3)

Therefore, uniformly in `r`,

`P(T in I | R=r)
 <= ||p_Z||_infinity * pi*delta/sqrt(det H)
 <= 2*pi*delta/sqrt(det H).`                                       (3.4)

Averaging in `R` gives the same interval domination unconditionally. Hence the law is dominated by `(2*pi/sqrt(det H))` times Lebesgue measure and has a density obeying (3.1).

If `Z` is literally a pair of original coordinates, its joint product density is bounded by one, so (3.4) improves by a factor two. QED.

### Important provenance point

The proof conditions only the genuinely independent random element `R`. The two projected coordinates in `Z` may be highly dependent. The sole rotated-source input is the source-valid joint cap (3.2).

## 4. A target-valid punctured rank-one-cross interpolation family

Take mutually independent cap-one scalar sources

`X_1, X_2, Y_1,...,Y_m, W`.

Let `u_1,u_2 in R^m` be orthonormal and define

`Z_1=u_1^T Y`, `Z_2=u_2^T Y`.

For `0<=epsilon<1`, set

`Q_(epsilon,U)
 = Z_1^2 + Z_2^2 + 2 X_1 Z_1 + 2 epsilon X_2 Z_2 + W^2`.          (4.1)

In original coordinates `(X_1,X_2,Y,W)`, the symmetric matrix is

`A_(epsilon,U) =
 [ 0  0      u_1^T        0 ]
 [ 0  0  epsilon u_2^T    0 ]
 [u_1 epsilon u_2  U U^T  0 ]
 [ 0  0        0           1 ]`,                                  (4.2)

where `U=[u_1 u_2]`.

The nonzero spectrum is

`lambda_+(1), lambda_-(1), lambda_+(epsilon), lambda_-(epsilon), 1`,

with

`lambda_+(sigma)=(1+sqrt(1+4 sigma^2))/2`,
`lambda_-(sigma)=(1-sqrt(1+4 sigma^2))/2`.                         (4.3)

For `0<=epsilon<1`,

`lambda_+(1)>1`, `lambda_+(epsilon)>=1`, and the appended eigenvalue is `1`,

while both negative eigenvalues have modulus `<1`. Thus this is a literal owner-target family and

`s_3(A_(epsilon,U))=1`.                                            (4.4)

The second crossing singular value `epsilon` is retained for every `epsilon>0`; no near-zero-as-zero substitution is made.

## 5. Application of the latest fleet02/B18 funnel

The latest designated partner result is fleet02/B18 run `fleet02-B18-20260924T020253Z-r11`, report commit

`54408b41c02166dbb98ac96c14635fd1ba353f27`,

with `QFORM-ZEROSELF-HS-D5-RANK4-FUNNEL-v1`.

For the zero-self split with left bank `(X_1,X_2)` and right bank `(Y,W)`, the family (4.2) has

`s=1`,
`c=||C||_op=1`,
`beta=||B||_op=1`,
`floor(sr(B))=floor(1+epsilon^2)=1` for `0<=epsilon<1`,
`e_5(B^T B)=0`.                                                    (5.1)

Therefore the partner's low-complement (`c<=s/2`), small-cross (`beta<s/2`), stable-rank-at-least-two, and fifth-volume exits do not fire. Its surviving conclusion is exactly the retained low-rank carrier branch

`B=B_4+E`, `rank(B_4)<=4`, `||E||_HS,||E||_op<beta/4`.            (5.2)

Here this is realized with the actual choice

`B_4=B`, `rank(B)=2` for `epsilon>0` (rank one at `epsilon=0`), and `E=0`.  (5.3)

Thus (4.2) is not merely analogous to the partner obstruction; it is a literal member of its unpaid survivor.

For comparison, the same completed partner theorem gives the concrete low-complement inequality

`c<=s/2  ==>  ||p_Q||_infinity <= 2*sqrt(pi)/sqrt(s(s-c))
                         <= 2*sqrt(2*pi)/s`.                       (5.4)

The new transfer below pays a complementary high-curvature active-plane state without using (5.4).

## 6. Closing the literal survivor family

Condition on `(X_1,X_2)`. In (4.1), the entire `Y`-dependence is through the projected pair `Z=U^T Y`, and

`H=I_2`, `a=(2X_1,2 epsilon X_2)`.

Theorem 3.1 gives, uniformly in the conditioning,

`||p_(Z_1^2+Z_2^2+2X_1 Z_1+2epsilon X_2 Z_2)||_infinity <= 2*pi`.

Averaging yields the same bound for the active part. The variable `W` is a disjoint original source, hence `W^2` is independent of the active part; convolution cannot increase the `L^infinity` norm. Therefore

`boxed( ||p_(Q_(epsilon,U))||_infinity <= 2*pi
       = 6.283185307179586... )`                                  (6.1)

uniformly in

- `m`,
- the orthonormal plane `U`,
- every `0<=epsilon<1`, including the punctured `epsilon downarrow 0` collar,
- and every admissible collection of independent cap-one input densities.

This closes a genuinely rotated/delocalized target-valid family in which the crossing block has floored stable rank one and a nonzero arbitrarily small second singular value.

If `u_1,u_2` select two original `Y` coordinates, the product-pair cap is one and (6.1) sharpens to

`||p_Q||_infinity <= pi`.                                         (6.2)

## 7. Continuity for the family, separately from the general theorem

Theorem 3.1 by itself proves essential boundedness only. For the family (4.1), however, continuity follows from the deliberately appended disjoint square.

Because `W` has an absolutely continuous law, `W^2` has an `L^1` density

`g(t)=[f_W(sqrt(t))+f_W(-sqrt(t))]/(2 sqrt(t))`, `t>0`.           (7.1)

The active part in (4.1) has an `L^1 cap L^infinity` density by (6.1) and is independent of `W^2`. Hence

`p_Q = p_active * g`.

The convolution of two `L^1(R)` functions has a continuous representative vanishing at infinity. Therefore every member of (4.1) has a `C_0` density satisfying the same bound (6.1).

This continuity statement is **only for this family**; it is not promoted to the full owner target.

## 8. What remains open

The fleet02/B18 survivor is much broader than (4.2). In the general state

`A=[[0,B],[B^T,C]]`,

one can have a retained rank-`<=4` carrier plus a genuinely nonzero residual `E`, while the complement curvature has active source dimension at least three, may be indefinite, and may overlap the crossing directions. LPP supplies bounded densities of fixed-dimensional projections but does not create independence between their coordinates, and the live correction inbox forbids deleting `E` or replacing a conditional cap by independence.

The precise next structural target suggested by this run is:

`QFORM-RANK4-SURVIVOR-TO-DEFINITE-ACTIVE-PLANE-OR-CROSS-VOLUME-v1`:
route the partner's `B=B_4+E` survivor either to a source-valid definite two-plane carrying determinant currency, or to an already-paid cross-volume/negative-moment branch, while retaining `E` exactly.

No exact published theorem matching all owner quantifiers was found in the primary-theorem check above. That is only a hypothesis comparison, not a novelty claim.

## 9. Corrections explicitly preserved

This proof uses none of the following false interfaces:

- law-uniform pointwise quadratic oscillatory decay;
- arbitrary-joint rank-three coarea;
- conditional projection cap promoted to independence;
- positive conditional-density moment bounds;
- post-rotation independence;
- a universally good fixed physical minor/cross cut;
- deletion of a small nonzero coefficient for arbitrary unbounded inputs.

The full QFORM conjecture remains `OPEN_NOT_PROVED_NOT_DISPROVED`.