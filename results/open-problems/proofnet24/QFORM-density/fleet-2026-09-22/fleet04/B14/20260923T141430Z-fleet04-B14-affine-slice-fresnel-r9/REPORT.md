SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B14, 2026-09-23T14:14:30Z.
attacking: translation-uniform slice-Fresnel closure of the heavy physical null branch, including conditioning-generated affine terms and kernel leakage.

# fleet04/B14 r9 — affine and kernel-leakage stability of the slice-Fresnel receiver

**Programme:** \`QFORM-DENSITY-3EIG-20260922\`  
**Status:** \`SUPPORTING_THEOREM_PROVED / CONDITIONING_INTERFACE_CLOSED_ON_HEAVY-NULL-DIFFUSE-BRANCH / FULL_QFORM_OPEN\`  
**Continuity:** only absolute continuity with an essentially bounded density is proved here; continuity is not asserted.  
**Execution:** \`WITHOUT_VERIFIED_BRAIN\`.

## 1. Result

This report proves that the new slice-Fresnel estimate is completely stable under arbitrary affine perturbations in the original physical coordinates. In particular, affine terms created by conditioning outside a physical core may have an arbitrary component in the kernel of the rank-three quadratic coefficient map. That component is not discarded or assumed to factor: it becomes a coordinatewise translation in the product Fourier integral, and the geometric Brascamp-Lieb constant is translation invariant.

The result supplies the missing conditioning interface for the residual-diffuse exact-rank-three heavy physical null-pivot branch.

## 2. Normal form with arbitrary affine leakage

Let
\[
A=RMR^T,\qquad R^TR=I_3,\qquad s_{\min}(M)\ge s>0.
\]
Assume an original coordinate \(0\) has leverage
\[
c=\|r_0\|^2>\frac12
\]
and exact physical null pivot \(A_{00}=0\). Rotate only the deterministic three-dimensional coefficient space so that \(r_0=\sqrt c\,e_1\). After a transverse rotation,
\[
M=\begin{pmatrix}0&b&0\\ b&\alpha&\delta\\0&\delta&\gamma\end{pmatrix},
\qquad |b|\ge s,\quad |\gamma|\ge s.
\tag{2.1}
\]
For \(j\ne0\), write \(r_j=(u_j,v_j,w_j)\), put
\[
T=\xi\cdot X_{-0},\quad V=v\cdot X_{-0},\quad W=w\cdot X_{-0},
\]
where \(u=\sqrt\rho\,\xi\), \(\rho=1-c\), and assume the residual-diffuse gate
\[
v_j^2+w_j^2\le\frac12\qquad(j\ne0).
\tag{2.2}
\]
Allow an arbitrary affine perturbation
\[
2q_0X_0+2g\cdot X_{-0}+q_\emptyset,
\qquad g\in\mathbb R^{n-1}.
\tag{2.3}
\]
No requirement is placed on the component of \(g\) orthogonal to \(\operatorname{span}\{u,v,w\}\).

Shearing only the deterministic phase, set
\[
z=w+\frac{\delta}{\gamma}v,\qquad Z=z\cdot X_{-0},\qquad
\kappa=\alpha-\frac{\delta^2}{\gamma}.
\]
Then
\[
Q=2X_0(hV+q_0)+Y_g,
\qquad h=b\sqrt c,
\tag{2.4}
\]
where
\[
Y_g=\gamma Z^2+2b\sqrt\rho\,VT+\kappa V^2+2g\cdot X_{-0}+q_\emptyset.
\tag{2.5}
\]

## 3. Translation-uniform slice theorem

For almost every \(l\), let \(\mu_{l,g}\) be the unnormalised distribution of \(Y_g\) on the physical hyperplane \(V=l\).

### Theorem 3.1 — \`QFORM-AFFINE-SLICE-FRESNEL-BL-v1\`

For every interval \(I\subset\mathbb R\), every \(g\in\mathbb R^{n-1}\), and almost every \(l\),
\[
\boxed{
\mu_{l,g}(I)
\le C_*|\gamma|^{-1/2}|I|^{1/2},
\qquad
C_*=4e^{1/8}2^{-1/4}\Gamma(1/4)<13.819.
}
\tag{3.1}
\]
The constant is independent of \(g,l,\rho\), the supports and tails of the input laws, and the ambient dimension.

### Proof

For \(t\ne0\), Fresnel linearisation of the single square \(\exp(it\gamma Z^2)\), followed by Fourier inversion in the normal coordinate of \(V=l\), gives
\[
|\widehat\mu_{l,g}(t)|
\le (4\pi|\gamma t|)^{-1/2}\frac1{2\pi}
\int_{\mathbb R^2}
\prod_{j\ne0}
\left|
\widehat f_j\!\left(sv_j+qz_j+2tb\sqrt\rho\,l\,\xi_j+2tg_j\right)
\right|\,ds\,dq.
\tag{3.2}
\]
The constant term and the \(\kappa l^2\) term have modulus one and disappear.

Let \(G\) be the Gram matrix of the columns \((v,z)\). The deterministic shear has determinant one, hence
\[
\det G=1,\qquad
c_j=(v_j,z_j)G^{-1}(v_j,z_j)^T=v_j^2+w_j^2\le\frac12,
\qquad \sum_jc_j=2.
\tag{3.3}
\]
The geometric Brascamp-Lieb inequality allows arbitrary translations in each one-dimensional factor. Therefore the shifts
\[
a_j=2tb\sqrt\rho\,l\,\xi_j+2tg_j
\]
cost exactly nothing:
\[
\int_{\mathbb R^2}\prod_j
|\widehat f_j(sv_j+qz_j+a_j)|\,ds\,dq
\le
\prod_{c_j>0}
\left(
c_j^{-1/2}\int_{\mathbb R}|\widehat f_j(\omega)|^{1/c_j}\,d\omega
\right)^{c_j}.
\tag{3.4}
\]
Using the newest-Claude cap-one Fourier inequality
\[
\int_{\mathbb R}|\widehat f(\omega)|^p\,d\omega\le\frac{4\pi}{\sqrt p},
\qquad p\ge2,
\tag{3.5}
\]
with \(p=1/c_j\), every bracket in (3.4) is at most \(4\pi\). Thus the two-dimensional integral in (3.2) is at most \((4\pi)^2\), uniformly in the entire affine vector \(g\). Consequently
\[
|\widehat\mu_{l,g}(t)|
\le4\sqrt\pi\,|\gamma t|^{-1/2}.
\tag{3.6}
\]
The Gaussian interval majorant and Fourier inversion now give (3.1), exactly as in the unshifted slice theorem.

For rough cap-one densities, convolve each \(f_j\) with a smooth approximate identity. The cap and mass are preserved. The absolute product-Fourier majorant above justifies the smooth calculation, and Fatou at the interval-measure level passes (3.1) to the original laws. No pointwise trace of an arbitrary density version is used. \(\square\)

## 4. Conditioning-generated affine terms are paid

The physical hub term in (2.4) is
\[
2X_0(hV+q_0).
\]
Changing the slice variable from \(V\) to \(L=hV+q_0\) changes the unnormalised slice constant by \(1/|h|\), but the translation \(q_0\) costs nothing. Applying the completed single-hub receiver to (3.1) yields
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
\frac12+
\frac{2\sqrt2\,C_*}{|b|\sqrt c\,\sqrt{|\gamma|}}.
}
\tag{4.1}
\]
At unit active scale \(s=1\), \(c>1/2\) gives
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<55.776.}
\tag{4.2}
\]
More generally the right side of (4.1) scales correctly with \(b,\gamma\).

This proves that, after conditioning arbitrary outside coordinates, dense outside couplings may generate any affine vector on the retained heavy-null diffuse core, including a non-factorable kernel component, without changing the receiver constant.

## 5. Equation-level application of completed fleet01/B05 mathematics

Apply fleet01/B05's exact pure-longitudinal absorption theorem at
\[
\texttt{math-open-problems@cd496fb2379767ef3ef467399080762d2000b921}.
\]
In its heavy-null regime \(c>127/128\), absorption and whitening give
\[
c_*=\frac{c}{c+\rho_M}\ge c,\qquad s_{\min}(B_*)\ge c.
\tag{5.1}
\]
Writing the resulting null normal form as in (2.1),
\[
|b_*|\ge c,\qquad |\gamma_*|\ge c.
\tag{5.2}
\]
The affine-stable estimate (4.1), applied to the retained variables, therefore gives the concrete inequality
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le\frac12+\frac{2\sqrt2\,C_*}{c^2}
<
40.22,
\qquad c>\frac{127}{128}.
}
\tag{5.3}
\]
This has no reciprocal loss in the mixed-support mass \(\rho_M\), including \(\rho_M\downarrow0\). In the pure quadratic subbranch fleet01/B05 also gives
\[
\|p_Q\|_\infty\le12(|\det B|\rho_M)^{-1/3}
\tag{5.4}
\]
under its leave-one-out gate; (5.3) is the complementary diffuse-slice payment and is uniform at the endpoint.

Scope warning: if one first absorbs a pure-longitudinal bank, arbitrary affine terms on that discarded bank cannot simply be forgotten. Inequality (5.3) applies after absorption only when those terms have already been retained or eliminated by an authorized conditioning/factorisation step. The unconditional affine theorem is (4.1), which does not perform that absorption.

## 6. What remains

This closes the translation and kernel-leakage interface for the residual-diffuse exact-rank-three heavy **exact-null** branch. It does not close:

1. a small nonzero physical pivot uniformly as it tends to zero;
2. the arbitrary-rank reduction to an exact-rank-three physical core;
3. the full coordinate-core extraction from only \(s_3(A)\ge1\);
4. continuity of the density.

The full conjecture remains open. The next local obstruction is the nonzero near-null pivot: its quadratic hub term cannot be called a small random error under unbounded inputs. A valid continuation must spend that curvature jointly with the slice geometry.

## 7. Sources actually used

- fleet02/B05 affine-free slice-Fresnel theorem and heavy-null closure:
  \`math-open-problems@c3b4b7a16269706cd53d6950a9b13a7f27d08dd2\`;
- fleet01/B05 pure-longitudinal absorption:
  \`math-open-problems@cd496fb2379767ef3ef467399080762d2000b921\`;
- newest-Claude one-dimensional Fourier inequality:
  \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`,
  \`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.

No independence after rotation, conditional density cap for a projected pair, moment assumption, support restriction, arbitrary-joint coarea theorem, or small-random-error argument is used.
