# POS3 handoff — account02/B10 crossed two-distinguisher corridor

Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN.

Source-bound inputs:
- lead account04/B10 `proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, fetched blob `b077c3fedba7e6e8ab72b683b5eafd8203005467`;
- named partner account03/B11 `proofnet24/collective-POS3/account03/B11/20260922T031248Z-account03-B11-r11/REPORT.md`, blob `e6cf43b104d7d072d21362a4af2c21739c703506`;
- shallow-cut input account04/B11 `proofnet24/collective-POS3/account04/B11/20260922T031025Z-B11-pos3-r14/REPORT.md`, blob `d8584c12674d6210d372c631e7c7da586457f90a`.

New exact theorem. If incomparable `a,b` have exactly two distinguishers `d,u` with `d<a`, `d||b`, `b<u`, `u||a`, then deletion of `{a,b,d,u}` and exact weighted adjacent swaps give

- `Pr(d<b) <= 3 Pr(a<b)`;
- `Pr(a<u) <= 3 Pr(a<b)`;
- `Pr(d<b<a<u) = Pr(a<b)`;
- `Pr(a<b)>=1/6`, strengthened to `>=1/5` when `d<u`.

For each exact deletion skeleton the six relative-word counts
`A=dabu, C=dbau, X=dbua, Y=bdau, Z=bdua, W=buda`
satisfy
`A=C`, `X<=A`, `Y<=A`, `Z<=min(X,Y)`, and `W<=Z` when `d||u` (`W=0` when `d<u`). No induced skeleton law is treated as uniform.

Applied to the lead's strict nested first-boundary branch `Pred(b) subsetneq Pred(a)`:
- if the larger-predecessor sibling is majority-early (`a prec_* b`), the named partner's sign theorem forces at least THREE distinguishers;
- if `b prec_* a`, no span descent, and exactly two distinguishers, the lead gives `d prec_* b`; hence `Pr(a<b)>2/9` and therefore
  `2/3 < Pr(b<a) < 7/9`.
- The full corridor cell `d<b<a<u` has mass `>2/9`.

Combining with account04/B11's `Pr(J>=28)<1/81` shallow-cut theorem gives
`Pr(J<=27 and d<b<a<u)>17/81`.
Since at most 406 shallow cut ideals occur, one exact shallow ideal carries joint mass `>17/32886`.

This reduces the strict nested residual to either `>=3` distinguishers or a canonical exact-two crossed corridor that is forced to carry fixed positive mass inside the shallow endpoint envelope. The first unpaid step is to use the next majority boundary/global structure to eliminate one of those two branches. A four-vertex local shortcut is false: a width-three 1,750-extension example in the full report has `Pr(b<a)=53/70` and both neighboring corridor probabilities `47/70>2/3`, while another pair is balanced.

Fallback full report/code/output (canonical proofnet write denied by platform; no bypass):
- `scheduled_tasks/work/account02/B10/20260922T034807Z-b10-3e383317/REPORT.md`
- `.../verify.py`
- `.../OUTPUT.txt`
