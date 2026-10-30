# QFORM B12: arbitrary-completion Schur-shear compiler

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-22T20:15:52Z.

attacking: a mixed-norm completion-of-squares compiler that absorbs arbitrary outside spectrum and all cross couplings once a physical rank-two core has a translation-uniform fractional trace bound; quantify exactly what local spectral reserve is sufficient and what remains unpaid.

## Status

Supporting theorem proved. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. This report proves essential boundedness in a quantitative arbitrary-completion branch; it does not prove continuity under the bare cap-one hypotheses.


## Dependencies actually read

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, complete supporting proof at
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   Its exact input used below is
   \[
   \sup_t \mathbb E\,|Y^T B Y+\ell^T Y-t|^{-1/2}
      \le 128\,|\det B|^{-1/4}
   \]
   for two independent cap-one coordinates `Y`, every invertible symmetric `2x2` matrix `B`, and every affine vector `ell`.

2. Assigned partner fleet04/B12 result `QFORM mixed-norm shear compiler`, complete supporting proof at
   `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260922T192552Z-fleet04-B12-mixed-shear-r1/REPORT.md`.
   If `(U,Z)` has joint density `h` and
   \[
   M(h)=\int \operatorname*{ess\,sup}_u h(u,z)\,dz<\infty,
   \]
   then for every measurable `psi`,
   \[
   \|p_{U+\psi(Z)}\|_\infty\le M(h).
   \]
   No independence of `U` and `Z` is required.

3. For the zero-diagonal comparison branch only, the full-matrix indefinite-pair theorem at
   `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

## Lemma 1: a cap-one translated square gives the exact half-Riesz kernel

Let `V` have a density bounded by one. For every `a != 0` and every shift `c`, the law of
\[
W=a(V+c)^2
\]
has density bounded by
\[
q(w)\le |a|^{-1/2}|w|^{-1/2}
\]
on the appropriate half-line (and zero on the other half-line).

Indeed, for `a>0`, the two inverse branches give
\[
q(w)=\frac{f(-c+\sqrt{w/a})+f(-c-\sqrt{w/a})}{2\sqrt{aw}}
\le \frac1{\sqrt{aw}},\qquad w>0,
\]
and reflection handles `a<0`. The estimate is uniform in the shift, so the shift may depend arbitrarily on variables on which we condition.

## Theorem 2: QFORM-ARBITRARY-COMPLETION-SCHUR-SHEAR-v1

Let `X_1,...,X_n` be independent with densities at most one and let `A` be any real symmetric matrix. Choose three ORIGINAL coordinates `I={i,j,k}`. Put
\[
M=A[I,I].
\]
Assume
\[
a=A_{ii}\ne0,\qquad \det M\ne0.
\]
Then `Q=X^TAX` has an essentially bounded density and
\[
\boxed{\|p_Q\|_\infty\le128\,|a\det M|^{-1/4}.}
\]
There is no condition whatsoever on the remaining principal block, on the cross couplings to the remaining coordinates, on the number or signs of the remaining eigenvalues, or on their magnitudes.

### Proof

Reorder the original coordinates as `(x,y,z)`, where `x=X_i`, `y=(X_j,X_k)` and `z` contains all remaining original coordinates. Write
\[
A=\begin{pmatrix}
 a&r^T&s^T\\
 r&C&L\\
 s&L^T&D
\end{pmatrix}.
\]
Complete the square only in the ORIGINAL coordinate `x`:
\[
Q=a\Bigl(x+a^{-1}(r^Ty+s^Tz)\Bigr)^2
  +y^TBy+2y^TGz+z^TEz,
\]
where
\[
B=C-a^{-1}rr^T,\qquad
G=L-a^{-1}rs^T,\qquad
E=D-a^{-1}ss^T.
\]
The `3x3` Schur determinant identity is
\[
\det M=a\det B,
\]
so `B` is invertible.

Fix `z`. Condition further on `y`. By Lemma 1, the conditional density contributed by the completed `x`-square is bounded by
\[
|a|^{-1/2}\,|t-(y^TBy+2y^TGz)|^{-1/2}.
\]
Average over the two independent cap-one coordinates in `y`. The rank-two affine half-Riesz theorem applies with affine vector `2Gz` and gives, uniformly in `z` and `t`,
\[
\|p_{U\mid Z=z}\|_\infty
 \le128\,|a|^{-1/2}|\det B|^{-1/4},
\]
where
\[
U=a\Bigl(x+a^{-1}(r^Ty+s^Tz)\Bigr)^2+y^TBy+2y^TGz.
\]
Let `g(z)` be the product density of the outside ORIGINAL coordinates. The joint density `h(u,z)=g(z)p_{U|Z=z}(u)` therefore obeys
\[
M(h)=\int \operatorname*{ess\,sup}_u h(u,z)\,dz
\le128\,|a|^{-1/2}|\det B|^{-1/4}.
\]
Now apply the completed fleet04/B12 mixed-norm shear theorem with
\[
\psi(z)=z^TEz.
\]
It yields the actual target inequality
\[
\|p_Q\|_\infty\le128\,|a|^{-1/2}|\det B|^{-1/4}.
\]
Finally `det M=a det B`, hence
\[
|a|^{-1/2}|\det B|^{-1/4}
 =|a\det M|^{-1/4}.
\]
This proves the theorem. No rotated coordinate was ever declared independent. QED.

## Corollary 3: literal arbitrary-completion stability

Fix a symmetric `3x3` matrix `M` with `det M != 0` and a diagonal entry `a=M_ii !=0`. For every `m>=0`, every real `3xm` matrix `C`, and every symmetric `mxm` matrix `D`, let
\[
A=\begin{pmatrix}M&C\\ C^T&D\end{pmatrix}.
\]
Then for every product cap-one input law,
\[
\boxed{\|p_{X^TAX}\|_\infty\le128|a\det M|^{-1/4}.}
\]
Thus an arbitrary number of added directions, with arbitrary signs and arbitrarily large or small resulting eigenvalues, together with arbitrary cross coupling to the protected three physical coordinates, costs exactly zero once the physical core is fixed. This is a genuine dependent-remainder statement, not convolution.

## Corollary 4: perturbative spectral-leverage price on the protected core

Let `M_0` be a protected `3x3` core, choose pivot `i`, and set
\[
a_0=(M_0)_{ii},\qquad \sigma_0=\sigma_{\min}(M_0).
\]
Let the final matrix have core `M=M_0+F` with
\[
\|F\|_{op}\le\delta<\min(|a_0|,\sigma_0).
\]
All outside coefficients and cross couplings remain unrestricted. Weyl gives
\[
|M_{ii}|\ge |a_0|-\delta,
\qquad
|\det M|\ge(\sigma_0-\delta)^3.
\]
Therefore
\[
\boxed{
\|p_Q\|_\infty
\le128\bigl[(|a_0|-\delta)(\sigma_0-\delta)^3\bigr]^{-1/4}.
}
\]
For a spectral perturbation `F_full=sum_r tau_r v_r v_r^T`, its compression to the protected core satisfies
\[
\|F\|_{op}
\le\sum_r |\tau_r|\,\|(v_r)_I\|_2^2.
\]
Hence even arbitrarily large added eigenvalues are harmless if their total weighted physical-core leverage stays below `delta`; their signs do not matter.

For the normalized core `M_0=diag(1,1,-1)` and `delta=1/2`, the conclusion is the explicit universal branch
\[
\boxed{\|p_Q\|_\infty\le256.}
\]

## Corollary 5: every nonsingular physical triple is at least an A-dependent bounded-density certificate

Under the target hypothesis `s_3(A)>=1`, let `M=A[I,I]` be any nonsingular original-coordinate `3x3` principal block.

If some diagonal entry of `M` is nonzero, Theorem 2 applies.

If every diagonal entry is zero, write
\[
M=\begin{pmatrix}0&b&c\\b&0&d\\c&d&0\end{pmatrix}.
\]
Then `det M=2bcd !=0`, so some off-diagonal entry, say `b`, is nonzero and the corresponding physical pair `[[0,b],[b,0]]` is invertible indefinite with `D=b^2` and `kappa=|b|`. The full-matrix indefinite-pair theorem therefore gives
\[
\|p_Q\|_\infty
\le3\,400^{1/3}|b|^{-5/6}.
\]
Choosing the largest of `|b|,|c|,|d|` and using `max>= (|det M|/2)^{1/3}` yields
\[
\|p_Q\|_\infty
\le3\,400^{1/3}(|\det M|/2)^{-5/18}.
\]
This is not a universal bound because a nonsingular physical triple may be arbitrarily ill-conditioned; it is an exact reduction of the remaining universal problem to quantitative aggregation of many small physical certificates.

## Stress test: why this does not close the full conjecture

For the standard singleton-plus-two-banks family
\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m),
\]
whose nonzero spectrum is exactly `{1,1,-1}`, take one physical coordinate from each block. Then
\[
M=\operatorname{diag}(1,1/m,-1/m),\qquad |a\det M|=m^{-2}.
\]
Theorem 2 gives `128 sqrt(m)`, and the obvious definite physical pair gives `pi sqrt(m)`. Both diverge although other completed aggregate arguments control this family uniformly. So the theorem correctly exposes, rather than hides, the remaining unpaid implication: product mass from many small coordinates must be aggregated before reciprocal local curvature is paid.

## Exact remaining implication

The additional-eigenvalue problem is now closed in the following precise local sense: once a physical `3x3` core has a nonzero pivot and nonzero determinant, every outside quadratic coefficient and cross coupling is absorbed with no extra price. The full target still requires an exhaustive, dimension-free mechanism producing either

1. a protected physical core with `|A_ii det A[I,I]|` bounded below by a universal constant,
2. a quantitatively useful indefinite physical pair covered by the full-matrix pair theorem, or
3. an aggregate/grouped-coordinate certificate that pays many small local determinants before inversion.

The singleton-plus-two-banks stress test shows (1) or (2) alone cannot be forced with a universal scale. The next B12 attack should therefore use the fleet04/B12 mixed norm on a grouped/bank statistic rather than select one physical triple.

## Regularity and integrity

The theorem proves existence of an essentially bounded density. A continuous representative is NOT established under arbitrary cap-one input densities; the partner's mixed translation-modulus condition is not proved here.

No Gaussianity, moments, compact support, connected support, log-concavity, diagonal-basis independence, pointwise oscillatory decay, worst conditional-fiber cap, or arbitrary-joint coarea bound is used. Repository transport occurred, but no authenticated native receiver-context retrieval occurred: `WITHOUT_VERIFIED_BRAIN`.
