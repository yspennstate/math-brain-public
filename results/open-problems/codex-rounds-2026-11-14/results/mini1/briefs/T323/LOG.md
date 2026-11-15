# T323 work log

Session began 2026-11-14 21:30 +04 (17:30 UTC).
Task: “push this problem forward by one checkable piece.”

## 21:30–21:32 +04 — orientation and literature

Read the startup memory index and compute governor state. The governor reported
`status=warn`, `mode=owner_away_open`, CPU saturation, and 54% free memory.
Only small, single-thread checks are planned. No subagents or git.
The task-specific instruction to write only in this folder overrides the older
brain/checklist/mesh write instructions; no commands that mutate those stores
will be run. Read-only search of brain views located an earlier T323 note;
its content is being checked before choosing a result.

Read-only commands: `pwd`, `rg --files ...`, `cat` of the memory index and
compute state, `ls -la`, `date`, and targeted `rg` of the brain views.
The working folder initially contained only PROMPT.md and runner files.

Web searches (2026-11-14):
- `self attention dynamics circle consensus all beta 2025 2026 Geshkovski clustering`
- `"2305.05465" circle Kuramoto synchronization 2025 2026`
- `"self-attention" "all temperatures" circle clustering`
- `self attention dynamics "value matrix" "skew" circle rotation`
- `"self-attention" "general" "V" clustering 2026 sphere value matrix convergence`

Opened arXiv:2507.22857 (abstract and HTML), arXiv:2312.10794 (abstract
and v5 HTML), arXiv:2305.05465 (abstract), and the publisher full text of
“Value Matrix Dynamics and Attractor Selection in a Reduced Transformer Model”.
Corollary 2.5 of arXiv:2507.22857 explicitly covers normalized circle
self-attention for every beta >= -0.16, hence the positive-beta circle
subproblem is already settled. General Q,K,V still needs separate treatment.
The literature check is ongoing, well within the ten-minute limit.

## 21:33 +04 — literature conclusion and chosen piece

The literature check ended after about three minutes. Corollary 2.5 of
Polyanskiy–Rigollet–Yao, arXiv:2507.22857 (2025), settles the normalized
circle case for every positive beta. Theorem 6.1 of the opened v5 survey
covers d >= 3. Thus the identity-matrix assertion in the prompt is already
settled, but this does not settle general Q,K,V. A separate literature note
will record the precise scope. No complete general-matrix theorem was found
in this bounded search; this is not a claim of exhaustive coverage.

Choice, before proof or computation: prove bistability for the explicit
general-matrix family on S^1

    Q = I, K = kappa J, V = a I - omega J,
    J = [[0,-1],[1,0]], a,omega,kappa > 0.

For every even n, aim to prove that a balanced antipodal configuration has
an open basin when beta*kappa*omega > a, while a rotating synchronized
cluster also has an open basin. For n=2, derive the full basin threshold
from a scalar separation equation. The reason for this choice is that it
tests the proposed dependence on the spectrum of V: V has positive definite
symmetric part aI and fixed complex spectrum a +/- i*omega, yet Q,K may
create a stable two-point limit. This is a concrete obstruction and exact
small-case classification, not a proposed solution for arbitrary matrices.

Read-only brain lookup: the navigation index contained a provisional note
about symmetric indefinite V=Q'K=diag(1,1,-mu), a different mechanism.
Its linked file was not at the indexed path (`No such file or directory`);
no mathematical claim here relies on it. Additional searches for skew
query/key matrices and antipodal states did not return this classification.

## Proof drafted

Wrote PROOF.md. The calculation strengthens the planned n=2 piece to every
even n: the balanced antipodal Jacobian is exactly
`-B I + (B/n)11' + (a/n)sigma sigma'`, where B=beta*kappa*omega.
Its transverse eigenvalues are a-B and -B, versus -a at rotating consensus.
A Taylor remainder argument supplies open basins and convergence of the
common phase. For two tokens the scalar basin function is strictly
increasing from 0 to beta*kappa, giving the full threshold including equality.
The proof also compares the identical V with Q=K=I.

Next: independently reconstruct the original Cartesian vector field in a
small standard-library script, finite-difference the full angular Jacobian,
and compare trajectories and thresholds without using the reduced equation
for the original-system integration.

## 21:37 +04 — independent numerical audit

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
```

First run exited 0. Relevant output:

```text
nice: setpriority: Operation not permitted
PASS: 1000 random parameter/angle cases, both query-key choices
maximum angular-velocity discrepancy: 3.442e-15
maximum projection radial residual: 7.772e-16
PASS: 32 full Jacobian comparisons (n=2,4,6,10)
maximum Jacobian discrepancy: 2.847e-10
separatrix (a=omega=kappa=1, beta=2): 1.863372534735285
independent Cartesian root discrepancy: 4.441e-16
uniform antipodal basin probability: 0.406870100550410
PASS: 5 monotonicity scans, including threshold endpoint bound H<q
PASS: 5 original-system RK4 trajectories, each repeated at half step
  pair_consensus: target spread=2.659e-09, half-step error=2.629e-13
  pair_antipodal: target spread=1.808e-09, half-step error=1.099e-11
  pair_identity_key: target spread=3.055e-13, half-step error=1.229e-11
  four_consensus: target spread=3.757e-10, half-step error=4.512e-13
  four_antipodal: target spread=2.123e-11, half-step error=1.615e-12
elapsed seconds: 0.608
data: audit_data.json
```

The `nice` warning requires checking the effective inherited priority;
it is not treated as successful priority setting. Added an explicit
`os.getpriority` assertion (must be >=15), peak-RSS measurement and a
120-second CPU limit. The script already has a 120-second wall alarm.
It uses only the Python standard library and tiny arrays. A repeat will
verify these resource conditions and preserve the final data.

## 21:39 +04 — resource check and mathematical audit

Repeated the identical command after adding the resource assertions. It
exited 0. Final captured output, also saved verbatim in audit_output.txt:

```text
nice: setpriority: Operation not permitted
process niceness: 20; peak RSS bytes: 15499264
PASS: 1000 random parameter/angle cases, both query-key choices
maximum angular-velocity discrepancy: 3.442e-15
maximum projection radial residual: 7.772e-16
PASS: 32 full Jacobian comparisons (n=2,4,6,10)
maximum Jacobian discrepancy: 2.847e-10
separatrix (a=omega=kappa=1, beta=2): 1.863372534735285
independent Cartesian root discrepancy: 4.441e-16
uniform antipodal basin probability: 0.406870100550410
PASS: 5 monotonicity scans, including threshold endpoint bound H<q
PASS: 5 original-system RK4 trajectories, each repeated at half step
  pair_consensus: target spread=2.659e-09, half-step error=2.629e-13
  pair_antipodal: target spread=1.808e-09, half-step error=1.099e-11
  pair_identity_key: target spread=3.055e-13, half-step error=1.229e-11
  four_consensus: target spread=3.757e-10, half-step error=4.512e-13
  four_antipodal: target spread=2.123e-11, half-step error=1.615e-12
elapsed seconds: 0.588
data: audit_data.json
```

The inherited niceness is 20, so the failed attempt to change priority
does not violate the low-priority requirement. The final measured peak
RSS was 15.5 MB. The compute governor read before these runs reported
`status=ok`, `mode=owner_away_open`, and 70% free memory.

Wrote AUDIT.md with a second analytic derivation from the Cartesian mean,
the cubic repulsion at the equality threshold, and explicit checks of
odd n, common-phase neutrality, directed query/key scores, self-interaction,
within-cluster splitting, and moving versus stationary limits. The equal
threshold was the main delicate case: it is not attracting, despite a zero
linear eigenvalue. No mathematical failure was found in the claimed scope.
The attempted extension to unequal antipodal populations does fail, and is
excluded. No exhaustive novelty claim or general Q,K,V classification is made.

## Completion

Wrote REPORT.md with the required `VERDICT: PROVED ...` first line, scoped
to the explicit family rather than the whole open problem. Final readback
confirmed the proof, independent audit, literature note, runnable script,
captured output and JSON data are present. A placeholder scan found no
TODO/FIXME/TBD text. No files outside this folder were written; no git,
subagents, external posts, or background jobs were used.
