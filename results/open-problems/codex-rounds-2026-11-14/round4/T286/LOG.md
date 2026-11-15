# T286 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Started 15 November 2026, 06:30 Asia/Tbilisi.

## Orientation and bounded literature check

Read REPORT.md and LOG.md from the original session, and REPORT.md, LOG.md, PROOF.md and check_cubic.py from round 3. The original folder has no PROOF.md or scripts. Read the startup memory and compute state. Compute is warn / owner_away_open with saturated CPU; use only tiny one-thread calculations. The task's explicit folder-only restriction overrides external mesh, checklist and brain writes. No git, external mutations or subagents.

Literature search began at about 06:30 and ended at 06:32, within five minutes. Queries: `"2510.24616" neural network rigorous general activations`; `"Bayes-optimal learning" "extensive-width" 2026 proof`. Opened https://arxiv.org/abs/2408.03733, https://arxiv.org/abs/2510.24616, https://arxiv.org/html/2510.24616v5 and https://arxiv.org/html/2605.10395v1. The latest displayed 2510 version is v5 (24 July 2026). Remark 4 still conjectures exactness; Appendix B.6 explicitly assumes Gaussian replacement and replica concentration. The 2605 paper calls its decoupling heuristic. No subsequent rigorous solution was found in this bounded search. This does not prove absence of a solution. No SOLVED_ELSEWHERE.md is warranted.

## Recheck of round 3

Read its full proof and verifier. The Wick identity gives V=C+(3/(2k))||sum_i(r_i-1)u_i||². Row sign symmetry makes different off-diagonal cubic edges uncorrelated. Thus Var(C)=(M6-M3²)/k+30(k-1)M3/(kd³), with M_p=prod_{a<p}(1+2a/d). The bias of C is 6/d+8/d². Independently separating B's mean and variance gives E[B]=3/d+12/d² and Var(B)=O(d^-3), so the constants 36+18/gamma and 81+18/gamma follow. This reproduces the main asymptotic argument without using the verifier's exact Cov(C,B) formula.

Reproduction command (read-only execution of the earlier script; bytecode disabled):

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T286/check_cubic.py > recheck_cubic.out 2>&1
```

Next: inspect its saved output, then select and record one extension before proving it.

Output: all five exact Wick checks pass; ALL CHECKS PASSED. Actual priority is 20 (the inherited priority is already below 15; nice reports a denied further adjustment), peak RSS 15,056,896 bytes. At d=16384, gamma=1 gives rescaled true MSE 99.058984724, tending to 99. Round 3's main result holds.

## Choice (06:34 local)

Choose ONE extension: a quantitative fresh-input Gaussian integration-by-parts / smooth replacement lemma for the cubic activation, valid for finitely many networks with arbitrary joint coupling provided each marginal is the Gaussian weight prior. This includes teacher and finitely many cavity-posterior replicas. Prove an explicit O(d^-1/2) averaged Stein discrepancy using tensor contractions, retaining the linear chaos caused by fluctuating row norms. Compute the prior self-contraction exactly. Show how the normalized average over n=alpha*d² samples behaves for tests with bounded derivatives. This addresses the next step named by round 3 without claiming control of the full likelihood-weighted log partition.

Reason: the cavity removes dependence of the omitted input from the weights, but the replicas remain dependent. A deterministic contraction inequality followed by the Bayes marginal identity can handle that dependence without assuming independent posterior draws after averaging. The full posterior and a continuum of replicas inside log Z still require additional work.

## Tensor derivation

Write F=I3(T)/sqrt(6)+b·X, T=k^-1/2 sum_i u_i^tensor3 and b=sqrt(3/(2k))sum_i(r_i-1)u_i. Let D(W)=||T contraction_2 T||_F². Direct row-parity enumeration gives

```
delta = E[D] = M6/k + ((k-1)/k)*M3²*(1/d + 3/(d*(d+2)) + 15/(d*(d+2)*(d+4))).
```

The three two-row partitions contribute respectively r_i²*r_j²*q_ij², r_i*r_j*q_ij^4 and q_ij^6; the all-equal partition contributes r_i^6. Thus d*delta -> 1+1/gamma. This is a fourth tensor moment, distinct from the self-variance concentration proved in round 3.

For arbitrary coupled networks, mixed contractions are bounded by the geometric mean of their self-contractions. Averaging uses only prior marginals. The resulting Stein discrepancy is bounded by

```
epsilon² = 6*delta + 2*(2*sqrt(delta) + (4/sqrt(6))*(delta*beta)^0.25)^2,
beta = E[||b||^4] (the exact round-3 expression).
```

Its rate is O(d^-1/2) after taking the square root. Next: write all steps and independently verify the contraction moment and the polynomial Stein identity.

## Proof draft and verifier

Wrote PROOF.md with the exact self-contraction, the deterministic mixed-contraction inequalities, the Stein matrix, and the cavity-posterior marginal argument. A Gaussian interpolation gives smooth replacement with covariance K; a second Gaussian interpolation replaces K by C at additional cost O(d^-1). The proof states the remaining gap to the likelihood-weighted log partition explicitly.

Wrote check_stein.py. It integrates the self-contraction as a polynomial in independent Gaussian weight coordinates, without using the proof's row-partition enumeration. It separately builds deterministic mixed-network Stein polynomials by differentiation, and checks the Wick expansion by coordinate Hermite polynomials and mixed polynomial tests. It includes identical, opposite, permuted and zero-row networks, and width ratios 1/2, 1 and 2.

Command:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_stein.py > check_stein.out 2>&1
```

First run exited 1 immediately; inspecting the output before any further changes.

Failure was macOS rejecting setrlimit(RLIMIT_DATA,512 MB) with `ValueError: current limit exceeds maximum limit`, despite getrlimit reporting an unlimited existing limit. Removed that unsupported guard. The calculation has fixed tiny dimensions, integrates products before expanding them to limit storage, retains the 120-second CPU cap, and reports peak RSS. No mathematical test had run before this failure.

Successful run: 0.049 seconds, peak RSS 16,121,856 bytes, actual priority 20. Six exact coordinate-moment checks and seven deterministic mixed Stein/Wick checks pass. For example delta(2,2)=3051/8 and delta(3,2)=23765/243. At gamma=1 and d=262144, d*delta=2.000167853 and d²*beta=9.000412006. The bound's sqrt(d)*epsilon is 5.452381582, tending slowly to sqrt(28)=5.291502622; the subleading norm-correction term decays only as d^-1/4 after rescaling.

Audit extension within the same lemma: added exact checks of both deterministic contraction inequalities, and direct polynomial integration of the averaged Stein residual over both W and X for four small dimensions. This checks the actual normalization independently of the tensor-product proof. Re-running the same command next.

Final verifier run: exit 0, 0.052 seconds, peak RSS 15,204,352 bytes, priority 20, OMP_NUM_THREADS=1. All checks pass. Direct averaged Stein variances are 365610 for (d,k)=(1,1), 193602 for (1,2), 23712 for (2,1), and 49931/4 for (2,2), all below the explicit bound. The deterministic tests verify the asymmetric mixed Stein matrix rather than assuming it is symmetric. The zero-row and opposite-network tests cover singular Gaussian covariances. No mathematical test failed.

## Final audit and report

Re-derived every coefficient in the Stein matrix from the Gaussian generator: the cubic contributes gradient H/sqrt(6) after the inverse generator, while the full gradient is 3H/sqrt(6)+b. Hence Gamma has coefficients 1/2, 1/sqrt(6), sqrt(3/2), 1. The quadratic product identity gives fourth-chaos coefficient 1/2 and second-chaos coefficient 2, yielding 4!/4=6 and 2!*2²=8; their sum explains the leading 14. Direct coordinate Hermite expansion verifies these normalizations independently.

Checked the three row-index equality patterns in the contraction expectation against the direct Gaussian-coordinate integrals, including d=1 and k=1. The mixed-contraction inequalities use only marginal prior moments, so no unproved joint replica independence enters. The norm correction is retained through beta and ell; removing it prematurely would give the wrong finite-dimensional covariance.

Checked the posterior scope: fresh-input independence holds after deleting the observation, not under the full posterior; no transfer of the lemma to a likelihood ratio or log Z is asserted. The sample normalization is an L1 triangle inequality, with no independence assumption across samples. The constant sqrt(14*(1+1/gamma)) describes the explicit upper bound, not an optimal convergence constant or prediction error.

Wrote REPORT.md with the required verdict. The only operational failure was the unsupported resource-limit guard; the inherited nice priority is already sufficiently low. No edits outside this folder, external writes, git, or subagents. The old folders were read only and bytecode creation was disabled for their verifier.
