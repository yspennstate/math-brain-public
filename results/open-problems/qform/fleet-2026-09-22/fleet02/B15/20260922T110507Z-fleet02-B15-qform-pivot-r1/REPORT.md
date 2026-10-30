# fleet02/B15 — principal-triple conditioning theorem and delocalized rank-three obstruction

**Run:** `20260922T110507Z-fleet02-B15-qform-pivot-r1`  
**Live owner target:** `Quadratic_Form_Bounded_Density_Conjecture` under OWNER CONTROL revision `2026-09-22.4`  
**Classification:** `SUBSTANTIVE_PARTIAL_THEOREM / MECHANISM_OBSTRUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full conjecture:** **OPEN / NOT PROVED**.

## 0. Control pivot and source use

This invocation began under the superseded all-team FEI order. A later fresh protected-control reread exposed OWNER CONTROL revision `2026-09-22.4`, which immediately supersedes the FEI target and moves the entire fleet to the quadratic-form bounded-density conjecture. The earlier FEI artifacts from this invocation are retained as historical immutable work but are not treated as the live deliverable.

The live target is:

> Let `X_1,...,X_n` be independent real random variables with Lebesgue densities bounded by `1`. Let `Q(x)=x^T A x`, with `A` real symmetric and having at least three eigenvalues whose absolute values are at least `1`. Prove that `Q(X)` has a density bounded by a universal constant.

I consumed the completed fleet03/B17 report

`yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec:qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`.

That report proves two important facts used here:

1. the suggested law-uniform pointwise Fresnel decay is false: for every fixed `s!=0`, the supremum of `|int exp(isx^2)f(x)dx|` over densities `0<=f<=1` is `1`;
2. if `A` is diagonal in the original independent coordinates and has three large coefficients, then `||p_Q||_infinity<=pi`, by selecting a same-sign pair.

The new result below goes beyond the coordinate-diagonal case: it handles an arbitrary rotated nonsingular quadratic block on **three original independent coordinates**, including indefinite signature, and therefore any high-dimensional form possessing one uniformly nondegenerate principal coordinate triple. It also gives an explicit delocalized rank-three family proving that the spectral hypothesis alone cannot supply such a fixed triple.

## 1. Three-variable affine quadratic theorem

Let `B` be a real symmetric `3x3` matrix and define

`kappa = sigma_min(B) = min_j |lambda_j(B)|`.

### Theorem 1.1 — `QFORM-3VAR-AFFINE-PRINCIPAL-v1`

Let `Y_1,Y_2,Y_3` be independent real random variables, each with density bounded by `1`. If `kappa>0`, then for every `b in R^3`, `c in R`,

\[
Z=Y^T B Y+2b^T Y+c
\]

has a density satisfying

\[
\boxed{
\|p_Z\|_\infty
\le {C_3\over\kappa},
\qquad
C_3:=2\pi+3\sqrt3<11.48.
}
\tag{1.1}
\]

No sign condition on the eigenvalues is required.

### Proof

Complete the square:

\[
Y^TBY+2b^TY+c
=(Y+B^{-1}b)^TB(Y+B^{-1}b)+c-b^TB^{-1}b.
\]

Coordinatewise translation preserves independence and the density bound, and an additive scalar does not affect the density norm. Scaling `B` by `kappa` scales the output density by `1/kappa`, so it is enough to prove (1.1) when every eigenvalue of `B` has absolute value at least `1`.

Let `F(y)=f_1(y_1)f_2(y_2)f_3(y_3)`, so `0<=F<=1` and `int F=1`. Fix an interval `J` of length `eta`; it suffices to prove

\[
\Pr(Y^TBY\in J)\le C_3\eta.
\tag{1.2}
\]

Split space into

\[
N=\{y:|By|\le1\},
\qquad
N^c=\{y:|By|>1\}.
\]

### 1a. Near the critical point: exact canonical three-dimensional volume

Write the polar decomposition of the symmetric invertible matrix as

\[
B=S|B|,
\]

where `S=sign(B)` is symmetric orthogonal, commutes with `|B|`, and has eigenvalues in `{+1,-1}`. Set

\[
z=|B|^{1/2}y.
\]

Then

\[
y^TBy=z^TSz,
\qquad
 dy=(\det|B|)^{-1/2}dz\le dz,
\]

because every singular value of `B` is at least `1`. Moreover

\[
|By|^2=y^TB^2y=z^T|B|z\ge|z|^2,
\]

so `N` maps inside the unit ball. Since `F<=1`,

\[
\Pr(Y\in N,\ Y^TBY\in J)
\le
\left|\{z:|z|\le1,\ z^TSz\in J\}\right|.
\tag{1.3}
\]

Up to an orthogonal change of variables there are only two cases.

* If `S=+I` or `S=-I`, put `t=|z|^2`. The volume density is `2 pi sqrt(t)<=2 pi` on `0<=t<=1`, hence every interval of `t`-length `eta` cuts volume at most `2 pi eta`.
* If the signature is `(2,1)` or `(1,2)`, write `z^TSz=r^2-s^2`, where `r^2=z_1^2+z_2^2`. For each fixed `s in [-1,1]`, planar area is `pi d(r^2)`, so the condition `r^2-s^2 in J` cuts area at most `pi eta`. Integrating over `s` gives at most `2 pi eta`.

Therefore

\[
\boxed{
\Pr(Y\in N,\ Y^TBY\in J)\le2\pi\eta.
}
\tag{1.4}
\]

### 1b. Away from the critical point: original-coordinate monotone slicing

If `|By|>1`, then at least one coordinate satisfies

\[
|(By)_i|>{1\over\sqrt3}.
\]

For `i=1,2,3`, let

\[
E_i=\{y:Y^TBY\in J,\ |(By)_i|>1/\sqrt3\}.
\]

The far event is contained in `E_1 union E_2 union E_3`.

Condition on the other two original coordinates. As a function of `t=y_i`,

\[
g(t)=Y^TBY
\]

is a real quadratic polynomial and

\[
g'(t)=2(By)_i.
\]

On the part of the line belonging to `E_i`, `|g'(t)|>2/sqrt3`. Since the derivative of a quadratic is affine, the set `|g'|>2/sqrt3` has at most two connected components, and `g` is monotone on each. On each component, the inverse image of an interval of length `eta` has length at most

\[
{\eta\over2/\sqrt3}={\sqrt3\over2}\eta.
\]

Thus the total allowed `t`-length is at most `sqrt3 eta`. Since the conditional one-coordinate density is at most `1`,

\[
\Pr(E_i\mid Y_{\widehat i})\le\sqrt3\eta.
\]

After averaging the other two independent coordinates and summing `i=1,2,3`,

\[
\boxed{
\Pr(Y\in N^c,\ Y^TBY\in J)\le3\sqrt3\eta.
}
\tag{1.5}
\]

Combining (1.4) and (1.5) proves (1.2), hence (1.1). `QED`.

## 2. High-dimensional principal-triple corollary

### Theorem 2.1 — `QFORM-PRINCIPAL-TRIPLE-CONDITIONING-v1`

Let `X_1,...,X_n` be independent with densities bounded by `1`, and let `A` be any real symmetric `n x n` matrix. Suppose there is a coordinate triple `I={i,j,k}` such that the principal block

\[
B=A_{I,I}
\]

satisfies

\[
\sigma_{\min}(B)\ge\kappa>0.
\]

Then

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le{2\pi+3\sqrt3\over\kappa}.
}
\tag{2.1}
\]

### Proof

Condition on all coordinates outside `I`. For a fixed outside vector `w`, the remaining quadratic polynomial is

\[
x_I^T Bx_I+2b(w)^Tx_I+c(w).
\]

The three coordinates in `I` remain independent with their original densities bounded by `1`. Theorem 1.1 applies uniformly in `b(w),c(w)`, so the conditional output density is bounded by `C_3/kappa`. Averaging over `w` preserves the same bound. `QED`.

This is strictly stronger than the coordinate-diagonal branch: arbitrary cross-terms with the other `n-3` coordinates are allowed, and the `3x3` principal block itself may be fully rotated and indefinite.

## 3. A useful two-coordinate refinement when a definite principal pair exists

For comparison, if a `2x2` principal block `C=A_{\{i,j\},\{i,j\}}` is positive or negative definite, conditioning on all other variables and completing the square gives

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le{\pi\over\sqrt{\det C}}.
}
\tag{3.1}
\]

Indeed the conditional two-dimensional joint density is at most `1`, and after the linear transformation reducing `C` to `+I` or `-I`, the coarea density of `z_1^2+z_2^2` is exactly `pi` in the normalization used here. This recovers the diagonal same-sign-pair theorem of fleet03/B17 as a special case and allows arbitrary couplings to the conditioned coordinates.

The three-variable theorem is needed because a signature `(2,1)` block can have **every** original-coordinate principal pair indefinite. For example

\[
B=I-2vv^T,
\qquad
v=(1,1,1)/\sqrt3,
\tag{3.2}
\]

has eigenvalues `(1,1,-1)`, while every `2x2` principal determinant equals `-1/3`.

## 4. Why the owner spectral hypothesis does not yield one good coordinate triple

Theorem 2.1 does not close the full conjecture, because the three large eigendirections can be completely delocalized across the original independent coordinates.

### Proposition 4.1 — `QFORM-FLAT-RANK3-PRINCIPAL-TRIPLE-OBSTRUCTION-v1`

For infinitely many `n`, there exists a real symmetric `n x n` matrix `A` with exactly three nonzero eigenvalues, all equal to `1`, such that for **every** coordinate triple `I`,

\[
\boxed{
\sigma_{\min}(A_{I,I})\le{3\over n}.
}
\tag{4.1}
\]

Consequently, any proof that first selects one principal coordinate triple and then invokes Theorem 2.1 must lose at least order `n` on this family.

### Proof

Take an `n x n` normalized real Hadamard matrix for any admissible infinite subsequence (for example Sylvester orders `n=2^m`) and let `U` be any three orthonormal columns. Every row `u_i in R^3` then has

\[
|u_i|^2={3\over n}.
\]

Set

\[
A=UU^T.
\]

Then `A` is the orthogonal projection onto a three-dimensional subspace, hence has three eigenvalues equal to `1` and all others `0`.

For a coordinate triple `I`,

\[
A_{I,I}=U_IU_I^T\succeq0
\]

and

\[
\operatorname{tr}(A_{I,I})
=\sum_{i\in I}|u_i|^2
={9\over n}.
\]

Its three nonnegative eigenvalues therefore have minimum at most one third of their sum, proving (4.1). `QED`.

There is nevertheless an exact aggregate invariant. By Cauchy-Binet,

\[
\boxed{
\sum_{|I|=3}\det(A_{I,I})
=
\sum_{|I|=3}\det(U_I)^2
=
\det(U^TU)=1.
}
\tag{4.2}
\]

So the flat rank-three projector has no useful **single** coordinate triple, yet carries unit total determinant mass spread over many triples. This identifies a concrete next bridge: aggregate many principal-triple slice estimates without paying the reciprocal of the smallest selected local curvature.

## 5. Mechanism status and next exact obligation

The completed fleet03/B17 result rules out the naive law-uniform pointwise Fresnel envelope and closes the coordinate-diagonal branch at `pi`. The present report closes two further source-exact branches:

1. every genuine three-variable quadratic form whose three eigenvalues have magnitude at least `1`, with explicit constant `2 pi + 3 sqrt(3)`;
2. every high-dimensional form with one principal coordinate triple uniformly nonsingular, by conditioning.

The first unresolved geometry is already represented by the flat rank-three projector `A=UU^T` in Proposition 4.1. For that model,

\[
Q(X)=|U^TX|^2,
\]

where `U` has orthonormal columns and highly delocalized rows. Fixed-triple conditioning is provably dimension-losing, while the aggregate minor identity (4.2) retains a dimension-free unit resource.

A genuinely new universal step should therefore prove an **aggregate principal-triple inequality**, or an equivalent product-measure estimate for the radial pushforward of `U^TX`, which converts the Cauchy-Binet mass

\[
\sum_{|I|=3}\det(U_I)^2=1
\]

into a density/small-ball bound without selecting a single minor. Brascamp-Lieb/product-marginal inequalities or a multilinear coarea/Loomis-Whitney argument are natural candidates. The known bound `||p_{U^TX}||_infinity<=2^{3/2}` for three-dimensional marginals of product measures is not by itself enough: an arbitrary bounded three-dimensional density can concentrate on a thin spherical shell, so the proof must retain more of the product-sum structure than the marginal `L^infinity` norm alone.

Full conjecture remains **OPEN**.

## 6. Source pins and literature context

* Live target/control: owner revision `2026-09-22.4` in `yspennstate/math-research-brain`.
* Completed fleet input: `yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec:qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`.
* Livshyts–Paouris–Pivovarov (2015) prove the dimension-free marginal-density bound `2^{k/2}` for `k`-dimensional marginals of product densities bounded by one; this is relevant to the final paragraph but is not needed in the proofs of Theorems 1.1 or 2.1.

No novelty or publication-priority claim is made. The full arbitrary-eigenvector conjecture is not proved.
