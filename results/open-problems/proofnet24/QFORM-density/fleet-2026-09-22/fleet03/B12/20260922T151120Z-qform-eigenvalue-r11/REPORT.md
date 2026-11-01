# fleet03/B12 — hybrid cross-leakage stability and signed-sea additional-eigenvalue control

**Run:** `20260922T151120Z-qform-eigenvalue-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_STABILITY_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and current correction discipline

The full target remains OPEN: for every dimension `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one dimension-free universal `L^infinity` bound, or give a valid counterexample. Continuity is a separate desired conclusion.

Fresh control immediately before publication was read at `yspennstate/math-research-brain@d178e8c7b67bacc0328a928ed2807401e901b7a0`; revision remains `2026-09-22.5`. I also re-read the live correction inbox after the new `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` correction appeared. None of the results below uses law-uniform pointwise van-der-Corput decay, independence after spectral rotation, naive fiber-supremum integration, a fixed cross minor as a universal extractor, or the refuted single-Schur rank-two dichotomy.

The purpose of this run is narrower and source-valid: once an original-coordinate smoothing certificate exists, price additional eigen-directions by **how much cross geometry they actually destroy**, rather than charging every large added eigenvalue one full cancellation direction. A second theorem prices a large favorable-sign spectral sea at zero inside a definite physical triple.

## 2. Completed source results actually applied

### 2.1 Reviewed regularized determinant theorem

From

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`,

if an original-coordinate cross block `B=A[I,J]` has five singular values at least `mu>0`, then for every admissible product source the law of `X^TAX` has a continuous density and

`||p||_infinity <= 5e/(2 mu)`.                                           (2.1)

This theorem already absorbs arbitrary self blocks, outside coordinates/couplings, signs and affine terms. It does not require independence of spectral coordinates.

### 2.2 Same-assignment completed B12 cancellation theorem

I apply the completed fleet02/B12 result

`yspennstate/math-open-problems@51c1d2f97802864da12b41a01e2555a248bea060`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T144812Z-qform-extraeig-r11/REPORT.md`.

Its exact rank-cancellation inequality is: if `rank(R)<=r`, then for any physical cross block

`s_5(B0+R[I,J]) >= s_{5+r}(B0)`.                                         (2.2)

That source then allows an operator-norm tail. Here I strengthen the interface by splitting the remaining additions into an **arbitrarily high-rank, arbitrarily high-magnitude cross-leakage part** and a small operator-norm tail.

### 2.3 Completed fleet04 dependent-square theorem

The assigned fleet04/B12 path still had no current QFORM handoff or canonical QFORM report at the fresh source-bound read, so no fleet04/B12 theorem can honestly be claimed. The compatible completed fleet04 result actually used is fleet04/B18:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

It proves: if a scalar random variable `R` has density bounded by `M` and the conditional law of `V|R=r` has density at most one, with no independence assumed, then

`||p_{R+aV^2}||_infinity <= 2 sqrt(M/|a|)`.                              (2.3)

Section 5 below applies (2.3) to the new cross-leakage certificate, producing a new end-to-end dependent smoothing inequality.

### 2.4 Previous fleet03/B12 physical-three-block theorem

The preceding B12 report

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`

proved that a physical `3x3` block having two same-sign eigenvalues of magnitude at least `L` and an arbitrary third eigenvalue gives

`||p||_infinity <= C_*/L`,

where

`C_* = C_3 + sqrt(C_3^2+3 pi^2) = 24.183038289961516...`,
`C_3 = 2pi+3sqrt(3)`.                                                     (2.4)

This is used in Section 4.

## 3. Hybrid rank + cross-leakage + small-tail stability

Let `I,J` be disjoint sets of original coordinates. For a symmetric matrix `G`, define its cross leakage across this physical cut by

`ell_{I,J}(G) := ||G[I,J]||_op`.                                         (3.1)

Unlike `rank(G)`, this can be zero for a perturbation containing arbitrarily many huge eigenvalues.

### Theorem 3.1 — `QFORM-CROSS-HYBRID-SPIKE-TAIL-STABILITY-v1`

Let `A0,R,G,S` be real symmetric matrices and let `r>=0`. Assume

`s_{5+r}(A0[I,J]) >= sigma > 0`,                                         (3.2)

`rank(R)<=r`,                                                            (3.3)

`ell_{I,J}(G) <= eta`,                                                   (3.4)

`||S||_op <= delta`,                                                     (3.5)

and

`mu := sigma-eta-delta > 0`.                                             (3.6)

Put

`A=A0+R+G+S`.

Then the final physical cross block has

`s_5(A[I,J]) >= mu`,                                                     (3.7)

and therefore, for every admissible product source,

`||p_{X^TAX}||_infinity <= 5e/(2mu)`.                                   (3.8)

The resulting density has a continuous representative vanishing at infinity.

#### Proof

Write

`B0=A0[I,J]`, `R0=R[I,J]`, `G0=G[I,J]`, `S0=S[I,J]`.

Restriction cannot increase rank or operator norm, hence

`rank(R0)<=r`, `||S0||_op<=delta`.

Apply the completed B12 rank-cancellation inequality (2.2):

`s_5(B0+R0) >= s_{5+r}(B0) >= sigma`.                                    (3.9)

Now use the 1-Lipschitz property of each singular value in operator norm:

`s_5(B0+R0+G0+S0)`
` >= s_5(B0+R0)-||G0+S0||_op`
` >= sigma-||G0||_op-||S0||_op`
` >= sigma-eta-delta = mu`.                                              (3.10)

Apply (2.1) to the **final** cross block. No output variable is decomposed into independent summands. QED.

### 3.2 Spectral spike form of the leakage ledger

Suppose the high-rank piece is supplied spectrally as

`G = sum_{j in K} tau_j v_j v_j^T`,                                     (3.11)

with orthonormal or merely unit vectors `v_j`; no restriction on the signs or magnitudes of `tau_j` is needed. Then

`G[I,J] = sum_j tau_j (v_j)_I (v_j)_J^T`,

so

`eta = ||G[I,J]||_op`
` <= sum_j |tau_j| ||(v_j)_I||_2 ||(v_j)_J||_2`.                         (3.12)

Thus each additional eigen-direction pays its **actual weighted cross angle**, not one unit of cancellation rank. An eigenvector supported entirely on `I`, entirely on `J`, or entirely outside `I union J` costs exactly zero regardless of eigenvalue magnitude. Arbitrarily many such directions are free.

Equation (3.12) is only a convenient computable upper bound; the sharper quantity is the operator norm of the signed aggregate cross leakage, so cancellations between added directions may be retained rather than discarded.

### 3.3 Strict strengthening over rank-only pricing

Theorem 3.1 and the completed rank-only theorem are complementary rather than redundant. For example, start with a five-direction certificate `s_5(B0)>=sigma`. Add an arbitrary number `N` of spectral directions of arbitrarily large magnitude whose eigenvectors are supported on one bank of the certified cut. Their total rank may be `N`, but `eta=0`; Theorem 3.1 keeps the same five-direction certificate with no `+N` redundancy requirement. A rank-only guarantee would need `5+N` certified base directions in the worst case.

More generally, if the large added directions have total weighted leakage `eta << sigma`, they cost only `eta` in singular-value scale, not their count.

## 4. Favorable-sign spectral seas are free around a definite physical triple

The previous cross theorem prices additions by cross leakage. There is a distinct Loewner branch in which an arbitrarily large spectral sea of one sign costs exactly zero.

### Theorem 4.1 — `QFORM-DEFINITE-TRIPLE-SIGNED-SEA-SPIKE-TAIL-v1`

Let `T` be three original coordinates. Fix `epsilon in {+1,-1}` and suppose

`epsilon A0[T,T] >= L I_3`                                              (4.1)

for some `L>0` in Loewner order.

Let

`A = A0 + epsilon P + R + S`,                                           (4.2)

where

`P>=0` is an arbitrary positive-semidefinite global matrix of any rank and norm,

`rank(R)<=1` with arbitrary sign and magnitude,

and

`||S||_op<=delta<L`.                                                     (4.3)

Then every admissible product source satisfies

`||p_{X^TAX}||_infinity <= C_*/(L-delta)`,                              (4.4)

with `C_*` from (2.4).

No assumption is made on any coefficient outside the physical triple.

#### Proof

On the triple,

`epsilon(A0[T,T] + epsilon P[T,T] + S[T,T])`
` = epsilon A0[T,T] + P[T,T] + epsilon S[T,T]`
` >= (L-delta) I_3`.                                                     (4.5)

Set the matrix in (4.5) equal to `H`. The remaining perturbation on the triple is `epsilon R[T,T]`, of rank at most one. For a Hermitian rank-one perturbation, eigenvalue interlacing gives

`lambda_2(H+epsilon R[T,T]) >= lambda_3(H) >= L-delta`.                  (4.6)

Therefore the final physical triple has at least two eigenvalues of sign `epsilon` and magnitude at least `L-delta`; its third eigenvalue is unrestricted. Apply the proved physical-three-block theorem (2.4), then condition on all outside original coordinates so outside couplings become affine tilts. QED.

### Interpretation

A definite physical smoothing triple survives simultaneously:

1. **arbitrarily many arbitrarily large added eigenvalues of the favorable sign** through `epsilon P`;
2. **one completely arbitrary eigen-direction**, even of the opposite sign and arbitrarily large magnitude, through `R`;
3. **an arbitrary cloud of smaller eigenvalues of either sign** through the operator-norm tail `S`.

The dependence warning is fully respected: the proof is a final-matrix physical-block argument, not a convolution argument for separate quadratic summands.

### Corollary 4.2 — signed-sea pair stability

If instead a physical pair satisfies `epsilon A0[T,T]>=L I_2` and

`A=A0+epsilon P+S`, `P>=0`, `||S||_op<=delta<L`,

then the final pair remains definite with gap `L-delta`, so original-coordinate conditioning and the two-square shell-area bound give

`||p||_infinity <= pi/(L-delta)`.                                       (4.7)

This corollary permits an arbitrary-rank favorable-sign sea and an arbitrary small unfavorable tail, but no unpriced arbitrary spike. It proves an essentially bounded density; continuity is not asserted from this argument alone.

## 5. Applying the completed fleet04 result: pivot + hybrid residual certificate

This section turns Theorem 3.1 into a dependent end-to-end smoothing statement by applying fleet04/B18's theorem (2.3), not merely citing it.

Fix one original coordinate `k` with

`a=A_kk != 0`, `b=A[-k,k]`.

Complete the square in the original coordinate:

`Q = a V^2 + R0`,

`V = X_k + a^{-1} b^T X_{-k}`,

`R0 = X_{-k}^T H X_{-k}`,

`H = A[-k,-k]-a^{-1}bb^T`.                                              (5.1)

Conditional on `X_{-k}`, `V` is a translate of `X_k`, hence has density at most one. Mixing over `X_{-k}` at fixed scalar `R0` preserves the conditional density cap required by fleet04/B18.

Assume that inside the Schur complement `H` there are disjoint original-coordinate sets `I,J subset -{k}` and a decomposition

`H=H0+R+G+S`                                                           (5.2)

such that

`s_{5+r}(H0[I,J])>=sigma`, `rank(R)<=r`,

`||G[I,J]||_op<=eta`, `||S||_op<=delta`,

`mu=sigma-eta-delta>0`.                                                 (5.3)

Theorem 3.1 applied to the residual quadratic form gives

`||p_{R0}||_infinity <= M := 5e/(2mu)`.                                 (5.4)

Now fleet04/B18's dependent-square lemma (2.3) gives

`||p_Q||_infinity`
` <= 2 sqrt(M/|a|)`
` <= sqrt(10e/(|a| mu))`.                                               (5.5)

Numerically the prefactor is

`sqrt(10e)=5.213714442179438...`.                                       (5.6)

### Theorem 5.1 — `QFORM-PIVOT-HYBRID-RESIDUAL-STABILITY-v1`

Under (5.1)--(5.3),

`||p_Q||_infinity <= 5.214 / sqrt(|a| (sigma-eta-delta))`.              (5.7)

This is an actual new application of the completed fleet04 mathematics. The residual may contain arbitrary signs, arbitrary self terms, a bounded-rank set of completely unconstrained added directions, an arbitrarily high-rank high-magnitude part paid only through cross leakage, and an arbitrary small operator-norm tail. The square pivot need not be independent of the residual after completing the square.

The conclusion in (5.7) is an essentially bounded density. I do not claim continuity from the dependent-square step without an additional continuity argument.

## 6. What is and is not solved

### Proved this run

1. `QFORM-CROSS-HYBRID-SPIKE-TAIL-STABILITY-v1`: rank cancellation, geometric cross leakage and a small spectral tail have an exact additive price `r` in direction count and `eta+delta` in singular-value scale; arbitrary same-bank additions cost zero.
2. `QFORM-DEFINITE-TRIPLE-SIGNED-SEA-SPIKE-TAIL-v1`: a definite physical triple tolerates an unlimited favorable-sign spectral sea, one arbitrary spike, and an arbitrary smaller both-sign tail.
3. `QFORM-PIVOT-HYBRID-RESIDUAL-STABILITY-v1`: combining the new hybrid residual certificate with fleet04/B18 yields the explicit dependent bound `sqrt(10e/(|a|mu))`.

### Not proved

The bare target hypothesis of only three global eigenvalues `|lambda|>=1` does **not** currently force any of the certificates above. In particular, live corrections exhibit rank-three star/bank families for which every fixed local principal/cross certificate degenerates while aggregate product structure still controls the law. The present theorems are therefore supporting stability interfaces, not a universal reduction.

Continuity is proved for Theorem 3.1 because the final five-cross-direction characteristic function is integrable. Continuity is **not** claimed for Theorem 4.1 or Theorem 5.1 from the present arguments; only an essentially bounded density is proved there.

### First unpaid implication and next mechanism

The first unpaid implication remains an aggregate structural passage from the three-large-eigenvalue hypothesis to a smoothing mechanism **before** paying inverse local minors. The new information is that extra spectral directions need not be classified merely by count: they can be routed into (i) a bounded-rank cancellation budget, (ii) a cross-leakage budget, (iii) a favorable Loewner sea, or (iv) a small operator-norm tail.

A next useful B12 attack is therefore an aggregate heavy/light partition theorem that bounds the total cross leakage of high-magnitude directions relative to a cut produced from the three principal large directions, while sending same-sign pieces into the free Loewner sea. This is materially different from the now-refuted attempt to extract one uniformly good local triple.

## 7. Source and integrity notes

The assigned fleet04/B12 partner still had no current QFORM artifact at the source-bound read, so none was fabricated. The closest compatible completed fleet04 theorem, fleet04/B18, was applied quantitatively in Section 5. The completed fleet02/B12 same-assignment theorem was applied in the proof of Theorem 3.1.

No Gaussian, moment, compact-support, connected-support, log-concavity, or post-rotation independence assumption was introduced. All conditioning is on original coordinates. No public release or scheduler mutation is part of this mathematical artifact.
