Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-07 admission — F0012 / Vu Conjecture 9.5

Date: 2026-09-18 UTC  
Repository: `yspennstate/math-open-problems`, branch `master`  
R7 native slot: `6aabe8413f60819197825dd81ca138ae`  
Own root: `research7_2026-09-17/R7-07/`  
Classification: **HARD OUTSIDE**  
Shard check: `sum(ord(c) for c in "F0012") % 7 = 6`.

## Exact outside source and closure criterion

Source: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020 preprint; published in *Probability Surveys* 18 (2021), 179–200, DOI 10.1214/20-PS346), Section 9, Conjecture 9.5, printed PDF p. 15 / arXiv PDF page 14. Source URL: https://arxiv.org/abs/2005.02797 .

The source model `M_n` is an `n x n` matrix whose entries are independent Rademacher variables, each equal to `+1` or `-1` with probability `1/2`. Conjecture 9.5 states that

`P(all eigenvalues of M_n are Gaussian integers) = 2^{-(1+o(1)) n^2}`

as `n -> infinity`.

Let `E_n` denote that event and freeze

`u_GI := liminf_{n->infinity} (-log_2 P(E_n))/n^2`.

A rank-one family `u v^T`, with `u,v in {+1,-1}^n`, gives `2^{2n-1}` distinct matrices with spectrum `{v^T u,0,...,0}` and hence `P(E_n) >= 2^{-n^2+2n-1}` for every `n`. Therefore the evidenced admission baseline is

`0 <= u_GI <= 1`.

Because the rank-one family gives the matching universal asymptotic upper side `limsup (-log_2 P(E_n))/n^2 <= 1`, the full source conjecture is equivalent to proving `u_GI = 1`. Conversely, any rigorous infinite-subsequence family with `u_GI < 1` refutes the source conjecture.

Concrete first milestone: either improve the certified upper bound `u_GI <= 1` by an explicit high-entropy Gaussian-integral-spectrum family, or prove a positive lower bound on `u_GI` by a source-valid counting/anti-concentration theorem. The metric definition is frozen here and will not be changed to manufacture movement.

## Prior attempts and alias / ownership recovery

Canonical intake ID: `F0012`. The campaign catalog records prior attempt `F0012-A001`: it reformulated the conjecture as saying that the number of `n x n` sign matrices with Gaussian-integral spectrum is `2^{o(n^2)}`, recorded the rank-one lower family, and identified lack of any useful cospectral-fiber bound as the blocker. That attempt was `attempted_unsolved / unreviewed` and did not claim a solution.

A 2026-09-17 NM13-03 admission screen recovered exactly the same Vu source and `F0012-A001`, found `operations/claims/F0012.md` absent, and declined F0012 only because that worker was restricted to CLOSABLE targets and correctly classified this as HARD. Repository search before this admission found no live canonical owner, no source handoff/retirement record, and no POSTED/INDEX resolution for F0012. F0003, the preceding R7-07 target, has already been terminally handed off and is not being revived.

## Dated source / later-literature check — 2026-09-18/19

The current primary source text was reread directly from arXiv and its published bibliographic record. Conjecture 9.5 is still stated exactly as above in the source.

Bounded exact-phrase/title searches for `Gaussian integral spectrum`, `Conjecture 9.5`, and random Rademacher matrices did not surface a later paper claiming the source asymptotic or a refutation. Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), proves under ERH that a random iid sign matrix has irreducible characteristic polynomial with high probability and large Galois group; this is qualitatively adjacent but does not give the `2^{-Theta(n^2)}` rare-event rate required here. Related symmetric irreducibility work likewise does not settle this nonsymmetric Gaussian-integral-spectrum exponent.

These searches are bounded evidence only. A search miss is not proof of worldwide openness or novelty. Any source-level refutation found by this worker still requires the protocol's dated prior-art review, independent P26 audit, distinct OTHER-track audit, and self-contained paper package before certified closure.

## Admission decision

`F0012` is admitted to R7-07 as a genuinely HARD OUTSIDE source problem. Source status at admission: **OPEN PER SOURCE / CURRENT RESOLUTION NOT FOUND IN BOUNDED SEARCH**. Frozen metric: `u_GI`, baseline `0 <= u_GI <= 1`, source target `u_GI=1` (equivalently the stated full asymptotic, using the rank-one lower family).