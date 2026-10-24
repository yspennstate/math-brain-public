# account01/B16 — fixed-pair determinant bank ledger for projection-product interaction

**Run:** `20260922T154258Z-account01-B16-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction-aware first implication

The full target remains open: for every dimension, every independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal dimension-, law-, and matrix-independent constant. Continuity is a separate desired conclusion and is not proved here.

Fresh control before publication was `yspennstate/math-research-brain@1f2dc7684a305ea574bb81d6f0d991cc0dbf085c`, owner revision `2026-09-22.5`; the live correction inbox at that commit has blob `2ee621225465e603dfd118f6bd86b1ddc853f40e`. In particular this report respects the corrections that generic bounded projection density does not control an indefinite quadratic trace, a single uniformly good physical minor need not exist, conditional density caps do not substitute for original-coordinate independence, and linear averaging of reciprocal local-minor costs can diverge.

The completed assigned-partner result actually applied is account02/B16 run `20260922T142906Z-account02-B16-QFORM-auto12`, canonical report

`yspennstate/math-open-problems@f1de723dfb00adf76b4a6e73f2336c47676cb6bc`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T142906Z-account02-B16-QFORM-auto12/REPORT.md`,

blob `65bb96d1245da44d1cf0c6787ecfe28dc737d6d2`.

Its theorem `QFORM-ZERODIAG-TRIPLE-PRODUCT-TRACE-v1` states that for a physical zero-diagonal invertible triple

`B=[[0,a,b],[a,0,c],[b,c,0]]`

and arbitrary outside couplings,

`||p_Q||_infinity <= C_off |det B|^(-1/3)`,                         (1.1)

where

`C_off=2^(4/3)[log 3+2 log(3/2)]=4.8117455951457755...`.           (1.2)

The proof keeps the original three-coordinate product source and pays the logarithmic product ridge before the final quadratic trace.

The other exact input is the sharp two-dimensional product-projection theorem transferred by account02/B18 from Livshyts--Paouris--Pivovarov: every two-dimensional orthogonal projection of a product law with one-dimensional density caps one has joint density at most two. In particular every normalized physical-coordinate linear bank has density at most two by adjoining an independent unit-density dummy coordinate.

**First implication attacked here:** identify an aggregate invariant which simultaneously (i) controls the actual physical projection bank and (ii) records the determinant mass of all physical triples through a fixed pair, without selecting one minor and without linearly averaging reciprocal minor costs.

## 2. Fixed-pair Cauchy--Binet identity

Work first with an exact-rank-three symmetric form

`A=R Lambda R^T`,                                                   (2.1)

where `R` is an `n x 3` real matrix with orthonormal columns,

`R^T R=I_3`,                                                        (2.2)

and `Lambda` is an invertible real symmetric `3 x 3` matrix. Let `r_k in R^3` denote the `k`-th row of `R`.

Fix two distinct physical indices `i,j`. Put

`G_ij = |r_i|^2 |r_j|^2 - <r_i,r_j>^2
      = |r_i x r_j|^2`.                                            (2.3)

For every `k` different from `i,j`, let `I_k={i,j,k}`. Then

`A_{I_k,I_k}=R_{I_k} Lambda R_{I_k}^T`,                            (2.4)

and therefore

`det A_{I_k,I_k}=det Lambda * det(R_{I_k})^2`.                     (2.5)

In particular all nonzero determinants on the right have the same sign, namely `sign(det Lambda)`.

### Theorem 2.1 — `QFORM-FIXED-PAIR-THIRD-MINOR-MASS-v1`

For every fixed pair `i,j`,

`boxed( sum_{k != i,j} |det A_{I_k,I_k}|
       = |det Lambda| G_ij. )`                                     (2.6)

### Proof

Let

`u=r_i x r_j`.

Since

`det(r_i,r_j,r_k)=u dot r_k`,                                      (2.7)

orthonormality of the columns of `R` gives

`sum_k det(r_i,r_j,r_k)^2
 =sum_k (u dot r_k)^2
 =u^T (sum_k r_k r_k^T)u
 =u^T(R^TR)u
 =|u|^2
 =G_ij`.                                                          (2.8)

The terms `k=i,j` vanish. Combining (2.5) with (2.8) proves (2.6). QED.

This is a fixed-pair refinement of global third-minor Cauchy--Binet. It is exactly adapted to a nested physical-pivot argument: once two physical coordinates have been selected, *all remaining determinant mass through that pair is already a probability-like bank.*

## 3. Gram--Schmidt form: the determinant weights are the projection-bank weights

Assume `G_ij>0`. Apply one deterministic orthogonal change only inside the three-dimensional spectral coefficient space; this does not rotate the physical inputs. Choose coordinates in `R^3` so that

`r_i=(sqrt(ell),0,0)`,                                              (3.1)

and

`r_j=(alpha,sqrt(h),0)`,                                           (3.2)

where

`ell=|r_i|^2`,

`h=G_ij/ell>0`.                                                     (3.3)

For every `k != i,j`, write

`r_k=(alpha_k,t_k,l_k)`.                                           (3.4)

Then direct expansion gives

`det(r_i,r_j,r_k)=sqrt(ell h) l_k`.                               (3.5)

Applying (2.8), or simply using the third-column normalization in (2.2), gives

`boxed( sum_{k != i,j} l_k^2=1. )`                                (3.6)

Thus the actual normalized one-dimensional physical-coordinate bank

`L=sum_{k != i,j} l_k X_k`                                        (3.7)

has coefficient vector of Euclidean norm one.

By the source-valid sharp product-projection theorem, adjoining an independent `U~Unif[0,1]` and projecting onto the orthonormal pair `(L,U)` yields joint density at most two. Since that joint density is

`p_L(s) 1_[0,1](u)`,                                               (3.8)

we obtain

`boxed( ||p_L||_infinity <=2. )`                                  (3.9)

No independence among spectral coordinates is asserted. Equation (3.9) is an aggregate statement about the original product law.

Meanwhile (2.5) and (3.5) give the exact atomwise determinant identity

`boxed( |det A_{I_k,I_k}|
       = |det Lambda| ell h l_k^2. )`                              (3.10)

Define

`P_ij:=|det Lambda| ell h=|det Lambda|G_ij`,

`w_k:=l_k^2`.                                                       (3.11)

Then

`w_k>=0`, `sum_k w_k=1`,                                          (3.12)

and

`boxed( |det A_{I_k,I_k}|=P_ij w_k. )`                            (3.13)

This is the projection--product bridge: the same weights that build the dimension-free capped aggregate bank `L` are *exactly* the normalized third-principal-minor masses through the pair `(i,j)`.

## 4. Exact application of the account02/B16 partner theorem

Suppose `k` is such that `w_k>0` and the physical principal triple on `I_k={i,j,k}` has zero diagonal:

`A_ii=A_jj=A_kk=0`.                                                (4.1)

Because (3.13) is then nonzero, the triple is invertible, and the completed account02/B16 theorem (1.1) applies after conditioning on all outside physical coordinates. Therefore

`||p_Q||_infinity
 <= C_off (P_ij w_k)^(-1/3)`.                                     (4.2)

This is an actual target-level density inequality for that structural branch, not merely a determinant identity.

### Corollary 4.1 — heavy transverse atom branch

If, in addition,

`w_k=l_k^2 >= tau>0`,                                              (4.3)

then

`boxed( ||p_Q||_infinity
       <= C_off tau^(-1/3) P_ij^(-1/3). )`                        (4.4)

Thus a zero-diagonal triple carrying a fixed fraction of the transverse projection bank is fully paid with the determinant-homogeneous exponent `-1/3`, with arbitrary outside couplings and arbitrary cap-one input laws.

This branch is particularly relevant to the outer/light-cone configurations where scalar-square pivots vanish: the partner's product-log-ridge theorem supplies the nonlinear payment precisely where a Schur scalar pivot is unavailable.

## 5. Cubic harmonic ledger for diffuse zero-diagonal triples

A single heavy atom need not exist; the bank may be diffuse. The correction `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` warns that selecting one small triple and paying its reciprocal constant is not a dimension-free strategy. The identities above show the exact nonlinear quantity in which all local partner bounds aggregate without loss.

Let `Z` be the set of indices `k` for which the triple `I_k` satisfies the zero-diagonal hypothesis (4.1) and `w_k>0`. Define its partner-theorem local bound

`M_k:=C_off(P_ij w_k)^(-1/3)`.                                    (5.1)

Then exactly

`M_k^(-3)=C_off^(-3)P_ij w_k`,                                    (5.2)

so

`boxed( sum_{k in Z} M_k^(-3)
       = C_off^(-3) P_ij sum_{k in Z} w_k. )`                      (5.3)

In the fully zero-diagonal-through-the-pair situation `Z={k:w_k>0}`,

`boxed( sum_k M_k^(-3)=C_off^(-3) P_ij. )`                        (5.4)

Thus the correct local determinant ledger is **cubic harmonic**, not linear reciprocal. The same probability weights `w_k` are simultaneously visible to the bounded-density bank (3.7)--(3.9).

Equation (5.4) does **not** by itself imply a bound on the density of the full quadratic form: there is no proved theorem allowing one to combine conditional `L^infinity` bounds by the cubic harmonic sum. Claiming such an aggregation would repeat the known local-minor error in a different notation. What (5.4) does prove is that the dimension loss in linear reciprocal averaging is not intrinsic to the determinant geometry; it is an artifact of applying the nonlinear trace estimate *before* aggregation.

## 6. A useful stress family: the bank identity is dimension-free when every local minor is tiny

Consider the standard delocalized exact-rank-three frame underlying block families such as normalized rank-one banks. In the Gram--Schmidt coordinates above suppose the transverse weights are essentially flat,

`w_k approximately 1/m`                                           (6.1)

across `m` coordinates. Then every individual determinant in (3.13) is only of order

`P_ij/m`,                                                         (6.2)

and the local partner cost is of order

`M_k approximately C_off P_ij^(-1/3)m^(1/3)`,                    (6.3)

which diverges if one insists on choosing one triple. But the exact bank has

`||p_L||_infinity<=2`                                              (6.4)

independently of `m`, and the cubic ledger remains

`sum_k M_k^(-3)=C_off^(-3)P_ij`.                                  (6.5)

So the fixed-pair identity reproduces, at the correct exponent, the qualitative lesson of the live diffuse counterexamples: aggregate first, pay curvature second.

## 7. Relation to the preceding B16 light-cone work

The preceding account01/B16 report treated an exact-rank-three nested-heavy Schur branch. After a nonzero outer physical pivot it wrote the residual two-frame in a basis with a heavy row and introduced a normalized transverse bank `L`. The difficult transition was the punctured residual light cone, where a Rayleigh coefficient tends to zero and reciprocal scalar-square estimates become singular.

The present theorem changes mechanism rather than repeating that interpolation attempt. It identifies the invariant carried by that same transverse bank before any reciprocal payment:

`P_ij=|det Lambda|G_ij`,                                           (7.1)

with atomwise masses `P_ij w_k` and dimension-free projection cap (3.9). In particular, whenever the light-cone configuration produces an actual zero-diagonal physical triple with a transverse atom of nonnegligible weight, Corollary 4.1 pays it directly by the completed partner theorem, with no `1/|beta|` singularity.

The diffuse case is not yet closed, but (5.4) identifies the exact aggregation scale that a successful nonlinear projection-product estimate would have to exploit.

## 8. First remaining implication

The first unpaid projection-product implication after this run is:

> **QFORM-CUBIC-BANK-AGGREGATION-v1.** Starting from a normalized original-coordinate bank `L=sum l_kX_k` with `||p_L||_infinity<=2`, and local curved-trace controls whose determinant costs satisfy `|det A_{ijk}|=P_ij l_k^2`, prove a joint nonlinear integration inequality that pays the diffuse bank at total scale `P_ij^(-1/3)` (or another universal target-valid scale) *before* taking reciprocal local-minor constants. The proof must retain original product provenance and allow arbitrary outside couplings. Alternatively, construct a valid product-law obstruction to this cubic aggregation principle.

A successful result of this type would address exactly the gap left by families where every physical triple is tiny but the spectral three-volume is order one. It must not be replaced by a generic bounded projected-density level-set bound, which is already refuted for indefinite traces.

Separately, even a complete exact-rank-three aggregation theorem would still need a stable passage to arbitrary additional spectral components; they are correlated with the selected spectral projection and cannot simply be convolved away as independent noise.

## 9. Status

**Proved in this report:**

1. `QFORM-FIXED-PAIR-THIRD-MINOR-MASS-v1`, equation (2.6).
2. Exact identification of normalized projection-bank weights with fixed-pair third-minor weights, equations (3.9)--(3.13).
3. A target-level heavy-transverse-atom zero-diagonal branch, equation (4.4), by substantive application of the completed account02/B16 theorem.
4. The exact cubic harmonic local-cost ledger, equations (5.3)--(5.4).

**Not proved:** the nonlinear diffuse-bank aggregation inequality, arbitrary exact-rank-three closure, the full theorem with additional spectrum, or continuity of the output density.

**Full QFORM conjecture: OPEN / NOT PROVED.**
