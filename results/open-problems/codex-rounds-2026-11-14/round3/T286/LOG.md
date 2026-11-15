# T286 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Started 2026-11-15 03:44 Asia/Tbilisi.

## Orientation and bounded literature check

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md under ~/codex_op_1114/briefs/T286. Directory listing confirms there is no PROOF.md or computation script there. Read startup MEMORY.md, the mesh protocol, the priority-related memory and compute_state.json. Compute status is warn / owner_away_open with saturated CPU; no large computation will be used. The explicit folder-only rule overrides external brain, checklist and mesh writes, so none of those stores is mutated. No git or subagents.

Commands: pwd; rg --files; cat earlier Markdown files; ls -la earlier folder; cat compute state; date; read startup memory. A tiny read through nice -n 15 printed 'setpriority: Operation not permitted'; later numerical scripts will report actual priority and enforce one thread and small memory.

Web search queries: '"2510.24616" generalization rigorous conjecture'; '"Bayes-optimal" "extensive-width" 2026 general activation proof'; '"extensive-width" "rigorous" "activation" 2026 Bayes'; '"2510.24616" proof interpolation concentration'. Opened https://arxiv.org/html/2510.24616v5, https://arxiv.org/abs/2510.24616, https://arxiv.org/abs/2503.14121 and https://arxiv.org/html/2503.14121v2. No new rigorous general-activation solution found. Search completed within five minutes; this is a bounded negative search, not a proof of absence.

## Rechecking the earlier finding

Independently read Remark 4 in 2510.24616v5: it expressly conjectures exactness for one hidden layer with vanishing second Hermite coefficient and identifies unresolved assumptions. Appendix B.6 calls its argument a potential route and restricts to mu_0=mu_1=mu_2=0 and all-ones readouts. Thus the earlier main claim (no completed proof supplied there) holds. No numerical or original theorem claim exists in the earlier report to reconstruct. The restricted quadratic theorem is a separate result and does not resolve this gap.

Next: inspect the exact interpolation expression before selecting a lemma. The choice will be recorded here before proving it.

## Choice (03:49 local)

Opened Appendix B.6, equations (159)–(170), especially the self-covariance condition (165) and the distinct replica condition (166). Choose ONE piece: prove the self-covariance concentration condition for the normalized cubic Hermite activation phi(z)=(z^3-3z)/sqrt(6), Gaussian weights and Gaussian inputs, with width proportional to dimension. Prove an explicit finite-dimensional second-moment bound, uniform in the interpolation parameter. Also compute the true conditional covariance, since Gaussian weight row norms are not exactly one and the displayed Hermite kernel omits their correction. This is a concrete missing lemma in the suggested appendix; it does not require proving the Gaussian equivalence or replica concentration assumptions.

The web status search is now closed. A shell curl fetch failed with 'Could not resolve host: arxiv.org'; no downloaded paper was obtained. Relevant equations were read using the web tool instead. The proof and a small exact-arithmetic check will follow; all source-dependent claims will cite the opened paper.

## Proof and independent exact check

Wrote PROOF.md and check_cubic.py. The proposition proves self-kernel and true conditional-variance concentration at rate O(d^-2) in squared L2 when k/d tends to a positive constant. The conditional-variance correction is the nonnegative Gram form B=(3/(2k))||sum_i (||w_i||^2/d-1)w_i/sqrt(d)||^2. Its mean is 3/d+12/d^2. Thus E[V]=1+9/d+20/d^2, rather than the unit-norm prediction 1 at finite d.

Independent check command:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_cubic.py > check_cubic.out 2>&1
```

Exit 0, elapsed less than one second. The sandbox prints 'nice: setpriority: Operation not permitted', but the script reports actual priority 20, which is already lower priority than the requested 15. OMP_NUM_THREADS=1; standard library only; peak RSS 15,302,656 bytes; CPU limit 90 seconds. No workload parallelism.

The independent derivation expands the network polynomial directly in W and X, squares it, integrates X by Gaussian moments, and checks polynomial equality to C+B. It then integrates the resulting polynomials over W by coordinatewise Gaussian moments. This avoids assuming the bivariate pairing formula or radial moment variance calculation in the proof. Cases (d,k)=(1,1),(1,3),(2,1),(2,2),(3,2) all pass exactly over rational numbers, including all constants in E[C], E[(C-1)^2], E[B], E[B^2] and E[V].

Output excerpts:

```
exact Wick check d=1 k=1: PASS; E[V]=30; E[(V-1)^2]=52339
exact Wick check d=2 k=2: PASS; E[V]=21/2; E[(V-1)^2]=6391/4
exact Wick check d=3 k=2: PASS; E[V]=56/9; E[(V-1)^2]=9556/27
rate checks k=d; columns: d, d^2*A, d^2*D, d^2*upper bound
16 88.491455078 22.504394531 200.247104339
256 55.646715764 9.442034282 110.932755015
16384 54.025275701 9.006596626 107.149164441
limits: 54 9 107.090815370
ALL CHECKS PASSED
```

Audit caught incorrect higher-order coefficients in the draft expansions of M6-M3^2 and h. Corrected them using exact symbolic product expansion; all five direct polynomial checks also verify the corrected identities independently. Leading rates were unaffected. Complete output is saved in check_cubic.out.

## Sharpening and attempts to break the lemma

The same exact moments give Var(B)=O(d^-3). Separating variance from bias sharpens the true conditional-variance result to the equality

    d^2 E[(V-1)^2] -> 81+18/gamma,

where k/d -> gamma>0. The displayed Hermite kernel instead has limit 36+18/gamma. These are concentration errors of a random conditional variance, NOT Bayes prediction errors. The difference is caused by the finite-dimensional norm correction and is of the same order as the self-kernel bias.

Re-ran the same command after extending the verifier with an exact formula for Cov(C,B). Its diagonal contribution is (3/(2k))(M6-2M5+M4-M3*b); its identical-edge contribution is 9(k-1)/(k*d*(d+2))*(M3-M2)^2, obtained from the fourth moment of the inner product of independent uniform directions. Direct polynomial integration checks this formula against all five small cases. The k=d rate check now has an additional true-MSE column: at d=16384 it is 99.058984724, tending to the proved constant 99. Added ratio checks gamma=1/2 and 2 to catch a reversed width normalization. Script reruns still finish in less than a second, at actual priority 20 and under 20 MB RSS.

Boundary checks: d=1, k=1 and k>1, and d>1, k=1 all satisfy the exact formulas; only the asymptotic rate assumes k/d bounded away from zero and infinity. Row-norm fluctuations were explicitly retained. No assumption of independent off-diagonal inner products is used: only pairwise vanishing covariance, proved by parity. Uniformity in interpolation concerns the averaged prior marginal, not a supremum of random posterior quantities.

Reopened the already-read quadratic paper using web find on Theorem 2.10 and Section 2.5: its explicit width exclusion and unique-maximizer qualification agree with the earlier report. This was source verification, not a new literature-search round. Reference: Yizhou Xu, Antoine Maillard, Lenka Zdeborová, Florent Krzakala, Fundamental Limits of Matrix Sensing: Exact Asymptotics, Universality, and Applications, https://arxiv.org/html/2503.14121v2.

What remains: this does not bound a likelihood-weighted log-partition remainder merely from the L2 estimate. Gaussian replacement (159), distinct teacher–replica covariance concentration (166), and the required remainder estimates still need proofs. No gradient-descent conclusion follows. No claim that the elementary lemma is new to the literature; it is new work beyond the earlier session and fills one stated deferred condition in a precise special case.

## Final audit

Wrote REPORT.md with the required first-line verdict. Read back PROOF.md and fixed its opening inline-math delimiters. Final exact-check output reports ALL CHECKS PASSED and 15,663,104 bytes peak RSS. At d=16384 the true-MSE rescalings for gamma=1/2,1,2 are respectively 117.093063334, 99.058984724, 90.041945419, converging toward 117,99,90 as predicted. Checked the report's first line with head and artifact line counts with wc (REPORT 26, PROOF 174, verifier 164 lines). No edits outside this folder, external writes, git, or subagents. The earlier folder was read only.
