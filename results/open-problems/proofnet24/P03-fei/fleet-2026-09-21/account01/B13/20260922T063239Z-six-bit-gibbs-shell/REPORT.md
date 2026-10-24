# account01/B13 — degree-weighted Gibbs shell forces a large first Fourier level in every balanced six-bit threat

**Classification:** `ESSENTIAL_STEP_APPLIED / BAL6_FIRST_SHELL_FORCED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source-bound mathematical artifacts were read directly; no separately verified native research-brain receiver/context entered the derivation.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact live candidate and compact end-to-end chain

This run binds to the current Campaign-A lead candidate in

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`

at the immutable scientific snapshot read this run, with

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
a^\dagger=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]
For a Boolean gate at product bias vector `p`, the live defect is

\[
D_{\Gamma^\dagger}(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma^\dagger(p_i)+h_2(V_{p_i})]
-\Gamma^\dagger(p_{\rm out})-\widetilde H_G(p).
\]
The source-exact gate reformulation says that proving
\(D_{\Gamma^\dagger}(P;p)\ge0\) for every finite composition-prime Boolean gate and every interior product bias implies the same for all gates by the composition cocycle and hence full FEI with constant \(C^\dagger\). This universal prime-gate statement is still open.

The previous own B13 run localized any uniform negative defect to an excessive signed request before the restriction tree reaches five live variables. This run changes mechanism: it attacks the smallest remaining balanced six-variable obstruction directly through the *degree-weighted entropy variational problem*, retaining the exact influence penalty instead of adding another restriction profile.

The exact named other-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T043158Z-balanced-six-two-generation/REPORT.md`.

That theorem proves that a balanced six-input uniform falsifier of the live centre inequality cannot have a zero singleton Fourier coefficient. I combine that Boolean two-generation result with the new theorem below; the combination forces the putative falsifier into a much smaller, quantitatively high-correlation chamber.

A second compatible source used to locate the frontier is

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0526Z-balanced-arity5-center/REPORT.md`,

which proves the entire balanced five-input uniform centre at the stronger constant 6. Thus the six-bit balanced slice is the first unresolved central slice after the completed five-bit theorem, and a restriction with strongly unbalanced children really is the relevant remaining direction rather than another balanced-child calculation.

## 1. Degree-weighted Gibbs inequality

Let
\[
f:\{-1,+1\}^6\to\{-1,+1\}
\]
be balanced under the uniform measure. Write
\[
p_S=\widehat f(S)^2,\qquad
W_1=\sum_{|S|=1}p_S=:w,
\qquad q=1-w.
\]
Balance gives \(p_\varnothing=0\). At the balanced uniform centre, the live gate inequality is exactly

\[
H(f)\le C^\dagger[I(f)-1].
\tag{1.1}
\]

For any \(C>0\), decompose its signed excess as

\[
\begin{aligned}
H(f)-C[I(f)-1]
={}&\sum_{|S|=1}p_S\log_2{1\over p_S}\\
&+\sum_{|S|\ge2}p_S
\left(\log_2{1\over p_S}-C(|S|-1)\right).
\end{aligned}
\tag{1.2}
\]

The singleton contribution is maximized at fixed total mass \(w\) by spreading that mass uniformly over the six singleton atoms:

\[
\sum_{|S|=1}p_S\log_2{1\over p_S}
\le w\log_2{6\over w}.
\tag{1.3}
\]

For the higher levels put

\[
y_S:=2^{-C(|S|-1)},\qquad
Z_C:=\sum_{|S|\ge2}y_S
=15\,2^{-C}+20\,2^{-2C}+15\,2^{-3C}+6\,2^{-4C}+2^{-5C}.
\tag{1.4}
\]

The log-sum inequality gives, with total high-degree mass \(q\),

\[
\begin{aligned}
\sum_{|S|\ge2}p_S
\left(\log_2{1\over p_S}-C(|S|-1)\right)
&=\sum_{|S|\ge2}p_S\log_2{y_S\over p_S}\\
&\le q\log_2{Z_C\over q}.
\end{aligned}
\tag{1.5}
\]

Therefore every balanced six-bit Boolean function satisfies the exact dimension-six Gibbs envelope

\[
\boxed{
H(f)-C[I(f)-1]
\le
w\log_2{6\over w}
+(1-w)\log_2{Z_C\over1-w}.
}
\tag{1.6}
\]

No Booleanity has yet been discarded except by enlarging the admissible spectra in the entropy maximization, so (1.6) is a valid upper bound for every actual Boolean spectrum.

## 2. Rigorous endpoint: `W_1 <= 83/256` is impossible for a live falsifier

Set \(C=C^\dagger\). We first bound the partition factor without a floating-point sign decision.

The positive atanh expansion gives

\[
\ln2
=2\sum_{k\ge0}{1\over(2k+1)3^{2k+1}}
>
2\sum_{k=0}^{2}{1\over(2k+1)3^{2k+1}}
>0.693.
\tag{2.1}
\]
Hence
\[
2^{0.52}=e^{0.52\ln2}
>e^{0.52(0.693)}.
\]
Using the positive Taylor polynomial through degree four,
\[
e^{0.52(0.693)}
>\sum_{j=0}^{4}{(0.52\cdot0.693)^j\over j!}
>{10000\over109\cdot64}.
\tag{2.2}
\]
Thus
\[
2^{-6.52}< {109\over10000}=0.0109.
\tag{2.3}
\]
Since \(C^\dagger>6.52\), if \(x=109/10000\), then

\[
Z_{C^\dagger}
<Z_*:=15x+20x^2+15x^3+6x^4+x^5
=0.165895710283759\ldots .
\tag{2.4}
\]

For fixed \(Z<1\), the right side of (1.6) is increasing in \(w\) throughout \(0<w\le83/256\), because its natural-log derivative is

\[
\ln {6(1-w)\over wZ}>0.
\tag{2.5}
\]
Consequently it suffices to test \(w=83/256\) and the larger value \(Z_*\).

The adjacent exact-arithmetic checker bounds logarithms with

\[
\ln r=2\sum_{k\ge0}{z^{2k+1}\over2k+1},
\qquad z={r-1\over r+1},
\tag{2.6}
\]
using a positive geometric remainder. With 100 terms it proves the **rational** upper bound on the natural-log numerator

\[
{83\over256}\ln {6\over83/256}
+{173\over256}\ln {Z_*\over173/256}
<-{3\over1000}.
\tag{2.7}
\]
Because \(0<\ln2<1\), division by \(\ln2\) makes this negative number even smaller. Therefore

\[
\boxed{
W_1\le{83\over256}
\quad\Longrightarrow\quad
H(f)-C^\dagger[I(f)-1]<-0.003.
}
\tag{2.8}
\]

### Theorem 2.1 — forced first-shell mass

Every balanced six-input uniform Boolean gate violating the current candidate must obey

\[
\boxed{W_1>{83\over256}.}
\tag{2.9}
\]

This is an analytic implication of the actual candidate, not a finite gate sweep.

## 3. Boolean quantization upgrades the threshold to `21/64`

For a balanced six-bit Boolean function, every singleton Walsh coefficient is an integer multiple of \(1/16\). Indeed, both \(f\) and a singleton character are balanced, so their Hamming distance is even; hence their unnormalized inner product is divisible by four. Thus

\[
\widehat f(\{i\})={m_i\over16},\qquad m_i\in\mathbb Z,
\tag{3.1}
\]
and
\[
W_1={1\over256}\sum_{i=1}^6m_i^2.
\tag{3.2}
\]

Combining (2.9) with integrality gives the stronger exact statement

\[
\boxed{
W_1\ge{84\over256}={21\over64}.
}
\tag{3.3}
\]

Now apply the consumed account03/B13 theorem: a live balanced six-bit falsifier must also have

\[
\boxed{m_i\ne0\quad\text{for all six coordinates}.}
\tag{3.4}
\]

Since six integer squares sum to at least 84, at least one satisfies \(m_i^2\ge14\), hence

\[
\boxed{
\max_i|\widehat f(\{i\})|\ge{1\over4}.
}
\tag{3.5}
\]

For a balanced parent, the two five-bit restrictions in coordinate \(i\) have opposite means \(\pm\widehat f(\{i\})\). Their output probabilities are therefore

\[
{1\over2}\mp {\widehat f(\{i\})\over2}.
\]
Thus every hypothetical balanced six-input falsifier has a **physical pivot whose two child output measures lie at or beyond**

\[
\boxed{3/8\quad\text{and}\quad5/8.}
\tag{3.6}
\]

There is a simple stronger dichotomy. If at most one \(|m_i|\) were at least 4, the other five squares would each be at most 9. Hence either

\[
\boxed{\text{at least two coordinates have }|\widehat f_i|\ge1/4,}
\tag{3.7a}
\]
or the unique large coordinate must satisfy

\[
\boxed{|\widehat f_i|\ge7/16,}
\tag{3.7b}
\]
which sends its two child output probabilities to at most \(9/32\) and at least \(23/32\).

This is exactly a structural condition for the selected physical restriction: the unresolved six-bit balanced threat cannot remain in a nearly-balanced-child tube on every coordinate.

## 4. Relation to the named obstructions and current lead

This theorem does **not** claim that large first-level mass is impossible. Majority-like Boolean functions can have substantial first-level mass, so replacing the remaining problem by a false generic `W_1` upper bound would simply reopen a known bad style of argument. Instead (2.9)-(3.7) say that *if* the live gate candidate fails in the first unresolved balanced central dimension, the failure must be carried by strong original-coordinate correlations and hence by an explicitly off-center five-bit child pair.

That conclusion dovetails with the completed account04/B12 balanced five-input theorem: balanced five-bit children are already safe, so the remaining six-bit central obstruction is necessarily pushed into the unbalanced-child sector. It also respects the addressing, sparse-defect, tensor, majority/tribes and biased-limit warnings: no assumption about any of those families enters (1.6), and no finite search over them is promoted to a universal statement.

The current account01/B18 MUX work already pays one important class of unequal-child restrictions, but it does not yet cover arbitrary five-bit children at output measures as far apart as (3.6). The next exact inference on this route is therefore sharply stated:

> **BAL6-STRONG-PIVOT.** For a balanced six-bit gate with `W_1>=21/64`, all singleton coefficients nonzero, and a physical pivot satisfying (3.6), use the actual five-bit child slacks plus the exact two-channel restriction cocycle to prove nonnegative parent defect; or construct a genuine Boolean counterexample in that chamber.

Proving `BAL6-STRONG-PIVOT` would close the balanced six-bit central slice of the live candidate. It would still not by itself prove all arities/all biases; full FEI remains open.

## 5. Exact old/new missing implications and status

**Old missing implication.** The preceding own B13 run showed that a uniform negative defect must generate an excessive signed request before the tree reaches five live variables, but it did not characterize the Boolean geometry of the first unresolved six-bit node. The compatible account03/B13 theorem only forced six nonzero singleton coefficients, i.e. \(W_1\ge3/128\).

**New proved inference.** The degree-weighted Gibbs envelope plus six-bit Walsh quantization upgrades that by a factor fourteen:

\[
\boxed{W_1\ge21/64,}
\]
with at least one original-coordinate correlation of magnitude \(1/4\), and the dichotomy (3.7). This is directly applied to the live candidate and to the physical restriction selected by Campaign A.

**Remaining obligation.** Pay or falsify the exact strongly-unbalanced five-bit child pair created by (3.6), preserving child slack and the source potential Jensen term. After that, analogous dimension-independent control would still be needed for higher arity and arbitrary interior bias.

Therefore the correct status is

\[
\boxed{\texttt{ESSENTIAL\_STEP\_APPLIED / FULL\_FEI\_OPEN}.}
\]

No claim of a complete FEI proof, no novelty/publication claim, and no claim that a finite computation settles the conjecture is made.

## 6. Verification artifact

`CHECK_GIBBS_SHELL.py` uses `fractions.Fraction` throughout the sign certificate. It verifies (2.1)-(2.4) and the rational logarithm bound (2.7) with a positive-tail atanh-series enclosure. The archived output is `CHECK_OUTPUT.txt`; it prints `PASS=True` and the endpoint natural-log upper bound

\[
-0.0030400471558462605\ldots<-0.003.
\]

The analytic proof above is independent of any enumeration of Boolean truth tables.
