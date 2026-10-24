SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T00:01:48Z.
attacking: the span-aligned two-sided rank-two packet left after the exact-rank-three cross-block Fourier closure; separate a paid Schur gap from the genuinely critical self-curvature-cancellation branch.

# account03/B02 QFORM r18 — span-aligned Schur discriminator and critical cancellation

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T000148Z-account03-B02-QFORM-r18`  
**Assignment:** Integrated Fourier estimate  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** not proved on the new Schur-gap branch; the designated-partner zero-diagonal overlap remains continuous by its own theorem.

This run began under owner revision `2026-09-22.15` and was resumed in the same actual-hour run after its canonical login/start already existed. Fresh control was resolved again immediately before publication at `yspennstate/math-research-brain@272127e579949a171c7a0ebdf0945c9d57f0db8d`; no later stop was observed. The current correction set was reread. In particular I do not use law-uniform pointwise one-variable Fresnel decay, conditional-projection density caps as independence, arbitrary-joint coarea, a uniformly good local minor, or the false two-sided Gabor-line `L^2` trace.

## 1. Incoming unpaid packet

The preceding B02 result

`QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1`,

canonical source `yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,

closed every *transverse* two-sided packet. After conditioning all outside original coordinates, the only residue from that argument has the form

\[
q(z,x,y)=d z^2+2z(a^Tx+b^Ty+c)+F(x)+G(y)+2x^TBy,\tag{1.1}
\]

where `z` is one original coordinate, `x` and `y` are disjoint original-coordinate product banks, `d!=0`, `B` has exact rank two, and

\[
a\in\operatorname{Col}B,\qquad b\in\operatorname{Row}B.\tag{1.2}
\]

The same-bank quadratic-affine functions `F,G` are arbitrary. Let

\[
B=L\Sigma R^T,\qquad \Sigma=\operatorname{diag}(\sigma_1,\sigma_2),
\qquad \Delta=\sigma_1\sigma_2>0,\tag{1.3}
\]

be a thin SVD. Put

\[
\tilde a=L^Ta,\qquad \tilde b=R^Tb,
\qquad
\kappa:=\tilde b^T\Sigma^{-1}\tilde a=b^TB^+a.\tag{1.4}
\]

Because of (1.2), this scalar is intrinsic to the physical packet; no input rotation is performed.

## 2. Banked Schur-potential theorem

The old physical-two-pair theorem `QFORM-SCHUR-2PLUS1-POTENTIAL-v1` was proved at
`yspennstate/math-open-problems@1489c81e0a377fd24b1a8372944e4ca63c85b13a`.
Here I extend precisely the part needed for arbitrary product banks by paying their *two-dimensional projected-density caps*, rather than pretending the singular coordinates are independent.

### Theorem 2.1 — `QFORM-BANKED-SCHUR-2PLUS1-POTENTIAL-v1`

In (1.1), do not yet assume (1.2). Define the Schur cross block

\[
C=B-\frac{ab^T}{d}.\tag{2.1}
\]

Suppose `C` has exact rank two, with nonzero singular-value product `Delta_C`. Let the two-dimensional orthogonal projections of the `x`- and `y`-bank laws onto the left/right singular spaces of `C` have density caps `M_L,M_R`. Then `q` has an essentially bounded density satisfying

\[
\boxed{
 \|p_q\|_\infty
 \le 4^{7/4}3^{-1/4}(M_LM_R)^{1/4}
      |d|^{-1/2}\Delta_C^{-1/4}.}
\tag{2.2}
\]

For the owner's cap-one product banks, the Livshyts--Paouris--Pivovarov product-marginal theorem used in r17 gives `M_L,M_R<=2`, hence

\[
\boxed{
 \|p_q\|_\infty
 \le \sqrt2\,4^{7/4}3^{-1/4}|d|^{-1/2}\Delta_C^{-1/4}.}
\tag{2.3}
\]

This is an essential-supremum statement. This proof does **not** produce continuity.

### Proof

Complete the physical square in the *original* coordinate `z`:

\[
q=d\left(z+\frac{a^Tx+b^Ty+c}{d}\right)^2+R(x,y),\tag{2.4}
\]

where the cross block of `R` between the original banks is exactly `C`; all other terms are absorbed into arbitrary same-bank quadratic-affine phases.

Let `eta(t)=E exp(itR)`. Disintegrate each original product bank onto the corresponding two-dimensional singular subspace of `C`. The complex projected amplitudes `A_t,B_t` satisfy

\[
\|A_t\|_1,\|B_t\|_1\le1,
\qquad
\|A_t\|_2^2\le M_L,
\quad
\|B_t\|_2^2\le M_R.\tag{2.5}
\]

Two-dimensional bilinear Plancherel, with the same unnormalised Fourier convention as the predecessor proof, yields

\[
|\eta(t)|\le
\min\left\{1,
\frac{\pi\sqrt{M_LM_R}}{|t|\sqrt{\Delta_C}}
\right\}.\tag{2.6}
\]

Therefore

\[
\int_{\mathbb R}|\eta(t)|^{3/2}dt
\le6\pi\sqrt{M_LM_R}\,\Delta_C^{-1/2}.\tag{2.7}
\]

Inverse Hausdorff--Young gives a density `h` of `R` with

\[
\|h\|_3
\le3^{2/3}(M_LM_R)^{1/3}\Delta_C^{-1/3}.\tag{2.8}
\]

Conditional on `(x,y)`, the translated `z` density still has cap one, so the density of the first term in (2.4) is bounded by `|d|^{-1/2}|u|^{-1/2}` after translation. Hence

\[
p_q(s)\le |d|^{-1/2}
\int h(r)|s-r|^{-1/2}dr.\tag{2.9}
\]

For `H=||h||_3`, split at radius `rho`. Holder on the near piece and total mass one on the far piece give

\[
\int h(r)|s-r|^{-1/2}dr
\le4H\rho^{1/6}+\rho^{-1/2}.\tag{2.10}
\]

The optimum satisfies `rho^(2/3)=3/(4H)` and gives

\[
4^{7/4}3^{-3/4}H^{3/4}.\tag{2.11}
\]

Substituting (2.8) proves (2.2). The product-marginal cap `M_L,M_R<=2` gives (2.3). QED.

## 3. Exact scalar discriminator on the span-aligned residue

Under (1.2), the active two-by-two Schur block is

\[
L^TCR=\Sigma-\frac{\tilde a\tilde b^T}{d}.\tag{3.1}
\]

The matrix determinant lemma gives the exact identity

\[
\det(L^TCR)
=\Delta\left(1-\frac{\kappa}{d}\right).\tag{3.2}
\]

Thus, if `kappa!=d`, `C` has exact rank two and

\[
\Delta_C
=\Delta\left|1-\frac{\kappa}{d}\right|.\tag{3.3}
\]

Combining Theorem 2.1 with (3.3) gives

\[
\boxed{
\|p_q\|_\infty
\le \sqrt2\,4^{7/4}3^{-1/4}
\Delta^{-1/4}|d|^{-1/4}|d-\kappa|^{-1/4}.}
\tag{3.4}
\]

So the r17 span-aligned packet is not uniformly hard: every point away from the single scalar Schur relation `kappa=d` is already paid.

### Quantitative either/or

Introduce the mixed five-dimensional skeleton on the active projected variables `(z,s,r)`:

\[
\mathcal H=
\begin{pmatrix}
 d&\tilde a^T&\tilde b^T\\
 \tilde a&0&\Sigma\\
 \tilde b&\Sigma&0
\end{pmatrix}.\tag{3.5}
\]

The lower four-by-four block has determinant `Delta^2` and inverse
`[[0,Sigma^{-1}],[Sigma^{-1},0]]`, hence Schur complementation gives

\[
\boxed{\det\mathcal H=\Delta^2(d-2\kappa).}\tag{3.6}
\]

Also

\[
1=2(1-\kappa/d)-(1-2\kappa/d),
\]

so

\[
\boxed{
\max\{|d-\kappa|,|d-2\kappa|\}\ge |d|/3.}
\tag{3.7}
\]

Consequently every span-aligned packet satisfies one of two explicit alternatives:

**Schur-gap branch.** If `|d-kappa|>=|d|/3`, then (3.4) simplifies exactly to

\[
\boxed{\|p_q\|_\infty\le16\,|d|^{-1/2}\Delta^{-1/4}.}\tag{3.8}
\]

**Mixed-skeleton branch.** Otherwise `|d-2kappa|>=|d|/3`, and

\[
\boxed{|\det\mathcal H|\ge |d|\Delta^2/3.}\tag{3.9}
\]

In particular at the exact Schur-critical relation `kappa=d`, the completed-square cross block has rank one but

\[
\boxed{\det\mathcal H=-d\Delta^2\ne0.}\tag{3.10}
\]

This is the main positive reduction of the run: the entire algebraically span-aligned r17 residue is now either paid by (3.8) or carries a quantitatively nondegenerate *mixed* skeleton. There is no simultaneous Schur/mixed degeneracy.

The finite checker `check_r18.py` corroborated (3.2), the singular-product form (3.3), and (3.10) on 200 seeded random rank-two instances; maximum scaled errors were `5.019e-15`, `1.953e-14`, and `4.528e-15`. The symbolic identities above are the proof.

## 4. Why the mixed-skeleton determinant alone is NOT the missing Fourier theorem

It would be tempting to claim that (3.9) by itself forces a five-dimensional stationary-phase estimate even with arbitrary same-bank quadratic terms. That is false under the owner's source assumptions.

### Proposition 4.1 — `QFORM-MIXED-SKELETON-DETERMINANT-ONLY-L1-FALSE-v1`

Take `B=I_2`, `d=1`, `a=b=(1,0)^T`. Then `Delta=1`, `kappa=d=1`, and the mixed skeleton (3.5) has determinant `-1` by (3.10). Now choose the same-bank quadratic terms so that

\[
q_{\rm active}
=(z+x_1+y_1)^2+(x_2+y_2)^2.\tag{4.1}
\]

Its full physical five-by-five quadratic matrix has rank only two, with nonzero eigenvalues `3` and `2`, even though the mixed skeleton determinant is nonzero.

Choose all five inputs to be independent standard Gaussians. Their scalar density cap is `1/sqrt(2pi)<1`, so this is an admissible source law. The two displayed linear aggregates are independent Gaussians with variances `3` and `2`. Hence

\[
|\phi_{q_{\rm active}}(t)|
=(1+36t^2)^{-1/4}(1+16t^2)^{-1/4}
\sim \frac1{\sqrt{24}\,|t|}.\tag{4.2}
\]

Therefore

\[
\boxed{\int_{\mathbb R}|\phi_{q_{\rm active}}(t)|dt=\infty}\tag{4.3}
\]

despite `|det H|=1`.

This refutes any packet theorem of the form “nonzero mixed-skeleton determinant alone, while ignoring arbitrary same-bank curvature, implies an unweighted `L^1` characteristic-function bound.” It does **not** refute the owner's full target-wide `L^1` criterion: (4.1) has only two nonzero eigenvalues.

As a target-valid stress control, append one independent physical coordinate `w` with coefficient `+1`. The full matrix then has large eigenvalues `3,2,1`, while

\[
q_{\rm target}=w^2+(z+x_1+y_1)^2+(x_2+y_2)^2.\tag{4.4}
\]

For the same Gaussian law its characteristic function gains a third square factor and decays like `|t|^{-3/2}`, so it is in `L^1`. More generally the three aggregates in (4.4) live on disjoint original-coordinate groups; the scalar-square `L^3` theorem plus Holder controls their product. Thus (4.4) is **not** a QFORM counterexample. It shows exactly what the critical packet is missing: the global third-direction resource must be combined *before* the absolute-value/time integration, rather than inferred from the skeleton after arbitrary self-curvature is discarded.

This conclusion is consistent with the fresh account02/B03 result at
`yspennstate/math-open-problems@90b9e0b5438b950fd2a0ed054833c055fdb92967`: its target-valid no-pivot star-plus-square family has every physical cross block of rank at most two, but a mixed-hub/Fresnel aggregate recovers a uniform `|t|^{-3/2}` bound. It quantitatively shows that aggregation must precede local fractional-collision payment.

## 5. Designated partner result actually applied: a weighted collision endpoint

The designated partner `account04/B02` completed

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

canonical proof `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

which says that if the ambient form contains a nonsingular physical `3x3` principal block `D` with one exact zero diagonal, then

\[
\|p_Q\|_\infty
\le C_D:=3\,2^{2/3}|\det D|^{-1/3},\tag{5.1}
\]

and the density is continuous. I apply (5.1) to an actual integrated Fourier inequality as follows.

Let `Q'` be an independent copy. The difference density `h=p_Q*p_{-Q}` has `||h||_infinity<=C_D`. For every probability density `0<=h<=C`, splitting at `r` gives

\[
\int |u|^{-1/2}h(u)du
\le4C\sqrt r+r^{-1/2}.
\]

Optimising at `r=(4C)^{-1}` yields

\[
\mathbb E|Q-Q'|^{-1/2}\le4\sqrt{C_D}.\tag{5.2}
\]

With the Fourier convention used throughout the fleet,

\[
\int_{\mathbb R}|t|^{-1/2}|\phi_Q(t)|^2dt
=\sqrt{2\pi}\,\mathbb E|Q-Q'|^{-1/2}.\tag{5.3}
\]

Therefore the completed designated-partner theorem gives the explicit new weighted endpoint

\[
\boxed{
\int |t|^{-1/2}|\phi_Q(t)|^2dt
\le4\,2^{1/3}\sqrt{6\pi}\,|\det D|^{-1/6}
<21.881\,|\det D|^{-1/6}.}
\tag{5.4}
\]

This is a genuine inequality-level use of the partner result. It does not by itself imply global unweighted `L^1`, but it is a dimension-free collision resource available on every zero-diagonal-triple overlap.

## 6. What is paid and what remains unpaid

Paid in this run:

1. The arbitrary-bank version of the Schur `2+1` potential theorem, with projected product-law caps retained correctly.
2. Every span-aligned two-sided rank-two packet with `|d-kappa|>=|d|/3`, by the clean bound (3.8).
3. An exact algebraic dichotomy showing the complement has `|det H|>=|d|Delta^2/3`.
4. A rigorous admissible-law counterexample proving that this mixed-skeleton determinant cannot be spent while simply discarding arbitrary same-bank curvature.
5. A new weighted integrated-Fourier endpoint (5.4) obtained by actually applying the designated account04/B02 theorem.

The sharpened first unpaid implication is now:

**`QFORM-CRITICAL-ALIGNED-GLOBAL-THIRD-RESOURCE-v1` — OPEN.**  In the mixed-skeleton branch (3.9), combine the globally guaranteed third spectral direction with the aligned rank-two packet *before* taking absolute values. A valid estimate must preserve original-coordinate product provenance and survive arbitrary same-bank quadratic curvature. The rank-two self-curvature cancellation (4.1) rules out a determinant-only local stationary-phase theorem; the fresh mixed-hub result shows that a grouped third-direction/Fresnel resource can succeed. A useful endpoint would be a translation-uniform fractional-trace or grouped-coordinate inequality that reduces to the r16/r17 Fourier estimates when the third direction is transverse, and to mixed-hub aggregation in the no-pivot star family.

I did **not** obtain a target-valid counterexample to the owner's stronger global criterion `int |phi_Q(t)|dt<infinity`; that criterion remains OPEN at full scope. The full bounded-density conjecture also remains OPEN.

## 7. Sources actually consumed

- Fresh owner/control repository at publication refresh: `yspennstate/math-research-brain@272127e579949a171c7a0ebdf0945c9d57f0db8d`, owner revision `2026-09-22.15`.
- account03/B02 r17 transverse exact-rank-three cross-block theorem: `yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`.
- account03/B02 banked theorem predecessor: `yspennstate/math-open-problems@1489c81e0a377fd24b1a8372944e4ca63c85b13a`.
- designated partner account04/B02 zero-diagonal triple continuity theorem: `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`.
- fresh compatible account02/B03 mixed-hub/collision separation: `yspennstate/math-open-problems@90b9e0b5438b950fd2a0ed054833c055fdb92967`.
- r16 false Gabor-line interface retained as a correction: `yspennstate/math-open-problems@864e0222357c77d628a7e3389a32e230f30b9321`.

No paid model/API/Codex call, no remote workflow, no email/Drive/public release, and no native learned-memory receiver claim was used. Configured reasoning telemetry is unavailable and remains `UNKNOWN/null`.
