# T073 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 2026-11-15 01:09 +04 (Asia/Tbilisi).

## Orientation and earlier files

Read the earlier REPORT.md, PROOF.md, LOG.md, audit.py in
~/codex_op_1114/briefs/T073 without editing that folder.
Read the startup memory and compute governor state: status warn, mode
owner_away_open, CPU saturated. Only tiny standard-library audits are planned.
The current folder-only order supersedes the standing shared mesh/checklist/
brain write requirements. No shared stores, git, subagents, or external
publication will be used. Commands use OMP_NUM_THREADS=1 and nice -n 15;
Python audits will check inherited priority and set a short CPU limit.

Initial literature searches (01:09):
- "majority vote" "Z^2" uniqueness 2026
- "noisy majority" "square lattice" proof phase transition 2026
- "majority vote" uniqueness high noise criterion continuous time

No solution appeared in these results. Checking primary sources next; the
literature stage is limited to five minutes from 01:09.

## Independent re-check and choice (01:13)

The earlier argument holds on re-derivation. With g=(0,0,1,2,2),
p(k)=epsilon+(1/2-epsilon)g(k). An ordered local pair's probability
increment divided by a=1/2-epsilon is g(U)-g(L). Telescoping bounds it
by the number M of disagreements, removing each uniquely disagreeing
coordinate when the other three are common and equal. The last-source-ring
argument samples a stationary post-ring disagreement of mean d. Its three
other clocks must all have younger ages; among four independent exponential
ages this has probability 1/4. Two equal forced mark choices give
2*epsilon^3/4=epsilon^3/2. Thus the earlier criterion is valid.
An independent finite audit will check all ordered pairs and both the
integral and clock-order calculations without running the older script
(which writes its output in the read-only earlier folder).

Chosen extension, before work: use the unused slack at M=4. The exact
local gap there is 2a and the earlier blocking terms all vanish. Prove a
positive lower bound P(M=4)>=c(epsilon)*d by broadcasting a disagreement
at the center to its four neighbors, while fresh noise fixes the four
diagonal sites to alternating common spins. Each neighbor then has one
fixed 0, one fixed 1, the disagreeing center, and an arbitrary outer axial
neighbor. Its update has disagreement probability at least a. This should
make the earlier uniqueness endpoint strict, and yield an explicit sharper
criterion. The marks at the four selected neighbor rings must be handled
by chronological conditional expectation, not by assuming independence of
the resulting spins. This is one extension of the earlier stationary bound;
it still concerns high noise, not low-noise coexistence.

## Earlier audit output

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py`.
Exit 0, under one second, peak RSS 13,680,640 bytes, inherited nice 20.
The requested nice prefix prints `setpriority: Operation not permitted`
because the process is already at nice 20; the audit verifies nice >=15.
Output:
```
PASS: ordered pairs by M: {0: 16, 1: 32, 2: 24, 3: 8, 4: 1}
PASS: independent integral: 1/4
PASS: earlier endpoint contraction: 4999531215835321/5000000000000000
PASS: earlier exact root bracket signs
```
No error found in the earlier result.

## Literature check closed within five minutes

Opened arXiv pages and full texts of:
- Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority Vote
  Process on Nonamenable Graphs*, arXiv:2508.06935,
  https://arxiv.org/abs/2508.06935 and https://arxiv.org/pdf/2508.06935 .
  The arXiv history still has only v1, 9 August 2025; its abstract requires
  graph expansion. No newer solution for the task was located.
- Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
  process on trees*, arXiv:2501.16202,
  https://arxiv.org/abs/2501.16202 and
  https://arxiv.org/html/2501.16202v1 . Its history still has only v1,
  27 January 2025, and its theorem concerns regular trees.
- G. Gielis, C. Maes, K. Vande Velde, *Randomly interacting particle systems:
  The uniqueness regime*, Annales de l'I. H. P., section A 70 (1999),
  445–472, https://www.numdam.org/item/AIHPA_1999__70_5_445_0.pdf .
  The opened abstract and model setup concern spatial disorder and mainly
  probabilistic cellular automata. No directly comparable explicit bound
  for the present homogeneous rule was established in this short check.
A speculative v2 URL for De Gaspari returned 404. Additional broad searches
returned mostly unrelated voting papers. This bounded search found no
solution; it does not prove absence or establish novelty of our bound.

## Refine the same chosen slack extension

Three disagreements already give slack at least a, and four give 2a.
Let T_x count triples of disagreeing neighbors. Then T_x=0,1,4 according
as M<=2, M=3, M=4. The deterministic improvement is at least (a/2)T_x,
which is compatible with the earlier blocking correction (the blocking
terms vanish whenever M>=2). It is better to broadcast to a specified
triple than require all four receiver rings. The four diagonal helpers
still suffice. For the clocks it is enough that each receiver's last ring
follow the last rings of its own two adjacent diagonal helpers. A finite
seven-element partial order gives the clock probability. Count it in two
independent ways before using its constant.

## Exact clock count and successful extended audit

Exploratory command, single thread and nice 15 with CPU limit 10 seconds:
```
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B -c 'import os,resource,itertools; assert os.getpriority(os.PRIO_PROCESS,0)>=15; resource.setrlimit(resource.RLIMIT_CPU,(10,10)); orders=[p for p in itertools.permutations(range(7)) if all(p.index(i)<p.index(4+j) and p.index(i+1)<p.index(4+j) for j,i in enumerate(range(3)))]; print(len(orders)); print(orders[:3])'
```
Output: 272, with sample legal orders. The seven-event order is the path
h0 < r0 > h1 < r1 > h2 < r2 > h3. Inclusion-exclusion gives independently
630-210-105-105+21+35+7-1=272. A third count by subset dynamic programming
agrees in the saved audit.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py`.
Exit 0; under one second; peak RSS 15,925,248 bytes; inherited nice 20;
CPU limit 30 seconds; only Python standard library. Full output is saved
in audit_output.json. Selected output:
```
status: all assertions passed
ordered_pairs: 81
local_slack_by_M: {0:[0], 1:[0], 2:[0,1], 3:[1], 4:[2]}
update_rule_checks: 64
transmission_cases: 3
geometry_checks: 24
linear_extensions_permutations: 272
linear_extensions_dynamic_program: 272
linear_extensions_inclusion_exclusion: 272
clock_order_probability: 17/315
age_integral: 1/8
clock_constant: 17/2520
broadcast_coefficient_before_e4_a3: 17/1260
contraction_correction_coefficient_before_e4_a4: 17/630
new_root_lower: 0.248076820004086075038875485072875637371225821
new_root_upper: 0.248076820004086075039087243309689212455992902
new_root_width: 1/4722366482869645213696
new_rational_endpoint: 0.24807685
new_contraction_at_endpoint: 0.999999878141927758593318886796535559035664022
old_contraction_at_endpoint: 1.0000002897895762272616601520125
```
The correction is `(17/630)*epsilon^4*(1/2-epsilon)^4`. The root improves
by approximately 1.01328926e-7. This is small but strictly positive and
covers a rational noise value not covered by the earlier criterion.
The audit checks the factored contraction against an independently expanded
polynomial, and checks the root by exact bisection and independent decimal
grid signs. No failed audit run occurred.

## Proof saved

Wrote PROOF.md with the full graphical construction and extremal stationary
coupling, the earlier last-ring bound re-derived, the strengthened local
inequality, the broadcast lemma, the seven-clock count, and the resulting
criterion. The proof handles the axial inputs arbitrarily and reveals
selected receiver marks chronologically. It does not assume conditional
independence of neighboring spin disagreements. The stationary Poisson
insertion calculation is written separately from the pure clock calculation
so that no backward-conditioning independence is silently used.

## Adversarial proof audit (01:19)

Read PROOF.md in full against the exact update table and the audit. The
following possible failures were checked:

- A chosen receiver has FOUR inputs, not three. The center disagreement,
  one forced 0, one forced 1, and arbitrary ordered axial input yield
  counts (1,2), (1,3), (2,3). The corresponding intervals have lengths
  a,2a,a. No assumption about the axial spin or its independence is needed.
- The helper clocks need precede only adjacent receivers, not every
  receiver. A helper whose selected ring is later than a nonadjacent
  receiver cannot compromise the latter's two already-fixed inputs.
- Conditioning on future helper forcing does not bias the selected
  receiver uniforms. For a precise check, fix all randomness except those
  three uniforms. Causality makes each pre-ring state a function of only
  earlier selected uniforms. The product lower bound therefore follows
  by iterated expectation even with arbitrary dependence through the rest
  of the lattice. Added this explicit formulation to PROOF.md.
- The receiver rings are last rings, so a success is not lost later.
  The source has no subsequent ring. All other updates remain unrestricted.
- Source events at distinct rings do not accumulate: at most one can have
  no later source ring. This justifies the pathwise sum bound; no union
  bound is used in the wrong direction.
- A source ring inserted at deterministic time sees a stationary pre-ring
  pair, and its mean POST-ring disagreement is d by the generator identity.
  The calculation does not condition on a present disagreement and then
  treat the past helper clocks as independent of it.
- For M=3 the new local correction uses only half the available slack;
  for M=4 it uses exactly all the slack. Blocking corrections and triple
  corrections do not conflict because blocking terms vanish for M>=2.
- Rotation of the construction works separately for each triple; full
  rotation invariance of the stationary coupling is unnecessary. Clarified
  this in the proof.
- Conditioning forced marks is unnecessary at epsilon=0 or 1/2, since
  the broadcast lower bound is then zero. Added an explicit endpoint case
  before using conditional forcing intervals.
- The root is characterized by monotonicity only on [0,1/4], where the
  correction increases. Above 1/4 the old criterion already applies;
  global monotonicity of the corrected expression is not presumed.
- The contraction improvement is ~4.1165e-7 near the old root, hence a
  threshold shift ~1.0133e-7 with slope about -4.06. Its sign and scale
  agree with the exact bracket. This is not an improvement to a low-noise
  coexistence estimate.

All load-bearing numbers have independent derivations: 272 by three
counts; the age integral by substitution and exponential expansion; the
prefactor by both the inserted-ring integral and 272/8! pure clock
ordering; the contraction by factored and expanded formulas; the root by
exact bisection and independent decimal-grid signs. No counterexample to
the new criterion was found. The finite audit is not a formal verification
of the probabilistic construction.

## Completion

Saved REPORT.md with the partial verdict, the new criterion and exact
bracket, the independent earlier-result check, reproduction commands,
failures, uncertainty, and a concrete next target. Deliverables:
PROOF.md, verify_previous.py, audit.py, audit_output.json, LOG.md, REPORT.md.
All intentional writes stayed in this task folder. No simulation, git,
subagent, shared-store mutation, or publication was used. The original
low-noise coexistence statement remains open in this work.
