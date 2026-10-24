SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-23T15:17:02Z.
attacking: rough-law continuity for the first pivoted hyperbolic-plus-square branch, uniformly through a zero/nonzero physical pivot and arbitrary outside-generated affine terms.

# account04/B15 r6 — pivot-neutral Lp convolution and C0 density

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260923T151702Z-account04-B15-pivoted-convolution-r6\`  
Status: \`NEW TARGET-VALID CONTINUOUS-DENSITY BRANCH / FULL QFORM OPEN\`  
Execution: \`WITHOUT_VERIFIED_BRAIN\`.

## 1. Scope and sources

Fresh control was read from \`yspennstate/math-research-brain@b2319f995a345e05be5da359e598f2329017f627\`. The correction inbox forbids post-rotation independence, pointwise quadratic Fourier decay, arbitrary-joint coarea, and treating a small matrix coefficient as a small random error for unbounded inputs. None is used.

The completed account01/B15 tent-scale regularity theorem is used at an actual inequality from
\`yspennstate/math-open-problems@92df77d33efcd04deeac76ec140f17608ad9d9d5\`,
\`proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260923T141230Z-account01-B15-QFORM-auto11/REPORT.md\`.

The physical-space fractional bathtub and square estimates are taken from the completed account01/B14 report at
\`yspennstate/math-open-problems@fa932fcf67bfc41d6df2175ac7043158aba8c9a9\`,
\`proofnet24/QFORM-density/fleet-2026-09-22/account01/B14/20260923T141444Z-account01-B14-QFORM-r38/REPORT.md\`.

The newest-Claude source files remain pinned at \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`, with blobs \`62e20ee976ddeb3f42d3ee5befd6ed49edc917a5\`, \`9da148eed6cd43b1046a6f91d0f9329e12921cb4\`, and \`ee721b237e206f31298b1871979faaab37a1bac2\`.

## 2. Pivot-neutral hyperbolic Lp lemma for arbitrary rough laws

Let \(X,Y\) be independent real variables with probability densities \(0\le f,g\le1\). Let \(b\ne0\), while \(a,u,v,c\in\mathbb R\) are arbitrary, and set
\[
T=aX^2+2bXY+2uX+2vY+c.
\tag{2.1}
\]
Then for every \(1<p<\infty\), \(T\) has a density and
\[
\boxed{\quad \|p_T\|_p\le p\,|b|^{-1+1/p}.\quad}
\tag{2.2}
\]
In particular,
\[
\|p_T\|_3\le3|b|^{-2/3}.
\tag{2.3}
\]

### Proof

Put \(\alpha=1-1/p\). Conditional on \(X=x\), (2.1) is an affine function of \(Y\):
\[
T=2(bx+v)Y+d(x),\qquad d(x)=ax^2+2ux+c.
\]
For almost every \(x\), its conditional density is
\[
k_x(t)=\frac1{|2(bx+v)|}
g\!\left(\frac{t-d(x)}{2(bx+v)}\right).
\]
The exceptional point \(x=-v/b\) is null for the law of \(X\). Minkowski's integral inequality and \(\|g\|_p\le1\) give
\[
\|p_T\|_p
\le
\int f(x)\,|2(bx+v)|^{-\alpha}\,dx.
\tag{2.4}
\]
The account01/B14 fractional bathtub estimate, uniformly in every shift \(r\), is
\[
\int f(x)|x-r|^{-\alpha}dx\le\frac{2^\alpha}{1-\alpha}=p\,2^\alpha.
\tag{2.5}
\]
Substituting \(r=-v/b\) into (2.4), the powers of two cancel:
\[
\|p_T\|_p
\le(2|b|)^{-\alpha}p2^\alpha
=p|b|^{-\alpha}.
\]
This proves (2.2).

The proof is already valid for arbitrary measurable density versions: it uses conditional pushforward densities only almost everywhere and integrates them by Tonelli/Minkowski. It never evaluates a projected density on a curve or surface. Alternatively, mollifying \(f,g\) preserves mass and the cap, and the uniform \(L^p\) estimate passes to the weak limit by lower semicontinuity. Thus no smoothness, support, moment, or interval-extremality assumption is hidden.

The same-coordinate curvature \(aX^2\) and affine term \(2uX+c\) merely translate each \(Y\)-fiber. They cost exactly zero, for arbitrary \(a\), rather than being treated as a small random error.

## 3. A disjoint square receiver

Let \(Z\) be independent of \((X,Y)\), with density bounded by one, and let \(\gamma\ne0\), \(w\in\mathbb R\). Put
\[
S=\gamma Z^2+2wZ.
\tag{3.1}
\]
Completing the square and applying account01/B14's rough square estimate gives
\[
\boxed{\quad \|p_S\|_{3/2}\le2|\gamma|^{-1/3}.\quad}
\tag{3.2}
\]
This estimate is uniform in \(w\), fragmented support, translations, and unbounded tails.

Since \(T\) and \(S\) are independent, Young-Hölder convolution at conjugate exponents \(3\) and \(3/2\) yields
\[
\boxed{\quad
\|p_{T+S}\|_\infty
\le6|b|^{-2/3}|\gamma|^{-1/3}.
\quad}
\tag{3.3}
\]

## 4. Continuity is genuinely proved on this branch

For \(1<p<\infty\), convolution maps \(L^p*L^{p'}\) into \(C_0(\mathbb R)\). Indeed,
\[
\sup_x|(F*G)(x+h)-(F*G)(x)|
\le \|\tau_hF-F\|_p\|G\|_{p'}\to0,
\tag{4.1}
\]
and compactly supported approximations in \(L^p,L^{p'}\) imply vanishing at infinity. Applying this to \(p_T\in L^3\) and \(p_S\in L^{3/2}\) proves
\[
\boxed{\quad p_{T+S}\in C_0(\mathbb R).\quad}
\tag{4.2}
\]

Now let \(W\) be any collection of the remaining original independent coordinates and suppose the physical principal block on \((X,Y,Z)\) is
\[
B(a,b,\gamma)=
\begin{pmatrix}
a&b&0\\
b&0&0\\
0&0&\gamma
\end{pmatrix},
\qquad b\gamma\ne0.
\tag{4.3}
\]
All outside quadratic coefficients and all couplings from \(W\) to \(X,Y,Z\) are arbitrary. Conditioning on \(W=w\) creates exactly arbitrary affine coefficients \(u(w),v(w),w_3(w)\) and an output constant. Sections 2–3 therefore give a conditional density \(p_w\in C_0\) with the uniform cap
\[
0\le p_w(x)\le6|b|^{-2/3}|\gamma|^{-1/3}.
\tag{4.4}
\]
The unconditional density
\[
p_Q(x)=\mathbb E\,p_W(x)
\tag{4.5}
\]
is continuous by dominated convergence, and tends to zero as \(|x|\to\infty\), again by dominated convergence applied to the pointwise \(C_0\) limit of each \(p_w\). Hence
\[
\boxed{
p_Q\in C_0(\mathbb R),\qquad
\|p_Q\|_\infty\le6|b|^{-2/3}|\gamma|^{-1/3}.
}
\tag{4.6}
\]
Translations and kernel leakage generated by all outside coordinates are retained exactly. Independence is used only among the original coordinate groups \((X,Y)\), \(Z\), and \(W\).

## 5. Actual application of completed account01/B15

Let
\[
K_\varepsilon(x)=\frac{(\varepsilon-|x|)_+}{\varepsilon^2}.
\]
Account01/B15 proves both the exact height characterization and the \(C_0\) convergence criterion. Applied to (4.6), they give the concrete inequalities
\[
\boxed{
\sup_{0<\varepsilon\le1}\|K_\varepsilon*\mu_Q\|_\infty
=\|p_Q\|_\infty
\le6|b|^{-2/3}|\gamma|^{-1/3},
}
\tag{5.1}
\]
and the genuine desmoothing statement
\[
\boxed{
\lim_{\varepsilon\downarrow0}
\|K_\varepsilon*p_Q-p_Q\|_\infty=0.
}
\tag{5.2}
\]
Thus this branch proves continuity rather than merely absolute continuity or an essential density cap. No uniform rate in (5.2) is claimed, consistent with account01/B15's phase-aligned obstruction to source-uniform shrinking-scale desmoothing.

## 6. A full-target family crossing the null pivot

The eigenvalues of the \(2\times2\) block in (4.3) are
\[
\lambda_\pm=\frac{a\pm\sqrt{a^2+4b^2}}2.
\]
Both have modulus at least one exactly when
\[
b^2\ge |a|+1.
\tag{6.1}
\]
Consequently, if \(b^2\ge|a|+1\) and \(|\gamma|\ge1\), the physical principal block itself has three eigenvalues of modulus at least one. Cauchy interlacing places every ambient extension with arbitrary outside block and couplings inside the owner's target class. For every admissible cap-one product law,
\[
\boxed{
p_{X^TAX}\in C_0(\mathbb R),\qquad
\|p_{X^TAX}\|_\infty
\le6|b|^{-2/3}|\gamma|^{-1/3}\le6.
}
\tag{6.2}
\]
The parameter \(a\) may be zero, nonzero, or cross zero; the analytic constant does not change. This resolves the nonzero-pivot regularity issue on the first product-preserving physical branch.

## 7. What remains

The unrestricted conjecture is still open. The new result requires an actual original-coordinate principal pattern (4.3), in particular a zero \(Y^2\) coefficient and a disjoint square coordinate. A general near-null physical core can have dense transverse self-coupling, so it need not reduce to this pattern without rotating independent inputs. The remaining task is to replace the zero \(Y^2\) structure by a grouped-coordinate or slice estimate that preserves original-coordinate independence and retains the same \(L^p\)-convolution regularity.

Continuity remains separate in the general theorem. It is proved here only for the stated branch, with no universal modulus.

## 8. Integrity

- Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.
- New theorem: pivot-neutral affine \(L^p\) estimate (2.2).
- New target-valid branch: (6.2), including arbitrary outside spectrum and couplings.
- Rough inputs are handled directly at the density/measure level; no pointwise surface trace is used.
- No moments, support bounds, Gaussian assumption, post-rotation independence, or small-random-error argument is used.
