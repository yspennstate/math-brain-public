# Independent cross-paper audit of the grouped Fourier branch

Run: 20260924T181215Z-fleet04-B20-nine-crosspaper-r1

Verdict: **PASS for the scoped analytic/no-pivot branch.** This is not an end-to-end certification of the full nine-eigenvalue paper, and it does not prove the unrestricted three-eigenvalue conjecture.

## Sources pinned

1. Candidate A:
   - path: proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex
   - commit: eeb752c8943536541b34b42b8bf48e924f4d3d2f
   - blob: 19fb119877426b640b2c0dae19ec2f78a399fe11
   - SHA-256: bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3
   - checked lines: 400--526, especially Lemma 4.7 and Theorem 4.9.

2. Independent reconstruction B:
   - path: proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex
   - commit: d3b12e27
   - blob: 823201f05363fcc60c38cce0feb5abb636f081d7
   - checked lines: 276--417, especially Theorem 4.1, Lemma 4.3, and Corollary 4.4.
   - audit blob: af65f076e2c6c63a493c4f87f1d070b5f974a98a.

The second reconstruction is separately written. I compared the proofs rather than treating its audit file as evidence.

## Exact dictionary between the two arguments

Let \(h\) be the number of promoted physical hub rows, let \(m\) be the residual diffuse order, and put \(q=h+m\). In Candidate A the grouped estimate has

\[
 |\phi_Q(t)|\le
 B_{h,m}|t|^{-q/2},
\]

where

\[
 B_{h,m}
 =
 \pi^{q/2}2^{m/4}e^{(h+2m)/4}
 \omega(m)^{1/4}
 S^{-1/2}Z^{-1/4},
 \qquad
 \omega(m)=\frac{m^m}{m!}.
\]

Here \(S^2=\Theta(H)\), while the residual Gram volume is

\[
 Z=\frac{\Theta_q(H)}{\Theta(H)}.
\]

Therefore

\[
\begin{aligned}
 B_{h,m}^2
 &=
 \pi^q2^{m/2}e^{(h+2m)/2}
 \omega(m)^{1/2}
 S^{-1}Z^{-1/2}\\
 &=
 \pi^q e^{q/2}(2e)^{m/2}
 \omega(m)^{1/2}
 \Theta_q(H)^{-1/2}.
\end{aligned}
\]

This is exactly the constant in Reconstruction B's Lemma 4.3:

\[
 |\phi_Q(t)|^2
 \le
 \pi^q e^{q/2}(2e)^{m/2}
 \omega(m)^{1/2}
 \Theta_q(H)^{-1/2}|t|^{-q}.
\]

Thus the two derivations agree term by term, including every factor of \(2\), \(\pi\), \(e\), the entropy factor, the hub determinant, the residual volume, and the Fourier exponent.

## Heavy-row promotion

Both proofs use the same physical-coordinate recursion. If a residual row carries more than half of the remaining \(q\)-volume, retain that literal original coordinate as a hub. After \(h\) promotions,

\[
 \Theta_q(H)>2^{-h}E_q(M).
\]

No rotation of the input vector occurs. The only projected-density input is applied to a deterministic linear image of a product law, and neither paper asserts independence of the projected coordinates.

The mollified \(L^2\) step also matches. Candidate A uses the image measure and a mollifier before passing to the \(L^2\) limit; Reconstruction B uses the corresponding kernel
\(\kappa_\varepsilon(M_HD)\). In both proofs the bound is uniform in the mollifier scale before the limit is taken. This avoids an unsupported pointwise conditional-density bound.

## Order-three constants

For \(q=3\), the density coefficients after \(h=0,1,2\) promotions are

\[
 c_h
 =
 3\sqrt2\,e^{1-h/6}
 \left(\frac{(3-h)^{3-h}}{(3-h)!}\right)^{1/6},
\]

and the terminal three-hub coefficient is \(3\sqrt{2e}\). Numerically,

\[
 c_0=14.818337662843,\quad
 c_1=10.957714649270,\quad
 c_2=8.263535690266,\quad
 c_3=6.994931944791.
\]

Hence the diffuse case is the worst one and

\[
 C_3=3\sqrt2\,e\,(9/2)^{1/6}
 =14.818337662843<15.
\]

In the no-pivot branch,

\[
 V_3(A)\ge\kappa^3,\qquad
 \kappa=\frac4{625},
\]

and the random cut supplies

\[
 E_3(M)\ge4^{-3}V_3(A)
 \ge \frac1{625^3}.
\]

Therefore

\[
 E_3(M)^{-1/6}\le25
\]

and both papers obtain exactly

\[
 \|p_Q\|_\infty
 \le25C_3
 =370.458441571075\ldots<375.
\]

The order-two formula also agrees:

\[
 C_2=8\sqrt e\,2^{-1/8}
 =12.095072570796\ldots.
\]

Candidate A records the looser \(C_2<14\); Reconstruction B records \(C_2<12.2\). This is not a mathematical disagreement.

## What the Lean package does not certify

Reconstruction B's AUDIT.md explicitly says that Fourier inversion, geometric Brascamp--Lieb, the product-projection consequence, and Theorem 4.1 are not formalized in Lean. The finite entropy and constant sublemmas are formalized, but the present PASS is an independent mathematical reconstruction, not a Lean-generated certificate.

## Release-gate consequence

This comparison supplies a second independent reconstruction of the grouped Fourier/heavy-row/no-pivot chain. It finds no disagreement between the two papers in that chain.

It does **not** supply a second end-to-end review of the diagonal-pivot and two-coordinate pivot branches. Accordingly:

- the scoped no-pivot branch is independently corroborated;
- the complete \(s_9\), constant-\(400\) theorem remains a candidate pending full independent reconstruction of the pivot branches;
- no claim is made for \(s_8\) or for the unrestricted three-eigenvalue conjecture.
