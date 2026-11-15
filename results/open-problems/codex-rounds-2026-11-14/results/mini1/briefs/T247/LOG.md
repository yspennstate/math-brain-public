# T247 work log

Task received: 14 November 2026, approximately 22:08 Asia/Tbilisi (18:08 UTC).
Task: “push this problem forward by one checkable piece.”

## 18:08 UTC — orientation and literature search started

Read the local memory index, brain navigation index, mesh protocol, and compute state. The task-specific instruction to write only in this folder overrides the global instructions to update the shared mesh, checklist, and brain. Those external stores will not be mutated. No subagents or git operations.

Command used for read-only orientation: `OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY' ... PY` with pathlib reads and `os.getpriority(os.PRIO_PROCESS, 0)`. The shell reports `nice: setpriority: Operation not permitted`, but Python reports inherited niceness **20**, already lower priority than requested. Keep that inherited priority. Compute state: `warn`, `owner_away_open`; no heavy computation planned.

Initial web queries: “deep neural network Jacobian spectrum simultaneous depth width limit orthogonal dynamical isometry 2025 2026”; “Collins Hayase asymptotic freeness Jacobian growing depth Pastur Slavin”. Relevant results include Collins–Hayase (arXiv:2103.13466), a 2026 paper on fixed-gates Lyapunov exponents, and a 2025 paper on designed orthogonal Jacobians. Need to open and distinguish these from the requested joint limit.

## 18:11 UTC — literature check and chosen piece

Opened the original paper (arXiv:1711.04735), Collins–Hayase (arXiv:2103.13466, PDF), Hanin–Nica (arXiv:1812.05994, abstract), Hanin–Paouris (arXiv:2005.08899, PDF), Hanin–Jiang (arXiv:2503.07872, PDF), Massucco–Murari–Schönlieb (arXiv:2508.02882, current abstract), and the PMLR page for Haas–Gatine–Cosse–Bouraoui (2026). The latter PDF could not be fetched with the web tool. Additional searches used “Jacobian spectrum joint depth width orthogonal limit”, “dynamical isometry growing depth theorem”, and the exact titles of the Gaussian-product and Pastur papers.

Important nearby progress: Hanin and Jiang prove a joint-limit theorem at any relative rate for products with i.i.d. entries, for squared singular values raised to the power 1/depth. It extends the Gaussian result of Hanin and Paouris. This is the linear product problem with a different normalization, not a theorem for derivative-dependent nonlinear factors or sigmoid dynamical isometry. The 2026 Haas et al. abstract treats fixed gates and Lyapunov separation. No solution of the stated nonlinear joint-limit problem was located. This is a bounded literature check, not a proof of absence. Search started 18:08 UTC and selection made by 18:11 UTC, within ten minutes. References and exact scopes will be recorded in LITERATURE.md.

**Choice before proving:** derive exact first and second trace moments, at every finite width and depth, for the independent-gate orthogonal surrogate: independent Haar O_l and diagonal D_l, with i.i.d. squared entries a_li of mean 1 and variance v_l. This is one part of the free-probability prediction that can be checked without asymptotic freeness. The rank-one two-moment recursion should make all accumulated width errors explicit. Consequences to check: the regime in which the free second moment is accurate, the gate-variance scaling needed for mean-square empirical isometry, and whether that implies control of every singular value. The actual network's gate/weight dependence remains outside this piece. No claim of novelty for the underlying Haar moment identity.

## Derivation saved

Wrote PROOF.md and LITERATURE.md. The exact formula obtained is E Z_L = (n+2)/3 [product_l(1+3 v_l/(n+2))-1], where Z_L = Tr((J_L J_L^top-I)^2)/n. The first trace stays mean one, and its variance is E Z_L/n. The finite-width error against the free prediction sum v_l is bounded above by 3 V^2 exp(3V/(n+2))/(2(n+2)). The proof includes a second derivation of the product factor via the fourth moment of one vector's norm.

Checks still to perform computationally: exact rational recursion against product formula; direct two-dimensional Bernoulli gate integration; simulated matrix products; the tanh variance coefficient 8; joint-regime values; and the kernel counterexample that prevents upgrading empirical to uniform isometry. Proof statements are limited to independent gates. The literature correction that the orthogonal Pastur paper has one author is recorded.

## Verification script saved

Created check_moments.py. It sets all common numerical thread counts to one before importing NumPy, has a 180-second alarm, checks inherited niceness, uses only matrices of size at most 8 in simulation, and records peak RSS. It independently integrates the two-layer n=2 Bernoulli case over Haar angle and all 16 gate choices using rational arithmetic. Simulation is diagnostic; the proof does not rely on simulation. Planned exact command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check_moments.py > verification_output.txt 2>&1`.

## 18:15 UTC — first verification run and audit

Ran the exact command above. Exit status 0. Output: 95 exact rational cases passed; independent circle integration s=15/4 and t=19/8; the three matrix simulations have maximum discrepancies 0.761, 1.045, and 0.806 estimated standard errors. Tanh v(q)/q^2 at q=0.0001 is 7.992008098, approaching the proved limit 8; changing Gaussian quadrature from 128 to 256 nodes changes the variances by at most 2.26e-13 relatively. Runtime 2.78 seconds, peak RSS 36.3 MiB, inherited niceness 20. Full output saved in verification_output.txt; all numerical estimates, standard errors, seeds, and parameters are in results.json.

Audited the distinction between distortion about 1, spectral variance about the random empirical mean, and randomness of that mean. Added the exact expected spectral variance (1-1/n) E Z_L to PROOF.md; this also resolves the n=1 boundary, where spectral variance is zero although the scalar gain is random. The formula was checked at zero gate variance, zero depth, width one, inhomogeneous variances, and the two-dimensional exact integral. Added explicit upper/lower error-bound checks to the rational verification script; rerun needed after this small addition. The attempted upgrade from empirical to uniform isometry fails by the Bernoulli kernel example, not by an unproved heuristic. Actual gate/weight dependence is the remaining mathematical obstruction.

## 18:16 UTC — final verification and report

Reran the command after adding bound checks:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check_moments.py > verification_output.txt 2>&1
```

Exit status: 0. Exact saved output:

```text
nice: setpriority: Operation not permitted
Exact rational cases: 95 passed (including error-bound checks)
Independent circle integration: s=15/4, t=19/8
Monte Carlo n=2, L=2, samples=12000: max error 0.761 SE
Monte Carlo n=4, L=8, samples=8000: max error 1.045 SE
Monte Carlo n=8, L=6, samples=6000: max error 0.806 SE
tanh v(q)/q^2 at q=0.0001: 7.992008098 (limit 8)
128/256-node quadrature max relative difference: 2.26e-13
v=1, L=n=100: E Z/n=5.831512996 (free 1)
v=1, L=n=1000: E Z/n=6.304755773 (free 1)
v=1, L=n=10000: E Z/n=6.356092964 (free 1)
Kernel example n=100, L=10: E Z=0.101145248, log P(invertible)=-10.0503359
Kernel example n=10000, L=100: E Z=0.010001015, log P(invertible)=-100.005
Kernel example n=1000000, L=1000: E Z=0.001000001, log P(invertible)=-1000.0005
Niceness: 20; peak RSS: 36.5 MiB; runtime: 2.81 s
All checks passed; data written to results.json
```

Recorded the finite-width proof, joint empirical criterion, exact failure of uniform isometry, all scopes and limitations, verification command, literature findings, and next mathematical target in REPORT.md. No external files, git state, messages, or accounts were modified.

Final read-only artifact audit: a small `OMP_NUM_THREADS=1 nice -n 15 python3` pathlib/JSON check verified the verdict line, all six supporting files, 95 passing rational cases, memory/runtime bounds, niceness, single-thread settings, and the success marker in saved output. Output: `Final artifact audit passed: report, proof, log, literature, script, data, and exact output are present and consistent.` Exit status 0. Work completed within this folder.
