Model actually running for this admission: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-07 admission — F0003 / sharp singularity exponent for fixed-degree random regular graphs

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
R7-07 native ID: `6aabe8413f60819197825dd81ca138ae`.  
Own root: `research7_2026-09-17/R7-07/`.  
Shard check: `sum(ord(c) for c in "F0003") % 7 == 6`.

## Outside source and exact endpoint

Van Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020; later Probability Surveys publication), Section 5 "Random regular graphs", immediately after Theorem 5.2. Primary source URL: https://arxiv.org/abs/2005.02797 .

For the uniformly random simple fixed-`d` regular graph `G_{n,d}`, `d >= 3`, with adjacency matrix `A_{n,d}`, Vu records Huang's polynomial estimate

`P(A_{n,d} singular) <= n^{-c_d}`

with `c_d = min{1/8,(d-2)/(5d-6)}`, notes the lower bound `P(A_{n,d} singular) >= n^{-d+2}` coming from local singularity mechanisms, and asks for the **sharp value of the exponent**.

The source-level closure criterion used by this worker is therefore:

> for every fixed integer `d>=3`, prove the logarithmic asymptotic exponent
> `-log P(A_{n,d} singular)/log n -> d-2`, equivalently the matching upper bound
> `P(A_{n,d} singular) <= n^{-d+2+o(1)}` together with the already known source lower-bound scale.

I will not silently replace this by mere nonsingularity, a directed model, a fixed finite support classification, or one value of `d`.

## Classification and milestone

Classification: **HARD OUTSIDE**. This is an asymptotic random-matrix problem; it is not called CLOSABLE merely because local mechanisms can be enumerated.

Concrete first milestone: settle the first unresolved degree `d=3` at the exponent level, i.e. prove the upper bound `P(A_{n,3} singular) <= n^{-1+o(1)}`. Before that, isolate rigorously which singularity mechanisms can contribute on the `n^{-1}` scale.

## Frozen mathematical metric

Define

`a_3 := sup{ a >= 0 : P(A_{n,3} singular) <= n^{-a+o(1)} }`.

Source closure at `d=3` requires `a_3=1`; full source closure requires the analogous value `a_d=d-2` for every fixed `d>=3`.

Evidenced admission baseline: **`a_3 >= 1/9`**, from Huang's source-cited exponent `min{1/8,(d-2)/(5d-6)}` evaluated at `d=3`. I do not promote the 2024 Nguyen–Pan directed-model `1/3+o(1)` estimate to the undirected metric without a source-exact transfer proof.

This metric is frozen for R7-07 while F0003 is active. Restricted structural theorems do not count as movement unless they improve this source-matching exponent bound.

## Prior attempts and alias/ownership recovery

Canonical intake: `probability_1000_intake_F_20260908/problems.jsonl`, row `F0003`. Prior attempt `F0003-A001` identifies twin vertices as the source lower-bound mechanism and reduces the conjectural picture to showing that other bounded or global kernel structures are negligible. Its global anti-concentration step remains open. The attempt's heuristic bounded-support discussion is not treated as a theorem unless re-proved here.

A 2026-09-17 R15 successor screen (`runs/R15/20260917_2306Z_successor_admission_f0016_f0003_f0005_m42c.md`) classified F0003 as HARD and declined it only because R15 required a CLOSABLE successor; it did not create an F0003 claim. That screen is not ownership.

Immediately before this admission write, a direct fetch of `operations/claims/F0003.md` on fresh master `57789c27bf03b4d80f291553dc178f1760ae7a6b` returned 404. Repository search found intake work and screens but no competing canonical claim. A fresh-master recheck is still required immediately before claim creation.

## Dated source/current-literature check — 2026-09-18

Primary-source text was checked directly on arXiv: Vu's Section 5 states Theorem 5.2 and then explicitly asks for the sharp exponent, with the lower scale `n^{-d+2}`. The arXiv record remains the 2020 survey source.

Bounded later-author/follow-up search found no Van Vu follow-up claiming the sharp exponent. Relevant later literature includes:

- Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465 / Duke Math. J.; polynomial nonsingularity, the quantitative baseline used by Vu.
- Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461, Eur. J. Combin. 2024; `n^{-1/3+o(1)}` for the directed model. This is neighboring progress, not silently substituted for the undirected source.
- Margalit Glasgow, Matthew Kwan, Ashwin Sah, Mehtaab Sawhney, *The Exact Rank of Sparse Random Graphs*, arXiv:2303.05435; local-dependency rank formulas for sparse Erdos–Renyi graphs, a useful analogue but not the fixed-degree regular model.
- Jiaoyang Huang, Theo McKenzie, Horng-Tzer Yau, *Ramanujan Property and Edge Universality of Random Regular Graphs*, arXiv:2412.20263; strong spectral rigidity/edge universality for fixed degree, but no sharp singularity exponent at zero.

Fresh exact-phrase/model searches on 2026-09-18 did not surface a later source-matching theorem giving exponent `d-2`. This is bounded negative evidence only; it is **not** a novelty certificate.

## Admission verdict

`F0003 = ADMISSIBLE HARD OUTSIDE / CURRENT-OPEN UNDER BOUNDED CHECK / SOURCE-SCOPE FROZEN`.

No mathematical resolution is claimed in this admission record. Canonical ownership must still be established create-only after a fresh master recheck.
