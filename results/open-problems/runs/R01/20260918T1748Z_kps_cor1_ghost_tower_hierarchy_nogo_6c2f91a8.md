Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT in the active source metric: `W_AS: 1 -> 1`; frozen I0024 remains `C=1`; status `OPEN / PARTIAL`; methods #11 DUALIZE, #19 MAKE IT AN ALGORITHM, #30 ONE SCALE/ONE DIRECTION AT A TIME.**

# R01 — Nielsen Corollary 1: ghost-tower duality and a no-go theorem for countable ultrafilter hierarchies

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime truth and repository continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or a guaranteed hour-long execution.

I continued from, rather than restarting before,

`runs/R01/20260918T1623Z_kps_cor1_claim_operator_diagonal_3a71c5e9.md`.

Before doing new mathematics I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the operative implementation record `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the exclusive claim `operations/claims/KPS-2026-NIELSEN-COR1.md`, current KPS ownership deltas, and the neighboring same-source R06 report

`runs/R06/20260918T1635Z_nielsen_t4_admission_structure_45.md`.

The R01 Corollary-1 claim remains exclusively owned by R01. R06 owns the distinct Nielsen-Theorem-4 question. I did not edit a shared ledger, another track's file, or any scheduler state.

## 2. I0024 remains frozen and is not reopened

Aldous--Fill Open Problem 3.44 remains internally complete at the exact distortion optimum

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with `C=1` and the preserved distinct audits

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`,
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

No work below changes or reopens that result.

## 3. Active source and recovered normal form

The active target is the question explicitly left open by M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1, submitted 17 September 2026:

> Do the approximation property and CHT together imply almost-sure convergence to the truth for an arbitrary probability function?

The direct arXiv source still records this as open in Section 10. Its Section 4 also isolates the valid weaker quantifier statement and explains that finite additivity blocks the countable-union diagonalization. The paper's Section 6 proves the claim only in its one-ultrafilter family.

I retain the metric from the preceding R01 run. For exact source-admissible `P,A`,

\[
F_A:=\{\omega:P_n(A)(\omega)\not\to\mathbf1_A(\omega)\},
\quad
\Gamma_{\rm AS}:=\sup_{P,A}P(F_A),
\]

and `W_AS=U_AS-L_AS` for a certified interval on `Gamma_AS`. The current interval remains `[0,1]`, hence

\[
\boxed{W_{\rm AS}=1.}
\]

From the preceding R01 run, every source-admissible `P` has a unique countably additive companion `R=P` on clopens, and approximation yields a Boolean-algebra homomorphism

\[
\Phi:\mathcal B\longrightarrow\mathcal B/\!\sim_R
\]

fixing clopens such that, with `B=Phi(A)` represented by a Borel event,

\[
P(A)=R(B),\qquad
P_n(A)=E_R[\mathbf1_B\mid\mathscr F_n].
\]

CHT is exactly the fixed-point condition on the corresponding posterior first-hitting opens. Also, the valid quantifier estimate in the source already gave the preceding R01 result

\[
P\!\left(\left\{\limsup_n|P_n(A)-\mathbf1_A|>r\right\}\right)=0
\qquad(r>0).
\tag{3.1}
\]

The work below starts from these recovered facts.

## 4. Method #11 — DUALIZE: every counterexample contains a positive-mass ghost tower

The previous report said that a counterexample must be diagonal. The following makes that obstruction exact and operator-valued.

### Theorem 4.1 (ghost-tower necessity)

Fix a source-admissible `P` and event `A`. Put

\[
e_n(\omega)=|P_n(A)(\omega)-\mathbf1_A(\omega)|,
\qquad
F=\{e_n\not\to0\}.
\]

For `m>=1` define

\[
E_m=\{\limsup_n e_n>1/m\},
\qquad
G_m=F\setminus E_m.
\]

If `gamma=P(F)>0`, then

\[
G_1\supseteq G_2\supseteq\cdots,
\qquad
\bigcap_{m\ge1}G_m=\varnothing,
\qquad
P(G_m)=\gamma\quad\text{for every }m.
\tag{4.1}
\]

Moreover, in the companion representation,

\[
R(\Phi(E_m))=0,
\qquad
\Phi(G_m)=\Phi(F)\quad(R\text{-a.e.})
\tag{4.2}
\]

for every `m`, and

\[
R(\Phi(F))=\gamma.
\tag{4.3}
\]

Thus a source counterexample is not merely a countable union of null threshold failures. It produces a decreasing sequence of nonempty Borel events with **empty set-theoretic intersection but identical positive image under `Phi`**.

### Proof

By (3.1), `P(E_m)=0` for every `m`. The sets `E_m` increase with `m`, because the threshold `1/m` decreases. Since `e_n` is nonnegative,

\[
F=\{\limsup_n e_n>0\}=\bigcup_{m\ge1}E_m.
\]

Therefore `G_m=F\setminus E_m` decreases and has empty intersection. Finite additivity, not countable additivity, is enough for

\[
P(G_m)=P(F)-P(E_m)=\gamma.
\]

Because `P(H)=R(\Phi(H))` for every Borel `H`, `P(E_m)=0` gives `Phi(E_m)=0` in the `R`-measure algebra. Booleanity then gives

\[
\Phi(G_m)=\Phi(F)\setminus\Phi(E_m)=\Phi(F),
\]

and (4.3) follows from `P(F)=gamma`.  QED.

### Corollary 4.2 (all failure mass must be carried by an ordinary martingale exceptional set)

Let `B=Phi(A)`, and let

\[
N_B=\left\{\omega:
E_R[\mathbf1_B\mid\mathscr F_n](\omega)
\not\to \mathbf1_B(\omega)
\right\}.
\]

Levy's upward theorem gives `R(N_B)=0`. Nevertheless, if `F_A` is the source failure event, then

\[
\boxed{P(F_A)\le P(N_B)=R(\Phi(N_B)).}
\tag{4.4}
\]

In particular, every genuine counterexample must assign positive finitely additive mass to an `R`-null **dyadic martingale differentiation exceptional set belonging to an event in the range of `Phi`**.

### Proof

Off `N_B`, the posterior converges to `1_B`. Hence on `N_B^c`, failure to converge to `1_A` is exactly the truth mismatch `A triangle B`. At every such mismatch point the limiting error is one, so

\[
F_A\setminus N_B\subseteq
\{\limsup_n e_n>1/2\}.
\]

The right-hand event is `P`-null by (3.1). Thus `P(F_A\setminus N_B)=0`; finite additivity and monotonicity give (4.4).  QED.

This is a useful dual target. It is no longer enough to invent a finitely additive null-ideal failure somewhere: it has to land specifically on the exceptional set of the ordinary `R`-martingale generated by a `Phi`-range event.

## 5. Method #19 — MAKE IT AN ALGORITHM: the natural countable hierarchical-ultrafilter construction cannot refute Corollary 1

The preceding run found a coherence obstruction for a two-level ultrafilter idea. I made that obstruction precise for an arbitrary **countable depth/branching hierarchy**. This rules out the most natural recursive attempt to evade Khan--Pedersen--Stinchcombe Proposition 6.7.

### Definition 5.1 (countable sequential ultrafilter hierarchy)

Let `I` be countable and let `X={x_i:i in I}` be distinct points of Cantor space. For each `i`, choose

- a sequence of child indices `c(i,k) in I` such that
  \[
  x_{c(i,k)}\longrightarrow x_i;
  \]
- a free ultrafilter `U_i` on `N`;
- a weight `w_i>0`.

Let `q in (0,1)` and `sum_i w_i=1-q`. Let `Q` be an atomless, full-support countably additive Borel probability with `Q(X)=0`. Define the two-valued charge

\[
u_i(A)=\lim_{k\to U_i}\mathbf1_A(x_{c(i,k)})
\]

and

\[
P(A)=qQ(A)+\sum_{i\in I}w_i u_i(A).
\tag{5.1}
\]

The series is absolutely bounded by `sum_i w_i`, so (5.1) is a well-defined finitely additive probability function.

This class includes arbitrarily many levels and arbitrary countable directed child structure. Every finite node is itself a positive-weight center; this is exactly the recursive idea “protect the outer ultrafilter by putting atoms at its children, then protect those children at the next level, and continue forever.”

### Theorem 5.2 (countable hierarchy no-go)

Every `P` of the form (5.1) satisfies the source positivity and approximation properties. If, in addition, `P` has CHT, then for every Borel event `A`,

\[
P_n(A)\longrightarrow\mathbf1_A
\qquad P\text{-almost surely}.
\tag{5.2}
\]

Consequently **no countable sequential ultrafilter hierarchy of the form (5.1) can refute Nielsen's Corollary 1**.

### Proof

#### Step 1: the companion measure and exact posterior representation

For a clopen `C`, convergence `x_{c(i,k)} -> x_i` makes membership in `C` eventually constant, hence

\[
u_i(C)=\mathbf1_C(x_i).
\]

Therefore the countably additive companion of `P` is

\[
R=qQ+\sum_{i\in I}w_i\delta_{x_i}.
\tag{5.3}
\]

In particular every nonempty cylinder has `P(C)=R(C)>=qQ(C)>0`, so the source positivity assumption holds.

For a Borel event `A`, define

\[
B_A=(A\setminus X)\cup\{x_i:u_i(A)=1\}.
\tag{5.4}
\]

Because `Q(X)=0`, for every clopen `C`, multiplicativity of each two-valued charge gives

\[
\begin{aligned}
P(A\cap C)
&=qQ(A\cap C)+\sum_i w_i u_i(A)u_i(C)\\
&=qQ(A\cap C)+\sum_i w_i u_i(A)\mathbf1_C(x_i)\\
&=R(B_A\cap C).
\end{aligned}
\tag{5.5}
\]

Taking `C=Omega` also gives `P(A)=R(B_A)`. Hence

\[
P_n(A)=E_R[\mathbf1_{B_A}\mid\mathscr F_n].
\tag{5.6}
\]

For clopen `C`, the same identity gives

\[
P(A\triangle C)=R(B_A\triangle C).
\tag{5.7}
\]

Clopens are dense in `R`-measure on Cantor space, so (5.7) proves the approximation property.

#### Step 2: CHT forces coherence between every node and its children

Assume now that `P` has CHT. Then the fixed-threshold nullity (3.1) is available.

At every center `x_i`, (5.3) has a positive atom `R({x_i})>=w_i>0`. Consequently the cylinder ratios in (5.6) converge **pointwise** at `x_i` to

\[
\mathbf1_{B_A}(x_i)=u_i(A).
\tag{5.8}
\]

Indeed the decreasing cylinders about `x_i` have intersection `{x_i}`, and countable additivity of `R` sends numerator and denominator to the corresponding atomic masses.

Put

\[
M_A=\{x_i:\mathbf1_A(x_i)\ne u_i(A)\}.
\tag{5.9}
\]

By (5.8), every point of `M_A` has limiting posterior error one, so

\[
M_A\subseteq\{\limsup_n|P_n(A)-\mathbf1_A|>1/2\}.
\]

Equation (3.1) therefore gives `P(M_A)=0`. Since `M_A subset X`, `Q(M_A)=0`, and (5.1) yields

\[
0=P(M_A)=\sum_i w_i u_i(M_A).
\tag{5.10}
\]

Every term is nonnegative and every `w_i` is positive, so

\[
\boxed{u_i(M_A)=0\quad\text{for every }i.}
\tag{5.11}
\]

Equivalently, for every node `i`, an `U_i`-large set of its children satisfies

\[
\mathbf1_A(x_{c(i,k)})=u_{c(i,k)}(A).
\tag{5.12}
\]

This is the exact coherence law the previous run was missing. It is not an extra design choice: **CHT forces it** through fixed-threshold nullity.

#### Step 3: the truth event and its companion agree `P`-almost surely

Outside `X`, (5.4) gives `A=B_A`. On a child center `x_{c(i,k)}`, membership in `A triangle B_A` is exactly the mismatch in (5.12). Hence (5.11) gives

\[
u_i(A\triangle B_A)=0\quad(i\in I).
\]

Together with `Q(A triangle B_A)=0`, this yields

\[
\boxed{P(A\triangle B_A)=0.}
\tag{5.13}
\]

#### Step 4: ordinary martingale exceptional sets are also `P`-null

Let

\[
N_A=\{E_R[\mathbf1_{B_A}\mid\mathscr F_n]\not\to\mathbf1_{B_A}\}.
\]

Levy's theorem gives `R(N_A)=0`. Because every `x_i` is an `R`-atom, the pointwise argument used in (5.8) shows that no center belongs to `N_A`. Thus every `u_i(N_A)=0`, and `R(N_A)=0` with `q>0` also gives `Q(N_A)=0`. Therefore

\[
\boxed{P(N_A)=0.}
\tag{5.14}
\]

#### Step 5: almost-sure learning

By (5.6), off `N_A` the posterior converges to `1_{B_A}`. By (5.13), `1_{B_A}=1_A` off a `P`-null event. The union of these two null events is null by finite additivity. Hence (5.2) holds. Since `A` was arbitrary, the theorem follows.  QED.

### What this eliminates

The source's one-level obstruction has a sharp dichotomy: leaving distinguished children atomless breaks CHT (their Proposition 6.3), whereas enough atomic protection yields almost-sure learning (their Proposition 6.7). A natural response was to recurse forever: protect level 1 with level-2 atoms, protect level 2 with level-3 atoms, and hope failure survives only at infinite depth. Theorem 5.2 shows that this **countable recursive repair cannot work**. Once every finite node is protected by a positive companion atom, CHT forces inter-level coherence, the ordinary martingale exceptional sets miss every node, and the whole hierarchy learns almost surely.

This is a restricted theorem, not a solution of the arbitrary-probability-function source question.

## 6. Method #30 — ONE SCALE / ONE DIRECTION AT A TIME: what a counterexample must now escape

The preceding two theorems isolate three simultaneous obligations for any genuine negative answer.

First, by Theorem 4.1, it must carry a positive-mass **ghost tower** `G_m downarrow emptyset` whose `Phi`-images are all the same positive measure-algebra element. Thus no fixed positive error scale witnesses failure.

Second, by Corollary 4.2, that mass must be supported by `P` on an ordinary `R`-null martingale exceptional set of a `Phi`-range event. Merely changing truth values on a harmless null set is not enough.

Third, Theorem 5.2 removes the obvious sequential hierarchy in which every outer generalized point is protected by positive-mass child centers recursively. In that architecture the very atom protection needed to keep CHT alive also makes all Levy exceptional sets invisible to every ultrafilter component, after CHT forces the node/child coherence relation (5.12).

So a counterexample, if one exists, must leave this sequential atom-protection category. Plausible remaining shapes include a genuinely non-sequential Stone-fiber charge, an uncountable family of generalized points not reducible to a summable countable hierarchy, or some different mechanism that makes all range-generated first-hitting opens `Phi`-fixed while still charging an `R`-null martingale differentiation set. These are search directions only; none is claimed to exist.

The positive direction is now equally concrete: it would suffice to prove from CHT that

\[
R(N)=0,\ N=N_B\text{ for a range event }B
\quad\Longrightarrow\quad
R(\Phi(N))=0.
\tag{6.1}
\]

Corollary 4.2 would then give `Gamma_AS=0` immediately.

## 7. Metric and status

The source-wide metric does not move numerically this run:

\[
\boxed{W_{\rm AS}:1\to1.}
\]

This is the second consecutive active-target run at width one, so the active-target unchanged count is now **2**. The source status remains **OPEN / PARTIAL**. This is not yet a stuck run under the three-run rule.

No finite checker was manufactured: Theorems 4.1 and 5.2 are analytic/infinite-dimensional and their complete arguments are written above. No audit was requested because this package is not source-closure-ready. The neighboring R06 KPS package is likewise OPEN/PARTIAL, so it is not a candidate for R01's limited second-audit budget.

The next run should not repeat `#11/#19/#30`. The best new attacks are:

- **#5 ADD A PARAMETER AND DIFFERENTIATE:** study the threshold family of martingale exceptional layers and whether CHT controls the derivative/jump measure of `delta -> O_R(B,delta)` strongly enough to prove (6.1);
- **#22 READ THE FAILURES, NOT THE SUCCESSES:** inspect Purves--Sudderth / finitely additive martingale convergence and lifting literature specifically for constructions that charge differentiation-exceptional sets while preserving all first-hitting continuities;
- **#29 ADD THE POINTS AT INFINITY:** pass to the Stone space of the Borel Boolean algebra, where `Phi` becomes a fiber map over Cantor space and (6.1) asks whether CHT excludes nonprincipal fiber mass over martingale-exception points.

## 8. Dated source / current-literature / prior-art check

Fresh checks on 2026-09-18 included:

- exact title and arXiv ID `2609.20683`;
- `Nielsen conditional hitting times finitely additive probability convergence`;
- `approximation property CHT almost-sure convergence finitely additive`;
- `finitely additive martingale almost sure convergence`;
- `Boolean homomorphism measure algebra Borel Cantor lifting`.

The direct arXiv record remains v1 from 2026-09-17 and Section 10 still lists Corollary 1's arbitrary-probability-function statement as open. The bounded search surfaced the original Nielsen paper, Purves--Sudderth's finitely additive probability work, later finitely additive martingale/ergodic convergence literature, and general lifting/measure-algebra literature, but no later source matching a proof or counterexample to this exact approximation+CHT implication. Because the source is roughly one day old, the absence of citing papers is weak negative evidence only. No publication-priority or novelty claim is made.

## 9. Model / scheduler control limitation

The operative scheduler evidence remains unchanged. The exposed task-management surface supplies prompt/title, schedule or relative-start, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-run model/effort receipt, and no guaranteed hour-long execution field. Thus `GPT-6 / maximum` cannot be enforced from this worker surface; it requires an owner-authorized product/workspace/API/admin surface that exposes persistent model/effort controls and runtime attestation.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary recorded in the implementation manifest. The lawful workaround is the owning/otherwise-authorized context or platform support, not duplication or a permission bypass. No scheduler or permission change was attempted.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  lane: CLOSABLE_OUTSIDE
  frozen_previous_source: I0024
  frozen_previous_metric: "C=1"
  source: KPS-2026-NIELSEN-COR1
  source_url: "https://arxiv.org/abs/2609.20683"
  source_scope: "Khan-Pedersen-Stinchcombe Section 10 / Nielsen Corollary 1: approximation + CHT => eventwise almost-sure posterior convergence for arbitrary source probability functions"
  ownership: "R01 exclusive; operations/claims/KPS-2026-NIELSEN-COR1.md"
  metric: "W_AS = U_AS - L_AS for Gamma_AS = sup_{P,A} P(nonconvergence event)"
  metric_before: 1
  metric_after: 1
  unchanged_count: 2
  tried_moves: [11, 19, 30]
  status: "OPEN / PARTIAL"
  new_rigorous_results:
    - "Ghost-tower theorem: any positive failure mass yields G_m downarrow empty with P(G_m) constant and Phi(G_m) identical positive."
    - "Null-transfer bound: P(F_A) <= P(N_{Phi(A)}), where N is the ordinary R-martingale exceptional set."
    - "Countable hierarchical-ultrafilter no-go theorem: any countable child-center hierarchy of form (5.1) satisfying CHT converges to truth almost surely."
    - "CHT forces exact parent/child truth-companion coherence in that hierarchy via the fixed-threshold nullity theorem."
  remaining_obligation: >-
    Prove CHT forces Phi to annihilate ordinary R-null martingale exceptional sets of range events, which would prove Corollary 1, or construct a genuinely non-sequential/non-atom-protected Phi that fixes every required hitting open yet charges such an exceptional set.
  evidence:
    - "Theorem 4.1 and Corollary 4.2 in this report"
    - "Theorem 5.2 in this report"
    - "previous R01 companion / Boolean-homomorphism normal form"
    - "Khan-Pedersen-Stinchcombe arXiv:2609.20683v1, Sections 4, 6, 9, 10"
    - "neighbor R06 same-source Theorem-4 report read; no scope overlap"
  audit_ids: []
  next_moves: [5, 22, 29]
```
