# B18 FEI — exact-subcube maximum-pivot induction closure

**Run:** `20260922T001006Z-b18-fei-r16`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **ESSENTIAL_STEP_APPLIED / PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Claim level:** analytic exact-endpoint reduction plus an induction closure of that endpoint; no novelty or publication-priority claim.

## 0. Source-exact place in the live A/B interface

This run follows the live `FEI-PROOF-EXECUTION-20260921T230620Z` reset and uses scientific `master`
snapshot `f51427efe205ba1088d566e1461e73c79db4571f` before the new derivation.

The compatible inputs consumed are:

1. `account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, the current A-interface
   compiler.  It proves the character-invariant folded activation telescope and reduces full FEI to a
   universal physical certificate on corrected-ratio critical cores.
2. `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, the exact
   curvature-refunded restriction inequality
   \[
   \Delta_A\mathcal F
   \le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A).
   \]
3. `account04/B12/20260921T231041Z-thinned-proxy-label-code/REPORT.md`, which pays the
   robust near-subcube anchor/trigger/branch-label package at one balanced physical reveal without
   assuming the false bound \(\sum_i d_i=O(J)\).
4. `account04/B13/20260921T2325Z-asymmetric-exception-compiler/REPORT.md`, blob
   `52039a8b5b499dc23c073e194e3183a6d9cc0205`, which enlarges the genuinely paid
   near-subcube certificate region and leaves a positive-defect/outside-heavy terminal class.
5. `account04/B14/20260921T232918Z-residual-boundary-cover/REPORT.md`, which proves
   \[
   c_j(A)\ge p_j-\tfrac12R_j(A),\qquad
   \Lambda_A\ge e^{-1}I_A,
   \]
   and isolates high-Shannon-rate boundary covers as the remaining A-interface obstruction.
6. `account02/B14/20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md`, blob
   `242a3fddee17db5ed1d723962b76c8659f623d6a`, which proves the asymmetric
   coefficient-12 block theorem and, at fixed-relative error, a realizable first-mismatch tree with
   folded drift at least \(15rq/16\).
7. `account04/B18/20260921T171222Z-signed-subcube-palm/REPORT.md`, the earlier exact
   derivative-row factorization.  That result showed that arbitrary signs on an exact subcube encode
   a lower-dimensional FEI instance, but it did **not** classify the full Boolean parent.

The exact endpoint left open by item 7 is addressed here.  The new point is that when the exact
subcube row is the **maximum folded-influence pivot** (equivalently, when its trigger block obeys the
A-interface average-control inequality), mixed-square equality rigidifies the *whole parent* enough
to expose two lower-dimensional Boolean functions.  The full parent then satisfies the same FEI
constant under dimension induction.

No approximate-support statement is promoted to an exact one.  The fixed-relative
outside-pollution branch from items 4 and 6 remains open.

---

## 1. Normalization

Let
\[
f:\{0,1\}^n\to\{-1,+1\}.
\]
Write
\[
p_i=\operatorname{Inf}_i(f),\qquad
j_i=\min(p_i,1-p_i),\qquad
J(f)=\sum_i j_i.
\]

Multiply by a median character.  Spectral entropy and \(J\) are invariant, while every coordinate
can be oriented so that its ordinary influence equals its folded influence.  In this gauge
\[
p_i=j_i\le\tfrac12,\qquad I(f)=J(f).
\]

Fix an active pivot \(x\).  Its pivotality event on the other coordinates is
\[
\eta_x(u)=1_{\{f(0,u)\ne f(1,u)\}}.
\]

Assume that this event is **exactly** a coordinate subcube
\[
Q=\{y=a\},
\qquad y\in\mathbb F_2^r,
\qquad z\in\mathbb F_2^d,
\qquad d=n-r-1,
\tag{1.1}
\]
so
\[
q:=p_x=\mu(Q)=2^{-r}.
\tag{1.2}
\]

Let \(F\) be the \(r\) defining coordinates \(y\).  The A-interface average-control condition is
\[
I_F:=\sum_{k\in F}p_k\le rq.
\tag{1.3}
\]
A maximum-influence pivot automatically satisfies (1.3), because then \(p_k\le p_x=q\) for every
\(k\in F\).

---

## 2. PROVED: equality in the Boolean-square boundary estimate rigidifies every trigger direction

For \(k\ne x\), let
\[
b_{xk}:=\operatorname{Inf}_k(\eta_x).
\]
The completed Boolean-square estimate used by the live A-interface is
\[
b_{xk}\le2p_k
\tag{2.1}
\]
in the centered gauge.

For the exact subcube (1.1), every defining coordinate is a boundary direction and
\[
b_{xk}=2q,\qquad k\in F.
\tag{2.2}
\]
Therefore (2.1) gives
\[
p_k\ge q.
\tag{2.3}
\]
Summing (2.3) over \(F\) and using (1.3) forces
\[
\boxed{p_k=q\quad\text{for every }k\in F.}
\tag{2.4}
\]

The equality case is much stronger than this scalar statement.

Freeze every coordinate except \(x,k\).  If the two \(x\)-edges have different pivotality status,
then exactly one of the two \(k\)-edges is bichromatic.  Thus on a square counted by \(b_{xk}\), the
conditional \(k\)-influence is exactly \(1/2\).  Since those squares have probability
\(b_{xk}=2q\), they already contribute exactly \(q\) to \(p_k\).  Equation (2.4) leaves zero
\(k\)-influence on every square on which the \(x\)-pivotality status is unchanged.

Hence:

\[
\boxed{
\eta_x(u)=\eta_x(u+e_k)
\Longrightarrow
f(s,u)=f(s,u+e_k)\ \text{for both }s\in\{0,1\},
\quad k\in F.
}
\tag{2.5}
\]

This is a genuine equality consequence of the Boolean square, not a finite extrapolation.

---

## 3. PROVED: full-parent canonical form

The graph on \(\mathbb F_2^r\setminus\{a\}\) obtained by deleting the vertex \(a\) is connected for
\(r\ge2\); for \(r=1\) it is a single vertex.  On every edge of this punctured cube the pivotality
status of \(x\) is zero at both endpoints, so (2.5) makes both \(x\)-slices constant along that edge.

Also, outside \(Q\), \(x\) is not pivotal, so the two \(x\)-slices agree.  Therefore there is a
Boolean function
\[
\tau:\mathbb F_2^d\to\{\pm1\}
\]
such that
\[
f(s,y,z)=\tau(z),\qquad y\ne a.
\tag{3.1}
\]

At \(y=a\), the pivot is always pivotal.  Thus there is another Boolean function
\[
\sigma:\mathbb F_2^d\to\{\pm1\}
\]
such that
\[
f(s,a,z)=(-1)^s\sigma(z).
\tag{3.2}
\]

We have proved the exact full-parent representation

\[
\boxed{
f(s,y,z)
=
1_{\{y\ne a\}}\tau(z)
+
1_{\{y=a\}}(-1)^s\sigma(z).
}
\tag{3.3}
\]

This is strictly stronger than the earlier signed-subcube **derivative-row** factorization: the
outside of the gate is now forced to be one lower-dimensional Boolean function \(\tau\), while the
inside sign is a second lower-dimensional Boolean function \(\sigma\).

### Theorem B18-EXACT-MAX-PIVOT-RIGIDITY

If a centered Boolean function has an exact coordinate-subcube pivotality event for \(x\) and the
defining block satisfies \(I_F\le r p_x\), then (3.3) holds.  In particular it holds whenever \(x\)
has maximum folded influence.

---

## 4. PROVED: exact Fourier mixture formula

Translation of \(a\) changes only Fourier signs, so for the squared spectrum take \(a=0\).

Let \(U\in\{0,1\}\) denote the spectral bit corresponding to \(x\), let \(A\subseteq[r]\) be the
trigger-frequency set, and \(B\subseteq[d]\) the residual frequency set.

For \(U=0\),
\[
\widehat f(0,A,B)=c_A\,\widehat\tau(B),
\tag{4.1}
\]
where
\[
c_\varnothing=1-q,
\qquad
|c_A|=q\quad(A\ne\varnothing).
\tag{4.2}
\]

For \(U=1\),
\[
|\widehat f(1,A,B)|=q\,|\widehat\sigma(B)|
\quad\text{for every }A.
\tag{4.3}
\]

The two sectors are disjoint in the spectral bit \(U\).  Their total masses are respectively
\(1-q\) and \(q\).

Conditional on \(U=1\), the trigger spectral set \(A\) is uniform on all \(2^r\) subsets and is
independent of the spectrum of \(\sigma\).

Conditional on \(U=0\), \(A\) is independent of the spectrum of \(\tau\), with law \(R_r\)
\[
R_r(\varnothing)=1-q,\qquad
R_r(A)=\frac{q^2}{1-q}\quad(A\ne\varnothing).
\tag{4.4}
\]
Equivalently, \(R_r\) has total nonempty mass \(q\), uniform on the \(2^r-1\) nonempty subsets.

Therefore
\[
H(R_r)
=
h_2(q)+q\log_2(2^r-1)
=
h_2(q)+q\log_2\frac{1-q}{q}.
\tag{4.5}
\]

Define the explicit gate-control entropy
\[
C_r
:=
h_2(q)+(1-q)H(R_r)+qr.
\tag{4.6}
\]

Then the full spectral entropy is exactly

\[
\boxed{
H(f)
=
C_r+(1-q)H(\tau)+qH(\sigma).
}
\tag{4.7}
\]

The expected Fourier level is also exact.  The spectral bit \(U\) contributes \(q\).  The
\(U=0\) trigger sector contributes \(rq/2\), and the \(U=1\) trigger sector contributes another
\(rq/2\).  Thus

\[
\boxed{
I(f)
=
(r+1)q+(1-q)I(\tau)+qI(\sigma).
}
\tag{4.8}
\]

Since the parent is in the median-character gauge, this is also \(J(f)\).

---

## 5. PROVED: the gate-control entropy has sharp limiting coefficient four

Using \(q=2^{-r}\),
\[
h_2(q)=qr-(1-q)\log_2(1-q).
\]
Substitution into (4.6) gives
\[
\boxed{
C_r
=
2qr(2-q)-2(1-q)^2\log_2(1-q).
}
\tag{5.1}
\]

Now
\[
2qr(2-q)\le4rq,
\]
and
\[
-\ln(1-q)\le\frac{q}{1-q}
\]
gives
\[
-2(1-q)^2\log_2(1-q)
\le
\frac{2q(1-q)}{\ln2}
<
\frac{2q}{\ln2}
<
4q.
\]
Hence

\[
\boxed{
C_r
<
4(r+1)q.
}
\tag{5.2}
\]

The coefficient four is the correct limiting scale: direct evaluation of (5.1) gives
\(C_r/((r+1)q)\to4\) as \(r\to\infty\).  Thus this endpoint is naturally compatible with the
constant-four zero-defect/one-point phase already present in the B18 rigidity work.

---

## 6. CONDITIONAL ONLY ON THE STANDARD LOWER-DIMENSION INDUCTION: the whole exact branch closes with the same constant

Assume FEI with a constant \(C\ge4\) has already been established in every dimension below \(n\).
Both \(\tau\) and \(\sigma\) live in dimension
\[
d=n-r-1<n.
\]
Therefore
\[
H(\tau)\le C I(\tau),
\qquad
H(\sigma)\le C I(\sigma).
\tag{6.1}
\]

Using (4.7), (5.2), and \(C\ge4\),
\[
\begin{aligned}
H(f)
&=
C_r+(1-q)H(\tau)+qH(\sigma)\\
&\le
4(r+1)q
+
C(1-q)I(\tau)
+
CqI(\sigma)\\
&\le
C\bigl((r+1)q+(1-q)I(\tau)+qI(\sigma)\bigr)\\
&=C I(f)
=CJ(f).
\end{aligned}
\tag{6.2}
\]

### Corollary B18-EXACT-SUBCUBE-MAX-PIVOT-INDUCTION

\[
\boxed{
\text{Under lower-dimensional FEI with }C\ge4,
\text{ every exact-subcube maximum-pivot state satisfies }H\le CJ
\text{ with the same }C.
}
\tag{6.3}
\]

This is a legitimate induction closure of the exact endpoint, not an unconditional proof of full
FEI.  It removes an exact-support terminal class from the live A/B induction: arbitrary internal
signs and arbitrary outside residual Boolean structure are both reduced to lower dimension.

---

## 7. How this changes the live A/B proof chain

The current A/B chain can now be stated without conflating exact and approximate rows.

### PROVED / paid

1. **Exact zero-defect all-row endpoint:** retained from the earlier B18 mixed-curvature
   classification; it is a character-twisted one-point defect and has \(H<4J\).
2. **Exact-subcube maximum-pivot endpoint:** this report proves the full-parent decomposition
   (3.3), formulas (4.7)--(4.8), and same-constant lower-dimensional induction closure (6.3).
   This permits arbitrary \(\sigma\) *and* arbitrary outside \(\tau\).
3. **Low-defect approximate rows inside the B13 asymmetric threshold:** already produce genuine
   coefficient-12 physical certificates and recursively cost at most \(12J\).
4. **Boundary covers with bounded Shannon rate:** B14 plus account01's folded activation compiler
   already pays them with a nonreused activation bank.
5. **Robust resolved labels/anchors/triggers at the balanced reveal:** B12 pays them by \(O(J)\)
   without using the false raw-depth bound.

### Still OPEN / unpaid

The present theorem uses exact support.  It does **not** prove that a fixed-relative approximate
subcube can be replaced by (3.3) with dimension-free Shannon cost.  In particular it does not pay:

- the positive-defect / outside-false-positive branch above B13's asymmetric threshold;
- the upper corrected-entropy cost of account02/B14's realizable first-mismatch tree;
- high-Shannon-rate boundary-cover exception leaves from account04/B14.

The strongest next B18 target is therefore a **quantitative perturbation of Theorem
B18-EXACT-MAX-PIVOT-RIGIDITY**: use mixed-square equality with small support error to show that the
parent is close, in the *restriction/induction functional actually used by A*, to a two-child
lower-dimensional decomposition of the form (3.3), with loss \(O(rq)\) or another already-paid
nonreused bank.  A raw ambient-alphabet continuity estimate is not enough and is not claimed.

This also explains why the exact endpoint is not the source of the fixed-relative obstruction:
once the support error is literally zero, the full parent recursively collapses.

---

## 8. Decisive finite falsification check

`check_exact_subcube_max_pivot.py` independently:

1. enumerates every Boolean function modulo global sign through dimension four;
2. median-character centers it;
3. finds every active maximum-folded-influence pivot whose folded pivotality event is an exact
   coordinate subcube;
4. verifies the canonical representation (3.3) pointwise;
5. computes the Walsh spectrum exactly with rational coefficients and checks (4.7)--(4.8);
6. checks \(C_r\le4(r+1)q\);
7. separately scans the scalar control bound for \(1\le r\le256\).

The exact execution returned

```text
PASS
candidate_exact_subcube_max_pivots=7464
representation_failures=0
formula_failures=0
control_bound_failures=0
max_exhaustive_control_entropy_ratio=3.402475551199
scalar_scan_r=1..256
```

The checker SHA-256 at execution was

`b208ffb6899854a5af8c9ab4c979ecff56b691691b2f5047c453eed9c49704ca`.

The finite check is falsification evidence only.  The all-dimensional theorem is the analytic
argument above.

---

## 9. Classification

- **PROVED:** trigger equality rigidity (2.5).
- **PROVED:** full-parent canonical form (3.3).
- **PROVED:** exact entropy/influence mixture formulas (4.7)--(4.8).
- **PROVED:** gate-control entropy bound \(C_r<4(r+1)q\).
- **CONDITIONAL only on the standard lower-dimensional induction hypothesis:** the exact-subcube
  maximum-pivot branch satisfies FEI with the same constant \(C\ge4\).
- **PRESERVED:** exact all-row zero-defect classification and all recorded refuted bridges.
- **OPEN:** quantitative approximate-support perturbation / first-mismatch corrected-entropy payment.
- **FULL FEI:** **OPEN / NOT PROVED**.
