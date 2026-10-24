Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# R7-04 source-status correction — F0124

## Snapshot and shard gate

- Repository: private `yspennstate/math-open-problems`, branch `master`.
- Run-start captured master: `e4eb6920ab45122a2228633062148c6052600286`.
- Fresh master immediately before this screen: `42129ecfbab6960c808022996f981e87d13ed6a8`.
- Slot: `R7-04`, native ID `6aabe7ea6e1881919a65503f8445a813`.
- Entering state: `PENDING_ADMISSION` after terminal handoffs of E0010 and F0106.
- Candidate: exact canonical ID `F0124`.
- Shard arithmetic: `ord(F)+ord(0)+ord(1)+ord(2)+ord(4)=70+48+49+50+52=269`, and `269 mod 7 = 3`; hence F0124 is in the R7-04 selection shard.
- `operations/claims/F0124.md` was absent when checked. Absence of a claim does not itself justify admission; source status controls first.

## Exact outside source and literal statement

Original source:

Frank den Hollander and Jeffrey E. Steif, **“Random walk in random scenery: A survey of some recent results”**, IMS Lecture Notes–Monograph Series 48 (2006), 53–65, arXiv `math/0608219`, **Conjecture 2.16, Section 2.6, PDF p. 9**.

The canonical intake records the literal source conjecture as follows. For the one-dimensional walk with increments in `{-1,+1}`, with

`P(X_i=+1)=p`, `P(X_i=-1)=1-p`, `p in [1/2,1]`,

and the two-colour iid scenery of Section 2.6, the source conjectures:

1. for `p in [1/2,4/5)`, **every** outside configuration `(Y_n)_{n != 0}` is bad for `Y_0`;
2. for `p in (4/5,1]`, **every** outside configuration is good for `Y_0`.

The closed endpoint `p=1/2` in clause (1) is part of the literal source quantifier. This matters decisively.

## Later-author theorem and exact logical contradiction

Later paper:

Sébastien Blachère, Frank den Hollander and Jeffrey E. Steif, **“A crossover for the bad configurations of random walk in random scenery”**, *Annals of Probability* 39 (2011), no. 5, 2018–2041, DOI `10.1214/11-AOP664`, arXiv `1103.1780`.

Its theorem/abstract gives, for `epsilon=0`:

- if `p in (1/2,4/5)`, all configurations are bad;
- if `p=1/2`, **both bad and good configurations exist**;
- for `(p,epsilon)` in an open neighborhood of `(1,0)`, all configurations are good.

Therefore at the exact source endpoint `p=1/2`, the 2006 clause

`every configuration is bad`

is false. A single good configuration is enough to contradict the universal quantifier, and the 2011 theorem proves the stronger fact that the set contains both types.

Hence the literal canonical source statement F0124 is not merely “half proved/open”; it is **REFUTED IN THE LITERATURE**.

This is positive source-matching evidence from later work by the source authors, not an inference from a failed search.

## Residual problem versus canonical source

There remains mathematically interesting unresolved scope, but it is not identical to the literal F0124 statement:

- the open interval `(1/2,4/5)` on the bad side is proved by the 2011 paper;
- the endpoint `p=1/2` refutes the source’s closed-interval first clause;
- on the good side, the 2011 result proves all-good only in a neighborhood of `p=1` (at `epsilon=0`), not all of `(4/5,1]`;
- the 2011 paper formulates a broader crossover conjecture with a holding probability `epsilon in [0,1)` and crossover value `4/5`.

That residual/later conjecture may be a valid future outside target only after it receives its own exact canonical source ID/admission. R7-04 must not silently rewrite F0124 by deleting the refuted endpoint or replacing the 2006 statement with the 2011 conjecture.

## Admission verdict

**F0124: NOT ADMITTED. Literal source status = KNOWN / REFUTED_IN_LITERATURE.**

No canonical claim is created. No Section-B research triple is charged because this was a source-admission/status iteration, not research on an admitted target.

The R7-04 successor state remains `PENDING_ADMISSION`. The successor source-matching metric remains `UNKNOWN/UNMEASURED`; no target-specific stagnation count starts, and no retired predecessor metric is inherited.

## Repository-status correction identified

The intake/campaign text currently describes F0124 approximately as “half proved” and keeps the good-side residual open. That is a useful residual-status note but is logically inaccurate as the status of the **full literal source conjecture**, because the later theorem contradicts its `p=1/2` universal clause. Shared intake/INDEX/RESULTS files are coordinator-owned and were not edited by R7-04; this screen records the correction for later reconciliation.

## Sources checked 2026-09-18

- Original arXiv record `math/0608219` and canonical repository transcription of Conjecture 2.16.
- Blachère–den Hollander–Steif, arXiv `1103.1780` / *Ann. Probab.* 39 (2011), DOI `10.1214/11-AOP664`.
- Current author/publication metadata pages for both papers.

No claim of novelty is made. The literal source’s refutation is already in published literature.
