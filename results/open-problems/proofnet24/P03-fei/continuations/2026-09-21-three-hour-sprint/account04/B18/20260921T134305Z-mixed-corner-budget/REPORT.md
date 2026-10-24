# B18 FEI proof integration — exact mixed-corner budget for the restriction tree

**Date:** 21 September 2026  
**Fleet scope:** account04/B18  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED universal decomposition. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Priority:** no novelty or publication-priority claim is made.

## 0. Fresh state and the unpaid implication attacked

This run follows `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`, account04/B18: **unified decomposition with a summable influence budget**. The scientific state was recovered through master `357cd199cb2d58f02edfe099c125535611fc8e3b`, including the fresh account02/B18 Han-credit block descent and the latest signed-transport work.

The exact compatible inputs used here are:

1. account01/B14, `fleet-2026-09-21/account01/B14/20260921T114221Z-js-influence-potential/REPORT.md` (blob `9878f58e996e3a3950fc47409fb29c817a105106`): if `B_i=H(S_i|S_{-i})` and `JS_i` is the recombination term in the restriction identity, then on **every** complete adaptive physical restriction tree,
   \[
   \sum_v \mu_v JS_{i(v)}(f_v)\le \frac{2}{\ln2}I(f).
   \tag{0.1}
   \]
2. account04/B18, `continuations/2026-09-21-three-hour-sprint/account04/B18/20260921T131816Z-b18-fei-r12/REPORT.md` (blob `a2eb9b018bb339d038384dad9ee5a894778b0a95`): the exact debit/reserve ledger
   \[
   H(f)=c_*I(f)+\mathcal E_{\mathcal T}(f)-\mathcal R_{\mathcal T}(f),
   \qquad c_*=\frac2{\ln2},
   \tag{0.2}
   \]
   with `E_i=B_i-(c_*/3)Q_i`, `Q_i>=0`, and `R_i>=0`.
3. account03/B18's proper-block compiler (blob `4d0a67f151c9fd9674bd985460c33113c3363418`) and account02/B18's fresh Han-credit block descent at commit `0e386eb3444cfd67d3c785afdf0158e5bf590a3f` are retained as the natural next block-level mechanisms. They are not assumed in the proof below.

The precise question attacked is:

> Can the **remaining erasure-only cost** on an adaptive coordinate restriction tree be charged to a root-level, tree-independent geometric quantity, rather than accumulating a fresh logarithmic loss at every depth?

The answer is **yes**. The root quantity is the total density of mixed `1-versus-3` Boolean two-faces. This gives an exact second-order obstruction and a universal decomposition. It does **not** by itself prove FEI because that mixed-corner budget can be large compared with total influence.

---

## 1. Pivotal indicators and the mixed-corner quantity

Let
\[
f:\{-1,1\}^n\to\{-1,1\}
\]
be Boolean. For a physical coordinate `i`, define the pivotal indicator on the remaining cube
\[
a_i(x_{\widehat i})
:=1_{\{f(+1,x_{\widehat i})\ne f(-1,x_{\widehat i})\}}.
\tag{1.1}
\]
Then
\[
\alpha_i:=\mathbb E a_i=\operatorname{Inf}_i(f).
\tag{1.2}
\]

For distinct `i,j`, put
\[
\beta_{ij}(f):=\operatorname{Inf}_j(a_i).
\tag{1.3}
\]

### Lemma 1.1 — exact mixed-face interpretation — **PROVED**

For every `i!=j`,
\[
\boxed{
\beta_{ij}=\beta_{ji}
=\Pr_{x_{\widehat{i,j}}}
\left[
 f_{++}f_{+-}f_{-+}f_{--}=-1
\right].
}
\tag{1.4}
\]

Thus `beta_ij` is exactly the fraction of physical `(i,j)`-faces on which the four Boolean values have odd sign product, equivalently a `1-versus-3` split.

#### Proof

Fix all coordinates other than `i,j`. On the resulting Boolean square, `a_i` differs between the two `j`-levels precisely when exactly one of the two `i`-edges is bichromatic. A Boolean square has exactly one bichromatic `i`-edge iff it has an odd number of minus signs, equivalently iff the product of its four values is `-1`. The same condition is symmetric in `i,j`, proving (1.4). QED.

Define the root **mixed-corner budget**
\[
\boxed{
\Gamma_2(f):=\sum_{1\le i<j\le n}\beta_{ij}(f).
}
\tag{1.5}
\]

---

## 2. PROVED: the mixed-corner budget is exactly conserved by every coordinate restriction tree

Take any complete adaptive physical **coordinate** restriction tree `T`. At an internal node `v`, let `f_v` be the current restricted function, let `i(v)` be the coordinate queried there, and let
\[
\mu_v=2^{-\operatorname{depth}(v)}
\]
be the uniform-input reach probability. Coordinates already fixed are deleted from `f_v`.

### Theorem 2.1 — pivotal-variation tree conservation — **PROVED**

For every such adaptive tree,
\[
\boxed{
\sum_{v\text{ internal}}
\mu_v\, I(a_{i(v)}^{f_v})
=\Gamma_2(f),
}
\tag{2.1}
\]
where `I(a)` denotes the total influence of the Boolean pivotal indicator on its remaining cube.

#### Proof

Expand the left side by physical pairs. At a node querying `i`,
\[
I(a_i^{f_v})=\sum_{j\ne i}\beta_{ij}(f_v).
\]
Fix one unordered pair `{i,j}` at the root. Along each root-to-leaf history, stop at the first node that queries either `i` or `j`. Before that stopping node neither member of the pair is fixed.

Let `M_ij` be the root event that the physical `(i,j)`-face determined by all other coordinates is mixed, i.e. has sign product `-1`. Conditional on the revealed prefix at any node before the stop,
\[
\beta_{ij}(f_v)=\Pr(M_{ij}\mid\text{that prefix}).
\tag{2.2}
\]
If `M_ij` occurs, the current function cannot have become constant before one of `i,j` is queried, because its residual `(i,j)`-face is nonconstant. Therefore the stopping nodes for the pair form a partition of `M_ij` up to null histories. Summing reach probability times the conditional probability in (2.2) over those stopping nodes gives exactly
\[
\Pr(M_{ij})=\beta_{ij}(f).
\]
Summing this equality over all unordered pairs proves (2.1). QED.

**Interpretation.** Coordinate restriction does not create a repeated second-order charge. Every root mixed face is paid exactly once: when the tree first queries one of its two directions.

---

## 3. PROVED: one-coordinate erasure is paid by pivotal variation plus ordinary influence

Let `S` be the Fourier spectral sample, so
\[
\Pr(S=A)=\widehat f(A)^2.
\]
For a coordinate `i`,
\[
B_i:=H(S_i\mid S_{-i}).
\]
Since `Pr(i in S)=Inf_i(f)=alpha_i`,
\[
B_i\le H(S_i)=h_2(\alpha_i).
\tag{3.1}
\]

### Lemma 3.1 — pivotal isoperimetric erasure bound — **PROVED**

For every Boolean `f` and every coordinate `i`,
\[
\boxed{
B_i
\le \frac12 I(a_i)+\frac{\alpha_i}{\ln2}.
}
\tag{3.2}
\]

#### Proof

Put
\[
r=\min\{\alpha_i,1-\alpha_i\}\le\frac12.
\]
The cube edge-isoperimetric inequality, applied to the smaller of the pivotal set and its complement, gives
\[
I(a_i)\ge 2r\log_2\frac1r.
\tag{3.3}
\]
Also
\[
(1-r)\log_2\frac1{1-r}
\le \frac r{\ln2}
\le \frac{\alpha_i}{\ln2},
\tag{3.4}
\]
using `-ln(1-r)<=r/(1-r)`. Since `h_2(alpha_i)=h_2(r)`, (3.1), (3.3), and (3.4) give (3.2). QED.

This estimate is deliberately local and Boolean. No independence assumption on the spectral sample is used.

---

## 4. The unified universal decomposition

On every complete adaptive coordinate restriction tree,
\[
H(f)=\sum_v\mu_v\bigl(B_{i(v)}(f_v)+JS_{i(v)}(f_v)\bigr).
\tag{4.1}
\]
The exact influence telescope gives
\[
\sum_v\mu_v\alpha_{i(v)}(f_v)=I(f).
\tag{4.2}
\]
By Theorem 2.1 and Lemma 3.1,
\[
\sum_v\mu_v B_{i(v)}(f_v)
\le \frac12\Gamma_2(f)+\frac1{\ln2}I(f).
\tag{4.3}
\]
The inherited bounded Jensen-Shannon potential (0.1) pays the recombination part once globally:
\[
\sum_v\mu_vJS_{i(v)}(f_v)
\le\frac2{\ln2}I(f).
\tag{4.4}
\]
Combining (4.1)-(4.4) gives the main theorem.

### Theorem 4.1 — mixed-corner FEI reduction — **PROVED**

Every uniform-cube Boolean function satisfies
\[
\boxed{
H(f)
\le
\frac3{\ln2}I(f)+\frac12\Gamma_2(f).
}
\tag{4.5}
\]
Numerically,
\[
\frac3{\ln2}=4.328085122666891\ldots.
\]

More precisely, retaining the rebates of the preceding B18 debit/reserve ledger, for **every** complete adaptive coordinate tree,
\[
\boxed{
H(f)
\le
\frac3{\ln2}I(f)+\frac12\Gamma_2(f)
-\frac{2}{3\ln2}\mathcal Q_{\mathcal T}(f)
-\mathcal R_{\mathcal T}(f),
}
\tag{4.6}
\]
where
\[
\mathcal Q_{\mathcal T}=\sum_v\mu_vQ_v\ge0,
\qquad
\mathcal R_{\mathcal T}=\sum_v\mu_vR_v\ge0.
\]

#### Proof of the sharpened form

The prior exact ledger is
\[
H=c_*I+\sum_v\mu_v\left(B_i-\frac{c_*}{3}Q_i\right)-\mathcal R_{\mathcal T},
\qquad c_*=\frac2{\ln2}.
\]
Apply (3.2), then (2.1) and (4.2). The coefficient of `I` becomes
\[
c_*+\frac1{\ln2}=\frac3{\ln2},
\]
and `c_*/3=2/(3 ln2)`. QED.

Thus the account04/B18 sprint assignment now has a source-exact answer: the erasure debit can be reduced to a **root-level tree-independent second-order budget**, while the exact influence budget and the recombination/orientation rebates remain globally summable.

---

## 5. A geometric reformulation: sensitivity corners minus parity refunds

Let
\[
s_f(x)=|\{i:f(x)\ne f(x^{\oplus i})\}|
\]
be pointwise sensitivity. Let `chi_ij` be the probability that an `(i,j)`-face is a checkerboard (`2-versus-2` with all four boundary edges bichromatic), and put
\[
\Xi_2(f)=\sum_{i<j}\chi_{ij}.
\]

On a mixed `1-versus-3` face, exactly one of its four vertices is simultaneously pivotal in both directions. On a checkerboard face, all four vertices are simultaneously pivotal in both directions. Other two-face types contribute zero. Hence
\[
\mathbb E\binom{s_f(X)}2
=\frac14\Gamma_2(f)+\Xi_2(f).
\tag{5.1}
\]
Equivalently,
\[
\boxed{
\frac12\Gamma_2(f)
=\mathbb E[s_f(X)(s_f(X)-1)]-2\Xi_2(f).
}
\tag{5.2}
\]
Therefore (4.6) can also be written
\[
H(f)
\le
\frac3{\ln2}I(f)
+\mathbb E[s(s-1)]-2\Xi_2
-\frac{2}{3\ln2}\mathcal Q_{\mathcal T}
-\mathcal R_{\mathcal T}.
\tag{5.3}
\]

This makes a useful compatibility with the signed/parity routes explicit: **checkerboard two-faces are an exact refund** against the second sensitivity moment. The unpaid second-order geometry consists only of mixed corners, not all pairs of pivotal directions.

---

## 6. Decisive obstruction: a universal `Gamma_2 <= K I` closure is false

The new reduction is not full FEI. The strongest immediate closure,
\[
\Gamma_2(f)\le K I(f)
\quad\text{with universal }K,
\tag{6.1}
\]
is false.

Take the one-point defect on `n` bits: `f=-1` at one cube vertex and `+1` everywhere else. For each coordinate,
\[
\operatorname{Inf}_i(f)=2^{1-n},
\]
so
\[
I(f)=n2^{1-n}.
\tag{6.2}
\]
For each pair `{i,j}`, exactly one of its `2^{n-2}` physical faces contains the exceptional vertex and is mixed, hence
\[
\beta_{ij}=2^{2-n}.
\]
Therefore
\[
\boxed{
\Gamma_2(f)=(n-1)I(f).
}
\tag{6.3}
\]
All checkerboard refunds vanish in this family.

So Theorem 4.1 must be combined with a **selector/block mechanism** in the corner-heavy regime; it cannot be closed by bounding `Gamma_2` alone. This is consistent with the fresh B17 exact selector-composition theorem: the canonical rare one-point selector is cheaply compositional even though its mixed-corner ratio diverges.

---

## 7. Targeted native calculation

A new standard-library checker for this run, not an audit of an old theorem, tests the exact identities and the new local inequality on all Boolean functions up to global sign through `n=4`.

Results:

- **130,933** relevant-coordinate tests of (3.2); minimum observed slack remained positive (`0.114947884252078` at `n=4`);
- fixed-order tree conservation (2.1) had **exact zero error** for every Boolean function through `n=4`;
- the one-point family for `n=2,...,8` produced `Gamma_2/I = 1,2,...,7`, matching the analytic obstruction (6.3).

These finite calculations are only checks. Theorems 1.1, 2.1, 3.1, and 4.1 are analytic and do not depend on enumeration.

---

## 8. Integration with the freshest B18 descent and the exact next lemma

The newly arrived account02/B18 Han-credit theorem proves that on a maximal-ratio critical core, every fixed-cardinality scale has a block descent toll equal to a recombination payment **minus a Han dependence credit**. The present theorem proves, independently, that the entire coordinate-tree erasure term is a root mixed-corner budget paid exactly once.

These fit without circularity:

- **low-corner regime:** (4.6) already gives a constant FEI bound once `Gamma_2/I` is bounded;
- **corner-heavy regime:** (6.3) shows that rare-selector/star geometry can make `Gamma_2/I` large, but the B17 selector-composition theorem demonstrates that at least the canonical star family is still cheap;
- **block escape:** account03/B18 proves that one proper-block erasure payment with a universal coefficient compiles globally with no lifetime loss, while account02/B18 provides a source-exact high-ratio block descent with Han credit.

The next nonredundant universal implication is therefore:

> **OPEN corner-compression lemma.** Prove that every Boolean state with large `Gamma_2/I` contains a proper physical selector/block whose restriction cost is paid by a universal multiple of its block influence and which removes a definite fraction of the mixed-corner budget; otherwise `Gamma_2 <= K I` already holds. The payment must retain the Han negative credit and the existing `Q/R` rebates.

A proof of this hybrid lemma would combine with the exact block lifetime telescope and Theorem 4.1 to give a dimension-independent FEI constant. The one-point family is **not** a counterexample to the hybrid statement; it is the motivating selector-heavy test case.

---

## 9. Claim ledger

### PROVED here

- `beta_ij=beta_ji` and its exact mixed `1-versus-3` face interpretation (1.4);
- exact adaptive-tree conservation of pivotal variation (2.1);
- the pivotal-isoperimetric erasure bound (3.2);
- the universal mixed-corner decomposition (4.5);
- the rebate-strengthened form (4.6), conditional only on the already-proved inherited debit/reserve identities at their stated scope;
- the exact sensitivity/checkerboard identity (5.2);
- the one-point obstruction `Gamma_2=(n-1)I` (6.3).

### COMPUTATIONAL SUPPORT

- exhaustive Boolean checks through `n=4` for the new local bound and fixed-order tree identity;
- exact one-point calibration through `n=8`.

### REFUTED / RETIRED

- `Gamma_2 <= K I` for a dimension-independent universal `K`.

### OPEN

- the corner-compression / block-selector lemma in Section 8;
- a dimension-independent universal bound from the combined corner, Han-credit, selector, and reserve banks;
- full uniform-cube Fourier entropy-influence.

**Full FEI remains OPEN / NOT PROVED.**
