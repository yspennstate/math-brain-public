# fleet01/B18 — tensor-centered orientation ledger from ratio-critical block total correlation

**Run:** `20260922T105415Z-centered-orientation-ledger`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub control/source retrieval was used; no native brain receiver/context was available.  
**Model self-report:** `GPT-5.6 Sol`. Configured reasoning effort and provider reasoning usage were not exposed.

## 0. Exact assignment and source state

The current all-team assignment asks for the exact replacement of raw hidden curvature after subtracting the cross-factor tensor baseline
\[
r_{ij}=q_iq_j,
\]
keeping signed covariance and proving which replacement is genuinely nonnegative under a realizable Boolean construction. Raw `U_4=O(J)` from terminality or qualitative tensor primitivity is explicitly prohibited.

The source inputs used here are:

1. **COPAIR_BARRIER**, `yspennstate/math-open-problems`, commit `85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`. It proves
   \[
   \kappa_{ij}=4r_{ij}=p_{ij}+4o_{ij},
   \qquad
   \omega_{i\leftarrow j}=p_{ij}-2c_{i\leftarrow j}+4o_{ij}=4r_{ij}-2c_{i\leftarrow j},
   \]
   and shows that for cross-factor pairs of an exact tensor, `r_ij=q_iq_j`, `p=c=0`, so raw hidden curvature contains a spurious tensor orientation baseline. It also gives a primitive all-block-terminal one-point-surgery family with `U_4/J -> infinity`, ruling out the raw shortcut.
2. **TERMINAL_CORE**, same repository/commit, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`. For a true minimum-dimensional `F/J` ratio core of ratio `rho`, every physical block `A` obeys
   \[
   \rho D_A\le \Delta_A F\le B_A-W_A,
   \quad
   D_A=\sum_{i\in A}q_i+C_A,
   \quad
   B_A=H(X_A\mid X_{A^c}),
   \quad
   W_A=\sum_{j\notin A}\mathfrak j'(q_j)c_j(A).
   \]
3. **CURVATURE**, `yspennstate/math-open-problems`, commit `200e3fd37fe201f78d882ba8809414d201efb829`, `proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`. It isolates the remaining hidden bank and proves the crossing-visible part is already paid by `P-DTC` on a true critical core.
4. **ROBUST_ROW**, `yspennstate/math-open-problems`, commit `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`. It converts a realizable robust derivative row into a terminal surplus demand and preserves the warning that the remaining weighted-depth bank is not automatically `O(J)`.

The newest compatible completed **partner** result consumed is fleet02/B18, corrected report at commit `1d39bc35fbb7ce60be36242c3bee6ea6bec55445`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T101659Z-c-admission-failure-logweight-redirect/REPORT.md`. Its `LOG-WEIGHT-NECESSITY-v1` theorem proves that every uniformly bounded self-adjoint quadratic compression of the complete Boolean convolution-defect vector is only `O(I)` on the sparse one-point-defect suspension, while the exact KL payment is of order `I log(1/p)`. I use this result below to keep the exact mutual-information/KL quantity as the primary centered currency; the quadratic covariance corollary is recorded only as a secondary consequence and is **not** promoted to a universal entropy replacement.

## 1. First attempted inference: direct subtraction inside the hidden remainder is false

Let
\[
X\subseteq[n],\qquad \Pr(X=S)=\widehat f(S)^2,
\]
be the spectral random set in the fixed median gauge, and write
\[
q_i=\Pr(i\in X),\qquad r_{ij}=\Pr(i,j\in X).
\]
The exact hidden remainder from COPAIR_BARRIER is
\[
\omega_{i\leftarrow j}=4r_{ij}-2c_{i\leftarrow j}\ge0.
\tag{1.1}
\]
The most literal tensor-centering would be
\[
\widetilde\omega_{i\leftarrow j}
:=\omega_{i\leftarrow j}-4q_iq_j
=4(r_{ij}-q_iq_j)-2c_{i\leftarrow j}.
\tag{1.2}
\]
This quantity is **not nonnegative**, even for a genuine two-bit Boolean function.

Take any non-affine two-bit Boolean function, e.g.
\[
f(0,0)=+1,\quad f(0,1)=-1,\quad f(1,0)=+1,\quad f(1,1)=+1.
\]
Every Walsh magnitude is `1/2`, so
\[
q_i=q_j=\frac12,\qquad r_{ij}=\frac14=q_iq_j.
\]
For either ordered singleton reveal, the surviving influence is `0` on one branch and `1` on the other, hence
\[
c_{i\leftarrow j}=c_{j\leftarrow i}=\frac12.
\]
Consequently
\[
\omega_{i\leftarrow j}=4\cdot\frac14-2\cdot\frac12=0,
\qquad
\boxed{\widetilde\omega_{i\leftarrow j}=-1.}
\tag{1.3}
\]
Thus the candidate statement

> `omega_{i<-j}-4q_iq_j >= 0` for every Boolean source

is refuted. This is a refutation of that intermediate tensor-centering rule, **not** a counterexample to FEI.

The exact signed object that remains after subtracting the tensor baseline is therefore the covariance
\[
\boxed{\delta_{ij}:=r_{ij}-q_iq_j=\operatorname{Cov}(1_{i\in X},1_{j\in X}).}
\tag{1.4}
\]
It genuinely has both signs and must not be replaced by `|delta_ij|` or `(delta_ij)_+` without a separate payment theorem.

## 2. Exact nonnegative replacement: the pair I-projection cost

For fixed `a=q_i`, `b=q_j`, the complete pair law is determined by `delta=delta_ij`:
\[
P_{11}=ab+\delta,
\quad P_{10}=a(1-b)-\delta,
\quad P_{01}=(1-a)b-\delta,
\quad P_{00}=(1-a)(1-b)+\delta.
\tag{2.1}
\]
Let
\[
\Psi_{a,b}(\delta)
:=D_{\mathrm{KL},2}(P_{ij}\Vert P_i\otimes P_j).
\]
Explicitly,
\[
\begin{aligned}
\Psi_{a,b}(\delta)
={}&(ab+\delta)\log_2\frac{ab+\delta}{ab}
+[a(1-b)-\delta]\log_2\frac{a(1-b)-\delta}{a(1-b)}\\
&+[(1-a)b-\delta]\log_2\frac{(1-a)b-\delta}{(1-a)b}
+[(1-a)(1-b)+\delta]\log_2\frac{(1-a)(1-b)+\delta}{(1-a)(1-b)},
\end{aligned}
\tag{2.2}
\]
with the usual limiting convention at boundary probabilities.

### Theorem 2.1 — exact tensor-centered pair currency

For every genuine Boolean spectral source,
\[
\boxed{
\Psi_{q_i,q_j}(\delta_{ij})
=I(X_i;X_j)\ge0.
}
\tag{2.3}
\]
For an exact tensor product and a cross-factor pair, `r_ij=q_iq_j`, hence `delta_ij=0` and
\[
I(X_i;X_j)=0.
\tag{2.4}
\]
Thus pair mutual information removes exactly the independence/tensor orientation baseline while retaining the actual sign of the covariance inside its source law. It is a source-valid nonnegative replacement, unlike (1.2).

The elementary Pinsker consequence is
\[
\boxed{
I(X_i;X_j)\ge \frac8{\ln2}\,\delta_{ij}^2,
}
\tag{2.5}
\]
because the total-variation distance between the pair law (2.1) and its product law is `2|delta_ij|`. Equation (2.5) is useful for selected-pair estimates only. By the consumed fleet02/B18 logarithmic-weight theorem, a uniformly bounded quadratic compression must not be mistaken for the full universal logarithmic entropy payment.

## 3. New ratio-critical block theorem: total correlation is physically budgeted

The assignment requires more than a nonnegative statistic: it must be paid under **true ratio-extremality**. The critical-core inequalities give exactly such a ledger.

Let `g` be a centered minimum-dimensional `F/J` ratio core with
\[
\rho:=\frac{F(g)}{J(g)}>4.
\]
For a nonempty physical block `A`, define its total correlation
\[
\operatorname{TC}(X_A)
:=\sum_{i\in A}h_2(q_i)-H(X_A)\ge0.
\tag{3.1}
\]

### Theorem 3.1 — critical block total-correlation ledger

Every physical block `A` of a true ratio-critical core satisfies
\[
\boxed{
\operatorname{TC}(X_A)
+\rho C_A+W_A
\le
\sum_{i\in A}\bigl[h_2(q_i)-\rho q_i\bigr].
}
\tag{3.2}
\]
Here `C_A` and `W_A` are exactly the physical posterior-crossing terms from TERMINAL_CORE; no correction is dropped or reused.

### Proof

Ratio-extremality gives the lower physical drift
\[
\rho D_A\le\Delta_A F.
\tag{3.3}
\]
The universal restriction theorem gives
\[
\Delta_A F\le B_A-W_A,
\qquad
B_A=H(X_A\mid X_{A^c}).
\tag{3.4}
\]
Since conditioning reduces entropy,
\[
B_A\le H(X_A)
=\sum_{i\in A}h_2(q_i)-\operatorname{TC}(X_A).
\tag{3.5}
\]
Finally
\[
D_A=\sum_{i\in A}q_i+C_A.
\tag{3.6}
\]
Substitute (3.5)--(3.6) into (3.3)--(3.4) and rearrange. QED.

This theorem is stronger than all-block `K=4` terminality: it uses the actual extremal ratio `rho` and preserves the nonnegative crossing correction.

## 4. New forest payment: a nonreusing tensor-centered orientation ledger

A matching is not the largest pair system that total correlation can pay. Any forest can be paid exactly once.

Let `T` be a forest on a subset `A` of the original physical coordinates. For each edge `{i,j}` write
\[
I_{ij}:=I(X_i;X_j)=\Psi_{q_i,q_j}(\delta_{ij}).
\]

### Lemma 4.1 — forest mutual information is below total correlation

For every joint law of `X_A` and every forest `T` on `A`,
\[
\boxed{
\sum_{\{i,j\}\in E(T)} I_{ij}
\le \operatorname{TC}(X_A).
}
\tag{4.1}
\]

### Proof

Root each tree component. The entropy chain rule and conditioning monotonicity give, component by component,
\[
H(X_{V})
\le H(X_r)+\sum_{v\ne r}H(X_v\mid X_{\mathrm{par}(v)}).
\]
Summing components and using entropy subadditivity across components,
\[
H(X_A)
\le\sum_{i\in A}H(X_i)
-\sum_{\{i,j\}\in E(T)}I(X_i;X_j).
\]
Rearrangement is (4.1). QED.

Combining Lemma 4.1 with Theorem 3.1 gives the central result of this run.

### Theorem 4.2 — ratio-critical tensor-centered forest ledger

For every physical block `A` and every forest `T` on `A`,
\[
\boxed{
\sum_{\{i,j\}\in E(T)}
I(X_i;X_j)
+\rho C_A+W_A
\le
\sum_{i\in A}\bigl[h_2(q_i)-\rho q_i\bigr].
}
\tag{4.2}
\]
In particular, because `rho>4`,
\[
\boxed{
\sum_{\{i,j\}\in E(T)}I(X_i;X_j)
+4C_A+W_A
\le
\sum_{i\in A}\bigl[h_2(q_i)-4q_i\bigr].
}
\tag{4.3}
\]
And the signed covariance consequence is
\[
\boxed{
\frac8{\ln2}\sum_{\{i,j\}\in E(T)}\delta_{ij}^2
+\rho C_A+W_A
\le
\sum_{i\in A}\bigl[h_2(q_i)-\rho q_i\bigr].
}
\tag{4.4}
\]

This is a genuine **nonreusing orientation selection theorem**: a forest may contain up to `|A|-1` physical pairs, pair dependence is charged once through an actual Shannon/KL total-correlation budget, and exact cross-factor tensor pairs cost zero. There is no coordinate relabeling, no affine selector, no absolute value of covariance, no raw `U_4` bound, and no assumption that qualitative primitivity creates a gap.

## 5. Relation to the hidden-curvature decomposition

COPAIR_BARRIER gives
\[
\omega_{i\leftarrow j}=4r_{ij}-2c_{i\leftarrow j}.
\]
Subtracting the tensor baseline yields the exact signed identity
\[
\boxed{
\omega_{i\leftarrow j}-4q_iq_j
=4\delta_{ij}-2c_{i\leftarrow j}.
}
\tag{5.1}
\]
Equation (1.3) proves that the left side has no universal sign. The correct ledger is therefore not a sum of centered hidden remainders. Instead:

* `delta_ij` is retained with its actual sign;
* `I(X_i;X_j)=Psi(delta_ij)` is the exact nonnegative cost of departing from the tensor baseline;
* on a true ratio-critical core, any **forest-selected** collection of those costs is paid by the same physical block surplus that also pays the posterior-crossing terms, via (4.2).

This directly addresses the tensor artifact responsible for the primitive-terminal `U_4/J` no-go. It does **not** assert that the entire complete-graph hidden bank is controlled.

## 6. Exact old and new missing implications

**Old missing implication.** Prove `U_4=O(J)` or otherwise pay the raw hidden bank on positive-defect all-block terminal cores. COPAIR_BARRIER refutes this from terminality plus qualitative tensor primitivity.

**New proved implication.** On a true ratio-critical core, every forest of tensor-centered pair dependencies satisfies the exact nonreusing KL ledger (4.2), and direct centering of `omega` is explicitly refuted by the two-bit Boolean example.

**New first unpaid implication.** Starting from the signed complete-graph quantities in (5.1), prove one of the following without absolute values or positive parts for free:

1. a realizable selection theorem showing that whenever the centered orientation contribution obstructs the Path-C compiler, some physical block and forest capture a fixed dimension-independent fraction of the required amount through the exact mutual-information terms in (4.2); or
2. a stronger block information identity that books the remaining cyclic complete-graph dependence into `TC(X_A)`, `C_A`, `W_A`, or another already-unspent physical entropy term.

A simple linear bound of `sum |delta_ij|` by the forest KL budget is not available near independence because mutual information is quadratic in small covariance. This is precisely where a threshold/multiscale selection or a nonquadratic source term is needed. The fleet02/B18 logarithmic-weight obstruction reinforces that this next step should retain exact KL rather than collapse the ledger to a bounded quadratic norm.

## 7. Status

**Classification:** `ESSENTIAL_STEP_APPLIED`.

The run supplies the exact tensor-centered variable, refutes the naive pointwise centered-hidden nonnegativity claim, identifies pair mutual information as the genuine nonnegative replacement, and proves a new ratio-critical forest payment with all physical crossing corrections retained.

**Full uniform-cube FEI remains OPEN / NOT PROVED.** The complete-graph-to-forest/block selection implication in Section 6 remains unpaid.
