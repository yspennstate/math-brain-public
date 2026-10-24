# account04/B13 handoff — near-null pivot star energy

Run: 20260924T061740Z-account04-B13-nearnull-star-r3  
Mathematics: yspennstate/math-open-problems@c30866924d918185e908ae4b3e22e31169366296  
Report: proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T061740Z-account04-B13-nearnull-star-r3/REPORT.md

Required base source retained: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/.

## New result

In the exact diffuse rank-two chamber
\[
A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad \max_i\|u_i\|^2\le\frac13,
\]
choose \(k\) with \(|d_k|=\|D\|_{\rm op}\ge1\), and set \(a=A_{kk}\). The actual physical star obeys
\[
\|A_{-k,k}\|_2
\ge\sqrt{\frac{1-c_k}{c_k}}\,|d_k-a|
\ge\sqrt2\,(|d_k|-|a|)_+.
\]
Combining this with account01/B13's slab inequality
\[
|a\det\Lambda|\le1536e^2\rho^{-4}
\]
gives
\[
\boxed{
|\det\Lambda|<3072e^2\rho^{-4}
\quad\text{or}\quad
\|A_{-k,k}\|_2\ge2^{-1/2}.
}
\]
Thus a near-null actual pivot is either a quantitatively near-rank-one latent packet or a fixed original-coordinate star.

If \(C\) contains the four largest diagonal coordinates, then on the star branch
\[
\|A_{C\setminus\{k\},k}\|_2\ge\frac12
\quad\text{or}\quad
\|A_{C^c,k}\|_2\ge\frac12,
\]
while the fifth-diagonal theorem retains
\[
\|D_{C^c}\|_{\rm op}\le2\sqrt{30\pi}\rho^{-1}.
\]

## Rough-law transfer

The cap-one-to-indicator purification is stated only in supremal form. Coordinatewise \(\varepsilon/n\)-near maximizers replace arbitrary factors by unit-measure indicators; no global bathtub optimizer or threshold attainment on the infinite line is assumed.

## Remaining debt

Build a product-preserving receiver for the literal four-coordinate core star or for the fixed-energy dense outside star with arbitrary same-bank self-couplings and the retained diagonal tail. Full QFORM and continuity remain open.
