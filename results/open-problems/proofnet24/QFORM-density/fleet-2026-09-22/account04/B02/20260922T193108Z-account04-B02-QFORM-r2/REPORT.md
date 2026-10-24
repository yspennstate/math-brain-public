SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 04, slot B02, 2026-09-22T19:31:08Z.
attacking: continuity and complete integration in the zero-diagonal physical-triple branch, bypassing the rejected target-wide unweighted L1 Fourier route.

# account04/B02 — continuous zero-diagonal triple theorem

Run: \`20260922T193108Z-account04-B02-QFORM-r2\`  
Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Fresh owner control: revision \`2026-09-22.13\`, observed main head \`363546ab35feb95c7666bfefbacab53fcbc1daac\`  
Status: \`ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN\`

## 1. Exact target and Fourier status

The full target is unchanged: for arbitrary dimension, arbitrary independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal density bound or give a valid counterexample. Continuity is a separate requested conclusion.

The fresh owner control rejects the target-wide unweighted criterion
\[
 \int_{\mathbb R}\left|\mathbb E e^{itX^TAX}\right|\,dt<\infty
\]
as a universal proof route. This report does not revive it and does not use a pointwise oscillatory-decay claim. I do not promote the owner's uniform-ball illustration into a new exact-product counterexample; the positive result below works directly with densities. Its Fourier consequence is the valid integrated \(L^2\) estimate, not an \(L^1\) assertion.

## 2. Source-pinned partner result

The completed designated partner result is account01/B02,
\`QFORM-ZERO-DIAGONAL-TRIPLE-v1\`, canonical report
\[
\texttt{yspennstate/math-open-problems@168c80d9837ca68e580ae9b750defb2b45504093}
\]
at
\[
\texttt{proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/}
\]
\[
\texttt{20260922T162035Z-account01-B02-qform-auto11/REPORT.md}.
\]

It proves: if a physical principal \(3\times3\) block \(B\) is nonsingular and has a zero diagonal entry, then, with arbitrary outside variables, quadratic terms, cross couplings and induced affine perturbations,
\[
 \|p_Q\|_\infty\le 3\,2^{2/3}|\det B|^{-1/3}.
 \tag{2.1}
\]
It records only essential boundedness and explicitly leaves continuity unproved. The same proof gives
\[
 \|\phi_Q\|_2^2\le 6\pi\,2^{2/3}|\det B|^{-1/3}.
 \tag{2.2}
\]

This run applies the partner's exact density formula and its two complementary estimates to prove continuity.

## 3. New theorem

### Theorem — \`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1\`

Let \(X=(X_1,\ldots,X_n)\) have independent real coordinates with probability densities \(0\le f_i\le1\). Let \(A\) be any real symmetric matrix. Suppose some physical principal block \(B=A[I,I]\), \(|I|=3\), is nonsingular and has a zero diagonal entry. Then \(Q=X^TAX\) has a continuous probability density satisfying
\[
 \boxed{\ \|p_Q\|_\infty
 \le 3\,2^{2/3}|\det B|^{-1/3}.\ }
 \tag{3.1}
\]
No sign condition, support condition, moment condition, or restriction on the matrix outside \(I\) is imposed.

Thus the partner constant is retained exactly while the separately requested continuity conclusion is added on this whole branch.

## 4. Conditional three-variable normal form

Relabel the selected physical coordinates as \(x,y,z\), with
\[
 B=\begin{pmatrix}
 0&a&b\\
 a&c&d\\
 b&d&e
 \end{pmatrix},
 \qquad D:=|\det B|>0.
\]
Condition on every coordinate outside \(I\). The conditional polynomial differs from the selected quadratic form only by arbitrary affine terms. The partner reduction sets
\[
 \rho^2=a^2+b^2,\qquad r_0=ay+bz,\qquad w=-by+az,
\]
and translates \(r=r_0+\ell_1\). Since \(D>0\), \(\rho>0\). The conditional polynomial is
\[
 P(x,r,w)=2xr+h(r,w),
 \tag{4.1}
\]
where, for every fixed \(r\),
\[
 h(r,w)=\gamma(w-\omega(r))^2+\eta(r),
 \qquad |\gamma|=D/\rho^4>0.
 \tag{4.2}
\]
The transformed \((r,w)\)-density \(g(r,w)\) satisfies
\[
 0\le g\le\rho^{-2},\qquad \iint g(r,w)\,dr\,dw=1.
 \tag{4.3}
\]
Write
\[
 m(r)=\int_{\mathbb R}g(r,w)\,dw,\qquad \int m(r)\,dr=1.
 \tag{4.4}
\]

For \(r\ne0\), integration in \(x\) gives the partner's exact slice density
\[
 k_r(s)=\int_{\mathbb R}
 \frac{g(r,w)}{2|r|}
 f_1\!\left(\frac{s-h(r,w)}{2r}\right)\,dw.
 \tag{4.5}
\]
The conditional output density is \(p_{\rm cond}(s)=\int k_r(s)\,dr\).

## 5. Each fixed-\(r\) slice is continuous

Fix \(r\ne0\). Push the finite measure \(g(r,w)\,dw\) forward under \(w\mapsto h(r,w)\). Because \(\gamma\ne0\), this pushforward is absolutely continuous. A density is
\[
 a_r(u)=
 {\bf1}_{\{\gamma(u-\eta(r))>0\}}
 \frac{
 g(r,\omega(r)+q_r(u))+
 g(r,\omega(r)-q_r(u))
 }{2\sqrt{|\gamma|\,|u-\eta(r)|}},
 \tag{5.1}
\]
where \(q_r(u)=\sqrt{(u-\eta(r))/\gamma}\) on the displayed one-sided support. The value at the critical point is irrelevant. By the one-dimensional area formula,
\[
 a_r\in L^1(\mathbb R),\qquad \|a_r\|_1=m(r).
 \tag{5.2}
\]

Define the scaled input density
\[
 b_r(v)=\frac1{2|r|}f_1\!\left(\frac{v}{2r}\right).
 \tag{5.3}
\]
Then \(b_r\in L^1\cap L^\infty\), \(\|b_r\|_1=1\), and
\[
 \|b_r\|_\infty\le\frac1{2|r|}.
 \tag{5.4}
\]
Equation (4.5) is exactly
\[
 k_r=a_r*b_r.
 \tag{5.5}
\]

This convolution is continuous even though the original input densities are merely measurable. Indeed,
\[
 \sup_s|k_r(s+h)-k_r(s)|
 \le \|\tau_h a_r-a_r\|_1\,\|b_r\|_\infty
 \longrightarrow0
 \quad(h\to0),
 \tag{5.6}
\]
by translation continuity in \(L^1\). Therefore \(k_r\) is uniformly continuous for every \(r\ne0\).

## 6. An integrable domination in \(r\)

The partner proof gives, uniformly in \(s\) and in every affine perturbation,
\[
 k_r(s)\le \frac{\sqrt2}{\sqrt D\,\sqrt{|r|}},
 \tag{6.1}
\]
using \(g\le\rho^{-2}\), the translated-square rearrangement estimate, and \(|\gamma|=D/\rho^4\). Dropping \(f_1\le1\) also gives
\[
 k_r(s)\le\frac{m(r)}{2|r|}.
 \tag{6.2}
\]

Fix any \(R>0\). Combine these as
\[
 0\le k_r(s)\le G_R(r):=
 \frac{\sqrt2}{\sqrt D\,\sqrt{|r|}}{\bf1}_{\{|r|\le R\}}
 +\frac{m(r)}{2|r|}{\bf1}_{\{|r|>R\}}.
 \tag{6.3}
\]
This majorant is integrable:
\[
 \int G_R(r)\,dr
 \le \frac{4\sqrt2\sqrt R}{\sqrt D}+\frac1{2R}.
 \tag{6.4}
\]

Since every \(k_r\) is continuous and (6.3) is independent of \(s\), dominated convergence yields
\[
 p_{\rm cond}(s)=\int k_r(s)\,dr
 \quad\text{continuous in }s.
 \tag{6.5}
\]
The same domination verifies directly that this continuous representative is a probability density.

Optimizing (6.4), exactly as in the partner proof, gives
\[
 \|p_{\rm cond}\|_\infty
 \le 3\,2^{2/3}D^{-1/3}.
 \tag{6.6}
\]

## 7. Removing the outside conditioning

Let \(U\) denote all original coordinates outside \(I\). For almost every \(u\), the preceding argument produces a continuous conditional density \(p_u(s)\). The quadratic block \(B\), \(D\), \(\rho\), and \(\gamma\) are unchanged by conditioning; outside couplings produce only the affine terms already allowed above. Hence
\[
 0\le p_u(s)\le M:=3\,2^{2/3}D^{-1/3}
 \quad\text{for all }s
 \tag{7.1}
\]
for almost every \(u\).

The unconditional density is
\[
 p_Q(s)=\mathbb E[p_U(s)].
 \tag{7.2}
\]
For \(s_j\to s\), \(p_U(s_j)\to p_U(s)\) almost surely and is dominated by \(M\). Bounded convergence gives \(p_Q(s_j)\to p_Q(s)\). Thus \(p_Q\) is continuous and (7.1) gives (3.1).

This step retains independence only in the original coordinates. It does not assert independence after the \((y,z)\mapsto(r,w)\) change; its Jacobian and the transformed joint density are explicit in (4.3).

## 8. Integrated Fourier consequence

Since \(p_Q\) is a probability density and obeys (3.1),
\[
 \|p_Q\|_2^2\le\|p_Q\|_\infty.
\]
Plancherel therefore gives the genuine integrated estimate
\[
 \boxed{\ 
 \int_{\mathbb R}|\phi_Q(t)|^2\,dt
 \le 6\pi\,2^{2/3}|\det B|^{-1/3}.
 \ }
 \tag{8.1}
\]
The continuity proof is physical-space integration, not an illicit inference from \(L^2\) Fourier control. No \(L^1\) characteristic-function conclusion is claimed.

## 9. Scope and first unpaid implication

This theorem closes the continuity debt on every branch carrying a nonsingular physical \(3\times3\) principal block with an exact zero diagonal, allowing arbitrary outside spectrum and couplings. It is a strict strengthening of the designated partner theorem with the same constant.

It is not the full conjecture. The bare three-large-eigenvalue assumption does not force a uniformly large fixed physical determinant; the singleton-plus-two-banks and diffuse determinant-bank corrections rule out that shortcut. The first remaining implication is still structural:

* aggregate a diffuse zero-diagonal determinant bank before paying reciprocal local-minor costs; or
* extract a dimension-free ridge, grouped-square, or indefinite-pair/Schur-pivot resource.

When such an exact zero-diagonal atom is extracted, both boundedness and continuity are now fully paid by (3.1).

## 10. Corrections honored

This proof does not use law-uniform pointwise van der Corput decay, a target-wide unweighted Fourier \(L^1\) bound, post-rotation independence, generic bounded projected density in place of product provenance, fiber-sup integration, a fixed-good-minor dichotomy, or positive conditional projection-height moments. It is compatible with the live near-zero half-Riesz correction because it treats the exact zero diagonal and uses the full product-coordinate density formula.
