# T073 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 2026-11-15 04:36 +04 (Asia/Tbilisi).

## Orientation, scope, and literature check (04:36–04:38)

Read the startup memory index and compute governor state (warn,
owner_away_open, CPU saturated). Only short, single-thread standard-library
audits are planned. The folder-only instruction supersedes shared-store
mutations: no mesh, checklist, recall log, or brain writes outside this
folder. No git or subagents. Earlier folders are read-only.

Read both preceding REPORT.md, PROOF.md, LOG.md and Python scripts.
The round 3 claim to audit is C1(e)<1, where a=1/2-e and
C1(e)=4a(1-e^3/2)-(17/630)e^4 a^4. Its key constant is
2*272/8!=17/1260 in the stationary triple-disagreement bound.

Web searches included noisy majority vote on Z^2, rigorous phase
transition on the square lattice in 2026, and continuous-time uniqueness.
Opened the arXiv pages and full texts of Jian Ding and Fenglin Huang,
*Non-ergodicity for the noisy majority vote process on trees*,
https://arxiv.org/abs/2501.16202 and
https://arxiv.org/html/2501.16202v1 ; and Damiano De Gaspari,
*Fredrickson Andersen Model and Noisy Majority Vote Process on Nonamenable
Graphs*, https://arxiv.org/abs/2508.06935 and
https://arxiv.org/pdf/2508.06935 . Both arXiv pages list only the 2025 v1.
De Gaspari's introduction still describes higher-dimensional Euclidean
equilibrium behaviour as open; the results require expansion. The HTML
URL for that paper returned 404, so the PDF was opened instead.

Also opened G. Gielis, C. Maes, K. Vande Velde, *Randomly interacting
particle systems: The uniqueness regime*,
https://www.numdam.org/item/AIHPA_1999__70_5_445_0.pdf . Its abstract
and model setup did not establish a directly comparable homogeneous bound.
A search surfaced an older claim about low-noise square-lattice phases;
opened its primary PDF to inspect the qualification and reference rather
than accepting the search snippet.

The literature check ended at approximately 04:38, within five minutes.
The older PDF's Section 6 references L. Gray (1985) for a possible
two-phase argument, not a theorem proved there. It explicitly gives the
standard high-noise upper bound 1/4. The search did not settle the status
of that older argument or identify a newer rigorous solution. No literature
novelty claim will be made. Only the opened sources are used.

## Independent re-derivation of round 3, before extension

The result holds on re-derivation. With g=(0,0,1,2,2), the local increment
is a[g(U)-g(L)]. The preceding blocking term removes the M=1 cases
with three equal common inputs. For M=3 the remaining gap is a, and for
M=4 it is 2a, so subtracting (a/2)*binom(M,3) is valid. The source's
post-ring disagreement has mean d by the stationary generator identity.
Four alternating forced diagonals transmit it to any specified triple
with conditional probability at least a^3: reveal the chosen receiver
marks chronologically, with all other randomness fixed. The seven-clock
order has 272 extensions and the last-source-ring integral contributes
1/8. Thus the coefficient is 2*272/8!=17/1260, as claimed. The same
last-ring reasoning gives the earlier blocking coefficient 2/4=1/2.
There is no conditional independence assumption about present spins.

Wrote verify_previous.py to check the local inequality directly from
p=(e,e,1/2,1-e,1-e), count clock orders recursively by minimal elements,
integrate by exponential expansion, and test the exact earlier root and
endpoint signs. It does not execute either older script or write in their
folders.

## Chosen extension, recorded before its computation

Use the unused two-disagreement slack suggested by round 3. For each
unordered pair A of neighbors of x let E_A mean: the two sites in A
disagree, and the other two sites are common and equal. These six events
are disjoint and do not overlap any triple-disagreement event. Each
contributes exactly a of additional local slack. Hold a source disagreement
at x, propagate to the selected pair using opposite-valued diagonal
helpers, and force the unselected neighbors to the same common spin.
Treat adjacent and opposite pairs separately because they have different
helper geometries. This is one extension of the same stationary local
method; it concerns high-noise uniqueness only. All clock and mark
coefficients will be derived twice, and tested against all 81 local pairs.

## Earlier-result audit output

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py`.
Exit 0, under one second. Output:
```
PASS: 81 local ordered pairs, counts [16, 32, 24, 8, 1]
PASS: earlier triple clock count 272
PASS: triple age integral 1/8 and coefficient 17/1260
PASS: both earlier root/endpoint claims
nice: 20
peak_rss_bytes_macos: 13778944
```
The nice prefix prints `setpriority: Operation not permitted` because the
inherited priority is already nice 20; the script verifies nice >=15.

## Pair-event derivation

For an adjacent pair, three diagonal helpers form a five-vertex alternating
fence with the two receivers. There are two opposite-valued helper
patterns. The other two neighbors of x are free clock vertices, forced
to a common value with two mark patterns. Thus seven clocks have
16*binom(7,5)*2!=672 admissible last-ring orders. Source integration gives
672/8!=1/60; the forcing marks give 4*e^5 and the two receiver successes
give at least a^2. Candidate bound: P(E_A)>=(1/15)e^5 a^2 d.

For an opposite pair the four helpers split into two independent
helper-helper-receiver triples. Their order probability is (1/3)^2;
with two free blocker clocks there are 4480 orders on eight vertices.
Source integration gives 4480/9!=1/81. There are four balanced helper
patterns and two equal blocker patterns, giving 8*e^6. Candidate bound:
P(E_A)>=(8/81)e^6 a^2 d. These statements will be proved with chronological
conditional expectation, allowing arbitrary outside spins.

The six pair events are disjoint and their local slack is separate from
the preceding triple term. Therefore the candidate contraction is
C2(e)=C1(e)-(4/15)e^5 a^3-(16/81)e^6 a^3.
Wrote audit.py with all 81 cases, all six geometries, clock counts by
permutations and order-ideal recursion, independent integral formulas,
polynomial algebra and exact root signs. Running it next.

## First extension audit: algebra check caught an error

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py`.
Exit 1 at the comparison of the hand-expanded polynomial with independent
polynomial multiplication. All local, geometry, transmission, clock-count,
and integral checks passed first. Three hand-combined coefficients
(degrees 6, 7, 8) were wrong. Re-expanding the powers of a=1/2-e gives
1529/11340, -187/945, -107/1890, respectively. Corrected only the
independent hand expansion; the factored criterion and geometry are
unchanged. Rerunning before using any numerical claim.

## Successful extension audit (04:40)

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py`.
Exit 0, under one second; full output saved in audit_output.json.
Selected output:
```
status: all assertions passed
ordered_local_pairs: 81
pair_slack_configurations: 12
rule_checks: 64
transmission_in_units_of_a: [1,2,1]
adjacent: 672 orders; integral 1/8; integrated clock coefficient 1/60
opposite: 4480 orders; integral 1/9; integrated clock coefficient 1/81
adjacent_pair_bound_coefficient_before_e5_a2: 1/15
opposite_pair_bound_coefficient_before_e6_a2: 8/81
root_lower: 38387847911459845608705571/154742504910672534362390528
root_upper: 9596961977864961402176393/38685626227668133590597632
root_width: 1/154742504910672534362390528
root approximately: 0.24807565273432671232676944
threshold improvement over round 3 approximately: 0.00000116726975936
endpoint: 0.248076
C2(endpoint): 0.999998589222393672254804273783232806
C1(endpoint): 1.000003331257626955193313049185227268
nice: 20
OMP_NUM_THREADS: 1
cpu_time_limit_seconds: 30
peak_rss_bytes_macos: 17186816
```
The correction is approximately 4.7420e-6 near the old threshold. Dividing
by a slope magnitude about 4.06 predicts a threshold shift about 1.17e-6,
consistent with the exact signs and bracket. The new rational endpoint
is excluded by the preceding criterion, so the extension is strict.

## Proof saved and challenged (04:43)

Saved PROOF.md with the construction of the stationary coupling, exact
local case split, a general last-ring insertion estimate, the earlier
blocking and triple estimates re-derived, and the two new pair bounds.
The numerical interval is proved by monotonicity on [0,1/4] and exact
signs, with the original criterion used above 1/4.

Read the proof back against the code and tried these failure cases:

- The unselected common neighbors could update after a receiver. This
  is allowed: they are not receiver inputs. Their effects through other
  sites are either overwritten by the selected helper marks or included
  in the arbitrary axial input. No blocker-before-receiver constraint is
  required.
- Selected successes could be dependent through outside sites. Fixing
  all other randomness leaves each selected receiver mark independent
  of its past. Its success probability is at least a for every ordered
  axial input, including an axial disagreement. The product bound is
  iterated conditional expectation, not independence of final spins.
- Forcing marks at times later than a selected receiver might bias its
  input. Those independent marks can be fixed without changing the fresh
  receiver uniform, and causality prevents any backward effect. Each
  receiver's own helpers must already have had their last rings.
- Opposite helper pairs really are disjoint; adjacent ones share exactly
  one diagonal. This accounts for four versus two helper assignments.
- Adding six lower bounds does not require disjoint construction events
  across different pairs. Their target events are disjoint; expectation
  is added separately for each, with no union probability asserted for
  the underlying constructions.
- Local slack cannot be counted twice. The pair term is nonzero only
  at M=2; the triple term only at M>=3. At M=3 half the gap is still
  unused, and at M=4 the previous correction uses the entire gap.
- Only the extremal coupling requires translation invariance. The
  squeezed stationary law can be arbitrary.
- Boundary forcing intervals at e=0 and a=0 need not be conditioned on:
  both new lower bounds are then trivial. No equality-at-threshold
  conclusion is claimed.
- The derivative signs used for uniqueness of the numerical root are
  asserted only below 1/4. Each correction e^m a^n has m>=n, so it
  increases there. The previous factor bounds everything above 1/4.

To check the missed-geometry possibility independently, extended audit.py
to reconstruct all four actual input coordinates for each of the twelve
pair/receiver cases, check disjointness of source/helpers/receivers/
blockers, and rebuild and count the clock order from the actual lattice
coordinates for all six pair orientations. Rerunning for these new checks.

## Final geometry audit

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py > audit_stdout.json`.
Exit 0, under one second. Both audit_output.json and the captured stdout
contain `status: all assertions passed`, `receiver_geometry_checks: 12`,
and the six actual-geometry clock counts 672,4480,672,672,4480,672.
All numerical values agree with the previous successful run. The audit
again used one thread, nice 20 and a 30-second CPU limit, far below 1 GB.
Its measured peak RSS was 16,171,008 bytes.
No geometric exception or probabilistic counterexample was found.

## Completion

REPORT.md records the partial verdict, exact sufficient uniqueness
criterion, new pair-event estimates, reproduction commands, the corrected
hand-expansion failure, uncertainty, and a concrete next step. PROOF.md is
self-contained and does not rely on edits to either predecessor folder.
All intentional writes stayed in this folder. No simulation, git,
subagent, shared-store mutation, or external publication was used.
The low-noise coexistence statement remains unresolved in this work.
