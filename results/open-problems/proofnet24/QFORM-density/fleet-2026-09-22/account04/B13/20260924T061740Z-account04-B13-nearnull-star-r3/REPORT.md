SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 04, slot B13, 2026-09-24T06:17:40Z.

# B13 report: near-null pivots force physical star energy

Run: 20260924T061740Z-account04-B13-nearnull-star-r3

## Scope and source pins

The target remains the full statement: independent real coordinates with probability densities at most one, arbitrary real symmetric \(A\), and at least three singular values of \(A\) at least one. Essential boundedness is the target here; continuity is separate.

Required base source retained:

- math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}.
- math-open-problems@7e23bcf74fa1862bfe9054591c946bfd8f3276cb, account01/B13 scalar Schur receiver.
- math-open-problems@635da12cb1c19b27c455c662be800eb1113dd845, account04/B13 fifth-diagonal sparsification.

The prior corrections are enforced: no post-rotation independence, no arbitrary-joint coarea estimate, no pointwise quadratic characteristic-function decay, no treatment of a small quadratic tail as a small random error, and no continuity inference from essential boundedness alone.

## 1. Optimizer-free transfer

For bounded measurable \(K\ge0\), every cap-one product law can be purified coordinate by coordinate, in supremal form, to unit-measure indicator factors:
\[
\int K(x)\prod_{j=1}^n f_j(x_j)\,dx
\le
\sup_{|E_1|=\cdots=|E_n|=1}
\int K(x)\prod_{j=1}^n{\bf1}_{E_j}(x_j)\,dx.
\]
Indeed, for every nonnegative section \(g\) and \(0\le f\le1\) with \(\int f=1\),
\[
\int gf\le\sup_{|E|=1}\int_Eg.
\]
At each coordinate choose only an \(\varepsilon/n\)-near maximizer, and then let \(\varepsilon\downarrow0\). No global maximizer or threshold attainment on the infinite line is used. Regularity gives bounded finite-union approximants when required.

## 2. Near-null pivot star-energy lemma

Let
\[
A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad
c_i:=\|u_i\|^2\le\frac13.
\]
Fix \(k\), and write
\[
d=d_k,\quad u=u_k,\quad c=\|u\|^2,\quad
a=A_{kk}=d+u^T\Lambda u.
\]
If \(U_0\) is \(U\) with row \(k\) removed, then the actual off-diagonal star is
\[
q=A_{-k,k}=U_0\Lambda u.
\]
Since \(U_0^TU_0=I_2-uu^T\succeq(1-c)I_2\),
\[
\begin{aligned}
\|q\|_2^2
&=(\Lambda u)^T(I_2-uu^T)(\Lambda u)\\
&\ge(1-c)\|\Lambda u\|^2\\
&\ge\frac{1-c}{c}(u^T\Lambda u)^2\\
&=\frac{1-c}{c}(d-a)^2.
\end{aligned}
\]
For \(c=0\), \(a=d\), so the near-null branch with \(|d|\ge1\) is impossible. For \(0<c\le1/3\),
\[
\boxed{
\|A_{-k,k}\|_2
\ge\sqrt{\frac{1-c}{c}}\,|d-a|
\ge\sqrt2\,(|d|-|a|)_+ .
}
\]
Thus exact cancellation \(a=0\), \(|d|\ge1\), forces
\[
\boxed{\|A_{-k,k}\|_2\ge\sqrt2.}
\]

## 3. Actual account01/B13 inequality

In the exact target chamber \(s_3(A)\ge1\), the rank-two perturbation cannot approximate \(A\) within operator norm below one. Hence
\[
\|D\|_{\rm op}=\max_i|d_i|\ge1.
\]
Choose \(k\) attaining this maximum. For every slab witness of ratio \(\rho\), account01/B13 gives
\[
|a\det\Lambda|\le1536e^2\rho^{-4}.
\]
Therefore,
\[
|\det\Lambda|\ge3072e^2\rho^{-4}
\quad\Longrightarrow\quad
|a|\le\frac12
\quad\Longrightarrow\quad
\boxed{\|A_{-k,k}\|_2\ge2^{-1/2}}.
\]
Equivalently every witness satisfies
\[
\boxed{
|\det\Lambda|<3072e^2\rho^{-4}
\quad\text{or}\quad
\|A_{-k,k}\|_2\ge2^{-1/2}.
}
\]
The first branch is a scale-correct near-rank-one latent packet; the second is a fixed physical star bank. The optimizer-free purification transfers this conclusion to arbitrary rough cap-one product laws.

## 4. Finite core versus outside bank

Let \(C\) contain the four indices with largest \(|d_i|\), with \(k\in C\). The fifth-diagonal theorem gives
\[
\|D_{C^c}\|_{\rm op}\le2\sqrt{30\pi}\,\rho^{-1}.
\]
This tail remains inside the quadratic phase.

On the non-near-rank-one branch,
\[
\|A_{C\setminus\{k\},k}\|_2^2+\|A_{C^c,k}\|_2^2
=\|A_{-k,k}\|_2^2\ge\frac12.
\]
Therefore
\[
\boxed{\|A_{C\setminus\{k\},k}\|_2\ge\frac12}
\quad\text{or}\quad
\boxed{\|A_{C^c,k}\|_2\ge\frac12}.
\]
So either the literal four-coordinate core contains a fixed star, or the retained outside coordinates contain a fixed-energy dense star bank despite their \(O(\rho^{-1})\) diagonal coefficients.

## 5. Remaining debt

This removes the false obstruction that a near-zero actual pivot is automatically unusable. The unrestricted conjecture remains open. The next receiver must consume either the four-coordinate core star with all affine terms retained, or the dense outside star together with arbitrary same-bank self-couplings and the diagonal tail. Treating that remainder as separable would be invalid. Continuity remains separate.
