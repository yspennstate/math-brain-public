Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-02 — Tier-3 shard-1 source gate: P0367

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Slot / native ID: `R7-02` / `6aabe797a39081919acc889f29f4c556`  
Own root: `research7_2026-09-17/R7-02/`  
Run-start captured master: `19d26f22ae96e542ed09a2bdeb46d4700724f8e3`  
Pre-write master recheck: `1ee0b41f63f07a1e5e2d29801dd074cb77ae19bf`  
Entering state: `PENDING_ADMISSION` after terminal P0169 handoff and the P0358 source-gate rejection.

## 1. Continuity and why this candidate is new work

I reread/recovered the controlling owner directive, `operations/VISIBLE_FLEET_2026-09-16.md`, the R7 native registry, root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md` and `RANKING.md`, the latest own R7-02 report, the prior post-P0169 shard screen, relevant Codex/intake rows, canonical claim locations, and useful neighboring frozen-percolation source checks.

The previous own run screened `P0358` in detail and rejected it because the source asks for a theorem-sized infinite-ray asymptotic constant under the full branching-random-walk hypotheses, not an honest finite-certificate endpoint. That report also noted that nearby `P0360` is an unrestricted frozen-percolation uniqueness implication and is HARD-shaped. This invocation therefore advances the Tier-3 shard-1 cursor to the next narrower unclaimed row, `P0367`, instead of repeating P0358/P0360 prose.

The exact owner partition is satisfied:

`sum(ord(c) for c in "P0367") = 288`, hence `288 mod 7 = 1`.

## 2. Original outside source and exact source scope recovered

Canonical intake ID: **P0367**  
Canonical title: **Support of the conditional burning-time law**.

Outside source recovered from the validated campaign source metadata and current repository literature screens:

- Authors: Balázs Ráth, Jan M. Swart, Tamás Terpai.
- Title: *Frozen percolation on the binary tree is nonendogenous*.
- Journal: *Annals of Probability* 49(5) (2021), 2272–2316.
- arXiv: `1910.09213`.
- DOI: `10.1214/21-AOP1507`.
- Primary URL recorded in repository evidence: `https://arxiv.org/abs/1910.09213`.
- Exact locator: **Question 6, PDF p. 15**.

The campaign's source-faithful statement is:

> Is the conditional law of the root burning time, given all activation times, supported on the entire interval allowed above the ordinary percolation time `X'`, including the never-burning state?

The retained source caveat is essential: the state space is `[0,1] union {infinity}`. The question is not refuted by pretending that there are ordinary real times strictly between `1` and `infinity`.

The historical source status is source-open. The campaign status remains `current-literature: unverified`, not a current-openness certificate.

## 3. Prior attempt and later-author/follow-up evidence

The existing campaign attempt is substantive but partial. For a Borel set `A`, write

`q_A(U) = P(X_root in A | U)`,

where `U` denotes the full activation-time field. A conditionally independent replica yields

`E[q_A(U)^2] = P(X_root in A, X'_root in A)`

for the relevant bivariate coupling. Therefore Cauchy–Schwarz gives

`P(q_A(U) > 0) >= P(X_root in A)^2 / E[q_A(U)^2]`

whenever the denominator is nonzero. This is a positive-probability support statement for a fixed set `A`; it does **not** show that `q_A(U)>0` for almost every admissible activation field.

Repository literature evidence also records the later Ráth–Swart–Szőke paper *A phase transition between endogeny and nonendogeny* (arXiv:2103.14408; EJP), which studies a structured family of freezing-time sets and proves an endogeny/nonendogeny phase transition. Current neighboring source checks do not record that paper as settling Question 6's full conditional-support assertion.

A fresh 2026-09-19 GitHub-only exact-title / Question-6 / conditional-support search did not surface a later repository record of a source-matching resolution. This is bounded negative evidence only. It is **not** proof of worldwide openness, novelty, or priority.

## 4. Ownership / exclusion gate

Immediately before this screen, direct fetch of `operations/claims/P0367.md` at the captured master returned 404. Repository search exposed the campaign source/attempt records but no canonical P0367 claim, no POSTED entry, and no campaign PROVED/REFUTED/KNOWN promotion for this exact source question.

That removes an ownership conflict, but it does **not** by itself make P0367 admissible: source shape and current-status gates remain independent requirements.

## 5. Source-shape analysis: why P0367 is not an honest CLOSABLE finite-certificate target

Let `K_U` denote a regular conditional distribution of the root burning time given the full activation field `U`, and let `x'(U)` be the ordinary percolation lower endpoint from the source.

For the finite part of the state space, full support can be reduced to a countable base: for every rational interval `(a,b)` with `0<a<b<=1`, whenever `(a,b)` meets the allowed interval above `x'(U)` (in particular on `x'(U)<b`), one must have

`K_U((a,b)) > 0`

for almost every admissible `U`. The source additionally asks that the never-burning point `infinity` belong to the conditional support, i.e. the corresponding conditional mass/support clause must also hold in the source topology.

This reformulation exposes the real quantifier burden. The target is not one scalar evaluation or one finite truth table. It is an almost-sure **pointwise-in-environment conditional-support theorem** across a countable family of intervals, with the conditioning sigma-field generated by the entire infinite activation field.

The old second-moment computation does not bridge that quantifier gap. For a fixed interval `I`, knowing

`P(K_U(I)>0) > 0`

is compatible with a positive-measure set of activation fields on which `K_U(I)=0`. Even a very good global lower bound on `E K_U(I)` or `E K_U(I)^2` cannot by itself rule out conditional gaps almost surely.

A genuine source-level **refutation** would need an explicit interval `I` and a rigorously positive-probability activation-field event `E` on which `K_U(I)=0` (or an analogous failure at the never-burning state). A genuine **proof** would need to exclude every such random gap for almost every `U`, simultaneously over a countable basis. The existing repository attempt has neither mechanism.

This also explains why manufacturing a finite checker here would be methodologically wrong. A finite-depth activation prefix does not, by itself, certify the conditional support of the root burning time in the infinite frozen-percolation process; the campaign's nearby frozen-percolation work explicitly records nonlocal influence from arbitrarily deep subtrees as a core obstruction.

Therefore P0367 is narrower than P0368's global fixed-point classification, but it is still an infinite conditional-law theorem, not the exact finite certificate/construction/counterexample endpoint that R7-02 is required to prioritize.

## 6. Admission decision

**Decision: DO NOT ADMIT P0367.**

Disposition:

`SHARD_PASS / OWNERSHIP_LOOKS_FREE / HISTORICALLY_SOURCE_OPEN / CURRENT_OPENNESS_UNVERIFIED / CLOSABLE_GATE_FAIL__INFINITE_CONDITIONAL_SUPPORT_THEOREM`.

No `operations/claims/P0367.md` is created. No successor metric is frozen, because doing so would encourage an artificial finite surrogate rather than preserve the source's almost-sure full-support quantifiers.

Successor state remains:

- target: `NONE / PENDING_ADMISSION`;
- metric before: `UNKNOWN/UNMEASURED`;
- metric after: `UNKNOWN/UNMEASURED`;
- successor stagnation: `NOT_STARTED`;
- stuck recoveries: `0`.

No Section-B method is charged. B2/B16/B19 remain `NOT_TRIED` for the first actually admitted successor.

## 7. Durable cursor and next lawful work

Durable cursor after this screen:

`POST_P0169_TIER3_SHARD1_P0367_SCREENED_REJECTED`.

Do not repeat P0358, P0360, or P0367 absent a material source/status/ownership change. Continue forward through exact shard-1 Tier-3 rows, prioritizing rows whose literal source statement can terminate in a finite witness, exact construction, finite obstruction, or sharp source constant. The next admission must still pass current-source/literature, prior-attempt, ownership, POSTED/KNOWN/resolved, and route-retirement gates before any claim is created.

No email/Gmail, Drive, public posting, third-party contact, paid compute, credential/access/settings change, workflow execution, force push, schedule modification, shared-root edit, or peer-file edit was performed.