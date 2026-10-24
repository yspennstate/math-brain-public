Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated reasoning-effort telemetry and no GPT-6 selector, so GPT-6 maximum is not claimed. F0097 NO MOVEMENT on the frozen source metric: `Omega_3 <= 0.9698` remains; F0097 unchanged count `4 -> 5`. This executes recovery action 1 selected by run46. Methods: #4 PROVE SOMETHING WEAKER, COMPLETELY; #18 SAY IT IN ANOTHER LANGUAGE; #13 FIND WHAT ONLY INCREASES.**

# R03 run47 — F0097 random k-SAT: exact linear-hypertree cavity analysis and a sharp generic-transfer obstruction

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0097 OPEN / R03 PARTIAL / RECOVERY ACTION 1 EXECUTED / source metric unchanged.**

The native title/prompt still names F0001 / sharp iid Rademacher singularity, but canonical R03 state handed F0001 off after its third stuck episode in `runs/R03/20260917T1907Z_41_third_stuck_handoff_f0097.md` and the create-only claim `operations/claims/F0097.md` says explicitly that R03 must not return to F0001 without reassignment. I therefore preserve F0001 as OPEN/PARTIAL/HANDED-OFF and continue the currently owned HARD OUTSIDE target F0097.

This report carries out exactly the recovery action chosen in run46: analyze the simplest collision-rich booster shape, a clean 3-CNF whose clause-intersection graph is a tree, adjacent clauses share exactly one variable, and no variable belongs to more than two booster clauses. The result is useful but negative at the source scale: the tree class admits a complete cavity analysis, and that analysis constructs an explicit exponentially bad obstruction to any **generic** mesoscopic-to-local transfer. Therefore a successful continuation must use the fact that the ambient measure is the solution measure of near-critical random 3-SAT, not merely that a tree booster covers its support.

## 1. Continuity, source, ownership, and current literature

I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the controlling owner directive, `operations/claims/F0097.md`, newest own report `runs/R03/20260918T0010Z_46_stuck_thinking_01_b91f.md`, the preceding R03 F0097 reports 42--45, the neighboring R02 F0097 admission screen, and the intake history `F0097-A001`. No previous failed route or stagnation count is reset.

The original outside source remains Alan Frieze, *Random Structures and Algorithms*, Proceedings of the ICM 2014. The primary PDF says on p. 332 that finding `c_k` for fixed `k=O(1)` is a major open problem, and its open-problem P3 on p. 334 asks to find the precise threshold for the satisfiability of random `k`-SAT.

Primary source URL: `https://www.math.cmu.edu/users/af1p/Texfiles/Proc.pdf`.

Fresh bounded current-status check, 2026-09-18 UTC:

- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (published online 27 March 2026), still states that the satisfiability threshold is known precisely for `k=2` and for `k>=k_0` with `k_0` an undetermined large constant; small fixed `k` remains outside that theorem.
- Ding--Sly--Sun, *Proof of the satisfiability conjecture for large k*, Annals of Mathematics 196 (2022), proves the exact threshold for all sufficiently large `k`, not the first unresolved small cases.
- Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, publication 16 August 2026, proves an `O(n/log n)` scaling window for every fixed `k>=3`; this does not prove convergence of the threshold location for small fixed `k`.
- For the special class used below, Dominik Scheder's *Satisfiability of Almost Disjoint CNF Formulas* (arXiv:0807.1282) is relevant prior art on linear CNFs. The tree-message calculation below is elementary dynamic programming, and the path recurrence is the negative-fugacity independence-polynomial / Shearer language. I make **no publication-novelty claim** for either mechanism. The new value of the calculation here is as a precise R03 obstruction to the route selected in run46.

A bounded search did not locate a later source-matching small-`k` threshold theorem. This is negative search evidence, not a worldwide novelty certificate.

The frozen source-valid metric remains

\[
\theta_{k,n}=\frac1n\min\{m:\Pr(F_k(n,m)\text{ SAT})\le1/2\},\qquad
\Omega_k=\limsup_n\theta_{k,n}-\liminf_n\theta_{k,n}.
\]

The first unresolved case tracked by R03 is `k=3`, with target `Omega_3=0`. The conservative retained rigorous bracket is

\[
\boxed{0\le \Omega_3\le 4.4898-3.52=0.9698.}
\]

Nothing below narrows this bracket.

## 2. The recovery class

Call a clean 3-CNF `B` a **loose hypertree booster shape** if:

1. every clause has three distinct variables;
2. its clause-intersection graph is a tree;
3. two adjacent clauses share exactly one variable and nonadjacent clauses are disjoint;
4. no variable belongs to more than two clauses.

If `B` has `t` clauses, then

\[
|\operatorname{supp}B|=3t-(t-1)=2t+1,
\qquad
q_{\rm coll}(B)=3t-(2t+1)=t-1.
\]

Thus this is the minimally collision-rich family immediately beyond the low-collision orbit-randomization regime isolated in run44.

For any satisfiable clean formula `H` on its own support write

\[
q(H)=\frac{|\operatorname{SAT}(H)|}{2^{|\operatorname{supp}H|}}.
\]

The run45 booster-to-overlap inequality C305 uses exactly this density.

## 3. Method #4 — prove something weaker, completely

### R03-C307 — golden-ratio cavity bound for every loose hypertree 3-CNF

Let

\[
\alpha=\frac{\sqrt5-1}{2},\qquad
\rho=1-\frac{\alpha}{4}=\frac{9-\sqrt5}{8}.
\]

Numerically,

\[
\alpha=0.6180339887\ldots,\qquad
\rho=0.8454915028\ldots .
\]

**Theorem C307.** If `B` is any loose-hypertree 3-CNF with `t>=1` clauses, with arbitrary literal signs, then

\[
\boxed{
q(B)\ge \frac78\,\rho^{t-1}.
}
\tag{C307}
\]

This is a theorem for the restricted tree class only; it does not move the F0097 source metric.

#### Boundary-message lemma

Root a nonempty loose hypertree `H` at a clause containing a distinguished **boundary variable** `x`, where `x` appears in no other clause of `H`. Under the uniform measure on `SAT(H)`, each of the two values of `x` has probability at most `alpha`.

**Proof.** Let `s` be the value of `x` that satisfies its literal in the root clause and `f` the value that falsifies it. Remove the root clause. Because the clause graph is a tree and variables have booster-degree at most two, the remaining pieces attached through the other two root variables are disjoint child subtrees.

Suppose `k in {0,1,2}` of the other two root variables lead to child subtrees; the remaining `p=2-k` variables are private to the root clause. For child `i`, let `q_i` be the probability, under the uniform satisfying measure of that child subtree, that its shared variable takes the value that falsifies its literal in the root clause.

When `x=s`, the root clause is already satisfied, so after normalizing the child-subtree and private-variable weights the extension weight is `1`. When `x=f`, the only forbidden configuration is that every other root literal also falsifies. Therefore the false-to-true extension-weight ratio is

\[
R=1-2^{-p}\prod_{i=1}^k q_i.
\tag{3.1}
\]

Inductively `q_i<=alpha`. Hence the three possible root types give

\[
\begin{array}{lll}
k=0:&R=3/4&\ge\alpha,\\[1mm]
k=1:&R\ge1-\alpha/2&\ge\alpha,\\[1mm]
k=2:&R\ge1-\alpha^2&=\alpha,
\end{array}
\]

where `alpha^2=1-alpha`. Also `R<=1`. Thus

\[
\Pr(x=f)=\frac{R}{1+R}\le\frac12\le\alpha,
\qquad
\Pr(x=s)=\frac1{1+R}\le\frac1{1+\alpha}=\alpha,
\]

using `alpha(1+alpha)=1`. This closes the induction. QED.

#### Leaf-peeling proof of C307

For `t=1`, one 3-clause is satisfied by exactly `7/8` of assignments, so `q(B)=7/8`.

For `t>=2`, remove a leaf clause `C`. It shares a single variable `x` with the remaining loose hypertree `H` and has two variables private to `C`. In `H`, the variable `x` is a boundary variable. Let

\[
p=\Pr_{\mu_H}(x\text{ takes the value falsifying its literal in }C).
\]

By the boundary-message lemma, `p<=alpha`.

For a satisfying assignment of `H`, if `x` satisfies its literal in `C`, all four assignments of the two new private variables extend; if `x` falsifies it, exactly three of the four extend. Hence

\[
q(B)=q(H)\left(1-\frac p4\right)
\ge q(H)\left(1-\frac\alpha4\right)
=\rho q(H).
\]

Iterating leaf removal down to one clause gives C307. QED.

### Consequence for the run45 overlap bound

Run45 proved, for a fixed booster shape `B` of support size `r`,

\[
\mathbb E\mathcal C_r(X)
\ge \beta_X(B)\frac{q(B)}{1-q(B)}.
\tag{C305b}
\]

For the present tree class `r=2t+1`; C307 therefore gives the stronger restricted estimate

\[
\boxed{
\mathbb E\mathcal C_{2t+1}(X)
\ge
\beta_X(B)\,\frac{\frac78\rho^{t-1}}
{1-\frac78\rho^{t-1}}
\ge
\beta_X(B)\,\frac78\rho^{t-1}.
}
\tag{C307b}
\]

Relative to the generic run45 use of only `q(B)>=2^{-(2t+1)}`, the density factor improves by

\[
\frac{(7/8)\rho^{t-1}}{2^{-(2t+1)}}
=7(4\rho)^{t-1},
\qquad
4\rho=\frac{9-\sqrt5}{2}=3.381966\ldots .
\]

This is a real exponential improvement **inside the special class**, but it is still exponential in `t`; therefore it does not by itself break the `K=Theta(log n)` architecture from C302.

## 4. Method #18 — say it in another language

The same tree class is a one-dimensional/factor-tree partition function. The cleanest exact example is a path.

### R03-C308 — exact opposite-polarity path partition function

Take a path `B_t={C_1,...,C_t}` of loose-hypertree clauses. Choose the literal signs on every shared variable so that the two incident clauses use opposite signs. Then the events

\[
E_i=\{C_i\text{ is falsified}\}
\]

have three properties under the uniform assignment measure:

1. `Pr(E_i)=1/8`;
2. adjacent `E_i,E_{i+1}` are mutually exclusive;
3. any collection indexed by an independent set of the path uses disjoint variables and therefore has intersection probability `8^{-|S|}`.

Inclusion--exclusion therefore gives

\[
q_t:=q(B_t)
=\sum_{S\subseteq[t]\atop S\text{ independent in }P_t}
(-1/8)^{|S|}
=I_{P_t}(-1/8),
\]

where `I_{P_t}` is the path independence polynomial. Equivalently,

\[
\boxed{
q_t=q_{t-1}-\frac18q_{t-2},\qquad
q_0=1,\quad q_1=\frac78.
}
\tag{C308a}
\]

Solving the recurrence,

\[
\boxed{
q_t=A\lambda_+^t+B\lambda_-^t,
\qquad
\lambda_\pm=\frac{2\pm\sqrt2}{4},
}
\tag{C308b}
\]

with

\[
A=\frac12+\frac{3\sqrt2}{8},
\qquad
B=\frac12-\frac{3\sqrt2}{8}.
\]

Thus

\[
q_t\sim A\lambda_+^t,
\qquad
\lambda_+=\frac{2+\sqrt2}{4}=0.8535533906\ldots .
\tag{C308c}
\]

So even an irredundant, maximally simple linear-tree clause family can have satisfying density `e^{-Theta(t)}`. The path recurrence is standard hard-core / independence-polynomial language; I am not claiming that recurrence as new prior art. Its role here is to test whether the run46 recovery class can possibly give a subexponential transfer just from its tree geometry.

The answer is no.

## 5. Method #13 — find what only increases

The cavity proof contains an exact normalized monotone. When a leaf clause is attached to a loose hypertree,

\[
q_{t}\ge\rho q_{t-1}.
\]

Therefore

\[
\boxed{
M_t:=\frac{q_t}{\rho^{t-1}}
}
\]

never decreases under leaf attachment, and `M_1=7/8`. This is exactly C307.

At the message level, the preserved invariant interval is

\[
R\in[\alpha,1],
\]

where `R` is the falsifying-to-satisfying boundary weight ratio. The golden-ratio endpoint is forced by the two-child worst-case map through

\[
1-\alpha^2=\alpha.
\]

This is the useful monovariant/invariant extracted by method #13; it closes the full tree recursion with no numerical checker.

## 6. The concrete obstruction: C305 is sharp for arbitrary measures even on this path

The path calculation exposes something stronger than merely “the lower bound is still exponential.” It gives an explicit measure showing that the entire run45 mesoscopic-to-local inequality is **generically sharp** and cannot be upgraded by tree geometry alone.

Let

\[
Q_t=\operatorname{SAT}(B_t)\subseteq\{0,1\}^{2t+1},
\qquad
U_t=Q_t^c,
\qquad
q_t=2^{-(2t+1)}|Q_t|.
\]

Let `u` be the uniform measure on the full cube and let

\[
\nu_t=u(\,\cdot\mid U_t),
\]

i.e. uniform measure conditioned on **violating at least one clause of `B_t`**. Then every sample from `nu_t` is killed by adding `B_t`:

\[
\nu_t(Q_t)=0.
\]

### R03-C309 — exact global divergence and exponentially invisible local marginals

The density ratio is `0` on `Q_t` and `1/(1-q_t)` on `U_t`, so directly

\[
\boxed{
\chi^2(\nu_t\|u)=\frac{q_t}{1-q_t}.
}
\tag{C309a}
\]

This is **equality** in the variational lower bound underlying C305. Hence C305 cannot be strengthened for arbitrary measures merely from the condition that the support avoids `SAT(B_t)`.

Moreover,

\[
\boxed{
\|\nu_t-u\|_{\rm TV}=q_t.
}
\tag{C309b}
\]

By data processing, for every coordinate set `S`,

\[
\|\nu_{t,S}-u_S\|_{\rm TV}\le q_t.
\tag{C309c}
\]

For a fixed `s=|S|`, writing `d_x=\nu_{t,S}(x)-2^{-s}`, this implies

\[
\sum_x|d_x|\le2q_t.
\]

Therefore

\[
\boxed{
\chi^2(\nu_{t,S}\|u_S)
=2^s\sum_xd_x^2
\le 2^{s+2}q_t^2.
}
\tag{C309d}
\]

In particular every 3-variable marginal obeys

\[
\chi^2(\nu_{t,S}\|u_S)\le32q_t^2.
\]

But the full-support chi-square is asymptotic to `q_t`. Combining with C308c,

\[
\frac{\max_{|S|=3}\chi^2(\nu_{t,S}\|u_S)}
{\chi^2(\nu_t\|u)}
\le 32q_t(1-q_t)
=\exp(-\Theta(t)).
\tag{C309e}
\]

So **an exponential mesoscopic-to-local loss is genuinely possible even for the simplest loose-hypertree obstruction** if one only assumes that the ambient measure is supported on assignments killed by the booster.

This is the concrete finite-structure obstruction the recovery was supposed to locate. It explains why another generic Fourier inequality cannot close `(BLOCK)`: the missing theorem must use the additional fact that the ambient measure is the solution measure of a near-critical random 3-CNF (or an equivalent random-CSP structural property). Tree geometry of `B` alone is insufficient.

No finite enumeration is involved in C307--C309; all claims are proved symbolically above, so no checker was manufactured.

## 7. What moved mathematically, and what did not

What improved:

- the selected collision-rich loose-hypertree class now has a complete exact cavity analysis;
- the generic `2^{-(2t+1)}` density floor in C305 is replaced inside this class by `(7/8)rho^{t-1}`;
- an explicit opposite-polarity path gives the exact exponential partition function `I_{P_t}(-1/8)`;
- the conditioned-complement measure proves C305 is exactly sharp for arbitrary measures and shows an exponential gap between full-support and bounded-local chi-square correlation.

What did **not** improve:

\[
0\le\Omega_3\le0.9698
\]

is unchanged. The source-level obligation remains to prove `Omega_3=0`, or otherwise obtain a genuinely source-moving fixed-`k` threshold theorem.

The remaining obstruction is now sharper than run46's schematic `(BLOCK)`:

\[
\boxed{
\text{Find a property specific to near-critical random 3-CNF solution measures that rules out the C309-type exponential hiding of correlation.}
}
\tag{BLOCK-47}
\]

Any argument valid for arbitrary Boolean-cube measures is now known to be incapable of doing this at subexponential loss, even on the simplest tree booster shape.

Because the frozen metric again did not move, the unchanged count is `4 -> 5`. Under the hard-target stuck policy, the **next R03 run is required to be the second Section-I thinking-only stuck recovery**, not another theorem/checker run. The three methods planned for that thinking run are **#11 DUALIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #29 ADD THE POINTS AT INFINITY**. It must choose exactly one second recovery action. If a later third stuck episode occurs after the second recovery cycle, F0097 must be handed off and R03 rotated rather than continuing indefinitely.

## 8. Model / scheduler-control status

This remains unchanged. The exposed scheduler-control surface available to this runtime has fields for prompt/title, schedule/timing, enablement and related task state, but **no model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` is still request text only; this report cannot honestly claim it ran.

The repository reconciliation also records that the old P26 `You cannot modify this task` failure was context-dependent: P26 later updated successfully from another authorized context, while R-series edits were denied in a different context. The legitimate workaround for a denied task is the owning/authorized account or workspace context, or platform support. A repository edit cannot repair scheduler ownership, and no permission bypass or duplicate schedule is authorized.

No scheduler state was changed in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R03
  lane: HARD_OUTSIDE
  current_target: F0097
  source_status: OPEN
  mathematical_status: PARTIAL
  prior_target_F0001: OPEN_PARTIAL_HANDED_OFF_DO_NOT_REOPEN_WITHOUT_REASSIGNMENT
  frozen_metric: Omega_3
  metric_before: "0 <= Omega_3 <= 0.9698"
  metric_after: "0 <= Omega_3 <= 0.9698"
  movement: false
  unchanged_count_before: 4
  unchanged_count_after: 5
  stuck_state: "recovery action 1 executed; next run = stuck thinking recovery 2"
  methods_used: [4, 18, 13]
  new_internal_claims: [R03-C307, R03-C308, R03-C309]
  claim_scope: "restricted loose-hypertree booster geometry / generic-measure obstruction only"
  closure_claimed: false
  checker_created: false
  next_methods: [11, 17, 29]
  next_run_mode: STUCK_THINKING_02
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  workflow_execution: false
  scheduler_change: false
```

## 10. Bottom line

The selected special case was not a dead end disguised as a lemma. It gives a complete answer to a precise methodological question: **loose-hypertree booster geometry alone cannot yield the subexponential mesoscopic-to-local transfer needed to beat the present logarithmic window architecture.** The exact obstruction is C309, and the path family makes the loss exponentially sharp. The next recovery must therefore move to a property of the *random 3-CNF solution measure itself* rather than further refining the deterministic booster tree.