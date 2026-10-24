# account02/B15 — principal-pivot regularity closure and qualitative bounded-density theorem

**Run:** `20260922T120155Z-account02-B15-qform-r1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.5`  
**Assignment:** `Absolute continuity and regularity`  
**Classification:** `TARGET-SUPPORTING-THEOREM / FULL_UNIVERSAL_CONSTANT_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The fresh owner control supersedes the older FEI prompt for this slot. The only live target is the quadratic-form density conjecture. The additional owner check-in `QFORM-CHECKIN-20260922T120815Z` was acknowledged in the shared brain during this run.

## 1. Sources actually consumed

The completed cross-account partner result is:

- `yspennstate/math-open-problems@1ce0598e1c9c4e0681f8f6b86d3dfef990ec5d4e`, `qform/fleet-2026-09-22/account03/B15/account03-B15-20260922T112830Z/REPORT.md`.

It proves the exact bathtub reduction: for every interval `J`, maximizing `P(X^TAX in J)` over independent one-dimensional densities bounded by one is equivalent to maximizing the shell volume over product sets `E_1 x ... x E_n` with `|E_i|=1`. I use that equivalence below to interpret the local principal-block theorem as an exact geometric certificate, not as a regularity-of-input argument.

I also consume the newer completed cross-block theorem at

- `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`, `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`.

Its proved rank-`r>2` cross-block Fourier estimate gives a bounded continuous density whenever an original-coordinate cut has cross-block rank at least three, and in particular closes a large delocalized rank-three branch. I use it only as a continuity/coverage input; the new theorem below is independent of it.

The previous account02/B15 report proved the `3 x 3` affine principal-block estimate

`||p||_infinity <= (2*pi+3*sqrt(3))/sigma_min(B)`

for every invertible symmetric `3 x 3` block `B`. This run extends that mechanism to `4 x 4`, proves a principal-pivot lemma that every symmetric matrix of rank at least three contains an invertible principal block of order three or four, and therefore closes the **qualitative bounded-density existence** problem for every fixed target matrix `A`. What remains open is exactly the dimension- and matrix-independent constant.

---

## 2. Absolute continuity needs no three-eigenvalue hypothesis

### Theorem 2.1 — `QFORM-ABSOLUTE-CONTINUITY-RANK1-v1`

Let `X` be any random vector in `R^n` with an absolutely continuous law, and let `A` be a nonzero real symmetric matrix. Then `Q=X^TAX` is absolutely continuous. In particular, under the owner target assumptions no singular component or atom can occur, independently of the desired universal `L^infinity` estimate.

### Proof

Let `r=rank(A)>=1`. Orthogonally diagonalize the nonzero spectral part:

`Q = sum_{j=1}^r lambda_j Z_j^2`, with every `lambda_j != 0`.

After the orthogonal change of variables the law of `Z` still has an `L^1` density. Integrating out the `n-r` null coordinates gives an `L^1(R^r)` density `h(z)` for the active spectral coordinates. Put

`q(z)=sum_{j=1}^r lambda_j z_j^2`.

For a Lebesgue-null set `N subset R`, the coarea formula on each ball `B_R` gives

`int_{q^{-1}(N) cap B_R} |grad q(z)| dz
 = int_N H^{r-1}(q^{-1}(t) cap B_R) dt = 0`.

Since `grad q(z)=2(lambda_1 z_1,...,lambda_r z_r)` vanishes only at `z=0`, it follows that `q^{-1}(N)` has `r`-dimensional Lebesgue measure zero. Hence

`P(Q in N)=int_{q^{-1}(N)} h(z) dz=0`.

Thus the pushforward is absolutely continuous. For almost every `t` one may take the coarea density

`p_Q(t)=int_{q^{-1}(t)} h(z)/|grad q(z)| dH^{r-1}(z)`.

This theorem is qualitative only; it does not bound the displayed integral uniformly.

---

## 3. A four-coordinate affine quadratic bound

The previous run treated dimension three. The only new local dimension needed for a general symmetric principal-pivot argument is four.

### Theorem 3.1 — `QFORM-4VAR-AFFINE-PRINCIPAL-v1`

Let `Y_1,...,Y_4` be independent real variables with densities bounded by `1`, and let `B` be an invertible real symmetric `4 x 4` matrix. For every `b in R^4` and `c in R`, the affine quadratic

`Z=Y^T B Y + 2 b^T Y + c`

has an essentially bounded density with

`||p_Z||_infinity <= C_4 / sigma_min(B)`,

where

`C_4 := 4*pi + 8 < 20.57`.

No sign condition is imposed on the inertia of `B`.

### Proof

Complete the square and translate the four independent coordinates. Translation preserves independence and the one-dimensional density bounds, so it suffices to take `b=0`. Scale `B` by `kappa=sigma_min(B)`; therefore it suffices to prove the interval estimate for `sigma_min(B)>=1`:

`P(Y^TBY in J) <= (4*pi+8)|J|`

for every interval `J`.

Write `F(y)=prod_i f_i(y_i)`, so `0<=F<=1` and `int F=1`. Split into

`N={y: |By|<=1}` and `N^c`.

#### Near region

Write the symmetric polar decomposition `B=S|B|`, where `S=sign(B)` is symmetric orthogonal and commutes with `|B|`. Set

`z=|B|^{1/2}y`.

Then

`y^TBy=z^TSz`,

`dy=(det|B|)^(-1/2) dz <= dz`,

and

`|By|^2=z^T|B|z >= |z|^2`.

Thus `N` maps inside the Euclidean unit ball. Since `F<=1`, its contribution is bounded by the Euclidean volume of

`{z: |z|<=1, z^TSz in J}`.

There are only three inertia types up to sign.

1. Signature `(4,0)`: with `u=|z|^2`, the four-ball volume is `(pi^2/2)u^2`, so the density with respect to `u` is `pi^2 u<=pi^2`.

2. Signature `(3,1)`: write `z=(x,s)` with `x in R^3`. For fixed `s`, the allowed interval in `|x|^2` has length at most `|J|`; the derivative of three-ball volume `(4*pi/3)u^{3/2}` with respect to `u` is `2*pi*sqrt(u)<=2*pi` inside the unit ball. Integrating `s in[-1,1]` gives at most `4*pi|J|`.

3. Signature `(2,2)`: write `z=(x,w)` with `x,w in R^2`. For fixed `w`, planar area has derivative `pi` with respect to `|x|^2`. Integrating over `w` in the unit disk gives at most `pi^2|J|`.

Hence in every signature

`P(N, Y^TBY in J) <= 4*pi |J|`.

#### Far region

If `|By|>1`, then some original coordinate satisfies `|(By)_i|>1/2`. Let

`E_i={Y^TBY in J, |(By)_i|>1/2}`.

Condition on the other three original independent coordinates. As a function `g(t)` of `t=y_i`,

`g'(t)=2(By)_i`.

On `E_i`, `|g'|>1`. Since `g'` is affine, the set `|g'|>1` has at most two monotone components. On each component the inverse image of an interval of length `|J|` has length at most `|J|`. The one-coordinate density is at most one, so

`P(E_i | Y_{hat i}) <= 2|J|`.

Summing `i=1,...,4` gives

`P(N^c, Y^TBY in J) <= 8|J|`.

Combining near and far regions proves the interval bound. Interval domination implies the stated Radon-Nikodym density estimate. Scaling restores the factor `1/sigma_min(B)`. QED.

### Unified local constants

Together with the previous `3 x 3` theorem, for `d in {3,4}` define

`C_3=2*pi+3*sqrt(3)`, `C_4=4*pi+8`.

Every invertible symmetric `d x d` principal block gives the conditional bound

`||p||_infinity <= C_d/sigma_min(B)`

uniformly over all affine terms created by conditioning the other coordinates.

---

## 4. Symmetric matrices of rank at least three always have a 3- or 4-pivot

### Lemma 4.1 — `QFORM-PRINCIPAL-PIVOT-34-v1`

Every real symmetric matrix `A` with `rank(A)>=3` has a nonsingular principal submatrix `A_{J,J}` with `|J|=3` or `|J|=4`.

### Proof

Perform symmetric Gaussian elimination using principal pivots on successive Schur complements.

At any stage let `C` be the current nonzero symmetric Schur complement.

- If some diagonal entry `c_ii` is nonzero, use the invertible `1 x 1` principal pivot `{i}`.
- If every diagonal entry is zero, choose an off-diagonal `c_ij != 0`. Then the principal block

  `[[0,c_ij],[c_ij,0]]`

  is invertible, so use the `2 x 2` pivot `{i,j}`.

After pivoting, the next Schur complement is symmetric and its rank drops by exactly the pivot size. By the block determinant formula, the union of the pivot indices chosen so far is a nonsingular principal submatrix of the original matrix: its determinant is the product of the successive nonzero pivot determinants.

Starting from rank at least three, stop the first time the accumulated pivot size is at least three. Because each pivot has size one or two, the first such size is either three or four. The corresponding original principal submatrix is nonsingular. QED.

This is the qualitative fact missing from the previous fixed-triple report: one uniformly good triple need not exist, but some finite nonsingular pivot of order at most four always exists.

---

## 5. Every fixed target matrix already has a bounded density

### Theorem 5.1 — `QFORM-FIXED-A-BOUNDED-DENSITY-v1`

Let `X_1,...,X_n` be independent real variables with densities bounded by one. Let `A` be a real symmetric matrix with `rank(A)>=3`. Then `Q=X^TAX` has an essentially bounded density.

More explicitly, define

`kappa_*(A)=max { sigma_min(A_{J,J}) : |J| in {3,4}, det(A_{J,J}) != 0 }`.

Lemma 4.1 gives `kappa_*(A)>0`. Then

`||p_Q||_infinity <= max(C_3,C_4)/kappa_*(A)`.

In fact one may take the better minimum over the available principal blocks:

`||p_Q||_infinity <= min_{J: |J| in {3,4}, det A_J !=0} C_|J|/sigma_min(A_J)`.

### Proof

Choose a nonsingular principal block `B=A_{J,J}` of order `d=3` or `4`. Condition on all variables outside `J`. The conditional polynomial in `Y=X_J` has the form

`Y^T B Y + 2 b(w)^T Y + c(w)`.

The coordinates in `J` remain independent with their original density bounds. The local theorem in dimension `d` bounds every conditional interval probability by

`(C_d/sigma_min(B)) |I|`,

uniformly in the conditioned value `w`. Averaging the conditional laws gives the same interval domination unconditionally, hence the same `L^infinity` density bound. QED.

### Exact product-set interpretation using the partner theorem

By account03/B15's bathtub theorem, Theorem 5.1 is equivalently the geometric statement that for every fixed rank-at-least-three symmetric `A`, every product set `E_1 x ... x E_n` with `|E_i|=1`, and every interval `I`,

`|{x in prod_i E_i : x^T A x in I}| <= C(A)|I|`

with the explicit finite certificate `C(A)` above. Thus arbitrary measurable input densities introduce no additional qualitative obstruction: **only uniformity of the constant over matrices and dimensions remains.**

---

## 6. Why this is not the full conjecture

The owner requires one universal constant independent of `A` and `n`. The quantity `kappa_*(A)` can approach zero under perfectly admissible three-large-eigenvalue matrices. The previous flat rank-three Hadamard projector already shows this: every `3 x 3` principal block has scale `O(1/n)`, while a `4 x 4` principal block is singular because the whole matrix has rank three. Thus Theorem 5.1 may only give an `O(n)` certificate on that family.

That dimension loss is a mechanism defect, not a target obstruction. The newer cross-block theorem at commit `862498...` proves a continuous density with a universal bound on a delocalized rank-three branch, including flat three-frames under its leverage hypothesis. So the current evidence gives a clean regularity split:

- **all** rank-at-least-three target matrices: bounded density with a finite matrix-dependent constant (this report);
- diagonal target matrices: bounded uniformly continuous density with constant `pi` (previous B15 report);
- matrices admitting a rank-at-least-three original-coordinate cross block with controlled determinant product: bounded continuous density (consumed cross-block theorem);
- fully delocalized rank-three frames: bounded continuous density with an explicit universal constant under the stated leverage condition (consumed cross-block theorem).

The full universal `L^infinity` conjecture is still **OPEN**, and the stronger continuous-representative conclusion is also not proved in the remaining localized/coupled regime.

---

## 7. First unresolved implication after this run

The qualitative regularity question is no longer the bottleneck: under the target hypotheses every fixed `A` already has an `L^infinity` density. The first missing target implication is now genuinely quantitative:

> Replace the matrix-dependent pivot certificate `1/kappa_*(A)` by a dimension-free aggregate-curvature payment using the spectral assumption that at least three eigenvalues have modulus at least one.

A single principal block cannot do this. Two mechanisms now cover opposite ends:

1. local principal pivots pay concentrated curvature but can lose dimension on flat frames;
2. rank-three cross-block Fourier smoothing pays sufficiently split/delocalized curvature and gives continuity.

The next concrete bridge should therefore be a **local/cross-block dichotomy with uniform constants**: prove that every admissible matrix either has a principal `3`/`4` block with `sigma_min>=c`, or admits an original-coordinate cut whose cross block has three singular directions with determinant product `>=c`, after first reducing harmless larger/smaller spectral components correctly. The flat-frame example lies in the second branch; diagonal matrices lie in the first/convolution branch. A counterexample to such a dichotomy would precisely identify the remaining mixed-leverage geometry.

No claim is made that this dichotomy is already true. It is the next quantified implication exposed by the two proved mechanisms.

---

## 8. Status and integrity

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MECHANISM CHANGE:** `one fixed nonsingular 3-coordinate block -> complete symmetric 1x1/2x2 pivot elimination yielding a nonsingular 3- or 4-coordinate block, plus a new 4-variable shell theorem`. This changes the qualitative conclusion from a conditional branch to **every fixed admissible matrix has some finite bounded-density constant**.

The stronger universal constant remains unpaid. No pointwise law-uniform Fresnel decay, projection independence, moment assumption, compact support, or diagonal-eigenbasis assumption is used. The rank-two opposite-sign logarithmic control is not contradicted: the local theorem begins at dimension three, exactly where the near-shell volume becomes linearly bounded.

No novelty or publication-priority claim is made.
