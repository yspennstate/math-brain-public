Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: RS-2026-CL-B remains `4/4 -> 4/4`, unchanged count `2 -> 3`; predecessor I0076 remains retired/frozen at positive-route `2/4`. Methods tried: #3 PROVE SOMETHING STRONGER, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS.**

Current owned target: Anastasia Kireeva, Randomstrasse 101, “Low-degree hardness of finding the largest clique in Erdős–Rényi graph (problems 36-38),” posted 2026-06-05, displayed unplanted clique/deficient-set inequality labeled “Conjecture 35”; canonical exclusive claim `operations/claims/RS-2026-CL-B.md`. Source status remains **REFUTED AS PRINTED by the exact `k=1` degree-zero witness; closure audits pending**.

The Burdzy–Scheutzow Problem 7.2 / I0076 predecessor is not reopened. Its six-unchanged-run CLOSABLE handoff remains controlling: OPEN / PARTIAL / RETIRED-HANDOFF, with the positive-route metric frozen at `2/4` and the continuous common-shift obstruction unresolved.

# 1. Repository, ownership, and source recovery

Before research I recovered the current campaign controls and exclusions (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`), the owner directive and implementation manifest, the canonical RS-2026-CL-B claim, the newest R15 report, recent neighbouring admission reports, and current R17 work. The canonical claim remains R15-exclusive. Repository-wide searches again found no P26 PASS/FAIL audit and no distinct second-OTHER-track PASS/FAIL audit for RS-2026-CL-B.

Fresh source check on 2026-09-17:

- live Randomstrasse source: `https://randomstrasse101.math.ethz.ch/posts/clique-low-degree/`;
- official AIM 2024 workshop report: `https://aimath.org/pastworkshops/lowdegreecomplexityrep.pdf`.

The live page still prints, with no stated `k` range and no centering, norm, equivariance, or additive normalization on `f`,

\[
\mathbb E\max_{S:\,S\text{ a }k\text{-clique}}
\langle 1_S,f(G)\rangle
\le C\,\mathbb E\max_{\substack{|S|=k,\\
|E_G(S)|\le(1-\varepsilon)\binom{k}{2}}}
\langle1_S,f(G)\rangle,
\qquad 0<C<1.
\tag{CL-B}
\]

The AIM report states a different null-optimization target: rule out degree `o(log^2 n)` polynomials that *find* a clique of size `0.9 log n`, and reports only a weaker fixed-degree symmetric correlation bound. The report also explicitly says symmetry breaking may be essential. Thus this R15 target remains the exact Randomstrasse display only; no claim is made that the broader AIM null-optimization problem is solved.

Dated bounded searches on 2026-09-17 for the exact displayed formulation, `Conjecture 35` + clique + `degree o(log n)`, and later/corrected Kireeva formulations found the same live source and no accessible source-matching correction. This is bounded negative evidence, not a novelty certificate.

# 2. Retained exact source refutation and fixed metric

The frozen source-level witness remains

\[
k_n=1,\qquad f_n(G)=\mathbf 1_n.
\]

It is degree zero. Every singleton is simultaneously a `1`-clique and a right-hand feasible set because `\binom12=0`, so both maxima are exactly `1` for every graph. Hence (CL-B) becomes `1\le C`, impossible for every allowed `0<C<1`.

The four frozen source-witness obligations remain proved:

1. `f_n` is source-admissible;
2. `deg(f_n)=0=o(log n)`;
3. both displayed maxima are well-defined and equal to `1`;
4. the display fails for every `0<C<1`.

Therefore the fixed metric remains `4/4`. The new work below is a robustness strengthening of plausible repairs, not a fifth obligation.

# 3. New theorem R15-CLB-4 — the centered normalized obstruction persists throughout the full sub-maximal clique scale `0<c<2`

The preceding run proved a centered/unit-norm obstruction only for `0<c<1`, using a greedy-clique argument. The natural question is whether that was merely an artifact of the elementary greedy threshold near `log_2 n`. It is not.

Fix constants

\[
0<c<2,\qquad 0<\varepsilon<\frac12.
\]

Along even `n`, let

\[
k_n=\lfloor c\log_2 n\rfloor,
\qquad A_n=\{1,\dots,n/2\},
\qquad B_n=[n]\setminus A_n,
\]

and define the deterministic degree-zero polynomial map

\[
f_n(G)_i=
\begin{cases}
+n^{-1/2},&i\in A_n,\\
-n^{-1/2},&i\in B_n.
\end{cases}
\tag{3.1}
\]

Pointwise,

\[
\sum_i f_n(G)_i=0,
\qquad \|f_n(G)\|_2=1,
\qquad \|f_n(G)\|_\infty=n^{-1/2},
\qquad \deg f_n=0.
\tag{3.2}
\]

Let `L_n(G)` and `R_n(G)` denote the left- and right-hand score maxima in (CL-B), taking a maximum over an empty family to be zero. More generally the conclusion below is unchanged under any empty-family convention bounded in absolute value by `O(k_n/\sqrt n)`.

Then

\[
\boxed{
\frac{\mathbb E L_n}{k_n/\sqrt n}\to1,
\qquad
\frac{\mathbb E R_n}{k_n/\sqrt n}\to1,
\qquad
\frac{\mathbb E L_n}{\mathbb E R_n}\to1.
}
\tag{R15-CLB-4}
\]

Consequently, for every fixed `0<C<1`, (CL-B) fails for all sufficiently large even `n`, despite pointwise centering, unit `L_2` norm, vanishing `L_\infty` norm, degree zero, and any logarithmic clique scale strictly below the information-theoretic maximum constant `2`.

## 3.1 Clique side: a self-contained second-moment argument

Put `N=n/2`, `k=k_n`, and let `X` be the number of `k`-cliques in the induced graph `G[A_n]\sim G(N,1/2)`. If `S,T` are independent uniformly random `k`-subsets of `[N]`, and

\[
p_j=\Pr(|S\cap T|=j),
\]

then the standard overlap decomposition gives

\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}
=
\sum_{j=0}^{k}p_j 2^{\binom j2}
=
1+\sum_{j=2}^{k}p_j\bigl(2^{\binom j2}-1\bigr).
\tag{3.3}
\]

For `j\ge2`, condition on `S`. By a union bound over the `j`-subsets of `S`,

\[
\begin{aligned}
p_j
&\le \Pr(|S\cap T|\ge j)\\
&\le \binom{k}{j}
\left(\frac{k}{N-j+1}\right)^j\\
&\le
\left(\frac{2e k^2}{jN}\right)^j
\end{aligned}
\tag{3.4}
\]

for all sufficiently large `n`, because `k=O(\log N)=o(N)`.

Write `L=\log_2 N`. Since `k=O(L)`, for all `2\le j\le k` and large `N`,

\[
\log_2\frac{2e k^2}{j}\le4\log_2 L.
\]

Hence

\[
p_j2^{\binom j2}
\le
2^{H_L(j)},
\qquad
H_L(j)=\frac{j(j-1)}2-jL+4j\log_2L.
\tag{3.5}
\]

As a function of real `j`, `H_L` is convex, so its maximum on `[2,k]` is attained at an endpoint. At the left endpoint,

\[
H_L(2)=-2L+O(\log L).
\tag{3.6}
\]

At the right endpoint, since `k/L\to c<2`,

\[
H_L(k)
=
\left(\frac{c^2}{2}-c+o(1)\right)L^2
=
-c\left(1-\frac c2+o(1)\right)L^2.
\tag{3.7}
\]

Thus for some `\eta=\eta(c)>0` and all large `N`, uniformly for `2\le j\le k`,

\[
H_L(j)\le-\eta L.
\]

Since `k=O(L)`, (3.3)--(3.5) yield

\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}=1+o(1).
\tag{3.8}
\]

Paley--Zygmund therefore gives

\[
\Pr(X>0)\to1.
\tag{3.9}
\]

Every `k`-set has score in `[-k/\sqrt n,k/\sqrt n]`, and a `k`-set contained in `A_n` has score exactly `k/\sqrt n`. Hence on `{X>0}`,

\[
L_n=\frac{k}{\sqrt n}.
\]

Using the uniform absolute bound on the score and (3.9),

\[
\frac{\mathbb E L_n}{k/\sqrt n}\to1.
\tag{3.10}
\]

## 3.2 Deficient-set side

Fix one deterministic `k`-set `S_0\subset A_n` and put

\[
m=\binom{k}{2},
\qquad
Y=|E_G(S_0)|\sim\operatorname{Bin}(m,1/2).
\]

Because `\varepsilon<1/2`, the deficient threshold `(1-\varepsilon)m` lies strictly above the mean `m/2`. Hoeffding gives

\[
\Pr\bigl(Y>(1-\varepsilon)m\bigr)
\le
\exp\{-2(1/2-\varepsilon)^2m\}
=o(1).
\tag{3.11}
\]

Therefore `S_0` is right-hand feasible with probability `1-o(1)`. On this event its score is `k/\sqrt n`, which is the largest score any `k`-set can have. Hence

\[
\frac{\mathbb E R_n}{k/\sqrt n}\to1.
\tag{3.12}
\]

Combining (3.10) and (3.12) proves R15-CLB-4. If an alternative empty-family convention has absolute value at most `M k/\sqrt n`, its contribution is confined to the `o(1)` exceptional events above and the same limits hold.

# 4. Section-B method outcomes

## #3 PROVE SOMETHING STRONGER

The a25 theorem was limited to `0<c<1` because it used the elementary greedy construction inside half the vertices. Replacing that step with the exact overlap second moment removes the algorithmic threshold and reaches every fixed `c<2`, i.e. the full constant-factor range strictly below the random-graph clique maximum.

**Outcome:** successful strengthening; no frozen source-metric movement because the exact source display was already refuted at `k=1`.

## #20 FIND WHY THE ALGORITHM FAILS

The displayed inequality is not actually testing whether `f` *finds* a clique. It asks for a support-function comparison. A graph-independent low-degree direction can therefore win simply because each feasible random family contains a set in a predetermined positive label block.

R15-CLB-4 makes the failure mechanism exact. For every `c<2`, with high probability:

- the clique polytope contains an indicator supported completely inside `A_n`;
- the deficient-set polytope contains the fixed indicator `1_{S_0}` inside the same `A_n`;
- the balanced centered direction `f_n\in\mathbf1^\perp` exposes both at the identical support value `k_n/\sqrt n`.

Thus low polynomial degree by itself cannot create a fixed multiplicative separation between these two score functionals. A repaired hardness statement needs an output-validity/rounding/calibration condition tying the polynomial to the observed graph, or another restriction of comparable force. Merely specifying logarithmic `k`, subtracting constants, centering, or normalizing `f` does not suffice.

**Outcome:** identifies the structural reason for failure rather than another isolated witness.

## #27 SWAP THE QUANTIFIERS

The strengthening may be stated uniformly at the parameter level:

\[
\boxed{
\forall c\in(0,2),\ \forall\varepsilon\in(0,1/2),\ \forall C\in(0,1),
\ \exists n_0\ \forall\text{ even }n\ge n_0:
\text{ the centered degree-zero family (3.1) violates (CL-B).}
}
\tag{4.1}
\]

This is much stronger than finding one convenient `c=0.9` instance. It shows that the obstruction persists up to every fixed fraction below the natural clique-number threshold constant `2`.

**Outcome:** successful; the obstruction is parameter-robust rather than sporadic.

# 5. Exact scope and literature boundary

Nothing here is presented as a solution of the broader AIM workshop problem. The AIM report asks to prove that no polynomial of degree `o(log^2 n)` can *find* a clique of size `0.9 log n`. It records only a weaker theorem for symmetric fixed-degree outputs with an explicit norm scale and notes that symmetry breaking may be essential. R15-CLB-4 instead says the Randomstrasse displayed **score comparison** is too weakly normalized/too detached from output validity to express that hardness goal.

The exact source refutation remains the elementary `k=1` theorem. R15-CLB-4 is evidence about what a faithful repair would have to change.

# 6. Audits, neighbouring duty, and closure state

Repository-wide searches this run found no P26 source-level audit and no distinct OTHER-track source-level audit for RS-2026-CL-B. Therefore:

- mathematical source verdict: **REFUTED AS PRINTED by owner proof**;
- frozen witness metric: **4/4**;
- independent audit count found: **0/2**;
- fleet closure status: **NOT CLOSED**;
- no paper folder is created and no audit ID is invented.

The newest visible R17 report is `runs/R17/20260917_0422Z_zfine_d4c7.md`. It explicitly labels the binary Chvátal--Sankoff problem OPEN and R17 PARTIAL while improving its deterministic upper endpoint. No source-closure package exists there, so R15's independent-audit trigger does not fire.

# 7. Three-unchanged-run threshold

This is the third consecutive RS-2026-CL-B run after the `0/4 -> 4/4` admission jump with no further fixed-metric movement:

\[
4/4\to4/4\to4/4\to4/4.
\]

Accordingly, if the required independent audits have still not appeared by the next R15 invocation, the next invocation must follow Section I as a **thinking-only stuck run** rather than add another strengthening theorem or decorative checker.

The exact blocking obligation is now operational, not mathematical:

\[
\boxed{
\text{source proof + exact self-check + prior-art log}
\quad +\quad
\text{P26 audit + one distinct OTHER-track audit}.
}
\tag{7.1}
\]

The source proof, checker, and bounded prior-art log exist; the two OTHER-task audits have not been found. This report does not simulate or substitute for them.

# 8. Model / scheduler / protected-task status

The implementation limitation is unchanged. The exposed scheduler/task surface provides prompt/title, schedule/start, timing mode, and enabled state, but no model-family selector, no reasoning-effort selector, no guaranteed hour-long execution setting, and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains a prompt request only in this run.

The historical P26 native update failure (`You cannot modify this task`) is recorded as an authorization/context boundary. The legitimate remedy is the owning authorized context, an owner/admin permission change, or platform support. Creating a duplicate task or bypassing the permission boundary is not an authorized workaround. No scheduler mutation was attempted in this run.

# 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  active_source: >-
    Anastasia Kireeva, Randomstrasse 101, 2026-06-05,
    displayed unplanted clique/deficient-set low-degree score conjecture
    (RS-2026-CL-B)
  ownership: R15_EXCLUSIVE
  predecessor:
    id: I0076
    source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.2"
    status: RETIRED_HANDOFF_OPEN_PARTIAL
    frozen_metric: "positive-route gates"
    value: "2/4"
    unchanged_count: 6
  metric: >-
    Number of four source-witness obligations proved for frozen family
    k_n=1, f_n(G)=1_n.
  before: "4/4"
  after: "4/4"
  unchanged_count_before: 2
  unchanged_count_after: 3
  status: REFUTED_AS_PRINTED_OWNER_PROOF_AUDITS_PENDING
  methods_this_run: [3, 20, 27]
  new_result:
    id: R15-CLB-4
    statement: >-
      For every fixed 0<c<2 and 0<epsilon<1/2, a deterministic centered
      unit-L2, vanishing-Linf, degree-zero balanced sign vector at
      k=floor(c log_2 n) makes both displayed expected score maxima
      asymptotic to k/sqrt(n), so their ratio tends to one.
    source_metric_movement: false
  evidence:
    claim: operations/claims/RS-2026-CL-B.md
    exact_source_refutation_report: runs/R15/20260917_0257Z_clb_constant_shift_a23.md
    intended_scale_report: runs/R15/20260917_0353Z_clb_intended_scale_a24.md
    centered_normalized_report: runs/R15/20260917_0456Z_clb_centered_normalized_a25.md
    current_report: runs/R15/20260917_0558Z_clb_subthreshold_secondmoment_a26.md
  audits_found: []
  audit_count: "0/2"
  remaining_obligation: >-
    Obtain P26 plus one distinct OTHER-track full source-claim audit.
    If absent next invocation, perform mandatory Section-I thinking-only
    stuck report; do not manufacture another theorem/checker as metric progress.
  prior_art_status: BOUNDED_SEARCH_NO_SOURCE_MATCHING_CORRECTION_FOUND_NOVELTY_UNVERIFIED
```

No new checker was created: the new result is theorem-sized and its full proof is on the page, while the finite source witness already has an executed exact self-check and the frozen metric did not move. No Gmail/email, Drive, public posting, purchase, permission change, shared-root edit, peer-file edit, workflow execution, or scheduler change was performed.
