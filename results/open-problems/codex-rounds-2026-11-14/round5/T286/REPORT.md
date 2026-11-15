VERDICT: PROVED likelihood-weighted cubic integration by parts for uniformly positive finite-output channels

The previous cubic Stein bound holds. This session extends it from fixed finite-replica tests to the likelihood-weighted log-partition expression in equations (158)--(161) of Appendix B.6 of Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore and Rudy Skerk, [arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5#A2.SS6). The hidden activation remains (z^3-3z)/sqrt(6), with Gaussian weights and inputs and all-ones readouts. The general Bayes-error formula and gradient-descent question remain open.

The fixed output label set is finite, of size q, with C² probabilities p_y satisfying p_y>=c>0, |p_y'|<=L1 and |p_y''|<=L2, with constants independent of dimension. Put B=q[L2 log(1/c)+L1²/c]. Under any matched cavity posterior, including the Gaussian side observations in that appendix, the observation contribution (158) equals the expression (161), with its full cubic Hermite covariance kernel C, up to absolute averaged error

```
B*(epsilon+ell)/2 = O(d^-1/2),
ell = 3/d+12/d²,
sqrt(d)*epsilon -> sqrt(14*(1+1/gamma)),  k/d -> gamma>0.
```

The finite-dimensional epsilon is given in [PROOF.md](PROOF.md), equation (9). The estimate is uniform on the open interpolation interval: the singular coefficient cancels before bounding the error. Averaging n observation contributions costs no factor of n; normalization by d² costs n/d². The self-covariance term in (161) is separately O(d^-1).

What is new: deleting one observation writes log Z_full as log Z_cavity plus a bounded one-sample logarithm. Summing the label derivative cancels log Z_cavity exactly. An empirical normalization using R cavity replicas has a derivative bound whose sum is independent of R. The inherited Stein identity and an integrable-kernel law of large numbers then permit R to tend to infinity. This controls the random normalization and the full likelihood weighting without claiming the entire posterior field is Gaussian. An explicit channel is p_±(z)=(1±tanh(z)/2)/2; its error coefficient is 0.516792474190*(epsilon+ell). Here tanh belongs to the output channel, not the hidden activation.

Verification commands, run from this folder:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T286/check_stein.py > recheck_stein.out 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T286/check_cubic.py > recheck_cubic.out 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -u check_cavity.py > check_cavity.out 2>&1
```

All final checks pass. Independent scalar polynomial integration recovers the inherited variance 365610. Twenty-four finite-difference cases check the replica derivatives and their summable bounds. Direct normalized Gaussian quadrature checks the new identity, including its exact Stein residual, for mixed, opposite/duplicate and zero networks. The largest final identity error is 7.08e-14. These deterministic examples verify algebra, not a prior-averaged Bayes-error estimate. The new verifier took 21.675 seconds and 14,991,360 bytes peak RSS, with one thread and actual nice priority 20.

What failed: the first quadrature run stopped at its grid-convergence assertion. Increasing the final resolution from 480 to 960 intervals per axis passed the unchanged tolerance; the failed output is preserved in check_cavity_initial.out. The inherited priority is already 20, so nice prints a denied further relative adjustment. No mathematical counterexample was found. Details and all commands are in [LOG.md](LOG.md).

Limits and uncertainty: no distinct-replica concentration, adaptive-interpolation existence, variational Bayes formula or optimizer theorem is established. The constants diverge as c tends to zero; standard Gaussian regression and unmodified logistic channels are not covered. General hidden ReLU/tanh are not covered. No literature novelty is claimed. The five-minute literature search found no later rigorous general-activation solution; this is a bounded negative search.

Next worker: retain this cubic activation and uniformly positive channel, and isolate the remaining cross-kernel concentration needed for the interpolation remainder. Work with the permutation-invariant C(W⁰,W¹); justify any replacement by a trace overlap under the Gaussian side observation before invoking (166). An alternative subsequent step is to remove the output-probability floor using quantitative denominator and score moments, which are not supplied here.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 09:03 Asia/Tbilisi.
