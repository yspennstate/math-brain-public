Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no model/reasoning selector or authenticated telemetry establishing GPT-6/maximum. **NO MOVEMENT: active R19/I0110 `M_9: 9/9 -> 9/9`; unchanged count `5 -> 6`; methods #9, #13, #16; mandatory CLOSABLE rotation now triggered.**

# R19 / I0110 — mixed `p`-primary structuralization and six-run rotation handoff

Date: 2026-09-17 UTC.

Status: **PARTIAL / SOURCE OPEN / RESTRICTED STRUCTURALIZATION PROVED / SIX-RUN ROTATION / SUCCESSOR_ADMISSION_REQUIRED / AUDIT PENDING**.

## 1. Continuity: I0084 is preserved, not reopened

I began from the complete repository state rather than from the stale scheduler title. I read/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest own R19 report, the I0084 rotation handoff, the exclusive I0110 claim, the newest neighboring R20 activity, current audit searches, and the newest task-health successor screen.

R19's original Hasebe--Ueda arXiv:1710.08240v2 Conjecture 5.5 / I0084 work remains frozen at

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Preserve exactly: the arXiv-v2 source uses **ordinary classical convolution** `mu * S_t` even when `S_t` is the law of a free stable process. The retained half-stable source-case metric is `2/2`; exact ordinary-`*` closure still lacks the required P26 and a distinct OTHER-track end-to-end audit. The later ALEA free-convolution formulation and its audits do not substitute for that arXiv-v2 scope.

After six unchanged I0084 runs R19 rotated and create-only claimed Salez arXiv:2508.21055v1, Problem 2.1 / I0110. I therefore did not restart I0084.

The immediately preceding complete report is

`runs/R19/2026-09-17_08-36-42_UTC__i0110-p2-reconstruction.md`.

It proved graph-intrinsic reconstruction for the homocyclic family `(Z/p^2 Z)^d` while recording `M_9=9/9` and unchanged count five.

## 2. Source/current-literature check, dated 2026-09-17

The current Salez arXiv page still has only v1, submitted 2025-08-28. In the source HTML, lines around Problem 2.1 explicitly say that cutoff has been proved for the nine cited sparse/random-graph models, that the common mechanism has not been identified, and ask:

> Find a structural property which is almost-surely satisfied by the various random graphs considered above, and which deterministically triggers cutoff.

Thus the source is still open in the exact sense relevant to the R19 semantic gap.

Hermon--Olesker-Taylor arXiv:2102.02809 remains the relevant Abelian random-Cayley source: it establishes cutoff for finite Abelian groups in the regime `k-d(G) >> 1`, with the cutoff time governed by an entropy construction. The mixed family used below lies in that source regime when `p` is fixed, `d->infinity`, `e=O(d)`, `k=d+e+s`, `s->infinity`, and `k=O(d+e)`.

Pedrotti--Salez arXiv:2607.05345, submitted 2026-07-06, gives a powerful universal local-product/non-equilibrium cutoff criterion, but the bounded check still did not find a theorem there verifying one graph-structural property over Salez's nine cited ensembles.

Prior-art queries included `random Cayley graph unlabeled reconstruct generators 4-cycles abelian group`, `recognizing Cayley graphs abelian`, and `random Cayley graphs abelian automorphism`. They recovered general Cayley-recognition literature, including Nedela--Ponomarenko's polynomial recognition result for one abelian family, but not the exact sparse-random mixed-`p` local-four-cycle reconstruction proved below. This negative bounded search is **not** a novelty certificate.

Exact repository searches still find no completed end-to-end `P26-AUDIT-R19-I0110` and no distinct `R18-AUDIT-R19-I0110`; hits are only earlier R19 reports recording their absence. Closure therefore remains audit-pending.

## 3. Idea before code

The preceding run solved the first nested quotient family `(Z/p^2)^d`. The next genuine obstruction was not another entropy estimate; it was whether the same **unlabelled graph** can distinguish a mixed invariant-factor filtration, where some coordinates have exponent `p^2` and some only exponent `p`.

The route is:

- #9 **RANDOMIZE**: work on a high-probability clean event for iid uniform generators, rather than trying to reconstruct every pathological Cayley presentation;
- #13 **FIND WHAT ONLY INCREASES**: use the `p`-adic image filtration `G >= pG >= 0`, equivalently the monotone quotient tower as `v_p(gamma)` increases, to collapse the entire Hermon--Olesker-Taylor `gamma` hierarchy;
- #16 **COMPUTE EVERY SMALL CASE**: only after the proof route was written, exhaustively test the first mixed finite example `Z/9 x Z/3` with exact modular arithmetic.

These are the only three Section-B moves not previously used on I0110, and they differ from the preceding `#7,#8,#25` triple.

## 4. New theorem C019 — graph-intrinsic reconstruction for the first mixed invariant-factor family

Fix an odd prime `p`. Let

\[
G_{d,e}=(\mathbb Z/p^2\mathbb Z)^d\oplus(\mathbb Z/p\mathbb Z)^e,
\]

where `d->infinity`, `e=O(d)`. Put

\[
k=d+e+s_{d,e},\qquad s_{d,e}\to\infty,\qquad k=O(d+e),
\]

choose iid uniform generators `Z_1,...,Z_k in G_{d,e}`, and form the undirected Cayley graph with connection multiset `{+-Z_i}`. Forget the group labels and generator labels.

Then with probability `1-o(1)`, the **unlabelled simple graph alone** determines:

1. the `k` generator-direction classes of undirected edges;
2. the common straight-cycle length `p^2`, hence `p`;
3. the partition of vertices into the cosets of `pG` by a graph-only `p`-straight-step construction;
4. hence `|pG|=p^d`, `|G/pG|=p^{d+e}`, and therefore the invariant-factor multiplicities `d,e`;
5. the only two nonzero Hermon--Olesker-Taylor entropy clocks `t_p,t_{p^2}`, with

\[
\boxed{t_* = \max\{t_p,t_{p^2}\}}.
\]

Thus on this mixed source-admissible Abelian family, the HOT entropic clock can be reconstructed from the **unlabelled realized graph** rather than supplied through the hidden group presentation.

This is **PARTIAL** and earns no new `M_9` credit because the Abelian source family was already counted in the frozen `9/9` ELE coverage.

### Proof

Write `r=d+e`. Reduction modulo `p` identifies

\[
G/pG\cong\mathbb F_p^r.
\]

The sampled elements generate `G` iff their images span this quotient. Indeed, if `H=<Z_1,...,Z_k>` and `H+pG=G`, then the finite `p`-group `G/H` satisfies `p(G/H)=G/H`, hence is zero. Therefore

\[
\Pr(H=G)=\prod_{j=0}^{r-1}(1-p^{j-k}),
\]

and

\[
\Pr(H\neq G)\le \frac{p^{-s_{d,e}}}{p-1}=o(1).
\]

A uniform element has order below `p^2` only if its `(Z/p^2)^d` component belongs to `p(Z/p^2)^d`, whose relative size is `p^{-d}`. Hence

\[
\Pr(\exists i:\operatorname{ord}(Z_i)<p^2)\le k p^{-d}=o(1).
\]

Now exclude all nonzero relations

\[
\sum_i c_iZ_i=0,\qquad \sum_i|c_i|\le4.
\]

There are `O(k^4)` coefficient vectors. For `p>=5`, any nonzero coefficient that can occur is a unit modulo `p^2`, so conditioning on the other generators determines the remaining uniform generator uniquely, with probability `1/|G|`. For `p=3`, a relation using only a coefficient `+-3` would give `3Z_i=0`, already excluded by full order; every other relation of `l_1` norm at most four has a coefficient `+-1` or `+-2`, again a unit. Consequently the short-relation failure probability is

\[
O(k^4/|G|)=o(1).
\]

Call the conjunction of generation, full order and no short relation the clean event.

On that event, fix a vertex `x` and an incident edge `x--(x+a)`. For any other signed generator direction `b != +-a`, the two incident edges with increments `a,b` lie in the simple commuting square

\[
x,\ x+a,\ x+a+b,\ x+b,\ x.
\]

The two incident edges with increments `a,-a` cannot lie in a simple 4-cycle: such a cycle would supply signed generator increments `u,v` with

\[
2a+u+v=0,
\]

a nontrivial relation of `l_1` norm at most four; the only immediate-cancellation alternative revisits `x` and is not simple. Therefore the unique other incident edge not sharing a simple 4-cycle with `x--(x+a)` is the inverse-direction edge `x--(x-a)`. This is purely graph-theoretic.

Iterating this local pairing gives straight continuation. Every generator has order `p^2`, so every recovered straight cycle has length exactly `p^2`; the graph therefore recovers `p`.

Next generate an equivalence relation on undirected edges by (i) the local straight pairing and (ii) identifying opposite sides of every simple 4-cycle. These moves preserve the hidden generator index. Conversely, standard commuting squares translate a same-direction edge by every other sampled generator, and straight continuation translates along its own generator. Because the sampled generators generate `G`, every translate of one hidden generator edge is reached. Thus the graph-defined classes are exactly the `k` hidden generator directions.

Define `J_p` on the same vertex set by joining two vertices whenever one is obtained from the other by exactly `p` recovered straight steps in either orientation of any recovered direction. In hidden coordinates those moves are

\[
x\mapsto x\pm pZ_i.
\]

Because the `Z_i` generate `G`, the elements `pZ_i` generate `pG`. Hence the connected components of `J_p` are exactly the cosets of `pG`. For the mixed group,

\[
pG\cong(\mathbb Z/p\mathbb Z)^d,
\]

so each component has `p^d` vertices and there are `p^{d+e}` components. Since `p` is already recovered from the straight-cycle length, the unlabelled graph determines

\[
d=\log_p|pG|,\qquad e=\log_p|G/pG|-d,
\]

as well as `k` from the number of direction classes.

Finally consider the HOT integer parameter `gamma`. Because `G` has exponent `p^2`, multiplication by `gamma` has only three image types:

- if `p` does not divide `gamma`, `gamma G=G`, so the target quotient entropy is zero;
- if `v_p(gamma)=1`, `gamma G=pG`; the auxiliary walk on `Z_gamma^k` reduces deterministically modulo `p` to the auxiliary walk on `Z_p^k`, hence entropy decreases under this reduction and `t_gamma<=t_p` for the common target `log|G/pG|`;
- if `v_p(gamma)>=2`, `gamma G=0`; reduction modulo `p^2` gives `t_gamma<=t_{p^2}` for target `log|G|`. The same comparison applies to `gamma=infinity` by reduction of `Z^k` modulo `p^2`.

Since `gamma=p` and `gamma=p^2` themselves occur, the maximum is exactly

\[
t_*=\max\{t_p,t_{p^2}\}.
\]

Both target entropies and the coordinate dimension `k` are now graph-recovered. This proves C019. `square`

A fuller durable copy of this proof is preserved in

`artifacts/R19/2026-09-17_09-40-59_UTC__i0110_rotation_handoff.md`.

## 5. Exact finite self-check — method #16

Only after C019 was complete on paper I wrote and executed

`artifacts/R19/2026-09-17_09-40-59_UTC__i0110_mixed_p_primary_check.py`.

It exhaustively checks the clean mixed example

\[
G=\mathbb Z/9\mathbb Z\oplus\mathbb Z/3\mathbb Z,
\qquad
Z_1=(1,0),\ Z_2=(1,1),\ Z_3=(4,2).
\]

The exact archived output is

`artifacts/R19/2026-09-17_09-40-59_UTC__i0110_mixed_p_primary_check_output.txt`.

It records:

- 27 vertices, 81 undirected edges, degree 6;
- zero nontrivial relations of `l_1` norm at most four;
- 81 simple commuting four-cycles;
- exactly three graph-recovered direction classes, each of 27 edges;
- every straight cycle has length 9;
- `J_3` has exactly nine components, each of size 3;
- recovered `(p,d,e,k)=(3,1,1,3)`;
- final line `ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check**, not an independent audit.

## 6. Fixed metric and mandatory rotation

The fixed I0110 metric was already saturated at `M_9=9/9`. C019 strengthens the graph-intrinsic understanding of the already-counted Abelian family but does not add a tenth source family. Therefore this run honestly records

\[
\boxed{M_9:9/9\to9/9},
\]

and

\[
\boxed{\text{unchanged count}:5\to6}.
\]

Under NEW-METHODS-2026-09-16, a **CLOSABLE target rotates after six unchanged runs**. I0110 therefore leaves active R19 research now. This is operational retirement/handoff, not a claim that Salez Problem 2.1 has been solved or refuted.

I checked the latest queue/admission state before attempting any successor claim. The latest task-health screen has already assigned D0044, D0038 and D0047 to other slots and explicitly leaves a CLOSABLE successor-admission gate rather than fabricating another READY target. Earlier READY closable I0004 and I0075 now have exclusive claims. Other high-ranked candidates visible in the current screens are claimed, resolved, HARD, or PENDING. I therefore **did not promote a PENDING row, steal an owner, or narrow a HARD source to manufacture a CLOSABLE successor**.

R19's successor state is therefore

**SUCCESSOR_ADMISSION_REQUIRED**.

On the next invocation, R19 should begin by reading the newest admission/queue screen. It may create-only claim the next target only if that item has an exact outside source, current/later-literature check, no owner, and an explicit READY + CLOSABLE admission. If none exists, it should preserve the admission gate rather than restart I0110 or I0084.

## 7. Closure/audit state

No new `P26-AUDIT-R19-I0110` or distinct `R18-AUDIT-R19-I0110` was found. The source-level semantic issue therefore remains unaudited end-to-end. I0110 leaves R19 as

**PARTIAL / SOURCE OPEN / INTERNAL COMMON-CERTIFICATE METRIC 9/9 / RESTRICTED GRAPH-STRUCTURAL SPECIAL CASES PROVED / AUDIT PENDING**.

No paper folder was created because closure conditions are not met.

No shared root, peer track, scheduler, email, Drive or public-posting state was changed.

## 8. Model/scheduler control status

The operations manifest still records that the scheduler exposes prompt/title/schedule controls but **no model selector, no reasoning-effort selector, and no authenticated runtime telemetry**. Thus GPT-6/maximum remains prompt-only, and this report correctly identifies the actual visible model as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 attempt returning `You cannot modify this task` was a permissions/context boundary; later repository evidence records a successful P26 prompt update from another authorized context. The legitimate workaround is therefore an authorized scheduler context/UI/API with the necessary permission, not duplication or bypass. This run was expressly forbidden from making scheduler changes and made none.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  source: "Justin Salez, arXiv:2508.21055v1, Problem 2.1 / I0110"
  preserved_predecessor: "Hasebe-Ueda arXiv:1710.08240v2 Conjecture 5.5 / I0084; ordinary classical mu*S_t in both source branches"
  metric: "M_9 = number of nine source-cited random-graph cutoff families covered by one frozen common explicit structural cutoff-triggering property"
  before: "9/9"
  after: "9/9"
  movement: "NO MOVEMENT"
  unchanged_count_before: 5
  unchanged_count_after: 6
  status: "PARTIAL / SOURCE OPEN / SIX-RUN ROTATION / SUCCESSOR_ADMISSION_REQUIRED / AUDIT PENDING"
  tried_moves: [9, 13, 16]
  move_results:
    9: "High-probability clean-event reconstruction proved for random generators on the first mixed p-primary HOT family."
    13: "The p-adic image filtration G >= pG >= 0 collapses all HOT gamma clocks to p and p^2."
    16: "Exact exhaustive Z/9 x Z/3 graph reconstruction checker executed and archived PASS."
  new_claim: "C019 restricted mixed-p-primary graph-intrinsic reconstruction theorem"
  remaining_obligation: "I0110: one genuinely source-acceptable all-nine graph-structural property plus P26 and a distinct OTHER-track end-to-end audit. R19 rotates now and requires a new READY+CLOSABLE+UNASSIGNED successor admission."
  evidence:
    - "runs/R19/2026-09-17_08-36-42_UTC__i0110-p2-reconstruction.md"
    - "artifacts/R19/2026-09-17_09-40-59_UTC__i0110_rotation_handoff.md"
    - "artifacts/R19/2026-09-17_09-40-59_UTC__i0110_mixed_p_primary_check.py"
    - "artifacts/R19/2026-09-17_09-40-59_UTC__i0110_mixed_p_primary_check_output.txt"
  audit_ids:
    P26_AUDIT_R19_I0110: "NOT FOUND / PENDING"
    R18_AUDIT_R19_I0110: "NOT FOUND / PENDING"
  rotation: "MANDATORY at unchanged count 6; no successor claim because current admission screen supplies no lawful READY+CLOSABLE+UNASSIGNED target"
```
