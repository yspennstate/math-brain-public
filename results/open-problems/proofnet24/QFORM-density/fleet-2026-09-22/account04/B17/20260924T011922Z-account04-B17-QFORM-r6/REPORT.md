# account04/B17 r6 — macroscopic fragmented strict-slack witness

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T011922Z-account04-B17-QFORM-r6\`  
Status: \`ESSENTIAL_STEP_APPLIED / NEW ANALYTIC WITNESS / FULL TARGET OPEN\`.

The unrestricted universal-density conjecture remains open. This report constructs a source-valid, entrywise-dense, strict-spectral-slack, disconnected-support family with a certified density lower bound above \(4\), while a nonvanishing fraction of the product mass lies outside the all-main cell. It is not a counterexample.

No histogram, moment assumption, bounded-support reduction, post-rotation independence, arbitrary-joint coarea estimate, or conditional-density supremum is used.

## 1. Pinned input

The completed partner theorem used is account01/B17's
\`QFORM-DIFFUSE-BANK-SPECTRAL-SLACK-COMPACTIFICATION-v1\`:

- scientific commit \`7d64d480f3b1b8f10f3ea1b169c1a6aeccbec5ea\`;
- completion commit \`d19c3dd3bc5e0e7a7f1c8eca725186ace671416f\`;
- path \`proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260924T003703Z-account01-B17-QFORM-auto11/REPORT.md\`.

For the dense three-bank matrices defined below and centered unit-interval inputs, it proves
\[
\|p_{Q_m^0}\|_\infty\longrightarrow 3\sqrt2. \tag{1.1}
\]
The proof uses the source-valid Fresnel--Brascamp--Lieb majorant from
\`e5f71d79eff325201dd0274053d20268ce65b837\`, so (1.1) is uniform-density convergence rather than an unsupported CLT assertion.

The earlier account04/B17 fragmented witness at commit
\`4e8d5ae06f2657e9e1ac8a89f7bc26c9ff95169e\`
used a fixed six-coordinate main cell and obtained \(p(0)>4.0468\). The present construction changes scale and mechanism: dimension tends to infinity, one eigenvalue is strictly beyond threshold, and the total probability of visiting satellite support does not vanish.

## 2. Exact matrix and spectrum

For \(m\ge2\), let
\[
n=\frac{(1,2,3)}{\sqrt{14}},\qquad
B_m=I-\left(2+\frac1m\right)nn^\top .
\]
Let \(R_m\) be the \(3m\times3\) synthesis matrix whose \(m\) rows in bank \(j\) equal \(e_j/\sqrt m\), and put
\[
A_m=R_mB_mR_m^\top .
\]
Since \(R_m^\top R_m=I_3\),
\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=
\left\{1,1,-\left(1+\frac1m\right)\right\}.} \tag{2.1}
\]
Thus every finite \(A_m\) is an exact target matrix with three eigenvalues of modulus at least one, and one magnitude is strictly larger than one.

All entries of \(B_m\), hence all entries of \(A_m\), are nonzero. Indeed the off-diagonal entries are nonzero and the diagonal entries are
\[
\frac{12-1/m}{14},\qquad
\frac{3-2/m}{7},\qquad
-\frac{4+9/m}{14}.
\]
This verifies the actual spectrum and rules out a hidden coordinate decomposition.

## 3. Cap-one fragmented laws with macroscopic satellite probability

Fix
\[
0<\theta<\frac13\log\!\left(\frac{3\sqrt2}{4}\right)
=0.0196305059427\ldots . \tag{3.1}
\]
For each \(m>\theta\), set
\[
\varepsilon_m=\frac{\theta}{m},\qquad
\ell_m=1-\frac{\theta}{m}.
\]
Choose any \(R_m^\star>1\), allowed to tend to infinity arbitrarily fast. Every physical coordinate has density
\[
f_m(x)=
\mathbf1_{[-\ell_m/2,\ell_m/2]}(x)
+\mathbf1_{[R_m^\star,R_m^\star+\varepsilon_m]}(x). \tag{3.2}
\]
The two supports are disjoint. Moreover
\[
0\le f_m\le1,\qquad
\int_{\mathbb R}f_m(x)\,dx=\ell_m+\varepsilon_m=1. \tag{3.3}
\]
Hence these are exactly normalized cap-one probability densities, with arbitrarily large support diameter. Use independent copies in all \(3m\) coordinates.

Let \(\mathcal M_m\) be the event that every coordinate lies in its main interval. Then
\[
\mathbb P(\mathcal M_m)=\ell_m^{3m}
\longrightarrow e^{-3\theta}, \tag{3.4}
\]
so
\[
\boxed{\mathbb P(\mathcal M_m^c)\longrightarrow1-e^{-3\theta}>0.} \tag{3.5}
\]
Thus fragmentation remains macroscopically visible at product level; it is not a vanishing-probability decoration.

## 4. Exact analytic lower-density certificate

Let \(U_i\) be independent \(\operatorname{Unif}[-1/2,1/2]\), and set
\[
Q_m^0=U^\top A_mU.
\]
Conditional on \(\mathcal M_m\), the physical vector has the exact law
\[
X=\ell_m U,
\]
and therefore
\[
X^\top A_mX=\ell_m^2Q_m^0. \tag{4.1}
\]
The unconditional law is a positive mixture over support-selection patterns. Its all-main component alone has weight \(\ell_m^{3m}\). Consequently, for the Radon--Nikodym densities,
\[
p_{X^\top A_mX}(t)
\ge
\ell_m^{3m-2}p_{Q_m^0}(t/\ell_m^2)
\quad\text{for a.e. }t, \tag{4.2}
\]
and hence
\[
\boxed{
\|p_{X^\top A_mX}\|_\infty
\ge \ell_m^{3m-2}\|p_{Q_m^0}\|_\infty.} \tag{4.3}
\]
This is an exact nonnegative-mixture inequality, not a Monte Carlo estimate.

Applying the completed account01/B17 limit (1.1),
\[
\ell_m^{3m-2}\to e^{-3\theta},
\]
so
\[
\boxed{
\liminf_{m\to\infty}\|p_{X^\top A_mX}\|_\infty
\ge3\sqrt2\,e^{-3\theta}.} \tag{4.4}
\]
By (3.1), the right side is strictly larger than \(4\).

For the concrete choice \(\theta=10^{-2}\),
\[
\boxed{
\liminf_{m\to\infty}\|p_{X^\top A_mX}\|_\infty
\ge3\sqrt2\,e^{-0.03}
=4.117251705266\ldots,} \tag{4.5}
\]
while
\[
\mathbb P(\mathcal M_m^c)\to1-e^{-0.03}
=0.029554466451\ldots . \tag{4.6}
\]

Each finite output has a continuous \(C_0\) density by the same completed diffuse-frame Fresnel theorem used by account01/B17; continuity is asserted only for this family.

## 5. Interpretation

This proves \`QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1\`:

> There are entrywise-dense exact-target matrices with spectrum
> \(\{1,1,-(1+1/m)\}\) and independent normalized cap-one two-component
> densities of arbitrarily large support diameter such that the probability
> of at least one satellite component converges to a positive constant and
> the output-density supremum has an analytic lower limit above \(4\).

The witness remains on the indefinite convex/two-sheet side. It shows that three tempting simplifications cannot support a universal proof:

1. strict inequality \(|\lambda|>1\) without a quantitative slack cannot improve the sharp obstruction;
2. disconnected or arbitrarily separated support is not automatically smoothing;
3. a fixed positive amount of global satellite mass does not force the density norm below \(4\).

The exact asymptotic lower value in (4.4) can be made arbitrarily close to \(3\sqrt2\) by taking \(\theta\downarrow0\), while retaining a positive (though correspondingly small) limiting satellite probability.

## 6. Remaining gap

This family is not a counterexample and does not resolve the unrestricted hybrid/convex-side class. It remains highly organized: three diffuse independent banks, uniform density on each support component, and no additional active spectrum. The full theorem must still handle arbitrary rough nonuniform cap-one laws, intermediate/localized leverage, shared-bank curvature, arbitrary additional spectrum, and the product-preserving moving-ridge/convex collar.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.
