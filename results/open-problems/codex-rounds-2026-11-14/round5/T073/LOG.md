# T073 work log

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, 07:57 +04 (Asia/Tbilisi).

## 07:57: orientation and bounded literature check

Read the startup memory, the memory index, and the compute governor state
(warn, owner_away_open, CPU saturation). Computations will be small,
single-threaded, under nice -n 15, with explicit CPU and memory guards.
The present folder-only order overrides writes to the shared brain, mesh,
and checklist. Those stores are not updated. Earlier folders are read-only.
No subagents, git, or external publication.

Web queries: `"majority vote" "Z^2" non ergodicity 2026`,
`"noisy majority" "lattice" "stationary" 2026 phase transition`,
`"2508.06935" "2501.16202" majority`,
`"noisy majority vote" "2026" ergodicity square lattice proof`,
`"majority vote" "Z2" uniqueness rigorous 2026`.
Opened both arXiv abstracts and the full texts:

* Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
  process on trees*, https://arxiv.org/abs/2501.16202 and
  https://arxiv.org/html/2501.16202v1 .
* Damiano De Gaspari, *Fredrickson–Andersen Model and Noisy Majority Vote
  Process on Nonamenable Graphs*, https://arxiv.org/abs/2508.06935 and
  https://arxiv.org/pdf/2508.06935 .

No later solution appeared in this bounded search. Both arXiv histories
still show the original 2025 version. The tree/expansion results do not
prove the stated Euclidean result. Their synchronous retained-tie rule
must be distinguished from the continuous-time fair-tie rule here.
The literature check ended within five minutes; this does not establish
absence of a solution or priority of the uniqueness bounds.

## Reading and verification in progress

Read REPORT.md, LOG.md, PROOF.md and all Python scripts in the original,
round 3 and round 4 folders. Independently reconstructed round 4's
constants without executing its file-writing audit in its old folder.

## Earlier result rechecked; choice before extension

The round 4 result holds on re-derivation. Its local inequality leaves
exactly a/2 at M=3 and zero at every other ordered local configuration.
The source's post-ring disagreement has mean d by the stationary generator
identity. The last-ring insertion calculation uses only independent future
clocks, not independence conditional on a present disagreement. Alternating
diagonal helpers give each receiver a common 0, common 1, source (0,1),
and arbitrary ordered axial input; the update intervals have lengths a,2a,a.
Chronological revelation of the selected receiver marks justifies their
product lower bound even with dependence through outside sites.

Command:
`OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py > previous_output.json`.
Exit 0, under one second. Output: all assertions passed; all 81 local pairs;
residual 1/2 only at M=3; counts 672 for four adjacent pairs, 4480 for two
opposite pairs, 272 for all four triples. Independently reconstructed
coefficients 1/15, 8/81, 17/1260. Checked both exact round 4 root signs,
its endpoint rational value, and the expanded polynomial. Peak RSS
14,893,056 bytes, actual nice 20. The nice prefix's diagnostic
`setpriority: Operation not permitted` comes from already inherited nice 20;
the script checks actual nice >=15 before computation.

Chosen ONE extension: implement the preceding report's exact-three event.
For each triple A, force the omitted compass neighbor to a common spin at
its last ring, as well as broadcasting from the center to A. This targets
F_A={D=1 precisely on A among the four neighbors}, so the four F_A are
disjoint and sum to {M=3}. Use the residual (a/2)1_{M=3} without changing
the earlier corrections. The added blocker is a free clock vertex: it
is not an input of any chosen receiver. Expect eight nonsource clocks,
four forcing assignments, and the same six helper-before-receiver edges.
Will independently count orders, audit all rotated geometries, and prove
the conditional argument before using a numerical threshold. This is a
high-noise uniqueness extension, not a low-noise coexistence argument.

## Exact-three calculation and audit (08:00)

For A={N,E,S}, use source x, the four diagonal helpers, the three
receivers A, and omitted neighbor W as blocker. Require every nonsource
site to have a last ring after the source ring. The helpers are forced
to either alternating pattern, and W to either common value. This gives
four disjoint forcing assignments, of total probability 4e^5. As before,
the receiver marks give conditional probability at least a^3.

The seven-site fence has 272 orders. Inserting the unrestricted blocker
in any of eight positions gives 2176 orders on eight vertices. The source
integral is 1/9, hence 2176/9!=17/2835. Consequently
P(F_A)>=(68/2835)e^5 a^3 d. Summing four disjoint target events and
using the residual a/2 yields the new contraction correction
(136/2835)e^5 a^4. Independently, the new single-triple coefficient is
the old 17/1260 multiplied by 2 for the blocker choices and 8/9 for the
extra clock: (17/1260)*2*(8/9)=68/2835.

Command:
`OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py > audit_stdout.json`.
Exit 0; all assertions passed. Full output in audit_output.json and
audit_stdout.json. The run checked all 81 cases, the now exact local
identity, all four rotated geometries, 72 transmission cases, clock counts
by permutations, order-prefix recursion, explicit source ordering, and
the independent fence count. Substitution and exponential expansion give
the same integral. Two polynomial constructions agree. Exact rational
bisection and an independent integer polynomial decimal-grid enclosure
agree on the new root:

```
0.24807560804638594994778148888689 < root
root < 0.24807560804638594994778149534925
integer grid: (0.248075608046385949, 0.248075608046385950)
threshold decrease: 4.46879407623789879e-8
endpoint: 0.24807562
C3(endpoint): 0.999999951438061612953781774988235293
C2(endpoint): 1.000000132984221050821350907284113492
nice: 20
peak RSS: 16,957,440 bytes
CPU limit: 30 seconds; one thread; runtime under one second
```

No assertion failed.

## Proof saved and challenged (08:04)

Saved and read back PROOF.md: full construction and stationary coupling,
exact local identity, last-ring insertion argument, re-proofs of earlier
event estimates, new exact-three estimate, contraction, monotonicity and
exact root signs. All load-bearing constants have multiple derivations.

Adversarial checks:

* The omitted neighbor is not a direct input of any selected receiver.
  Its earlier or later forcing can still change outside histories, which
  are handled by the arbitrary ordered axial input. Fixed helper marks
  overwrite any earlier influence. All four actual coordinate geometries
  are enumerated; each has six precedence edges and 2176 legal orders.
* Forcing a common omitted neighbor does not require it to match a
  diagonal. Both common values are permitted independently. There are
  exactly four disjoint forcing assignments, each of probability e^5.
* Fixing future helper/blocker marks leaves the selected receiver marks
  independent uniforms. Causality and the uniform a bound give a^3 by
  chronological conditional expectation. Independence of resulting spins
  is never presumed, including when an axial input disagrees.
* The extra clock changes the source integral from 1/8 to 1/9; retaining
  the former would overstate the coefficient. Counting the source as an
  explicit minimal element independently gives 2176/9!, in agreement with
  the forward inserted-ring integral and the (8/9) ratio of coefficients.
* The old T term and the new J term overlap at M=3. The exact identity
  proves their two half-gap contributions sum to exactly one there. At
  M=4, J=0 and T/2=2 already consumes the whole local gap. The eight
  exact-three local configurations (four omissions, two common values)
  are all included. The four F_A target events partition {M=3}.
* Candidate source contributions are disjoint because there is no later
  source ring. A source with no ring in the finite initial interval is
  omitted in a valid lower bound. The inserted ring has mean post-ring
  disagreement d by stationarity, independently of its future clocks.
* No noise endpoint conditioning is required when e=0 or a=0: event
  lower bounds then vanish. The criterion at e=1/2 is zero. The root
  monotonicity argument is restricted to [0,1/4], where all four
  correction terms increase; the old bound covers the remaining interval.
* Near the old root the new correction is about 1.81546e-7. Dividing by
  a slope magnitude about 4.06 predicts a threshold drop about 4.47e-8,
  consistent with the exact independent enclosures. The sign is correct:
  the sufficient high-noise interval grows toward smaller noise.

No mathematical counterexample or audit failure was found. Clarified that
the alternate 8/9 coefficient calculation compares explicit clock/mark
coefficients, rather than assuming independence of the two spin events.
Used exp(-s) for exponentials to distinguish them from powers of noise e.
The finite audit does not formally verify the infinite-volume argument.

## Completion

REPORT.md records the partial verdict, exact criterion, strict new endpoint,
reproduction commands, bounded literature findings, limits, and next step.
The local identity now exhausts the configuration-wise slack of this
particular one-site decomposition. Further improvement must sharpen its
event bounds or use a different observable. The original low-noise
coexistence question remains unresolved here.

Deliverables: PROOF.md, REPORT.md, LOG.md, verify_previous.py,
previous_output.json, audit.py, audit_output.json, audit_stdout.json.
All intentional writes stayed in this folder; predecessor folders were
only read. No git, subagents, simulations, shared-store writes, or external
publication were used.
