Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0067 source-status reconciliation — Janson height problem is resolved

Date checked: 2026-09-18 UTC  
Slot: `R7-03 Boundary-Case Research`  
Repository: private `yspennstate/math-open-problems`, branch `master`  
Start snapshot for this run: `3eca581996fa3f970f22547c4fbd97e6970f8815`

## 1. Canonical intake scope

Canonical row `F0067` is Janson's problem on subcritical simply generated trees:

- Source: Svante Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and condensation*, Probability Surveys 9 (2012).
- Intake locator: Problem 20.7, Section 20.3, PDF p. 136 (numbering of the version used by the intake).
- Exact source-level question carried by the row: if the simply generated tree has boundary mean parameter `nu < 1`, must

  `H(T_n) / sqrt(n) -> 0` in probability?

The current intake row still records this as unverified/open and cites the 2022 universal height-width paper as only obtaining a polylogarithmically weaker statement.

## 2. Later source-matching theorem

A fresh literature check on 2026-09-18 located:

Louigi Addario-Berry and Serte Donderwinkel, **Random trees have height O(sqrt n)**, *Annals of Probability* 52(6) (2024), 2238–2280, DOI `10.1214/24-AOP1694`; arXiv `2201.11773`.

The decisive point is not a search-engine inference. In the paper itself, immediately after the subcritical Bienaymé-tree statement, the authors say that their result solves a slight variant of Janson's Problem 21.7 and then explicitly state that **they solve the problem in full; see Theorem 19**. The Problem 21.7 numbering is the published-version numbering of the same Janson problem that the campaign's source copy numbers Problem 20.7: the mathematical statement is the same `nu < 1 => H(T_n)/sqrt(n) ->_p 0` question.

Primary records checked:

- Annals of Probability publication page: https://doi.org/10.1214/24-AOP1694
- arXiv record: https://arxiv.org/abs/2201.11773

## 3. Reconciliation

Therefore the literal canonical source problem `F0067` is **KNOWN / RESOLVED_IN_LITERATURE**, not a presently open CLOSABLE candidate. R7-03 must not admit or claim it.

This corrects two stale repository surfaces without mutating them here:

1. the `F0067` intake row's `current_status: unverified`, and
2. R7-03's earlier admission screen that conservatively classified `F0067` as HARD because it had not yet recovered this 2024 theorem.

Only the coordinator should reconcile shared intake/index/queue state. This screen is immutable evidence for that future reconciliation.

## 4. Admission consequence

No target is admitted from this correction. The slot remains `PENDING_ADMISSION`; no target-specific metric or stagnation counter starts. This is positive source-matching resolution evidence, not an openness/novelty inference from a failed search.
