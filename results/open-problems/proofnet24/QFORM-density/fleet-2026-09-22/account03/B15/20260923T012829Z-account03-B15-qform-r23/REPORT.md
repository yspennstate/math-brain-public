# QFORM countable Gaussian heat testing normal form

**Run:** `20260923T012829Z-account03-B15-qform-r23`  
**Account/slot:** account03/B15  
**Assignment:** absolute continuity and regularity  
**Outcome:** `ESSENTIAL_STEP_APPLIED / COUNTABLE_HEAT_CERTIFICATE`  
**Full universal QFORM bound:** OPEN / NOT PROVED  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and purpose

Let \(\mu\) be the law of
\[
Q=X^TAX,
\]
where the coordinates of \(X\) are independent with probability densities
\(0\le f_i\le1\), and where \(A=A^T\) has at least three eigenvalues of
absolute value at least one.

The central target is a universal bound on the output density height.  This
run does not prove that bound.  It proves an exact countable testing normal
form for it: no loss of constant and no prior absolute-continuity assumption.
The reduction is designed to remove the two continuous parameters (heat scale
and center) from the positive-heat formulation.

No Gaussian input assumption, moment assumption, log-concavity, compact
support, connected support, diagonal-basis independence, pointwise
van-der-Corput decay, fiber supremum, or reciprocal-minor estimate is used.

## 2. Completed partner result used

I use the completed account04/B15 theorem

- `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

For a Borel probability measure \(\mu\) on \(\mathbb R\), define
\[
\gamma_\varepsilon(u)
 =\frac{1}{\sqrt{2\pi}\,\varepsilon}
   e^{-u^2/(2\varepsilon^2)},
\qquad
H_\varepsilon(\mu;y)
 =\int \gamma_\varepsilon(x-y)\,d\mu(x),
\]
and
\[
M_\varepsilon(\mu)=\sup_y H_\varepsilon(\mu;y).
\]
The partner theorem proves that \(M_\varepsilon\) is nonincreasing as
\(\varepsilon\) increases and
\[
\boxed{
\sup_{\varepsilon>0}M_\varepsilon(\mu)
 =D(\mu),
}
\]
where \(D(\mu)=\|p_\mu\|_\infty\) if \(\mu=p_\mu\,dx\) has a bounded
density and \(D(\mu)=+\infty\) otherwise.

Thus for every sequence \(\varepsilon_k\downarrow0\),
\[
M_{\varepsilon_k}(\mu)\uparrow D(\mu)
\]
with the value \(+\infty\) allowed.

## 3. A quantitative center discretization lemma

### Lemma 3.1

For every probability measure \(\mu\) and every \(\varepsilon>0\), the
function \(y\mapsto H_\varepsilon(\mu;y)\) is in \(C_0(\mathbb R)\cap
C^1(\mathbb R)\), and
\[
\boxed{
\|\partial_y H_\varepsilon(\mu;\cdot)\|_\infty
\le \frac{1}{\sqrt{2\pi e}\,\varepsilon^2}.
}
\]

### Proof

Differentiate the Gaussian kernel.  Since
\[
\gamma_\varepsilon'(u)
 =-\frac{u}{\varepsilon^2}\gamma_\varepsilon(u),
\]
and the function \(r e^{-r^2/2}\) has maximum \(e^{-1/2}\) at \(r=1\),
\[
\|\gamma_\varepsilon'\|_\infty
 =\frac{1}{\sqrt{2\pi e}\,\varepsilon^2}.
\]
Differentiation under the finite measure is justified by the bounded
kernel derivative, hence
\[
|\partial_y H_\varepsilon(\mu;y)|
\le \int\|\gamma_\varepsilon'\|_\infty\,d\mu
=\frac{1}{\sqrt{2\pi e}\,\varepsilon^2}.
\]
Continuity follows similarly.  Vanishing at infinity follows by first
choosing a compact interval carrying all but \(\eta\) of \(\mu\), using the
Gaussian tail uniformly on that compact part, and bounding the remaining
mass by \(\eta\|\gamma_\varepsilon\|_\infty\).  Therefore the supremum
\(M_\varepsilon\) is attained.  \(\square\)

### Lemma 3.2 (grid error)

Fix a mesh \(h>0\), and define
\[
G_{\varepsilon,h}(\mu)
 :=\sup_{m\in\mathbb Z}
 H_\varepsilon(\mu;mh).
\]
Then
\[
\boxed{
0\le M_\varepsilon(\mu)-G_{\varepsilon,h}(\mu)
\le
\frac{h}{2\sqrt{2\pi e}\,\varepsilon^2}.
}
\]

### Proof

Let \(y_*\) be a maximizer of \(H_\varepsilon\), and choose
\(m\in\mathbb Z\) with \(|y_*-mh|\le h/2\).  Lemma 3.1 and the mean-value
estimate give
\[
M_\varepsilon
=H_\varepsilon(y_*)
\le H_\varepsilon(mh)
 +\frac{h}{2\sqrt{2\pi e}\,\varepsilon^2}
\le G_{\varepsilon,h}
 +\frac{h}{2\sqrt{2\pi e}\,\varepsilon^2}.
\]
The other inequality is immediate because the grid is a subset of all
centers. \(\square\)

## 4. Exact countable heat certificate

Set
\[
\varepsilon_k=2^{-k},\qquad h_k=\varepsilon_k^3=2^{-3k},
\qquad k=1,2,\ldots,
\]
and
\[
G_k(\mu)
:=\sup_{m\in\mathbb Z}
H_{2^{-k}}\!\left(\mu;m2^{-3k}\right).
\]
Lemma 3.2 gives the explicit inequality
\[
\boxed{
0\le M_{2^{-k}}(\mu)-G_k(\mu)
\le \frac{2^{-k}}{2\sqrt{2\pi e}}.
}
\tag{4.1}
\]
The right side tends to zero.

Combining (4.1) with the completed account04/B15 heat-height theorem gives
\[
G_k(\mu)\longrightarrow D(\mu)
\]
with the extended-real convention when \(D(\mu)=+\infty\).  Also
\(G_k(\mu)\le M_{2^{-k}}(\mu)\le D(\mu)\) for every \(k\).  Hence

### Theorem 4.1 (countable Gaussian certificate)

For every Borel probability measure \(\mu\) on \(\mathbb R\),
\[
\boxed{
D(\mu)
=\sup_{k\ge1}\sup_{m\in\mathbb Z}
\int
\gamma_{2^{-k}}\!\left(x-m2^{-3k}\right)
\,d\mu(x).
}
\tag{4.2}
\]
The equality is exact, with no multiplicative or additive loss in the final
height constant.  If \(\mu\) has no bounded density, both sides are
\(+\infty\).

More generally, the same proof works for any deterministic
\(\varepsilon_k\downarrow0\) and meshes \(h_k>0\) satisfying
\[
\frac{h_k}{\varepsilon_k^2}\longrightarrow0.
\]

## 5. Exact target-level equivalence

Apply Theorem 4.1 to \(\mu=\mathcal L(Q)\).  The full QFORM conjecture with
constant \(C\) is equivalent to the following purely countable family of
positive inequalities:

for every admissible \((n,A,f_1,\ldots,f_n)\), every integer \(k\ge1\), and
every \(m\in\mathbb Z\),
\[
\boxed{
\mathbb E\left[
\frac{1}{\sqrt{2\pi}\,2^{-k}}
\exp\!\left(
-\frac{(X^TAX-m2^{-3k})^2}{2\,2^{-2k}}
\right)
\right]
\le C.
}
\tag{5.1}
\]

Indeed, if the density bound \(\|p_Q\|_\infty\le C\) holds, every Gaussian
convolution is at most \(C\), so (5.1) follows.  Conversely, (5.1) bounds
all \(G_k\) by \(C\); Theorem 4.1 then gives \(D(\mu_Q)\le C\), which in
particular proves absolute continuity and the same density bound.

Thus the continuum of heat scales and centers in the positive-heat normal
form can be replaced, without changing the sharp universal constant, by the
single deterministic countable set
\[
\{(\varepsilon,y)=(2^{-k},m2^{-3k}):k\ge1,\ m\in\mathbb Z\}.
\]

This reduction is independent of the special structure of quadratic forms;
all QFORM structure is now concentrated in proving the expectations in
(5.1).

## 6. Actual partner inequality applied

Equation (4.1) is the quantitative bridge to the completed account04/B15
result.  Concretely, for every target law,
\[
M_{2^{-k}}(Q)
\le
\sup_{m\in\mathbb Z}
\mathbb E\gamma_{2^{-k}}(Q-m2^{-3k})
+\frac{2^{-k}}{2\sqrt{2\pi e}}.
\]
Letting \(k\to\infty\) and using the partner theorem yields
\[
\boxed{
\|p_Q\|_\infty
=\sup_{k,m}
\mathbb E\gamma_{2^{-k}}(Q-m2^{-3k}),
}
\]
again with value \(+\infty\) when no bounded density exists.

This is an actual inequality application of the assigned partner result, not
just a citation.

## 7. Separation from continuity

The countable certificate proves the central `L^infinity` statement if its
right side is uniformly bounded.  It does **not** by itself prove that the
resulting density has a continuous representative.  Continuity remains a
separate regularity assertion.

The current B15 source chain reports a separate fixed-matrix theorem giving a
bounded `C_0` density for every rank-at-least-three product target.  This run
does not need that theorem for (4.2) or (5.1), so the countable certificate
remains valid even if one wishes to review the continuity proof separately.

## 8. Why this is useful and what remains unpaid

The new normal form has three advantages for a full proof or a compactness
argument:

1. it removes the uncountable center parameter exactly;
2. it removes the uncountable heat-scale parameter exactly;
3. it keeps the functional positive and in original coordinates, so it does
   not invoke the refuted pointwise oscillatory-decay shortcut, arbitrary-joint
   coarea premise, worst-fiber cap, or single tiny-minor inversion.

The remaining mathematical implication is still substantial: prove a
universal bound for (5.1) uniformly over all admissible matrices and product
laws.  No such bound is proved here, so the full QFORM conjecture remains
OPEN.

A promising use is to attack one fixed lattice pair \((k,m)\) at a time with
product-preserving ridge/grouped-coordinate arguments and then keep the
constant uniform in \(k,m\).  The countable formulation also supports
source-valid diagonal/subsequence arguments without having to select an
uncountable family of centers and scales.

## 9. Corrections and scope

Fresh controls and the live correction inbox were re-read before
publication.  This proof does not use any of the currently refuted
intermediate mechanisms, including:

- law-uniform pointwise quadratic-phase decay;
- arbitrary-joint rank-three coarea bounds;
- conditional projection-density positive moments;
- fiberwise supremum integration;
- conditional cap preservation after sum/difference transformations;
- a uniformly good single physical minor or Schur pivot.

No Monte Carlo or numerical histogram is used.
