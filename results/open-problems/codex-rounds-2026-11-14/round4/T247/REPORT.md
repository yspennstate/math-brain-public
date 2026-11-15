VERDICT: PARTIAL unnormalized joint-limit empirical isometry for vanishing-variance backward-critical orthogonal tanh networks

The earlier results hold. The new result removes the random scalar normalization in a concrete genuine nonlinear network, with a deterministic gain identical at every layer. The full joint-limit density and the fixed positive-variance critical problem remain unresolved here.

Let

\[
h_l=\tanh(g_nO_lh_{l-1}),\qquad
g_n^2=\left[\mathbb E_{G\sim N(0,1)}\operatorname{sech}^4(\sqrt{a_n}G)\right]^{-1},
\qquad g_n^2\|h_0\|^2/n=a_n>0,
\]

with independent real Haar \(O_l\), zero bias, and deterministic input. If \(n,L(n)\to\infty\) and

\[
L(n)a_n^2+\frac{L(n)a_n}{n}\longrightarrow0,
\]

then the empirical distribution of the squared singular values of the **ordinary, unnormalized** input-output Jacobian converges to \(\delta_1\) in \(W_2\), in probability. The same theorem holds for the spherical derivative-critical gain, or any deterministic gain satisfying \(|\log(g_n^2)-2a_n|\leq15a_n^2\). The input may have any deterministic direction.

This extends round 3 in two ways within the same argument: it supplies the missing high-probability forward-radius envelope and proves that the accumulated scalar gain tends to one. Precisely, with

\[
q_l=g_n^2\|h_{l-1}\|^2/n,\qquad
S_L=\prod_{l=1}^L g_n^2\mu_n(q_l),
\]

the proof gives \(\max_{l\leq L+1}|\log(q_l/a_n)|\to0\) and \(S_L\to1\) in probability. It does not require \(La_n\to0\): for example, \(a_n=n^{-2}\), \(L=\lfloor n^{5/2}\rfloor\) are covered. [PROOF.md](PROOF.md) contains every estimate and an explicit finite probability bound in equation (37).

The main step compares \(\log S_L\) with the telescoping forward log-radius. For the exact spherical forward ratio \(F(q,u)\),

\[
\mathbb E\log F(q,u)=-\frac{2n}{n+2}q+O(q^2),\qquad
\operatorname{Var}(\log F(q,u))\leq36q^2,
\]

with the first remainder bounded by \(24q^2\), uniformly in dimension. The scalar/radius drift mismatch is at most \(4q/(n+2)+39q^2\). A restoring-drift argument and a stopped martingale control the forward radius. The preceding dependent-gate distortion theorem then applies to a frozen Gram process and agrees with the actual Jacobian on the high-probability event. No independent-gate replacement or freeness assertion is used.

Verification commands, all exiting 0:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_independent.py > recheck_independent_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_dependent.py > recheck_dependent_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_critical.py > verification_output.txt 2>&1
```

The first two are local copies of the round-3 scripts; only the dependent script's JSON output filename was changed. They reproduced 20 rational product checks, 15 exact residual-Haar integrations, eight full-Haar quadratures and the actual depth-30 network checks. An independent algebraic re-derivation also confirmed the earlier accumulated bound.

New checks include eight exact Dirichlet-moment calculations; 110-digit global scalar inequalities, including large coordinates and tiny variances; doubled sphere quadrature; both leading radial/scalar coefficients; and 100000 checks of the discrete last-crossing inequality. The scalar/radius mismatch coefficient at n=3 was -0.7999999996, versus exact -0.8. Actual critical-gain Jacobian products at n=64, L=120 had mean unnormalized distortion .000158672 and mean normalized distortion .000158685, below the proved stopped bound .0639479. The final script used less than 1 GB RAM, one thread, niceness 20 and a few seconds; exact resource measurements and parameters are in [results.json](results.json) and [verification_output.txt](verification_output.txt).

What failed or remains uncertain: no mathematical or numerical verification failed in this session. A direct absolute sum of the scalar increments would require the stronger condition \(La_n\to0\); the radius comparison avoids that restriction. The estimates are deliberately coarse. At n=64, L=10000, a=.0002, a separate forward simulation gave mean S=.910903; finite-width scalar drift is visible, consistently with the required \(La/n\to0\) condition. Expected unnormalized distortion convergence, operator isometry, spectral edges, necessity of the sufficient scaling, and positive stationary variance with bias are not proved. The gain is backward-critical at the target a; exact zero-bias forward stationarity at that target is not assumed. No novelty claim relative to the entire literature is made.

The bounded literature check found no verified resolution; details and opened sources are in [LITERATURE.md](LITERATURE.md). Both earlier folders were read without modification. All intentional writes stayed in this folder; no git, subagents, messages or external-store updates were used.

Next worker: extend the radius/scalar comparison to a small nonzero stationary variance maintained by independent biases at the usual simultaneous forward/backward critical initialization. The present proof isolates what must change: the exact radial recursion and the dependent-gate one-layer estimate with bias. A different next target is determining whether the sufficient \(La/n\to0\) condition can be removed for empirical isometry by exploiting the special geometry of the forward direction. Neither task is claimed complete.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 05:12 Asia/Tbilisi.
