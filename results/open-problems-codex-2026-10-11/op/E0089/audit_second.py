from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('The same estimate works at graph-dependent critical q_G, since it is uniform for vacancy densities','The same estimate works at graph-dependent vacancy density 1-q_G, since it is uniform for vacancy densities')
s+=r'''

## 6. Numerical and finite checks, and a referee audit

All computations ran in seconds to minutes, with local arrays far below 1 GB. No empirical conclusion about final-success concentration is drawn.

- `second_finite_checks.py`: 12288 exact message/peeling equality checks (two 8-vertex 4-regular graphs, all 256 initial sets, r=2,3,4, eight rounds); 303 rational polynomial evaluations; 30 exact joint-survival calculations on adjacent or distance-two tree stars at d=3,4 and several rational densities. All passed. `second_finite_checks.json` records the counts.
- `CriticalRecursion.lean`: six kernel-checked algebraic/constant statements, no sorry and no native_decide; exit 0 in `second_lean_check.txt`. This does not formalize the CLTs.
- `second_experiments.py`: at q=8/9 the exact one-round tree mean is h_1=16384/19683 and tree variance per vertex sigma_1^2=147374080/387420489, approximately 0.38039826025. It sampled six simple 4-regular graphs at each n=64,256,1024 and 2048 independent seed configurations per graph. The sample variance/n ranges were [0.3402,0.4044], [0.3770,0.4029], [0.3493,0.3953]. These modest samples are consistent with the variance calculation, but are not claimed to verify asymptotic convergence.
- For the same 18 graphs, the TWO-round conditional mean was computed exactly, rather than estimated from seeds: enumerate all distinct initial vacancy bits used by each exceptional two-hop neighbourhood; use the tree value only when the forward branches have distinct vertices. Deviations from n h_2 were between -0.337111 and -0.114097. The tree h_2 is the exact fraction 4453232545890304/5559060566555523. This supports the O(1) common-graph mean-fluctuation mechanism, which is proved independently by (A2)-(A3).
- The critical recursion was checked through 100000 iterations with 40-digit Decimal arithmetic against BOTH explicit bounds in (B4). At t=100000, t z_t is approximately 0.749812, approaching the proved limit 3/4.
- `second_replica_example.py` and `check_joint_derivative.py`: exact enumeration checks universal one-round expected counts and (D2) for t=1 on both previous 8-vertex examples.

A useful finite warning for approach B: mix G=K_{4,4} and its 04,15 -> 01,45 switch H with equal probabilities, and take fixed occupied density p=1/4. Their final-success probabilities differ by

  [g_H(2)-g_G(2)]P(Bin(8,p)=2)=10p^2(1-p)^6=3645/32768.

Thus two independently seeded final-success indicators on this shared random graph have annealed covariance

  (3645/32768)^2/4=13286025/4294967296>0.

Yet the independently seeded one-round vacant counts have covariance exactly zero at the SAME vacancy density 3/4, by (A8) (their common mean is 8[4(3/4)^4-3(3/4)^5]=567/128). This demonstrates why neither seed independence conditional on G nor cancellation of local conditional means proves cancellation of final exploration fluctuations. It is a finite fixed-density example, not an asymptotic counterexample and not a graph-specific-median assertion.

Referee issues checked explicitly:

1. The target graph is SIMPLE and fixed-degree. Configuration cycle bounds are transferred only after invoking the verified positive simplicity theorem. No CLT from the configuration multigraph is silently transferred.
2. The process and message variables are distinguished. Their equality by rounds is proved in Section 3 and exhaustively checked on small graphs; the tree recursion uses independent forward branches only on the actual infinite tree.
3. Local dependence is conditional on the fixed graph and uses independent Bernoulli bits. It is NOT asserted for bits conditioned on the global count. Corollary C handles that conditioning by a joint limit, with its denominator bounded away from zero.
4. Graph mean error uses B_t, and variance error uses B_{3t}, not B_t. This larger radius is needed to contain both overlapping balls and is included in all cycle bounds.
5. All constants hidden in the moment argument are controlled when t grows: dependency degree D, per-variable magnitudes after normalization, and cycle-type counts are n^{o(1)} in the specified range. Odd and exceptional even moments vanish with explicit negative powers of n. No uniform theorem at t~n^(1/4) is claimed.
6. Positive variance has a direct degree-one lower bound. Gaussian normalization is not justified by numerical variance or an assumed nondegenerate limit.
7. Limits of paired counts use conditional independence PLUS a quenched distribution theorem. Vanishing covariance alone is not used to infer asymptotic independence.
8. In the graph-specific-median extension, the density is allowed to depend on G, but the moment bounds are uniform in that density; the statistic is centred at its OWN tree mean n h_t(1-p_G). The possible uncorrected random centre is not discarded.
9. Gaussian conditioning remains valid at a degenerate joint limit rho=1 because each marginal has a continuous distribution and the rectangle boundary has zero mass.
10. The fixed-K source observable is final success. The count-CDF replica theorem proves a different, explicitly specified observable; it is not called a solution to E0089.
11. The n^(1/4) result is about the critical TREE DRIFT approximation. It is not asserted as a theorem on finite-graph running time, nor a universal impossibility result.
12. No claim has been promoted from numerical evidence to proof. Lean only certifies the algebra listed in the artifact; all probabilistic claims have handwritten proofs and explicit assumptions.

Precise remaining gap after this second attempt: prove a quenched approximation/factorization for FINAL r-core emptiness in the n^-1/2 critical-density window, at a fixed upper-count cutoff K, such as ATTEMPT.md equation (6). The local conditional replica factorization in Corollary C applies up to (d-1)^t=o(log n), while even early completion at those depths differs from critical final occupation by probability tending to 1/2. A shared-pairing exploration theorem or another global reduction is still required. Approach B identifies the joint adaptive-exposure covariance that would have to be controlled, but no such cancellation is proved.

Final verdict of the second attempt: PARTIAL. Theorems A and B, Corollary C, and the exact critical-recursion bounds are additional proved special cases/reductions. E0089 itself remains unresolved here.
'''
p.write_text(s,encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s+=r'''

## 10. Second serious attempt (2026-10-12)

The new full proofs are recorded in SECOND_ATTEMPT.md. Two previously untried approaches were written down: local finite-round peeling with quenched dependency-graph limits, and a joint two-colour adaptive configuration exploration. The former was pursued and yielded:

- Theorem A: fixed-round quenched Gaussian fluctuations of vacancy counts and independent-replica factorization; graph variance of the conditional count mean is O(1).
- Theorem B: this extends to growing rounds t_n with (d-1)^t_n=o(log n), using uniformly controlled cycle moments, variance bounds, and dependency-connected moment counts.
- Corollary C: local-count CDFs still concentrate under the source's upper-initial-count conditioning, using a joint Gaussian limit with the initial count. It also covers the graph-specific median, with explicitly density-dependent centering.
- At d=4,k=2, exact critical recursion z_(t+1)=z_t-(4/3)z_t^2-(16/9)z_t^3, explicit reciprocal bounds, and t z_t->3/4. The polynomial identities and rational constants passed Lean's kernel check.
- A precise limitation: approximating the critical tree drift on the n^-1/2 scale requires depth Omega(n^(1/4)), beyond tree-ball arguments; early completion even at the allowed growing depths has L1 discrepancy tending to 1/2 from the final critical event.

The gap in Section 5 remains: concentration/factorization of FINAL occupation under the fixed-K conditioned initial law. No solution or counterexample to Question 1.4(a) has been proved. Final verdict remains PARTIAL.
'''
p.write_text(s,encoding='utf8')
p=Path('CLAIMS.jsonl');rows=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()];rows.extend([
 dict(problem_id='E0089',claim='Under a fixed upper-initial-count conditioning, local vacancy-count CDFs have vanishing graph variance and independent-replica factorization up to (d-1)^t_n=o(log n); the locally centred graph-specific-median version also holds.',status='proved_special_case',proof_location='SECOND_ATTEMPT.md, Corollary C and median extension',remaining_gap='The observable is a locally normalized vacancy-count CDF, not final occupation; the required final-success factorization remains unproved.',checks='Full joint dependency-graph moment proof, exact covariance/derivative identity, positive conditioning denominator, compactness including degenerate Gaussian limit; finite derivative check saved.'),
 dict(problem_id='E0089',claim='A finite mixture of two 8-vertex 4-regular graphs has zero independent-replica covariance for one-round vacant counts but positive independent-replica covariance for final-success indicators at fixed occupied density 1/4.',status='proved_special_case',proof_location='SECOND_ATTEMPT.md, Section 6; second_replica_example.json',remaining_gap='Finite fixed-density example, not an asymptotic counterexample or a graph-specific-median statement.',checks='Exact Fraction enumeration of all 256 seed masks; final covariance 13286025/4294967296.')])
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf8')
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8');s=s.replace(', later Combinatorics, Probability and Computing 18 (2009), 205-225.','.').replace(', Physical Review E 91, 052802 (2015).','.').replace(', ACM Transactions on Parallel Computing 3(1) (2016), article 7.','.');p.write_text(s,encoding='utf8')
print('Second attempt audit saved; claims:',len(rows))
