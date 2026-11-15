VERDICT: PROVED quantitative cubic Gaussian replacement for finitely many cavity replicas

The round-3 self-covariance constants hold. This session adds an explicit Gaussian integration-by-parts and smooth replacement bound for the normalized cubic Hermite activation, Gaussian weights and Gaussian inputs. The general Bayes-error formula and the gradient-descent question remain open.

The new lemma permits any joint coupling of finitely many networks as long as each marginal is the Gaussian weight prior and the tested input is independent of their joint law. In particular, it applies to a teacher and replicas drawn from the matched posterior after removing one observation. It does not assume the replicas are independent after averaging the data.

For T=k^-1/2 sum_i(w_i/sqrt(d))^tensor3, the exact prior contraction moment is

```
delta = E[||T contraction_2 T||_F^2]
      = M6/k + ((k-1)/k)*M3^2*(1/d + 3/(d*(d+2)) + 15/(d*(d+2)*(d+4))),
M_p = product_{j=0}^{p-1}(1+2*j/d).
```

A deterministic mixed-contraction inequality makes this useful for dependent replicas. The resulting averaged Stein discrepancy epsilon is O(d^-1/2), with the explicit bound in [PROOF.md](PROOF.md), equation (1). If k/d tends to gamma>0, sqrt(d)*epsilon tends to sqrt(14*(1+1/gamma)). This is the asymptotic constant of the proved upper bound; no optimality of that bound is claimed. Smooth replacement uses the true random covariance K, or the displayed Hermite covariance C with an additional O(d^-1) error for Gaussian row-norm fluctuations. The bounds cover singular covariance matrices.

For smooth tests with uniform derivative bounds, averaging the remainder over n samples costs no additional factor of n. Normalization by d^2 costs n/d^2, so the bound still vanishes when n/d^2 tends to alpha. These conclusions concern the cavity law at each omitted input.

Verification: [check_stein.py](check_stein.py) integrates the contraction moment directly over Gaussian weight coordinates, independently of the proof's row-parity enumeration. Six exact moment checks pass. Seven deterministic mixed-network checks verify the Wick expansion, integration by parts, and contraction inequalities, including identical, opposite, permuted and zero-row cases. Four further checks directly integrate the actual Stein residual over weights and inputs. All pass. The final run took 0.052 seconds, used 15,204,352 bytes peak RSS, and ran at inherited nice priority 20 with one thread. Complete output: [check_stein.out](check_stein.out).

Commands:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T286/check_cubic.py > recheck_cubic.out 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_stein.py > check_stein.out 2>&1
```

Failures and limits: macOS rejected a proposed 512 MB RLIMIT_DATA guard before any calculation; the unsupported guard was removed. The numerical workload is fixed and tiny, and retains a 120-second CPU cap. `nice -n 15` reports a denied relative adjustment because the inherited priority is already 20. No mathematical check failed. No proof of a likelihood-normalization estimate, full-posterior Gaussian replacement, distinct-replica concentration, Bayes error or optimizer optimality was obtained. No literature novelty is claimed for this use of Gaussian polynomial contractions.

The bounded literature check found no later rigorous general-activation solution. Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore and Rudy Skerk, [arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5), still retain Gaussian replacement and concentration assumptions in Appendix B.6. The new result addresses a finite-dimensional cavity version of their replacement assumption, not their complete sum rule. Search details and the independent rederivation of the previous constants are in [LOG.md](LOG.md).

Next worker: express the likelihood-weighted term (158) through the posterior with sample mu removed. For a specified smooth output channel, first identify a class of cavity functionals whose derivatives have uniformly summable bounds when represented by replicas. Prove control of the random one-sample likelihood normalization and of the log-partition derivative, then apply the present Stein identity. A finite-replica central limit theorem alone does not bound that functional. Treat the separate replica concentration and hidden-unit permutation issue in (166) afterward.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 06:30 Asia/Tbilisi.
