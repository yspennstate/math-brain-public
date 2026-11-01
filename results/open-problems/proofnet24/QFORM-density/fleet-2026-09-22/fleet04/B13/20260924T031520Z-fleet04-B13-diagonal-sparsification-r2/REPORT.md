SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B13, 2026-09-24T03:15:20Z.
attacking: the exact/two-strip rank-two endpoint — repair the optimizer-free product reduction and use an actual physical five-coordinate gate to compress distributed diagonal curvature to four centers plus an O(rho^{-1}) diagonal tail, without deleting that tail.

# fleet04/B13 r2 — diagonal fifth-order sparsification in the rank-two endpoint

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T031520Z-fleet04-B13-diagonal-sparsification-r2\`  
Status: **NEW SLAB-SCALE DIAGONAL SPARSIFICATION + GROUPED-CORE GATE / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

All coordinates are original physical coordinates. There is no post-rotation independence, moment/support regularity, attained slab optimizer, common support diameter, fixed fragment count, or deletion of a coefficient-small quadratic term.

## 1. Sources and live scope

\`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`,
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.
No valid counterexample is known there, and the full theorem is not claimed.

Fresh compatible inputs:

- fleet01/B13, \`math-open-problems@ac747ce0b42789059a2b1dee4261dc18f6a634a2\`, especially the optimizer-free scope correction and \`QFORM-LOWSCORE-TO-HUBSTRIP-18-v1\`;
- fleet02/B13, \`math-open-problems@2af615c6d649e207191127733fc6dd180db14944\`, especially \`QFORM-FINITE-DIRECTION-FINITE-DIAGONAL-GROUPING-v1\`;
- fleet03/B13, \`math-open-problems@37177f7694c9aab73604b36c452e2a92c612aad4\`, the two-line normal form;
- fleet04/B07, \`math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa\`, the physical coordinate-core theorem.

## 2. Optimizer-free product reduction, with no threshold attainment

Let \(h\ge0\) be bounded measurable and let \(0\le f\le1\), \(\int f=1\). Put
\[
M(h)=\sup_{|E|=1}\int_E h.
\]
Then
\[
\boxed{\int f h\le M(h).} \tag{2.1}
\]

Indeed, by the layer-cake formula,
\[
\int f h=\int_0^\infty\int_{\{h>s\}}f(x)\,dx\,ds
\le\int_0^\infty\min\{1,|\{h>s\}|\}\,ds.
\]
The last quantity is \(\int_0^1h^*(u)\,du=M(h)\), where the equality is as a supremum; no maximizing threshold set is required.

Apply (2.1) successively to each coordinate fiber of any bounded nonnegative kernel \(K\). For every product density \(0\le f_i\le1\), \(\int f_i=1\), and every \(\varepsilon>0\), there are measurable unit sets \(E_i\) such that
\[
\boxed{
\int K\prod_i1_{E_i}
\ge \int K\prod_i f_i-\varepsilon.
} \tag{2.2}
\]
Lebesgue regularity then replaces each \(E_i\) by a bounded finite union of intervals with another arbitrarily small loss. This proves the safe optimizer-free reduction directly, including on the noncompact line.

For \(K=1_{\{x^TAx\in J\}}\), a witness of slab ratio \(\rho\) therefore yields, for every \(\eta>0\), a bounded-finite-union unit-product witness of ratio at least \(\rho-\eta\). This is the form used below.

## 3. New diagonal fifth-order sparsification theorem

Consider the exact diffuse rank-two chamber
\[
A=D+U\Lambda U^T,\qquad D=\operatorname{diag}(d_1,\dots,d_n),\qquad \operatorname{rank}(U\Lambda U^T)\le2,
\]
with \(s_3(A)\ge1\). Let \(d_{(1)}\ge d_{(2)}\ge\cdots\) be the decreasing rearrangement of \((|d_i|)\). Define
\[
C_5:=2\sqrt{30\pi}=19.41625912555699\ldots .
\]

### Theorem 3.1 — \`QFORM-R2-DIAGONAL-FIFTH-SPARSIFICATION-v1\`

For every interval \(J\) of positive length and every cap-one product input,
\[
\rho:=\frac{\Pr\{X^TAX\in J\}}{|J|}
\quad\Longrightarrow\quad
\boxed{d_{(5)}\le \frac{C_5}{\rho}.} \tag{3.1}
\]

Equivalently, for every \(t>C_5/\rho\), at most four physical diagonal coefficients satisfy \(|d_i|\ge t\).

### Proof

Suppose five physical coordinates \(I\) satisfy \(|d_i|\ge t\). On that literal five-coordinate block,
\[
A[I,I]=D_I+R_I,\qquad \operatorname{rank}R_I\le2.
\]
The subspace \(\ker R_I\) has dimension at least three, and for every \(x\in\ker R_I\),
\[
\|A[I,I]x\|=\|D_Ix\|\ge t\|x\|.
\]
By the min-max characterization of singular values,
\[
s_3(A[I,I])\ge t. \tag{3.2}
\]
Apply the completed fleet04/B07 physical-core theorem with \(r=2\), \(\varepsilon=0\), and \(d=t\). It gives the full ambient quadratic form
\[
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le \frac{2\sqrt{6\pi(2+3)}}{t}
=\frac{C_5}{t}. \tag{3.3}
\]
Every interval ratio is therefore at most \(C_5/t\). Taking \(t=d_{(5)}\) proves (3.1), with the usual limiting interpretation if ties occur. QED.

This is an actual principal-block spectral gate. It does not say that the remaining diagonal quadratic form is probabilistically small.

## 4. Rank-six core plus retained slab-scale diagonal tail

Let \(S\) be the four coordinates of largest \(|d_i|\), put
\[
D_S=\operatorname{diag}(d_i1_{i\in S}),\qquad
A_{\rm core}=D_S+U\Lambda U^T,\qquad
E=D-D_S.
\]
Then
\[
\boxed{\operatorname{rank}A_{\rm core}\le6,\qquad
\|E\|_{\rm op}\le C_5/\rho.} \tag{4.1}
\]
Weyl's inequality gives the deterministic final-matrix gate
\[
\boxed{s_3(A_{\rm core})\ge1-C_5/\rho.} \tag{4.2}
\]
In particular, if \(\rho\ge2C_5=38.8325182511\ldots\), then \(s_3(A_{\rm core})\ge1/2\).

In the exact two-projective-line endpoint of fleet03/B13, all rows of \(U\) outside \(S\) lie in at most two latent directions. The fleet02/B13 finite-direction grouping theorem therefore applies to \(A_{\rm core}\) with
\[
N\le |S|+2\le6.
\]
After rescaling the spectral threshold \(1/2\) to one, it gives the concrete stand-alone core estimate
\[
\boxed{
\|p_{X^TA_{\rm core}X}\|_{\infty,\mathrm{ess}}
\le2\cdot250e\cdot6(8+\log6)
<39850.286.
} \tag{4.3}
\]
Equation (4.3) is not transferred to \(A=A_{\rm core}+E\) by perturbation: \(X^TEX\) is entangled with the grouped variables and can be large on unbounded or remotely fragmented supports. The exact remaining obstruction is now a paid six-dimensional grouped core coupled to a diagonal tail satisfying the deterministic operator gate in (4.1).

## 5. Equation-level application of fleet01/B13

Use the optimizer-free transfer (2.2) with loss \(\eta>0\), and put \(\widetilde\rho=\rho-\eta\). In the fleet01/B13 low-score hard branch, its theorem yields a physical near-pivot strip \(H\) satisfying
\[
\sum_{i\in H}\|u_i\|^2>\frac5{6144},\qquad
\operatorname{dist}(u_i,\operatorname{span}u_k)
<6.064\,\widetilde\rho^{-1/8},
\]
and actual cross-two-volume
\[
Z_{\rm strip}>\frac54e^2\widetilde\rho^{-4}. \tag{5.1}
\]
Applying Theorem 3.1 to the same witness gives simultaneously
\[
\boxed{
d_{(5)}\le C_5\widetilde\rho^{-1}.
} \tag{5.2}
\]
Letting \(\eta\downarrow0\), a hypothetical unbounded-ratio sequence in that low-score branch must therefore have, at the same time,

1. fixed coefficient-frame mass and slab-scale two-volume in an \(O(\rho^{-1/8})\) near-hub strip; and
2. all but four diagonal coefficients in an \(O(\rho^{-1})\) operator-norm tail.

This is a sharper coupled normal form than either input alone. It avoids selecting or inverting an individual tiny Pluecker minor.

## 6. Exact remaining implication

Full QFORM remains open and no counterexample is produced. Continuity remains separate.

The first unpaid implication is now
\`QFORM-HUBSTRIP-PLUS-R2-DIAGONAL-TAIL-RECEIVER-v1\`:

> Prove an affine-uniform interval bound for the rank-at-most-six grouped core coupled to the retained diagonal tail \(\|E\|_{\rm op}=O(\rho^{-1})\), using the simultaneous near-hub strip currency (5.1), or construct a valid bounded-finite-union product-indicator counterexample in this exact normal form.

Small operator norm alone is not enough under unbounded inputs; the next mechanism must keep \(X^TEX\) inside the phase or condition/group it product-preservingly.
