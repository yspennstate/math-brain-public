# B12 — quantitative Boolean endpoint for the Gibbs/Bellman FEI residual

**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_BOOLEAN_ENDPOINT / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact candidate, peer version, and before/after

This run binds to the current all-gate candidate

`LIMIT-PRIME-GATE-LIFT-v1`,

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p).
\]

The universal unpaid implication remains

\[
D_{\Gamma^\dagger}(P;p)\ge 0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every }p\in(0,1)^k.
\tag{0.1}
\]

The exact named other-account result consumed and applied is fleet03/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`.

That report fixes the common Shannon residual `B-GIBBS-KL-v1`.  For the actual biased spectral law \(w\), after conditioning on nonempty spectrum, it writes

\[
R_B(G;p)
=D_{\rm KL,2}(w^+\|\nu_x^+)-\log_2{A_0\over x_q},
\qquad
D_{\Gamma^\dagger}(G;p)=V_q R_B(G;p),
\tag{0.2}
\]

and proves the exact Bellman decomposition

\[
R_B(G;p)
=D_{\rm KL,2}(w^+\|\rho_\lambda)
+\lambda m-\log_2{A_\lambda\over x_q}
\tag{0.3}
\]

for every real \(\lambda\).  The peer also proves that the scalar-price part is optimal among arbitrary laws with the same mean price.  Its first essential Boolean gap is therefore explicit: in the low-Bellman-price region one must force residual shape information from signed Boolean realizability.  At the balanced uniform endpoint, the relaxed optimizer spreads mass among several singleton frequencies, while a Boolean equality case is a single character.  The peer leaves a quantitative stabilization of that fact as the next Boolean inference.

This report proves such a stabilization in every dimension, then plugs it back into (0.3).  It does **not** complete the remaining shape-KL payment, so (0.1) and full FEI remain open.

## 1. Compact conditional chain to full FEI

1. **Proved elsewhere and consumed:** the all-gate inequality for one finite symmetric nonnegative \(\Gamma\) is equivalent to FEI.
2. **Proved elsewhere and retained:** the live candidate reduces by the nonnegative composition cocycle to composition-prime gates.
3. **Proved by fleet02/B15 and fleet03/B18:** the exact gate defect is the Gibbs conditional-KL residual (0.2), and its scalar-price part has the exact Bellman/I-projection solution (0.3).
4. **First missing Boolean inference before this run:** quantify the statement that a balanced Boolean source whose spectral mean level is close to the Poincare endpoint \(1\) must put almost all spectral mass on one *actual character*, rather than on the non-Boolean multi-singleton Bellman optimizer.
5. **Proved below:** if \(I(f)=1+\delta\), one singleton coefficient has squared mass at least \(1-(3+\sqrt3)\delta\).  This is dimension-free and uses the signed Boolean identity, not merely a probability-law relaxation.
6. **Still open:** convert this one-character concentration plus the actual higher-level cost into enough residual shape KL throughout the whole low-price region, at arbitrary bias and then every arity.  Only after that universal step does the live candidate prove full FEI.

## 2. Main theorem: dimension-free stabilization of the Boolean Poincare endpoint

### Theorem 2.1

Let

\[
f:\{-1,1\}^k\to\{-1,1\},\qquad \mathbb Ef=0,
\]

with uniform Fourier expansion

\[
f=\sum_{\varnothing\ne S\subseteq[k]} a_S\chi_S,
\qquad
\sum_S a_S^2=1.
\]

Write

\[
I(f)=\sum_S |S|a_S^2=1+\delta.
\]

Then

\[
\boxed{
\max_{1\le i\le k} a_{\{i\}}^2
\ge
1-(3+\sqrt3)\delta.
}
\tag{2.1}
\]

Equivalently, whenever the right side is positive, an actual singleton character carries all but at most

\[
(3+\sqrt3)\delta
=4.732050807568877\ldots\,\delta
\]

of the spectral mass.

### Proof

Put

\[
b_i=a_{\{i\}},
\qquad
L=\sum_i b_i\chi_i,
\qquad
s=\|L\|_2^2=\sum_i b_i^2,
\qquad
\varepsilon=1-s.
\tag{2.2}
\]

Because \(f\) is balanced, every Fourier atom has level at least one.  Hence

\[
\delta=I(f)-1
=\sum_{|S|\ge2}(|S|-1)a_S^2
\ge\sum_{|S|\ge2}a_S^2
=\varepsilon.
\tag{2.3}
\]

Now use Booleanity with its sign intact.  Since \(f^2\equiv1\),

\[
\mathbb E(fL)=\sum_i b_i\widehat f(\{i\})=s,
\]

and therefore

\[
\|fL-1\|_2^2
=\mathbb E L^2+1-2\mathbb E(fL)
=1-s=\varepsilon.
\tag{2.4}
\]

The constant Fourier coefficient of \(fL-1\) is \(s-1=-\varepsilon\), so its total **nonconstant** Fourier energy is exactly

\[
\varepsilon-\varepsilon^2=\varepsilon s.
\tag{2.5}
\]

For a pair \(\{i,j\}\), \(i<j\), the corresponding Fourier coefficient of \(fL-1\) is

\[
c_{ij}=2b_i b_j+e_{ij},
\qquad
e_{ij}=\sum_{\ell\notin\{i,j\}}b_\ell a_{\{i,j,\ell\}}.
\tag{2.6}
\]

By (2.5),

\[
\sum_{i<j}c_{ij}^2\le\varepsilon s.
\tag{2.7}
\]

For the error vector, Cauchy--Schwarz gives

\[
e_{ij}^2
\le s\sum_{\ell\notin\{i,j\}}a_{\{i,j,\ell\}}^2.
\]

After summing over \(i<j\), every level-three coefficient is counted exactly three times; hence

\[
\sum_{i<j}e_{ij}^2
\le3s\sum_{|S|=3}a_S^2
\le3s\varepsilon.
\tag{2.8}
\]

Let \(u_{ij}=2b_i b_j\).  From \(u=c-e\), (2.7), (2.8), and the triangle inequality in \(\ell_2\),

\[
\begin{aligned}
4\sum_{i<j}b_i^2b_j^2
=\|u\|_2^2
&\le(\|c\|_2+\|e\|_2)^2\\
&\le(1+\sqrt3)^2\varepsilon s\\
&=(4+2\sqrt3)\varepsilon s.
\end{aligned}
\tag{2.9}
\]

Therefore

\[
\begin{aligned}
\sum_i b_i^4
&=s^2-2\sum_{i<j}b_i^2b_j^2\\
&\ge s^2-(2+\sqrt3)\varepsilon s\\
&=s\,[1-(3+\sqrt3)\varepsilon].
\end{aligned}
\tag{2.10}
\]

If \(s=0\), (2.1) is trivial because its right side is nonpositive.  If \(s>0\),

\[
\max_i b_i^2
\ge {\sum_i b_i^4\over\sum_i b_i^2}
\ge1-(3+\sqrt3)\varepsilon
\ge1-(3+\sqrt3)\delta,
\]

using (2.3).  This proves the theorem. \(\square\)

The proof uses the actual signed Boolean source twice: first through \(f^2=1\) in (2.4), and then through the exact signed pair coefficient (2.6).  An arbitrary probability law on spectral subsets need not satisfy either identity.

## 3. Direct application to the peer's Gibbs/Bellman residual

Specialize the peer's exact residual to the balanced uniform slice:

\[
p_i=q=\frac12,
\qquad
C=C^\dagger,
\qquad
x=2^{-C}.
\]

Because \(w(\varnothing)=0\), here \(w^+=w\).  For any real \(\lambda\), put

\[
y=x^{1-\lambda},
\qquad
A=(1+y)^k-1.
\]

Then the Bellman comparison law is

\[
\rho_\lambda(S)={y^{|S|}\over A}
\qquad(S\ne\varnothing),
\tag{3.1}
\]

and its mass on each fixed singleton is \(y/A\).

Let \(I(f)=1+\delta\), let

\[
t=(3+\sqrt3)\delta,
\]

and choose \(i_*\) from Theorem 2.1.  If \(t<1\) and

\[
1-t\ge {y\over A},
\tag{3.2}
\]

data processing through the event \(S=\{i_*\}\) gives

\[
D_{\rm KL,2}(w\|\rho_\lambda)
\ge
 d_2\!\left(1-t\,\middle\|\,{y\over A}\right),
\tag{3.3}
\]

where \(d_2\) is binary relative entropy in bits.  Applying (3.3) to the exact peer identity (0.3), and using \(m=C(1+\delta)\), yields

\[
\boxed{
R_B(f;1/2^k)
\ge
 d_2\!\left(1-t\,\middle\|\,{y\over A}\right)
+\lambda C(1+\delta)-\log_2{A\over x}.
}
\tag{3.4}
\]

The expression simplifies exactly to

\[
\boxed{
R_B(f;1/2^k)
\ge
\lambda C\delta
-h_2(t)
-t\log_2{A-y\over y}.
}
\tag{3.5}
\]

This is a source-valid quantitative Boolean correction to the scalar Bellman relaxation.  It excludes the peer's generic multi-singleton endpoint optimizer: as \(\delta\to0\), the actual source has one singleton atom of mass tending to one.

Equation (3.5) is **not** asserted nonnegative for every \(k,\delta\).  It is an explicit applied bound on the exact common residual.  Its remaining loss treats all non-dominant spectral mass as one undifferentiated leakage packet and therefore pays the binary entropy \(h_2(t)\) without using the excess-level price of that leakage.  That is now the precise missing conditional-Shannon increment.

## 4. A stronger tempting endpoint claim is false: sparse balanced defects

One might hope to replace the linear leakage in Theorem 2.1 by a universal quadratic bound

\[
1-\max_i a_{\{i\}}^2=O(\delta^2).
\tag{4.1}
\]

That is false even for genuine balanced Boolean sources.

Start from the dictator \(\chi_1\) on \(k\) variables and flip its value at two vertices with opposite \(\chi_1\)-sign and Hamming distance at least two.  Balance is preserved.  The coefficient of \(\chi_1\) becomes

\[
\alpha=1-2^{2-k},
\]

so

\[
1-\alpha^2
=2^{3-k}-2^{4-2k}.
\tag{4.2}
\]

Choose the two flipped vertices so that their incident edge sets do not overlap.  Relative to the dictator, at each flipped vertex the coordinate-1 boundary edge is removed and the other \(k-1\) incident edges are added.  Hence

\[
I(f)-1=(k-2)2^{2-k}.
\tag{4.3}
\]

Consequently

\[
{1-\alpha^2\over (I(f)-1)^2}
\asymp {2^k\over k^2}\to\infty.
\tag{4.4}
\]

Thus a quadratic one-character concentration theorem cannot be the missing universal step.  This is exactly the kind of sparse-defect obstruction that must be applied before strengthening the endpoint lemma.  The remaining proof has to spend the **actual degree/price structure of the leakage**, not simply demand that the leakage mass be quadratically small.

## 5. Exact old/new missing implications

**Candidate/version:** `LIMIT-PRIME-GATE-LIFT-v1`, common residual `B-GIBBS-KL-v1` from fleet03/B18 `20260922T075546Z-gibbs-price-bellman`.

**Old first essential missing implication:** in the low Bellman-price region, quantitatively rule out the non-Boolean multi-singleton I-projection by signed Boolean realizability.

**New proved inference:** every balanced Boolean source with spectral mean level \(1+\delta\) has a genuine singleton atom of mass at least \(1-(3+\sqrt3)\delta\), and this gives the explicit residual lower bounds (3.4)--(3.5) when applied to the exact Gibbs/Bellman identity.

**Refuted stronger shortcut:** `best-character leakage = O(delta^2)` is false by the balanced two-point sparse-defect family (4.2)--(4.4).

**New first essential missing implication:** refine (3.3) by a source-valid decomposition of the non-dominant leakage according to actual Gibbs price/degree (and, off center, original-coordinate price) so that its conditional entropy is paid by its excess mean cost rather than by the coarse `h_2(t)` term.  This must survive sparse defects, addressing-type coordinate-label stress, tensor products, majority/tribes, and biased limits.  No such universal refinement is proved here.

**Target-level status:** `OPEN -> OPEN`; this is an applied essential Boolean step, not a full proof candidate.

## 6. Scope and provenance

Only the authorized FEI repository state and the named source-bound peer theorem above were used.  This report contains no credentials, scheduler identifiers, machine paths, unrelated private material, held-out benchmark content, email/Drive data, public-posting action, remote workflow, paid compute, or permission change.  The mathematics was manually reviewed for the stated scope before commit.  No claim of publication priority is made.
