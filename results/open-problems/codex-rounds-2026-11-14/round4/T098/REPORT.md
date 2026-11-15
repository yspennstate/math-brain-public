VERDICT: PARTIAL dimension-independent first rotation at good barriers in Bernoulli-diluted Ising chains

The earlier first-flip resonance estimate holds under independent analytic
and computational checks. The new result constructs the local rotation
requested by the round-3 report, bounds its exact remainder, and identifies
the new order-two denominators. The full T098 problem remains open here.

For a frozen site f, suppose every first-flip denominator, over all adjacent
block eigenstates and outer frozen assignments, has magnitude at least delta.
After adding V_f=epsilon_f X_f, there is an anti-Hermitian local generator
with

\[
 [H_0,A_f]=V_f,\qquad
 \|A_f\|\le a_f:=\sqrt{8/3}\,|\epsilon_f|/\delta.
\]

The constant does not depend on the adjacent blocks' dimensions or on chain
length. Interlaced spectra and degeneracies within either sector are allowed.
The proof uses an integrable Fourier multiplier equal to 1/x outside the
excluded gap. The rotation acts on the two adjacent active blocks, f, and
their outer frozen controls. The earlier bounds give failure probability at
most F_p(4rho delta) and support-radius tail at most 2p^r-p^(2r), conditional
on f being frozen. The estimate covers all local states simultaneously.

For one perturbed barrier the exact rotated Hamiltonian is

\[
 e^{A_f}(H_0+V_f)e^{-A_f}=H_0+\tfrac12[A_f,V_f]+T_f,
 \qquad \|T_f\|\le\tfrac43 a_f^2|\epsilon_f|.
\]

The total correction has norm at most a_f|epsilon_f|. Since the quadratic
term preserves Z_f, the dressed involution satisfies

\[
 \|[H_0+V_f,e^{-A_f}Z_fe^{A_f}]\|
       \le\tfrac83 a_f^2|\epsilon_f|.
\]

The factors 4/3 and 8/3 were independently re-derived from an exact one-spin
rotation; their limiting ratios are attained when the bounds are expressed
in terms of the actual norm ||A_f||. No optimality is claimed for sqrt(8/3).
Every step is in [PROOF.md](PROOF.md).

For several perturbed barriers, the proof gives the finite-volume Taylor
coefficient, including the terms involving bad barriers. A good-good pair
term vanishes unless the two sites are consecutive in the ordered frozen-site
list, and its norm is at most 2 sqrt(8/3)|epsilon_f epsilon_g|/delta for a
common threshold. A twice-at-the-same-barrier term can mix active-block
labels: an explicit three-site example has off-diagonal norm
6.490601756172087e-5. Its endpoint energy gap contains no h_f, so the earlier
averaging argument at f does not control it. Two-distinct-barrier bare
endpoint gaps remain affine in their two fields. Renormalized energy gaps
already need not be affine; even one spin produces 2h+epsilon^2/h at order
two. These distinctions are explicit in the proof.

Reproduce the checks from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_rotation.py > rotation_stdout.txt 2> rotation_stderr.txt
```

The accepted run passed 84 exact rational capped-sum comparisons, 63 exact
finite-volume probability checks, 129 physical barrier cases, 313 local
control sectors, 111 barrier-pair checks, 15 generic interlacing/degeneracy
cases, and the spectator, Taylor, and trigonometric checks. The largest
local inverse-equation residual was 8.49e-13. Direct Sylvester solves audit
the spectral inverse independently; direct unitary conjugations audit the
remainders, and an independent spectral path sum audits the order-two formula.
These matrix checks use floating-point arithmetic, not certified intervals.

Final run: 39,141,376 bytes peak RSS and .421 seconds, with all numerical
thread limits one. Inherited nice value was 20, verified through libc.
stderr contains only macOS's denial of the redundant nice adjustment.
No numerical check failed. Data: [rotation_verification.json](rotation_verification.json),
[stdout](rotation_stdout.txt), [stderr](rotation_stderr.txt), and
[LOG.md](LOG.md). No files in either previous folder were modified.

The bounded literature search found no newer unconditional solution.
John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains*,
[arXiv:1403.7837](https://arxiv.org/abs/1403.7837), retains the level-attraction
assumption. Francois Huveneers, *Many-body localization: an introduction for
mathematicians*, [arXiv:2609.39462, Section 4.5](https://arxiv.org/html/2609.39462v1#S4.SS5),
discusses the remaining high-probability problem. Both sources were opened.
An unindexed result could have been missed. No literature novelty is claimed
for the elementary rotation lemma.

What is missing is a volume-uniform remainder estimate for the simultaneous
rotation, followed by control of the new active-label and renormalized gaps.
The single-barrier cubic commutator bound does not apply unchanged when
other barriers are also perturbed. The global Taylor identity in the proof
does not claim a volume-independent bound for the norm of sum_f A_f.

The next worker should truncate to good cells of diameter at most ell,
leave the other cells unrotated, and bound the simultaneous rotation's
higher-order terms in a per-site interaction norm, uniformly in volume.
That is the next checkable extension of the present local norm estimate.
The same-barrier active-label gap problem must still be addressed before
claiming convergence of a second rotation.

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, approximately 04:50 Asia/Tbilisi.
