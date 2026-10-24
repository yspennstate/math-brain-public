Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: active `W_CHT: 1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; active unchanged count `4 -> 5`; the prescribed simplest-special-case recovery remains PARTIAL; methods #8 GO THE OTHER WAY AND DISCRETIZE, #10 DERANDOMIZE, #25 COUNT THE SAME THING TWICE.**

# R06 — Nielsen Theorem 4: open-neighborhood rigidity and a canonical full-Borel extension no-go

Date: 2026-09-18 UTC  
Worker: R06  
Lane: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`

## 1. Runtime truth and repository continuity

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or a guaranteed hour-long execution.

I continued from the newest complete own-track report rather than obeying the stale native title as a restart instruction:

`runs/R06/20260918T2020Z_nielsen_t4_stuck1_open_algebra_49_c3f1.md`.

That report was the mandatory first stuck/thinking recovery after three unchanged active-target runs. It selected exactly one recovery action for this invocation: **prove the simplest still-unproved special case**, namely extension of the hidden-tail probability from

\[
\mathcal A_0=\operatorname{alg}(\mathcal C\cup\{A\})
\]

to

\[
\mathfrak A_{\rm open}=\operatorname{alg}(\mathcal A_0\cup\tau),
\]

where `tau` is the topology of Cantor space. I therefore attacked that special case rather than adding another local lemma to the retired Lyons--Peres route.

Before research I reread the required current state on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/I0056.md`;
- the active exclusive claim `operations/claims/KPS-2026-NIELSEN-THEOREM4.md`;
- the preceding R06 report named above;
- the neighboring R01/KPS report `runs/R01/20260918T2000Z_kps_cor1_stuck2_zero_threshold_boundary_52b9d4e1.md`, solely to avoid duplicating its distinct Corollary-1 question.

The root R-series table is explicitly a retained/stale configuration view; the own-track immutable reports and create-only active claim control mathematical continuity.

## 2. Frozen predecessor I0056: exact source retained, no reopening

The original source is Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20. The exact source question is:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

The canonical repository claim is `operations/claims/I0056.md`, intake `I0056` in `probability_1000_intake_I_20260914/problems.jsonl`.

The frozen R06 pair is the Schlaefli `{5,5}` tessellation `H_{5,5}`, degree 5, face degree 5, with the **outer vertex boundary** normalization. Its certified result remains

\[
\Phi_V(H_{5,5})=\sqrt5,
\qquad
[L,U]=[\sqrt5,\sqrt5],
\qquad
U-L=0.
\]

This frozen subtarget is PROVED / audit-complete. The two distinct recorded outside audits remain

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / REGULAR-COREGULAR-FIRST-CLAUSE / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

The **full** Lyons--Peres Question 6.20 remains PARTIAL because its more-general transitive-plane-graph clause is not closed here. Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, explicitly settle the triangular and quadrangular regular hyperbolic cases (face degree 3 and 4); those remain prior art and are not relabelled as R06 work. A fresh 2026-09-18 source/literature check again recovered the exact Lyons--Peres wording and the Haslegrave--Panagiotis statement; nothing in this run changes I0056.

`POSTED.md` now also records *Outer Vertex-Isoperimetry of Regular Plane Tessellations* in the owner's 18 September ResearchGate snapshot. That is bibliographic state only and is not a new mathematical audit.

## 3. Active outside source and fresh status check

The active exclusive R06 successor is:

M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1, submitted 2026-09-17.

The source reopens Michael Nielsen's Theorem 4 under Nielsen's strict cylinder-positivity Assumption 1:

> There are uncountably many probability functions on the Borel subsets of Cantor space that have CHT but do not have the approximation property.

Khan--Pedersen--Stinchcombe state that the published extension proof of Theorem 4 fails and explicitly **do not decide the standalone truth** of the theorem. Their exact CHT condition is, for every Borel event `E` and threshold `delta in (0,1)`, continuity from below along the posterior first-hitting union

\[
P(O(E,\delta))=\lim_{N\to\infty}P(O_N(E,\delta)),
\]

where every finite `O_N` is clopen and `O` is open.

Fresh 2026-09-18 bounded searches used the exact arXiv ID, exact title, author names, `Nielsen Theorem 4`, `CHT`, and `approximation property`. The official arXiv record still shows only v1, dated 17 September 2026, and no later source-matching resolution surfaced. This is dated bounded negative evidence, **not** a novelty certificate and not a claim about unpublished work.

The active ownership remains create-only `operations/claims/KPS-2026-NIELSEN-THEOREM4.md`. R01 owns the distinct KPS/Nielsen Corollary-1 question and is not modified here.

## 4. Active metric

Retain

\[
D(P):=\sup_{E\in\mathcal B}\inf_{C\in\mathcal C}P(E\triangle C),
\]

and

\[
\Delta_{\rm CHT}:=
\sup\{D(P):P\text{ satisfies source positivity and CHT}\}.
\]

Always

\[
0\le \Delta_{\rm CHT}\le \frac12,
\]

so the frozen active interval remains `[0,1/2]` and

\[
\boxed{W_{\rm CHT}=\frac12.}
\]

The results below materially constrain the selected extension route but do **not** certify either a positive lower endpoint for `Delta_CHT` or a smaller upper endpoint. Therefore the source metric does not move:

`W_CHT: 1/2 -> 1/2`,

and the consecutive unchanged count is `4 -> 5`.

## 5. Idea before code

The preceding stuck report isolated the first meaningful completion layer

\[
\mathfrak A_{\rm open}
=
\operatorname{alg}(\mathcal A_0\cup\tau).
\]

The key observation is that this domain already contains **every total posterior hitting set**, because each total hitting set is open. So instead of invoking another abstract extension theorem, test what CHT itself forces on open sets before trying to extend anything.

At the symmetric hidden-tail parameter let

\[
\Omega=\{0,1\}^{\mathbb N},
\qquad Q=\text{fair-coin measure},
\]

and

\[
A=\{\omega:\omega_n=1\text{ infinitely often}\}.
\]

Then `A` and `A^c` are both dense, `Q(A)=1`, and `A^c` is countable. On

\[
\mathcal A_0=\operatorname{alg}(\mathcal C\cup\{A\})
\]

every event has the unique form

\[
E(C,D)=(A\cap C)\cup(A^c\cap D),
\qquad C,D\in\mathcal C,
\]

and the preceding report's hidden-tail probability is

\[
P_{1/2}(E(C,D))
=\frac12Q(C)+\frac12Q(D).
\tag{5.1}
\]

In particular, for every clopen `C`,

\[
P_{1/2}(C)=Q(C),
\qquad
P_{1/2}(A\cap C)=P_{1/2}(A^c\cap C)=\frac12Q(C).
\tag{5.2}
\]

The attack is therefore: assume only that an extension `P` of (5.1) to a Boolean algebra containing all opens has CHT, and squeeze the mass of a hitting open in two different ways. No code is needed because the finite core is an exact partition identity at each level `n`.

## 6. Method #8 — DISCRETIZE: CHT on this extension is exact `P(H)=Q(H)` for every generated hitting open

Let `P` be any finitely additive extension of `P_{1/2}` to a Boolean algebra containing all open subsets of `Omega`, and suppose the event `E` under consideration lies in the domain.

For fixed `E` and `delta`, let

\[
H:=O(E,\delta),
\qquad
H_N:=O_N(E,\delta).
\]

Each `H_N` is a finite union of finite-information events and hence clopen. Because `P` extends (5.1), it agrees with `Q` on every clopen. Thus

\[
P(H_N)=Q(H_N)
\qquad\text{for every }N.
\tag{6.1}
\]

The sets `H_N` increase to the open set `H`, so countable additivity of `Q` gives

\[
\lim_N Q(H_N)=Q(H).
\tag{6.2}
\]

Therefore CHT for `(E,delta)` is **equivalent in this hidden-tail extension problem** to

\[
\boxed{P(H)=Q(H).}
\tag{6.3}
\]

This is the useful finite-level reduction. The difficult condition is no longer an abstract infinite sum: for every self-generated hitting open, the extension must give exactly its fair-coin mass.

## 7. Method #25 — COUNT THE SAME THING TWICE: open-neighborhood rigidity

### Proposition 7.1 — boundary-half lower bound

Let `P` be any finitely additive extension of `P_{1/2}` to a domain containing an open set `H`.

If `A^c subset H`, then

\[
\boxed{P(H)\ge \frac{1+Q(H)}2.}
\tag{7.1}
\]

The same inequality holds if `A subset H`.

### Proof

Fix `n` and partition `Omega` into its `2^n` length-`n` cylinders. Let `K_n` be the union of those length-`n` cylinders `C` that are wholly contained in `H`.

For `C subset H`,

\[
P(H\cap C)=P(C)=Q(C).
\tag{7.2}
\]

For every other length-`n` cylinder, the assumption `A^c subset H` gives

\[
A^c\cap C\subset H\cap C.
\]

By monotonicity and (5.2),

\[
P(H\cap C)
\ge P(A^c\cap C)
=\frac12Q(C).
\tag{7.3}
\]

Finite additivity across the level-`n` cylinder partition gives

\[
\begin{aligned}
P(H)
&=\sum_{|s|=n}P(H\cap[s])\\
&\ge Q(K_n)+\frac12(1-Q(K_n))\\
&=\frac{1+Q(K_n)}2.
\end{aligned}
\tag{7.4}
\]

Because `H` is open, `K_n` increases to `H`: every `x in H` has some finite cylinder around it lying inside `H`. Countable additivity of **Q**, not of `P`, therefore yields `Q(K_n) -> Q(H)`. Taking the numerical limit in (7.4) proves (7.1).

The `A subset H` case is identical using `P(A cap C)=Q(C)/2`.  QED.

### Corollary 7.2 — any CHT hitting open containing either hidden half has full fair-coin mass

If `H=O(E,delta)` is a hitting open for which CHT holds and `A^c subset H` or `A subset H`, then by (6.3) and (7.1), with `q=Q(H)`,

\[
q=P(H)\ge\frac{1+q}{2}.
\]

Hence

\[
\boxed{Q(H)=P(H)=1.}
\tag{7.5}
\]

This already shows that CHT is extremely rigid at the dense hidden boundary: a self-generated open that captures either hidden half cannot have intermediate fair-coin mass.

### Theorem 7.3 — every open neighborhood of either hidden half must itself have P-mass one

Assume `P` extends `P_{1/2}` to a Boolean algebra containing all open sets and satisfies CHT for every event in its domain. If `G` is open and

\[
A^c\subset G,
\]

then

\[
\boxed{P(G)=1.}
\tag{7.6}
\]

The same conclusion holds for every open `G` containing `A`.

### Proof

Fix `delta in (0,1)` and let

\[
H_\delta:=O(G,\delta).
\]

Every `x in G` has a finite cylinder `[x|n]` contained in `G`, because `G` is open. On such a cylinder

\[
P_n(G)(x)=\frac{P(G\cap[x|n])}{P([x|n])}=1.
\]

Therefore `x` eventually lies in the posterior-threshold set for every `delta<1`; hence

\[
G\subset H_\delta.
\tag{7.7}
\]

In particular `A^c subset H_delta`. Corollary 7.2 and CHT give

\[
Q(H_\delta)=1.
\tag{7.8}
\]

Now perform the second exact count, this time on the disjoint first-hitting pieces `D_n(G,delta)`. For each finite `N`, on `D_n` the time-`n` posterior exceeds `delta`. Since `D_n` is a union of length-`n` cylinders and `P=Q` on cylinders,

\[
\begin{aligned}
\delta Q(D_n)
&< \int_{D_n}P_n(G)\,dQ\\
&= P(G\cap D_n).
\end{aligned}
\tag{7.9}
\]

Summing the finitely many disjoint pieces through time `N` gives

\[
\delta Q(H_N)
< P(G\cap H_N)
\le P(G).
\tag{7.10}
\]

Letting `N -> infinity` uses countable additivity only for `Q` and yields

\[
\delta Q(H_\delta)\le P(G).
\tag{7.11}
\]

Together with (7.8),

\[
P(G)\ge\delta.
\]

This holds for every `delta<1`, so `P(G)=1`. The proof for open `G superset A` is symmetric.  QED.

### Interpretation

Any CHT-preserving extension of the maximal-defect hidden-tail charge to `A_open` would have to be **maximally outer-nonregular**:

\[
P(A)=P(A^c)=\frac12,
\]

but simultaneously

\[
\boxed{
P(G)=1
\quad\text{for every open }G\supset A
\text{ and for every open }G\supset A^c.
}
\tag{7.12}
\]

Equivalently, every closed subset of either `A` or `A^c` must have `P`-mass zero. This is a strong necessary condition for the selected special case, but it is **not a contradiction under finite additivity**. Both hidden sets are dense; finite additivity permits severe failure of outer regularity. I therefore do not label (9.2) solved.

## 8. Method #10 — DERANDOMIZE: the canonical truncation-ultrafilter extension fails CHT

The preceding theorem gives a sharp test for a natural explicit extension.

For `N>=1`, define the truncation map

\[
T_N(\omega)
=(\omega_1,\ldots,\omega_N,0,0,\ldots),
\]

and the countably additive probability

\[
\nu_N:=Q\circ T_N^{-1}.
\]

Every point in the support of `nu_N` has only finitely many ones, so

\[
\nu_N(A^c)=1.
\]

Fix any free ultrafilter `U` on the positive integers and define, for every Borel `B`,

\[
\nu(B):=\lim_{N\to\mathcal U}\nu_N(B).
\tag{8.1}
\]

Ultrafilter limits preserve finite sums, so `nu` is a finitely additive Borel probability. If `C` is clopen, it is decided by finitely many coordinates and therefore

\[
\nu_N(C)=Q(C)
\]

for all sufficiently large `N`; hence

\[
\nu(C)=Q(C).
\tag{8.2}
\]

Also

\[
\nu(A^c)=1,
\qquad
\nu(A)=0.
\tag{8.3}
\]

Now set

\[
P^*:=\frac12Q+\frac12\nu.
\tag{8.4}
\]

For an `A_0` event

\[
E(C,D)=(A\cap C)\cup(A^c\cap D),
\]

we have `Q(E)=Q(C)` and `nu(E)=Q(D)`, so

\[
P^*(E(C,D))
=\frac12Q(C)+\frac12Q(D)
=P_{1/2}(E(C,D)).
\tag{8.5}
\]

Thus `P*` is a perfectly explicit full-Borel finitely additive extension of the hidden-tail charge, and it preserves strict cylinder positivity.

It nevertheless **fails CHT**.

To see this without any abstract existence theorem, enumerate the countable dense set

\[
A^c=\{z_1,z_2,\ldots\}
\]

and choose a cylinder `C_j` containing `z_j` with

\[
Q(C_j)\le 2^{-j-2}.
\]

Then

\[
G:=\bigcup_{j\ge1}C_j
\]

is open, contains `A^c`, and satisfies

\[
Q(G)\le\frac14.
\tag{8.6}
\]

Because every `nu_N` is supported on `A^c subset G`,

\[
\nu(G)=1,
\]

so

\[
P^*(G)=\frac12+\frac12Q(G)\le\frac58<1.
\tag{8.7}
\]

But Theorem 7.3 says that **every** CHT-preserving extension of `P_{1/2}` must assign mass one to every open neighborhood of `A^c`. Therefore (8.7) proves

\[
\boxed{P^*\text{ does not satisfy CHT}.}
\tag{8.8}
\]

One can expose an actual violating hitting threshold: choose any

\[
\delta\in(P^*(G),1).
\]

Because `G` is open, its hitting open `H_delta` contains `G` and hence `A^c`. If CHT held, Corollary 7.2 would force `Q(H_delta)=1`; but the finite first-hit count (7.10) would give

\[
\delta Q(H_\delta)\le P^*(G)<\delta,
\]

a contradiction.

This rules out the most canonical truncation/ultrafilter completion of the hidden-tail algebra. It is a genuine failure-mode result, not a source-level refutation.

## 9. What moved conceptually, and what did not

The prescribed recovery action was to attack the simplest special case `A_open`. It is **not yet decided**, but it is now sharply constrained:

> Any CHT extension of `P_{1/2}` from `A_0` to a domain containing all opens must assign probability one to **every** open neighborhood of `A` and of `A^c`.

This is substantially stronger than merely saying generic Horn--Tarski extensions need not preserve CHT. It gives an explicit necessary open-set boundary condition that any positive construction must meet and kills a natural full-Borel extension in closed form.

The result still does not move `Delta_CHT` because no full-Borel CHT/nonapproximation witness has been constructed, and no theorem shows that all such witnesses are impossible. The source status therefore remains **OPEN / PARTIAL**.

The strongest remaining obligation on the selected route is now:

\[
\boxed{
\text{Does there exist a finitely additive extension }
P\supset P_{1/2}
\text{ on }\mathfrak A_{\rm open}
\text{ satisfying CHT and }(7.12)?
}
\tag{9.1}
\]

A YES would keep the maximal-defect positive route alive past the first-hitting-open closure. A NO would kill this hidden-tail route at exactly the first topology-complete layer, but would still not refute Nielsen's full theorem.

No finite-arithmetic checker was created: every new claim above is an exact analytic/finite-partition argument written on the page; manufacturing a checker would not validate its infinite-domain step and would violate the research-first instruction.

## 10. Literature / failure check for this run

The current KPS primary source itself explains two relevant failures:

1. Nielsen's old proof of Theorem 4 sought nontrivial finitely additive Borel extensions agreeing with fair-coin measure on every open set. KPS prove that agreement with a regular Borel probability on all opens forces equality on all Borel events.
2. They also show Nielsen's proposed dense-set extension formula is not even well-defined: a countable dense set can be represented in two ways that the formula assigns different values.

The present R06 route deliberately does **not** impose agreement with `Q` on every open set. Theorem 7.3 instead shows that CHT itself forces a different extreme rule only on opens containing one of the two hidden dense halves. I found no exact source in the bounded current search stating this specific hidden-tail open-neighborhood rigidity theorem or the truncation-ultrafilter no-go. **Priority remains UNVERIFIED.** These are new-to-track deductions, not asserted literature-first discoveries.

## 11. Next-run rule

The active metric has now been unchanged for five consecutive R06 successor runs. Under the controlling CLOSABLE rule, one further unchanged run reaches the six-run rotation threshold. Therefore the next invocation must not drift into an indefinite sequence of extension lemmas.

If a next attack cannot move `W_CHT` away from `1/2`, it must write the required handoff/rotation record and leave this KPS/Nielsen-Theorem-4 target available for later reassignment with a fresh route.

The next three methods, if one final source-valid attack is made before that threshold is assessed, are:

- **#9 RANDOMIZE:** test whether a randomized family of dense-half completions can meet the forced rule (7.12) without collapsing to a countably additive charge;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** search finite-additive/category-measure and topological charge literature specifically for charges assigning one to every open neighborhood of two complementary dense Borel sets;
- **#29 ADD THE POINTS AT INFINITY:** pass to the Stone space of `A_open` and ask whether the two dense-half constraints force incompatible support on the remainder fibers.

These are planned attacks only; no result from them is claimed in this report.

## 12. Scheduler/model control status

The operative implementation manifest still records that the scheduler surface used for these tasks has **no model selector and no reasoning selector**, no authenticated per-run model/reasoning telemetry, and no guaranteed hour-long execution control. GPT-6 / maximum is therefore a prompt request only on that surface.

The same manifest records the historical P26 ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` in one native context. That permission boundary was not bypassed and no replacement task was created there. Root `RESULTS.md` separately records that a later authorized context successfully updated P26. The legitimate workaround is therefore an owning/admin context with permission to the task, not a worker-side permission bypass.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  active_source:
    authors: "M. Ali Khan; Arthur Paul Pedersen; Maxwell B. Stinchcombe"
    title: "Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times"
    locator: "arXiv:2609.20683v1; Nielsen Theorem 4 / Section 10"
    claim: "operations/claims/KPS-2026-NIELSEN-THEOREM4.md"
  active_target: "Nielsen Theorem 4: uncountably many source-positive Borel probability functions with CHT but without approximation"
  metric:
    name: "W_CHT = width of certified interval for Delta_CHT"
    before: "1/2"
    after: "1/2"
    movement: "none"
  status: "OPEN / PARTIAL"
  unchanged_count:
    before: 4
    after: 5
  tried_moves:
    - 8
    - 10
    - 25
  results:
    - "For hidden-tail extensions, CHT for a generated hitting open H is exactly P(H)=Q(H)."
    - "OPEN-NEIGHBORHOOD RIGIDITY: any CHT extension of P_{1/2} to a domain containing all opens must give P(G)=1 for every open G containing A or A^c."
    - "The canonical truncation-ultrafilter full-Borel extension P*=1/2 Q + 1/2 nu extends P_{1/2} but fails CHT."
  remaining_obligation: "Decide existence of a CHT extension of P_{1/2} to A_open under the forced neighborhood rule, or obtain a source-level bound moving Delta_CHT; otherwise rotate at six unchanged runs."
  evidence:
    - "runs/R06/20260918T2020Z_nielsen_t4_stuck1_open_algebra_49_c3f1.md"
    - "operations/claims/KPS-2026-NIELSEN-THEOREM4.md"
    - "https://arxiv.org/abs/2609.20683"
    - "operations/claims/I0056.md"
    - "https://www.stat.berkeley.edu/~aldous/206-SNET/Papers/lyons_peres.pdf"
    - "https://doi.org/10.1002/rsa.20946"
  audit_ids:
    active_target: []
    frozen_I0056:
      - "R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z"
      - "P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15"
  novelty: "UNVERIFIED; bounded current search only"
  frozen_predecessor:
    source: "Lyons-Peres Question 6.20 / I0056"
    pair: "H_{5,5}"
    normalization: "outer vertex boundary"
    interval: "[sqrt(5), sqrt(5)]"
    width_before: 0
    width_after: 0
    subtarget_status: "PROVED / AUDIT-COMPLETE"
    full_source_status: "PARTIAL"
```

## 14. End state

- I0056 remains frozen at width 0 and is not reopened.
- The active KPS/Nielsen-Theorem-4 metric remains `W_CHT=1/2`.
- The selected `A_open` special case is not solved, but any positive extension now has the exact forced boundary rule (7.12).
- A canonical full-Borel truncation-ultrafilter extension is ruled out by an explicit CHT contradiction.
- Active unchanged count is now 5; a sixth unchanged run triggers CLOSABLE rotation/handoff.
- No active-target audit is claimed, no checker-only artifact was manufactured, and no shared root or peer-track file was edited.
