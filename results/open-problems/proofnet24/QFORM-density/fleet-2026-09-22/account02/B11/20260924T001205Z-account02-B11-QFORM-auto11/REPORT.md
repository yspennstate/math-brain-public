SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-24T00:12:05Z.
attacking: QFORM-R43-NONRANKONE-OR-ALIGNED-SHAREDHUB-CURVATURE-v1; use a source-preserving L2 hyperbolic-pair estimate to pay a non-rank-one subbranch without deleting a small term.

# account02/B11 r45 — one-sided-curvature hyperbolic L2 receiver and a source-disjoint rank-two crossing closure

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: indefinite signatures / complementary constructions and source-valid obstructions.
Status: **NEW ANALYTIC RECEIVER / REAL TARGET INEQUALITY / PARTNER r44 APPLIED / FULL QFORM OPEN**.
Execution: authenticated repository retrieval and receiver use occurred in this run; `WITHOUT_VERIFIED_BRAIN` is therefore absent for this invocation.

The unrestricted theorem is still open. The result below does not assume moments, support bounds, log-concavity, identical laws, diagonalisation in the independent coordinates, or independence after a spectral rotation. Continuity is proved only for the displayed source-disjoint subclass.

## First unpaid implication

The first unpaid implication after this run is

`QFORM-R44-RANK2-CROSSING-SAMEBANK-INTERPOLATION-v1`:

> In the r43/r44 unique-heavy-row chamber, interpolate uniformly between partner r44's exact-rank-one transverse crossing receiver and a genuinely rank-two crossing when the second crossing singular value is nonzero but may tend to zero, while retaining arbitrary same-bank phases/curvature and original-coordinate product provenance. Equivalently: obtain the L2 hyperbolic-pair gain below when the two factors are projected from the same product bank, or force a source-disjoint physical-pair/volume/square exit.

The new theorem pays the corresponding rank-two crossing when the two hyperbolic pairs can be made genuinely source-disjoint and curvature is one-sided on each pair. It does **not** replace a same-bank projected pair by an arbitrary joint density.

## 1. Universal L2 bound for one hyperbolic pair with arbitrary one-sided curvature

### Theorem 1 — `QFORM-HYPERBOLIC-PAIR-L2-ONE-SIDED-CURVATURE-v1`

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying

`||f||_infinity <= F`, `||g||_infinity <= G`.

Let `c != 0`, `d` be real, and let `R` be an arbitrary measurable real function. Put

`W = c X Y + d Y + R(X)`.

Then `W` has a density `p_W` in `L2(R)` and

\[
\boxed{
\|p_W\|_2^2\le \frac{4FG}{|c|},
\qquad
\|p_W\|_2\le 2\sqrt{\frac{FG}{|c|}}.
}
\tag{1.1}
\]

No regularity or growth condition on `R` is needed. In particular, `R(X)` may contain an arbitrary square coefficient, arbitrary affine term, or any same-variable phase produced by conditioning.

### Proof

Conditioning on `X=x`,

\[
p_W(w)=\int f(x)\,
 g\!\left(\frac{w-R(x)}{cx+d}\right)\frac{dx}{|cx+d|}
\tag{1.2}
\]

for almost every `w`; the exceptional point `cx+d=0` is null for `X`.

Square (1.2), integrate in `w`, and use Tonelli on the nonnegative integrand. Write

`a=cx+d`, `a'=cx'+d`.

After the change `w=R(x)+ay`, the inner overlap is

\[
\frac1{|a'|}\int g(y)g\!\left(\frac{R(x)-R(x')+ay}{a'}\right)dy.
\tag{1.3}
\]

For every nonzero real `r` and every translation `b`,

\[
\int g(y)g(ry+b)dy
\le G\min\{1,|r|^{-1}\}.
\tag{1.4}
\]

Indeed, bound either the second factor by `G`, or the first factor by `G` and change variables in the second. Therefore (1.3) is at most

\[
\frac{G}{\max(|a|,|a'|)}.
\tag{1.5}
\]

The random variable `U=cX+d` has density cap `K=F/|c|`. If `U'` is an independent copy, then

\[
\mathbb E\frac1{\max(|U|,|U'|)}
=\int_0^\infty \frac{\Pr(|U|<s)^2}{s^2}\,ds.
\tag{1.6}
\]

Since `Pr(|U|<s)<=min(1,2Ks)`, splitting at `s=(2K)^{-1}` gives

\[
\int_0^{1/(2K)}4K^2ds+
\int_{1/(2K)}^\infty s^{-2}ds
=4K.
\tag{1.7}
\]

Combining (1.2)--(1.7) yields

\[
\|p_W\|_2^2\le G\cdot4F/|c|,
\]
which is (1.1). QED.

### Rank-two logarithmic control is retained, not erased

For independent centered unit uniforms,

\[
p_{2XY}(t)=\log\frac1{2|t|},
\qquad 0<|t|<\frac12,
\tag{1.8}
\]

so the rank-two density is genuinely unbounded. The point of (1.1) is different: the logarithmic singularity is still square-integrable. For the elementary product `XY` on two unit uniforms on `[0,1]`, `p(z)=-\log z` on `(0,1)`, hence `||p||_2=\sqrt2`; (1.1) gives the universal cap `2` at `c=1`.

## 2. Two source-disjoint hyperbolic pairs give a linear density bound

### Corollary 2 — `QFORM-DOUBLE-HYPERBOLA-L2-CONVOLUTION-v1`

Let `(X,Y)` and `(U,V)` be independent pairs, with coordinate density caps `F_X,F_Y,F_U,F_V`. Let

\[
W_1=c_1XY+d_1Y+R_1(X),
\qquad
W_2=c_2UV+d_2V+R_2(U),
\tag{2.1}
\]

with `c_1c_2 != 0` and arbitrary measurable `R_1,R_2`. Then

\[
\boxed{
\|p_{W_1+W_2}\|_\infty
\le
4\sqrt{\frac{F_XF_YF_UF_V}{|c_1c_2|}}.
}
\tag{2.2}
\]

Moreover `p_{W_1+W_2}` has a continuous `C_0` representative.

Proof: Theorem 1 gives both densities in `L2`; then Cauchy-Schwarz/Young gives
`||p_1*p_2||_infinity<=||p_1||_2||p_2||_2`. Translation continuity in `L2` makes the convolution continuous, and approximation by compactly supported `L2` functions gives vanishing at infinity. QED.

For cap-one inputs and quadratic cross terms `2alpha XY`, `2sigma UV`, this becomes

\[
\boxed{
\|p\|_\infty\le \frac{2}{\sqrt{|\alpha\sigma|}}.
}
\tag{2.3}
\]

This is the exact smoothing mechanism here: neither hyperbolic pair has to possess a bounded density; their logarithmic singularities are `L2`, and source-disjoint convolution turns `L2 x L2` into `L-infinity`.

## 3. A non-rank-one source-disjoint crossing branch with arbitrary hub pivot and aligned crossing

Let `H,Y,Z,U,V` be five mutually independent original coordinates, each with density cap one. Let `alpha,sigma` be nonzero and let `a,b,beta,delta` and all affine coefficients be arbitrary. Consider

\[
\begin{aligned}
Q={}&aH^2+2\alpha HY+2\beta HZ+2\delta YZ\\
 &+bU^2+2\sigma UV+\text{arbitrary affine terms}.
\end{aligned}
\tag{3.1}
\]

### Theorem 3 — `QFORM-SOURCE-DISJOINT-RANK2-CROSSING-L2-v1`

The law of `Q` has a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty\le\frac{2}{\sqrt{|\alpha\sigma|}}.
}
\tag{3.2}
\]

If `beta != 0`, symmetry between `Y` and `Z` also gives

\[
\boxed{
\|p_Q\|_\infty
\le\frac{2}{\sqrt{|\sigma|\max(|\alpha|,|\beta|)}}.
}
\tag{3.3}
\]

### Proof

Condition only on the original coordinate `Z=z`. The `H,Y` portion becomes

\[
2\alpha HY+(2\delta z+\ell_Y)Y+R_z(H),
\tag{3.4}
\]

where

\[
R_z(H)=aH^2+(2\beta z+\ell_H)H+\text{constant}.
\]

Theorem 1 with `c_1=2alpha` gives, uniformly in `z`,

\[
\|p_{(3.4)}\|_2\le\sqrt{2/|\alpha|}.
\tag{3.5}
\]

The independent `U,V` portion has the form

\[
2\sigma UV+\ell_VV+R(U)
\]

and therefore

\[
\|p_{UV\text{-portion}}\|_2\le\sqrt{2/|\sigma|}.
\tag{3.6}
\]

The two portions use disjoint original sources and remain independent after conditioning on `Z`. Corollary 2 yields the conditional `L-infinity` bound (3.2), uniformly in `z`; averaging over `Z` preserves it. The same dominated-convergence argument preserves `C_0`. Conditioning on `Y` instead gives the `beta` version and hence (3.3). QED.

The term `2delta YZ` is an honest second crossing coefficient. It is not deleted even when small: after conditioning on `Z`, it becomes the allowed affine-in-`Y` term in Theorem 1. Thus Theorem 3 is a genuine non-rank-one crossing closure, but only in the source-disjoint/one-sided-curvature geometry explicitly displayed above.

## 4. Concrete target-valid indefinite family

Set

\[
Q_*=2HY+2HZ+2YZ+2UV.
\tag{4.1}
\]

The physical coefficient matrix is the direct sum

\[
\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}
\oplus
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{4.2}
\]

Its exact spectrum is

\[
\boxed{\{2,1,-1,-1,-1\}}.
\tag{4.3}
\]

Hence it lies inside the owner's target for arbitrary independent cap-one input laws. Theorem 3 gives the full-line inequality

\[
\boxed{\|p_{Q_*}\|_\infty\le2.}
\tag{4.4}
\]

No spectral-coordinate independence is used.

For comparison, deleting the `2UV` term leaves the exact-rank-three triangle

\[
R=2HY+2HZ+2YZ,
\tag{4.5}
\]

with spectrum `{2,-1,-1}`. Taking the physical indefinite pair `(H,Y)`, the two-variable core `2HY` has the logarithmic singularity (1.8), while its Schur complement in `Z` is the nonzero square coefficient `-2`. The completed pair-log theorem therefore gives a finite full-line bound (for `s=1`, `|det B|=sigma_min(B)=1`)

\[
\|p_R\|_\infty\le 8\sqrt5.
\tag{4.6}
\]

This is the literal three-direction removal of the rank-two logarithm: the rank-two receiver remains logarithmically singular; the third Schur direction supplies the square-root small-ball input that the logarithmic kernel can integrate.

## 5. Required pinned `e5f71d79...` result applied to a real inequality

The completed ruled-level-set Theorem C in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

(`COUNTEREXAMPLE_SEARCH.md`) states that for signature `(+,+,-)` the one-sheet side satisfies `p(s)<=pi sqrt(2)`. Apply it to `-R`, whose eigenvalues are `{1,1,-2}`. Since `p_R(t)=p_{-R}(-t)`,

\[
\boxed{
p_R(t)\le\pi\sqrt2,
\qquad t\le0.
}
\tag{5.1}
\]

This is strictly sign-specific. I do not transfer it to `t>0`; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction rules out that inference from X-ray control alone. The full-line bound (4.6) pays that opposite side for this exact physical family.

A second comparison uses the pinned Theorem H. For

\[
Q_m=2H(Y+Z)+2\sigma U\,m^{-1/2}\sum_{j=1}^mV_j,
\qquad m\ge2,
\tag{5.2}
\]

with all displayed sources independent cap-one variables, take hubs `{H,U}` and leaves `{Y,Z,V_1,...,V_m}`. The leaf Gram matrix is `diag(2,sigma^2)`; the normalised leverages are `1/2,1/2,1/m,...,1/m`, all at most `1/2`. The pinned Theorem H therefore gives

\[
|\phi_{Q_m}(t)|
\le
\min\left\{1,
\frac{2\sqrt2\pi^2}{|\sigma|}|t|^{-2}
\right\},
\]

and hence

\[
\boxed{
\|p_{Q_m}\|_\infty
\le 2^{7/4}|\sigma|^{-1/2}
=3.3635856610\ldots|\sigma|^{-1/2}.
}
\tag{5.3}
\]

The L2 mechanism above is a complementary spatial proof in the more source-disjoint specialization; it shows why one should not count two leaf banks sharing one hub as two independent smoothing directions, but a genuinely separate hyperbolic pair does regularise the logarithmic endpoint.

## 6. Partner account03/B11 r44 applied and the exact remaining bridge

The latest compatible designated partner is account03/B11 r44:

`yspennstate/math-open-problems@388ba1f1ccf6a89dad0ca0a0fdb71d281ad6239b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T231333Z-account03-B11-QFORM-r44/REPORT.md`.

For a physical hub and two disjoint original-coordinate banks, with star vectors `c,r`, interbank block `N`, and

\[
C=P_cNP_r,
\qquad
T=\|c\|^2\|r\|^2\|C\|_F^2,
\]

r44 proves, when `rank N=1` and `T>0`,

\[
\boxed{
\|p_Q\|_\infty\le3\,2^{2/3}T^{-1/6},
}
\tag{6.1}
\]

for arbitrary hub pivot and arbitrary same-bank phases. It identifies the Fourier gains as `|t|^{-1}` from the shared hub and `|t|^{-1/2}` from a source-disjoint transverse bilinear crossing.

The new Theorem 3 is complementary rather than stronger: it permits a genuine second crossing coefficient and does not pay a determinant as that aligned coefficient tends to zero, but it uses a stricter physical source split and one-sided curvature on the two hyperbolic pairs. Together these results localise the remaining analytic debt to **same-bank dependence plus nonzero rank-two crossing**.

There is also a sharp warning against the most naive extension of r44. After shearing a general `2x2` crossing relative to the two star directions, the crossing is

\[
\delta Y_1Z_1+\sigma Y_2Z_2,
\qquad
\delta=\det(B)/\sigma.
\tag{6.2}
\]

The first r44 operator then has kernel

\[
k_t(y+z)e^{i2t\delta yz}.
\tag{6.3}
\]

After reflection and unitary chirps, its `L2->L2` norm is the supremum of the Fourier transform of `k_t(s)e^{it\delta s^2}`. If the allowed hub phase contains `aH^2` and `a=1/\delta`, the Fresnel phase cancels at frequency zero and this multiplier has size exactly of order

\[
\sqrt{\pi/(|t\delta|)},
\tag{6.4}
\]

not `|t|^{-1}`. Combined with the transverse `|t|^{-1/2}` this leaves the nonintegrable `|t|^{-1}` endpoint. This is an obstruction to that **operator-norm proof interface**, not a QFORM counterexample. It explains why the remaining interpolation must exploit additional product/curvature structure before absolute values, rather than mechanically replacing r44's rank-one crossing by a full-rank `2x2` crossing.

## 7. Scope and next step

What is paid here:

- a new law-uniform `L2` theorem for one hyperbolic pair with arbitrary one-sided curvature;
- `L2 x L2 -> L-infinity` smoothing for two genuinely source-disjoint hyperbolic pairs;
- an explicit non-rank-one crossing family with arbitrary hub pivot and aligned crossing;
- a concrete target-valid indefinite matrix with spectrum `{2,1,-1,-1,-1}` and density at most `2`;
- the pinned ruled theorem applied on the correct one-sheet side of the exact-rank-three triangle;
- partner r44's arbitrary-pivot rank-one tensor receiver incorporated at its exact scope.

What remains unpaid:

1. `QFORM-R44-RANK2-CROSSING-SAMEBANK-INTERPOLATION-v1`: obtain the same smoothing when the relevant pair coordinates are projections of the same product bank and arbitrary same-bank curvature is present, uniformly as the second crossing singular value tends to zero; or force a source-disjoint exit.
2. Even closure of that exact-rank-three chamber does not by itself pay arbitrary additional nonseparable spectrum in the owner's full matrix target.
3. Full-target continuity remains separate.

No counterexample to the full conjecture is claimed.
