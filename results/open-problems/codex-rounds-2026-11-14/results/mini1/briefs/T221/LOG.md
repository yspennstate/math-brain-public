# T221 work log

Task: “push this problem forward by one checkable piece.” Session began
2026-11-14 22:06 Asia/Tbilisi (18:06 UTC).

## 22:07 — orientation and literature search started

Read the startup memory index and compute state, and listed this folder. The
folder initially contained PROMPT.md and runner logs only. Compute state was
`warn`, mode `owner_away_open`; no substantial computation is planned.
The task-specific instruction to write only in this folder supersedes the
global instructions to update the external brain, checklist, and mesh. Those
external state-mutating commands will not be run. No subagents or git.

Read commands: `pwd`; `ls -la .`;
`sed -n '1,160p' ~/.claude/projects/-Users-user/memory/MEMORY.md`;
`cat ~/.claude/compute/compute_state.json`.

Web searches: `"Rokhlin" "Bernoulli" "2026" entropy`;
`"RBS" "Rokhlin" entropy 2025 2026`;
`"Rokhlin entropy" "Bernoulli shifts" solved`.
Results include Seward's original paper, a 2026 ICM survey still posing the
positive-Rokhlin-entropy existence question, and Bowen–Chapman's
arXiv:2511.06586 concerning invariant random subgroups. These are leads,
not yet grounds to declare the original problem resolved.

## 22:08 — literature check completed; concrete choice

Opened Brandon Seward, *Krieger's finite generator theorem for actions of
countable groups II*, arXiv:1501.03367v4, including the PDF introduction,
Theorems 1.10 and 1.12. Opened Lewis Bowen and Michael Chapman,
*Surjunctivity does not characterize cosoficity of invariant random subgroups*,
arXiv:2511.06586, including Theorem 4.1 and its finite-window formulation.
Also opened Tim Austin's 2026 ICM survey *Some Recent Developments in
Structural Ergodic Theory*, and the arXiv page for Zongrui Hu, Leiye Xu,
Shuhao Zhang, arXiv:2607.11549. No resolution of RBS for arbitrary groups
was found. The IRS result is related prior work, not a resolution for groups.
Search occupied less than four minutes, below the ten-minute cap.

Choice, before starting the proof: prove a finite-witness reduction with an
explicit correction partition, then use the witness to lift a hypothetical
counterexample to a finitely presented group. This is one reduction, not a
claim to prove RBS. The point is that a single finite multiplication pattern,
local rule, and decoder can certify an entropy gap; no global generating
claim needs to be guessed by a search. Seward's two stated theorems will
handle the infinite-base caveat in a corollary. Bowen–Chapman already give a
related and sharper conditional-entropy criterion in the IRS setting;
the contribution here is a self-contained explicit correction construction
and the finitely presented lifting argument, without a claim of priority.

Planned checks: verify both directions of the entropy formula, noncommutative
coordinate order, dependence on finite product sets, preservation of all
collisions when passing to a finitely presented cover, and the infinite-base
corollary. A small exhaustive Boolean-code calculation will audit the
correction construction by independent probability calculations.

## 22:12 — proof written; audit launch exposed a platform limit

Wrote PROOF.md: variational formula, explicit rank correction, finite-subgroup
exclusion, finitely presented lift, and the full-conjecture corollary using
Seward's two theorems. In particular, the infinite-base case is not silently
discarded. The construction reads products in the order DS.

Wrote audit_local_codes.py to enumerate 768 binary encoder/decoder pairs
(16 encoders × 16 decoders × 3 rational bases) with exact probabilities.
The first run used:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_local_codes.py
```

It exited before enumeration: `nice: setpriority: Operation not permitted`,
followed by `ValueError: current limit exceeds maximum limit` while trying
to set RLIMIT_AS to 768 MiB. No mathematical output was produced. Next:
inspect the inherited priority and resource limits, and adjust the memory
guard to this Mac's supported limits without increasing process priority.

## 22:13 — exhaustive audit passed

Diagnostic command:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os,resource; print("priority",os.getpriority(os.PRIO_PROCESS,0)); print("AS",resource.getrlimit(resource.RLIMIT_AS)); print("RSS",resource.getrlimit(resource.RLIMIT_RSS)); print("RSS_usage",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'
```

Output: priority 20; AS and RSS limits both
`(9223372036854775807, 9223372036854775807)`; RSS 11,452,416 bytes.
The inherited process is already at nice 20. The `nice -n 15` wrapper emits
`setpriority: Operation not permitted`, but Python still runs at priority 20,
as asserted inside the audit. No priority increase was attempted to bypass it.
Removed the unsupported RLIMIT_AS call; the enumeration is bounded to 768
small records, has a 60-second alarm, and records/checks peak RSS below 1 GiB.

Successful command (exit 0, under one second):

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_local_codes.py
```

Output, apart from the explained `nice` diagnostic, is saved verbatim as
`local_code_audit.json`. Main values:

| P(input=1) | pairs | exact negative gaps | exact zero gaps | exact positive gaps |
|---|---:|---:|---:|---:|
| 1/2 | 256 | 0 | 36 | 220 |
| 1/3 | 256 | 0 | 36 | 220 |
| 2/3 | 256 | 0 | 36 | 220 |

Total: 768 pairs; 6,144 pointwise reconstruction checks; floating minimum
gap 0.0 for each base. Maximum entropy-chain discrepancy
2.220446049250313e-16; maximum subadditivity excess 0.0. Effective nice
priority 20; peak RSS 16,515,072 bytes. Data: local_code_audit.csv.

Independent checks inside the run:

1. Compute every joint (Y,residual) distribution by summing the eight input
   triples with exact Fraction probabilities.
2. Recompute the same distribution by conditioning on the middle bit and
   multiplying the independent left and right conditional distributions.
   Exact dictionary equality is required in every case.
3. Compute H(Y,residual) directly and separately as H(Y)+H(residual|Y).
4. Re-derive the sign of every cost-minus-base-entropy value without logs.
   For a common probability denominator Q, exponentiating Q times the gap
   gives Q^Q times the product of base counts to their own powers, divided
   by the analogous output and residual products. Compare integers exactly.
   The 108 zero-gap cases are exact equalities, not rounding decisions.

This tests the construction and a small known case over Z. It is not
evidence that unrestricted RBS follows from bounded tests.

## 22:14 — proof audit and final report

Added the exact integer-product gap formula (10) for every rational finite
base, not only the binary audit. It follows by writing each entropy as
log Q minus (1/Q) times the sum of n log n; the audit independently uses
the equivalent product formula in the binary case.

Checked the proof by tracing the two directions separately. The correction
alone proves h <= local cost. Approximation starts with a countable
finite-entropy generator, chooses the decoder first, truncates its finitely
many labels second, and only then approximates by a local function. This
order avoids assuming that one fixed decoder works for all approximations.
The finite-alphabet entropy continuity estimate is proved directly, and
both error terms can be made small after the decoder window is fixed.

Cases explicitly examined:

* Noncommutative groups: Y_t reads x_{ts}, so the support is DS. The word
  list for the lift includes every v_t w_s and the identity coordinate.
* Equal coordinates: impose every equality among that list. Unequal
  coordinates cannot become equal because the presented group still maps
  onto H. This is the independent quotient-map check on the distribution
  argument; imposing relations alone would not justify the inequality claim.
* Finite H: a full-name entropy calculation contradicts a strict witness.
  Thus the presented cover is infinite; finite-group ergodicity is never used.
* Decoder error 0 or 1 and zero probabilities: correction entropy remains
  valid with 0 log 0=0; integer products use 0^0=1. A one-point supported
  base has entropy zero and cannot have a strict negative entropy witness.
* Countable and nonatomic infinite-entropy bases: Section 6 uses Seward's
  exact dichotomy. It does not infer entropy monotonicity under factors.
* Finite entropy with infinite countable support: Theorem 1.10 supplies a
  failing finite uniform base whenever the original base fails.

Final independent artifact audit parsed the script AST, read all CSV rows,
and recomputed sign totals: 768 rows, 108 zero signs, 660 positive signs,
0 negative signs; these agree with the JSON totals. The final file listing
contains the proof, report, log, script, CSV, JSON and the pre-existing runner
files. A first literal-string presence check returned false because equation
10 is written as a LaTeX tag, not the literal text `(10)`; the corrected
check for `\\tag{10}` and the theorem references passed. No mathematical
test failed. No git, external state writes, subagents, or heavy computation.

Wrote REPORT.md with a PARTIAL verdict: the reduction is proved, but RBS
itself remains unresolved. The report identifies prior overlap and gives
the exact run command, data, launch failure, limitations and next step.

## Exact output of the successful audit command above

```text
nice: setpriority: Operation not permitted
{
  "group": "Z",
  "S": [
    0,
    1
  ],
  "D": [
    0,
    1
  ],
  "input_support": [
    0,
    1,
    2
  ],
  "cases": [
    {
      "p_one": "1/2",
      "rules_and_decoders": 256,
      "negative_gap_exact": 0,
      "zero_gap_exact": 36,
      "positive_gap_exact": 220,
      "min_gap_float": 0.0,
      "max_chain_difference": 2.220446049250313e-16,
      "max_subadditivity_excess": 0.0
    },
    {
      "p_one": "1/3",
      "rules_and_decoders": 256,
      "negative_gap_exact": 0,
      "zero_gap_exact": 36,
      "positive_gap_exact": 220,
      "min_gap_float": 0.0,
      "max_chain_difference": 2.220446049250313e-16,
      "max_subadditivity_excess": 0.0
    },
    {
      "p_one": "2/3",
      "rules_and_decoders": 256,
      "negative_gap_exact": 0,
      "zero_gap_exact": 36,
      "positive_gap_exact": 220,
      "min_gap_float": 0.0,
      "max_chain_difference": 2.220446049250313e-16,
      "max_subadditivity_excess": 0.0
    }
  ],
  "probabilities": "exact fractions",
  "gap_sign": "exact integer-product comparison",
  "total_rules_and_decoders": 768,
  "pointwise_reconstruction_checks": 6144,
  "nice_priority": 20,
  "peak_rss_bytes": 16515072
}
```
