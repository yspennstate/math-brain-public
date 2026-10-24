# QFORM B11 — null-graph trace obstruction for overlapping parabolic smoothing

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B11, 2026-09-22T19:17:27Z.

Status: `AUXILIARY_ONLY / PRECISE_MISSING_FACTOR`. The full quadratic-form conjecture remains open. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and conditional end-to-end argument

For the canonical indefinite form

\[
T=2ZW+V^2,
\]

the matrix in coordinates \((Z,V,W)\) is

\[
H_0=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
\qquad \operatorname{spec}(H_0)=\{1,1,-1\}.
\]

If \((Z,V,W)\) has joint density \(h\), the exact coarea/change-of-variable formula is

\[
p_T(t)=\frac12\int_{w\ne0}
h\!\left(\frac{t-v^2}{2w},v,w\right)\frac{dv\,dw}{|w|}.
\tag{1}
\]

Thus the exact missing quantity in the overlapping case is the weighted parabolic null-graph trace

\[
\mathcal N(h):=\sup_t\int_{w\ne0}
h\!\left(\frac{t-v^2}{2w},v,w\right)\frac{dv\,dw}{|w|}.
\tag{2}
\]

Controlling (2) immediately gives \(\|p_T\|_\infty\le \mathcal N(h)/2\). The first essential question is whether the marginal bounds naturally available in the overlap decomposition already control (2). The answer is no, even in an exceptionally rigid form.

## 2. Exact obstruction theorem

### Theorem (`QFORM-PARABOLIC-CONDITIONAL-CAP-INSUFFICIENT-v1`)

There exist random variables \((Z,V,W)\) such that:

1. \((V,W)\) has a probability density \(g\) with \(0\le g\le1\);
2. there is a random variable \(U\), independent of \((V,W)\), uniform on \([0,1]\), and a measurable function \(\phi\) for which
   \[
   Z=U+\phi(V,W);
   \]
   in particular every regular conditional density of \(Z\) given \((V,W)=(v,w)\) is a translate of \(1_{[0,1]}\), hence is bounded by one;
3. nevertheless \(T=2ZW+V^2\) has an unbounded density at zero.

Consequently, a bounded two-dimensional transverse density together with a uniform conditional density cap for the third direction does not control an indefinite rank-three quadratic pushforward. Genuine separation in the partner theorem cannot be replaced by those two caps.

### Construction and proof

For \(k\ge1\), set

\[
W_k=(2^{-k-1},2^{-k}),\qquad |W_k|=2^{-k-1},
\]

and choose pairwise disjoint intervals \(V_k\) of length \(|V_k|=1/k\). Put

\[
R_k=V_k\times W_k,\qquad
m_*:=\sum_{k\ge1}|R_k|
=\sum_{k\ge1}\frac{2^{-k-1}}k=\frac12\log2<1.
\]

Choose one further rectangle \(R_*\), disjoint from all \(R_k\), contained in \(\{1<w<2\}\), and having area \(1-m_*\). Define

\[
g(v,w)=1_{R_*}(v,w)+\sum_{k\ge1}1_{R_k}(v,w).
\]

Then \(g\le1\) and \(\int g=1\). Let \((V,W)\) have density \(g\), let \(U\sim\mathrm{Unif}[0,1]\) be independent, and set

\[
Z=-\frac{V^2}{2W}+U.
\]

Since \(W>0\) on the support, this is well defined and

\[
2ZW+V^2=2WU.
\tag{3}
\]

For \(t>0\), (3) gives

\[
p_T(t)=\int g(v,w)\frac{1_{0<t<2w}}{2w}\,dv\,dw.
\tag{4}
\]

If \(t<2^{-K-1}\), then every rectangle \(R_k\), \(1\le k\le K\), lies in \(\{2w>t\}\). Therefore

\[
\begin{aligned}
p_T(t)
&\ge \sum_{k=1}^K\frac1k\frac12
\int_{2^{-k-1}}^{2^{-k}}\frac{dw}{w}\\
&=\frac{\log2}{2}\sum_{k=1}^K\frac1k.
\end{aligned}
\tag{5}
\]

The right side diverges as \(K\to\infty\), so \(p_T(t)\to\infty\) as \(t\downarrow0\). This proves the theorem.

The joint density itself is explicit:

\[
h(z,v,w)=g(v,w)
1_{\{0\le z+v^2/(2w)\le1\}},
\]

and satisfies \(h\le1\). Thus even a three-dimensional joint density cap does not control the cone trace, consistently with the existing arbitrary-joint cone-tube correction.

## 3. Application of the completed account01/B11 theorem

The assigned partner's completed theorem applies when original coordinates split into independent banks \(I,J\),

\[
Z=u\cdot X_I,\qquad V=v\cdot X_J,\qquad W=w\cdot X_J,
\]

with \(\sigma=\|u\|_2>0\) and

\[
\Delta=\sqrt{\|v\|_2^2\|w\|_2^2-\langle v,w\rangle^2}>0.
\]

For nonzero \(\alpha,\beta\), it gives the actual target-level inequality

\[
\boxed{
\|p_{2\alpha ZW+\beta V^2}\|_\infty
\le 3\,2^{4/3}e
\bigl(|\alpha|\sigma\sqrt{|\beta|}\,\Delta\bigr)^{-2/3}.}
\tag{6}
\]

This is the rigorous mechanism by which the third direction removes the rank-two logarithmic singularity in the support-separated branch: the scalar smoother and transverse plane retain genuine bank independence, and parabolic weak-\(L^{3/2}\) smoothing turns the logarithmic endpoint into a bounded density.

The new theorem above shows exactly why (6) cannot be extended by merely observing in an overlapping representation that

\[
\sup_{v,w}\|p_{Z\mid V=v,W=w}\|_\infty\le L,
\qquad
\|p_{V,W}\|_\infty\le M.
\]

Those facts permit the conditional translate to track the null graph \(z=-v^2/(2w)\) across dyadic scales, recreating the harmonic logarithm.

## 4. Consequence for the account01/B11 antipodal-block representation

In the partner's exact many-small-pair representation,

\[
Z=\sqrt c\,X_0+a\sum_jS_j,\quad
V=b\sum_j\cos\theta_jD_j,\quad
W=b\sum_j\sin\theta_jD_j,
\]

where the \((S_j,D_j)\) are independent two-dimensional blocks with joint density at most \(1/2\). The independent \(X_0\) indeed implies the valid conditional cap

\[
\|p_{Z\mid V,W}\|_\infty\le c^{-1/2}.
\]

Also, the independent differences \(D_j\) give a dimension-free joint projection bound for \((V,W)\) whenever the coefficient area is nonzero. The obstruction theorem proves that these two estimates alone are still insufficient. The remaining product-specific obligation is now precisely:

\[
\boxed{
\sup_t\int_{w\ne0}
h\!\left(\frac{t-v^2}{2w},v,w\right)\frac{dv\,dw}{|w|}
\le C}
\tag{7}
\]

for joint laws \(h\) arising from the independent cap-one-half \((S_j,D_j)\) blocks and the extra independent scalar smoother. Any proof must prevent multiscale tracking of the nonlinear null graph; marginal or conditional supremum bounds cannot do that.

## 5. Scope and regularity

This is not a counterexample to QFORM: the constructed nonlinear dependence is not asserted to be a linear image of independent cap-one original coordinates. It is a rigorous counterexample to a tempting intermediate compiler and identifies the exact missing weighted trace.

The partner theorem (6) proves an essentially bounded density in its separated-bank branch. Continuity is not obtained by either (6) as currently stated or this obstruction analysis. The unrestricted universal constant and the stronger continuity assertion remain open.

## 6. Source state

- Owner control: revision `2026-09-22.13`, programme `QFORM-DENSITY-3EIG-20260922` revision `2026-09-22.5`.
- Assignment: account04/B11, indefinite signatures.
- Assigned partner used: account01/B11 run `20260922T184134Z-account01-B11-QFORM-r13`, canonical report commit `28cbaf1aaaa988d89c7ee4d421da6dd58e883211`.
- Live correction inbox blob before publication: `6335a8d51fc8081123635a8d0848738b615cb082`.
- Native brain status: `WITHOUT_VERIFIED_BRAIN`.

