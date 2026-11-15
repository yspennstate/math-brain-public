VERDICT: PROVED measurable linear-growth drift extension for unbounded diffusion and arbitrary L2 initial states, conditional on the prior drift-free input

The round-3 result checks. Independently re-derived its ordered-gap mass
conservation, comparison limit, and martingale identification. Re-ran its
exact-arithmetic diagnostic successfully. No error was found in its main
claim. Its external input remains Yi Han's bounded-start theorem; the main
full-positive-Hölder argument in that preprint has not been audited here.

The new piece is weak existence and uniqueness for

    dU = (Delta U + b(t,x,U)) dt + g(U) dW,

with every deterministic u0 in L2(T), unbounded uniformly elliptic globally
beta-Hölder g, 0<beta<1, and Borel b satisfying
|b(t,x,z)| <= B_T(1+|z|) on each finite horizon. No bounded initial spatial
norm is assumed. PROOF.md gives the complete transfer from the prior
drift-free result, a canonical density determined by the state path, and
mutual absolute continuity of drifted and drift-free path laws.

It also proves the exact entropy identities

    Ent(mu_b | mu_0) = (1/2) E_mu_b integral ||b(U)/g(U)||_2^2 dt,
    Ent(mu_0 | mu_b) = (1/2) E_mu_0 integral ||b(U)/g(U)||_2^2 dt.

Both quantities are finite, with an explicit bound depending only on the
horizon, coefficient bounds, ellipticity constant and ||u0||_2. These
identities check the density's sign and the factor 1/2. They do not require
uniqueness of the joint state-noise law.

The transfer method is already Proposition 8.5 of Yi Han,
*Weak uniqueness for the stochastic heat equation with nondegenerate
diffusion: the full Hölder regime*,
[arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1).
The new scope comes from combining it with the round-3 L2 extension. This
is not an independent proof of the original full-Hölder uniqueness result.
The brief literature check found no later change to the residual
unbounded-diffusion, rough-initial-data case already isolated by the prior
workers. No new SOLVED_ELSEWHERE.md was written.

Commands run:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T179/check_estimates.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_transfer.py
```

Both exited 0. The new diagnostic checked 27 rational Volterra parameter
triples, four Fourier/Gaussian heat-trace comparisons, and 24 exact
Gaussian density/sign/entropy cases. Actual priority was nice 20; peak
RSS was 13.27 MiB, runtime 0.002s. The launcher warning reflects the
inherited priority, verified inside both scripts. Full output is in LOG.md.
These are arithmetic diagnostics, not numerical tests of uniqueness.

What failed: applying full Novikov directly is not valid. For g=1, u0=0,
b(z)=kz, the drift-free law has E exp(A/2)=infinity whenever k^2 T^2>=3;
PROOF.md derives this sufficient, non-sharp divergence condition two ways.
The stopped-energy proof still works. No calculation or diagnostic failed.
A clarification removes a possible circular explanation: weak-to-mild
conversion under changed measures is localized before applying moment bounds.

Uncertainty: the conclusion retains the same external bounded-start
uniqueness input as round 3. No unresolved estimate is assumed in the new
transfer proof. No pathwise uniqueness or initial-data contraction for the
drifted equation is claimed.

Next worker: audit the canonical predictable-integral construction and the
entropy change of integrator in Sections 6–7. If these check, a concrete
next extension is a nonanticipating H-valued drift B(t,path), with growth
bounded by C(1+||path_t||_2). The current moment and energy estimates suggest
this transfer, but its path-space predictability hypotheses and density
construction should be written out before claiming it.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 04:59 Asia/Tbilisi.
