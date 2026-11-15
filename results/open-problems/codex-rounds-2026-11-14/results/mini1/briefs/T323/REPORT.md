VERDICT: PROVED bistability for an explicit general-matrix family and its exact two-token basin threshold

For normalized self-attention on S^1, including self-interaction, take
Q=I, K=kappa J, V=aI-omega J, where J is the counterclockwise quarter-turn
and a, omega, kappa are positive. If beta*kappa*omega>a, every even n
admits both an open basin of rotating consensus and an open basin of
stationary balanced antipodal pairs. All directions that split individual
tokens within a cluster are included in the stability proof.

The antipodal transverse eigenvalues are a-beta*kappa*omega and
-beta*kappa*omega, the latter with multiplicity n-2. Rotating consensus
has transverse eigenvalue -a. A direct nonlinear estimate proves open
basins and convergence of the limiting phase. PROOF.md contains every step.

For n=2 the basin boundary is the unique delta in (0,pi) satisfying

    tan(delta/2) tanh((beta*kappa/2) sin(delta)) = a/omega.

It exists precisely when beta*kappa*omega>a. Below that parameter threshold,
including equality, every nonantipodal pair synchronizes onto a rotating
trajectory. Above it, larger separations converge to stationary antipodes.
For a=omega=kappa=1 and beta=2, the boundary is approximately
1.863372534735285 radians and the antipodal basin has probability
0.406870100550410 under independent uniform initialization.

Keeping the identical V but taking Q=K=I makes every nonantipodal two-token
configuration synchronize. Thus the spectrum of V alone cannot decide
between these outcomes for unrestricted Q,K. The example even has symmetric
part (V+V^T)/2=aI>0 and spectrum a +/- i*omega.

The identity-matrix part of the original problem is already solved:
Yury Polyanskiy, Philippe Rigollet and Andrew Yao,
*Synchronization of mean-field models on the circle*,
[arXiv:2507.22857](https://arxiv.org/abs/2507.22857), Corollary 2.5,
covers the normalized circle equation for all positive beta. Together with
the higher-dimensional theorem recorded in SOLVED_ELSEWHERE.md this covers
all d>=2. The literature check took about three minutes. The general-matrix
classification remains unresolved here.

Reproduce the independent audit with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
```

All checks passed: 1,000 random parameter/angle comparisons, 32 full
Jacobian comparisons, five monotonicity scans, two independent separatrix
root calculations, and five Cartesian-system trajectories repeated at half
step. Maximum Jacobian discrepancy was 2.847e-10. Data: audit_data.json;
complete output: audit_output.txt; independent analytic checks: AUDIT.md.
The final run used effective niceness 20, 15.5 MB peak RSS and 0.588 seconds.
The nice utility warns that its priority change was denied; the script
checks that the inherited niceness is already >=15 before computing.

What failed or remains uncertain: unequal antipodal populations are not
stationary in this model, so no odd-n result is claimed. No global basin
classification is proved for n>=4. No result for symmetric positive definite
V or symmetric positive query-key products is claimed. The literature search
was bounded and does not establish novelty. Numerical decimals are checks,
not certified intervals; none is needed for the proof.

Next: derive and classify the relative equilibria for unequal populations
in the same skew-key family, then check their stability against splitting
within each group. This would test whether the stationary antipodal
attractor continues to an attracting rotating two-cluster state for odd n.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
21:30 +04 session start.
