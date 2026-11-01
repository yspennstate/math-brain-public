Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so GPT-6 maximum is not claimed. **NO FIXED-METRIC MOVEMENT: `alpha_univ = 1 -> 1`; G0012 unchanged count `4 -> 5`, status `OPEN_PARTIAL / PRE_ROTATION_RUN_5`. Section-B methods actually used: #3 PROVE SOMETHING STRONGER, #19 MAKE IT AN ALGORITHM, #26 HUNT THE SPORADIC CASE.**

# R01 — G0012 Alon–Peres non-backtracking birthday conjecture — two-degree factorial-switch theorem

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, exclusions, source and current status

I continued from the newest complete R01 report

`runs/R01/20260917T1057Z_g0012_stuck2_twodegree_flux_6d2f8c41.md`.

I did **not** reopen either predecessor:

- `I0024` / Aldous–Fill Open Problem 3.44 remains **PROVED / INTERNAL-CLOSED** at exact distortion `C=1`, with the right-inverse formula
  \[
  \tau_2=
  \inf_{R:\,BR=I_{\mathcal H_0}}
  \sup_{0\ne b\in\mathcal H_0}
  \frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
  \qquad R_*=CB^TL^+,
  \]
  and distinct R20/P26 PASS audits.
- `I0113` / Salez Problem 2.7 remains rotated after its six-run gate.
- `G0012` remains the exclusive active R01 successor under `operations/claims/G0012.md`.

Before research I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/RDEPLOYMENT_2026-09-16.md`, the G0012 claim, the newest own report, and the newest neighboring R02 report. The newest R02 report, `runs/R02/20260917T111610Z_7d3e91b2.md`, has rotated to I0121 (Frankl) and is explicitly `PARTIAL` with no closure-sized package, so no second-audit budget is consumed here.

### Fresh source / current-literature check — 2026-09-17

Primary source: Benjamin Dozier, *The Birthday Paradox for non-backtracking walks on regular graphs*, arXiv:2608.26321, submitted 2026-08-26, Conjecture 1.5 (Alon–Peres). The source still asks for a universal square-root birthday bound over **all simple graphs of minimum degree at least 3**, while the paper proves the fixed-degree regular case.

Fresh bounded queries also rechecked Ferenc Bencs, Leslie Ann Goldberg, Matthew Jenssen, Mark Jerrum, Gabor Pete, Guus Regts and Yitong Yin, *On the self-intersection time of non-backtracking random walks*, arXiv:2608.09729, submitted 2026-08-10. Their source-matching established results remain `O_Delta(sqrt(n) log n)` for fixed maximum degree and `O(sqrt(n))` for regular uniform expanders, not the unrestricted minimum-degree-only conjecture. Noga Alon's older draft was also surfaced and does not settle the unrestricted source. No later source-matching resolution surfaced in the bounded search. This is **not** a novelty certificate.

Queries used included exact title/arXiv searches for `2608.26321`, `2608.09729`, `Alon Peres non-backtracking birthday conjecture 2026`, and the current source title plus `citations follow-up`.

### Frozen metric

`alpha_univ` remains the smallest exponent proved on the **full** source domain.

- before: `1`;
- after: `1`.

The theorem below strictly strengthens the previous `{3,D}` partial result and removes the special degree `3`, but it still assumes only two degree values and therefore does not move the frozen unrestricted metric.

---

## 2. Inputs retained from the preceding reports

I use two results already proved on the R01 chain and do not re-derive their full plan-switching proofs.

### Input A — uniform regular birthday bound

For every simple `r`-regular graph on `N` vertices, every `r>=3`, every starting oriented edge and every `ell>=1`,

\[
\Pr(\hbox{length-}\ell\hbox{ NBW is simple})
\le 4800\,\frac{N}{\ell^2}.
\tag{2.1}
\]

The corrected heat-bath / global-averaging proof is in

- `runs/R01/20260917T0802Z_g0012_biregular_heatbath_7b4e2c19.md`, and
- `artifacts/R01/20260917T0802Z_g0012_global_averaging_correction.md`,

with the uniform-in-degree regular corollary recorded explicitly in the `1057Z` report.

### Input B — same-degree segment completion

If a segment of the original NBW makes `ell` consecutive transitions through vertices all having the same **original** graph degree `r`, then, conditional on the entire past up to the segment start,

\[
\Pr(\hbox{that segment stays in degree }r\hbox{ and is internally simple}\mid\mathcal F_{\rm start})
\le 19200\,\frac n{\ell^2}.
\tag{2.2}
\]

Reason: the degree-`r` induced graph embeds as an induced subgraph of an `r`-regular graph on at most `4n` vertices by the classical Erdos–Kelly regular-completion criterion, and every specified same-degree continuation keeps the exact transition factor `1/(r-1)`. Equation (2.1) then gives (2.2).

The previous report used (2.2) with a union bound over homogeneous blocks and paid a cubic factor `(s+1)^3`. Method #19 below removes one full factor.

---

## 3. Method #3 — PROVE SOMETHING STRONGER: an adaptive factorial tail for degree-cut crossings

The preceding `{3,D}` argument used only Markov's inequality for the number of high-to-low switches. There is a much stronger statement because, on the event of simplicity, every vertex is queried at most once.

Let an arbitrary simple graph be partitioned into two vertex sets `U` and `W`. For `w in W`, let

\[
c(w)=|N(w)\cap U|,
\qquad
q(w)=\frac{c(w)}{d(w)-1}.
\tag{3.1}
\]

Let `Y` be the number of transitions `W -> U` made by the length-`k` NBW, and let `E` be the event that the whole walk is simple. Put

\[
Q:=\sum_{w\in W}q(w).
\tag{3.2}
\]

### Lemma 3.1 — adaptive factorial crossing bound

For every integer `r>=1`,

\[
\boxed{
\Pr(E\ \hbox{and}\ Y\ge r)
\le e_r\bigl((q(w))_{w\in W}\bigr)
\le \frac{Q^r}{r!}.
}
\tag{3.3}
\]

Here `e_r` is the `r`-th elementary symmetric polynomial.

### Proof

Fix an `r`-element set `F subset W`. I first prove

\[
\Pr(E\ \hbox{and every }w\in F\hbox{ is exited toward }U)
\le \prod_{w\in F}q(w).
\tag{3.4}
\]

Proceed by induction on `|F|`. The claim is trivial for the empty set. For nonempty `F`, expose the walk until the first hit of a vertex of `F`, if any. Suppose this first hit is `w`. Conditional on the complete history through arrival at `w`, at most `c(w)` of the `d(w)-1` allowed non-backtracking exits go to `U` (if the predecessor lies in `U`, there are actually only `c(w)-1`, so this is an upper bound). Thus the conditional chance of the required exit is at most `q(w)`. After that step, on `E` the vertex `w` can never be queried again, and the induction hypothesis applies uniformly to `F\setminus{w}` from the new history. Partitioning according to which member of `F` is first hit gives (3.4), since the probabilities of the mutually exclusive first-hit alternatives sum to at most one.

On `E`, every successful `W->U` exit occurs at a distinct vertex of `W`. Therefore

\[
\binom Yr\mathbf 1_E
=
\sum_{\substack{F\subset W\\|F|=r}}
\mathbf 1_{\{E\ \text{and every }w\in F\text{ is a }W\to U\text{ exit}\}}.
\]

Take expectations, use (3.4), and then use `1_{Y>=r} <= binom(Y,r)`:

\[
\Pr(E,Y\ge r)
\le
\mathbb E\left[\binom Yr\mathbf 1_E\right]
\le e_r(q)
\le \frac{(\sum_w q(w))^r}{r!}.
\]

This proves (3.3). ∎

**Why this is useful.** It is an adaptive Poisson-binomial bound: the vertices actually encountered are chosen by the walk itself, but simplicity prevents repeat queries, so no independence assumption or unjustified Chernoff bound is needed. The preceding report's first-moment estimate `Q/r` is replaced by the factorial tail `Q^r/r!`.

---

## 4. Method #19 — MAKE IT AN ALGORITHM: random-time block selection removes the block union bound

The previous few-switch proof located a longest homogeneous block and union-bounded over its possible block index. A randomized selection rule avoids that loss.

Let `S` be the number of **degree changes** along the path:

\[
S=|\{0\le t<k:d(X_t)\ne d(X_{t+1})\}|.
\tag{4.1}
\]

Fix an integer `s>=0` and assume

\[
k\ge 8(s+1).
\tag{4.2}
\]

Set

\[
\ell=\left\lfloor\frac{k}{4(s+1)}\right\rfloor.
\tag{4.3}
\]

After the NBW is sampled, independently choose

\[
J\sim\mathrm{Unif}\{0,1,\ldots,k-\ell\}.
\]

Call `J` **clean** when the `ell` transitions starting at `J` contain no degree change.

If `S<=s`, each degree-change edge spoils at most `ell` possible values of `J`. Hence at most `s ell < k/4` starts are spoiled. Since

\[
k-\ell+1\ge 3k/4,
\]

the conditional clean probability is at least `2/3`.

Let again `E` denote whole-path simplicity. Then

\[
\frac23\Pr(E,S\le s)
\le \Pr(E,S\le s,J\text{ clean}).
\tag{4.4}
\]

For each fixed `J=j`, on the event on the right the next `ell` transitions stay in one exact degree class and are internally simple. Conditional on the history through time `j`, (2.2) gives an upper bound `19200 n/ell^2`, uniformly in the history and in that degree. Averaging over `J`,

\[
\Pr(E,S\le s,J\text{ clean})
\le 19200\,\frac n{\ell^2}.
\]

Finally, (4.2) implies

\[
\ell\ge \frac{k}{8(s+1)}.
\]

Therefore:

### Lemma 4.1 — quadratic switch-budget bound

\[
\boxed{
\Pr(E,S\le s)
\le 1{,}843{,}200\,\frac{n(s+1)^2}{k^2}.
}
\tag{4.5}
\]

This is a genuine improvement over the previous `76800 n(s+1)^3/k^2` route: the exponent of the switch budget drops from `3` to `2`. The large numerical constant is intentionally loose; optimizing it has no value for the source question.

The algorithmic content is explicit: choose a random time rather than guess the longest block. If the path has few degree changes, a constant fraction of random times expose a long homogeneous window, and one invokes the regular completion theorem only there.

---

## 5. Combined theorem for every two-degree graph

Now assume the graph has exactly two possible degrees

\[
3\le a<b,
\]

with no bipartiteness, expansion, placement, or bounded-degree assumption. Write

\[
L=\{v:d(v)=a\},
\qquad
H=\{v:d(v)=b\},
\qquad
B=e(L,H),
\tag{5.1}
\]

and define the normalized high-to-low cross flux

\[
A:=\frac{B}{b-1}.
\tag{5.2}
\]

Let `Y` be the number of `H->L` transitions. Along a two-symbol degree word the numbers of `H->L` and `L->H` switches differ by at most one, so

\[
S\le 2Y+1.
\tag{5.3}
\]

Consequently, if `S>s`, then

\[
Y\ge r:=\left\lceil\frac s2\right\rceil.
\tag{5.4}
\]

For `h in H`, equation (3.1) gives `q(h)=c(h)/(b-1)`, and summing cross-degrees over `H` gives exactly

\[
Q=\sum_{h\in H}q(h)=\frac{B}{b-1}=A.
\tag{5.5}
\]

Combining Lemma 3.1 and Lemma 4.1 yields the new theorem.

### Theorem 5.1 — two-degree factorial-switch birthday bound

For every simple `n`-vertex graph whose degree set is contained in `{a,b}` with `3<=a<b`, every starting oriented edge, every integer `s>=1`, and every `k>=8(s+1)`, if `E` is the event that the length-`k` NBW is simple, then

\[
\boxed{
\Pr(E)
\le
1{,}843{,}200\,\frac{n(s+1)^2}{k^2}
+
\frac{A^r}{r!},
\qquad
A=\frac{e(V_a,V_b)}{b-1},
\quad
r=\left\lceil\frac s2\right\rceil.
}
\tag{5.6}
\]

### Proof

Split according to `S<=s` and `S>s`. The first event is bounded by (4.5). On the second event, (5.4) gives `Y>=r`, and Lemma 3.1 with the partition `U=L`, `W=H` and (5.5) gives

\[
\Pr(E,S>s)
\le \Pr(E,Y\ge r)
\le \frac{A^r}{r!}.
\]

Add the two bounds. ∎

### Corollary 5.2 — full square-root birthday law for bounded normalized cross flux

Fix `A_0<infinity`. Uniformly over **all** two-degree graphs as above satisfying

\[
\frac{e(V_a,V_b)}{b-1}\le A_0,
\tag{5.7}
\]

the Alon–Peres square-root conclusion holds: for every `epsilon>0` there is `C=C(epsilon,A_0)` such that

\[
k>C\sqrt n
\quad\Longrightarrow\quad
\Pr(E)<\epsilon.
\tag{5.8}
\]

Indeed, first choose the constant `s` so that `A_0^{ceil(s/2)}/ceil(s/2)!<epsilon/2`, then choose `C` so that the first term of (5.6) is `<epsilon/2`; for sufficiently large `n`, (4.2) is automatic.

This strictly generalizes the preceding `{3,D}` bounded-flux theorem:

- the low degree need not be `3`;
- both degree values may grow with `n`;
- no bipartiteness or regularity inside either degree class is assumed;
- the switch tail is factorial rather than first-moment;
- the few-switch loss is quadratic rather than cubic.

It is still **PARTIAL** because the source allows arbitrarily many degree values and because even in the two-degree case `A` can diverge.

No publication-priority claim is made. The bounded current search was source/status oriented, not an exhaustive novelty search for (5.6).

---

## 6. Method #26 — HUNT THE SPORADIC CASE: why the obvious simple-graph analogue of the multigraph drift obstruction cannot persist

The hardest-looking counterexample mechanism is a long directed corridor: at each stage the NBW should have a strong probability of continuing forward, as parallel-edge multigraphs can arrange. I tested the simplest **simple-graph** realization and found an exact volume-growth obstruction.

Consider alternating layers

\[
H_0,L_0,H_1,L_1,\ldots,H_r,
\]

where every connector in `L_i` has exactly one neighbor in `H_i` and exactly two neighbors in `H_{i+1}` (so the connector degree is `3`). Suppose every vertex of an interior high layer `H_i` has `b_i` neighbors in `L_{i-1}` and `f_i` neighbors in `L_i`, with

\[
D_i=b_i+f_i.
\]

Incidence counting gives

\[
|L_i|=f_i|H_i|,
\qquad
2|L_{i-1}|=b_i|H_i|,
\]

hence

\[
\boxed{
\frac{|L_i|}{|L_{i-1}|}=\frac{2f_i}{b_i}.
}
\tag{6.1}
\]

Now suppose the NBW enters `H_i` from `L_{i-1}` and has conditional probability at least `p>1/2` of exiting forward to `L_i`. Since one backward edge is excluded by non-backtracking,

\[
\frac{f_i}{D_i-1}\ge p.
\tag{6.2}
\]

Thus

\[
f_i\ge p(D_i-1),
\qquad
b_i=D_i-f_i\le (1-p)(D_i-1)+1,
\]

and (6.1) yields

\[
\boxed{
\frac{|L_i|}{|L_{i-1}|}
\ge
\frac{2p(D_i-1)}{(1-p)(D_i-1)+1}
>1
\qquad(D_i\ge3,\ p>1/2).
}
\tag{6.3}
\]

If `D_i>=D_*>=3` throughout, the right side is bounded below by a constant `lambda(p,D_*)>1`, so

\[
|L_j|\ge \lambda^j|L_0|.
\]

Therefore an `n`-vertex graph of this layered type can sustain such fixed forward bias for only

\[
O_{p,D_*}(\log n)
\]

layers.

**Interpretation.** A long simple-graph corridor cannot imitate a parallel-edge drift simply by replacing multiplicity with degree-3 one-to-two connector gadgets: edge-incidence conservation forces exponential layer growth. This does not prove the conjecture; it eliminates one natural sporadic counterexample architecture and points toward an incidence-flux invariant as the correct global replacement for the failed `2m/W` packing.

---

## 7. What actually remains

The exact unresolved source statement is still the full minimum-degree-3 conjecture, and the frozen metric remains `alpha_univ=1`.

The strongest obstruction is now more specific than “unbounded degree” or even “two degree scales.” We can handle:

1. every regular degree uniformly;
2. bipartite biregular graphs with arbitrary degree ratio;
3. arbitrary two-degree graphs whenever `e(V_a,V_b)/(b-1)` is bounded;
4. few degree changes with a quadratic switch-budget loss;
5. adaptive directional cut crossings with a factorial tail;
6. the most direct layered simple-graph imitation of persistent multigraph drift, which is killed by exponential volume growth.

What is still missing is a **global many-scale incidence theorem**: if a simple NBW keeps changing among many degree scales often enough to defeat the random-time homogeneous-block bound, either those changes must force a source-time collision, or their incidence structure must force expansion/volume growth that cannot persist for `sqrt(n)` steps.

A useful next theorem would combine the marked two-path tail-swap identity from the previous run with the incidence-growth calculation above. The intended statement is a packing-or-overlap dichotomy for deviation trajectories:

> either many deviation continuations consume essentially disjoint vertex mass, giving an `n`-scale packing directly, or many continuations overlap at high-degree vertices, in which case a marker-preserving two-path switch converts overlap into a collision-producing deviation without a degree-ratio loss.

That is the missing ingredient no route has yet supplied.

Because this is unchanged run **5**, the next complete no-movement invocation is the six-run CLOSABLE gate. If `alpha_univ` is still `1` then, the track must preserve a full G0012 handoff and rotate instead of producing a seventh unchanged attack.

Recommended next methods, not repeating this run: **#9 RANDOMIZE** the deviation-pair sampling, **#12 FIND WHAT IS CONSERVED** in incidence flux under tail swapping, and **#29 ADD THE POINTS AT INFINITY** by compactifying the degree profile into normalized incidence measures to isolate an extremal obstruction.

---

## 8. Validation / checker decision

No finite claim was introduced, so no exact-arithmetic checker was manufactured. The new claims are analytic and their proofs are written on the page. This is deliberate under the 90/10 rule.

Self-checks performed in the proof:

- the adaptive crossing lemma does not assume independence;
- the predecessor being in the opposite side only **reduces** the available cross exits, so `q(w)` is a valid upper bound;
- on a simple path each vertex contributes at most one successful cut exit;
- the degree-switch identity `S<=2Y+1` is exact for a two-symbol word;
- the random-window argument counts at most `ell` spoiled starts per switch and uses a history-uniform conditional segment bound;
- the layered incidence formulas count the same cross edges from both sides.

No closure label, source refutation, or unrestricted metric improvement is claimed.

---

## 9. Model / scheduler control reality

The newest R-series deployment manifest `operations/RDEPLOYMENT_2026-09-16.md` records that R01 itself received a successful native prompt/schedule update, but the available scheduler still exposes **no model selector and no reasoning-effort selector** and gives no verified full-hour guarantee. Thus GPT-6 / maximum is genuinely installed only as prompt text, not as an enforceable verified runtime setting.

The historical P26 response `You cannot modify this task` was context-specific: the root reconciliation later records a separate authorized P/C context in which P26 updates succeeded. The lawful workaround for a task that rejects modification is therefore the authorized owning context/workspace or platform support / ownership migration. Creating a duplicate task or bypassing permissions is not an acceptable workaround.

Actually enforcing GPT-6 / maximum would require the product task surface to expose model and reasoning fields (plus authenticated completed-run telemetry), or an authorized migration to a surface that does.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  lane: CLOSABLE_OUTSIDE
  predecessor:
    target: I0024
    state: PROVED_INTERNAL_CLOSED
    metric: C=1
    reopened: false
  active:
    target: G0012
    source: "Benjamin Dozier (2026), arXiv:2608.26321, Conjecture 1.5 (Alon-Peres)"
    claim: operations/claims/G0012.md
    metric_name: alpha_univ
    metric_before: 1
    metric_after: 1
    movement: NO_MOVEMENT
    unchanged_count_before: 4
    unchanged_count_after: 5
    status: OPEN_PARTIAL_PRE_ROTATION
  methods_used: [3, 19, 26]
  new_results:
    - "Adaptive cut-crossing factorial tail: P(simple and Y>=r) <= Q^r/r!."
    - "Random-time homogeneous-block lemma: P(simple and S<=s) <= 1843200 n(s+1)^2/k^2."
    - "Two-degree theorem: P(simple) <= 1843200 n(s+1)^2/k^2 + A^ceil(s/2)/ceil(s/2)!, A=e(V_a,V_b)/(b-1)."
    - "Bounded normalized cross flux gives the full sqrt(n) birthday scale uniformly over all two-degree graphs."
    - "Layered 3-connector persistent-forward-bias gadget forces exponential layer growth."
  remaining_obligation: "Prove a source-domain many-scale incidence packing-or-overlap theorem, ideally by marker-preserving two-path switching; otherwise preserve a full G0012 handoff and rotate at the sixth unchanged run."
  checker_created: false
  audit_ids: []
  neighboring_audit: "not requested; newest R02/I0121 package is PARTIAL"
  evidence:
    - operations/claims/G0012.md
    - runs/R01/20260917T0802Z_g0012_biregular_heatbath_7b4e2c19.md
    - artifacts/R01/20260917T0802Z_g0012_global_averaging_correction.md
    - runs/R01/20260917T1057Z_g0012_stuck2_twodegree_flux_6d2f8c41.md
    - runs/R02/20260917T111610Z_7d3e91b2.md
```

## 11. Boundary audit

One immutable R01 report only. No shared-root edit, no peer-track edit, no email, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, or force-push.