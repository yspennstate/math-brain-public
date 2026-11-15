# T073 work log

Task: “push this problem forward by one checkable piece.” Started 2026-11-14,
approximately 20:51 +04 (Asia/Tbilisi).

## 20:51–20:54: orientation and literature check

Read the startup memory and the compute governor state. The governor reported
`status: warn`, `mode: owner_away_open`, CPU saturation. No simulation or heavy
computation is planned. No subagents, git, or external publication are used.
The current task's folder-only restriction takes precedence over the standing
instructions to update the shared mesh, checklist, and brain: those stores are
outside this folder and have not been deliberately updated.

Read-only command attempted:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall 'majority vote Z2 positive rates Toom research proof'
```

Output: `nice: setpriority: Operation not permitted`; a Python/onnx telemetry
warning followed, with no useful recall result. Do not repeat this recall:
it loads unnecessary machinery. `ps` is also denied by the sandbox. A startup
memory records a macOS failure when relative nice is stacked on an already
niced process. Further scripts will verify inherited absolute priority and
stay single-threaded and memory limited.

Web searches included:

- `"majority vote" "Z^2" phase transition stationary measures noise`
- `"majority vote" "square lattice" "open problem" rigorous`
- `"noisy majority" "2026" lattice ergodicity`
- `"majority vote" "square lattice" rigorous proof phase transition 2025 2026`

Opened Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
process on trees*, arXiv:2501.16202, especially Section 1.1:
https://arxiv.org/html/2501.16202v1 . The update is synchronous discrete time;
ties retain the previous spin; noise is fair resampling. Thus this paper's
rule is not the continuous-time, random-tie rule in the task. Away from ties,
its noise parameter is twice the minority-choice parameter of this task.

Opened Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority Vote
Process on Nonamenable Graphs*, arXiv:2508.06935, abstract and PDF:
https://arxiv.org/abs/2508.06935 and https://arxiv.org/pdf/2508.06935 .
Page 2 explicitly describes the Euclidean-lattice equilibrium problem as
open. Its results require expansion.

Opened the arXiv page of J. F. Silva Neto, D. S. M. Alencar, L. T. Brito,
G. A. Alves, F. W. S. Lima, A. Macedo-Filho, R. S. Ferreira, T. F. A. Alves,
*Supervised and Unsupervised Deep Learning Applied to the Majority Vote Model*,
arXiv:2509.14155, https://arxiv.org/abs/2509.14155 . This is numerical work,
not a proof of coexistence. No solution located in this bounded search.

## Choice recorded before the mathematical work

Prove a modest explicit improvement of the elementary high-noise uniqueness
criterion epsilon > 1/4 for the exact four-neighbor, random-tie, continuous-time
rule. Use a stationary monotone coupling and an event on which three neighbors
are freshly forced to a common spin while the fourth site's disagreement is
preserved by having no clock ring. Such an event removes that site's influence.
This is finite, local, and checkable without simulation. It addresses the
opposite end of the phase diagram from the requested low-noise conjecture;
no claim of low-noise coexistence or literature novelty will be made.

Planned deliverables: PROOF.md with a complete proof, a small independent
exact-arithmetic audit script and saved output, and REPORT.md. Check all ordered
local spin pairs and independently rederive the blocking-event constant.

## 20:55–20:57: close the literature check and resolve execution limits

Additional searches: `"majority vote" uniqueness "1/4"`,
`"majority vote" "ergodicity" "Dobrushin"`, and
`"majority vote" "2026" "stationary measures" lattice`.
Opened De Gaspari's PDF at Definition 2.3, page 5: his process is also
synchronous with ties retained. The same paragraph distinguishes the
continuous-time process of Bramson–Gray. Thus synchrony as well as tie-breaking
must be kept separate in any attempted transfer of the tree results.

Opened Damiano De Gaspari's 2026 thesis catalog entry, *Out-of-equilibrium
systems: stationary measures and superdiffusivity*,
https://repositum.tuwien.at/handle/20.500.12708/231354 . Its abstract still places
the majority-vote results on nonamenable graphs. A potentially relevant
Minnesota thesis PDF returned HTTP 403 when opened:
https://conservancy.umn.edu/bitstreams/47a7ef23-15b3-4076-9079-79ef0e63a969/download .
Its contents have not been verified and it is not used as evidence.
The bounded literature search is complete, within ten minutes. No solution
or substantial new rigorous advance for this exact Z^2 process was located;
this is a search outcome, not proof of absence.

Execution diagnostic:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B -c 'import os, resource; print("priority", os.getpriority(os.PRIO_PROCESS, 0)); print("address_space_limit", resource.getrlimit(resource.RLIMIT_AS)); print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))'
```

Output:

```text
nice: setpriority: Operation not permitted
priority 20
address_space_limit (9223372036854775807, 9223372036854775807)
OMP_NUM_THREADS 1
```

The worker already has nice 20, lower priority than nice 15. Keep the requested
`nice -n 15` prefix and verify inherited nice >= 15 inside the audit script.
A preceding diagnostic trying `setrlimit(RLIMIT_AS, (536870912, 536870912))`
failed with `ValueError: current limit exceeds maximum limit`; no computation
ran after that failure. Avoid that unsupported macOS limit. The audit will use
only Python standard-library integer arithmetic over a fixed, tiny state set.

## Derivation saved: stationary disagreement and last-ring decomposition

Wrote PROOF.md. For a=1/2-epsilon the four consecutive increments of the
update probability are 0,a,a,0. In a stationary ordered coupling, the mean
disagreement d equals the mean probability difference at an update.
If three other neighbors are common and equal in the two copies, changing
the fourth neighbor has no influence.

The initial fixed-window idea gives a valid but unnecessarily small constant.
The proof instead sums over the last update of the potentially disagreeing
neighbor. At age s, preserving its disagreement and forcing the other three
neighbors to a common value has future probability
`exp(-s) * 2*epsilon^3 * (1-exp(-s))^3`.
Stationarity makes the mean disagreement immediately after an inserted
source update equal to d. Integrating ages gives the blocking bound
`E[D_y 1_B] >= (epsilon^3/2)*d`, since the remaining integral is 1/4.
The resulting sufficient uniqueness condition is
`(2-4*epsilon)*(1-epsilon^3/2) < 1`.

Important dependence check: the proof does not condition on a discrepancy
at the observation time and assume neighboring spins independent. It
conditions on the past at the last source ring, and uses independent future
clocks and marks. Later influence on the other three sites is overwritten
by their last forced marks. Contributions from candidate last rings are
disjoint because the source has no later ring.

Next: exhaustive local checks, two independent derivations of the integral
constant, exact rational endpoint and root bracketing, then a proof audit.

## First audit run

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py`.
The process passed the nice >= 15 assertion, all 64 update-rule checks,
all 81 ordered local pairs and 1,944 telescoping-order checks, the integral
checks, and the exact rational endpoint sign check. It then failed a root
bracket assertion: the fallback coarse grid's upper endpoint 0.249 was
incorrectly required to lie below the theorem's endpoint 0.2481. This is
an audit-script bracket bookkeeping error, not a failed mathematical
inequality. Fix the bracket and rerun before making any numerical claim.

## Successful exact audit

Corrected the independent decimal grid to [0.248076, 0.248077], checked its
endpoint signs without a fallback, then ran the exact command again:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

Exit code: 0. Output saved in full as `audit_output.json`. Output that matters:

```text
nice: setpriority: Operation not permitted
status: all assertions passed
nice: 20
OMP_NUM_THREADS: 1
cpu_time_limit_seconds: 30
peak_rss_bytes_macos: 15613952
update_rule_checks: 64
ordered_local_pairs: 81
pair_order_checks: 1944
age_integral_substitution = 1/4
age_integral_expansion = 1/4
age_integral_clock_ordering = 1/4
blocking_coefficient_before_epsilon_cubed = 1/2
contraction_at_endpoint = 4999531215835321/5000000000000000
                        = 0.9999062431670642
polynomial_at_endpoint = -468784164679/5000000000000000
                       = -0.0000937568329358
polynomial_raw_numerator_denominator_10_to_16 = -937568329358
root_lower = 558619565237287/2251799813685248
           = 0.2480769213330122902050334232626482844353
root_upper = 69827445654661/281474976710656
           = 0.2480769213330127342942432733252644538879
root_bracket_width = 1/2251799813685248
```

Runtime was below one second; measured peak memory was approximately 15.6 MB
in decimal units. The macOS nice diagnostic persists because priority is
already 20. The script verifies this before doing the audit. Only the Python
standard library is used, with no numerical or parallel libraries.

Second derivations: the four-neighbor fair-tie probabilities are reconstructed
by uniformly deleting one neighbor and taking the remaining triple's majority.
The age integral is checked both by substitution and by expanding its four
exponentials; independent enumeration of the 24 clock orderings gives 6/24.
The rational endpoint is checked by the factored contraction and the expanded
quartic separately. The root is checked by exact dyadic bisection and by
independent decimal-grid signs. Updated PROOF.md with the exact integers.

## Adversarial mathematical audit

Read the complete proof back against the actual update table and the code.
The checks aimed at the following possible failure cases:

1. **Ties or self-dependence.** The theorem uses fair resampling at a tie,
   independent of the site's old spin. A retained-tie rule is not silently
   substituted. The proof's local probability table is exactly the task's
   table. Noise epsilon is minority-choice probability; fair-resampling
   noise would be 2*epsilon away from ties.
2. **Nontranslation-invariant stationary measures.** Only the constructed
   extremal coupling needs translation invariance. Every stationary measure,
   whether translation invariant or not, is squeezed between its marginals.
   Thus the conclusion is full stationary uniqueness.
3. **Stationary joint law.** Individual monotone limits alone do not prove
   joint convergence. The proof explicitly constructs a stationary joint
   law by time averaging the shared-clock pair and compactness.
4. **Dependence at the observation time.** The noise calculation uses future
   randomness after an inserted source ring. It does not factor a conditional
   law of neighboring spins given a present disagreement. Arbitrary updates
   at x or elsewhere are allowed before the last forced neighbor marks.
5. **Multiple candidate source rings.** The no-later-ring condition makes
   the summands in the pathwise bound disjoint. If the source never rings
   during [0,T], its contribution is simply omitted in a lower bound.
6. **Clock sampling bias.** A deterministic inserted ring sees the stationary
   pre-ring law because clocks have state-independent rate one. The expected
   post-ring disagreement is not assumed to be d: it is derived from the
   stationary generator identity E[q_y-D_y]=0. This is the load-bearing
   step in the last-ring argument.
7. **Boundary cases.** At epsilon=0 the blocking bound vanishes and gives
   no uniqueness claim. At epsilon=1/2 both copies get identical updates
   and the contraction factor is zero. At epsilon=1/4 the factor is
   127/128, consistent with a strict improvement of the elementary bound.
   At the quartic root the inequality is non-strict and proves nothing.
8. **Magnitude and sign.** The endpoint factor is below one by
   0.0000937568329358, the root is below 0.2481, and the rational interval
   extends the elementary 1/4 bound by 0.0019. No low-noise conclusion is
   inferred from these small high-noise improvements.

No mathematical counterexample to the stated criterion was found. This is
an explicit proof with a finite arithmetic audit, not a computer-verified
formal proof. No novelty or comparison with the best published high-noise
bound is claimed. The fixed-window approach was superseded within the same
piece by the stronger last-ring argument; no extra problem was pursued.

## Completion

Saved REPORT.md with the partial verdict, exact criterion, reproducible command,
rule caveat, failures, uncertainty, and a next step. Final deliverables are
PROOF.md, audit.py, audit_output.json, LOG.md, and REPORT.md. All were written
inside this folder. No low-noise coexistence theorem has been established.
