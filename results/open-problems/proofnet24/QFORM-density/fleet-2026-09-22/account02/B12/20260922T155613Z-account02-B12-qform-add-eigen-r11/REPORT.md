# account02/B12 — full-matrix spike/tail control through a physical Schur pivot

**Run:** `20260922T155613Z-account02-B12-qform-add-eigen-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_REDUCTION_AND_STABILITY / FULL_TARGET_OPEN`  
**Execution:** authenticated private-repository retrieval was used in this run; no claim is made of native learned-memory ingestion.

## 1. Exact target, correction discipline, and first unpaid implication

The full target remains OPEN: for arbitrary dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or produce a valid counterexample.

This report does not rotate the random vector and never treats a rotated remainder as an independent convolution. All pivots and cross blocks are in the original physical coordinates. Live corrections consumed before publication include the failures of pointwise law-uniform Fresnel decay, naive fiber-supremum integration, a universal fixed cross minor, a universal single-Schur rank-two extraction, and a local cross-rank-three dichotomy.

The first unpaid implication attacked here is narrower and source-valid: **if a source-valid physical pivot/cross certificate exists for a base matrix, how do arbitrary added eigen-directions of unbounded magnitude and a smaller full-rank tail propagate through the Schur complement?** The nonlinearity of the Schur complement makes it invalid simply to say that a rank-r full-matrix perturbation remains rank-r after completing a square without proof. That exact propagation is proved below.

## 2. Completed source results actually applied

### 2.1 Assigned partner account03/B12

Latest completed partner report used here:

`yspennstate/math-open-problems@cb592aa97e7d74af9b23dbbb32493e5a36f937e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T151120Z-qform-eigenvalue-r11/REPORT.md`.

Its `QFORM-PIVOT-HYBRID-RESIDUAL-STABILITY-v1` states that for a physical pivot `a!=0`, if the Schur residual has a decomposition whose fixed cross block consists of a base block with `s_{5+r}>=sigma`, a rank-`r` perturbation, cross leakage `eta`, and an operator-norm tail `delta`, with `mu=sigma-eta-delta>0`, then

`||p_Q||_infinity <= sqrt(10e/(|a| mu)) < 5.214/sqrt(|a| mu)`.

That theorem assumed the residual decomposition. Sections 3--5 below derive such a decomposition from a **full-matrix** rank-r added-eigendirection perturbation plus a small arbitrary tail.

### 2.2 Square-pivot ridge theorem

A newer compatible completed theorem is account03/B09:

`yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T155042Z-qform12/REPORT.md`.

For a physical pivot `a!=0`, if a Schur-complement cross block has ridge effective dimension `theta>q`, `1<=q<=2`, and ridge leverage at most `q/2`, then the full quadratic form has an essentially bounded density. In particular, with `q=2`, **three** Schur-cross singular values at least `sigma` imply

`||p_Q||_infinity < 18.084/sqrt(|a| sigma)`.

This no-leverage endpoint is used in Section 6 to reduce the required residual redundancy from `5+r` to `3+r`.

### 2.3 One-scale ridge source

The ridge characteristic-function theorem underlying account03/B09 is

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

I use only the source-stated scope; no independent-review status is transferred beyond what is actually recorded.

## 3. Exact algebra: a rank-r full-matrix spike remains rank-r in the Schur residual

For a symmetric matrix `M` and an original coordinate `k` with `M_kk!=0`, write

`Sc_k(M) = M[-k,-k] - M[-k,k] M[k,-k]/M_kk`.

### Lemma 3.1 — `QFORM-SCHUR-RANK-SPIKE-PRESERVATION-v1`

Let `A0` be symmetric with `a0=(A0)_kk!=0`. Let `R` be symmetric with `rank(R)<=r`, and suppose the final pivot `a=(A0+R)_kk` is also nonzero. Then

`rank( Sc_k(A0+R) - Sc_k(A0) ) <= r`.                     (3.1)

No norm, sign, or eigenvalue-size assumption is imposed on `R`.

#### Proof

Permute `k` to the first coordinate and write

`A0 = [[a0, b0^T],[b0,C0]]`, `H0=C0-b0 b0^T/a0`.

Use the unit lower-triangular congruence

`L=[[1,0],[-b0/a0,I]]`.

Then

`L A0 L^T = diag(a0,H0)`.

Such a shear leaves the scalar Schur complement invariant. Also `Rtilde=L R L^T` has rank at most `r`. Factor its nonzero part as

`Rtilde = V J V^T`,

where `V` has `r'<=r` columns and `J` is an invertible symmetric `r' x r'` matrix. Partition

`V=[[c^T],[W]]`.

The final transformed matrix is

`[[a0+c^T J c, c^T J W^T], [WJc, H0+WJW^T]]`.

Its pivot is the original final pivot `a`, because the first row of `L` is the first coordinate row. Taking its Schur complement gives

`Sc_k(A0+R)-H0
 = W [ J - J c c^T J /(a0+c^T J c) ] W^T`.

The bracket is an `r' x r'` matrix, so the difference has rank at most `r'<=r`. QED.

For a single added eigen-direction `R=tau vv^T`, the formula specializes to the exact rank-one update

`Sc_k(A0+tau vv^T)
 = H0 + [tau a0/(a0+tau v_k^2)] ww^T`,                  (3.2)

where

`w=v_{-k}-(v_k/a0)b0`,

provided `a0+tau v_k^2!=0`. Thus an arbitrarily large eigenvalue does not create higher residual rank. When `v_k!=0`, its Schur coefficient even saturates as `|tau|->infinity`; the only algebraic exceptional branch is cancellation of the physical pivot.

## 4. A small full-matrix tail has an explicit Schur price

### Lemma 4.1 — `QFORM-SCHUR-TAIL-LIPSCHITZ-v1`

With the same block notation, let `S` be symmetric and

`||S||_op <= delta < |a0|`.

Set

`kappa = ||b0||_2/|a0|`,

`eps = delta (1+kappa)^2 / (1-delta/|a0|)`.               (4.1)

Then the perturbed pivot of `A0+S` is nonzero and

`|| Sc_k(A0+S)-Sc_k(A0) ||_op <= eps`.                    (4.2)

#### Proof

Write

`S=[[s,u^T],[u,D]]`.

Then `|s|,||u||,||D||<=delta`, and `|a0+s|>=|a0|-delta`. Expanding the two Schur complements,

`Sc_k(A0+S)-H0
 = D - (b0 u^T+u b0^T+u u^T)/(a0+s)
   + b0 b0^T (1/a0-1/(a0+s))`.

Taking operator norms gives

`<= delta + (2||b0||delta+delta^2)/(|a0|-delta)
          + ||b0||^2 delta/(|a0|(|a0|-delta))`.

Substitute `kappa=||b0||/|a0|` and `delta/|a0|`; the numerator collapses exactly to `(1+kappa)^2`, yielding (4.1). QED.

The factor involving `kappa` is unavoidable for a fixed pivot: a tiny perturbation of the scalar denominator can be amplified when the base pivot has a very large off-diagonal row. No hidden moment or support assumption is used.

## 5. Main stability reduction: full-matrix spike plus tail -> residual rank plus tail

### Theorem 5.1 — `QFORM-FULLMATRIX-SPIKE-TAIL-TO-SCHUR-v1`

Let

`A = A0 + S + R`,

where `A0,S,R` are symmetric, `rank(R)<=r`, and at an original coordinate `k`

`a0=(A0)_kk!=0`, `||S||_op<=delta<|a0|`.

Let `a=A_kk` and assume the final pivot `a!=0`. Put

`H0=Sc_k(A0)`, `H=Sc_k(A)`,

and let `eps` be (4.1). Then there exist symmetric matrices `T,E` on the residual coordinates such that

`H = H0 + T + E`,

`||T||_op<=eps`, `rank(E)<=r`.                             (5.1)

#### Proof

Set `A1=A0+S`. Lemma 4.1 gives `T=Sc_k(A1)-H0` with `||T||<=eps`, and the pivot of `A1` is nonzero. Apply Lemma 3.1 to `A1` and the arbitrary rank-r matrix `R`; since the final pivot is nonzero,

`E=Sc_k(A1+R)-Sc_k(A1)`

has rank at most `r`. This proves (5.1). QED.

This is the desired source-valid reduction. A full-matrix spectral spike is never declared independent of the residual; it is converted by exact physical-coordinate algebra into a low-rank residual perturbation.

### Exceptional branch

If the added spike cancels the chosen pivot exactly (`a=0`), the Schur/pivot certificate at this coordinate is unavailable. The theorem makes no claim in that branch. One must choose another physical pivot or use a non-pivot mechanism. This exceptional case is essential and is not silently divided out.

## 6. Applying completed peer results

Fix disjoint residual original-coordinate banks `I,J`, and write

`B0=H0[I,J]`.

Because taking a submatrix cannot increase rank or operator norm, (5.1) gives on this cross block a rank-`r` perturbation plus an operator-norm tail at most `eps`.

### 6.1 Assigned partner account03/B12: five-direction high-quality bound

If

`s_{5+r}(B0) >= sigma > eps`,                                  (6.1)

then the partner theorem `QFORM-PIVOT-HYBRID-RESIDUAL-STABILITY-v1` applies with residual cross leakage zero and tail `eps`. Therefore

`||p_{X^T A X}||_infinity
 <= sqrt(10e/(|a|(sigma-eps)))
 < 5.214/sqrt(|a|(sigma-eps)).`                                (6.2)

This is a new **full-matrix** corollary of the partner theorem: `r` arbitrarily large added eigen-directions of arbitrary signs and magnitudes, plus an arbitrary full-rank small operator-norm tail, are now allowed before the square completion. The only quantitative degradation from the small tail is the explicit Schur price `eps` in (4.1).

### 6.2 Newer account03/B09 pivot-ridge theorem: three-direction version

The square-pivot ridge theorem needs only three substantial residual cross directions when `q=2`. From rank interlacing and Weyl,

`s_3(H[I,J]) >= s_{3+r}(B0)-eps`.                            (6.3)

Hence if

`s_{3+r}(B0) > eps`,

put

`sigma = s_{3+r}(B0)-eps >0`.

Then account03/B09 gives the stronger redundancy statement

`||p_{X^T A X}||_infinity
 < 18.084 / sqrt(|a| sigma)`
` = 18.084 / sqrt(|a| (s_{3+r}(B0)-eps)).`                    (6.4)

Thus a physical square pivot plus `3+r` base Schur-cross directions survives `r` completely arbitrary full-matrix added eigen-directions and a small arbitrary full-rank tail. The price is explicit and dimension-free.

This does not contradict the partner's `5+r` theorem: (6.2) has a much better constant and uses the five-cross determinant route; (6.4) exploits the physical square pivot and the newer ridge `L^p` route to reduce direction count.

## 7. Arbitrary larger eigenvalues can be completely free when their physical cross leakage vanishes

The reduction also clarifies a useful zero-cost case. If an added symmetric matrix is supported entirely inside one side of a certified physical cut, it contributes no cross block there, regardless of its rank, signs, or eigenvalue magnitudes. Likewise, in Lemma 3.1 an arbitrary rank-r full-matrix spike costs only rank `r` in the Schur residual, not its spectral norm.

Consequently, the phrase "additional eigenvalue" should not be priced solely by eigenvalue size: the correct source-valid costs are physical pivot cancellation, residual rank, and physical cross leakage.

## 8. A genuine target-class mechanism test: a large rank-one spike can destroy a low-q ridge certificate without threatening QFORM

The need to preserve the exceptional/spike branch is real. Let

`A0 = [[0,I_6],[I_6,0]]`

on twelve original coordinates. It has six `+1` and six `-1` eigenvalues, hence lies well inside the target spectral class. Across the obvious `6+6` physical cut, choose ridge scale `gamma=sqrt(3/2)`. Then

`K_gamma=(2/5)I_6`, `theta=12/5`,

so the direct ridge theorem works with `q=1`.

Now add the genuine symmetric rank-one eigen-direction

`R_tau = tau z z^T`, `z=(e_1^I+e_1^J)/sqrt(2)`.

The new cross block is

`B_tau=diag(1+tau/2,1,1,1,1,1)`.

Let

`w_tau=(1+tau/2)^2/(3/2+(1+tau/2)^2)`.

The largest ridge leverage is `w_tau` and `theta_tau=w_tau+2`. Any admissible `q` must satisfy `q>=2w_tau`. If `w_tau>=2/3`, equivalently

`tau >= 2(sqrt(3)-1)`,

then

`theta_tau=w_tau+2 <=4w_tau <=2q`,

so **no** `q in [1,2]` satisfies the direct ridge criterion on this fixed cut and scale. The final matrix still has at least ten untouched eigenvalues of absolute value one, so this is not a QFORM counterexample. It is a source-valid counterexample to the stronger statement that an arbitrary-magnitude added eigen-direction preserves a fixed low-q ridge certificate.

The pivot-ridge mechanism of account03/B09 can still rescue suitable square-pivot configurations because its threshold is `theta>q`, not `theta>2q`. This illustrates why the added-eigenvalue analysis must switch certificates rather than insist on monotone preservation of one ridge inequality.

## 9. What changed and what remains open

### Target-level status

`OPEN -> OPEN.` No universal bound was derived from the bare hypothesis of only three global eigenvalues `|lambda|>=1`.

### Mechanism-level progress

1. A rank-r arbitrary full-matrix spectral addition produces at most rank r in the physical Schur residual, provided the chosen final pivot remains nonzero.
2. A small arbitrary full-rank matrix tail of operator norm `delta<|a0|` has the explicit Schur price

   `eps=delta(1+||b0||/|a0|)^2/(1-delta/|a0|)`.

3. Applying the assigned account03/B12 theorem gives the source-valid full-matrix stability bound (6.2).
4. Applying the newer pivot-ridge theorem reduces the needed residual redundancy from `5+r` to `3+r`, giving (6.4).
5. A genuine target-class rank-one construction shows that arbitrary spikes need not preserve a fixed low-q ridge certificate, so the exceptional/spike mechanism cannot be omitted.

### Remaining first implication

The unresolved full-target bridge is still structural: starting only from three global large eigenvalues, force either an already-paid aggregate/bank branch or a physical pivot and Schur-cross certificate with **uniform scale**. The theorem here says that once such a base certificate is found, arbitrary added large eigendirections and small tails can be transported through the square completion without any false post-rotation independence claim. It does **not** prove that the required pivot/cross certificate always exists.

Continuity is not claimed for the pivot-based bounds (6.2) or (6.4); they establish an essentially bounded density in their stated scopes.
