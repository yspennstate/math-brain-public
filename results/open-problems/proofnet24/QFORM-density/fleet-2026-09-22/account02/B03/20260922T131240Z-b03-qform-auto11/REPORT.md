# account02/B03 — coloop-bank obstruction and prepayment by independent aggregation

**Run:** `20260922T131240Z-b03-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Decoupled time integral`  
**Classification:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/transport only.

## 1. Target and corrections

The target is unchanged: for arbitrary independent real coordinates with probability densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one dimension- and law-independent essential density bound for `X^T A X`, or give a genuine target counterexample.

This run respects the current corrections: no law-uniform pointwise Fresnel decay, no post-rotation independence, no naive fiber-supremum reduction, no universal `pi` constant, no use of conditional sum/difference density caps as if they preserved independence, and no absolute-value Holder route that discards displacement cancellation.

The named partner result actually applied is the latest completed `account03/B03` theorem:

- `yspennstate/math-open-problems@d62131527f6bcb996c27a9fbf04fc1059797a9aa`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T125813Z-account03-B03-QFORM-r12/REPORT.md`.

For an exact-rank-three frame `A=U Lambda U^T`, it defines Pluecker weights `w_I=det(U_I)^2`, the disjoint mass `R(U)=sum_{I cap J=empty}w_Iw_J`, proves

`E_S[det(U_S^T U_S) det(U_T^T U_T)] = R(U)/64`,

and converts a positive random-cut resource into an original-coordinate rank-three cross block and a bounded-density theorem. Its preceding all-copy hierarchy also gives the exact equivalence between a density bound `B` and `J_k(eps)<=B^(k-1)` at every collision order.

A second source-pinned theorem used below is `account02/B15`:

- `yspennstate/math-open-problems@60e7f51716e67553ce759519f9801ff3674dcce9`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T120155Z-account02-B15-qform-r1/REPORT.md`.

For independent density-one variables and any invertible symmetric physical `3 x 3` block `B`, including arbitrary affine terms from outside conditioning,

`||p||_infinity <= C_3/sigma_min(B)`, `C_3=2*pi+3*sqrt(3)`.

For the aggregation estimate I also use Beckner's sharp Young convolution inequality, source William Beckner, *Inequalities in Fourier analysis*, Ann. of Math. 102 (1975), 159–182, DOI `10.2307/1970980`. Its sharp Euclidean convolution constant is the only external analytic input in Section 5.

## 2. A new exact target family

For an integer `m>=2`, let `n=2m+1`. In a three-dimensional spectral space with orthonormal basis `(e_1,e_2,e_3)`, define an `n x 3` frame `U_m` by the rows

`u_0=e_1`,

`u_j=e_2/sqrt(m)` for `1<=j<=m`,

`u_{m+j}=e_3/sqrt(m)` for `1<=j<=m`.

Then

`U_m^T U_m=I_3`.

Take

`Lambda=diag(1,1,-1)`

and

`A_m=U_m Lambda U_m^T`.

In the original coordinate order,

`boxed( A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m). )`       (2.1)

Its nonzero eigenvalues are exactly `1,1,-1`. Hence every `A_m` is a genuine matrix in the full owner target; the ambient dimension grows while the three large eigenvalues stay fixed.

The geometry is a **spectral coloop plus two diffuse banks**: every spectral basis of the row frame must use the single hub row `u_0`.

## 3. Exact failure of the partner random-cut resource

The row leverages are

`ell_0=1`,

`ell_i=1/m` for the other `2m` rows.

A three-row minor of `U_m` is nonzero iff it is exactly

`I={0,j,m+k}`

with `1<=j,k<=m`. Every such determinant has magnitude `1/m`, so

`w_I=1/m^2`.

There are `m^2` such bases and their weights sum to one, as Cauchy--Binet requires.

But every two nonzero Pluecker bases share the hub `0`. Therefore

`boxed( R(U_m)=0. )`                                                (3.1)

Applying the named partner's **exact** random-cut identity gives

`boxed( E_S[det G_S det G_T]=0. )`                                  (3.2)

This is not a loose estimate: for every original-coordinate partition `(S,T)`, one side misses the unique hub, so

`boxed( rank A_m[S,T] <= 2. )`                                      (3.3)

Thus no rank-three cross block exists at all. The latest partner theorem is correctly silent on this family; the obstruction is an exact endpoint of its disjoint-Pluecker resource.

Also

`1-sum_i ell_i^2 = 1-(1+2/m)=-2/m`,

so its elementary lower surrogate is nonpositive, consistently with (3.1).

## 4. Counterexample to the proposed local/cross uniform dichotomy

The current fixed-matrix theorem suggested the following possible universal bridge: either one has a uniformly nonsingular physical principal `3`/`4` block, or an original-coordinate cut has a uniformly nondegenerate rank-three cross block.

The family (2.1) refutes that proposed bridge.

Every nonsingular principal `3 x 3` submatrix must contain the hub, one coordinate from the positive diffuse bank, and one from the negative diffuse bank. It is exactly

`diag(1,1/m,-1/m)`

up to permutation. Therefore

`boxed( sigma_min(A_m[I,I])=1/m,  |det A_m[I,I]|=1/m^2. )`          (4.1)

Every `4 x 4` principal block is singular because `rank(A_m)=3`. By (3.3), every cross block has rank at most two. Hence simultaneously

`max_{nonsingular principal |I|=3,4} sigma_min(A_m[I,I])=1/m ->0`,

while

`max_{cuts S|T} rank A_m[S,T] <=2`.                                (4.2)

So no positive dimension-free constant `c` can make the proposed `principal >=c OR rank-three-cross >=c` dichotomy true under the three-large-eigenvalue hypothesis.

This is a **source-valid counterexample to a proof architecture**, not a counterexample to QFORM itself.

## 5. The same family is uniformly easy after aggregating independent banks first

Let the original inputs be independent with arbitrary densities at most one. Define the normalized bank sums

`P_m = m^(-1/2) sum_{j=1}^m X_j`,

`R_m = m^(-1/2) sum_{j=1}^m X_{m+j}`.

The three variables `X_0,P_m,R_m` are independent, and (2.1) becomes exactly

`boxed( Q_m = X_0^2 + P_m^2 - R_m^2. )`                            (5.1)

The key point is to **aggregate before paying a reciprocal coordinate minor**.

### Lemma 5.1 — universal density cap for a normalized bank

If `X_1,...,X_m` are independent and each density is bounded by one, then

`S_m=m^(-1/2)sum_j X_j`

has density satisfying

`boxed( ||p_{S_m}||_infinity <= c_m := (m/(m-1))^((m-1)/2) <= sqrt(e). )`  (5.2)

**Proof.** Put `p=m/(m-1)` and `p'=m`. Since every input density has `L^1=1` and `L^infinity<=1`, interpolation gives `||f_j||_p<=1`. Beckner's sharp `m`-fold Young inequality to `L^infinity` has constant

`C_p^m`, where `C_p=p^(1/(2p))/(p')^(1/(2p'))`.

Thus

`||f_1*...*f_m||_infinity <= C_p^m`

with

`C_p^m = (m/(m-1))^((m-1)/2) / sqrt(m)`.

Scaling the sum by `m^(-1/2)` multiplies its density norm by `sqrt(m)`, proving (5.2). Finally `(1+1/(m-1))^(m-1)<=e`. QED.

### Proposition 5.2 — explicit uniform density bound for the adversary

If a real random variable `Z` has density cap `L`, then for `y>0`

`p_{Z^2}(y)=[f_Z(sqrt(y))+f_Z(-sqrt(y))]/(2sqrt(y)) <= L/sqrt(y)`. (5.3)

Applying this to `X_0` and `P_m`, the density of their independent positive sum obeys the beta-integral bound

`||p_{X_0^2+P_m^2}||_infinity`
` <= c_m integral_0^y [u(y-u)]^(-1/2) du`
` = pi c_m`.                                                        (5.4)

Convolution with the independent probability law of `-R_m^2` cannot increase `L^infinity`. Therefore

`boxed( ||p_{Q_m}||_infinity <= pi c_m <= pi sqrt(e) < 5.180. )`    (5.5)

So the family that kills **both** rank-three random-cut smoothing and uniformly good physical principal pivots has a small dimension-free density constant after exact bank compression.

## 6. Direct insertion into the partner's decoupled time hierarchy

The partner's all-copy identity says, with Gaussian mollification `p_eps`, that

`J_k(eps)=int p_eps(y)^k dy`

and a density bound `B` implies

`J_k(eps)<=B^(k-1)` for every integer `k>=2` and every `eps>0`.

Applying (5.5) gives the actual inequalities

`boxed( J_k(eps) <= (pi c_m)^(k-1) <= (pi sqrt(e))^(k-1) )`         (6.1)

for the entire coloop-bank family.

At the independent-copy level this includes

`boxed(
 (2*pi)^(-1) int_R |phi_m(t)|^2 exp(-eps^2 t^2) dt <= pi sqrt(e).
)`                                                                  (6.2)

No independence of `U_i=X_i+X_i'` and `V_i=X_i-X_i'` is asserted or used. The all-order estimate (6.1), rather than a fixed `L^2` bound alone, recovers the required **linear** small-ball scale:

`P(Q_m in I) <= pi sqrt(e) |I|`.                                    (6.3)

This is a direct mathematical use of the named partner's completed time-integral mechanism.

## 7. Corrected sufficient statement: three independent diffuse banks

The preceding repair is not limited to the diagonal signature (2.1).

Partition original coordinates into three disjoint banks of sizes `m_1,m_2,m_3`. Let the spectral frame contain, on bank `r`, repeated rows `e_r/sqrt(m_r)`, so `U^T U=I_3`. Let `Lambda` be any real symmetric `3 x 3` matrix with

`sigma_min(Lambda)>=1`.

For the normalized bank sums `Y=(Y_1,Y_2,Y_3)`, the quadratic form is exactly

`Q=Y^T Lambda Y`,

and the `Y_r` are independent. Lemma 5.1 gives density caps `c_r<=sqrt(e)`. Put `D=diag(c_1,c_2,c_3)` and `Z=DY`; then the `Z_r` are independent with density caps at most one, while

`Q=Z^T B Z`, `B=D^(-1) Lambda D^(-1)`.

Hence

`sigma_min(B) >= sigma_min(Lambda)/||D||^2 >= 1/e`.                 (7.1)

Applying the source-pinned `account02/B15` three-variable theorem yields

`boxed(
 ||p_Q||_infinity <= e(2*pi+3*sqrt(3)) < 31.205.
)`                                                                  (7.2)

This is a genuine exact-rank-three coupled family: `Lambda` may be indefinite and nondiagonal in the bank coordinates. The correct principle exposed by (7.2) is:

> **Compress disjoint independent coordinate banks before paying a reciprocal finite physical minor.**

The principal-pivot certificate may be arbitrarily small in the uncompressed coordinates even though the compressed three-variable matrix retains all spectral curvature at constant scale.

## 8. What remains unpaid

The full conjecture remains open. The new family removes one tempting structural bridge and identifies a stronger replacement obligation.

A successful general theorem must recognize **compressible spectral banks / shared hubs** in addition to the partner's disjoint-Pluecker resource. In exact rank three, the next concrete implication is a product-preserving structural alternative of the following type:

1. positive disjoint Pluecker mass gives the partner's random-cut cross-block theorem; or
2. the near-coloop/overlap-heavy frame admits a bounded number of **independent original-coordinate aggregates** whose joint quadratic matrix has uniformly controlled singular values and whose aggregate one-dimensional density caps stay universal.

The coloop-bank family proves that branch (2) is essential and can succeed even when every rank-three cut is impossible and every physical nonsingular principal triple has scale `1/m`.

For matrices with additional eigendirections, the separate cancellation/absorption problem also remains: one must form the product-preserving compression for the actual full quadratic form rather than discarding spectral components.

## 9. Exact computation

`CHECK.py` and `CHECK_OUTPUT.txt` in this immutable run directory independently verify for `m=2,3,4,5`:

- spectrum exactly `{1,1,-1,0,...,0}`;
- `m^2` nonzero Pluecker bases, each weight `1/m^2`;
- disjoint Pluecker mass exactly zero;
- `kappa=-2/m`;
- every nonsingular physical principal triple has smallest singular value `1/m` and determinant `-1/m^2`;
- every coordinate cut has cross rank at most two.

The output ends `STATUS=PASS`. This finite computation is regression evidence only; Sections 2–7 are the all-`m` proof.

## 10. Status ledger

- `QFORM-FULL`: **OPEN**.
- `QFORM-COLOOP-DIFFUSE-BANK-ADVERSARY-v1`: **PROVED**.
- Uniform `principal 3/4 OR rank-three cross-cut` structural dichotomy: **REFUTED** by (4.2).
- `QFORM-NORMALIZED-BANK-CAP-v1`: **PROVED**, equation (5.2), using sharp Young.
- `QFORM-COLOOP-BANK-DENSITY-v1`: **PROVED**, bound `pi sqrt(e)`.
- `QFORM-THREE-BANK-COMPRESSION-v1`: **PROVED** in the scope of Section 7, bound `e(2*pi+3sqrt(3))`.
- named partner `account03/B03` latest random-cut theorem: **APPLIED** exactly to show `R=0` and to obtain (6.1) from the uniform density bound.
- `QFORM-UV-CONDITIONAL-CAP-FALSE`: **CONSUMED**; no invalid conditional independence/cap is used.
- native learned-memory receiver/context use: **NOT OBSERVED**; execution remains `WITHOUT_VERIFIED_BRAIN`.
