VERDICT: PROVED global population-gradient-flow convergence for two untied scalar attention step sizes with all other blocks fixed

The new result is an exact d=1, two-layer case of the earlier report's
suggested untying problem. For every integer N>=1 and every unequal
initial pair a(0),b(0), population gradient flow converges to the global
minimum. Thus independent continuous random step-size initialization
succeeds almost surely. The learned step sizes, in either order, are

    a_± = N/(N+2) [1 ± sqrt(2/(N+4))].

The resulting predictor implements two empirical least-squares gradient
steps from zero. Its exact squared prediction risk is

    8/[(N+2)(N+4)],

which approaches the noiseless scalar Bayes risk zero at rate 8/N^2.
At equal initialization, the trajectory instead converges to a strict
saddle. PROOF.md gives the full argument, including global existence,
stationary-point classification and exclusion of the saddle for every
unequal initial pair.

This advances the earlier folder, which contained a literature audit and
no proof or numerical scripts. Its comparison-ODE correction was
independently rederived and holds, conditional on the cited gradient
inequality. The scalar loss was then rederived directly from the source's
token update. No sharp matrix rate from that paper is imported.

The brief web check found no full solution superseding that report.
Opened sources and queries are recorded in LOG.md. The relevant
architecture is from Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi,
Stefanie Jegelka, Sanjiv Kumar, *Can Looped Transformers Learn to Implement
Multi-step Gradient Descent for In-context Learning?*,
[arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1), Section 3 and
Appendix A.1. No claim of exhaustive literature novelty is made.

Validation command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_scalar.py
```

The standard-library script independently expands Gaussian sum moments
and verifies exact risks for N=1,2,3,5,10,100,1000. Rational polynomial
checks verify the gradients, loss gap and parameter-difference equation;
direct rational token updates verify the forward pass. All checks passed.
Peak RSS was about 13 MiB. The nice wrapper reports a priority-setting
warning, but a direct query confirms inherited nice=20; the final script
asserts nice>=15. Its optional address-space cap was unavailable. These
short runs remained far below 1 GiB and used one thread, with no numerical
libraries, GPU, training run, git or writes outside this folder.

What remains open: full random initialization of all transformer blocks,
d>1, softmax attention, and discrete or stochastic training. The proof
uses direct trainable Q entries, not separately trainable key/query
factors. No uniform training-time bound in N is established. The full
T325 claim is not proved.

Next worker: keep d=1 and the fixed blocks, and extend the convergence
proof to L>=3 independently initialized scalar step sizes. In elementary
symmetric coordinates the risk is again a strictly convex quadratic,
but repeated step sizes make the coordinate map singular. The missing
piece is a classification and attraction analysis of stationary points
with repeated roots. Alternatively, d>1 requires controlling genuinely
noncommuting layer matrices; the two-dimensional scalar proof does not
settle that obstacle.

Task: “take the NEXT checkable step on this problem, building on that work.” — 15 November 2026, 03:47 Asia/Tbilisi.
