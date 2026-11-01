# C0032 — global parametric elimination of the BCC self-consistency and all origin jets

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, heavy-tailed limiting law `mu_alpha`; underlying scalar characterization from Bordenave–Caputo–Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*.

Status of this artifact: theorem-sized PARTIAL progress toward the source request for an explicit all-radius density.  It removes the fixed-point unknown from the BCC scalar equation by a global monotone parameter, gives Mellin-Barnes formulae for the two remaining scalar transforms, and proves explicit Gamma-function formulae for every finite origin jet.  It does **not** by itself claim source-level closure or novelty.

## 1. Source equations and notation

Fix `0<alpha<2` and put

\[
\beta=\alpha/2\in(0,1),\qquad c_\beta=\Gamma(1-\beta).
\]

Let `S,S'` be independent positive beta-stable random variables normalized by

\[
\mathbb E e^{-tS}=e^{-c_\beta t^\beta},\qquad t\ge0.
\]

Write

\[
r=|z|^2,\qquad Y(r)=y_*(r)^2,
\]

where the BCC scalar fixed point is

\[
1=\mathbb E\bigl(r/S+Y(r)S'\bigr)^{-\beta}.
\tag{1.1}
\]

For `q>0`, the negative moments are

\[
m_q:=\mathbb E S^{-q}
=\frac{\Gamma(1+q/\beta)}
{\Gamma(1+q)c_\beta^{q/\beta}}.
\tag{1.2}
\]

Let `T=SS'`.  If `\widetilde g_\alpha(r)=g_\alpha(\sqrt r)`, the BCC density identity is

\[
\pi\widetilde g_\alpha(r)
=(Y-rY')\,\mathbb E\frac{T}{(r+YT)^2}.
\tag{1.3}
\]

The preceding R7-06 run differentiated these equations only at `r=0`.  The point here is to remove `Y` globally.

## 2. B5 — introduce the ratio parameter and eliminate the fixed point

Define

\[
a=\frac r{Y(r)}
\tag{2.1}
\]

and the deterministic scalar function

\[
F(a):=\mathbb E\bigl(S'+a/S\bigr)^{-\beta},\qquad a\ge0.
\tag{2.2}
\]

Then (1.1) factors exactly as

\[
1=Y(r)^{-\beta}F(a).
\]

Hence

\[
\boxed{Y(a)=F(a)^{1/\beta}},\qquad
\boxed{r(a)=aF(a)^{1/\beta}}.
\tag{2.3}
\]

There is no self-consistent unknown on the right-hand side of (2.3).

### Smoothness

For every integer `n>=0`, differentiation under the expectation is justified by the finite negative moments (1.2), and

\[
F^{(n)}(a)
=(-1)^n(\beta)_n
\mathbb E\left[S^{-n}(S'+a/S)^{-\beta-n}\right].
\tag{2.4}
\]

In particular,

\[
\boxed{F^{(n)}(0)=(-1)^n(\beta)_n m_n m_{\beta+n}}.
\tag{2.5}
\]

Here `(beta)_n=beta(beta+1)...(beta+n-1)` and `m_0=1`.

### Strict monotonicity of the radial parameter

From (2.3),

\[
r'(a)=F(a)^{1/\beta}
\left(1+\frac{aF'(a)}{\beta F(a)}\right).
\tag{2.6}
\]

But

\[
-\frac{aF'(a)}\beta
=\mathbb E\left[(S'+a/S)^{-\beta}
\frac{a/S}{S'+a/S}\right]
<F(a)
\tag{2.7}
\]

for every `a>0`.  Therefore

\[
\boxed{r'(a)>0\quad(a\ge0)}.
\tag{2.8}
\]

Moreover `r(0)=0`.  The positive beta-stable tail satisfies
`P(S>x)~C_beta x^{-beta}`.  Consequently

\[
\mathbb E[S^\beta;S\le a]\asymp\log a.
\]

On `{S\le a,S'\le1}` we have

\[
(S'+a/S)^{-\beta}\ge 2^{-\beta}(S/a)^\beta,
\]

so for large `a`,

\[
F(a)\ge C a^{-\beta}\log a.
\]

Thus

\[
r(a)=aF(a)^{1/\beta}\ge C'(\log a)^{1/\beta}\longrightarrow\infty.
\tag{2.9}
\]

Hence `a -> r(a)` is a strictly increasing `C^infty` bijection from `[0,infinity)` to `[0,infinity)`.

## 3. Exact global density and radial CDF in the new parameter

Define

\[
K(a):=\mathbb E\frac1{a+T},\qquad
J(a):=\mathbb E\frac{T}{(a+T)^2}.
\tag{3.1}
\]

Then

\[
J(a)=(aK(a))'.
\tag{3.2}
\]

Using `r=aY`,

\[
Y-r\frac{dY}{dr}
=\frac{Y^2}{r'(a)}.
\tag{3.3}
\]

Also

\[
\mathbb E\frac{T}{(r+YT)^2}=Y^{-2}J(a).
\tag{3.4}
\]

Substituting (3.3)–(3.4) into the source density formula (1.3) gives the global parametric identity

\[
\boxed{
\pi\widetilde g_\alpha(r(a))=\frac{J(a)}{r'(a)}.
}
\tag{3.5}
\]

Let

\[
M(r):=\mu_\alpha\{z:|z|^2\le r\}.
\]

Since `M'(r)=pi tilde g_alpha(r)`, (3.2) and (3.5) imply

\[
\frac d{da}M(r(a))=J(a)=(aK(a))'.
\]

Both sides vanish at `a=0`, hence

\[
\boxed{M(r(a))=aK(a).}
\tag{3.6}
\]

Equations (2.3), (3.5), and (3.6) identify the complete radial law by one monotone deterministic parameter and contain no BCC fixed-point unknown.

## 4. B18 — Mellin translation and Mellin-Barnes inversion

The fixed point has now been replaced by two ordinary scalar transforms `F` and `K`.  Both have closed Mellin transforms.

### Mellin transform of F

For `0<Re(s)<beta`, Tonelli/Beta integration gives

\[
\begin{aligned}
\int_0^\infty a^{s-1}F(a)\,da
&=\mathbb E\int_0^\infty
 a^{s-1}(S'+a/S)^{-\beta}\,da\\
&=B(s,\beta-s)\,\mathbb E S^s\,\mathbb E S^{s-\beta}.
\end{aligned}
\tag{4.1}
\]

For `0<Re(s)<beta`,

\[
\mathbb E S^s
=c_\beta^{s/\beta}
\frac{\Gamma(1-s/\beta)}{\Gamma(1-s)}.
\tag{4.2}
\]

Combining (1.2), (4.1), and (4.2), and simplifying Gamma factors,

\[
\boxed{
\mathcal M F(s)
=c_\beta^{-1+2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}
{\Gamma(1+\beta)\Gamma(1-s)}
},
\qquad 0<\Re s<\beta.
\tag{4.3}
\]

Thus for any `sigma in (0,beta)`, standard Mellin inversion yields

\[
\boxed{
F(a)=\frac1{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
 c_\beta^{-1+2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}
{\Gamma(1+\beta)\Gamma(1-s)}
 a^{-s}\,ds.
}
\tag{4.4}
\]

This is a generalized Mellin-Barnes / Fox-H type representation.

### Mellin transform of K

For `0<Re(s)<1`,

\[
\int_0^\infty\frac{a^{s-1}}{a+T}\,da
=T^{s-1}\Gamma(s)\Gamma(1-s).
\]

Since `T=SS'`, the negative-moment formula gives

\[
\boxed{
\mathcal M K(s)
=\frac{\Gamma(s)\Gamma((1-s)/\beta)^2}
{\beta^2\Gamma(1-s)c_\beta^{2(1-s)/\beta}}
},
\qquad 0<\Re s<1.
\tag{4.5}
\]

Therefore, for `sigma in (0,1)`,

\[
\boxed{
K(a)=\frac1{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
\frac{\Gamma(s)\Gamma((1-s)/\beta)^2}
{\beta^2\Gamma(1-s)c_\beta^{2(1-s)/\beta}}
 a^{-s}\,ds.
}
\tag{4.6}
\]

Together, (2.3), (3.5), (3.6), (4.4), and (4.6) are a global one-parameter Mellin-Barnes representation of the BCC law with the self-consistency eliminated.

## 5. B21 — import formal inversion to solve every finite origin jet

The product-stable transform also makes every local coefficient finite and explicit.

From (3.1),

\[
\boxed{
J^{(n)}(0)=(-1)^n(n+1)!m_{n+1}^2.
}
\tag{5.1}
\]

Because `F(0)=m_beta>0`, (2.3) has nonzero linear derivative at the origin.  For every fixed finite order, ordinary smooth inverse-function Taylor calculus (equivalently the finite-jet form of Lagrange-Bürmann inversion) applies to

\[
r=aF(a)^{1/\beta}.
\]

If

\[
\widetilde g_\alpha(r)=\sum_{k=0}^N c_{\alpha,k}r^k+o(r^N),
\]

then the exact coefficient identity is

\[
\boxed{
\pi c_{\alpha,k}
=[a^k]\,J(a)F(a)^{-(k+1)/\beta},
\qquad k=0,1,2,\ldots
}
\tag{5.2}
\]

where `[a^k]` means the coefficient in the finite Taylor jet at `a=0`.

Proof of (5.2): since `M(r(a))=aK(a)` and `(aK)'=J`, Lagrange-Bürmann gives

\[
[r^{k+1}]M(r)
=\frac1{k+1}[a^k]J(a)F(a)^{-(k+1)/\beta}.
\]

Differentiating `M` in `r` and using `M'(r)=pi tilde g_alpha(r)` gives (5.2).

By (2.5) and (5.1), each finite Taylor coefficient on the right of (5.2) is a finite algebraic/Bell-polynomial expression in the Gamma values appearing in (1.2).  Therefore:

**All-jet theorem.** For every `0<alpha<2` and every integer `N>=0`,

\[
\boxed{
g_\alpha(\rho)=\sum_{k=0}^N c_{\alpha,k}\rho^{2k}+o(\rho^{2N}),
}
\tag{5.3}
\]

with every `c_{alpha,k}` explicitly computable from finitely many Gamma values by (5.2).

This moves the frozen campaign metric `M_jet` from `1` to `+infinity` in the precise sense that **every finite jet order is now proved explicit**.

### Checks at orders 0, 1, 2

Order zero recovers the source value

\[
\boxed{
\pi c_{\alpha,0}=m_1^2m_\beta^{-1/\beta}.
}
\tag{5.4}
\]

Order one gives

\[
\boxed{
\pi c_{\alpha,1}
=2m_\beta^{-2/\beta}
\left(\frac{m_1^3m_{\beta+1}}{m_\beta}-m_2^2\right),
}
\tag{5.5}
\]

exactly reproducing the previous run's independently derived curvature coefficient.

For a nontrivial new finite check, put

\[
A=\frac{m_1m_{\beta+1}}{m_\beta},\qquad
B=\frac{m_2m_{\beta+2}}{m_\beta}.
\]

Then (5.2) gives

\[
\boxed{
\pi c_{\alpha,2}=m_\beta^{-3/\beta}
\left[
3m_3^2-6m_2^2A
+\frac32m_1^2\bigl((\beta+3)A^2-(\beta+1)B\bigr)
\right].
}
\tag{5.6}
\]

All quantities in (5.6) are explicit Gamma functions through (1.2).

## 6. Special certificate at alpha=1

For `alpha=1`, `beta=1/2` and `c_beta=sqrt(pi)`.  The preceding run reduced the fixed-point equation to

\[
1=\int_0^\infty
\frac{e^{-\sqrt\pi\,y_*(r)s}}
{\sqrt{\pi/4+rs^2}}\,ds.
\tag{6.1}
\]

With `a=r/y_*(r)^2`, set `z=pi/(2sqrt(a))`.  The change of variables

\[
t=\frac{\sqrt\pi}{2\sqrt a}\sinh u
\]

gives

\[
F(a)=\frac1{\sqrt a}\int_0^\infty e^{-z\sinh u}\,du.
\tag{6.2}
\]

Using the classical Schlaefli representation

\[
\int_0^\infty e^{-z\sinh u}\,du
=\frac\pi2\bigl(\mathbf H_0(z)-Y_0(z)\bigr),\qquad z>0,
\]

where `mathbf H_0` is the Struve function and `Y_0` the Bessel function of the second kind,

\[
\boxed{
F(a)=\frac\pi{2\sqrt a}
\left[\mathbf H_0\!\left(\frac\pi{2\sqrt a}\right)
-Y_0\!\left(\frac\pi{2\sqrt a}\right)\right].
}
\tag{6.3}
\]

Consequently

\[
\boxed{
r(a)=
\left\{\frac\pi2
\left[\mathbf H_0\!\left(\frac\pi{2\sqrt a}\right)
-Y_0\!\left(\frac\pi{2\sqrt a}\right)\right]\right\}^2.
}
\tag{6.4}
\]

Thus the `alpha=1` finite-radius fixed point is eliminated in standard named special functions, not merely at the origin.

## 7. Exact scope and remaining gap

What is proved here:

1. the BCC scalar fixed point is globally eliminated by the monotone parameter `a=r/Y`;
2. the full radial CDF and density are given parametrically by (2.3), (3.5), (3.6);
3. the two scalar functions needed in that parameterization have explicit Mellin-Barnes transforms (4.4), (4.6);
4. every finite Taylor coefficient of `g_alpha` at zero has an explicit Gamma-function formula (5.2), so `M_jet=+infinity`;
5. at `alpha=1`, the radial map itself reduces to standard Struve/Bessel functions.

What is **not** claimed:

- that a monotone Mellin-Barnes parameterization meets every intended meaning of the source phrase “known explicitly”;
- that the inverse `a=a(r)` is itself a standard named special function for arbitrary irrational `beta`;
- that these identities are absent from all later literature; the bounded literature search is only negative evidence;
- source-level closure, independent P26 audit, distinct OTHER-track audit, or paper-package completion.

The sharper remaining mathematical question is therefore no longer the BCC fixed point.  It is whether the globally explicit monotone map `r(a)=aF(a)^{1/beta}` can be inverted in an accepted closed class, or whether the parametric CDF/density representation itself should count as the explicit identification requested by the survey.
