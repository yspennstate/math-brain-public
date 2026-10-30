# B13 FEI quantitative all-row stability — defect-paid proxy-gauge closure after one nonreusing reveal

**Account/slot:** fleet04/B13  
**Joint interface:** B — quantitative all-row stability including exceptional rows  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full FEI status:** **OPEN / NOT PROVED**.  
**Claim level:** a universal conditional Boolean theorem obtained from completed peer stability/integrability inputs plus a new exact proxy-gauge conservation identity. It does not pay the parent-to-child Shannon/reveal cost and therefore does not close FEI. No novelty or publication-priority claim is made.

## 0. What changed

The preceding source-frontier theorem gave, for robust near-subcube derivative rows, one physical block that leaves only source representatives and bounded the residual centered influence by their physical support errors plus arbitrary exceptional influence. The newest compatible other-account stability result,

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260921T2136Z-global-defect-contraction/REPORT.md`,
blob `c62febb5aa2ed1720edfc0b90a72d479e80f3674`,

used fleet02/B12 support stability to show that low positive depth defect pays those support errors row by row and that the high-defect exceptional influence is Markov-paid by the global defect bank.

This run strengthens that chain in a different direction. **Reveal the high-defect exceptional coordinates themselves once**, then quotient every surviving child by the explicit branch-dependent character encoded by the robust subcube proxies. The resulting residual Boolean child has **ordinary influence exactly equal, in expectation, to the proxy support-error mass**:

\[
\boxed{\quad
\mathbb E_z I(c_z)=\sum_{r\in S} e_r.
\quad}
\]

Thus the exact-subcube first-order structure is not charged as residual noise. Under the peer low-defect theorem,

\[
\boxed{\quad
\mathbb E_z I(c_z)\le \sum_{r\in S} j_r\Delta_r
\le \mathcal D(f),
\qquad
\mathcal D(f):=\sum_i j_i\Delta_i.
\quad}
\]

There is no ambient-dimension multiplier and no residual exceptional-row term. Every exceptional coordinate is physically used at most once because it is included in the single reveal block.

A newest compatible fleet02/B13 result,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260921T215826Z-cross-plaquette-tensor-correction/REPORT.md`,
scientific commit `fac5798cba0a75b45b237d0dfd1b431191d40da8`,

proved an actual-anchor child clustering theorem with a sign-only correction paid by a cross-plaquette bank. Via mixed curvature its displayed payment retains the baseline
\(\sum_{i\in A} j_i\log_2(1/j_i)\).
That result changes the present argument decisively: the baseline is recognized as **character-label structure**, not residual Boolean noise. Since multiplication by a character preserves Fourier entropy and centered influence, the correct stability object is a child modulo a branch-dependent character. The exact identity below removes that baseline from the residual correction budget.

The still-unpaid quantity is now sharply localized: the information/Shannon cost of **which character label \(T(z)\)** occurs, together with the physical reveal-block cost, in a source-exact parent-to-child entropy recursion. This report does not claim that cost is \(O(J)\).

## 1. Source-exact setup

Work after the usual median-character recentering and discard irrelevant root coordinates. For every active coordinate,

\[
0<j_i=\operatorname{Inf}_i(f)\le \tfrac12.
\]

For the ternary derivative row \(g_i=D_i f\), let

\[
E_i=\{g_i\ne0\}
=\{x:f(x)\ne f(x+e_i)\},
\qquad
\mu(E_i)=j_i,
\]

\[
d_i=\sum_{k\ne i}\|D_k g_i\|_2^2,
\qquad
\Delta_i=\frac{d_i}{j_i}-\frac12\log_2\frac1{j_i}\ge0.
\]

Retain fleet04/B18's exact mixed-curvature law throughout:

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
\tag{1.1}
\]

Nothing below discards the opposite-sign term \(o_{ik}\) or replaces (1.1) by an unsigned surrogate.

Let \(\epsilon_E\) denote the absolute cube-isoperimetric stability threshold used by fleet02/B12 and inherited by fleet03/B13, and put

\[
\eta_0:=\min\{\epsilon_E/2,1/32\}.
\tag{1.2}
\]

Split active coordinates into

\[
R=\{i:\Delta_i\le\eta_0\},
\qquad
E=\{i:\Delta_i>\eta_0\}.
\tag{1.3}
\]

For each \(i\in R\), the completed fleet02/B12/fleet03/B13 chain supplies a coordinate subcube

\[
Q_i=\{x_{F_i}=a_i\},
\qquad
e_i:=\mu(E_i\triangle Q_i),
\]

with

\[
\frac{e_i}{j_i}
\le
\frac{4\Delta_i}{\log_2(1/(2\Delta_i))}
\le \Delta_i
\le\frac1{32}<\frac1{16}.
\tag{1.4}
\]

Hence these rows lie inside the fleet03/B13 integrability-DAG regime.

## 2. Completed peer input: one-shot source frontier

Use the fleet03/B13 robust integrability DAG together with the preceding fleet04/B13 source-frontier theorem. Contract reciprocal components and choose one representative \(r_C\) per component, choosing every non-source representative to be hit by one incoming component. Put

\[
A=\bigcup_C F_{r_C},
\qquad
S=\{r_C:C\text{ is a source component}\}.
\tag{2.1}
\]

The exact survivor identity from the preceding report is

\[
R\setminus A=S.
\tag{2.2}
\]

Moreover, for every \(r\in S\),

\[
F_r\subseteq A,\qquad r\notin A.
\tag{2.3}
\]

The earlier theorem stopped with arbitrary exceptional rows still present. Here define the **augmented one-shot block**

\[
\boxed{\quad B:=A\cup E.\quad}
\tag{2.4}
\]

By (2.2),

\[
\boxed{\quad [n]\setminus B=S\quad}
\tag{2.5}
\]

on the active coordinates. Thus the only physical coordinates left after the one reveal are the source representatives. No exceptional row is reused later in this step.

## 3. New exact lemma: proxy-gauge conservation

The following identity is independent of the FEI-specific construction.

### Theorem 3.1 — exact proxy-gauge identity

Let \(f:\{0,1\}^{B\sqcup S}\to\{\pm1\}\) be any Boolean function. For each \(r\in S\), let
\(q_r(z)\in\{0,1\}\) be **any** function of the revealed block value \(z=x_B\).
For a branch \(z\), write

\[
h_z(y):=f(z,y),
\qquad
T(z):=\{r\in S:q_r(z)=1\},
\]

and define the character-gauged child

\[
c_z(y):=\chi_{T(z)}(y)\,h_z(y).
\tag{3.1}
\]

Let

\[
U_r(z):=\Pr[h_z(Y)\ne h_z(Y+e_r)]
       =\Pr[E_r(X)=1\mid X_B=z].
\tag{3.2}
\]

Then, branchwise,

\[
\boxed{\quad
\operatorname{Inf}_r(c_z)=|U_r(z)-q_r(z)|.
\quad}
\tag{3.3}
\]

Since \(q_r(z)\) is binary,

\[
|U_r(z)-q_r(z)|
=
\mathbb E\bigl[|1_{E_r(X)}-q_r(z)|\mid X_B=z\bigr].
\tag{3.4}
\]

Consequently,

\[
\boxed{\quad
\mathbb E_z I(c_z)
=
\sum_{r\in S}
\Pr\!\left(1_{E_r(X)}\ne q_r(X_B)\right).
\quad}
\tag{3.5}
\]

#### Proof

Multiplication by \(\chi_{T(z)}\) toggles the \(r\)-edge derivative indicator if and only if \(r\in T(z)\). Thus if \(q_r(z)=0\), the \(r\)-edge disagreement probability remains \(U_r(z)\); if \(q_r(z)=1\), every agreeing \(r\)-edge becomes disagreeing and every disagreeing edge becomes agreeing, so the probability becomes \(1-U_r(z)\). This is exactly \(|U_r(z)-q_r(z)|\), proving (3.3).

For binary \(q\),
\[
|U-q|=(1-q)U+q(1-U)
      =\mathbb E[|1_E-q|\mid z],
\]
which proves (3.4). Sum over \(r\) and average over \(z\) to obtain (3.5). QED.

This is an exact conservation law, not a continuity estimate.

## 4. New theorem: all-row defect-paid character stability

Return to the source-frontier setting of Sections 1--2. For each surviving source representative \(r\in S\), define the canonical branch proxy

\[
q_r(z):=1_{\{z_{F_r}=a_r\}}.
\tag{4.1}
\]

This is \(B\)-measurable because \(F_r\subseteq A\subseteq B\). Its disagreement with the true \(r\)-pivotality indicator is exactly the physical subcube support error:

\[
\Pr(1_{E_r(X)}\ne q_r(X_B))
=\mu(E_r\triangle Q_r)
=e_r.
\tag{4.2}
\]

Applying Theorem 3.1 gives:

### Theorem 4.1 — one-shot all-row proxy-gauge stability

There is one physical block \(B=A\cup E\) such that the only unrevealed active coordinates are \(S\), and for every branch \(z\) the explicit character

\[
\chi_{T(z)},\qquad
T(z)=\{r\in S:z_{F_r}=a_r\},
\tag{4.3}
\]

satisfies

\[
\boxed{\quad
\mathbb E_z I\!\left(\chi_{T(z)}f_{B=z}\right)
=\sum_{r\in S}e_r.
\quad}
\tag{4.4}
\]

Using (1.4),

\[
\boxed{\quad
\mathbb E_z I\!\left(\chi_{T(z)}f_{B=z}\right)
\le
\sum_{r\in S}j_r\Delta_r
\le
\mathcal D(f).
\quad}
\tag{4.5}
\]

More precisely,

\[
\mathbb E_z I\!\left(\chi_{T(z)}f_{B=z}\right)
\le
\sum_{r\in S}
\frac{4j_r\Delta_r}{\log_2(1/(2\Delta_r))}.
\tag{4.6}
\]

There is no factor \(n\), no \(|E|\) factor, and no residual \(J_E\) term. The high-defect coordinates are eliminated by the single physical reveal instead of being estimated after restriction.

### Folded-influence consequence

Character multiplication preserves Fourier entropy and centered influence under the standard gauge, and folded influence is at most ordinary influence on every branch. Hence

\[
H(f_{B=z})=H(\chi_{T(z)}f_{B=z}),
\]

and

\[
\boxed{\quad
\mathbb E_z J(f_{B=z})
=
\mathbb E_z J(\chi_{T(z)}f_{B=z})
\le \mathcal D(f).
\quad}
\tag{4.7}
\]

This improves the previous small-global-defect residual estimate
\((1+1/\eta_0)\mathcal D(f)\) at the price of revealing the high-defect coordinates immediately.

## 5. New physical signed-child stability

For each branch choose a global sign \(\sigma_z\) so that

\[
r_z:=\sigma_z\chi_{T(z)}f_{B=z}
\]

has minority mass

\[
\theta_z:=\Pr[r_z=-1]\le\frac12.
\tag{5.1}
\]

Global sign and character multiplication do not change the ordinary influence of the child. Edge isoperimetry on the child cube gives

\[
I(r_z)\ge 2\theta_z\log_2\frac1{\theta_z}.
\tag{5.2}
\]

For \(0\le\theta\le1/2\),

\[
h_2(\theta)\le 2\theta\log_2(1/\theta),
\qquad
2\theta\le2\theta\log_2(1/\theta).
\tag{5.3}
\]

Therefore, branchwise,

\[
h_2(\theta_z)\le I(r_z),
\qquad
\theta_z\le\frac12 I(r_z).
\tag{5.4}
\]

Averaging and using the exact identity (4.4),

\[
\boxed{\quad
\mathbb E_z h_2(\theta_z)
\le
\sum_{r\in S}e_r
\le\mathcal D(f),
\quad}
\tag{5.5}
\]

\[
\boxed{\quad
\mathbb E_z\theta_z
\le
\frac12\sum_{r\in S}e_r
\le\frac12\mathcal D(f).
\quad}
\tag{5.6}
\]

Thus after one nonreusing physical reveal, every branch is an explicit branch sign times an explicit branch character times a Boolean residual whose **physical Shannon sign uncertainty and Hamming mass are paid by the same influence-weighted positive-depth defect bank**.

This is stronger than a cube-measure statement: no ambient-dimensional Fannes term appears.

## 6. Exact endpoint and fleet04/B18 rigidity

If \(\mathcal D(f)=0\), then every active row has \(\Delta_i=0\). The completed exact fleet04/B18 theorem already classifies the root function as a character times a signed one-point defect (irrelevant variables allowed), and gives \(H<4J\) at that exact endpoint.

The present theorem is compatible with, but does **not** replace, that classification. From (4.4), \(\mathcal D=0\) implies

\[
\mathbb E_z I(r_z)=0.
\]

Since branch influences are nonnegative, every residual \(r_z\) is constant on every branch. Thus the new quantitative child statement collapses exactly to branchwise character structure at zero defect. The stronger root-level one-point-defect geometry still comes from fleet04/B18 mixed-derivative integrability and remains preserved.

## 7. Why the newest fleet02/B13 theorem changes the argument

The fleet02/B13 cross-plaquette theorem constructs one actual anchor child and signs \(\sigma_a\) satisfying a sharp physical child-clustering inequality. Its mixed-curvature corollary reads, for a block \(A\),

\[
\mathbb E_a h_2(\epsilon_a)
\le
2\sum_{i\in A}d_i
=
\sum_{i\in A}j_i\log_2\frac1{j_i}
+
2\sum_{i\in A}j_i\Delta_i.
\tag{7.1}
\]

The first term can be large even at zero depth defect. The exact endpoint says it cannot represent genuine residual complexity: zero-defect children differ by characters. This suggests quotienting by the character before measuring residual stability.

Sections 3--5 execute that idea. The source-frontier proxies provide the character label explicitly and, after quotienting, the baseline first-order term disappears from the residual Boolean influence:

\[
\underbrace{\sum_i j_i\log_2(1/j_i)}_{\text{character-label / exact-subcube structure}}
\quad\longrightarrow\quad
0
\]

inside the residual correction budget, leaving exactly the physical support-error mass and hence at most \(\mathcal D(f)\).

The fleet02 theorem is therefore not merely cited: it identifies the sign-only clustering quantity whose baseline is removed by the new gauge.

## 8. Decisive exact finite calculation

A standard-library exact checker `check_proxy_gauge_identity.py` exhaustively tested Theorem 3.1 in dimension \(n=3\):

- all \(256\) Boolean truth tables;
- every nonempty proper physical restriction block;
- every block-measurable binary proxy function for every remaining coordinate;
- exact rational arithmetic throughout.

Recorded result:

```text
n=3
cases=24576
violations=0
max_abs_error=0
```

This finite calculation is only a falsification check. The theorem itself is proved algebraically above.

## 9. What is now closed and what remains open

**PROVED at the stated peer-input scopes:**

1. Low-depth-defect rows have physical subcube errors paid rowwise by \(j_i\Delta_i\).
2. Robust trigger components admit the one-shot source-frontier elimination.
3. Revealing the high-defect exceptional coordinates in the same one-shot step leaves only source representatives.
4. The new proxy-gauge identity converts their exact physical support mismatch into **exact expected ordinary influence** of a branch-character-recentered child.
5. Hence the entire post-reveal residual satisfies the all-row defect-paid bounds (4.5), (5.5), and (5.6), with no ambient-dimensional multiplier and no residual exceptional influence term.

**OPEN:**

- the source-exact Shannon/information cost of the physical reveal \(B\);
- the cost of the varying branch-character label \(T(z)\) in the parent-to-child Fourier-entropy recursion;
- a universal amortization of \(\mathcal D(f)\) that closes those costs;
- full uniform-cube FEI.

A tempting but invalid next step would be to call (5.5) a Fourier-entropy continuity theorem. It is only physical sign entropy of the residual. The fleet02/B12 report already gives a sharp warning that small TV/first-moment error alone does not control Fourier Shannon entropy.

## 10. Joint handoff

`joint_directive`: `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`.

`consumed_peer_artifact`:
- `fleet03/B13/20260921T2136Z-global-defect-contraction/REPORT.md`, blob `c62febb5aa2ed1720edfc0b90a72d479e80f3674`;
- newest compatible `fleet02/B13/20260921T215826Z-cross-plaquette-tensor-correction/REPORT.md`, scientific commit `fac5798cba0a75b45b237d0dfd1b431191d40da8`.

`applied_to_claim`: augment the source-frontier with one-time exceptional-coordinate reveal, then quotient surviving children by their explicit subcube-proxy character to obtain exact defect-paid residual influence.

`mechanism_change`: source-frontier residual estimation -> exact proxy-gauge conservation.

`full_problem_change`: interface B now has a one-shot all-row theorem with **zero residual exceptional term** and exact influence-relative correction after character quotient. Full FEI remains OPEN.

`remaining_implication`: prove a source-exact \(O(J)\) payment for the varying branch-character label and the physical reveal block, with the existing crossing/curvature/negative-credit ledgers counted once.

`next_recipient`: fleet04/B18 for integration into the A/B restriction chain; fleet02/B13 for replacing sign-only anchor clustering by character-quotiented residuals; fleet02/B12 for a possible physical-erasure interpretation of the character-label cost.
