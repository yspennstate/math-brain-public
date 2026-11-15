VERDICT: PARTIAL joint-limit logarithmic volume law for critical orthogonal tanh Jacobians without the La/n restriction

The earlier result holds. The new result identifies the signed finite-width drift of a genuine Jacobian spectral statistic. The full joint-limit singular-value distribution remains unresolved.

Use the round-5 biased orthogonal tanh network and simultaneous Gaussian critical initialization:

\[
h_l=\tanh(gO_lh_{l-1}+\sqrt b\,\xi_l),\quad
g^2=\mu_G(a)^{-1},\quad b=a-g^2A_G(a),\quad
\|h_0\|^2/n=A_G(a),
\]

where mu_G(a)=E sech^4(sqrt(a)G), A_G(a)=E tanh^2(sqrt(a)G), O_l are independent real Haar matrices, and xi_l are independent standard Gaussian vectors. If n,L tend to infinity and La^2 tends to zero, then

\[
\frac{\displaystyle\max_{k\leq L}
\left|\frac1n\log\det(J_kJ_k^\top)+\frac{4ak}{n+2}\right|}
{1+La/(n+2)}\xrightarrow{\mathbb P}0.
\]

In particular, if La/n tends to t<infinity,

\[
\frac1n\log\det(J_LJ_L^\top)\xrightarrow{\mathbb P}-4t,
\qquad \det(J_LJ_L^\top)^{1/n}\xrightarrow{\mathbb P}e^{-4t}.
\]

If La/n tends to infinity, the logarithmic statistic divided by La/n tends to -4, and the geometric mean tends to zero. A uniform time version at depth floor(t(n+2)/a) also holds when na tends to zero. [PROOF.md](PROOF.md) gives all steps and the finite probability bound (30).

The same law holds for the auxiliary scalar S_k from round 5. Moreover max_k |n^(-1)log det(J_k J_k^T)-log S_k| tends to zero in probability, without any condition on La/n. The proof covers the wider deterministic parameter class 0<=b<=14a^3, |log(g^2)-2a|<=15a^2, |q_1/a-1|<=14a^2.

What is new: round 5 bounded the absolute mismatch between scalar gain and forward-radius drift. Retaining its sign gives s(q)-d(q)=-4q/(n+2)+O(a^2). A new global log-cosh estimate then transfers the scalar law to the determinant of the ordinary input-output Jacobian, with expected one-step absolute error at most 150a^2 on active steps. No freeness or independent-gate replacement is used.

This does not show that La/n->0 is necessary for empirical isometry. One squared singular value exp(-4tn), with all others one, has logarithmic mean -4t while its empirical W2 distortion tends to zero. The theorem does show that S_L->1 cannot be carried unchanged into a regime with La/n->t>0.

Reproduction commands, all final runs exit 0:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B recheck_bias.py > recheck_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B verify_volume.py > verification_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 clang++ -std=c++17 -O2 forward_volume.cpp -o forward_volume
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 ./forward_volume > forward_results.json 2> forward_stderr.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B summarize_forward.py > forward_summary.txt
```

The earlier 42 gate bounds, 25 Haar/bias trace quadratures, 48 exact radial bounds, 36 drift quadratures and 100000 crossing checks reproduce without discrepancy. New verification includes 75-digit global log-cosh inequalities, 18 exact rational signed-coefficient checks, nine independent 65-digit sphere marginal quadratures with maximum extrapolation error 2.19e-14, and 24 whole-vector biased determinant comparisons. Direct scalar elimination of small full Jacobian products agrees with summed layer log determinants within 1.74e-13. The full-product checks use Gaussian critical parameters computed at 65 digits.

Longer forward-only simulations use exact-in-law spherical images and biases for the radius and determinant; they do not compute the rest of the spectrum. Their parameters are in the wider deterministic class, rather than exactly Gaussian critical. With a=1/(64n^2), La/n approximately .1, n=16,32,64, the mean logarithmic volumes are -.268188795,-.336817678,-.368997457, approaching -.4 with a visible finite-width transient. All 27 checkpoints pass. The scalar is bracketed with a rigorous Taylor error rather than treated as exact numerical quadrature. The n=16,32 diagnostics lie outside the n>=64 finite-bound assumptions. Data and outputs are in [results.json](results.json), [verification_output.txt](verification_output.txt), [forward_results.json](forward_results.json), and [forward_summary.txt](forward_summary.txt).

Resource measurements: the new Python checks used 157.7 MiB peak RSS and 2.47 seconds; C++ used 1.312 MiB and 8.861 seconds. All numerical runs used one thread and actual niceness 20. The nice warning reports an attempted priority adjustment from an already lower-priority process.

What failed: the first Python run stopped on a FloatingPointError in NumPy slogdet. Its output is preserved in [verification_first_failed.txt](verification_first_failed.txt). The cause is not established. Replacing that call with scalar partial-pivot elimination produced a clean final run with all floating-point exceptions still enabled. No mathematical counterexample to the new theorem was found.

What remains uncertain: no full density, spectral-edge theorem, operator isometry, or empirical W2 isometry under La^2->0 alone is proved. The determinant statistic is sensitive to very small singular values. The finite constants are coarse, and no claim of priority against the whole literature is made. The bounded literature check found no verified external resolution; opened references and scopes are in [LITERATURE.md](LITERATURE.md).

Next worker: track the forward-direction energy and its transport in the conditional trace identities, aiming to remove La/n from empirical isometry. The volume law gives a constraint: any bulk-isometry proof at La/n->t>0 must allow small singular values whose logarithms contribute order n in total. It does not prove that only one direction carries this contribution. A moving decomposition into the forward direction and its orthogonal complement may isolate the missing estimate.

All intentional writes stayed in this folder; earlier folders were read without modification. No git, subagents or external-store updates.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 11:28 Asia/Tbilisi.
