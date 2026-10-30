# fleet02/B15 — independent regularity review: rank >= 3 product quadratics have an instancewise bounded C0 density

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `fleet02/B15`  
**Run:** `20260922T213535Z-fleet02-B15-qform-r11`  
**Owner control at pre-publication refresh:** revision `2026-09-22.15`; full QFORM target active; no B15 stop observed.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The full problem is still OPEN. The first unpaid implication is purely quantitative:

\[
\boxed{
\sup_{\substack{n,\;0\le f_i\le1,\;\int f_i=1\\ A=A^T,\;s_3(A)\ge1}}
\|p_{X^TAX}\|_\infty<\infty .
}
\]

Here `s_3(A)` is the third largest singular value, equivalently the third largest absolute eigenvalue. Nothing in the regularity argument below gives a matrix-independent constant, and no continuity assertion is used to infer one.

This run independently checks the assigned partner `fleet03/B15` regularity chain and obtains a one-review supporting conclusion:

> **QFORM-RANK3-PRODUCT-C0-INDEPENDENT-REVIEW-v1.** For every fixed real symmetric `A` with `rank(A)>=3`, and every product law of independent real coordinates whose one-dimensional densities are bounded by one, `Q=X^TAX` has an essentially bounded density with a representative in `C_0(R)`. The resulting height bound may depend arbitrarily badly on `A`.

The proof is product-coordinate based. It does not use the refuted arbitrary-joint rank-three coarea estimate, a conditional projection-density moment, independence after rotation, law-uniform pointwise oscillatory decay, or a uniformly good physical minor.

## 2. Sources reviewed and actually applied

The assigned partner result under review is

- `fleet03/B15`, run `20260922T192818Z-fleet03-B15-qform-r16`, `yspennstate/math-open-problems@c2bc78fc4f8e642f5d8c85fcc7d53956730b5cb1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T192818Z-fleet03-B15-qform-r16/REPORT.md`.

Its complementary nonzero-physical-diagonal branch is

- `fleet03/B15`, run `20260922T153101Z-fleet03-B15-r12`, `yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T153101Z-fleet03-B15-r12/REPORT.md`.

The fixed-matrix bounded-density input is independently available from

- `fleet01/B15`, `yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md`.

The binary indefinite `L^3` ingredient is

- `fleet01/B11`, `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T121344Z/REPORT.md`.

For the extremal consequence in Section 8 I actually apply the completed current partner result

- `fleet03/B15`, run `20260922T202624Z-fleet03-B15-qform-r17`, `yspennstate/math-open-problems@fd40f8241efcd355b798669de5a0421f8f25e1d0`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T202624Z-fleet03-B15-qform-r17/REPORT.md`,

which itself applies the completed continuous-output envelope

- `fleet04/B15`, `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`.

## 3. Absolute continuity is strictly weaker and already settled

Let `X` have any Lebesgue density on `R^n`, and let

\[
P(x)=x^TAx+2b^Tx+c,
\qquad A\ne0.
\]

The critical set `C={x:Ax=-b}` is empty or an affine subspace of positive codimension. If `N subset R` is null, define

\[
E_m=\{x\in B(0,m):P(x)\in N,\ |\nabla P(x)|\ge1/m\}.
\]

Coarea on each ball gives

\[
\int_{E_m}|\nabla P|dx
=
\int_N \mathcal H^{n-1}(E_m\cap P^{-1}(t))dt=0,
\]

so `|E_m|=0`. The union of the `E_m`, together with the null critical set, covers `P^{-1}(N)` up to null sets. Hence `P(X)` is absolutely continuous.

This requires neither rank three nor product structure. It has no quantitative `L^infinity` content. Rank one already separates the assertions: for `X~Unif[0,1]`, `X^2` is absolutely continuous but has density `1/(2sqrt(t))`, unbounded at zero.

## 4. Instancewise L-infinity for rank at least three

A symmetric matrix of rank at least three has an invertible original-coordinate principal submatrix of order three or four. The proof is symmetric pivot elimination. Starting with a nonzero diagonal `1x1` pivot when available, or an off-diagonal invertible block `[[0,a],[a,0]]` otherwise, take Schur complements. A nonzero Schur complement either has a nonzero diagonal and extends the principal pivot by one coordinate, or has zero diagonal and a nonzero off-diagonal entry and extends it by two. The first accumulated pivot size reaching three is therefore three or four.

For an invertible physical block `B`, the completed finite-dimensional bounds give, uniformly over affine terms,

\[
\|p\|_\infty\le {2\pi+3\sqrt3\over\sigma_{\min}(B)}\quad(d=3),
\]

and

\[
\|p\|_\infty\le {4\pi+8\over\sigma_{\min}(B)}\quad(d=4).
\]

Conditioning on all coordinates outside the selected original-coordinate block preserves independence of the selected coordinates and changes only affine/constant terms. Averaging the conditional measures gives a finite matrix-dependent height bound for every fixed rank-`>=3` `A`.

This already proves

\[
\boxed{
\operatorname{rank}(A)\ge3
\Longrightarrow
p_{X^TAX}\in L^\infty(\mathbb R)
\text{ for each fixed }A,
}
\]

but the physical-block singular value can tend to zero along valid target matrices. Thus this is not the universal theorem.

## 5. Independent audit of the nonzero-diagonal C0 branch

Assume an invertible selected physical block `B` of order `d=3` or `4` has a nonzero physical diagonal pivot `b`. After permuting coordinates and translating the original independent variables,

\[
Y^TBY=R(U)+b\,(Z+M(U))^2,
\]

where `R(U)=U^TSU`, `S` is the invertible Schur complement and `M` is linear.

The reviewed proof needs two facts.

First, `p_R in L^3`. For `d=3`, `S` is binary. If it is indefinite, the determinant-scale theorem gives

\[
\|p_R\|_3\le C_{bin}(-\det S)^{-1/3};
\]

if definite, the two-dimensional quadratic height bound gives `p_R in L^infinity`, hence in `L^3` because it has mass one. For `d=4`, the three-variable physical-block theorem gives `p_R in L^infinity`, again hence in `L^3`.

Second, when `M` is nonzero, the map

\[
\Psi(u)=(R(u),M(u))=(u^TSu,v^Tu)
\]

has rank below two only when `Su` is parallel to `v`, i.e. on the one-dimensional subspace `S^{-1}(span(v))`, a null set in dimensions two or three. Coarea therefore gives an absolutely continuous joint law `(R,M)` with density `H(r,m)`. Adding the independent pivot coordinate gives

\[
K(r,z)=\int H(r,m)f_Z(z-m)dm,
\]

so for almost every `r`, `K(r,.) in C_0`, and, crucially,

\[
0\le K(r,z)\le\int H(r,m)dm=p_R(r).
\]

For `T=R+bV^2`, one-dimensional change of variables then gives

\[
p_T(t)\le |b|^{-1/2}
\int_{\operatorname{sgn}(b)(t-r)>0}
{p_R(r)\over\sqrt{|t-r|}}dr.
\]

Writing `M_3=||p_R||_3`, split at distance `L`. Holder gives

\[
\int_0^L p_R(t-s)s^{-1/2}ds
\le4^{2/3}M_3L^{1/6},
\]

while the far part is at most `L^{-1/2}`. Taking `L=1/(4M_3^{3/2})` yields

\[
\boxed{
\|p_T\|_\infty\le4|b|^{-1/2}M_3^{3/4}.
}
\]

For continuity, fix `delta>0`. Away from the moving square-root endpoint, continuity of `K(r,.)` and the envelope by `p_R` give dominated convergence. The endpoint contribution is uniformly `O(M_3 delta^{1/6})`. Letting first `t_n->t` and then `delta->0` proves continuity. The same split at large `|t|`, with the near part controlled by the local `L^3` mass of `p_R`, proves `p_T(t)->0`. The uncoupled case is an ordinary `L^3 * L^{3/2}` convolution and is also in `C_0`.

Starting the principal-pivot extension from a prescribed nonzero physical diagonal produces an invertible 3- or 4-block containing that diagonal. Conditioning outside it therefore proves

\[
\boxed{
\operatorname{rank}(A)\ge3,\;\exists j:A_{jj}\ne0
\Longrightarrow p_Q\in C_0\cap L^\infty.
}
\]

I find no gap in this branch.

## 6. Independent audit of the zero-diagonal branch

Assume now `diag(A)=0`, `rank(A)>=3`.

### 6.1 Triangle branch

If the physical support graph contains a triangle, the selected three-coordinate quadratic part is

\[
q(x,y,z)=2axy+2bxz+2cyz,
\qquad abc\ne0,
\]

plus arbitrary affine terms after conditioning outside.

The first delicate estimate is the exact product-variation kernel. Let `0<=h<=1` have mass `delta`, let `0<=g<=1` have mass one, and let

\[
k(s)=\int h(u)g(s/u){du\over|u|}.
\]

For any `r>0`, on `|u|>=r` the cap-one bathtub bound is

\[
\int_{|u|\ge r}h(u){du\over|u|}
\le2\log(1+\delta/(2r)).
\]

On `|u|<r`, substitute `v=s/u`; the same cap-one bathtub bound for `g` gives

\[
\int_{|u|<r}h(u)g(s/u){du\over|u|}
\le2\log(1+r/(2|s|)).
\]

With `r=sqrt(delta|s|)` the terms match, hence

\[
\boxed{
k(s)\le\Phi_\delta(s):=
4\log\!\left(1+{1\over2}\sqrt{\delta/|s|}\right).}
\]

The second delicate estimate averages this logarithmic singularity. If

\[
P(|W|\le\rho)\le\min(1,L\sqrt\rho),
\]

then, with

\[
\Omega(a)=2a\log(1+2/a)+4\log(1+a/2),
\]

integration by parts gives

\[
\boxed{E\Phi_\delta(W)\le\Omega(L\sqrt\delta).}
\]

Indeed after scaling `R=|W|/delta`, putting `a=Lsqrt(delta)`, and then `x=sqrt(R)`, the exact integral is

\[
\int_0^\infty {4\min(1,ax)\over x(2x+1)}dx
=
2a\log(1+2/a)+4\log(1+a/2).
\]

Completing the triangle as `2aUV+H(z)` leaves a one-dimensional quadratic `H` with nonzero quadratic coefficient. Therefore the moving singular value `W=(t-H(Z))/(2a)` obeys the required square-root small-ball estimate. Replacing one triangle marginal at `L^1` distance `delta` changes the output density by a quantity of order

\[
{1\over2|a|}\Omega\!\left(
{2\sqrt2|a|\over\sqrt{|bc|}}\sqrt\delta
\right),
\]

with the symmetric analogues for the other coordinates. This tends to zero as `delta->0`. Setting `delta=1` also supplies a finite conditional height, so every outside marginal is `L^1`-Lipschitz at the output-density level.

All constants here are matrix-dependent, which is allowed for this regularity theorem.

### 6.2 Triangle-free branch

If the zero-diagonal support graph is triangle-free, choose a nonzero edge `{i,j}`. Its `2x2` pivot

\[
P=\begin{pmatrix}0&a\\a&0\end{pmatrix}
\]

is invertible. The Schur complement has rank at least one. Triangle-freeness forces every diagonal entry of that Schur complement to vanish; hence it has a nonzero off-diagonal edge `{k,l}`. The resulting principal four-block is invertible. Its triangle-free support graph is bipartite, and invertibility rules out a `1+3` bipartition, so after permutation it has the form

\[
B=\begin{pmatrix}0&C\\ C^T&0\end{pmatrix},\qquad C\in GL_2.
\]

Translations in the two original-coordinate pairs remove affine terms and leave `2U^TCV` up to an output translation.

For fixed `u`, the scalar linear form in the independent pair `V` has coefficient vector `2C^Tu`. The standard two-coordinate projection bound is

\[
\|p_{2u^TCV}\|_\infty\le{1\over\sqrt2\,\|C^Tu\|}.
\]

For any planar subdensity `0<=F<=1` of mass `delta`, the radial bathtub principle gives exactly

\[
\int {F(u)\over|u|}du\le2\sqrt{\pi\delta}.
\]

Since `||C^Tu||>=sigma_min(C)|u|`, replacing one of the four block marginals at `L^1` distance `delta` changes the output density by at most

\[
\boxed{
{\sqrt{2\pi\delta}\over\sigma_{\min}(C)}.
}
\]

Again `delta=1` gives a finite affine-uniform block height and hence `L^1`-Lipschitz control for every outside marginal.

I find no gap in the graph reduction, the projection constant, or the planar bathtub step.

### 6.3 Rough inputs by uniform output convergence

Approximate each cap-one marginal in `L^1` by compactly supported smooth cap-one probability densities. For the all-smooth approximants, the output density is in `C_0` by the completed smooth-output theorem. Telescope the marginals using the triangle or bilinear-block moduli above. This makes the smooth output densities uniformly Cauchy. Their uniform limit `p` is in `C_0`.

The product input laws converge in total variation, hence their quadratic pushforwards converge in total variation. The same pushforwards also converge to `p(t)dt` because of the uniform density convergence on compact intervals plus total mass one; therefore `p` is a density of the original rough output.

Thus

\[
\boxed{
\operatorname{diag}(A)=0,\;\operatorname{rank}(A)\ge3
\Longrightarrow p_Q\in C_0\cap L^\infty.
}
\]

Combining Sections 5 and 6 proves the reviewed rank-`>=3` product regularity theorem.

## 7. Exact implication ledger

The mathematical implications now supported by the reviewed chain are:

1. `A!=0` plus any absolutely continuous joint input law implies absolute continuity of `X^TAX`. This is qualitative and much weaker than the target.
2. Independent cap-one inputs plus `rank(A)>=3` imply an individually bounded density with a `C_0` representative. The bound may depend on `A`.
3. A dimension- and matrix-independent `L^infinity` constant is still OPEN. Neither continuity nor the existence of an instancewise bound supplies it.

The thresholds cannot be conflated. Rank one gives absolute continuity with an unbounded density (`X^2` for a uniform input). Rank two positive definite product examples can have a bounded but discontinuous density, while rank-two opposite-sign examples exhibit the familiar logarithmic singularity. The rank-three result above is therefore a genuinely stronger product-regularity statement, not a repackaging of absolute continuity.

## 8. Completed partner application: exact continuous-output normal form for the full height problem

The completed `fleet03/B15` r17 theorem gives an exact target-level normalization. Define

\[
M(A,f)=\sup_I {P(X^TAX\in I)\over |I|}.
\]

For `s=s_3(A)>=1` and `B=A/s`,

\[
\boxed{s_3(B)=1,\qquad M(B,f)=sM(A,f).}
\]

Thus normalization to the exact spectral boundary cannot reduce a bad height.

Combining this with the completed continuous-output envelope and algebraic genericization gives, including the value `+infinity`,

\[
\boxed{C_{all}=C_{C_0}=C_{sm}=C_{norm},}
\]

where `C_norm` is the supremum over compactly supported smooth cap-one product inputs, exact `s_3(A)=1`, continuous `C_0` outputs, and any prescribed finite homogeneous algebraic genericity package.

This is the key application to the unresolved universal theorem: **continuity is extremally harmless but quantitatively powerless by itself.** If the universal conjecture is false, there exists a source-valid counterexample sequence entirely inside that smooth normalized class, with actual attained continuous peaks tending to infinity. Conversely, proving one uniform height bound on that normalized continuous-output class proves the full rough-input conjecture.

Therefore the first unpaid implication may be sharpened to

\[
\boxed{
\sup_{\substack{f_i\in C_c^\infty,\ 0\le f_i\le1\\ s_3(A)=1,\;A\text{ homogeneous-algebraically generic}}}
\max_t p_{X^TAX}(t)<\infty,
}
\]

uniformly all the way to every physical near-degeneracy. Any proof that pays an uncancelled reciprocal local minor is still insufficient.

## 9. Corrections and integrity

Consumed and respected before publication:

- `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`;
- `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`;
- `QFORM-POINTWISE-DECAY-FALSE`;
- `QFORM-FIBER-SUP-DIMENSION-LOSS`;
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`;
- the current `QFORM-PARTNER-L2-COMPILER-HOMOGENEITY-FALSE-v1` correction, which is unrelated to and unused by this review.

No arbitrary-joint coarea estimate is smuggled into the proof. Every smoothing/conditioning step retains original-coordinate product provenance. No moment, bounded support, connected support, log-concavity, Gaussianity, or rotated-independence assumption is added.

**Review status:** independent mathematical PASS of the `fleet03/B15` r12+r16 regularity chain, with the full QFORM universal-height conjecture still OPEN. Shared claim promotion remains a consolidation action for the owner/B20; this worker does not edit shared control state.

No novelty or publication-priority claim is made.
