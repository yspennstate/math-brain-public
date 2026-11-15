# T073 work log

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, 10:25 +04 (Asia/Tbilisi).

## Orientation and bounded literature check

Work is confined to this folder; predecessor folders are read-only. The
specific folder-only order precludes shared mesh, checklist, or memory
updates. No git, subagents, or publication. Read the compute state:
status warn, mode owner_away_open, CPU saturated. Only short standard-library
single-thread calculations at nice >=15 are planned, with resource guards.
Consulted brain recall for the subject; it returned no relevant T073 note.

Opened the arXiv pages and full texts of Jian Ding and Fenglin Huang,
*Non-ergodicity for the noisy majority vote process on trees*,
https://arxiv.org/abs/2501.16202 and
https://arxiv.org/html/2501.16202v1 ; and Damiano De Gaspari,
*Fredrickson–Andersen Model and Noisy Majority Vote Process on Nonamenable
Graphs*, https://arxiv.org/abs/2508.06935 and
https://arxiv.org/pdf/2508.06935 . Both pages list the original 2025
versions. Their expansion results do not settle the square lattice case.
The Ding–Huang rule is synchronous with retained ties and unbiased noise
resampling; it differs from the continuous-time fair-tie rule here.

Also opened the primary PDF of Tânia Tomé, Mário J de Oliveira and
Maria Augusta Santos, *Non-equilibrium Ising model with competing Glauber
dynamics*, https://fge.if.usp.br/~oliveira/JPA_24_3677_1991.pdf . Section 6
describes the fair-tie majority rule and quotes the uniqueness bound 1/4.
Its sentence about possible low-noise phases refers to Gray (1985), not
to a proof supplied there; this lead also appeared in round 4's log.
No later solution was found in the bounded search. This is not a proof
that no solution or stronger uniqueness criterion exists. Literature
search is now closed, within five minutes of starting.

## Rechecking the predecessor

Read the predecessor proofs. For M=0,1,2,3,4 disagreements among the
neighbors, the exact round 5 decomposition has increment (in units of
a=1/2-e) M minus the blocked terms, minus binom(M,3)/2, minus the
equal-common pair indicators, minus 1_{M=3}/2. Direct case splitting
confirms this identity. The stationary last-source-ring insertion uses
E q=d, not independence conditional on the present disagreement.
The receiver success product is justified by chronological revelation
of fresh independent receiver marks and a uniform lower bound for every
outer axial input. These parts appear sound; an independent exact audit
will be saved before extending the bound.

## Independent predecessor audit completed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py > previous_output.json`.
Exit 0. Reconstructed all 81 ordered local states and all four event
coefficients without importing predecessor scripts. Clock counts by an
order-ideal dynamic program agree with a second calculation: condition
on receiver times, integrate the minimum receiver time for each helper
over the receiver-order simplices. Counts 272, 2176, 672, 4480 give
17/1260, 68/2835, 1/15, 8/81 respectively. The source age integrals
agree by substitution and exponential expansion. Both exact predecessor
root signs, bracket width, expanded polynomial, and endpoint check pass.
The round 5 result holds on this re-derivation. Actual nice is 20; the
nice prefix prints the inherited-priority diagnostic seen in earlier
rounds. Peak RAM is recorded in previous_output.json.

## Chosen extension, before its calculation

Extend the triple broadcast to every assignment of common diagonal
helper values. Previously only the two alternating assignments were
used. Whenever a receiver's two diagonal helpers have the same value b,
force its outer axial input to common 1-b before its last ring. The
receiver then has three common inputs containing both values and the
source disagreement, giving success probability a. For receivers whose
helpers differ, the previous uniform lower bound a still applies, with
arbitrary axial input. The sixteen diagonal assignments are disjoint
forcing-mark events at the same four last rings, so their success
probabilities can be added for each fixed candidate source ring.

This is one finite extension of the triple-broadcast lemma. Apply it to
both at-least-three and exactly-three events, retaining the pair bounds.
It gives a concrete improvement without assuming a conditional density
of axial disagreements (the subtle step suggested in round 5). Compute
all added clock posets by two independent methods and check every rotated
geometry and forcing assignment. No change to the local identity is needed.

## Extension calculation completed (10:30)

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py > audit_stdout.json`.
Exit 0, under one second, all assertions passed. Full output is in
audit_output.json and audit_stdout.json. Let P(e) and R(e) be the
single-triple coefficients, with the common factor a^3 d removed, for
at-least-three and exactly-three disagreements respectively. The result is

```
P(e) = 17 e^4/1260 + 7 e^5/270 + 767 e^6/45360 + 23 e^7/6160
R(e) = 68 e^5/2835 + 7 e^6/150 + 767 e^7/24948 + 23 e^8/3360.
```

For monochromatic receiver-index sets S=empty,{0},{1},{2},{0,1},
{0,2},{1,2},{0,1,2}, the last-ring order counts are respectively
272,1582,1540,1582,10160,10360,10160,74520 on 7+|S| clocks.
All eight are checked both by order-ideal recursion and by integrating
helper minima conditional on three receiver times. An independent
coordinate reconstruction checks all 4*16=64 rotated forcing patterns
and 384 receiver/input cases. The free omitted-neighbor clock changes
each coefficient by 2e*(8+|S|)/(9+|S|), checked by explicitly counting
the enlarged poset. An explicit minimal source gives the same counts.

The new contraction is
`C4(e) = 4a(1-e^3/2) - 4e^5 a^3/15 - 16e^6 a^3/81 - 2a^4(P(e)+R(e))`.
The earlier expression is recovered by retaining only the leading term
of each polynomial. Exact roots and endpoints:

```
38387828333112147431787763/154742504910672534362390528 < new root
new root < 9596957083278036857946941/38685626227668133590597632
new root approximately 0.24807552621222013612253301
independent integer-polynomial grid: (0.248075526212220136, 0.248075526212220137)
threshold decrease approximately 8.18341658138252485e-8
endpoint e=0.24807553:
  C4 = 0.999999984612015744454758680159985502...
  C3 = 1.000000317065932486634429222017556278...
```

Two polynomial constructions agree: direct coefficient multiplication,
and the preceding polynomial minus only the six added event terms.
Dyadic rational bisection and independent integer decimal-grid signs
give the same root enclosure. Actual nice 20; OMP_NUM_THREADS=1;
30-second CPU guard; measured peak RSS 16,302,080 bytes. No assertion
failed. Writing the full proof and testing the dependence argument next.

## Proof saved and challenged (10:34)

Saved PROOF.md with the stationary ordered coupling, exact local identity,
last-ring insertion, re-derived blocking/pair estimates, all sixteen new
diagonal assignments, both clock derivations, and the resulting uniqueness
criterion. Read it back against the script and challenged these points:

- Adding bounds across different diagonal patterns is valid only because
  each construction uses the same four diagonal last rings for a fixed
  source ring. Different forced values require disjoint mark intervals.
  The extra axial clocks can differ; that does not alter disjointness.
  Across source rings, the no-later-source-ring condition gives at most
  one nonzero contribution. The proof now states both arguments explicitly.
- Same-valued diagonal helpers need an opposite common axial value, not
  an arbitrary common value. This gives counts (1,2) or (2,3), hence
  exactly a. The script independently reconstructs these values from
  actual coordinates. With different diagonal values all three ordered
  axial states remain allowed.
- A forced axial site can influence a diagonal before its selected ring,
  but the diagonal's forced last mark overwrites that influence. After
  its own last ring it cannot change. Each needed helper-before-receiver
  edge is imposed; no unsupported independence of spin histories is used.
- Fixing other underlying marks, including future forcing marks, leaves
  selected receiver uniforms independent. Causality prevents later
  selected marks from affecting an earlier selected input. The uniform
  receiver bound therefore multiplies by iterated conditional expectation.
- The omitted neighbor is absent from every receiver input set. Its
  arbitrary earlier effects are covered by unrestricted axial histories,
  or overwritten by required axial forcing. Its added clock changes the
  integrated coefficient by (8+m)/(9+m), not by one.
- T and J overlap, but the exact 81-case identity allocates exactly two
  half-gaps at M=3. No additional local slack has been introduced. The
  new work only sharpens lower bounds for the same observables.
- A draft endpoint sentence incorrectly said every event lower bound
  vanishes at a=0. The blocking bound has no factor a. Corrected the
  justification: at e=1/2 the stationary identity gives d=0 because
  q=0, so all bounds are trivial. No coefficient, criterion, or numerical
  result changed.
- The new contraction correction is about 3.32454e-7 near the old root.
  With slope magnitude about 4.06, this predicts a threshold shift of
  about 8.18e-8, consistent in sign and magnitude with the exact brackets.

The finite checks cannot formalize the infinite-volume argument, but no
counterexample to the construction was found. The governor now reports
status ok, mode owner_away_open; computations remain short and single-threaded.

## Completion

REPORT.md records the partial verdict, exact new criterion, strict
extension, reproducible commands, literature limits, the endpoint wording
correction, and a next step on the retained pair bounds. Deliverables:
PROOF.md, REPORT.md, LOG.md, verify_previous.py, previous_output.json,
audit.py, audit_output.json, audit_stdout.json. All intentional file writes
stayed in this folder; no predecessor was changed, and no git, subagent,
simulation, deployment, or publication was used. The low-noise coexistence
problem has not been solved.
