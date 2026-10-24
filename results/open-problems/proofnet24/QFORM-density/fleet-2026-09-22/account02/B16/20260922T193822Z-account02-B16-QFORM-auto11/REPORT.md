SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T19:38:22Z.
attacking: the owner-revision-15 decoupled L^3/Hölder bridge, specifically whether three conditional factors can be controlled uniformly in the difference fiber without losing the product-law weight.

# account02/B16 — weighted conditional L^3 disintegration and the square-root gap

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: `Projection-product interaction`.
Status: **supporting theorem + source-valid correction; full QFORM remains OPEN / NOT PROVED**.
Control used for this proof before publication: `yspennstate/math-research-brain@6de9595a16521f1e0e1dfacdd89db1daa7af9843`, OWNER CONTROL revision `2026-09-22.15`.
Execution memory: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and the first unpaid implication

Let

\[
\phi_A(t)=\mathbb E e^{itX^TAX}
\]

for independent real coordinates with densities bounded by one.  For an independent copy \(X'\), set

\[
U=X-X',\qquad V=X+X'.
\]

Then

\[
X^TAX-X'^TAX'=U^TAV=\sum_j (AU)_jV_j.
\]

Since the coordinate pairs \((X_j,X'_j)\) are independent, conditional on the full vector \(U\) the variables \(V_j\) are conditionally independent.  Hence, with

\[
\psi_{j,u}(s):=\mathbb E(e^{isV_j}\mid U_j=u),
\]

one has the exact polarization identity

\[
\boxed{
|\phi_A(t)|^2
 =\mathbb E_U\prod_j\psi_{j,U_j}(t(AU)_j).
}
\tag{1.1}
\]

The owner-revision-15 proposal is to exploit three \(L^3\) factors in this product.  The first unpaid point is whether those conditional \(L^3\) norms are uniform in \(U\) and whether three factors actually give the required \(L^1(dt)\) bound for \(\phi_A\).

They do not.  The correct statement retains the density of the difference fiber.

## 2. A sharp source-valid one-coordinate weighted L^3 estimate

### Theorem `QFORM-DECOUPLED-CONDITIONAL-L3-WEIGHT-v1`

Let \(X,X'\) be iid with a probability density \(f\) satisfying \(0\le f\le1\).  Put

\[
U=X-X',\qquad V=X+X'.
\]

Let \(m\) be the density of \(U\).  For a.e. \(u\) with \(m(u)>0\), let \(g_u\) be the conditional density of \(V\mid U=u\) and let

\[
\psi_u(s)=\int e^{isv}g_u(v)\,dv.
\]

Then

\[
\boxed{
 m(u)\int_{\mathbb R}|\psi_u(s)|^3\,ds\le \pi.
}
\tag{2.1}
\]

Consequently, for every nonzero real \(a\),

\[
\boxed{
 m(u)|a|\int_{\mathbb R}|\psi_u(at)|^3\,dt\le\pi.
}
\tag{2.2}
\]

#### Proof

The change of variables

\[
(x,x')=\left(\frac{v+u}{2},\frac{v-u}{2}\right)
\]

has Jacobian \(1/2\).  Therefore the joint density of \((U,V)\) is

\[
r(u,v)=\frac12f\!\left(\frac{v+u}{2}\right)
              f\!\left(\frac{v-u}{2}\right),
\tag{2.3}
\]

so

\[
0\le r(u,v)\le\frac12,
\qquad
m(u)=\int r(u,v)\,dv\le1.
\tag{2.4}
\]

For \(m(u)>0\), \(g_u(v)=r(u,v)/m(u)\).  Thus

\[
\int g_u(v)^{3/2}\,dv
 =m(u)^{-3/2}\int r(u,v)^{3/2}\,dv
 \le m(u)^{-3/2}2^{-1/2}\int r(u,v)\,dv
 =(2m(u))^{-1/2}.
\tag{2.5}
\]

Hence

\[
\|g_u\|_{3/2}\le(2m(u))^{-1/3}.
\tag{2.6}
\]

With Fourier convention \(\widehat g(s)=\int e^{isv}g(v)\,dv\), Hausdorff--Young in the normalization already used in the current QFORM programme gives

\[
\|\psi_u\|_3\le(2\pi)^{1/3}\|g_u\|_{3/2}.
\tag{2.7}
\]

Cubing (2.7) and using (2.6) gives exactly (2.1).  The scaling \(s=at\) gives (2.2).  No independence of \(U\) and \(V\), no moment condition, and no support condition is used.  QED.

The scaling \(m(u)^{-1/3}\) of the conditional \(L^3\) norm is not an artifact; the next section gives an exact family with this blow-up.

## 3. Uniform-in-U conditional L^3 is false already for iid uniforms

### Correction `QFORM-DECOUPLING-UNIFORM-U-L3-FALSE-v1`

Take \(X,X'\) iid uniform on \([0,1]\).  For \(|u|<1\), write

\[
\ell(u)=1-|u|.
\]

Then

\[
m(u)=\ell(u),
\tag{3.1}
\]

and \(V\mid U=u\) is uniform on the interval

\[
[|u|,2-|u|]=[1-\ell(u),1+\ell(u)].
\]

Thus

\[
\psi_u(s)=e^{is}\frac{\sin(\ell(u)s)}{\ell(u)s}.
\tag{3.2}
\]

Let

\[
C_{\rm sinc}:=\int_{\mathbb R}\left|\frac{\sin r}{r}\right|^3dr,
\qquad 0<C_{\rm sinc}<\infty.
\]

Then

\[
\boxed{
\int|\psi_u(s)|^3ds=\frac{C_{\rm sinc}}{\ell(u)}.
}
\tag{3.3}
\]

So \(\|\psi_u\|_3\to\infty\) as \(|u|\uparrow1\).  After the frequency scaling that actually occurs in (1.1), the failure is even stronger.  For the diagonal form \(A=I_3\), take a difference fiber with

\[
U_1=U_2=U_3=\varepsilon\in(0,1).
\]

Since \((AU)_j=\varepsilon\),

\[
\int_{\mathbb R}
\prod_{j=1}^3|\psi_{\varepsilon}(t\varepsilon)|\,dt
 =\frac{C_{\rm sinc}}{\varepsilon(1-\varepsilon)}.
\tag{3.4}
\]

Therefore

\[
\boxed{
\sup_U\int\prod_{j=1}^3
|\psi_{j,U_j}(t(AU)_j)|\,dt=\infty
}
\tag{3.5}
\]

even for the completely separable target-class example \(A=I_3\) with iid unit uniforms.  The divergence occurs both at small difference \(\varepsilon\downarrow0\), through the scale factor \((AU)_j\), and near the edge \(\varepsilon\uparrow1\), through the collapsing conditional fiber.

This does **not** refute QFORM or the decoupling identity.  It refutes only the proposed uniform-in-\(U\) three-factor implementation.

## 4. The exact weighted three-factor inequality

Let the coordinates be arbitrary independent cap-one laws, and let \(m_j\) be the density of \(U_j=X_j-X'_j\).  Fix three physical indices \(J=\{j_1,j_2,j_3\}\).  For a full difference vector \(u\), put

\[
a_j=(Au)_j.
\]

Since every conditional characteristic function has modulus at most one, three-factor Hölder and (2.2) give, in the extended sense when one \(a_j=0\),

\[
\begin{aligned}
\int_{\mathbb R}\prod_k
 |\psi_{k,u_k}(t a_k)|\,dt
&\le
\prod_{j\in J}
\|\psi_{j,u_j}(a_j\cdot)\|_3\\
&\le
\boxed{
\pi
\left[
\prod_{j\in J}m_j(u_j)|a_j|
\right]^{-1/3}.
}
\end{aligned}
\tag{4.1}
\]

Thus the product-law compensation is not a uniform conditional bound; it is the **difference-density weight** \(m_j(u_j)\) carried together with the physical frequency \((Au)_j\).

Taking absolute values in (1.1), Tonelli, and (4.1) yields the honest conditional implication

\[
\boxed{
\int_{\mathbb R}|\phi_A(t)|^2dt
\le
\pi\,
\mathbb E_U
\left[
\prod_{j\in J}
\{m_j(U_j)|(AU)_j|\}^{-1/3}
\right],
}
\tag{4.2}
\]

whenever the right side is finite.

This is a useful exact interface, but it also exposes the exponent gap: three conditional \(L^3\) factors after one polarization naturally control \(|\phi_A|^2\) in \(L^1\), i.e. \(\phi_A\) in \(L^2\).  Fourier inversion needs \(\phi_A\in L^1\).

There is no valid step replacing

\[
|\phi_A(t)|=\sqrt{\mathbb E_U Z_U(t)}
\]

by \(\mathbb E_U\sqrt{Z_U(t)}\) from above; concavity gives the reverse inequality

\[
\mathbb E_U\sqrt{Z_U(t)}\le\sqrt{\mathbb E_U Z_U(t)}.
\tag{4.3}
\]

So a direct three-factor Hölder argument applied only after this single decoupling loses a square root.  A fixed-fiber argument on \(\sqrt{Z_U}\) would formally require six \(L^3\) factors, not three.  This is an algebraic warning about the proposed implementation, not a proof that every joint decoupling/cancellation route fails.

## 5. Designated partner result actually applied

The newest completed designated-partner result read in full is account03/B16 run `20260922T185149Z-account03-B16-QFORM-r15`, canonical mathematics

`yspennstate/math-open-problems@3ef9d49fd04c756ea20b5f7c6e1d5c24dd579780`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T185149Z-account03-B16-QFORM-r15/REPORT.md`.

Its theorem `QFORM-SCALAR-PIVOT-DIFFUSE-SCHUR-BRIDGE-v1` proves that for an original-coordinate pivot

\[
A=\begin{pmatrix}\alpha&b^T\\ b&C\end{pmatrix},\qquad
S=C-bb^T/\alpha,
\]

if \(\alpha\ne0\), \(S\) has two eigenvalues of modulus at least \(\mu\), and the \(\mu/64\) Schur spectral window has maximum coordinate leverage at most \(1/32\), then

\[
\boxed{
\|p_{X^TAX}\|_\infty<27(|\alpha|\mu)^{-1/2}.
}
\tag{5.1}
\]

Moreover under the target normalization \(s_3(A)\ge1\), the stable-pivot factorization supplies

\[
\mu=(1+\|b\|/|\alpha|)^{-2}.
\tag{5.2}
\]

I use this theorem as an actual branch elimination: whenever (5.1)--(5.2) and the diffuse-window condition hold, no new decoupling estimate is needed.  The weighted decoupling interface (4.1)--(4.2) is therefore aimed only at the complementary branch in which every usable stable pivot has a heavy Schur spectral-window coordinate/group.  This keeps the new obligation in original physical coordinates rather than rotating the independent inputs.

## 6. What remains unpaid

The new theorem does not prove a universal \(L^1\) characteristic-function estimate.  The precise surviving bridge is:

**`QFORM-WEIGHTED-DECOUPLING-L1-BRIDGE-v1` (OPEN).**  Starting from (1.1), exploit the product difference densities \(m_j(U_j)\), the physical frequencies \((AU)_j\), and the three-large-singular-value condition \(s_3(A)\ge1\) to bound

\[
\int_{\mathbb R}\sqrt{
\mathbb E_U\prod_j
|\psi_{j,U_j}(t(AU)_j)|
}\,dt
\]

by a universal constant, at least on the complement of the completed diffuse-Schur branch (5.1).

A source-valid solution must aggregate the \(U\)-fibers before a worst-case fiber supremum and must overcome the square-root loss in (4.3).  It may not assume that projected coordinates are independent.  The uniform-in-\(U\) shortcut is now explicitly excluded by (3.4).

## 7. Scope and correction status

The proof uses only original-coordinate product structure, exact polarization, a two-dimensional Jacobian, Hausdorff--Young, and Hölder.  It does not use the refuted arbitrary-joint rank-three coarea statement, positive conditional-projection moments, pointwise scalar van der Corput, independence after rotation, or a fiberwise normalized density supremum.

This report establishes a supporting theorem and a correction to one proposed implementation.  It is **not** a counterexample to the quadratic-form conjecture.  The full target and the requested continuous-representative conclusion remain open.
