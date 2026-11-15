# T285 work log

Task received: 2026-11-14, approximately 21:28 Asia/Tbilisi (17:28 UTC).
User's task: “push this problem forward by one checkable piece.”

## Step 1: orientation and literature search (started 21:28)

The folder initially contained only PROMPT.md. Read the startup memory index and
compute governor state (status ok, owner_away_open). A brain recall surfaced a
previous provisional T285 calculation of an AMP instability constant, not a proof.
The recall command was
`OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall "committee machine statistical computational gap specialization low degree"`.
It finished before an attempted interrupt. No mesh/checklist/brain writes will be
requested: this task's folder-only rule overrides the general shared-state ritual.

`nice -n 15` prints `setpriority: Operation not permitted` in this sandbox.
Checking inherited niceness before any computation; no heavy computation planned.

Web searches begun at 21:28: committee machine specialization rigorous large K;
committee machine low-degree; computational lower bounds for committee machines.
Opened arXiv:1806.05451 (v3, revised 29 February 2024) and arXiv:2512.16556
(soft committee/ReLU, annealed analysis, a different model). Further focused
searches are in progress. The literature search will end within ten minutes.

## Step 2: literature outcome and choice (before derivation)

The inherited process priority is already nice 20, checked with
`OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os, resource; print("nice", os.getpriority(os.PRIO_PROCESS, 0)); print("rss", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'`:
output `nice 20`, `rss 11780096`. The warning is relative niceness stacking.
Use the requested command prefix and verify priority again in the audit script.
No numerical libraries or heavy jobs are needed.

Opened the prior local T285 note: its 3.27 K^2 AMP instability constant uses a
formal Edgeworth expansion and is explicitly not rigorous. Do not count it as a
theorem or repeat its computation as this session's piece.

Opened arXiv:2603.17896v1 by Leonardo Defilippis, Florent Krzakala, Bruno
Loureiro, Antoine Maillard. Its large-width odd-activation specialization result
is explicitly non-rigorous (Remark 4.4 and Appendix E); its even-case theorem
concerns a noisy separable sum, not majority-of-signs classification. Opened
arXiv:2506.05500 by Alex Damian, Jason D. Lee, Joan Bruna: its low-degree
exponents concern fixed index dimension and do not establish the growing-K
prefactor here. Also opened arXiv:2405.15480 (latest title: Fundamental
computational limits of weak learnability in high-dimensional multi-index
models). No settlement of the whole problem found. Literature search ended
within seven minutes; a separate literature note will record exact references.

**Chosen piece:** exact degree-three Gaussian Hermite signal in the odd-K,
orthonormal-teacher hard committee, with the aggregate teacher direction revealed.
Compute the population matrix obtained by contracting the cubic tensor with that
direction, prove its contrast eigengap is asymptotic to an explicit constant/K,
and give an elementary finite-sample spectral recovery bound of order
K^2 d times a logarithm. Audit the constants using exact sign enumeration and a
second combinatorial formula. This is an oracle-assisted special case and an
upper bound, not a low-degree or polynomial-time lower bound. It isolates an
exact K-dependent signal without exchanging replica or state-evolution limits.

## Step 3: proof written

Created PROOF.md. Exact result: the projected cubic matrix is
`-rho_K P_V`, where `rho_K=sqrt(2/pi)(1-2/pi)p_K/sqrt(K)` and
`p_K=binom(K-1,(K-1)/2)/2^(K-1)`. Its eigengap times K tends to
`(2/pi)(1-2/pi)`. Two algebraic derivations are included: Hermite tensor
contraction and direct raw Gaussian moments. The finite-sample proof uses
clipping only in the revealed aggregate coordinate, scalar moment bounds,
a 1/4-net, and an explicit eigenspace calculation. It gives
`O(K^2 (d+log(1/delta)) log(K/epsilon)/epsilon^2)` samples.
The theorem explicitly distinguishes contrast-subspace recovery from
individual-unit recovery and excludes claims about the original thresholds.

Next: exact sign enumeration, Gaussian moment checks, and an adversarial
audit of symmetry, K=3, d=K, and the concentration constants.

## Step 4: deterministic audit completed

Created `audit.py` using only the Python standard library. Ran exactly
`OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1`.
Exit code 0. Full output is in `audit_output.txt`; exact sign coefficients
and eigenvalue checks are in `exact_checks.csv`, and recurrence-versus-lgamma
checks are in `asymptotic_checks.csv`. The run enumerated every sign vector
for K=3,5,...,17 and integrated Gaussian magnitudes analytically. This is
independent of the pivotal-event proof of the Boolean coefficients.

Added the immediate population-moment corollary: all one-sample moments of
feature degree at most two, allowing arbitrary transformations of the binary
label, are determined by K and the aggregate u. The cubic projected matrix
is the first such moment here to expose V. This is explicitly not a bound
on polynomials in the entire dataset.

Clock check at this point: 2026-11-14 17:35:13 UTC, 21:35:13 Asia/Tbilisi.
Earlier step headings used rough elapsed-time estimates; replaced them with
step numbers rather than retain inaccurate clock labels.

Audit output that matters:

```text
priority=20; OMP_NUM_THREADS=1; standard library only
exact enumeration: K=3,5,...,17; all rational identities PASS
largest raw-moment vs tensor eigenvalue error: 1.39e-17
lim K*rho_K = 0.23133503779823
K=100001 K*rho_K=0.231335616131 ratio=1.000002499978
Gaussian moments, variance=2, clipping, concentration constants: PASS
peak RSS (Darwin bytes): 15433728
```

## Step 5: possible removal of the oracle

The exact first moment estimates u. Before final reporting, check whether a
dimension-free Lipschitz bound on the contracted Hermite tensor permits a
sample-split estimator to replace known u. This would strengthen the same
orthonormal-teacher special case without addressing the full threshold problem.
Keep the oracle theorem as proved even if this extension fails.

## Step 6: oracle removed in the orthonormal special case

Added Section 7 to PROOF.md. For the cubic Hermite tensor,
`||C(a)||_op <= sqrt(6)||a||` follows from the exact Gaussian L2 norm
`6<a,h>^2+2||a_perp||^2`. Projection then gives the dimension-free bound
`||N(v)-N(u)||_op <= 5 sqrt(6)||v-u||`.
An independent label-weighted sample mean estimates u with error O(1/K)
using O(K^2 d) samples at fixed confidence. Combining with the clipped
matrix from a fresh batch proves contrast-subspace recovery using
O(K^2 d log K) total samples, for fixed accuracy and confidence, without
revealed teacher information. Full finite-sample constants and failure
probabilities are written in the corollary. The scope remains exact
orthonormal teachers and subspace recovery.

## Step 7: final audit and report

Re-ran the exact command after adding the sample-splitting constants:
`OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1`.
Exit code 0; output now additionally includes
`sample-split extension: Hermite L2=6; constants 19200 and 131072: PASS`.
Final peak RSS: 15368192 bytes. Both runs were below one second and used
inherited nice 20 with OMP_NUM_THREADS=1.

Manually re-derived the Gaussian Hermite L2 bound from moments 15,3,1;
the Markov normalization budget gives exactly 19200; replacing epsilon by
epsilon/2 in the matrix bound gives exactly 131072. Rechecked the Chernoff
substitution, 1/4-net cardinality, clipping bias, and the use of independent
samples when conditioning on an estimated direction.

Cases checked to break the claim: K=3, excluded K=1/even K, d=K, sign of
the eigenvalue, arbitrary external noise directions, subspace versus neuron
recovery, and one-sample moments versus polynomials in all samples. Exact
orthonormality is used in the sign/magnitude independence and remains a
limitation; growing-K Gaussian teacher Gram errors are not controlled here.

Created REPORT.md with a PROVED verdict restricted to the orthonormal special
case, reproduction command, data/output paths, failed extensions, and next
steps. The original thresholds and computational lower bounds remain unproved.
The literature note is SOLVED_ELSEWHERE.md; it records relevant advances
without claiming the whole problem was solved.

Last clock check before final file review: 2026-11-14 17:38:09 UTC,
21:38:09 Asia/Tbilisi.
