# T098 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, approximately 01:28 Asia/Tbilisi (14 November,
21:28 UTC). All writes remain in this folder; the earlier folder is read-only.
No git, subagents, shared-brain/mesh/checklist writes, or external messages.
The task-specific folder-only instruction overrides those global write duties.

## Startup and literature check

Read the earlier REPORT.md, LOG.md, PROOF.md and verify.py. Read the startup
memory and compute state without invoking recall commands that log elsewhere.
Compute state: warn, owner_away_open, CPU saturation; only small serial checks
are planned, with thread limits and nice -n 15. No heavy computation is needed.

Within the five-minute literature allowance, searched with the web tool:
`many body localization unconditional proof limited level attraction November
2026 Imbrie`; `many body localization 2026 2027 rigorous proof full spectrum one
dimensional`; `"many-body localization" "unconditional" "2026" proof`;
`"many-body localization" "November" "2026" theorem`.
Opened John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains*,
https://arxiv.org/abs/1403.7837, and Francois Huveneers, *Many-body localization:
an introduction for mathematicians*, https://arxiv.org/html/2609.39462v1,
including Section 4.5. The former retains the level-attraction hypothesis;
the latter discusses the outstanding high-probability step. No new solution
was found. This is a bounded search, not a certificate of nonexistence.

## Earlier result: analytic recheck before extension

Re-derived the controlled-block identity: in each frozen-spin sector the
Hamiltonian is a sum of disjoint active-block matrices plus scalar frozen
terms. Their controlled diagonalizers commute because their only overlap is
diagonal control projectors. Conjugation therefore cancels every gate missing
the original support; it cannot propagate through successive gates. For a
fixed site and r>=1, extension past i+r is equivalent, when the boundary
allows it, to r active indicators immediately to the right. Left and right
events use disjoint indicators. This independently recovers
P(R_i>r)<=2p^r-p^(2r), with the earlier boundary qualification. The simplicity
discriminant argument and degenerate-eigenvector qualification also hold.
No error found in the earlier theorem. A fresh small-matrix audit will follow.

## Choice (recorded before extension)

Prove a volume-uniform anti-concentration estimate for every transition
denominator caused by flipping one formerly frozen spin, simultaneously over
the adjacent block eigenstates and the outer frozen-spin assignments. Assume
its independent longitudinal field has density bounded by rho. This is the
specific next target in the earlier report. Count only the two adjacent active
blocks, then average their geometric sizes. Determine both the linear regime
and the weaker bound when the naive geometric moment diverges. This supplies
one first-step resonance estimate, not stability under repeated rotations.

## Independent audit of earlier result: PASS

Created audit_earlier.py, assembling the diagonalizer as a direct sum over
frozen-spin sectors of tensor products of block eigenvectors. This differs
from the earlier script's product of embedded controlled gates. Independently
assembled the full Hamiltonian from Pauli tensor products, checked its
diagonalization and l-bit commutators for all 62 masks at L=1,...,5. Independently
enumerated padded-block support probabilities using exact rational weights.

Command:
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_earlier.py > earlier_audit_stdout.txt 2> earlier_audit_stderr.txt
```

Output: PASS; 62 matrix cases; largest normalized residual
1.5051624251407905e-15; 612 exact rational probability checks, zero error;
peak RSS 33,193,984 bytes; elapsed 0.1324 seconds; actual nice value 20.
stderr contains only `nice: setpriority: Operation not permitted`: the inherited
priority is already lower than nice 15, verified by libc. No numerical warnings.
Read back both streams. The earlier exact-barrier claim holds in this audit.

## Extension written: first-step denominators

Wrote PROOF.md. For a frozen f and m adjacent active spins, every relevant
energy difference is 2 h_f + c, with c independent of h_f. At most four outer
frozen assignments and 4^m state pairs give conditional probability at most
min(1,4 rho delta 4^m). Spectators cancel: there is no factor 2^L.
For the infinite-line dominating size M, P(M=k)=(k+1)(1-p)^2 p^k.
The resulting capped sum F_p(t), t=4 rho delta, is explicit. It is O(t) for
p<1/4, O(t log^2(1/t)) at p=1/4, and O_p(t^alpha log(1/t)) for p>1/4,
alpha=log(1/p)/log 4. A fractional-power bound independently shows convergence
to zero for every p<1. The divergence of the uncapped first moment at p=1/4
does not imply a physical transition.

Audit targets before accepting: slope two (interval length delta, not twice
delta), both empty adjacent blocks, outer-boundary multiplicity, reverse-flip
double counting, spectators sharing outer controls, exact p=1/4, exact powers
of four in the floor formula, and finite-volume truncation. No subsequent
rotation or independence of spatial resonance events is claimed.

## First denominator audit and added spectator test

Initial denominator audit passed: 135 conditional matrix cases, 240 integrated
uniform-field interval unions, 108 exact capped-sum comparisons, and 126 exact
finite-volume domination checks. The largest absolute spectral residual was
2.49e-14. Added an explicit seven-site test with active spectators at both
ends sharing the outer controls, to test spectator cancellation in a full
Hamiltonian rather than only in the algebraic proof. The added test failed
on its first run; inspecting the traceback and basis indexing before drawing
a conclusion. The previous passing JSON is not the result of that failed run.

The failing test accidentally placed active labels in the outer-control bit
positions and conversely. On the reduced five-site interval the order is
(eta_left, active_left, f, active_right, eta_right), so the correct index is
16 eta_left + 8 active_left + 4 f + 2 active_right + eta_right.
Corrected that fixture; no theorem or bound was changed. The independent
support partial-trace check had already passed before that assertion. Saved
the failing traceback as spectator_initial_stderr.txt and reran the full suite.

## Accepted denominator audit: PASS

Command (also used for the initial and corrected runs):
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_denominators.py > denominator_stdout.txt 2> denominator_stderr.txt
```

Final output, read back from stdout and denominator_verification.json:

```text
status: PASS
conditional matrix cases: 135
largest physical matrix dimension (including spectator test): 128
max_block_spectrum_error: 1.9539925233402755e-14
max_field_shift_error: 2.2315482794965646e-14
max_difference_operator_error: 2.4868995751603507e-14
max_overlap_unitarity_error: 1.1224923650381607e-14
uniform_field_interval_union_checks: 240
factor_four_saturation_probability: 1/16
degenerate_interval_probability: 1/64
exact_capped_sum_checks: 108
fractional_power_checks: 108
finite_volume_domination_checks: 126
spectator_support_error: 1.3693519822168146e-15
spectator_energy_cancellation_checks: 64
nice_value: 20
peak_rss_bytes: 36175872
elapsed_seconds: 0.20186487497994676
```

stderr again contains only the redundant nice adjustment denial. All NumPy
floating-point warnings are fatal; none occurred. A final rerun after correcting
the reported largest dimension to include the spectator test gave the values
above. No further computation is needed.

Independent checks of load-bearing quantities:

1. The 135 sector matrices include a,b=0,...,3 with a+b<=5, all four choices
   of existence of the outer controls, and all their signs. Direct restriction
   of the full Pauli Hamiltonian agrees with independently assembled left/right
   block eigenvalue sums. The field shifts verify coefficient +/-1 for each
   sector, hence coefficient 2 in the transition denominator.
2. A Kronecker-difference operator independently reproduces every pairwise
   eigenvalue difference for m<=3. This tests the d^2 count without assuming
   pairwise independence. Overlap matrices between the two eigenbases are
   unitary, including nontrivial transverse fields.
3. Integrated the union of all h_f resonance intervals against a uniform
   density in 240 cases. For m=0 with J_left=1,J_right=3, h_f uniform on
   [-8,8], delta=1/4, four disjoint intervals give probability exactly 1/16
   =4 rho delta. This saturates the factor four over outer controls. With
   all offsets coincident the probability is 1/64, checking that multiplicity
   does not mean independence. These last two checks use exact rationals.
4. Evaluated the capped sum independently as a double geometric expectation
   with collapsed tails, exactly in rational arithmetic. Compared to the
   closed formula at p=1/10,1/4,1/2,9/10, t=1,2,1/2 and on either side of
   eight powers of four: 108 exact comparisons. All matched. At t=1/65536,
   F_(1/4)=109/262144 and F_(1/2)=6913/262144. Fractional-power checks used
   q=1/32, admissible even at p=9/10; these use floating-point arithmetic.
5. Enumerated every finite-chain mask for L<=6, every distinguished frozen
   site, three p values, and two t values: 126 exact checks of finite-volume
   domination. This includes a chain consisting of f alone.
6. The seven-site full Hamiltonian has active end spectators, frozen controls
   at sites 2 and 6 (one-based), active neighbors of f=4, and an exact frozen
   f. Partial trace verifies that U*X_f U is identity on the spectators.
   For every outer assignment and all 16 local pairs, changing either
   spectator label preserves the energy difference: 64 checks.

The proof's asymptotics were also re-derived by splitting the geometric
series at K and by the separate fractional-moment estimate. Constants,
signs, empty intervals, degeneracies, physical boundaries, reverse flips,
spectator cancellation, and the critical p=1/4 case have been checked.

## Scope audit and report

Wrote REPORT.md with verdict PARTIAL: this proves the requested first-step
anti-concentration lemma under a bounded field density, not the full T098
statement. It applies to all local transition labels simultaneously at a
specified site and has constants independent of L. The capped geometric
majorant tends to zero for every p<1, but can be weak near p=1; for example
F_(9/10)(1/65536)=403174072157/512000000000, about 0.78745.

What remains: construct and bound the first rotation on good cells, then
control overlapping cells and the second-order denominators. The affine-field
argument cannot be assumed to survive those rotations. No spatial independence,
LLA theorem, or full nonzero-transverse-field stability follows here. The
result is elementary; no literature novelty is asserted.

Final artifact audit: parsed both Python files, checked that each stored JSON
exactly matches its accepted stdout and has status PASS, checked both stderr
streams contain only the nice adjustment denial, and checked the exact report
verdict and required file presence. The check ran under the same thread limits
and nice -n 15 via a short read-only Python command. Output:
`Final artifact audit: PASS; JSON matches stdout; both accepted suites passed;
required files present.` No files outside this folder were modified.
