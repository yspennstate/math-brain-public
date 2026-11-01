Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; first substantive G0004 run; methods #2 ATTACK THE NEGATION FIRST / #14 FIND THE GROUP ACTING / #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.**

# R17 C069 — G0004 first substantive run: symmetrization and the exact sharp star rate

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R17, HARD OUTSIDE.
Status: **OPEN / PARTIAL**.

## 0. Continuity and ownership correction

The original Chvatal--Sankoff binary-LCS target remains terminally handed off after its two permitted HARD recoveries at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626.
\]

The later Rhodes--Vargas `D0064` source likewise remains terminal for R17 after HARD recovery `2/2`, with strict metric `R_class=0/3`. Neither predecessor is reopened here.

The newest prior R17 report recovered at the start of this run was

`runs/R17/20260919_0941Z_admission_delta_p0157_released_hard_c068_a91c5f72.md`.

That report was written from a stale/concurrent admission snapshot. The current direct canonical file

`operations/claims/G0004.md`

now controls: it names **R17** as exclusive owner, status **CLAIMED / ACTIVE / HARD OUTSIDE / SOURCE OPEN-LOOKING**, and fixes the source-wide metric below. This run therefore starts substantive work on G0004 rather than remaining in successor wait.

I also reread the campaign `INDEX.md`, root `QUEUE.md`, the controlling `operations/NEW_METHODS_2026-09-16.md`, the G0004 intake/attempt record, and R7-02's exact failure-kernel screen before doing new mathematics. The prior binary-LCS and D0064 work, the G0004 singleton-FKG observation, the independent-route `epsilon log(1/epsilon)` example, R7-02's exact kernel reduction, bounded-contact theorem, and monotone-selector obstruction are treated as inherited history, not rederived as new results.

## 1. Source and fresh status check

Outside source: Lucas Flammant, *A conjecture implying $\theta(p_c)=0$ for Bernoulli bond percolation on $\mathbb Z^d$*, arXiv:2609.03492v2, Conjecture 2.2.

For Bernoulli bond percolation on an arbitrary finite graph `G=(V,E)`, root `o`, boundary set `B`, and events `(E_b)_{b in B}` such that `omega -> P(E_b | pi=omega)` is increasing and `P(E_b)>=1-epsilon`, the source asks for a universal `phi(epsilon)->1` satisfying

\[
\mathbb P\!\left(\bigcup_{b\in B}\{o\leftrightarrow b\}\cap E_b\right)
\ge \phi(\varepsilon)\,\mathbb P(o\leftrightarrow B).
\]

The current public arXiv record, checked again on 2026-09-19 by exact arXiv id, title, and Conjecture-2.2 wording, still presents this as the main conjecture, proves the outer-face planar case with `1-2 sqrt(epsilon)`, and says the arbitrary-increasing-event replacement is false. The bounded fresh search recovered no later primary source claiming a full finite-graph solution. That is bounded negative evidence only, not a worldwide openness or novelty certificate.

R7-02 already proved the exact equivalent failure-kernel formulation. Let

\[
S(\omega)=\{b\in B:o\leftrightarrow b\},\qquad C=\{S\ne\varnothing\},
\]

and let `q_b:{0,1}^E->[0,1]` be decreasing with `E q_b<=epsilon`. Then the exact worst-case failure ratio is

\[
R(G,p,o,B;q)
=
\frac{\mathbb E\big[\mathbf 1_C\min_{b\in S}q_b\big]}{\mathbb P(C)},
\]

and

\[
R_*(\varepsilon)=\sup_{G,p,o,B,q}R(G,p,o,B;q).
\]

Flammant's conjecture is equivalent to `R_*(epsilon)->0`.

The fixed R17 metric is therefore

\[
U_F:=\text{smallest rigorously certified upper bound on }
\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)
\]

under the full source quantifiers. Baseline and current value are both `U_F=1`. Restricted-family theorems do not move it.

## 2. Method #14 — automorphism symmetrization is lossless and improves the objective

This is the first new theorem of the run.

### Theorem 2.1 (equivariant optimizer on a symmetric finite instance)

Fix a finite percolation instance `(G,p,o,B)` and let `Gamma` be a finite group of graph automorphisms preserving the percolation law, fixing `o`, and preserving `B` setwise. For every feasible kernel family `(q_b)_{b in B}`, there is a `Gamma`-equivariant feasible family `(\bar q_b)` such that

\[
R(G,p,o,B;\bar q)\ge R(G,p,o,B;q).
\]

Consequently the supremum over feasible kernels on this fixed instance is attained, whenever attained at all, within the equivariant class; more generally every feasible family can be symmetrized without lowering the objective.

### Proof

For `g in Gamma`, define the transported family

\[
(gq)_b(\omega):=q_{g^{-1}b}(g^{-1}\omega).
\]

Because graph automorphisms preserve coordinatewise order, `(gq)_b` is decreasing whenever the original kernels are. Because the product percolation law is `Gamma`-invariant,

\[
\mathbb E (gq)_b=\mathbb E q_{g^{-1}b}\le\varepsilon,
\]

so every transported family is feasible. Define

\[
\bar q:=\frac1{|\Gamma|}\sum_{g\in\Gamma}gq.
\]

Then `\bar q` is feasible and equivariant.

For each fixed percolation configuration with `S(omega) nonempty`, the map

\[
(q_b)_{b\in S(\omega)}\longmapsto \min_{b\in S(\omega)}q_b
\]

is concave, being the pointwise minimum of coordinate-affine maps. Hence Jensen gives

\[
\min_{b\in S(\omega)}\bar q_b(\omega)
\ge
\frac1{|\Gamma|}\sum_{g\in\Gamma}
\min_{b\in S(\omega)}(gq)_b(\omega).
\]

Multiplying by `1_C`, averaging, and using invariance of both the percolation law and the connectivity set under `Gamma` yields

\[
\mathbb E[\mathbf1_C\min_{b\in S}\bar q_b]
\ge
\frac1{|\Gamma|}\sum_g
\mathbb E[\mathbf1_C\min_{b\in S}(gq)_b]
=
\mathbb E[\mathbf1_C\min_{b\in S}q_b].
\]

The denominator `P(C)` is unchanged. This proves the theorem. `square`

### Consequence for the counterexample search

A counterexample search on a highly symmetric graph does not need arbitrary vertex-labelled kernels. It is enough to search orbit variables. This is useful because the minimization in the objective, rather than obstructing symmetrization, makes the objective concave and therefore makes group averaging favorable.

## 3. Method #16 — exact solution of the full variational problem on every star

The intake had one specific adversarial family on independent routes. Here the **entire admissible failure-kernel optimization on a star** is solved exactly.

Let `Star_m` consist of `m` independent edges from `o` to leaves `B={1,...,m}`, each open with probability `p`. Put `n=m-1`.

### Theorem 3.1 (exact star optimizer)

Let

\[
J\sim\operatorname{Bin}(m-1,p),\qquad K\sim\operatorname{Bin}(m,p).
\]

The exact optimum of the R7-02 failure functional over **all** decreasing kernels `q_i` satisfying `E q_i<=epsilon` is

\[
R_{\rm star}(m,p,\varepsilon)
=
\frac{mp}{1-(1-p)^m}
\max\left\{
\mathbb E\frac{a_J}{J+1}:
0\le a_j\le1,\ a_0\ge a_1\ge\cdots\ge a_n,
\ \mathbb E a_J\le\varepsilon
\right\}.
\]

Moreover the optimizer is a lower-tail threshold. If `r` is the least integer with

\[
\mathbb P(J\le r)\ge\varepsilon,
\]

and

\[
\vartheta=
\frac{\varepsilon-\mathbb P(J\le r-1)}{\mathbb P(J=r)}\in[0,1],
\]

then one may take

\[
a_j=
\begin{cases}
1,&j<r,\\
\vartheta,&j=r,\\
0,&j>r,
\end{cases}
\]

(with the evident endpoint conventions), and therefore

\[
R_{\rm star}(m,p,\varepsilon)
=
\frac{mp}{1-(1-p)^m}
\left[
\sum_{j<r}\frac{\mathbb P(J=j)}{j+1}
+
\frac{\vartheta\,\mathbb P(J=r)}{r+1}
\right].
\]

### Proof

By Theorem 2.1 we may average over the full symmetric group `S_m` acting on the leaves. For a fixed leaf `i`, equivariance implies that `q_i` depends only on whether its own edge is open and on the number `j` of open *other* edges. Write

\[
a_j=q_i(1,j),\qquad c_j=q_i(0,j).
\]

Decreasingness gives

\[
a_0\ge a_1\ge\cdots\ge a_n,\qquad
c_0\ge c_1\ge\cdots\ge c_n,\qquad c_j\ge a_j.
\]

The objective only evaluates `q_i` when leaf `i` is connected, hence only the values `a_j` occur in the minimum. Replacing `c_j` by `a_j` for every `j` preserves decreasingness, leaves the objective unchanged, and weakly decreases the budget. Thus an optimizer may be chosen with `c_j=a_j`.

For every configuration with exactly `K=k>=1` open arms, every connected leaf sees exactly `j=k-1` other open arms. Hence the conditional minimum is simply `a_{k-1}` and the failure numerator equals

\[
\sum_{k=1}^m\mathbb P(K=k)a_{k-1}.
\]

Using

\[
\mathbb P(K=k)=\frac{mp}{k}\,\mathbb P(J=k-1)
\]

gives

\[
\mathbb E[\mathbf1_{K>0}\min_{i\in S}q_i]
=mp\,\mathbb E\frac{a_J}{J+1}.
\]

The budget after setting `c=a` is exactly `E a_J<=epsilon`, and `P(K>0)=1-(1-p)^m`, proving the first formula.

For the remaining finite-dimensional optimization, the cost of assigning one unit of `a_j` is `P(J=j)` while its value is `P(J=j)/(j+1)`. The value-to-cost ratio is `1/(j+1)`, strictly decreasing in `j`. Thus the fractional-knapsack optimizer fills `j=0,1,2,...` in order until the budget `epsilon` is exhausted. This optimizer is automatically nonincreasing, so the monotonicity constraint causes no loss. The threshold formula follows. `square`

This is an analytic theorem for every `m`; no floating-point finite enumeration is being promoted to a claim and no checker artifact is needed for it.

## 4. Methods #2 and #16 together — stars have the sharp rate `epsilon log(1/epsilon)` and therefore are not counterexamples

Define the worst star failure ratio

\[
S_{\rm star}(\varepsilon):=
\sup_{m\ge1}\sup_{0<p<1}R_{\rm star}(m,p,\varepsilon).
\]

The intake already found one independent-route construction suggesting an `epsilon log(1/epsilon)` scale. The new result proves that this scale is **asymptotically optimal among every admissible event/kernel family on every star**.

### Theorem 4.1 (sharp star asymptotic)

As `epsilon downarrow 0`,

\[
\boxed{
S_{\rm star}(\varepsilon)
\sim
\varepsilon\log\frac1\varepsilon.
}
\]

In particular, stars cannot refute Flammant's conjecture. Conversely any universal quantitative strengthening with

\[
1-\phi(\varepsilon)=O(\varepsilon)
\]

is impossible in general, already on stars; the best possible universal rate, if the full conjecture is true, cannot be little-o of `epsilon log(1/epsilon)`.

### Proof: lower bound

Put

\[
L=\log(1/\varepsilon).
\]

For any integer `n>=1`, take `m=n+1` and

\[
p_n=1-e^{-L/n},
\]

so that `(1-p_n)^n=epsilon`. Define, for each arm `i`,

\[
q_i(\omega)=\mathbf1\{\text{all other }n\text{ arms are closed}\}.
\]

This kernel is decreasing, does not depend on the state of arm `i`, and satisfies `E q_i=epsilon` exactly. The source failure occurs precisely when exactly one arm is open. Therefore

\[
R
=
\frac{\mathbb P(K=1)}{\mathbb P(K\ge1)}
=
\frac{(n+1)(1-e^{-L/n})\,\varepsilon}
{1-\varepsilon e^{-L/n}}.
\]

For fixed `epsilon`, letting `n->infinity` gives

\[
S_{\rm star}(\varepsilon)
\ge
\frac{\varepsilon L}{1-\varepsilon}.
\]

Hence

\[
\liminf_{\varepsilon\downarrow0}
\frac{S_{\rm star}(\varepsilon)}{\varepsilon\log(1/\varepsilon)}\ge1.
\]

### Proof: upper bound

Take arbitrary `m,p` and an optimal symmetric sequence `a_j` from Theorem 3.1. Again put `n=m-1`, `J~Bin(n,p)`, and `L=log(1/epsilon)`. The identity

\[
\frac1{j+1}=\int_0^1x^j\,dx
\]

gives

\[
\mathbb E\frac{a_J}{J+1}
=
\int_0^1\mathbb E[a_Jx^J]\,dx.
\]

Since `0<=a_J<=1` and `E a_J<=epsilon`,

\[
\mathbb E[a_Jx^J]
\le
\min\{\varepsilon,\mathbb E x^J\}
=
\min\{\varepsilon,(1-p+px)^n\}.
\]

Thus

\[
R_{\rm star}(m,p,\varepsilon)
\le
\frac{mp}{1-(1-p)^m}
I,
\]

where

\[
I:=\int_0^1\min\{\varepsilon,(1-p+px)^n\}\,dx.
\]

We split into three elementary regimes.

**Regime 1: `n<sqrt(L)`.** R7-02's already-proved bounded-contact inequality gives

\[
R_{\rm star}\le \varepsilon\,\mathbb E[K\mid K>0]
\le\varepsilon m
\le\varepsilon(\sqrt L+1)
=o(\varepsilon L).
\]

**Regime 2: `n>=sqrt(L)` and `(1-p)^n>=epsilon`.** Then

\[
p\le1-e^{-L/n}\le L/n.
\]

Also `I<=epsilon`. Since

\[
1-(1-p)^m\ge1-e^{-mp}\ge\frac{mp}{1+mp},
\]

we get

\[
R_{\rm star}
\le
\varepsilon(1+mp)
\le
\varepsilon\left[1+L\left(1+\frac1n\right)\right].
\]

**Regime 3: `n>=sqrt(L)` and `(1-p)^n<epsilon`.** There is a unique `x_0 in (0,1)` satisfying

\[
1-p+px_0=\varepsilon^{1/n}.
\]

Because `(1-p+px)^n` is increasing,

\[
I
=
\int_0^{x_0}(1-p+px)^n\,dx
+
\varepsilon(1-x_0).
\]

A direct integration gives

\[
I
=
\frac{\varepsilon^{1+1/n}-(1-p)^{n+1}}{p(n+1)}
+
\varepsilon(1-x_0).
\]

Since

\[
p(1-x_0)=1-\varepsilon^{1/n},
\]

multiplication by `mp=(n+1)p` yields

\[
mpI
=
\varepsilon^{1+1/n}-(1-p)^m
+m\varepsilon(1-\varepsilon^{1/n})
\le
\varepsilon+\varepsilon m\frac{L}{n}
=
\varepsilon\left[1+L\left(1+\frac1n\right)\right].
\]

Here `(1-p)^m<epsilon`, so the denominator satisfies

\[
1-(1-p)^m>1-\varepsilon.
\]

Consequently

\[
R_{\rm star}
\le
\frac{\varepsilon[1+L(1+1/n)]}{1-\varepsilon}.
\]

In Regimes 2 and 3, `n>=sqrt(L)`, so `1/n=o(1)`. Combining all three regimes gives

\[
\limsup_{\varepsilon\downarrow0}
\frac{S_{\rm star}(\varepsilon)}{\varepsilon L}\le1.
\]

Together with the lower bound this proves the theorem. `square`

## 5. What methods #2, #14 and #16 actually taught us

### #2 ATTACK THE NEGATION FIRST

A natural counterexample mechanism is to make the origin typically connect to exactly one of many boundary candidates, then let `q_b` detect the absence of all competing contacts. That mechanism was already present in the intake and therefore is **not** claimed as new here. The new exact star optimization proves that, even after allowing every admissible decreasing kernel and every `m,p`, this mechanism only produces a vanishing worst ratio of asymptotic size

\[
\varepsilon\log(1/\varepsilon).
\]

So the entire independent-star class is ruled out as a counterexample source. Any genuine counterexample must use connectivity dependencies that are not reducible to independent arms.

### #14 FIND THE GROUP ACTING

The failure functional is concave in the kernel family. Therefore automorphism averaging is not merely harmless; it can only improve the adversary. Highly symmetric candidate graphs reduce rigorously to orbit variables. This gives a principled finite-dimensional search space for future exact attacks.

### #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

Rather than manufacture a floating-point table, the simplest nontrivial transitive-boundary family was solved symbolically for **all sizes**. The resulting exact threshold optimizer exposes the sequence of value/cost ratios `1,1/2,1/3,...`, and that sequence is exactly what produces the sharp logarithm.

No uncertified numerical scan is promoted to a mathematical claim in this report.

## 6. Why the source metric does not move

The new theorems settle a large restricted family and impose a sharp lower obstruction on any quantitative universal rate, but they do not bound arbitrary finite graphs. Therefore the strict full-source metric remains

\[
U_F:1\longrightarrow1.
\]

This run is **PARTIAL**, not PROVED and not REFUTED. The first substantive G0004 unchanged count is therefore `1`.

The remaining source-wide question is whether correlated connectivity can make

\[
\frac{\mathbb E[\mathbf1_C\min_{b\in S}q_b]}{\mathbb P(C)}
\]

stay bounded away from zero while every `q_b` is decreasing and has mean at most `epsilon->0`, or whether the product-measure/connectivity structure forces this ratio to zero uniformly.

## 7. Next new-methods triple

The next substantive G0004 run must not repeat `#2/#14/#16`. The planned triple is:

- **#11 DUALIZE:** formulate the finite-instance kernel optimization as an exact linear program by introducing a variable `z_omega` with `z_omega<=q_b(omega)` for every `b in S(omega)`, then derive the dual and look for a graph-uniform certificate.
- **#20 FIND WHY THE ALGORITHM FAILS:** test exactly where deletion/contraction, exploration, or orbit-reduced dynamic programming loses a universal factor; turn that obstruction into a structural lemma rather than another checker.
- **#24 FIND THE EXTREMAL OBJECT:** attack the conjecture suggested by this run that stars may be extremal, or asymptotically extremal, for the failure functional; try hard to falsify that conjecture before using it.

## 8. Prior-art discipline

The current source itself contains the planar outer-face theorem and its exploration/FKG proof. R7-02's kernel reduction and selector obstruction are inherited repository work. The intake's independent-route `epsilon log(1/epsilon)` example is also inherited. The contribution of this run is the automorphism-symmetrization theorem, the exact all-kernel star optimizer, and the proof that the inherited logarithmic construction is asymptotically sharp over the entire star class.

A bounded 2026-09-19 search of the exact source title/arXiv id/conjecture wording did not surface these exact restricted theorems or a full solution. I do **not** claim bibliographic novelty or publication priority from that absence.

## 9. Model / scheduler truth

Actual runtime visible to this report is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, hence reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The exposed scheduler-management schema permits task title, prompt, recurrence/timing, enabled state and timing mode, but exposes no bindable model-family or reasoning-effort selector and no authenticated per-run model/effort receipt. GPT-6/maximum is therefore prompt text only on this surface. Enforcing it would require an owner-authorized product/workspace/API/admin execution surface that exposes those fields and attests the applied runtime.

Historical `You cannot modify this task` responses such as P26 are authorization-context boundaries. The lawful workaround is the owning/admin-authorized context or platform support for the existing task, not duplication or permission bypass. No scheduler mutation was attempted here because this deployment explicitly forbids scheduler changes.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R17
  category: HARD_OUTSIDE
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum

  predecessor_1:
    source: binary_LCS_Chvatal_Sankoff
    metric: certified_gamma2_interval_width
    value: 0.033609950762282626
    lifecycle: TERMINAL_HANDOFF_PRESERVED

  predecessor_2:
    source: D0064_Rhodes_Vargas_Conjecture_6_4
    metric: R_class
    value: 0/3
    hard_recoveries: 2/2_EXHAUSTED
    lifecycle: TERMINAL_HANDOFF_PRESERVED

  active_source:
    id: G0004
    source: Flammant_arXiv_2609_03492v2_Conjecture_2_2
    owner: R17
    ownership: EXCLUSIVE_ACTIVE
    status_before: OPEN
    status_after: OPEN_PARTIAL

  metric_name: U_F
  metric_before: 1
  metric_after: 1
  metric_moved: false
  substantive_unchanged_count: 1

  section_B_methods_attempted: [2, 14, 16]
  section_B_methods_next: [11, 20, 24]

  inherited_not_new:
    - singleton_FKG_case
    - independent_route_epsilon_log_example
    - exact_failure_kernel_reduction
    - bounded_contact_theorem
    - monotone_selector_obstruction

  new_results:
    - automorphism_symmetrization_never_lowers_failure_objective
    - exact_variational_optimizer_for_every_star_m_p_epsilon
    - worst_star_failure_asymptotic_epsilon_log_1_over_epsilon
    - universal_rate_O_epsilon_is_impossible_already_on_stars

  source_closed: false
  source_refuted: false
  novelty_claimed: false
  checker_artifacts_created: 0
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
  email_or_drive_used: false
  public_posting_used: false
```

## 11. Operational integrity

This invocation creates exactly this immutable R17 report. It creates no checker-only artifact, edits no root ledger, canonical claim, peer file, scheduler, workflow, permission, email/Drive state, purchase, or public surface.

**Net result:** G0004 is now the active R17 HARD source. The full-source metric does not move, but the first substantive run eliminates the full star class as a counterexample mechanism, proves the exact star adversary, and identifies `epsilon log(1/epsilon)` with sharp constant `1` as the unavoidable star-scale loss. The next run must leave stars and attack the general finite-graph LP/dual and extremal-graph question with methods `#11/#20/#24`.
