# fleet02/B17 — vanishing-density high-ratio Boolean defects and an exponential-codimension safety theorem

**Run:** `20260922T061440Z-b17-primegate`  
**Common candidate:** `LIMIT-PRIME-GATE-LIFT-v1`  
**Classification:** `ESSENTIAL_STEP_APPLIED / STRONGER_DENSITY_SHORTCUT_REFUTED / REPLACEMENT_THEOREM_PROVED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact live target and three-report change

The later owner control keeps the FEI fleet on the all-gate formulation.  The current source-defined scalar lift used by the completed neighboring reports is

\[
 C^\dagger=6.521851214,\qquad
 \Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\]

and the missing implication is

\[
 D_{\Gamma^\dagger}(P;p)\ge 0
 \tag{0.1}
\]

for every finite composition-prime Boolean gate \(P\), every arity and every interior product-bias vector.  At the balanced uniform point, this is exactly

\[
 C^\dagger [I(P)-1]-H(P)\ge0.
 \tag{0.2}
\]

**FULL-PROBLEM CHANGE:** none.  Full FEI remains open.

**MECHANISM CHANGE:** yes.  The preceding B17 runs (i) sharpened the shared-graft lower obstruction by a thin one-coordinate spine, then (ii) closed the first changed-support neighborhoods of the 18-cell source, and (iii) proved slope \(4\) for one fixed two-point defect under dummy dilution.  The latest completed fleet03/B18 report generalized (iii) to *every fixed finite* balance-preserving defect pattern and explicitly left growing-support patterns open.  This run does not enumerate another support neighborhood.  It attacks the fixed-pattern hypothesis itself and then replaces the failed density shortcut by a geometry-free codimension theorem.

The named completed **other-account** results consumed and applied are:

1. fleet03/B18, `20260922T051809Z-finite-pattern-fourier-dust/REPORT.md`: every fixed finite balance-preserving point-defect pattern has incremental entropy/influence slope \(4\) under dummy dilution.  Its fixed-pattern hypothesis is the one challenged below.
2. fleet01/B18, `20260922T002302Z-gate-refutation-balanced-excess/REPORT.md`: for balanced Boolean functions the excess ratio \(H/(I-1)\) is exactly the FEI ratio after the standard fresh-character reduction, and balanced self-composition preserves that excess ratio while the ordinary \(H/I\) ratio tends to it.  Its certified 18-input seed has
   \[
   I_0=\frac{261}{128},\qquad
   6.776605309005978082519790221891882314787235038
   \le H_0\le
   6.776605309005978082519790221891882314787235039,
   \]
   hence
   \[
   \rho_0:=\frac{H_0}{I_0-1}
   =6.5218457109230465756581\ldots .
   \tag{0.3}
   \]

This report uses (2) to show that merely letting the physical defect density go to zero does **not** extend the fleet03/B18 slope-\(4\) theorem.

## 1. Exact rare-gating transform

Let \(f:\{0,1\}^d\to\{\pm1\}\) be balanced.  Add \(m\) fresh gating bits \(v\in\{0,1\}^m\), put \(\delta=2^{-m}\), and define

\[
 A=\{(x,v):f(x)=-1,\ v=0^m\},
 \qquad
 h(x,v)=1-2\,1_A(x,v).
 \tag{1.1}
\]

Finally add one fresh unbiased bit \(y\) and set

\[
 G(y,x,v)=(-1)^y h(x,v).
 \tag{1.2}
\]

Every \(G\) is an actual balanced Boolean function.

Write a Fourier frequency of \(h\) as \((R,V)\), with \(R\subseteq[d]\) and \(V\subseteq[m]\).  Since \(f\) is balanced,
\(1_{\{f=-1\}}=(1-f)/2\) has empty coefficient \(1/2\) and nonempty coefficients \(-\widehat f(R)/2\).  Therefore the normalized Walsh coefficients of \(h\) are exactly

\[
 \widehat h(\varnothing,\varnothing)=1-\delta,
 \tag{1.3}
\]
\[
 \widehat h(\varnothing,V)=-\delta\qquad(V\ne\varnothing),
 \tag{1.4}
\]
\[
 \widehat h(R,V)=\delta\,\widehat f(R)
 \qquad(R\ne\varnothing,\;V\subseteq[m]).
 \tag{1.5}
\]

Multiplication by the fresh character \((-1)^y\) only translates the Fourier support, so

\[
 H(G)=H(h),\qquad I(G)-1=I(h).
 \tag{1.6}
\]

### Theorem 1.1 — exact entropy and influence of a rare-gated core

Define

\[
 e_0(\delta)
 =(1-\delta)^2\log_2\frac1{(1-\delta)^2}.
\]

Then

\[
 \boxed{
 I(G)-1=\delta\,[I(f)+m]
 }
 \tag{1.7}
\]

and

\[
 \boxed{
 H(G)
 =\delta H(f)+4m\delta-2m\delta^2+e_0(\delta).
 }
 \tag{1.8}
\]

**Proof.**
For (1.7), the \(R\ne\varnothing\) atoms contribute
\[
 \delta I(f)+\frac m2\delta
\]
after summing all \(2^m\) gating frequencies, while the \(R=\varnothing,\ V\ne\varnothing\) atoms contribute another \(m\delta/2\).  For (1.8), the \(R\ne\varnothing\) atoms contribute
\[
 \delta H(f)+2m\delta,
\]
the \(2^m-1\) nonempty pure-gating atoms contribute
\[
 2m(\delta-\delta^2),
\]
and the empty atom contributes \(e_0(\delta)\).  Summing proves the identities.  \(\square\)

For a fixed \(f\), (1.7)--(1.8) recover the fixed-pattern slope \(4\).  But when the core itself grows, the first term in (1.8) can survive at leading order.

## 2. Actual Boolean obstruction to the “vanishing density implies slope 4” shortcut

Let \(B\) be the certified balanced 18-input seed from fleet01/B18, with \((I_0,H_0)\) above.  Let \(f_k=B^{\circ k}\) be its balanced disjoint self-composition.  The exact composition law from that report gives

\[
 I(f_k)=I_0^k,
 \qquad
 H(f_k)=H_0\frac{I_0^k-1}{I_0-1}.
 \tag{2.1}
\]

Apply Theorem 1.1 to \(f_k\) with \(m=k\), obtaining \(G_k\).  The physical defect set in (1.1) has density

\[
 \rho_k=2^{-k-1}\longrightarrow0.
 \tag{2.2}
\]

Yet

\[
 \frac{H(G_k)}{I(G_k)-1}
 =
 \frac{
 H(f_k)+4k-2k2^{-k}+e_0(2^{-k})/2^{-k}
 }{
 I(f_k)+k
 }.
 \tag{2.3}
\]

Since \(k/I_0^k\to0\) and \(e_0(2^{-k})/2^{-k}=O(1)\),

\[
 \boxed{
 \lim_{k\to\infty}
 \frac{H(G_k)}{I(G_k)-1}
 =
 \frac{H_0}{I_0-1}
 =\rho_0
 >6.5218457109230465756581.
 }
 \tag{2.4}
\]

Thus the stronger bridge

> every balanced character-defect family whose physical defect density tends to zero has asymptotic excess ratio at most \(4\)

is **false on genuine Boolean sources**.  The fixed-pattern hypothesis in fleet03/B18 is essential: here the number and intrinsic complexity of changed points grow with the core.

This is **not** a counterexample to FEI and not a counterexample to the current \(C^\dagger\) lift.  The source interval gives
\[
 \rho_0<C^\dagger,
\]
with gap about \(5.50\times10^{-6}\).  The construction is also decomposable, so it does not itself falsify the prime-gate implication (0.1).  Its role is adversarial: it rules out using physical density \(\rho\to0\) alone as a universal prime-gate safety surrogate.

## 3. Replacement mechanism: exponential-codimension safety

The obstruction above shows that “rare” must be quantified relative to ambient dimension, not only by \(\rho\to0\).

Let \(A\subseteq\{0,1\}^n\) have density \(\rho\in(0,1/2)\), define
\[
 h_A=1-2\,1_A,
\]
fix coordinate \(j\), and assume
\[
 g=\chi_j h_A
\tag{3.1}
\]
is balanced.  The balance condition is equivalent to the two \(j\)-sections of \(A\) having equal cardinality; each section therefore has density exactly \(\rho\) in \(Q_{n-1}\).

### Theorem 3.1 — geometry-free character-defect bound

For every such \(A,j,g\),

\[
 \boxed{
 I(g)-1\ge 2\rho\left(\log_2\frac1\rho-1\right).
 }
 \tag{3.2}
\]

Also, with \(V=4\rho(1-\rho)\),

\[
 \boxed{
 H(g)\le h_2(V)+V\log_2(2^n-1).
 }
 \tag{3.3}
\]

Consequently

\[
 \boxed{
 \frac{H(g)}{I(g)-1}
 \le
 \frac{
 h_2(4\rho(1-\rho))
 +4\rho(1-\rho)\log_2(2^n-1)
 }{
 2\rho(\log_2(1/\rho)-1)
 }.
 }
 \tag{3.4}
\]

**Proof of (3.2).**
Character multiplication shifts Fourier sets by \(j\), hence
\[
 I(g)-1
 =\sum_{i\ne j}\operatorname{Inf}_i(h_A)
   -\operatorname{Inf}_j(h_A).
 \tag{3.5}
\]
Each of the two \(j\)-sections has size \(\rho 2^{n-1}\).  Edge isoperimetry in \(Q_{n-1}\) gives internal boundary at least
\[
 \rho2^{n-1}\log_2(1/\rho)
\]
per section.  Since influence in the full cube is boundary divided by \(2^{n-1}\),
\[
 \sum_{i\ne j}\operatorname{Inf}_i(h_A)
 \ge2\rho\log_2(1/\rho).
 \tag{3.6}
\]
The \(j\)-boundary is the symmetric difference of the two sections, whose size is at most their total size \(\rho2^n\); therefore
\[
 \operatorname{Inf}_j(h_A)\le2\rho.
 \tag{3.7}
\]
Substitution in (3.5) proves (3.2).

**Proof of (3.3).**
Character multiplication preserves spectral masses.  The empty Fourier mass of \(h_A\) is \((1-2\rho)^2\), so the total nonempty mass is
\[
 V=1-(1-2\rho)^2=4\rho(1-\rho).
\]
Conditioning that mass on at most \(2^n-1\) nonempty Fourier frequencies gives entropy at most \(\log_2(2^n-1)\), hence (3.3).  \(\square\)

This theorem keeps the exact Boolean source and all coordinate prices.  There is no arbitrary probability-law or real-row relaxation.

## 4. A clean codimension threshold for the live center

For \(\rho\le1/4\), use
\[
 h_2(V)\le V\log_2(e/V),\qquad V\le4\rho,
\]
and \(\log_2(2^n-1)<n\).  Since \(x\mapsto x\log_2(e/x)\) is increasing on \(0<x\le1\),

\[
 H(g)
 \le
 4\rho\left[
 n+\log_2\frac1\rho-2+\log_2 e
 \right].
 \tag{4.1}
\]

Writing \(L=\log_2(1/\rho)>1\),

\[
 \boxed{
 \frac{H(g)}{I(g)-1}
 \le
 2\,\frac{n+L-2+\log_2 e}{L-1}.
 }
 \tag{4.2}
\]

If
\[
 \rho\le2^{-\alpha n},
\tag{4.3}
\]
then the right side is decreasing in \(L\), so asymptotically

\[
 \limsup_{n\to\infty}\frac{H(g)}{I(g)-1}
 \le 2+\frac2\alpha.
 \tag{4.4}
\]

For the live center \(C^\dagger=6.521851214\), every

\[
 \alpha>\alpha_*:=\frac2{C^\dagger-2}
 =0.4422967287839648\ldots
 \tag{4.5}
\]

is therefore eventually safe.

A concrete source-independent finite corollary is particularly simple:

### Corollary 4.1

If \(n\ge21\) and
\[
 \rho\le2^{-n/2},
\]
then
\[
 \boxed{
 H(g)<C^\dagger[I(g)-1].
 }
 \tag{4.6}
\]

Indeed \(\log_2 e<1.443\), so at \(n=21\) the upper bound (4.2) is below
\[
 6.514316<C^\dagger,
\]
and the bound decreases with \(n\).

Thus no balanced-uniform counterexample to the live candidate can lie in this entire exponentially thin character-defect regime.  The theorem applies to every support geometry and cardinality, including growing patterns.

## 5. What the two theorems say together

The fleet03/B18 fixed-pattern theorem and Theorems 1.1/3.1 separate two genuinely different notions of sparsity.

* **Fixed cardinality on a fixed scaffold:** exact incremental slope \(4\).
* **Density merely tending to zero:** insufficient.  The actual Boolean family \(G_k\) in (2.4) has density \(2^{-k-1}\to0\) while retaining excess ratio \(6.5218457\ldots\).
* **Exponential sparsity in ambient dimension:** geometry-free safety once the codimension exponent exceeds \(0.4422967\ldots\); in particular exponent \(1/2\) is safe from dimension \(21\) onward.

For the adversary (2.4), the ambient dimension is \(18^k+k+1\) while
\[
 \log_2(1/\rho_k)=k+1,
\]
so its codimension exponent tends to zero.  It sits exactly outside the replacement theorem rather than contradicting it.

This pinpoints the surviving balanced-uniform threat more sharply than “growing support”: a dangerous character-defect family must have defect codimension sublinear relative to its ambient dimension, or use a different overlap mechanism.  The separate universal all-bias prime-gate obligation (0.1) remains open.

## 6. Decisive checks and scope

`CHECKER.py` performs exact rational Walsh checks for the rare-gating formulas on tensor powers of three-bit majority for four small \((k,m)\) pairs, verifies
\[
 H(\mathrm{Maj}_3)=2,\qquad I(\mathrm{Maj}_3)=3/2,
\]
and checks the finite \(n=20\) versus \(n=21\) crossover of the coarse \(\rho\le2^{-n/2}\) certificate.  The captured output is `PASS`.

These finite tests are implementation sanity checks only.  Theorems 1.1 and 3.1 are analytic and all-dimensional.

A fresh literature check on 22 September 2026 found the September 18 plateaued-function theorem (sharp class constant \(4\)) and the May 29 stopping/restriction work, but no retrieved universal FEI resolution.  No novelty or publication-priority claim is made for the present internal lemmas; the edge-isoperimetric ingredient is standard.

## 7. Exact old/new missing implications

**Old immediate subproblem:** extend the fixed finite defect/dummy-dust safety mechanism to growing changed supports.

**Refuted stronger bridge:** “defect density \(\rho\to0\) alone forces asymptotic excess ratio at most \(4\).”  The actual Boolean \(G_k\) above converges instead to the certified \(6.521845710923\ldots\) balanced-excess ratio.

**New proved replacement:** exponential-codimension character defects obey (3.4), and every \(\rho\le2^{-n/2}\) source is live-center safe for \(n\ge21\).

**Remaining universal implication:** prove
\[
 D_{\Gamma^\dagger}(P;p)\ge0
\]
for every composition-prime Boolean gate and every interior bias, or find an actual prime gate/bias falsifier.  On the balanced uniform character-defect slice, any remaining threat must evade the exponential-codimension regime above.

**Implication to full FEI:** direct but partial.  One large growing-support regime is removed, and one tempting density-only shortcut is source-exactly refuted.  Full FEI remains **OPEN / NOT PROVED**.

Scoped privacy review: this report contains only FEI mathematics, logical account/slot labels, source-bound repository paths and nonsecret scientific hashes.  It contains no credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private data, email/Drive actions, paid/remote model calls, workflow dispatch or permission changes.
