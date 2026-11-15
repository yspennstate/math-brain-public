# T177 working log

Task received: 2026-11-14, session started approximately 21:19 Asia/Tbilisi.
Task: “push this problem forward by one checkable piece.”

## 2026-11-14 21:22 — orientation and literature check

Read the startup memory and the existing local memory about a previously refereed
Derrida–Retaux moment reduction. That note reports that survival asymptotics imply
conditional geometric convergence and convergence of all ordinary moments; merely
repeating that reduction would not be a new piece. No scripts that write shared
brain, mesh or checklist state were run: the current task explicitly forbids writes
outside this directory. No git or subagents used.

Read compute_state.json: status warn, mode owner_away_open, CPU saturated. All
computation below will be small, single threaded, nice 15, and bounded in time.

Web searches (web search tool):
- Derrida Retaux critical regime survival probability sharp asymptotics 2026 2025
- Derrida Retaux conjecture geometric conditional distribution critical 2026
- Derrida critical 2026 asymptotics
- A max-type recursive model Conjecture 1

Opened original sources:
- Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi,
  arXiv:1705.04787v2, https://arxiv.org/pdf/1705.04787.
- Xinxing Chen, Yueyun Hu and Zhan Shi, arXiv:2108.05610v1,
  https://arxiv.org/pdf/2108.05610.
- Thomas Duquesne and Zhan Shi, arXiv:2609.11435v1,
  https://arxiv.org/html/2609.11435v1.
- Zenghu Li and Run Zhang, arXiv:2411.13068v3,
  https://arxiv.org/html/2411.13068v3.
- Xinxing Chen, Victor Dagard, Bernard Derrida, Yueyun Hu, Mikhail Lifshits
  and Zhan Shi, arXiv:1907.01601v3 abstract and PDF.

No full solution found in this first check. The September 2026 paper explicitly
says that convergence of the original critical discrete model to its proposed
continuous branching limit has not been proved. Li–Zhang treat geometric random
offspring, rather than the fixed m of this problem.

A formulation issue is already certain: the original 2019 paper assumes X_0 is
not almost surely constant (page 1). The supplied statement omits that assumption.
For m=2 and X_0=1 almost surely, the critical equality holds and X_n=1 forever.
The 2021 survival exponent theorem also assumes an exponential moment at some
t>m, not just the critical first tilted moment. These caveats must be retained.

## Concrete piece chosen before starting the proof

Develop a finite-time quantitative reduction of the conditional law to the local
variation of the survival probabilities. The target is an explicit bound on the
total-variation distance to the predicted geometric law in terms of q_n,
q_{n+1},...,q_{n+L}, with an exponentially small remainder in L and a quadratic
collision error. This is more informative than re-proving the previously known
qualitative implication from a power law, and isolates what must be controlled
to obtain a convergence rate. Independently verify the finite-time identities
using exact rational recursion on small distributions. Also state the omitted
deterministic exception precisely. No claim of a new sharp survival asymptotic.

## 2026-11-14 21:26 — proof and first attempted audit

Wrote PROOF.md. The finite-window bound implies total-variation convergence from
q_n -> 0 and q_{n+1}/q_n -> 1, without a moment or criticality assumption.
An additional consequence is a full first-order signed-measure expansion if
q_n=o(1/n) and q_{n+1}/q_n=1-beta/n+o(1/n). It predicts distance beta/(mn),
conditionally on those unproved local smoothness assumptions.

Initial audit command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_bounds.py > audit_output.txt 2>&1`

It exited before computation: Darwin rejected setting RLIMIT_AS to 768 MB with
`ValueError: current limit exceeds maximum limit`. A separate tiny check also
found RLIMIT_DATA unavailable. Replaced that unsupported limit with a resident
memory guard and a strict small-support limit. A 180 CPU-second cap and 240-second
wall alarm are supported.

The nice wrapper printed `setpriority: Operation not permitted`. A read-only
Python check showed the inherited nice value is already 20, below the requested
priority; the wrapper tries to add 15 to that. The audit keeps the requested
wrapper and records actual priority. No escalation attempted.

## 2026-11-14 21:27 — exact rational audit passed

Repeated the audit with the same command after replacing the unsupported memory
limit:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_bounds.py > audit_output.txt 2>&1
```

Exit code 0. Output:

```text
nice: setpriority: Operation not permitted
PASS: exact rational audits; no distribution truncation
models: 24
exact_one_step: 68
independent_enumerations: 58
critical_moment_checks: 28
finite_window_identities: 147
finite_window_bounds: 147
simplified_bounds: 147
collision_bounds: 68
first_correction_constants: 33
max_support: 129
deterministic_exception_tv: 1/2
actual_nice: 20
peak_rss_bytes: 16859136
data: exact_checks.csv, audit_summary.json
```

This run used approximately 16.1 MiB peak resident memory and less than one
second. Data are exact fractions in exact_checks.csv, and model definitions and
check counts are in audit_summary.json. The output is also in audit_output.txt.
The cases include four nonconstant critical laws, the deterministic critical
exception, subcritical and supercritical examples, the zero law, and sixteen
seeded rational examples with m=2,...,5. Maximum support index is 129. Trailing
zero coefficients are retained, so the zero-law entry's recorded allocated
support endpoint is larger than its actual support {0}.

Two independent routes were compared: polynomial convolution versus direct
enumeration of input tuples; and the signed error computed from the collision
event versus the backward measure identity. All comparisons were exact. The
infinite geometric tail was included analytically in every TV computation.

Literature check ended well within ten minutes; no complete solution found.
One further correction to the supplied background: Theorem 1.1 in the opened
arXiv:1907.01601v3 proves exp(-(p-p_c)^(-1/2+o(1))), not the stronger existence
of the precise constant C in the exponent. This is separate from the critical
problem and is not used in the proof.

## 2026-11-14 21:29 — final independent checks and report

Added an independent check of the first correction from the forward equation:
h(k)-m h(k+1)=beta g(k). The script verifies it exactly at 99 coordinates
for each of 33 (m,beta) pairs. Added AUDIT.md with this derivation, the
generating function beta*m*s*(1-s)/(m-s)^2, the independent lower bound
from the event {1}, and the limit-interchange majorant.

Also proved the reverse implication: when q_n->0, conditional geometric
convergence is equivalent to q_{n+1}/q_n->1, and it is enough to check the
conditional mass at 1. This uses the exact summed recursion and
|R_n-B_n|<=m(m-1)q_n^2, not an asymptotic assumption about the whole law.

Reran the same audit command after adding the independent recurrence check.
Exit code 0, all counts unchanged and all checks PASS. Final complete output:

```text
nice: setpriority: Operation not permitted
PASS: exact rational audits; no distribution truncation
models: 24
exact_one_step: 68
independent_enumerations: 58
critical_moment_checks: 28
finite_window_identities: 147
finite_window_bounds: 147
simplified_bounds: 147
collision_bounds: 68
first_correction_constants: 33
max_support: 129
deterministic_exception_tv: 1/2
actual_nice: 20
peak_rss_bytes: 17285120
data: exact_checks.csv, audit_summary.json
```

Wrote REPORT.md. The exact critical conjecture remains open in this work.
The completed piece is the quantitative scalar-to-conditional-law reduction
and its conditional first-order correction. All files are inside this folder;
no git, external writes, subagents, or background jobs were used.
