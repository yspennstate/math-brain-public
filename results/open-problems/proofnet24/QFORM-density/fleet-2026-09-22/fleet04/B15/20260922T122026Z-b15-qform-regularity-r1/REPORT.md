# fleet04/B15 — absolute continuity, interval domination, and a continuity criterion

**Run:** 20260922T122026Z-b15-qform-regularity-r1  
**Programme:** QFORM-DENSITY-3EIG-20260922, control revision 2026-09-22.5  
**Assignment:** Absolute continuity and regularity  
**Classification:** TARGET-SUPPORTING-THEOREMS / ESSENTIAL-STEP-APPLIED / FULL-TARGET-OPEN  
**Execution context:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and current status

The owner target asks for one universal finite \(C\) such that, for every \(n\), every independent real \(X_i\) with probability densities \(0\le f_i\le1\), and every real symmetric \(A\) having at least three eigenvalues of absolute value at least \(1\), the law of
\[
Q=X^TAX
\]
has a density \(p_Q\) with \(\|p_Q\|_\infty\le C\). A continuous representative is requested separately.

The full universal-constant conjecture remains open. The current correction inbox was reread before publication. In particular, this report uses neither uniform pointwise oscillatory decay, nor diagonalized independence, nor a cross-minor-only implication, nor the now-refuted claim that the universal sharp constant is \(\pi\).

The completed assigned-partner result actually used is:

yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553

proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md

That report proves an instancewise \(L^\infty\) bound for every rank-at-least-three matrix via invertible principal blocks of order three or four. I apply it below to an actual interval inequality and to a new continuity theorem on an original-coordinate block-splitting branch.

## 2. Absolute continuity is automatic for every nonzero quadratic form

### Theorem 2.1 — QFORM-NONZERO-COORDINATE-AC-v1

Let \(X\) be an \(\mathbb R^n\)-valued random vector with a Lebesgue density. If \(A\) is a nonzero real symmetric matrix, then \(X^TAX\) has an absolutely continuous law.

This needs neither independence, nor density bound \(1\), nor rank three.

### Proof

Choose a coordinate \(i\) whose row in \(A\) is nonzero. Conditional on \(X_{\widehat i}=z\), the quadratic is
\[
q_z(t)=a t^2+2b(z)t+c(z),
\qquad
a=A_{ii},\quad
b(z)=\sum_{j\ne i}A_{ij}z_j.
\]

If \(a\ne0\), then \(q_z\) is a nonconstant quadratic for every \(z\). The inverse image under a nonconstant one-variable quadratic of a Lebesgue-null set is null: remove the one critical point and split the line into countably many compact intervals on which the map is a \(C^1\) diffeomorphism with locally Lipschitz inverse. The critical singleton is null.

If \(a=0\), then some \(A_{ij}\ne0\). The scalar linear functional \(b(X_{\widehat i})\) has an absolutely continuous law: rotate only for this measure-theoretic statement, or apply Fubini after using \(x_j\) as the integrating coordinate. Hence \(b(X_{\widehat i})\ne0\) almost surely. For such a conditioning value, \(q_z(t)=2b(z)t+c(z)\) is a nonconstant affine map, so it also pulls null sets back to null sets.

Thus for every one-dimensional null set \(N\),
\[
\Pr(q_{X_{\widehat i}}(X_i)\in N\mid X_{\widehat i})=0
\]
for almost every conditioning value. Integrating proves
\[
\Pr(X^TAX\in N)=0.
\]
Therefore the pushforward law is absolutely continuous. \(\square\)

Under the owner hypothesis \(A\) is certainly nonzero, so absolute continuity itself is fully settled. The hard issue is the universal \(L^\infty\) constant.

## 3. Exact equivalence between small-ball bounds and bounded density

### Theorem 3.1 — QFORM-INTERVAL-DOMINATION-EQUIVALENCE-v1

Let \(\mu\) be a finite Borel measure on \(\mathbb R\) and \(C<\infty\). The following are equivalent.

1. For every bounded interval \(I\),
   \[
   \mu(I)\le C|I|.
   \]
2. \(\mu\ll dx\) and its Radon–Nikodym density \(p\) satisfies
   \[
   \|p\|_\infty\le C.
   \]

### Proof

The second statement immediately implies the first. Conversely, every open subset of \(\mathbb R\) is a countable disjoint union of intervals, so the interval estimate gives \(\mu(O)\le C|O|\) for every open \(O\). Outer regularity then gives \(\mu(E)\le C|E|\) for every Borel \(E\). Hence \(\mu\ll dx\), and the Radon–Nikodym derivative is at most \(C\) almost everywhere. \(\square\)

Thus a universal estimate
\[
\sup_{t\in\mathbb R}\Pr(Q\in[t,t+h])\le Ch
\quad(h>0)
\]
already contains both absolute continuity and the desired \(L^\infty\) conclusion. No separate Fourier inversion theorem is needed.

## 4. Applying the completed fleet01/B15 theorem

For a real symmetric \(A\) of rank at least three, define
\[
\kappa_{3,4}(A)
=
\max\left\{
\sigma_{\min}(A_{I,I}):
|I|\in\{3,4\},\ \det A_{I,I}\ne0
\right\}.
\]
The fleet01/B15 principal-block theorem proves \(\kappa_{3,4}(A)>0\) and, uniformly over all allowed product input laws,
\[
\Pr(X^TAX\in I)
\le
\frac{4\pi+8}{\kappa_{3,4}(A)}\,|I|
\tag{4.1}
\]
for every interval \(I\).

Applying Theorem 3.1 to (4.1) gives the actual density inequality
\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
\frac{4\pi+8}{\kappa_{3,4}(A)}.
}
\tag{4.2}
\]

Therefore every individual matrix in the owner class already has a bounded density, uniformly over its admissible input laws. The remaining conjectural step is exactly to remove the matrix-dependent factor \(1/\kappa_{3,4}(A)\). Flat rank-three frames show that single-block selection cannot do this dimension-freely.

## 5. A target-level criterion for a continuous representative

Bounded density and continuous density are distinct conclusions. The exact missing regularity can be expressed using only small-ball probabilities.

For \(r>0\), define the centered interval average
\[
S_r\mu(t)
=
\frac{\mu((t-r,t+r))}{2r}.
\]

### Theorem 5.1 — QFORM-STEKLOV-CONTINUITY-CRITERION-v1

Assume \(\mu(I)\le C|I|\) for all intervals. Then:

1. \(0\le S_r\mu(t)\le C\) for all \(r,t\).
2. Each \(S_r\mu\) is continuous; in fact
   \[
   |S_r\mu(t+h)-S_r\mu(t)|
   \le \frac{C}{r}|h|.
   \tag{5.1}
   \]
3. The measure \(\mu\) has a continuous density representative \(p\) if and only if
   \[
   S_r\mu\longrightarrow p
   \quad\text{locally uniformly as }r\downarrow0.
   \tag{5.2}
   \]
4. A useful sufficient condition is: for every \(R<\infty\),
   \[
   \sum_{k=0}^\infty
   \sup_{|t|\le R}
   \left|
   S_{2^{-k-1}}\mu(t)-S_{2^{-k}}\mu(t)
   \right|
   <\infty.
   \tag{5.3}
   \]
   Under (5.3), the dyadic averages converge locally uniformly to a continuous density \(p\) with \(0\le p\le C\).

### Proof

The first statement is interval domination. For (5.1), the symmetric difference of \((t-r,t+r)\) and \((t+h-r,t+h+r)\) has length at most \(2|h|\); domination by \(Cdx\) yields (5.1).

If \(p\) is continuous, then on each compact interval it is uniformly continuous, and
\[
S_r\mu(t)=\frac1{2r}\int_{t-r}^{t+r}p(s)\,ds
\]
converges to \(p(t)\) uniformly on that compact. Conversely, if the averages converge locally uniformly to a continuous \(q\), the Lebesgue differentiation theorem says the same averages converge to the Radon–Nikodym density \(p\) almost everywhere. Hence \(q=p\) almost everywhere, so \(q\) is a continuous representative.

Finally, (5.3) makes the dyadic averages locally uniformly Cauchy. Their locally uniform limit is continuous, bounded by \(C\), and equals the Radon–Nikodym density almost everywhere by differentiation. \(\square\)

This theorem cleanly separates the two owner requests:

- the central conjecture asks only for the uniform height bound \(S_r\mu\le C\);
- continuity requires additional scale coherence such as (5.3).

The distinction is genuine. The uniform law on \([0,1]\) satisfies \(\mu(I)\le|I|\), but its density \(1_{[0,1]}\) has no continuous representative. If a continuous representative existed, continuity and almost-everywhere equality would force it to equal both \(1\) and \(0\) at an endpoint.

## 6. New continuity theorem from the partner bound plus independent smoothing

### Lemma 6.1 — bounded density plus independent AC noise

If \(R\) has a density \(p_R\) with \(\|p_R\|_\infty\le C\), and \(S\) is independent of \(R\) with an \(L^1\) density \(g\), then \(R+S\) has the uniformly continuous density
\[
p_{R+S}=p_R*g,
\qquad
\|p_{R+S}\|_\infty\le C.
\]
Indeed,
\[
\|\tau_h(p_R*g)-p_R*g\|_\infty
\le
\|p_R\|_\infty\|\tau_hg-g\|_1
\longrightarrow0.
\tag{6.1}
\]

### Theorem 6.2 — QFORM-BLOCK-SPLIT-CONTINUOUS-v1

Suppose, after permuting the original independent coordinates,
\[
A=B\oplus D,
\]
where \(\operatorname{rank}(B)\ge3\) and \(D\ne0\). Then \(Q=X^TAX\) has a bounded uniformly continuous density, and
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{4\pi+8}{\kappa_{3,4}(B)}.
}
\tag{6.2}
\]

### Proof

Write
\[
R=X_I^TBX_I,\qquad S=X_J^TDX_J.
\]
The two variables are independent because the blocks use disjoint original coordinates. The fleet01/B15 theorem and Theorem 3.1 give a density \(p_R\) satisfying the displayed bound. Since \(D\ne0\), Theorem 2.1 gives an \(L^1\) density \(g\) for \(S\). Lemma 6.1 now proves uniform continuity and (6.2). \(\square\)

This extends the known diagonal smoothing mechanism to an arbitrary rotated quadratic inside the first original-coordinate block. It does not handle a general dense \(A\), because cross-block terms destroy the independent additive decomposition.

## 7. Exact remaining implications

The substantive ledger is now:

- **Absolute continuity:** proved for every nonzero quadratic form under an absolutely continuous joint input law.
- **Bounded density for every fixed target matrix:** supplied by fleet01/B15 and converted explicitly by (4.1)–(4.2).
- **Universal constant independent of \(A,n\):** open. The missing step is delocalized aggregation that removes \(1/\kappa_{3,4}(A)\).
- **Uniformly continuous density:** proved on the original-coordinate block-split branch of Theorem 6.2, including arbitrary signs and arbitrary internal rotations in \(B,D\).
- **Continuous representative for a fully dense rotated form:** open even after a universal interval bound. The Steklov criterion (5.3) is an exact sufficient target: establish summable scale increments of normalized interval probabilities without assuming forbidden pointwise Fourier decay.

No Gaussianity, log-concavity, moment, compact-support, connected-support, or eigenbasis-independence assumption is used. No novelty or publication-priority claim is made.
