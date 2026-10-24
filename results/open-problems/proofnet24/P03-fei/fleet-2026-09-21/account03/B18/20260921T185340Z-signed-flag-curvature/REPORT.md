# B18 FEI proof integration — character-folded signed flag curvature and the missing orientation bank

**Date:** 21 September 2026  
**Scope:** `account03 / B18`, full-FEI proof integration  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact universal Boolean source theorems, an exact Boolean obstruction to an unsigned-only compiler interface, and a corrected signed-Hilbert compiler target. No novelty or publication-priority claim.

## 0. Fresh state and exact implication attacked

This run followed the live FEI owner order and read, in order, `TASKS_2026-09-21.md`, `REPORT.md`, and `APPROACHES.md` before new mathematics. Scientific `master` was refreshed during the run through commit `91c43c9c0bd4e8c03637a5a68520c67ca154f35c`.

The compatible newest inputs used are:

1. account03/B18 `20260921T183340Z-flag-square-radon`: for the unsigned physical derivative-support disagreement
   \[
   p_i(w)=\Pr[\eta_i(x)\ne\eta_i(x+w)],
   \qquad \eta_i=1_{\{f(x)\ne f(x+e_i)\}},
   \]
   the ordered physical flag pays
   \[
   \sum_i\mathbb E_{\nu_i^\pi}p_i(W)^2\le J(f),
   \]
   and the random-order second moment has an exact Hardy collision kernel;
2. account02/B16 `20260921T184541Z-actual-current-parent-mask-incidence`: after authentic same-syndrome signed aggregation, the central clone-pair current has exact positive parent coefficients
   \[
   \mu_{R,j}^{\rm cen}=\frac{\varepsilon_{q_R,k_R}}{r_R}b_R^2,
   \]
   but the physical source pushforward is still open;
3. account04/B16 `20260921T184003Z-phase-switch-dirichlet`: the odd-syndrome current is an exact global phase-switch Dirichlet energy, the dual-code quadratic response cancels, the first possible retained response is quartic, and the next stated target is to insert the ordered physical flag/Hardy kernel at large Borel time **before taking absolute values**;
4. the phase/sign stability line: derivative rows are ternary `0,±1`, and sign information cannot in general be reconstructed from their support alone.

The exact implication attacked here is the source-side part of the marked-pair pushforward:

> **Can the authentic additive clone-pair curvature be sent to the previously proved unsigned support-disagreement bank \(p_i(w)\) without retaining an additional phase/orientation variable?**

The answer is **no in general, already for a genuine Boolean function**. The obstruction is exact and has a clean repair. The correct physical Hilbert source is the **signed derivative curvature**
\[
\kappa_i(w)=\|d_i-\tau_w d_i\|_2^2,
\]
which differs from \(p_i(w)\) by one explicit opposite-sign overlap bank. That signed bank is itself dimension-free under the same ordered flag, and after the same minimizing-character gauge used in the newest B16 phase-switch argument it is paid by \(J(f)\).

This does **not** prove that the authentic B16 compiler has the required PSD contraction. It changes the correct target of that contraction and removes a genuine Boolean obstruction to an unsigned-only identification.

---

## 1. Character-gauged signed derivative rows

Let
\[
f:\mathbb F_2^n\to\{-1,+1\}.
\]
For a character \(K\subseteq[n]\), write
\[
g_K(x)=f(x)(-1)^{K\cdot x}.
\]

Fix a physical coordinate \(i\). On the quotient with \(x_i=0\), define the oriented derivative row
\[
d_i^K(y)
=\frac{g_K(0,y)-g_K(1,y)}2
\in\{-1,0,+1\}.
\tag{1.1}
\]
Its support density is exactly
\[
\alpha_i^K:=\mathbb E_y (d_i^K(y))^2
=\operatorname{Inf}_i(g_K).
\tag{1.2}
\]

Character multiplication flips the edge-disagreement bit exactly on coordinates belonging to \(K\). Hence
\[
\operatorname{Inf}_i(g_K)
=
\begin{cases}
\operatorname{Inf}_i(f),&i\notin K,\\
1-\operatorname{Inf}_i(f),&i\in K.
\end{cases}
\tag{1.3}
\]
Therefore, with
\[
K_*=\{i:\operatorname{Inf}_i(f)>1/2\},
\qquad
\beta_i=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
\tag{1.4}
\]
we have
\[
\boxed{\alpha_i^{K_*}=\beta_i,\qquad
I(g_{K_*})=\sum_i\beta_i=:J(f).}
\tag{1.5}
\]

The newest B16 phase-switch continuation already works in this minimizing-character gauge. No claim below silently changes gauge: the \(J(f)\) version is to be used only where that same character conjugation is legitimate. Without it, all statements remain valid with \(I(g_K)\).

For \(w_i=0\), define the signed Hilbert curvature
\[
\boxed{
\kappa_i^K(w)
:=\mathbb E_y\bigl(d_i^K(y)-d_i^K(y+w)\bigr)^2.
}
\tag{1.6}
\]

---

## 2. PROVED — exact plaquette sign decomposition

Let
\[
\eta_i^K(y)=(d_i^K(y))^2\in\{0,1\}.
\]
If \(i\notin K\), this is the ordinary \(i\)-sensitivity bit of \(f\); if \(i\in K\), it is its complement. Therefore its symmetric-difference probability is independent of \(K\):
\[
p_i(w)
:=\Pr_y[\eta_i^K(y)\ne\eta_i^K(y+w)].
\tag{2.1}
\]

Define the opposite-orientation overlap
\[
o_i^K(w)
:=\Pr_y[
d_i^K(y)=-d_i^K(y+w)\ne0].
\tag{2.2}
\]

### Theorem 2.1 — `P03-B18-SIGNED-PLAQUETTE-DECOMPOSITION` — PROVED

For every Boolean \(f\), every character gauge \(K\), every coordinate \(i\), and every \(w\) with \(w_i=0\),
\[
\boxed{
\kappa_i^K(w)=p_i(w)+4o_i^K(w).
}
\tag{2.3}
\]

### Proof

For a pair
\[
a=d_i^K(y),\qquad b=d_i^K(y+w)
\]
there are only four relevant cases.

* Exactly one of \(a,b\) is nonzero: \(a^2\ne b^2\), so the support-disagreement contributes \(1\), the opposite-sign indicator contributes \(0\), and \((a-b)^2=1\).
* Both are zero: all three quantities vanish.
* Both are equal nonzero: all three quantities vanish.
* Both are nonzero with opposite signs: the support bits agree, so \(p\) contributes \(0\); \(o\) contributes \(1\); and \((a-b)^2=4\).

Averaging gives (2.3). \(\square\)

This identity isolates exactly what the unsigned q-flip source forgets: **orientation reversal on an edge that remains sensitive on both sides of the plaquette**.

---

## 3. REFUTED — additive physical curvature is not dominated by unsigned \(p_i\)

Any universal pointwise claim of the form
\[
\kappa_i^K(w)\le C\,p_i(w)
\quad\text{or}\quad
(\kappa_i^K(w))^2\le C\,p_i(w)^2
\tag{3.1}
\]
with finite \(C\) is false.

A two-variable parity already suffices. Take
\[
f(x_i,x_j)=(-1)^{x_i+x_j},
\qquad K=\varnothing,
\qquad w=e_j.
\]
Then the \(i\)-edge is sensitive everywhere, so
\[
\eta_i\equiv1,\qquad p_i(e_j)=0.
\]
But the oriented derivative is
\[
d_i(x_j)=(-1)^{x_j},
\]
hence translation by \(e_j\) reverses its sign everywhere:
\[
o_i(e_j)=1,\qquad
\kappa_i(e_j)=4.
\tag{3.2}
\]

Thus an **unsigned-only identification of a generic additive q-flip curvature with the scalar transport distance \(p_i\)** is impossible on genuine Boolean data.

This does **not** refute the authentic B16 compiler contraction itself. The retained dual-code/same-syndrome structure could annihilate this component. What it refutes is the shortcut that such annihilation may be assumed merely because the unsigned dependent-face transport is small. A correct proof must either:

1. prove that the authentic compiler kills the \(o_i^K\) component; or
2. retain and pay that component.

The next sections show option 2 is dimension-free.

---

## 4. PROVED — ordered-flag signed Dirichlet payment

Fix a coordinate order \(\pi\). Let
\[
L_i^\pi=\{j:\pi(j)>\pi(i)\}
\]
and let \(\nu_i^\pi\) be the uniform law on all subsets of \(L_i^\pi\), including the harmless zero vector.

Expand the quotient row in Walsh characters:
\[
d_i^K(y)=\sum_{U\subseteq[n]\setminus\{i\}}
\widehat d_i^K(U)\chi_U(y),
\qquad
b_i^K(U):=\widehat d_i^K(U)^2.
\tag{4.1}
\]
Parseval gives
\[
\sum_U b_i^K(U)=\alpha_i^K.
\tag{4.2}
\]

Group squared coefficients by their trace on the later flag:
\[
B_{i,\pi}^K(V)
=
\sum_{U:U\cap L_i^\pi=V}b_i^K(U),
\qquad V\subseteq L_i^\pi,
\tag{4.3}
\]
and put
\[
T_{i,\pi}^K
=\sum_{V\ne\varnothing}B_{i,\pi}^K(V)
\le\alpha_i^K.
\tag{4.4}
\]

Translation diagonalizes the Walsh basis, so
\[
\kappa_i^K(w)
=
2T_{i,\pi}^K
-
2\sum_{V\ne\varnothing}
B_{i,\pi}^K(V)(-1)^{V\cdot w}
\tag{4.5}
\]
for \(w\subseteq L_i^\pi\).

Uniform flag characters are orthogonal. Therefore:

### Theorem 4.1 — `P03-B18-SIGNED-FLAG-DIRICHLET` — PROVED

For every Boolean \(f\), gauge \(K\), order \(\pi\), and coordinate \(i\),
\[
\boxed{
\mathbb E_{W\sim\nu_i^\pi}\kappa_i^K(W)
=2T_{i,\pi}^K
\le2\alpha_i^K.
}
\tag{4.6}
\]

Summing the physical pivots,
\[
\boxed{
\sum_i\mathbb E_{\nu_i^\pi}\kappa_i^K(W)
\le2I(g_K).
}
\tag{4.7}
\]

In the minimizing-character gauge \(K_*\),
\[
\boxed{
\sum_i\mathbb E_{\nu_i^\pi}\kappa_i^{K_*}(W)
\le2J(f).
}
\tag{4.8}
\]

This is the Hilbert-space source analogue of the unsigned flag theorem. It is already a **quadratic** quantity—the squared \(L^2\) distance between two signed derivative rows—so a PSD compiler contraction into (4.8) does not require squaring a scalar Wasserstein discrepancy again.

---

## 5. PROVED — the missing sign bank is itself paid once

Average the exact identity (2.3) under the flag. Since \(p_i\ge0\),
\[
4\mathbb E o_i^K(W)
\le
\mathbb E\kappa_i^K(W)
\le2\alpha_i^K.
\]
Hence
\[
\boxed{
\mathbb E_{\nu_i^\pi}o_i^K(W)
\le\frac{\alpha_i^K}{2}.
}
\tag{5.1}
\]

Summing:
\[
\boxed{
\sum_i\mathbb E_{\nu_i^\pi}o_i^K(W)
\le\frac12I(g_K).
}
\tag{5.2}
\]
In the minimizing-character gauge,
\[
\boxed{
\sum_i\mathbb E_{\nu_i^\pi}o_i^{K_*}(W)
\le\frac12J(f).
}
\tag{5.3}
\]

Thus the precise orientation correction missed by the unsigned source is not an uncontrolled new ledger. Under the same physical flag it costs at most one half of the folded influence bank.

No terminal, R16/moment, negative-entropy, or resolvent-boundary credit is used in (5.3).

---

## 6. PROVED — signed flag second moment and a sharp folded constant

Squaring (4.5) and using flag-character orthogonality gives the exact Plancherel identity
\[
\boxed{
\mathbb E_{\nu_i^\pi}\kappa_i^K(W)^2
=
4(T_{i,\pi}^K)^2
+
4\sum_{V\ne\varnothing}B_{i,\pi}^K(V)^2.
}
\tag{6.1}
\]

Because the \(B(V)\) are nonnegative and sum to \(T\),
\[
\sum_{V\ne0}B(V)^2\le T^2.
\]
Therefore
\[
\boxed{
\mathbb E\kappa_i^K(W)^2
\le8(T_{i,\pi}^K)^2
\le8(\alpha_i^K)^2.
}
\tag{6.2}
\]

In the minimizing gauge \(\alpha_i^{K_*}=\beta_i\le1/2\), so
\[
8\beta_i^2\le4\beta_i
\]
and hence
\[
\boxed{
\sum_i\mathbb E_{\nu_i^\pi}
\kappa_i^{K_*}(W)^2
\le4J(f).
}
\tag{6.3}
\]

So there are two compiler-facing sinks:

* **Hilbert quadratic sink:** a PSD term dominated directly by \(\kappa_i\) costs at most \(2J(f)\);
* **scalar-square sink:** a scalar discrepancy bounded in absolute value by \(\kappa_i\) costs at most \(4J(f)\).

### Sharp folded local example

The constants \(2\), \(4\), and \(1/2\) above are all attained coordinatewise.

Use three coordinates \((a,i,b)\), ordered \(a<i<b\), and define
\[
f(a,i,b)=
\begin{cases}
1,&a=1,\\
(-1)^{i+b},&a=0.
\end{cases}
\tag{6.4}
\]
Then
\[
d_i(a,b)=1_{\{a=0\}}(-1)^b,
\qquad
\alpha_i=\frac12.
\]
The later flag at \(i\) is \(\{\varnothing,\{b\}\}\). For \(w=e_b\), the support is unchanged but the derivative sign reverses on its whole support:
\[
p_i(e_b)=0,\qquad
o_i(e_b)=\frac12,\qquad
\kappa_i(e_b)=2.
\]
Consequently
\[
\mathbb E_\nu\kappa_i=1=2\alpha_i,
\]
\[
\mathbb E_\nu\kappa_i^2=2=4\alpha_i,
\]
and
\[
\mathbb E_\nu o_i=\frac14=\frac{\alpha_i}{2}.
\tag{6.5}
\]

So the orientation correction cannot be removed even after folding to influence \(1/2\), and the stated coordinatewise constants cannot be improved.

---

## 7. PROVED — exact signed Hardy collision kernel

Average the coordinate order uniformly and then sample \(W\sim\nu_i^\Pi\). The inherited random-flag calculation
\[
\mathbb E_{\Pi,W}(-1)^{U\cdot W}
=\frac1{|U|+1}
\tag{7.1}
\]
applies to the signed derivative row just as it does to the unsigned support indicator.

Therefore
\[
\boxed{
\mathbb E_{\Pi,W}\kappa_i^K(W)
=
2\sum_{U\ne\varnothing}
b_i^K(U)\frac{|U|}{|U|+1}.
}
\tag{7.2}
\]

The second moment has the exact pair kernel
\[
\boxed{
\mathbb E_{\Pi,W}\kappa_i^K(W)^2
=
4\sum_{U,V\ne\varnothing}
b_i^K(U)b_i^K(V)K(U,V),
}
\tag{7.3}
\]
where
\[
\boxed{
K(U,V)
=
1-\frac1{|U|+1}-\frac1{|V|+1}
+\frac1{|U\triangle V|+1}.
}
\tag{7.4}
\]

Equivalently,
\[
K(U,V)
=
\int_0^1
\left(
1-t^{|U|}-t^{|V|}+t^{|U\triangle V|}
\right)\,dt
\ge0.
\tag{7.5}
\]

This is the same Hardy collision geometry found for the unsigned source, but it is now applied to the **signed derivative spectrum**. Hence it sees the parity/orientation modes that the support law \(p_i\) can miss entirely.

This is precisely the form relevant to the newest account04/B16 instruction to insert the ordered physical Hardy kernel before taking absolute values at large Borel time.

---

## 8. Compiler-facing consequence and exact remaining gap

The authentic B16 central current is, after legitimate same-syndrome signed aggregation, a positive quadratic clone-pair bank
\[
\mathcal E_{\rm cen}
=
\frac18
\int_{x,y\le1/2}\int_0^1
\frac{1-y^2}{xy}
\sum_j
\langle D_j\Phi,
N_xC_{y,\lambda}^{(j)}D_j\Phi\rangle
\,d\lambda\,dy\,dx.
\tag{8.1}
\]

The previous B18 route attempted to land such a term in scalar dependent-face discrepancies bounded by the unsigned \(p_i(w)\). Sections 2–3 show why that source interface is incomplete for **additive** curvature unless the authentic compiler proves an additional sign-annihilation statement.

The corrected sufficient interface is:

### Conditional compiler criterion — `P03-B18-SIGNED-HILBERT-COMPILER-CRITERION`

Use the same minimizing character \(K_*\) as the retained phase-switch gauge.

If a portion \(\mathcal Q\) of the authentic post-refund current admits a no-reuse PSD contraction
\[
\boxed{
\mathcal Q
\le
A\sum_i
\mathbb E_{W\sim\nu_i^\pi}
\kappa_i^{K_*}(W),
}
\tag{8.2}
\]
then the proved source theorem gives
\[
\boxed{
\mathcal Q\le2A\,J(f).
}
\tag{8.3}
\]

If instead the compiler produces scalar amplitudes \(z_i(W)\) with
\[
|z_i(W)|\le\kappa_i^{K_*}(W)
\]
and
\[
\mathcal Q\le A\sum_i\mathbb E|z_i(W)|^2,
\]
then
\[
\boxed{
\mathcal Q\le4A\,J(f).
}
\tag{8.4}
\]

These are **conditional implications**, not the missing compiler proof itself.

The important change is conceptual and source-exact: the compiler may preserve the signed Hilbert curvature all the way to the physical flag instead of scalarizing first to unsigned support transport. This is more closely matched to the genuine \(D_j\Phi\) square and to the newest phase-switch instruction to delay absolute values.

The exact next obligation is now:

> Expand one authentic large-Borel marked-pair term through the retained sine-product/MacWilliams representation in the minimizing-character gauge and determine whether its physical image is a PSD contraction of the signed Hardy form (7.2)/(7.3). If yes, (8.3) pays it by \(J(f)\) with no ambient-dimension loss. If not, preserve an explicit authentic R32 packet witnessing the failure and identify the component orthogonal to all signed derivative rows.

The fixed-scale quartic phase-switch estimate, terminal ledger, R16/moment refunds, negative R32 credits, dual-code multiplicity, and resolvent-boundary credits remain untouched here and must not be spent twice.

---

## 9. Exact computation / falsification

`check_signed_flag_curvature.py` uses only the Python standard library and exact `Fraction` arithmetic for the exhaustive part.

It verifies:

* the pointwise identity \(\kappa=p+4o\);
* the exact fixed-flag first and second moment formulas;
* \(\mathbb E\kappa\le2\alpha\);
* \(\mathbb E o\le\alpha/2\);
* \(\mathbb E\kappa^2\le8\alpha^2\);
* in the folded range \(\alpha\le1/2\), \(\mathbb E\kappa^2\le4\alpha\).

Coverage:

* every Boolean function through dimension \(3\), every coordinate, and every possible later-coordinate set: **3,140 exact cases**;
* **4,096** deterministic random Boolean functions in dimension \(4\), all coordinates and all later-coordinate sets: **131,072 additional cases**;
* parity sharpness through dimension \(10\);
* the explicit folded sharp example (6.4).

The exhaustive and sampled maximum of
\[
\frac{\mathbb E\kappa_i(W)^2}{\alpha_i}
\]
is exactly \(8\), attained by the parity obstruction before folding. The folded example gives exactly
\[
\frac{\mathbb E\kappa_i}{\alpha_i}=2,\qquad
\frac{\mathbb E\kappa_i^2}{\alpha_i}=4,\qquad
\frac{\mathbb E o_i}{\alpha_i}=\frac12,
\]
while its unsigned \(p_i\) bank is identically zero on the nontrivial flag translation.

Checker SHA-256:
`cbd52764d4a7c1b5e691a9980a1e84c017a0ee4646ab5648570b3e86c7f0ffbe`.

Sanitized stdout SHA-256:
`ac31cd564870cad303af0dd4de66757eef8ada9a52ed5d50b0619d54106ea88b`.

The computation is falsification/self-check evidence. The all-dimensional statements are proved algebraically above.

---

## 10. Classification

### PROVED

1. Exact Boolean plaquette decomposition
   \[
   \kappa_i^K(w)=p_i(w)+4o_i^K(w).
   \]
2. Exact ordered-flag signed Dirichlet identity and payment
   \[
   \sum_i E\kappa_i^K\le2I(g_K),
   \qquad
   \sum_i E\kappa_i^{K_*}\le2J(f).
   \]
3. Exact dimension-free orientation correction
   \[
   \sum_iEo_i^{K_*}\le J(f)/2.
   \]
4. Exact signed flag second moment and folded payment
   \[
   \sum_iE(\kappa_i^{K_*})^2\le4J(f).
   \]
5. Exact random-order signed Hardy first- and second-moment kernels.

### REFUTED

A generic additive physical q-flip curvature cannot be dominated by the unsigned support-disagreement \(p_i(w)\), pointwise or after squaring. Genuine Boolean parity gives \(p_i(w)=0\) while signed curvature is positive.

### CONDITIONAL

If the authentic post-refund compiler PSD-contracts into the minimizing-gauge signed flag Hilbert bank, it is paid by \(2A J(f)\); a scalar-square version is paid by \(4A J(f)\).

### OPEN

* Derive that authentic PSD contraction from the retained Borel/MacWilliams/sine-product compiler, or produce an authentic R32 packet that refutes it.
* Integrate the large-Borel/endpoint portion without reusing fixed-scale, terminal, R16/moment, negative-credit, or Ward ledgers.
* Close the global FEI proof.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
