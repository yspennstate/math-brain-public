VERDICT: PROVED efficient additive-error ℓ2-robust learning for two spherical Gaussians with bounded parameters

For balanced classes with conditional laws N(mu_y,sigma_y^2 I_d), d>=2,
unknown means and unequal unknown scales, assume 1<=sigma_y<=S and
||mu_1-mu_0||<=M. For epsilon>0, a learner achieves robust risk at most the
optimal Borel-classifier risk plus eta, with probability at least 1-alpha.
It uses O((d+1)/(alpha eta^2)) real labelled samples per class and polynomial
arithmetic time in d,S,M,1/epsilon,1/eta,1/alpha. Additional samples used for
the optimization are generated internally from a fitted Gaussian model.

This settles a special case of T345 at additive accuracy, not the whole
problem. For polynomially bounded parameters and inverse-polynomial target
error, spherical Gaussian pairs do not exhibit the proposed superpolynomial
learning-time obstruction in the stated real-arithmetic model.

The central reduction is exact, without parameter bounds: axial coordinate
and distance to the line of means reduce the optimal robust risk in R^d to
the optimal robust risk on a Euclidean half-plane. The conditional quotient
law is N(a_y,sigma_y^2) times sigma_y chi_{d-1}. Meridian sections give the
lower bound against every Borel classifier, and an exact ball-image identity
gives the reverse bound. A finite weighted bipartite graph then approximates
the quotient optimum. Gaussian dilation controls its radius slack. Fitting
the unknown model in total variation transfers the guarantee to real data
without a mean-separation assumption.

The complete argument is in [PROOF.md](PROOF.md). The independent derivations,
edge cases, and negative controls are in [AUDIT.md](AUDIT.md).

Reproduction command, from this directory:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check.py
```

The final run passed 320 geometric checks, exhaustive comparison of 4,096
classifiers on each of five finite symmetry problems, and exhaustive comparison
of 1,024 subsets on each of 80 weighted graph problems. Four chi-density
integrations, three independent KL integrations, and a continuous Gaussian
interval-classifier calculation passed. Deliberately removing angular
independence, changing to l_infinity geometry, or omitting a factor two exposes
failures, as recorded in the checks. The continuous classifier's exact robust
risk was 0.0417737614 against its claimed upper bound 0.0885598445.

Data: [checks.json](checks.json). Exact commands and outputs:
[LOG.md](LOG.md). Final measured runtime was 0.072 seconds and peak RSS
15,810,560 bytes. The nice launcher emitted a sandbox warning, but the process
inherited nice 20, lower priority than requested. macOS refused an address-space
limit; the soft CPU limit was installed and measured memory stayed below 1 GB.

The literature search stayed below ten minutes. No opened paper settles all
of T345, and no verified post-status-date solution was found. Shared-covariance
Gaussian results already exist, including Chen Dan, Yuting Wei, and Pradeep
Ravikumar, [arXiv:2006.16384](https://arxiv.org/abs/2006.16384).
[LITERATURE.md](LITERATURE.md) records all opened papers and the scope of each.
The short search does not establish novelty of the assembled theorem here.

What failed or remains uncertain: directly transferring the Euclidean quotient
to l_infinity fails. The grid initially introduces a larger comparison radius;
this is resolved by the explicit dilation bound, not ignored. The theorem
does not cover general covariance pairs, optimal minimax rates, or uniform
polynomial bit complexity for exponentially ill-scaled inputs. It proves a
polynomial arithmetic-time construction, which can have an impractically
large grid. The full high-dimensional learner was not implemented; its finite
components and proof constants were audited.

Next worker: first check whether this precise unequal-spherical-variance
approximation theorem is already stated in the transport literature. For
mathematical extension, test common block-spherical covariances with a fixed
number of rotational blocks: a quotient retaining one radius per block may
preserve the fixed-dimensional optimization. General covariance pairs require
a different argument because the common independent angular law disappears.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:30 Asia/Tbilisi (T345).
