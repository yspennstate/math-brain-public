SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T21:34:00Z.
attacking: exact-constant compactification and affine homogenization, so arbitrary shifts, remote fragments, unbounded supports, and threshold eigenvalues can be removed without a moment or tail loss.

# QFORM exact-constant compactification and affine homogenization

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Status:** supporting target-level localization theorem proved; FULL QFORM remains OPEN.  
**Continuity:** not obtained by the limiting steps below; the conclusion is an essentially bounded density.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Main theorem

Let \(C<\infty\). Assume the following *restricted* statement holds in every dimension \(m\):

> For every vector \(Z=(Z_1,\ldots,Z_m)\) of independent real random variables with compactly supported probability densities \(0\le g_i\le1\), and every real symmetric \(B\) having at least three eigenvalues of absolute value **strictly greater than** \(1\), the law of \(Z^T BZ\) satisfies
> \[
> \Pr\{Z^TBZ\in I\}\le C|I|
> \tag{R}
> \]
> for every bounded open interval \(I\).

Then the same constant \(C\) works for the full owner target: for every \(n\), arbitrary independent cap-one input densities with no support or moment assumptions, and every real symmetric \(A\) with at least three eigenvalues of absolute value at least \(1\),
\[
\Pr\{X^TAX\in I\}\le C|I|,
\tag{1.1}
\]
and hence \(X^TAX\) has a density \(p\) with \(\|p\|_{\infty,\mathrm{ess}}\le C\).

Moreover exactly the same \(C\) holds for every affine perturbation
\[
X^TAX+b^TX+c,
\tag{1.2}
\]
with arbitrary deterministic \(b\in\mathbb R^n,c\in\mathbb R\).

Thus, at the level of the universal constant, the full conjecture is equivalent to its compact-support, strict-spectral-margin version. Arbitrary coordinate translations can also be removed at zero cost after passing to the affine formulation.

This theorem does **not** impose a uniform diameter, a uniform fragment count, a common support center, or any moment bound. Compact supports used in the approximation may move arbitrarily far out and may contain arbitrarily remote fragments.

## 2. Cap-preserving compactification of one marginal

Let \(f\) be any probability density on \(\mathbb R\) with \(0\le f\le1\). For \(R>0\), put
\[
\delta_R=\int_{|x|>R} f(x)\,dx.
\]
Choose the interval
\[
J_R=[R+1,R+1+\delta_R]
\]
(and take \(J_R=\varnothing\) if \(\delta_R=0\)), and define
\[
f^{(R)}(x)=f(x)\mathbf 1_{[-R,R]}(x)+\mathbf 1_{J_R}(x).
\tag{2.1}
\]
Because \(J_R\cap[-R,R]=\varnothing\),
\[
0\le f^{(R)}\le1,
\qquad
\int f^{(R)}=1-\delta_R+|J_R|=1.
\tag{2.2}
\]
Its support is compact. On the tail \(\{|x|>R\}\),
\[
\begin{aligned}
\|f^{(R)}-f\|_1
&=\int_{J_R}(1-f)+\int_{\{|x|>R\}\setminus J_R}f\\
&=2\left(\delta_R-\int_{J_R}f\right)
\le2\delta_R.
\end{aligned}
\tag{2.3}
\]
Hence the total-variation distance between the two one-dimensional laws is at most \(\delta_R\to0\).

Two points are important for the present assignment.

1. No tail moment occurs: only the tail **mass** \(\delta_R\) is used.
2. The missing tail mass is restored by a cap-one interval. We never renormalize the truncated density, so the density cap is preserved exactly.

## 3. Product and pushforward transfer with no constant loss

For independent coordinates, construct \(X_i^{(R)}\) using (2.1). By the standard telescoping/coupling inequality,
\[
d_{\rm TV}\!\left(\bigotimes_{i=1}^n\mathcal L(X_i^{(R)}),
                 \bigotimes_{i=1}^n\mathcal L(X_i)\right)
\le\sum_{i=1}^n\delta_{i,R}.
\tag{3.1}
\]
Every measurable pushforward contracts total variation. Therefore for every Borel map \(F:\mathbb R^n\to\mathbb R\), in particular every quadratic or affine-quadratic form,
\[
d_{\rm TV}(\mathcal L(F(X^{(R)})),\mathcal L(F(X)))
\le\sum_i\delta_{i,R}.
\tag{3.2}
\]
Consequently, if for all \(R\)
\[
\Pr\{F(X^{(R)})\in I\}\le C|I|,
\tag{3.3}
\]
then
\[
\Pr\{F(X)\in I\}
\le C|I|+\sum_i\delta_{i,R}.
\tag{3.4}
\]
Letting \(R\to\infty\) gives the identical constant \(C\).

Thus arbitrary unbounded support is removed without a tail penalty, and arbitrary distant fragments are retained rather than collapsed into a bounded-diameter model.

## 4. Removing the spectral threshold equality

Assume now that the inputs are compactly supported and \(A\) has at least three eigenvalues with \(|\lambda|\ge1\). For \(\eta>0\), set
\[
A_\eta=(1+\eta)A,
\qquad
Q_\eta=X^TA_\eta X=(1+\eta)Q.
\]
The three relevant eigenvalues of \(A_\eta\) have absolute value strictly greater than \(1\), so (R) gives
\[
\Pr\{Q_\eta\in (1+\eta)I\}\le C(1+\eta)|I|.
\]
Since \(Q_\eta=(1+\eta)Q\),
\[
\Pr\{Q\in I\}\le C(1+\eta)|I|.
\tag{4.1}
\]
Let \(\eta\downarrow0\):
\[
\Pr\{Q\in I\}\le C|I|.
\tag{4.2}
\]
So proving the theorem with a strict spectral margin is enough, with no loss at the threshold \(|\lambda|=1\).

## 5. Affine homogenization by one far-translated cap-one coordinate

The key translation lemma is stronger: the homogeneous theorem implies the affine theorem with the **same** constant.

First take compactly supported \(X\), a target matrix \(A\), and \(b\ne0\). For \(T>0\), let
\[
U\sim\operatorname{Unif}[0,1]
\]
be independent of \(X\), and set \(Y_T=T+U\). This is a compactly supported cap-one input. Define
\[
e_T=\frac{\|b\|_2}{2T},
\qquad
\delta_T=2e_T=\frac{\|b\|_2}{T},
\tag{5.1}
\]
and the \((n+1)\times(n+1)\) symmetric matrix
\[
B_T=
\begin{pmatrix}
(1+\delta_T)A & b/(2T)\\
 b^T/(2T) & 0
\end{pmatrix}.
\tag{5.2}
\]
Let
\[
D_T=\operatorname{diag}((1+\delta_T)A,0),
\qquad
E_T=B_T-D_T.
\]
The off-diagonal rank-two block has
\[
\|E_T\|_{\rm op}=\frac{\|b\|_2}{2T}=e_T.
\tag{5.3}
\]
Every eigenvalue of \(D_T\) corresponding to one of the three target eigenvalues of \(A\) has absolute value at least \(1+\delta_T=1+2e_T\). Weyl's eigenvalue perturbation inequality therefore leaves the corresponding eigenvalues of \(B_T\) outside \([-1-e_T,1+e_T]\); explicitly positive ones remain at least \(1+e_T\), negative ones at most \(-1-e_T\). Hence \(B_T\) has at least three eigenvalues with absolute value strictly greater than \(1\).

The homogeneous quadratic form of the independent cap-one vector \((X,Y_T)\) is
\[
\begin{aligned}
\widetilde Q_T
&=(X,Y_T)^TB_T(X,Y_T)\\
&=(1+\delta_T)X^TAX+\frac{Y_T}{T}\,b^TX.
\end{aligned}
\tag{5.4}
\]
By the restricted theorem (R),
\[
\Pr\{\widetilde Q_T\in I\}\le C|I|.
\tag{5.5}
\]
Couple all \(Y_T\) using the same \(U\). Then
\[
\frac{Y_T}{T}=1+\frac UT\longrightarrow1,
\qquad
\delta_T\longrightarrow0.
\]
For every finite sample value of \(X\),
\[
\widetilde Q_T\longrightarrow X^TAX+b^TX
\qquad\text{almost surely}.
\tag{5.6}
\]
No integrability of \(X\) is used. Thus the laws converge weakly. If \(I\) is open, Portmanteau gives
\[
\Pr\{X^TAX+b^TX\in I\}
\le\liminf_{T\to\infty}\Pr\{\widetilde Q_T\in I\}
\le C|I|.
\tag{5.7}
\]
The case \(b=0\) is Section 4; adding a scalar \(c\) merely translates the output. This proves the affine theorem for compact inputs. Section 3 then transfers it to arbitrary unbounded cap-one product laws with the same \(C\).

This is the main localization point: an arbitrary deterministic affine term is absorbed by **one extra independent cap-one coordinate located far away**, while its matrix coupling tends to zero. The far translation causes no moment problem because \(Y_T/T\to1\) uniformly.

## 6. Density conclusion

Suppose a probability measure \(\mu\) on \(\mathbb R\) obeys
\[
\mu(I)\le C|I|
\]
for every bounded open interval. By countable disjoint decomposition this extends to every open set, and by outer regularity to every Borel set. Therefore \(\mu\ll dx\), and the Radon--Nikodym density satisfies \(p\le C\) almost everywhere.

The limiting argument does not imply that \(p\) has a continuous representative. Uniform \(L^\infty\) bounds are weak-* compact but do not preserve continuity. Thus the owner-requested continuity conclusion remains a separate full-target obligation.

## 7. Translation corollary

Let \(m\in\mathbb R^n\) be arbitrary and write \(X=Z+m\). Coordinate translation preserves independence and the density cap. Then
\[
X^TAX=Z^TAZ+2(Am)^TZ+m^TAm.
\tag{7.1}
\]
By the affine theorem, translating the physical supports of the independent coordinates by arbitrary deterministic amounts does not change the universal density constant. In particular, a proof may recenter any chosen compact approximation or any selected fragment without paying for the translation.

What cannot be done is impose a universal diameter or universal number of fragments: existing correction events rule those reductions out. The present lemma deliberately preserves arbitrary fragment geometry.

## 8. Application of the completed account04/B14 theorem to an actual inequality

Use account04/B14's completed scale-covariant conjugate-shear theorem at
\[
\texttt{yspennstate/math-open-problems@2ac84e141e8e939506cbd5cd8314589141b714d5},
\]
whose active form is
\[
Q=2cX_1X_2+\frac d2\big((1-\alpha)X_3+(1+\alpha)X_4-\beta\big)^2
   +\ell_1X_1+\ell_2X_2+\gamma.
\tag{8.1}
\]
Under
\[
|c|\ge1,
\qquad
|d|(1+\alpha^2)\ge1,
\tag{8.2}
\]
that theorem gives, on compact cap-one laws (indeed it proves more),
\[
\Pr\{Q_R\in I\}\le C_0|I|,
\qquad
C_0=4+2\log8<8.159.
\tag{8.3}
\]
For arbitrary unbounded or remotely fragmented cap-one laws, use the compactifications of Section 2. Writing \(\delta_{j,R}=\Pr(|X_j|>R)\), (3.2) gives the concrete inequality
\[
\boxed{
\Pr\{Q\in I\}
\le
(4+2\log8)|I|+\sum_{j=1}^4\delta_{j,R}.
}
\tag{8.4}
\]
Sending \(R\to\infty\) yields
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}\le4+2\log8<8.159
}
\tag{8.5}
\]
with **no** moment, support-radius, translation, diameter, or fragment-count term. This is a direct equation-level use of the partner result. The transfer uses only tail masses, not a normalized tail law.

## 9. What this buys the full proof

The unrestricted conjecture is still open: this report does not prove the core analytic estimate for compact product laws. It removes three logically separate sources of technical debt from that remaining estimate:

1. **unbounded supports:** cap-preserving compactification transfers any interval bound with zero loss;
2. **eigenvalues exactly at the threshold:** strict margin \(>1\) suffices, again with zero loss;
3. **conditioning-generated deterministic affine terms / arbitrary support translations:** homogeneous bounds imply affine bounds with the same constant via one far-translated auxiliary cap-one coordinate.

Therefore future full-target arguments may work on compactly supported product laws, with strict spectral margin, and may ignore deterministic coordinate locations once they retain arbitrary affine terms. They still may **not** assume a uniform support diameter, connected support, finite fragment count, moments, or independence after rotation.

The next B14 question is no longer tail localization. It is to combine this exact-constant compiler with an overlapping-third-resource compact-core estimate; any success there automatically propagates to the original unbounded, threshold, translated problem.

## 10. Scope and corrections respected

No pointwise van-der-Corput decay is used. No rotated coordinates are declared independent. No arbitrary-joint coarea theorem or normalized conditional density cap is used. No Monte Carlo statement is used as proof. The theorem is purely measure-theoretic plus Weyl perturbation and preserves the exact universal constant.

**FULL QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Full-target continuity:** OPEN.
