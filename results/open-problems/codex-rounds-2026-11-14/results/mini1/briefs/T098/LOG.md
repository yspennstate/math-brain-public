# T098 work log

Task: “push this problem forward by one checkable piece.” Session began
2026-11-14 at approximately 21:58 Asia/Tbilisi (17:58 UTC).

## Scope and startup

All writes stay in this folder. No git, external publication, subagents, or
background workers. The task-specific folder-only rule takes precedence over
global instructions to update the shared brain, mesh, and checklist. Read the
startup memory index and compute governor state without changing either.
Governor: `status=warn`, `mode=owner_away_open`, CPU saturation reported; only a
small serial verification will be run. Python commands will use
`OMP_NUM_THREADS=1`, other numerical thread limits, and `nice -n 15`.

Read-only commands: `pwd`; `ls -la`; `cat
~/.claude/compute/compute_state.json`; read the memory index
and search navigation files with `rg`. Initial folder contained only PROMPT.md,
codex.log, and run.pid. No previous mathematical deliverable was overwritten.

## Literature check (started 17:58 UTC; bounded by ten minutes)

Used the web search tool, including queries:

- `many body localization unconditional proof Imbrie limited level attraction 2026`
- `"Huveneers" "2609.39462"`
- `"many-body localization" "2026" rigorous proof positive energy density`
- `"many-body localization" "proof" "November 2026"`
- `"many-body localization" "limited level attraction" 2026 proof`
- `"many-body localization" rigorous "October" "2026" proof`
- `"many-body localization" "diluted" "transverse field"`

Opened primary sources:

1. John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains*,
   https://arxiv.org/abs/1403.7837 (v4, 30 March 2016). Abstract explicitly
   assumes limited level attraction.
2. Francois Huveneers, *Many-body localization: an introduction for
   mathematicians*, https://arxiv.org/abs/2609.39462 and full HTML
   https://arxiv.org/html/2609.39462v1. Section 4.5 explicitly leaves a
   high-probability extension of its resonance-free argument open and discusses
   LLA. This is consistent with the supplied open status; the simplified
   argument reviewed there should not be confused with Imbrie's full result.
3. Alexander Elgart and Abel Klein, *Many-body localization for the random XXZ
   spin chain in fixed energy intervals*, https://arxiv.org/abs/2602.01441.
   Full abstract and theorem scope are being checked before final citation.

No unconditional solution of the stated full-spectrum problem was found.
Search results alone are not cited as papers.

## Choice (recorded before the proof or computation)

Prove exact full-spectrum probabilistic locality for the interacting Ising
chain with iid Bernoulli-diluted transverse fields:
`gamma_i = xi_i g_i`, with `P(xi_i=1)=p<1` and exact `gamma_i=0` at barriers.
The longitudinal fields may retain the iid law in the question; no assumption
on their density or the size of the couplings is needed for this special case.

Reason: the zero-transverse sites have conserved Z spins. Conditional on those
spins, the active intervals are finite independent quantum blocks. Controlled
block diagonalizers should commute even when two blocks share a frozen
boundary. This gives exact l-bits and an explicit exponential locality tail
without LLA, while making the missing step in the original problem precise:
stability when the barriers acquire nonzero transverse terms.

Planned audit: prove the controlled-unitary support bound algebraically; then
independently assemble small dense Hamiltonians and check diagonalization,
commutators, complete l-bit labels, shared-boundary gates, degeneracies, and
the Bernoulli tail by exact finite enumeration. Exact barriers make this a
restricted solvable case, not a proof for generic nonzero transverse fields.

## Literature check completed, approximately 18:02 UTC

The check took less than ten minutes. Verified the authors and abstract of
Elgart–Klein from the arXiv page and full HTML v3: the energy interval is fixed
at the bottom of the spectrum, so it does not establish positive energy-density
or full-spectrum localization.

Also opened Jessica Kaijia Jiang, Federica Maria Surace, Olexei I. Motrunich,
*Charge Transport Capacity as a Probe of Resonances in Models of Many-Body
Localization*, https://arxiv.org/abs/2604.18710, and the published page
https://journals.aps.org/prb/abstract/10.1103/l7n9-ql9y (16 October 2026;
published author forms Jessica K. Jiang, Federica M. Surace, Olexei I.
Motrunich). This is numerical and perturbative evidence about resonances,
not an unconditional full-spectrum theorem. No SOLVED_ELSEWHERE.md is warranted
by the sources found. This search cannot certify absence of an unindexed paper.

## Algebraic construction and candidate constants

For each maximal active block B, diagonalize its finite Hamiltonian separately
for each assignment of its one or two frozen boundary spins. Promote these
diagonalizers to controlled unitaries V_B. Different V_B commute: their active
targets are disjoint and their overlaps contain only diagonal frozen controls.
Candidate U is the product of V_B, and tau_i = U Z_i U*.

For a one-site operator, only gates whose padded support contains that site
can affect its conjugate. Their union is a support envelope S_i. The right
endpoint exceeds i+r only if the r sites i+1,...,i+r are active; the analogous
left event uses a disjoint set of indicators. For r>=1 this gives the uniform
bound P(R_i>r) <= 2 p^r - p^(2r), with equality for the envelope in the bulk
when both sides have at least r+1 sites. The distinction between this envelope
and the minimal support of a particular operator will be kept explicit.

## Proof written, 18:04 UTC

Created PROOF.md, including the exact finite-volume diagonalizer, complete
l-bits, geometric tail, an expected norm approximation bound, and a local
infinite-volume automorphism. Also proved almost-sure finite-volume simplicity
for absolutely continuous longitudinal fields using a nonzero discriminant
polynomial. This last fact removes the ambiguity between a localized
eigenbasis and arbitrary vectors in degenerate energy eigenspaces; it is
not a quantitative level-spacing estimate.

Audit points identified before computation:

- Shared frozen controls must commute, not be treated as disjoint gates.
- The tail formula requires r>=1 and has finite-boundary corrections.
- The radius describes a common support envelope, not the minimal support.
- At a frozen site the l-bit itself is exactly Z, although a general local
  operator can spread into both adjacent blocks.
- Infinite volume gives a quasi-local algebra automorphism, not necessarily
  a unitary in an unspecified infinite Hilbert-space representation.
- Adding epsilon X at a barrier breaks its old l-bit with commutator norm
  exactly 2|epsilon|. This will be tested, rather than assuming stability.

## Initial verification run

Dependency probe (same thread environment as below):
`nice -n 15 python3 -c 'import numpy; print(numpy.__version__)'` -> `2.2.3`.
macOS printed `nice: setpriority: Operation not permitted`. A read-only libc
`getpriority(0,0)` probe returned `20` with errno 0: this process is already
running at lower priority than requested. `ps` is denied by the sandbox.
The verification script asserts a nice value of at least 15 before doing work.

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

Initial stdout summary:

```text
status: PASS
nice_value_from_libc: 20
peak_rss_bytes: 60211200
elapsed_seconds: 0.4427468340145424
matrix_cases: 69
largest_normalized_matrix_residual: 4.6629367034256575e-15
exact_probability_checks: 855
exact_probability_error: 0
epsilon: 0.03125
barrier_commutator_norm: 0.0625
old_diagonalizer_off_diagonal_norm: 0.0312500000000019
zero_H_GHZ_lbit_variance: 0.9999999999999998
base-three field-only minimum gaps: 2 for L=1,...,8
```

Important diagnostic: NumPy's `@` calls emitted divide-by-zero, overflow, and
invalid-value warnings even though all reported residuals were finite and
small. This run is not accepted as the final numerical audit. Replace matrix
multiplication by explicit unoptimized einsum contractions, make floating
point warnings fatal, and require finite values before accepting the rerun.
The analytic proof does not depend on floating point output.

The first attempt to apply this verification change lacked the patch terminator;
the patch tool rejected it without modifying files. Corrected the patch.

## Accepted independent verification, 18:09 UTC

Preserved the first numerical data as verification_initial.json. Changed every
matrix-matrix product to `np.einsum("ij,jk->ik", ..., optimize=False)`, set
`np.seterr(all="raise")`, and added explicit finite-value assertions. Reran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > verification_stdout.txt 2> verification_stderr.txt
```

Output (the full JSON stdout is in verification_stdout.txt):

```text
status: PASS
nice_value_from_libc: 20
peak_rss_bytes: 57671680
elapsed_seconds: 4.743929790973198
matrix_cases: 69
largest_normalized_matrix_residual: 4.9960036108132044e-15
exact_probability_checks: 855
exact_probability_error: 0
epsilon: 0.03125
barrier_commutator_norm: 0.0625
old_diagonalizer_off_diagonal_norm: 0.03125000000000196
zero_H_GHZ_lbit_variance: 0.9999999999999998
base-three field-only minimum gaps: 2 for L=1,...,8
```

stderr contained only `nice: setpriority: Operation not permitted`; there were
no numerical warnings. The checked libc priority remained 20. Data files:
verification.json (all matrix cases and residual categories), tail_checks.csv
(all 855 rational probability comparisons), verification_stdout.txt, and
verification_stderr.txt. Read back both stdout and stderr after the run.

Independent checks of the load-bearing claims:

1. Assembled each full H by Kronecker products, independently of the bit-flip
   assembly used for conditional blocks; compared both full assemblies too.
   Checked all 62 indicator patterns for L=1,...,5, five seven-site cases,
   and two deliberately degenerate cases: 69 matrices in total, dimensions
   at most 128. Parameters used seeded random real h, g, J except for the
   stated degeneracy cases; this is numerical verification, not interval
   certification.
2. Compared U*HU with the sum of independently computed block energy labels,
   and compared those labels with direct full-H diagonalization. Checked
   unitary and gate commutators, l-bit involutions, mutual and Hamiltonian
   commutators, frozen l-bits, and completeness using the distinct spectrum
   of a binary-weighted sum of l-bits.
3. Checked both conjugation directions on each site's X, Y, Z by partial
   trace onto the proposed envelope. This tests general one-site operators
   by linearity, including frozen-site X operators that spread both ways.
4. Independently found envelopes by (a) unions of padded blocks and (b)
   scans to the nearest frozen sites. Enumerated all 1022 indicator patterns
   for L=1,...,9. For p=1/3,1/2,2/3, used exact rational arithmetic for all
   sites and r=1,...,L: 855 probability checks, error exactly zero. Tested
   finite-boundary corrections as well as the bulk inclusion-exclusion
   formula. At L=9, site 5, p=1/2, the probabilities for r=1,2,3 are
   3/4, 7/16, 15/64. For r=4, the physical boundary forces probability 0,
   while the uniform bound remains 31/256.
5. Re-derived the simplicity proof's field-only gap lower bound by exact
   integer enumeration at h_i=3^(i-1): minimum gap 2 for L=1,...,8.
6. Tested the failure under one barrier perturbation on five sites:
   epsilon=1/32 gives commutator norm 1/16 exactly numerically, and old-U
   off-diagonal norm 1/32 to about 2e-15. The Pauli calculation in PROOF.md
   gives these numbers independently without diagonalization.
7. Tested the degeneracy caveat with H=0 and a GHZ vector. Its variance of
   Z at a barrier is 1, so an arbitrary degenerate eigenvector need not
   carry a definite l-bit label. The proof only asserts a complete common
   eigenbasis in that generality and proves simplicity separately for
   absolutely continuous fields.

The exact-barrier result is elementary and no claim of literature novelty is
made. It isolates a tractable special case; it does not establish a stable
MBL phase for nonzero transverse terms at the barriers.

## Report and final scope audit

The first report patch also lacked its patch terminator and was rejected
without mutation; reapplied it with the terminator.

Wrote REPORT.md with verdict PARTIAL, the exact special-case hypotheses,
commands and outputs, opened-paper references, the rejected first numerical
run, and the missing stability step. Re-read verification.json and the tail
data after the accepted run. The report distinguishes exact rational checks
from floating-point matrix checks and does not claim a solution of T098 or
literature novelty. Final check will read back the report and inspect the
deliverable names and sizes. No further computation is needed after the
passing independent checks.

Final readback completed: REPORT.md begins with the required `VERDICT: PARTIAL`
line. All named proof, script, data, and output files are present in this
folder. The largest generated data file is about 22 KB; the computational
run stayed below 58 MB RSS and five seconds. The final report preserves the
distinction between the proved exact-barrier family and the unsolved
nonzero-barrier stability question. Task completed for this session.
