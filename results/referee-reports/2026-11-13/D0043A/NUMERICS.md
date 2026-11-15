# Numerical evidence and checks

The proof is independent of these computations. Random seeds and numerical settings are in the code; individual eigenvalues and diagnostics are in data/. All calculations ran at inherited nice10 with one numerical thread, below4GB. The largest recorded RSS among the experiment processes was204MB; the spectral/HMC runs used at most142MB. No dense n×n matrix was used for n=10000 or100000. Tridiagonal bisection computes the first three eigenvalues in linear storage; a sparse shift-invert calculation independently checked an artificial sample.

## Independent critical profile and operator discretization

The artificial matrices in SCALING.md use standardized centered χ₁ diagonal noise and exact integrated variance in each cell. There are96 independent samples at each β,n. The operator discretization uses Gaussian increments with that same exact cell variance, not a singular point evaluation at t=0. Meshes h=.025 and.0125 span length128. Entries below are sample means of −λ₀, followed by sample standard deviations in parentheses. These are Monte Carlo summaries, not exact limiting means.

| β | χ profile n=10000 | χ profile n=100000 | Gaussian h=.025 | Gaussian h=.0125 |
|---|---:|---:|---:|---:|
| 1 | -0.6915 (0.6420) | -0.4965 (0.7312) | -0.5651 (0.7902) | -0.5148 (0.8400) |
| 2 | -1.1701 (0.3919) | -1.0988 (0.4735) | -0.9884 (0.5454) | -1.0869 (0.5377) |
| 4 | -1.2763 (0.3196) | -1.3215 (0.3518) | -1.3124 (0.3418) | -1.3197 (0.3670) |

A separate96-sample coupled-Brownian refinement check aggregates pairs of fine increments to build the coarse mesh. The root-mean-square changes in the ground eigenvalue from h=.025 to.0125 were β=1: 0.01342, β=2: 0.01649, β=4: 0.00443. Restricting the same paths from length128 to64 changed the first three eigenvalues by at most 4.9e-12. This last number is an observed finite-sample boundary check at numerical precision, not a uniform probabilistic bound. The deterministic mesh/boundary check is also saved.

## Genuine critical quartic

The target is exactly the KRV entry density with V=U/2, U=x⁴/20−4x³/15+x²/5+8x/5. In q_i=log b_i coordinates its negative log density is nβ trU(T)/2−βΣ(n−i)q_i; the Jacobian is included. Metropolis-corrected HMC updates all2n−1 entry variables. A fixed pentadiagonal Hessian mass at the finite-n mode accounts for the coefficient correlations. Cholesky factors and triangular solves use linear storage. The mass matrix is fixed throughout a chain; its use does not approximate the target. At each n=256,1000,10000 and β=1,2,4, two chains used300 warm-up trajectories, then400 retained draws per chain, thinning2. Step-size adaptation ends before retained sampling. Last sampled a,b vectors are saved in NPZ files.

An earlier diagonal-preconditioned run failed mixing diagnostics (split R-hat as high as2.60 and ESS below20); its raw data and diagnostics are retained but excluded from the summaries below. The banded run had split R-hat0.9995–1.0323 and within-chain autocorrelation ESS118–601 per800 draws. These basic diagnostics support exploratory comparisons but are not proof of stationarity, independence or rare-tail accuracy. There were no recorded divergent trajectories, and no Hessian diagonal shift was needed.

| n | β | mean c n^(2/7)(λmax−2) | sample SD | split R-hat | estimated ESS |
|---:|---:|---:|---:|---:|---:|
| 256 | 1 | -1.5632 | 2.4196 | 1.0322 | 144.8 |
| 256 | 2 | -4.0600 | 1.4343 | 1.0117 | 118.2 |
| 256 | 4 | -4.8499 | 0.6253 | 1.0015 | 601.3 |
| 1000 | 1 | -1.5554 | 2.6018 | 1.0080 | 175.9 |
| 1000 | 2 | -4.0241 | 1.3778 | 1.0158 | 137.3 |
| 1000 | 4 | -4.8024 | 0.5925 | 0.9995 | 598.9 |
| 10000 | 1 | -1.4670 | 2.6488 | 1.0111 | 163.1 |
| 10000 | 2 | -3.9641 | 1.4459 | 1.0052 | 161.0 |
| 10000 | 4 | -4.8749 | 0.6236 | 1.0024 | 579.0 |

Here c=6^(2/7) is the Claeys–Vanlessen kernel normalization. To compare with the displayed operator using the *formal deterministic drift* calculation, multiply these scaled eigenvalues by γ/c, where γ=2^(−6/7). This constant is derived algebraically in SCALING.md and is not fitted. For n=10000:

| β | quartic formal-scale mean | approximate MC SE | Gaussian operator mean | independent-sample SE |
|---|---:|---:|---:|---:|
| 1 | -0.4854 | 0.0686 | -0.5148 | 0.0857 |
| 2 | -1.3116 | 0.0377 | -1.0869 | 0.0549 |
| 4 | -1.6129 | 0.0086 | -1.3197 | 0.0375 |

The mismatch of sample means under this formal normalization is evidence only. It cannot exclude another constant normalization; the rigorous tail argument excludes every fixed positive normalization.

## Independent β=2 finite-n check and limiting-law computation

For n=256, a separate quadrature projection-kernel computation approximated the largest-eigenvalue CDF of the genuine unitary quartic ensemble. It used fully reorthogonalized weighted polynomials on [−3.5,6], with4096 and8192 Gauss–Legendre nodes. The maximum CDF change on45 comparison points was 0.00612; the orthogonality residual was below 3.1e-15. The800 HMC draws differed from the finer-grid CDF by at most 0.03616 on this grid. This is a quadrature consistency and sampler check, not an independent-sample goodness-of-fit test. Domain truncation and quadrature error are not certified.

An initial quadrature attempt formed exp(−n(U−minU)) before taking its square root; this underflowed near the edge and was rejected. The corrected code exponentiates half the exponent before normalizing. The final projection is checked for finiteness and orthogonality. This matters even at n=256.

The limiting higher-order TW₂ Fredholm determinant itself was not evaluated. Claeys–Olver1111.3527 describes numerical RH/Fredholm evaluation, but a verified implementation was not available in this workspace. The finite-n determinantal CDF above is explicitly distinguished from that limiting law. The rigorous comparison uses the published critical-kernel right-tail estimate, not an ordinary TW₂ approximation.

## Algebra, solver and tail checks

- Direct trace-vs-dense-eigenvalue action error: 1.78e-15.
- Exact quartic gradient vs centered finite differences: maximum error 6e-10.
- The banded analytic Hessian vs independently differenced gradients: maximum error 1.82e-09.
- Tridiagonal eigenvalue solver vs sparse shift-invert, n=10000: maximum error 1.89e-14.
- SymPy rederived the edge powers, the local quartic equations, x=D³/8+O(D⁴), c=2, and γ=2^(−6/7). Direct integration of the equilibrium density gives total mass0.9999999999916908; its Stieltjes transform independently has leading term1/z.
- Exact Gaussian log probabilities of the trial-function events are tabulated for k=0,1,2, β=1,2,4 and s=1,…,4096 in rayleigh_tail.csv. These are probabilities of a variational *sufficient event*, hence rigorous-formula lower bounds on an operator tail, not sampled eigenvalue-tail probabilities or estimates of its exact exponent.

Original plots: `data/eigenvalue_comparison.png`, `data/unitary_cdf_check.png`, and `data/trial_tail_powers.png`. No paper images or scans are present.

The final integrity audit (`code/audit.py`, results in `data/audit.json`) checks source-text hashes, PDF absence, report control characters, all saved row counts and sampled-matrix dimensions, numerical summary consistency, and the Gaussian trial-event power calculations. Mathematical proof steps were audited separately and matched to Baslingker's theorem.

## Reproduction

From this directory, with nice≥10 and one numerical thread:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_algebra.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/verify_models.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py artificial --draws 96
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py quartic --ns 256 1000 10000 --banded --burn 300 --draws 400 --thin 2
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/coupled_mesh.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/finite_unitary.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py tail
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/build_report.py
```

If the shell is not already at nice10, prefix the Python command with `nice -n 10`; the scripts check inherited priority. Sources can be regenerated with code/acquire.py and the URLs in sources/manifest.json. Versions and resource metadata are saved in data/environment.json.
