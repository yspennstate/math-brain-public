# fleet02/B13 — three-bank rank-three aggregation closes a delocalized product branch

**Run:** `20260922T125435Z-fleet02-B13-80c2a32d`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Extremal product laws`  
**Classification:** `PROVED TARGET-LEVEL SUBCLASS / PARTNER REDUCTION APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture remains **OPEN / NOT PROVED**.

## 1. First unpaid implication and correction-aware start

The preceding B13 run proved the exact reduction from arbitrary one-dimensional densities `0<=f_i<=1`, `int f_i=1`, to unit-measure product indicators, and then to bounded finite unions of intervals, for every fixed quadratic slab. The newest proof assembly isolates a product-origin trace/aggregation gap: local principal triples and fixed cross blocks can all become ill-conditioned even when the spectral rank-three resource is perfectly nondegenerate.

The first unpaid implication for this run is therefore:

> **Can a genuinely delocalized rank-three form be paid by product-preserving aggregation before selecting a bad local minor?**

The answer proved below is yes for the exact three-bank geometry: if the rank-three spectral frame has only three projective row directions, then the product law aggregates to three independent scalar banks and the full rank-three density is bounded by a universal constant `<23`, even when every useful fixed physical triple degenerates with dimension.

Corrections consumed before publication include: law-uniform pointwise Fresnel decay is false; fiber suprema may lose dimension; rotation does not preserve independence; a cross minor alone is insufficient; generic X-ray control is insufficient for an indefinite shell; conditional sum/difference densities need not retain their marginal cap; and a single Schur pivot need not expose a rank-two cross block. None of those mechanisms is used below.

## 2. Source inputs actually used

### 2.1 Three-variable quadratic theorem

I use the source theorem

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`.

It proves: if `Z_1,Z_2,Z_3` are independent, each has density at most one, and `B` is a real symmetric invertible `3 x 3` matrix with `kappa=sigma_min(B)`, then

`||p_{Z^T B Z+2b^T Z+c}||_infinity <= C_3/kappa`,

where

`C_3=2 pi+3 sqrt(3)<11.48`.

No sign restriction is imposed on `B`.

### 2.2 One-dimensional product-marginal theorem

I use the sharp marginal-density theorem of Livshyts--Paouris--Pivovarov, arXiv:1507.07949: for a product density with one-dimensional factors bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. In particular, for any unit vector `a`, the normalized linear form `sum a_i X_i` has density at most `sqrt(2)`.

### 2.3 Assigned partner result

The assigned partner `fleet03/B13` has now completed

`yspennstate/math-open-problems@44e5051b996705fe5fe47fb2f848d1a2ed51024f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/fleet03-B13-20260922T123422Z/REPORT.md`.

It proves that for every fixed candidate constant `C`, any strict failure of the full QFORM inequality has a witness with rational symmetric matrix, three eigenvalues satisfying `|lambda|>1` strictly, rational finite-fragment unit supports, and a rational test interval, with no loss in `C`. I apply this theorem in Section 6 to sharpen the residual falsification class after the new aggregation theorem.

## 3. Exact three-bank normal form

Let `A` have rank exactly three. Write

`A=R Lambda R^T`,

where `R` is `n x 3`, `R^T R=I_3`, and `Lambda` is real symmetric invertible. Under the owner hypothesis in the rank-three case,

`sigma_min(Lambda)>=1`.

Let `r_i in R^3` be the `i`th row of `R`.

Assume the nonzero rows lie in the union of three one-dimensional subspaces of `R^3`. Because `R` has rank three, all three directions are needed. Thus, after partitioning the active physical coordinates into nonempty disjoint sets `G_1,G_2,G_3`, there are nonzero direction vectors `w_k` and scalars `alpha_i` such that

`r_i=alpha_i w_k` for `i in G_k`.

Set

`s_k=(sum_{i in G_k} alpha_i^2)^(1/2)`,

and

`v_k=s_k w_k`.

The frame identity is

`I_3=R^T R=sum_i r_i r_i^T=sum_{k=1}^3 v_k v_k^T`.  (3.1)

Let `V=[v_1 v_2 v_3]`. Equation (3.1) is

`V V^T=I_3`.

Since `V` is square, it is orthogonal. Hence:

**Parseval rigidity.** The three weighted row directions `v_1,v_2,v_3` are automatically an orthonormal basis.

Equivalently, define the `n x 3` matrix `C` by

`C_{ik}=alpha_i/s_k` for `i in G_k`, and zero otherwise.

Then the columns of `C` have disjoint physical supports and unit Euclidean norm, so `C^T C=I_3`, and

`R=C V^T`.  (3.2)

Therefore

`A=C B C^T`,

where

`B=V^T Lambda V`  (3.3)

is orthogonally similar to `Lambda`. In particular

`sigma_min(B)=sigma_min(Lambda)>=1`.  (3.4)

This is an exact product-preserving normal form. No eigenbasis rotation is applied to the random vector `X`: the rotation `V` occurs only in the three-dimensional coefficient space, while `C` has disjoint supports in the original independent coordinates.

## 4. Three independent aggregate coordinates

For each bank define

`Y_k=(C^T X)_k=(1/s_k) sum_{i in G_k} alpha_i X_i`.

Because the physical sets `G_1,G_2,G_3` are disjoint and the original `X_i` are independent, the three random variables `Y_1,Y_2,Y_3` are independent.

For each `k`, the coefficient vector `(alpha_i/s_k)_{i in G_k}` has Euclidean norm one. The one-dimensional Livshyts--Paouris--Pivovarov marginal theorem therefore gives

`||p_{Y_k}||_infinity <= sqrt(2)`.  (4.1)

Coordinates whose row `r_i` is zero do not enter `A` at all and may simply be integrated out.

Using (3.2)--(3.3),

`X^T A X=(C^T X)^T B(C^T X)=Y^T B Y`.  (4.2)

Thus the delocalized rank-three problem has collapsed, **without loss of independence**, to a genuine three-variable quadratic form whose independent marginal densities are bounded by `sqrt(2)`.

## 5. Universal density bound for the three-bank class

### Theorem — `QFORM-RANK3-THREE-BANK-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by one. Let `A` be real symmetric of rank exactly three, with all three nonzero eigenvalues of absolute value at least one. Assume the nonzero rows of an orthonormal spectral frame for `range(A)` lie in at most three projective directions; equivalently, `range(A)` admits an orthonormal basis whose three vectors have pairwise disjoint physical supports.

Then `Q=X^T A X` has an essentially bounded density satisfying

`||p_Q||_infinity <= 2 C_3 = 4 pi+6 sqrt(3) < 23`.  (5.1)

#### Proof

By Sections 3--4, `Q=Y^T B Y`, where the `Y_k` are independent, `||p_{Y_k}||_infinity<=sqrt(2)`, and `sigma_min(B)>=1`.

Set

`Z_k=sqrt(2) Y_k`.

Then the `Z_k` remain independent and each has density bounded by one. Moreover

`Q=(1/2) Z^T B Z=Z^T (B/2) Z`,

and

`sigma_min(B/2)>=1/2`.

Apply the three-variable affine quadratic theorem with matrix `B/2`, `b=0`, `c=0`, and `kappa=1/2`. This gives

`||p_Q||_infinity <= C_3/(1/2)=2C_3=4 pi+6 sqrt(3)`.

Numerically this is about `22.958676`, hence strictly less than `23`. QED.

The proof uses no moments, support restrictions, sign restrictions, log-concavity, or independence after a spectral rotation. The aggregation is performed on disjoint sets of original independent coordinates.

### Product-set geometric form

By the exact B13 bang-bang reduction from the preceding run, the same theorem is equivalently the slab-volume estimate

`|{x in prod_i E_i : x^T A x in J}| <= (4 pi+6 sqrt(3)) |J|`

for every family of measurable unit-measure sets `E_i`, hence also for bounded finite unions of intervals.

## 6. Actual application to the partner rational-witness theorem

Fix the candidate constant `C=23`. Suppose the full QFORM inequality with constant `23` fails. The completed `fleet03/B13` rational strict-slack theorem supplies a **strict** witness in which:

- each input law is the indicator of a rational-endpoint finite union of intervals of total measure one;
- `A` is rational symmetric;
- at least three eigenvalues satisfy `|lambda|>1` strictly;
- the test interval has rational endpoints.

If that rational witness had rank exactly three and its spectral range had the three-bank structure above, Theorem (5.1) would instead give

`P(Q in J) <= (4 pi+6 sqrt(3)) |J| < 23 |J|`,

contradicting the strict partner witness.

Therefore:

**Corollary — `QFORM-RATIONAL-23-RESIDUAL-v1`.** Any strict rational finite-fragment counterexample to the candidate constant `23` must either

1. have rank greater than three, or
2. have rank exactly three with **at least four distinct projective row directions** in its spectral frame.

This is a genuine use of the completed assigned-partner theorem: it removes arbitrary real laws/data and the spectral-threshold boundary from the falsification side, while the new theorem removes the exact three-bank rank-three geometry from that countable residual.

## 7. The fleet01/B19 hard family is now a direct corollary

The proof-assembly worker `fleet01/B19` exhibited, for `n=2m+1`, the rank-three family whose spectral frame has

`u_1=e_0`,

`u_2=m^(-1/2) 1_Y`,

`u_3=m^(-1/2) 1_Z`,

and spectral matrix

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`.

It has eigenvalues `{1,1,-1}`, no disjoint physical cross block of rank three, and every principal physical triple has smallest singular value at most `1/m` (with equality on its only nonsingular triple type). The prior proof closed it by a specialized hyperbolic-square aggregation.

Its nonzero spectral-frame rows lie exactly on the three coordinate directions `e_1,e_2,e_3`. Hence `QFORM-RANK3-THREE-BANK-v1` applies immediately and gives the uniform bound

`||p_Q||_infinity <23`

for every `m` and every admissible product law.

This identifies the structural reason the family is harmless despite the collapse of every local-minor mechanism: the globally delocalized frame is an exact three-bank Parseval frame, so high-cardinality aggregation reconstructs an orthogonal three-variable product channel before any inverse-minor cost is paid.

## 8. Target-level movement and remaining implication

**Before:** B13 had removed the arbitrary-density quantifier by exact bang-bang/finite-fragment purification, but the geometric slab estimate remained untouched in the delocalized branch.

**After:** a nonlocal, dimension-independent rank-three geometric branch is closed at the explicit constant `4 pi+6 sqrt(3)<23`, including a known family where all fixed principal triples degenerate and no rank-three disjoint cross block exists.

The new first unpaid implication is no longer “can aggregation beat bad local minors?” in general. It is the sharper statement:

> **`QFORM-RANK3-MULTIDIRECTION-AGGREGATION-v1` (OPEN):** for a rank-three spectral frame with at least four projective row directions, convert the Parseval identity `sum_i r_i r_i^T=I_3` and original-coordinate product structure into a universal small-ball/density bound without selecting one inverse-conditioned local minor and without replacing the spectral projection by an arbitrary bounded three-dimensional density.

After rank three is closed, arbitrary additional spectral directions remain a separate interaction problem except in already-paid near-diagonal, diffuse-separable, principal-block and other scoped branches.

## 9. Integrity/status

- Full QFORM: **OPEN / NOT PROVED**.
- New theorem: analytic, dimension-free, arbitrary-sign rank-three subclass.
- Assigned partner result: read in full and applied in Section 6.
- No single-interval extremality is assumed.
- No pointwise law-uniform Fourier decay, fiber supremum, cross-minor-alone, conditional-density-cap, or independence-after-rotation argument is used.
- The optional continuous-density conclusion is not claimed here; the theorem establishes an essentially bounded density.
