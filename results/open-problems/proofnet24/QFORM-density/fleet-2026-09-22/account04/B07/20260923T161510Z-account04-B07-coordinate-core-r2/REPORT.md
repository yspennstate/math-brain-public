SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B07, 2026-09-23T16:15:10Z.

# account04/B07 — low-rank cancellation cannot erase \(r+3\) physical diagonal pivots

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Status: **PROVED SUPPORTING COORDINATE-CORE THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed**.

## 1. Scope and sources

The target remains: independent real \(X_i\) with densities at most one, arbitrary symmetric \(A\), and \(s_3(A)\ge1\).

Fresh control was read from \`yspennstate/math-research-brain\` main, observed immediately before publication at \`f89c6ddf42332d9cd8fc47501cb1061716ee9071a\`. The live correction inbox was retained. The newest Claude-source directory was checked through its later continuation commit \`7ffd1ed79398611eb06752f622be0ce33dcacb5a\`.

The completed account01/B07 theorem actually applied below is the rank-two-tube Plücker compiler at

\`yspennstate/math-open-problems@45934a636682207f422de4ab3f94c658030ba1ac\`

\`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T160359Z-r28/REPORT.md\`.

Its concrete inequality used here is: in its double-heavy near-rank-two branch,
\[
 \chi_*\le \rho_0:=\frac94-\sqrt5
 \quad\Longrightarrow\quad
 |\det K[R_*,C_*]|^2\ge\frac{\Omega}{8},
 \tag{1.1}
\]
and hence some physical edge in that actual \(2\times2\) cross minor obeys
\[
 |A_{ij}|\ge 2^{-5/4}\Omega^{1/4}.
 \tag{1.2}
\]

The physical-fiber theorem already established in account04/B07 is also used:
if an actual original-coordinate principal block \(A[I,I]\), \(|I|=m\), satisfies
\(s_3(A[I,I])\ge\gamma>0\), then
\[
 \|p_{X^TAX}\|_\infty
 \le \frac{2\sqrt{6\pi m}}{\gamma}.
 \tag{1.3}
\]
This conclusion retains arbitrary outside coordinates, couplings, spectra, and conditioning-generated affine terms.

No rotated independence, moment/support hypothesis, or small-random-quadratic-error argument is used.

## 2. Coordinate-core extraction through an arbitrary low-rank cancellation

### Theorem 2.1 — \`QFORM-DIAGONAL-RANK-TAIL-CORE-v1\`

Let \(I\) be a set of \(m=r+3\) original coordinates. Suppose the actual principal block has a deterministic decomposition
\[
 A[I,I]=D+R+E,
 \tag{2.1}
\]
where

* \(D=\operatorname{diag}(d_i:i\in I)\) and \(|d_i|\ge d>0\);
* \(\operatorname{rank}R\le r\), with no bound on \(\|R\|_{\rm op}\) and no sign restriction;
* \(E=E^T\) and \(\max_{i,j\in I}|E_{ij}|\le\varepsilon\).

Then
\[
 \boxed{\;
 s_3(A[I,I])\ge d-(r+3)\varepsilon.
 \;}
 \tag{2.2}
\]
Consequently, whenever \(d>(r+3)\varepsilon\),
\[
 \boxed{\;
 \|p_{X^TAX}\|_\infty
 \le
 \frac{2\sqrt{6\pi(r+3)}}
 {d-(r+3)\varepsilon}.
 \;}
 \tag{2.3}
\]

### Proof

Since \(\operatorname{rank}R\le r\),
\[
 \dim\ker R\ge m-r=3.
 \tag{2.4}
\]
For every \(x\in\ker R\),
\[
 (D+R)x=Dx,
 \qquad
 \|(D+R)x\|_2=\|Dx\|_2\ge d\|x\|_2.
 \tag{2.5}
\]
The max-min characterization of singular values therefore gives
\[
 s_3(D+R)
 =
 \max_{\dim V=3}\ \min_{\substack{x\in V\\\|x\|_2=1}}
 \|(D+R)x\|_2
 \ge d,
 \tag{2.6}
\]
by taking any three-dimensional subspace of \(\ker R\).

The entrywise tail is charged only on this actual \(m\)-coordinate block:
\[
 \|E\|_{\rm op}\le\|E\|_{\infty\to\infty}
 \le m\varepsilon=(r+3)\varepsilon.
 \tag{2.7}
\]
Singular-value perturbation yields (2.2). Equation (2.3) is the direct application of the physical-fiber theorem (1.3). QED.

The important point is that \(R\) may be arbitrarily large. It is defeated by nullity, not treated as a small perturbation. Likewise \(E\) is never declared a small random quadratic form; its operator norm is used only after localization to \(r+3\) physical coordinates.

## 3. High-slab-ratio consequence

Suppose a slab witness has ratio
\[
 \rho=\frac{\Pr\{X^TAX\in J\}}{|J|},
 \tag{3.1}
\]
and on some physical region the deterministic coefficient decomposition satisfies
\[
 A=D+R+E,\qquad \operatorname{rank}R\le r,
 \qquad |E|_{\max}\le\frac{c}{\rho}.
 \tag{3.2}
\]

If \(D\) has \(r+3\) physical diagonal entries of magnitude at least \(d\), choose those coordinates as \(I\). Equations (2.2)-(2.3) give
\[
 \rho
 \le
 \frac{2\sqrt{6\pi(r+3)}}
 {d-(r+3)c/\rho}.
 \tag{3.3}
\]
Multiplying by the positive denominator gives the explicit necessary inequality
\[
 \boxed{\;
 \rho\le
 \frac{(r+3)c+2\sqrt{6\pi(r+3)}}{d}.
 \;}
 \tag{3.4}
\]

Thus, above the right side of (3.4), a diagonal-plus-rank-\(r\) survivor can have at most \(r+2\) physical diagonal coefficients of size \(d\). This is a quantitative coordinate-core extraction, not a claim that one universally good \(3\times3\) minor exists.

For the current max-volume survivor parameters
\[
 r=28,\qquad c=32\sqrt{2e},\qquad m=31,
 \tag{3.5}
\]
the threshold is
\[
 \boxed{\;
 \rho\le
 \frac{992\sqrt{2e}+2\sqrt{186\pi}}{d}
 <\frac{2361.337}{d}
 \;}
 \tag{3.6}
\]
whenever there are \(31\) such physical diagonals. Hence any larger-ratio survivor has at most \(30\) large diagonal coordinates outside the pre-existing bounded exceptional set.

## 4. Actual use of account01/B07's new Plücker inequality

Apply account01/B07 r28 in its double-heavy near-rank-two branch. From (1.1)-(1.2), an actual physical edge satisfies
\[
 |b|:=|A_{ij}|\ge 2^{-5/4}\Omega^{1/4}.
 \tag{4.1}
\]
For its genuine symmetric principal pair
\[
 B=\begin{pmatrix}A_{ii}&b\\ b&A_{jj}\end{pmatrix},
 \tag{4.2}
\]
either the already-paid indefinite-pair branch occurs, or
\[
 \max\{|A_{ii}|,|A_{jj}|\}\ge |b|/2
 \ge 2^{-9/4}\Omega^{1/4}.
 \tag{4.3}
\]

Therefore repeated disjoint double-heavy tubes cannot indefinitely regenerate only unpaid large-diagonal exits. If they produce \(r+3\) distinct physical diagonal pivots at a common scale
\[
 d=2^{-9/4}\Omega_*^{1/4},
 \tag{4.4}
\]
then Theorem 2.1 gives the actual full-target inequality
\[
 \boxed{\;
 \|p_{X^TAX}\|_\infty
 \le
 \frac{2\sqrt{6\pi(r+3)}}
 {2^{-9/4}\Omega_*^{1/4}-(r+3)\varepsilon}
 \;}
 \tag{4.5}
\]
whenever the denominator is positive. This applies account01/B07's new macroscopic-minor output at a concrete density inequality and turns sufficiently many large-diagonal exits into a paid physical core.

## 5. Remaining obstruction

This does not prove the full conjecture. After the current structural decompositions, a high-ratio survivor is now forced into a sharper bounded-complexity shape:

* at most \(r+2\) large diagonal coordinates in the diagonal-plus-rank-\(r\) region;
* no paid actual \(s_3\)-principal core;
* no paid indefinite pair / pair-tail receiver;
* and, in the near-rank-two cross tubes, failure of the double-heavy Plücker face or insufficiently many distinct regenerated diagonal pivots.

For \(r=28\), the diagonal support outside the already exceptional coordinates is reduced to at most \(30\). The remaining difficulty is the dimension-growing entrywise-small dense tail together with the one-hub Plücker faces. An entrywise bound alone still does not control the global operator norm, so the tail cannot be deleted.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity remains separate.
