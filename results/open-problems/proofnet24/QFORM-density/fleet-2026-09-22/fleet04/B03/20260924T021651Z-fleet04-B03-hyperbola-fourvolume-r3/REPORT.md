SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B03, 2026-09-24T02:16:51Z.
attacking: dependence-safe hyperbolic-edge peel with fourth-order Schur-volume cancellation, consuming the completed fleet01/B03 bipartite Moyal receiver at a literal inequality.

# fleet04/B03 — hyperbolic-edge / fourth-order Schur-volume cancellation

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW_SUPPORTING_THEOREM / FLEET01_APPLIED / FULL_QFORM_OPEN / CONTINUITY_NOT_CLAIMED`.

The unrestricted conjecture remains open. All coordinates below are original independent real variables with probability densities bounded by one. No moment, support, smoothness, Gaussian, or post-rotation independence assumption is used.

## 1. Sources and corrections

The required Claude directory was checked through its latest directory commit `7ffd1ed79398611eb06752f622be0ce33dcacb5a`; the designated base remains `e5f71d79eff325201dd0274053d20268ce65b837`. Retained corrections: no law-uniform pointwise quadratic decay, no separation of dependent \(X-X'\) and \(X+X'\), no arbitrary-joint coarea height bound, and no assumption of a universally good physical minor.

The completed fleet01/B03 theorem used below is `QFORM-BIPARTITE-MOYAL-CS-v1`, at `math-open-problems@6c4698000d4fd206b465a18231ba8c7a8f643f59`. For a four-coordinate residual
\[
R=X^TCX+2X^TBY+Y^TDY+\text{affine},\qquad X,Y\in\mathbb R^2,
\]
with literal original-coordinate banks and invertible \(B\), it proves
\[
\sup_s\mathbb E|R-s|^{-1/2}\le4\sqrt2\,|\det B|^{-1/4}.
\tag{1.1}
\]
Its proof uses the exact Moyal identity and one global Cauchy--Schwarz inequality, retaining each conjugate sum/difference pair jointly.

For the aggregate branch I use the completed marginal-free theorem `QFORM-Z2-HALFRIESZ-MARGINAL-FREE-v1`, at `math-open-problems@68e6d8f52d904033878f6f55c376c38fd214684e`:
\[
\sup_s\mathbb E|R-s|^{-1/2}\le8e^{1/4}Z_2^{-1/8},
\qquad Z_2=e_2(MM^T).
\tag{1.2}
\]

## 2. Translation-uniform hyperbola peel

### Lemma 2.1

Let \(U,V\) be independent cap-one variables and \(a,b\in\mathbb R\). For \(\mu\ne0\),
\[
Y=2\mu(U+a)(V+b)
\]
has a density satisfying
\[
\boxed{p_Y(y)\le\sqrt2\,|\mu|^{-1/2}|y|^{-1/2}}
\tag{2.1}
\]
for almost every \(y\ne0\), uniformly in \(a,b\).

After translating, write the densities as \(f,g\). For \(W=(U+a)(V+b)\),
\[
p_W(w)=\int_{\mathbb R}f(u)g(w/u)\,\frac{du}{|u|}.
\]
On \(|u|\ge\sqrt{|w|}\), use \(g\le1\) and \(\int f=1\), giving at most \(|w|^{-1/2}\). On \(|u|<\sqrt{|w|}\), substitute \(v=w/u\), then use \(f\le1\) and \(\int g=1\), giving the same bound. Thus \(p_W(w)\le2|w|^{-1/2}\), and scaling gives (2.1).

If \(Z\) is independent of \(U,V\) and
\[
Q=2\mu[U+\alpha(Z)][V+\beta(Z)]+R(Z),
\tag{2.2}
\]
then conditioning only on \(Z\) and mixing interval probabilities gives
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}
\le\sqrt2\,|\mu|^{-1/2}\sup_s\mathbb E|R-s|^{-1/2}.}
\tag{2.3}
\]
This is an essential-density statement. No continuity follows merely from the random-center mixture.

## 3. Exact physical Schur formulation

Let \(A\) be symmetric and \(H=\{h_1,h_2\}\) a physical pair with
\[
A[H,H]=
\begin{pmatrix}0&\mu\\ \mu&0\end{pmatrix}
=:B_H,\qquad\mu\ne0.
\tag{3.1}
\]
Put \(K=H^c\), \(C=A[H,K]\), and
\[
S=A[K,K]-C^TB_H^{-1}C.
\tag{3.2}
\]
Exact completion in the two original coordinates of \(H\), including arbitrary affine terms, gives
\[
X^TAX+\ell^TX+c
=
2\mu[U+\alpha(Z)][V+\beta(Z)]
+\bigl(Z^TSZ+\eta^TZ+c'\bigr).
\tag{3.3}
\]
Thus (2.3) applies to the full affine Schur residual. Conditioning on ambient outside original coordinates merely changes affine terms and is harmless.

## 4. Single fourth-order minor and exact cancellation

Choose disjoint two-element sets \(I,J\subset K\) such that \(S[I,J]\) is invertible. Define
\[
\Delta_{H;I,J}=\det A[H\cup I,H\cup J].
\tag{4.1}
\]
The block determinant identity yields
\[
\Delta_{H;I,J}=\det(B_H)\det S[I,J]
=-\mu^2\det S[I,J].
\tag{4.2}
\]

Apply the completed fleet01/B03 theorem (1.1) to the residual using the literal original-coordinate banks \(I,J\), while conditioning on all remaining residual coordinates. Equations (1.1), (2.3), and (4.2) give
\[
\begin{aligned}
\|p_Q\|_{\infty,\mathrm{ess}}
&\le\sqrt2|\mu|^{-1/2}\cdot4\sqrt2|\det S[I,J]|^{-1/4}\\
&=8|\mu|^{-1/2}\left(\frac{|\Delta_{H;I,J}|}{|\mu|^2}\right)^{-1/4}.
\end{aligned}
\]
The hyperbola coefficient cancels exactly:
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}
\le8\,|\Delta_{H;I,J}|^{-1/4}.}
\tag{4.3}
\]
This is the requested actual application of the completed fleet01/B03 theorem.

## 5. Aggregate fourth-order Schur volume

Define
\[
\mathcal F_4(H)=
\sum_{\substack{I,J\subset K,\ |I|=|J|=2\\I\cap J=\varnothing}}
\det A[H\cup I,H\cup J]^2.
\tag{5.1}
\]
By (4.2),
\[
\mathcal F_4(H)=
\mu^4
\sum_{\substack{|I|=|J|=2\\I\cap J=\varnothing}}
\det S[I,J]^2.
\tag{5.2}
\]

Choose a random Bernoulli cut \(K=L\sqcup R\). Cauchy--Binet gives
\[
Z_2(S[L,R])=
\sum_{\substack{I\subset L,\ J\subset R\\|I|=|J|=2}}
\det S[I,J]^2.
\tag{5.3}
\]
For each fixed disjoint ordered \(I,J\), the inclusion event has probability \(1/16\). Hence
\[
\mathbb E_{L|R}Z_2(S[L,R])
=\frac{\mathcal F_4(H)}{16\mu^4}.
\tag{5.4}
\]
Some physical cut has at least this value. Apply (1.2) on that literal cut and then (2.3):
\[
\begin{aligned}
\|p_Q\|_{\infty,\mathrm{ess}}
&\le8\sqrt2\,e^{1/4}|\mu|^{-1/2}Z_2^{-1/8}\\
&\le8\sqrt2\,e^{1/4}|\mu|^{-1/2}
\left(\frac{16\mu^4}{\mathcal F_4(H)}\right)^{1/8}.
\end{aligned}
\]
Again \(\mu\) cancels:
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}
\le16e^{1/4}\mathcal F_4(H)^{-1/8}
<20.545\,\mathcal F_4(H)^{-1/8}.}
\tag{5.5}
\]

## 6. Concrete full-target inequality

Consider the six-coordinate principal block
\[
A_*=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\oplus
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}.
\tag{6.1}
\]
Its spectrum is three \(+1\)'s and three \(-1\)'s. Taking \(H=\{1,2\}\), \(I=\{3,4\}\), \(J=\{5,6\}\), one has \(|\Delta_{H;I,J}|=1\). Therefore
\[
\boxed{\|p_{X^TA_*X}\|_{\infty,\mathrm{ess}}\le8}
\tag{6.2}
\]
for every admissible product law.

The same bound holds for every ambient symmetric extension containing \(A_*\) as this principal block: conditioning outside changes only affine terms. By interlacing, every such extension has at least three eigenvalues at least \(1\) and at least three at most \(-1\), so it lies in the full target class.

## 7. Remaining implication

The former missing half-power is now supplied by a genuine physical hyperbola, while the completed fleet01 Moyal theorem supplies the residual half-Riesz resource. The determinant identity aggregates the scales before inversion and removes a potentially tiny \(\mu\).

The new paid exits are:

- a zero-diagonal hyperbolic pair plus one literal disjoint fourth-order mixed minor, (4.3);
- the same pair plus aggregate disjoint fourth-volume, (5.5).

Full QFORM remains open because \(s_3(A)\ge1\) alone has not been shown to force \(\mathcal F_4(H)\gtrsim1\) for some zero-diagonal physical pair, nor to force this branch versus an already-paid diagonal, pivot, hub, ridge, or crossing exit. A general indefinite pair with nonzero diagonal cannot be sheared into (3.1) probabilistically without losing product structure. Continuity is not claimed.
