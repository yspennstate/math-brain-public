SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T02:36:39Z.
attacking: one-null-diagonal Schur mixed edges; extend the bilinear logarithmic-potential receiver without using continuity to obtain height, then audit the ruled rough-input bridge.

# account02/B15 — one-null-diagonal logarithmic-potential extension

Programme: `QFORM-DENSITY-3EIG-20260922`. Full QFORM remains OPEN.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The local B15 gap is now narrower than the exact-zero-diagonal chamber: after the theorem below, the unpaid Schur interface is a genuinely indefinite two-coordinate remainder in which **both physical Schur diagonal coefficients are nonzero**, unless a product-preserving structural reduction first exposes a one-null edge, a semidefinite rank-two bank, a grouped crossing, or another already-paid receiver. The live correction `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1` forbids treating arbitrary same-bank quadratic curvature as harmless slope innovation.

Globally, the owner target remains the universal bound for arbitrary independent cap-one marginals and symmetric A with at least three eigenvalues of modulus at least one. Aggregate-before-inversion structural routing remains unpaid.

## 2. New theorem: arbitrary one-sided nonlinear term does not hurt the affine-bilinear logarithmic potential

Define, for q>0,

\[
\Phi(q)=
\begin{cases}
2q\left(2+\log\frac1{2q}\right),&0<q\le \frac12,\\
2+\log(2q),&q\ge\frac12.
\end{cases}
\]

### Theorem 2.1 — `QFORM-ONE-SIDED-NONLINEAR-BILINEAR-LOG-POTENTIAL-v1`

Let U,V be independent real random variables with probability densities bounded by one. Let s != 0, let F:R->R be arbitrary measurable, and let beta,gamma be arbitrary reals. Put

\[
T=2sUV+F(U)+\beta V+\gamma.
\]

Then for every L>0,

\[
\boxed{
\sup_{t\in\mathbb R}\mathbb E\log_+\frac{L}{|T-t|}
\le \Phi\!\left(\frac{L}{|s|}\right).
}
\tag{2.1}
\]

This strictly extends account03/B15 auto30's affine-bilinear theorem: the U-dependence may be completely arbitrary. Only the V-dependence must remain affine after conditioning.

### Proof

Translate U in the ORIGINAL coordinate:

\[
U'=U+\frac{\beta}{2s}.
\]

Then U' remains independent of V with density cap one and

\[
T=2sU'V+\widetilde F(U')+\gamma
\]

for another arbitrary measurable function \widetilde F. Divide by |s| and absorb signs/constants into the target point. It is enough to show, with q=L/|s|, that for every measurable center function a(u),

\[
\mathbb E\log_+\frac{q}{|2UV-a(U)|}\le\Phi(q).
\tag{2.2}
\]

Condition on U=u. For u != 0, 2uV has a probability density bounded by c_u=(2|u|)^{-1}. The kernel y -> log_+(q/|y-a(u)|) is symmetric decreasing about a(u). By the one-dimensional bathtub principle, among probability densities bounded by c_u its integral is maximized by the cap c_u on the centered interval of length 1/c_u=2|u|. Hence, uniformly in the center a(u),

\[
\mathbb E\left[\left.\log_+\frac{q}{|2uV-a(u)|}\right|U=u\right]
\le g_q(u),
\]

where

\[
g_q(u)=
\begin{cases}
1+\log(q/|u|),&0<|u|\le q,\\
q/|u|,&|u|\ge q.
\end{cases}
\tag{2.3}
\]

The function g_q is symmetric and nonincreasing in |u|. A second bathtub application to the cap-one law of U gives

\[
\mathbb E g_q(U)\le\int_{-1/2}^{1/2}g_q(u)\,du.
\]

For q>=1/2 this integral is 2+log(2q). For 0<q<=1/2 it is

\[
2\int_0^q[1+\log(q/u)]\,du+2\int_q^{1/2}\frac q u\,du
=2q\left(2+\log\frac1{2q}\right).
\]

This proves (2.1). No regularity of F and no smoothness of either marginal is used. QED.

## 3. Physical-pair consequence: only one Schur diagonal must vanish

Split ORIGINAL coordinates as X=(P,Z), P=(X_1,X_2), and write

\[
A=\begin{pmatrix}D&B\\B^T&C\end{pmatrix},
\qquad
S=C-B^TD^{-1}B,
\]

where D is an invertible indefinite physical 2x2 block. Let

\[
\Delta=|\det D|,\qquad \kappa=\sigma_{\min}(D).
\]

Assume there are two remaining ORIGINAL coordinates U,V such that

\[
S_{VV}=0,\qquad s:=S_{UV}\ne0,
\tag{3.1}
\]

while S_UU and every other entry of S are arbitrary.

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-ONE-NULL-SCHUR-EDGE-v1`

For arbitrary independent cap-one marginals, the full quadratic form Q=X^TAX has an essentially bounded density and, for every r>0,

\[
\boxed{
\|p_Q\|_\infty
\le \frac{2\sqrt2}{r}
+\Delta^{-1/2}\Phi\!\left(\frac{2r^2}{\kappa|s|}\right).
}
\tag{3.2}
\]

Equivalently, with q=2r^2/(\kappa|s|),

\[
\boxed{
\|p_Q\|_\infty
\le4(\kappa|s|)^{-1/2}q^{-1/2}+\Delta^{-1/2}\Phi(q),\quad q>0.
}
\tag{3.3}
\]

In particular q=1/2 gives

\[
\boxed{
\|p_Q\|_\infty\le\frac{4\sqrt2}{\sqrt{\kappa|s|}}+\frac2{\sqrt\Delta}.
}
\tag{3.4}
\]

If \kappa|s|<=8\Delta, optimizing the large-q branch at q_*=4\Delta/(\kappa|s|) gives

\[
\boxed{
\|p_Q\|_\infty
\le\frac{4+\log(8\Delta/(\kappa|s|))}{\sqrt\Delta}.
}
\tag{3.5}
\]

### Proof

Complete the physical pair in the original coordinates. The completed account03/B15 physical-pair logarithmic envelope gives conditionally on Z=z

\[
p_{Q|Z=z}(t)
\le \frac{2\sqrt2}{r}
+\Delta^{-1/2}
\log_+\frac{2r^2}{\kappa|t-R(z)|},
\tag{3.6}
\]

where R(z)=z^TSz+\ell^Tz+c.

Now condition on every coordinate of Z except U,V. For each fixed outside value W=w, (3.1) makes

\[
R_w(U,V)=S_{UU}U^2+2sUV+\alpha_wU+\beta_wV+\gamma_w.
\tag{3.7}
\]

Apply Theorem 2.1 with

\[
F_w(U)=S_{UU}U^2+\alpha_wU,
\qquad L=2r^2/\kappa.
\]

The bound is uniform in w,t and all affine coefficients. Average (3.6) over U,V and then W. This proves (3.2); the remaining formulas are algebraic optimization exactly as in the zero-two-diagonal chamber.

The Schur 2x2 principal block on U,V is

\[
\begin{pmatrix}S_{UU}&s\\s&0\end{pmatrix}
\]

with determinant -s^2, hence rank(S)>=2 and, since D is nonsingular, rank(A)=2+rank(S)>=4. Thus any separately established same-constant rank>=3 C0 compiler may be invoked **after** (3.2) is paid. Continuity is not used to establish the height. QED.

## 4. Concrete exact-target payment

Let X,Y,U,V be arbitrary independent cap-one variables and

\[
\boxed{Q=4XY+U^2+2UV.}
\tag{4.1}
\]

Its matrix is block diagonal with

\[
D=\begin{pmatrix}0&2\\2&0\end{pmatrix},
\qquad
S=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]

The eigenvalues are

\[
2,-2,\frac{1+\sqrt5}{2},\frac{1-\sqrt5}{2},
\]

so exactly three have modulus at least one. Here \Delta=4, \kappa=2 and s=1. Formula (3.5) therefore gives the law-uniform owner-target inequality

\[
\boxed{
\|p_Q\|_\infty
\le\frac{4+\log 16}{2}
=2+2\log2
=3.3862943611\ldots .
}
\tag{4.2}
\]

Since rank(A)=4, the completed same-constant regularity compiler may then be applied to obtain the canonical representative

\[
\boxed{p_Q\in C_0(\mathbb R),\qquad \|p_Q\|_\infty\le2+2\log2.}
\tag{4.3}
\]

The order is important: (4.2) is paid before (4.3).

## 5. Required owner-pinned ruled theorem applied to the same target

Use the completed one-sheet theorem from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, with its later correction that an affine term must lie in the quadratic range. Condition in (4.1) on the ORIGINAL coordinate V=v:

\[
Q=4XY+U^2+2vU=4XY+(U+v)^2-v^2.
\]

The active 3x3 block on (X,Y,U) is invertible with eigenvalue magnitudes (2,2,1), signature (+,+,-). Hence the affine-range condition is automatic, and U -> U+v is only an original-coordinate translation.

Taking (lambda_1,lambda_2,mu)=(2,1,2), the source coefficient equals

\[
C_+
=\frac12\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta/2+\cos^2\theta+1/2}}
=\int_0^{2\pi}\frac{d\theta}{\sqrt{4+2\cos^2\theta}}
\le\pi.
\tag{5.1}
\]

Therefore, after averaging v,

\[
\boxed{
\Pr\{Q\in I,\ Q\ge -V^2\}\le\pi|I|
}
\tag{5.2}
\]

for every interval I, and the corresponding owner-scale tent estimate is

\[
\boxed{
\mathbb E[(\varepsilon-|Q-y|)_+\mathbf1_{\{Q\ge-V^2\}}]
\le\pi\varepsilon^2.
}
\tag{5.3}
\]

This is a genuine essential-density payment for a positive majority submeasure of an exact target instance. It is not a continuity statement.

## 6. Independent ruled rough-input audit

For a general invertible active physical 3x3 block B, conditioning on all outside original coordinates W=w gives

\[
Q_w(x)=x^TBx+2d(w)^Tx+c_0(w)
=(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\]

Thus the source's affine-range requirement is automatic and square completion is an ORIGINAL-coordinate translation; independence and the cap-one property are preserved.

For arbitrary rough active marginals, mollify only those three original-coordinate densities: f_i^(eta)=f_i*gamma_eta. Then f_i^(eta)<=1 and

\[
\left\|\prod_{i=1}^3f_i^{(\eta)}-\prod_{i=1}^3f_i\right\|_1
\le\sum_{i=1}^3\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{6.1}
\]

The bound is unchanged by the conditional translation and is uniform in w. Restriction to the fixed conditional majority event and deterministic quadratic pushforward both contract total variation. Hence the smooth ruled inequality passes to the rough conditional submeasure with exactly the same coefficient, and averaging W yields the ambient interval domination. At the cone vertex there is no hidden atom because the zero set of the nonzero quadratic polynomial has Lebesgue measure zero.

The geometric factors also check independently. For q_0(z)=z_1^2+z_2^2-z_3^2 and the one-sheet ruling

\[
F(\theta,t)=\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3),
\]

one has

\[
F_\theta\times F_t=\frac12\nabla q_0(F),
\qquad
\frac{d\sigma}{|\nabla q_0|}=\frac12\,d\theta\,dt.
\]

Undoing spectral scaling produces the non-arclength direction

\[
v_\theta=\left(-\frac{\sin\theta}{\sqrt{\lambda_1}},
\frac{\cos\theta}{\sqrt{\lambda_2}},
\frac1{\sqrt\mu}\right).
\]

The line integral therefore contributes 1/|v_theta|. The two-dimensional product-projection cap 2 cancels the coarea factor 1/2 and reproduces exactly the source coefficient. No continuity of the rough output appears anywhere in this bridge.

## 7. Regularity ledger

Absolute continuity is qualitative and separate. Let q(x)=x^TAx with A != 0 and let the joint input have an L1 density F. For every null N and every ball, local coarea gives

\[
\int_{q^{-1}(N)}F(x)|\nabla q(x)|\,dx=0.
\]

Since \nabla q=2Ax vanishes only on the proper null subspace ker(A), F=0 almost everywhere on q^{-1}(N) outside a Lebesgue-null set. Hence q_#(Fdx)<<dx. This has no universal-height content.

Essential boundedness in Sections 3--5 is paid directly by logarithmic-potential/interval estimates. Continuity is a later consequence only after an L-infinity bound is already established (for example by the same-constant rank>=3 C0 compiler or by an independent original-block convolution). Therefore no continuity assertion is used to smuggle in the target bound.

## 8. State

Full QFORM: OPEN. New paid chamber: invertible indefinite physical pair plus a Schur mixed edge with at least one exact zero diagonal, allowing arbitrary curvature on the opposite Schur diagonal and arbitrary remaining couplings. First local unpaid extension: both Schur diagonals nonzero without a product-preserving reduction. Global unpaid step: structural aggregate-before-inversion routing forced solely by s_3(A)>=1.

Dependencies actually used: account03/B15 auto30 affine-bilinear logarithmic potential / physical-pair log envelope; the owner-pinned `e5f71d79...` one-sheet theorem with the later affine-range correction; and the completed same-constant C0 compiler only after height was paid.
