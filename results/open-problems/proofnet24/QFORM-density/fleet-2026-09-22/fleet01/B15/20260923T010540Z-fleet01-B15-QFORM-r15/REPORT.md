# QFORM fleet01/B15 r15 — exact two-sheet hyperbolic-trace normal form

Run: `20260923T010540Z-fleet01-B15-QFORM-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: absolute continuity and regularity  
Status: `ESSENTIAL_STEP_APPLIED / EXACT_TWOSHEET_HYPERBOLIC_TRACE_NORMAL_FORM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and conclusion

The owner target remains open: for independent one-dimensional probability densities `f_i<=1` and a real symmetric matrix having at least three eigenvalues of modulus at least one, prove one matrix- and dimension-independent bound for the density of `X^T A X`.

This run closes no higher-rank structural branch. It gives a precise regularity normal form for the exact-rank-three indefinite obstruction. The assigned partner `fleet02/B15` has now paid the entire majority-sign one-sheet branch by a universal ruled estimate. I combine that result with a full-dimensional change of variables on the minority-sign region and obtain an exact hyperbolic-ray trace formula. Consequently, for exact rank three and signature `(2,1)`, finiteness of the full universal height is equivalent to one and only one remaining statement: a uniform bound on the product-provenance hyperbolic-ray trace on the two-sheet side. No arbitrary-joint trace estimate is asserted.

The run also separates the regularity levels cleanly:

1. nonconstant quadratic pushforwards of absolutely continuous input laws are absolutely continuous;
2. the partner theorem gives a universal `L^infinity` bound on the one-sheet submeasure only;
3. the independently completed partner regularity theorem gives an instance-dependent full density in `C_0(R)` for rank at least three;
4. continuity upgrades the one-sheet essential bound to a pointwise bound at the critical value, but does not supply the missing two-sheet height.

## 2. Source-valid partner results used

### 2.1 Majority-sign ruled theorem

I consumed the completed `fleet02/B15` report

- `yspennstate/math-open-problems@113aff6eea39e748c1bb6685c7656add2487c03e`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T000548Z-fleet02-B15-QFORM/REPORT.md`.

For orthonormal `r_1,r_2,r_3`, independent cap-one physical coordinates, and

\[
Q=\lambda_1\langle r_1,X\rangle^2+\lambda_2\langle r_2,X\rangle^2-\mu\langle r_3,X\rangle^2,
\qquad \lambda_1,\lambda_2,\mu>0,
\]

the partner proves that the restriction of the output law to `[0,infinity)` has density at most

\[
C_+(\lambda_1,\lambda_2,\mu)
=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\left(
\frac{\sin^2\theta}{\lambda_1}+
\frac{\cos^2\theta}{\lambda_2}+
\frac1\mu
\right)^{-1/2}d\theta.
\tag{2.1}
\]

It also proves the affine-in-range extension after physical translation. No post-rotation independence is assumed.

Let

\[
s:=\min(\lambda_1,\lambda_2,\mu)=s_3(A)
\]

for this exact-rank-three matrix. Rewriting the integrand gives

\[
\frac1{\sqrt{\lambda_2\mu\sin^2\theta+\lambda_1\mu\cos^2\theta+\lambda_1\lambda_2}}
\le \frac1{s\sqrt2},
\]

hence the actual inequality I use below is

\[
\boxed{
\|p_+\|_\infty\le \frac{\pi\sqrt2}{s}.
}
\tag{2.2}
\]

Here `p_+` denotes the density of the submeasure `1_{Q>=0} dP_Q`.

### 2.2 Full fixed-matrix `C_0` regularity

I also consumed the independently completed `fleet02/B15` regularity report

- `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T200544Z-fleet02-B15-qform-r11/REPORT.md`.

It proves that for every fixed real symmetric `A` with `rank(A)>=3` and every cap-one product source, the full output density is bounded with an instance-dependent bound and has a representative in `C_0(R)`. The physical-block constants are not uniform in `A`, so this is a regularity theorem and not the owner conjecture.

## 3. Absolute continuity baseline

The following statement is useful because it does not need independence or the three-large-eigenvalue hypothesis.

> **Lemma 3.1.** Let `q(x)=x^T A x+2b^T x+c` be a nonconstant quadratic polynomial on `R^n`, and let `X` have any absolutely continuous joint law. Then `q(X)` is absolutely continuous.

**Proof.** The critical set

\[
\{x:\nabla q(x)=0\}=\{x:Ax+b=0\}
\]

is empty or a proper affine subspace unless `q` is constant, hence it is Lebesgue-null. Let `N subset R` be null. On

\[
E_k=\{|x|\le k,\ |\nabla q(x)|\ge1/k\},
\]

coarea gives

\[
\int_{E_k\cap q^{-1}(N)} |\nabla q(x)|\,dx
=\int_N \mathcal H^{n-1}(E_k\cap q^{-1}(t))\,dt=0.
\]

Thus `Leb(E_k cap q^{-1}(N))=0`. The complement of the union of the `E_k`, modulo a null set, lies in the critical affine subspace. Therefore `q^{-1}(N)` is null, and every absolutely continuous input law assigns it probability zero. `q(X)` is absolutely continuous. ∎

This lemma is only an existence statement. Rank one already shows that absolute continuity does not imply bounded density.

## 4. Exact minority-side hyperbolic coordinates

Now assume exact rank three and signature `(2,1)`. Write

\[
A=R\,\operatorname{diag}(\lambda_1,\lambda_2,-\mu)R^T,
\qquad R^TR=I_3,
\qquad \lambda_1,\lambda_2,\mu>0.
\]

The same calculation applies to the affine-in-range form

\[
Q_{a,c}=\lambda_1(Y_1-a_1)^2+\lambda_2(Y_2-a_2)^2-\mu(Y_3-a_3)^2+c,
\qquad Y=R^TX.
\tag{4.1}
\]

The target homogeneous case is `a=0,c=0`. Put `h=Ra` and `X'=X-h`. This is a deterministic translation of each physical coordinate, so the coordinates of `X'` remain independent and each translated density is still bounded by one. Put

\[
Z=D R^T X',\qquad
D=\operatorname{diag}(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt\mu).
\]

Because `DR^T` has rank three and the joint law of `X'` is absolutely continuous, `Z` has an `L^1(R^3)` probability density `\rho`. No pointwise cap on `\rho` is needed below. Then

\[
Q_{a,c}=c+q(Z),\qquad q(z)=z_1^2+z_2^2-z_3^2.
\tag{4.2}
\]

For `alpha>0`, `theta in [0,2pi)`, `w>sqrt(alpha)`, and `sigma in {+1,-1}`, define

\[
F_\sigma(\alpha,\theta,w)
=
\big(
\sqrt{w^2-\alpha}\cos\theta,
\sqrt{w^2-\alpha}\sin\theta,
\sigma w
\big).
\tag{4.3}
\]

Then `q(F_sigma)=-alpha`. More importantly, this is a **full-dimensional** parametrization of the region `q<0`, separately on `z_3>0` and `z_3<0`, apart from null boundary/axis sets. Its ordinary three-dimensional Jacobian is exactly

\[
\boxed{\left|\det D F_\sigma\right|=\frac12.}
\tag{4.4}
\]

Indeed, in cylindrical coordinates `r=sqrt(w^2-alpha)` one has `r dr=-(1/2)d alpha` at fixed `w`; equivalently a direct determinant computation from (4.3) gives `1/2`.

Therefore, for every nonnegative Borel function `Phi`, ordinary change of variables and Tonelli give

\[
\begin{aligned}
\mathbb E\big[\Phi(c-Q_{a,c})\mathbf1_{\{Q_{a,c}<c\}}\big]
&=\int_{q(z)<0}\Phi(-q(z))\rho(z)\,dz\\
&=\frac12\sum_{\sigma=\pm1}
\int_0^\infty \Phi(\alpha)
\int_0^{2\pi}\int_{\sqrt\alpha}^{\infty}
\rho(F_\sigma(\alpha,\theta,w))\,dw\,d\theta\,d\alpha.
\end{aligned}
\tag{4.5}
\]

Define the **minority hyperbolic-ray trace density**

\[
\boxed{
H_\rho(\alpha)
:=\frac12\sum_{\sigma=\pm1}
\int_0^{2\pi}\int_{\sqrt\alpha}^{\infty}
\rho\!\left(
\sqrt{w^2-\alpha}\cos\theta,
\sqrt{w^2-\alpha}\sin\theta,
\sigma w
\right)
\,dw\,d\theta,
\quad \alpha>0.
}
\tag{4.6}
\]

Equation (4.5) proves, without evaluating a codimension-one trace of a rough representative, that `H_rho` is a genuine `L^1` density of `c-Q` on the event `Q<c`. In particular,

\[
\int_0^\infty H_\rho(\alpha)\,d\alpha
=\Pr(Q_{a,c}<c)\le1,
\tag{4.7}
\]

and for almost every `alpha>0`,

\[
\boxed{p_{Q_{a,c}}(c-\alpha)=H_\rho(\alpha).}
\tag{4.8}
\]

This formula is source-valid for rough cap-one inputs because (4.5) is a full-dimensional change of variables. It is not an arbitrary-joint *bound*; it merely identifies the exact remaining positive trace functional.

## 5. Exact rank-three indefinite height reduction

For an exact-rank-three signature `(2,1)` instance define

\[
M_-(A,f):=s\,\operatorname*{ess\,sup}_{\alpha>0}H_\rho(\alpha),
\qquad s=s_3(A).
\tag{5.1}
\]

By (2.2), the majority branch has

\[
s\,\operatorname*{ess\,sup}_{t\ge c}p_Q(t)\le\pi\sqrt2.
\tag{5.2}
\]

By (4.8), the minority branch has exactly

\[
s\,\operatorname*{ess\,sup}_{t<c}p_Q(t)=M_-(A,f).
\tag{5.3}
\]

Since the two submeasures have disjoint supports up to the single critical value, the full essential height satisfies the **actual partner-applied inequality**

\[
\boxed{
M_-(A,f)
\le s\|p_Q\|_\infty
\le \max\{\pi\sqrt2,\,M_-(A,f)\}.
}
\tag{5.4}
\]

Let

\[
\mathcal M_-:=\sup_{\text{exact-rank-3 signature }(2,1)}M_-(A,f),
\]

where the supremum runs over all dimensions, all cap-one product sources, and all coefficient triples. Let `C_{3,ind}` be the sharp scaled density constant on the same exact-rank-three indefinite class. Then

\[
\boxed{
\mathcal M_-\le C_{3,ind}\le\max\{\pi\sqrt2,\mathcal M_-\}.
}
\tag{5.5}
\]

Hence

\[
\boxed{
C_{3,ind}<\infty
\quad\Longleftrightarrow\quad
\mathcal M_-<\infty.
}
\tag{5.6}
\]

This is a zero-loss **finiteness equivalence**: after the completed partner theorem, the exact-rank-three indefinite problem has only the two-sheet hyperbolic-ray trace left. For signature `(1,2)`, apply the statement to `-Q`; the minority side and the direction of the critical half-line are reversed.

The correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is fully respected. Equation (4.6) is not claimed to be controlled by generic line-X-ray caps. The live counterexample shows that such a projection-only implication is false for arbitrary joint densities. The remaining theorem must use the fact that `rho` comes from a three-dimensional linear projection of an original-coordinate product law.

## 6. Tent functional: exact positive-kernel form of the same obstruction

For

\[
\tau_{\varepsilon,y}(t)=(\varepsilon-|t-y|)_+,
\qquad \int_\mathbb R\tau_{\varepsilon,y}(t)\,dt=\varepsilon^2,
\]

the partner inequality (2.2) gives

\[
s\varepsilon^{-2}
\mathbb E\big[\tau_{\varepsilon,y}(Q)\mathbf1_{\{Q\ge c\}}\big]
\le\pi\sqrt2.
\tag{6.1}
\]

Applying (4.5) with `Phi(alpha)=tau_{epsilon,y}(c-alpha)` gives the exact minority term

\[
\mathbb E\big[\tau_{\varepsilon,y}(Q)\mathbf1_{\{Q<c\}}\big]
=
\int_0^\infty
\tau_{\varepsilon,y}(c-\alpha)H_\rho(\alpha)\,d\alpha.
\tag{6.2}
\]

Therefore

\[
\boxed{
 s\varepsilon^{-2}\mathbb E\tau_{\varepsilon,y}(Q)
\le
\pi\sqrt2
+
 s\varepsilon^{-2}
\int_0^\infty
\tau_{\varepsilon,y}(c-\alpha)H_\rho(\alpha)\,d\alpha.
}
\tag{6.3}
\]

This identifies the exact positive-kernel quantity which the remaining two-sheet proof has to control. If `M_-(A,f)<=M`, then the second term in (6.3) is at most `M`, because the tent has total mass `epsilon^2`. Conversely, by the approximate-identity property, uniform control of the minority tent term over all `epsilon,y` gives the essential bound for `H_rho`.

Thus the interval, density, and fixed-tent formulations are aligned on the same minority object; no Fourier `L^1` or pointwise oscillatory-decay step is needed.

## 7. Continuity is separate, but it localizes any bad maximum

Now apply the second completed `fleet02/B15` theorem from Section 2.2. Since `rank(A)=3`, the full density has an instance-dependent representative

\[
p_Q\in C_0(\mathbb R).
\tag{7.1}
\]

The essential one-sheet estimate (2.2) therefore upgrades, for the same fixed instance, to the pointwise statement

\[
\boxed{
p_Q(t)\le\frac{\pi\sqrt2}{s}\quad\text{for every }t\ge c,
\qquad
p_Q(c)\le\frac{\pi\sqrt2}{s}.
}
\tag{7.2}
\]

Indeed a continuous function which is bounded by a constant almost everywhere on an open half-line is bounded by the same constant everywhere there, and continuity passes the bound to the endpoint.

Since `p_Q in C_0`, it attains its maximum. Hence

\[
\boxed{
\max_t p_Q(t)>\frac{\pi\sqrt2}{s}
\quad\Longrightarrow\quad
\text{every maximizing point with that height lies strictly on }t<c.
}
\tag{7.3}
\]

Consequently any sequence of exact-rank-three indefinite target instances with

\[
s_m\max_t p_m(t)\to\infty
\]

must, after taking actual maximizers, realize the divergence on the genuine minority/two-sheet side. The cone critical value itself can never carry the divergence.

This is a qualitative localization, not a uniform neighborhood estimate. The fleet has explicit source-valid families showing there is no target-uniform raw continuity/Besov modulus in general. I therefore do **not** infer a universal distance of a bad maximizer from the critical value.

## 8. Why the new normal form is useful

The remaining two-sheet object (4.6) has three important features.

1. It is positive and exact. There is no cancellation bookkeeping and no representative ambiguity because it comes from a full-dimensional coordinate change.
2. It keeps the product-projection provenance visible: `rho` is not an arbitrary joint density but the law of `D R^T(X-Ra)` for original-coordinate independent cap-one variables.
3. It makes the failed projection-only shortcut explicit. The geometric curve

\[
w\mapsto
(\sqrt{w^2-\alpha}\cos\theta,
 \sqrt{w^2-\alpha}\sin\theta,
 \pm w)
\]

is a hyperbolic ray, not one of the affine rulings available on the one-sheet side. The correction ledger says generic X-ray control alone does not bound this trace. Any successful proof must aggregate the original product law before or jointly with this curved trace.

Thus the first unpaid exact-rank-three implication is now the following source-faithful statement:

> **Hyperbolic-ray product-projection bound.** Prove one finite universal `M` such that for every cap-one product source, every orthonormal `R`, every `lambda_1,lambda_2,mu>0`, with `s=min(lambda_1,lambda_2,mu)`, and `rho` the density of `D R^T X`,
> \[
> s\,\operatorname*{ess\,sup}_{\alpha>0}H_\rho(\alpha)\le M.
> \]

Proving this closes the exact-rank-three indefinite class with `s||p_Q||_infinity<=max(pi sqrt(2),M)`. It still would not by itself close the higher-rank N3/hybrid structural step of the owner conjecture.

## 9. Correction audit

This report uses none of the prohibited interfaces:

- no law-uniform pointwise quadratic Fourier decay;
- no independence after spectral rotation;
- no projection-only implication for the two-sheet side;
- no arbitrary-joint rank-three coarea height bound;
- no conditional projection `L^infinity` positive-moment estimate;
- no reciprocal tiny principal-minor payment.

The only use of spectral coordinates is deterministic notation for the three-dimensional pushforward density `rho`; all independence claims remain in the original physical coordinates. The one-sheet bound is imported only from the source-checked partner theorem, whose proof returns to rough product inputs by total variation.

## 10. Status

Full unrestricted QFORM: **OPEN / NOT PROVED**.

New durable result: `QFORM-EXACT-R3-TWOSHEET-HYPERBOLIC-TRACE-NORMAL-FORM-v1`, comprising (4.5)-(4.8), the sharp finiteness reduction (5.4)-(5.6), the tent identity (6.2)-(6.3), and the critical-value/maximizer localization (7.2)-(7.3).

First unpaid B15 implication: prove the universal hyperbolic-ray product-projection bound above, or embed it into the current grouped-coordinate/N3 aggregate mechanisms without collapsing to generic X-ray information.
