VERDICT: PROVED running-path-supremum linear-growth drift extension, conditional on the prior drift-free input

The round-5 result checks. Independently reconstructed its universal
predictable representative and weighted canonical integral, including
the change of integrator under equivalent measures. Re-ran its 54-case
history-dependent Gaussian diagnostic successfully. No error was found.

The new piece replaces its current-norm growth bound by

    ||B(t,path)||_2 <= K(1 + sup_(r<=t)||path_r||_2).

PROOF.md establishes weak existence and uniqueness of the state-path law,
equivalence with the drift-free law, and both finite entropy identities
under this larger hypothesis. It permits jointly Borel nonanticipating
H-valued drift, unbounded elliptic globally beta-Hölder diffusion,
0<beta<1, and every deterministic L2 initial state, conditional on the
same drift-free input as the earlier reports.

The missing estimate is now proved uniformly for all predictable drift
multipliers kappa in [0,1]:

    E sup_(t<=T)||U_t||_2^8 <= C8(T)(1+||h||_2^8),
    E(1+sup_(t<=T)||U_t||_2^2) <= C2(T)(1+||h||_2^2).

Hilbert-space factorization with p=8 and eta=3/16 gives this bound by
ordinary integral Gronwall. Its inner heat singularity is 7/8 and its
outer Holder exponent is -13/14. The combined time factor is t. All
constants and the localization argument are written out. This supplies
the uniform energy bound needed for both stopped changes of measure.

The unbounded delay drift B(t,path)=a path_((t-delta)^+) is a strict new
example, even with a fixed zero initial state. A rank-one delay example
also gives direct conditional Gaussian normalization and both entropies
a^2 delta^2/4 on [0,2delta]. Its endpoint mass variance is independently
checked by Brownian covariances and stochastic isometry.

The external input remains Proposition 8.1 of Yi Han,
*Weak uniqueness for the stochastic heat equation with nondegenerate
diffusion: the full Hölder regime*,
[arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1),
combined with round 3's initial-data extension. The short literature
check found the same version and scope already recorded by the earlier
rounds. No later result changed that picture, and no new
SOLVED_ELSEWHERE.md was written. This is not an independent proof or
full audit of Han's positive-Hölder uniqueness theorem.

Commands, both exiting 0:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T179/check_history.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_maximal.py
```

The new diagnostic checks nine exact time-integral identities, five general
scaling cases, the explicit martingale constant, 24 exact delay variance
cases, and continuous random-spike moment examples. The nonsingular beta
integral quadrature residual was 1.27e-12. Runtime was 0.001s and peak RSS
13.58 MiB; actual nice was 20. The prior rerun used 13.89 MiB and 0.280s.
The launcher's priority warning reflects the inherited nice value, checked
inside both scripts. Full output is in LOG.md. These are arithmetic
diagnostics, not simulations or numerical proofs of SPDE uniqueness.

What failed: fixed-time moment bounds cannot replace the required maximal
bound; an explicit continuous fixed-start random-spike mixture has bounded
fixed-time second moments and infinite expected squared maximum. Full
Novikov can also fail for the rank-one delay example when a^2 delta^2>=3
(a sufficient, non-sharp condition), despite exact density normalization.
The proof avoids both shortcuts. One patch failed context matching and
was reapplied; no diagnostic failed.

Uncertainty: the same external drift-free theorem remains unaudited in
full. No unresolved estimate is assumed in this transfer proof. The
explicit constants are large upper bounds. No beta=0, pathwise uniqueness,
or superlinear-history-growth result is claimed.

Next worker: audit the H-factorization and stopped-history comparison in
Sections 2--3. If these check, extend the theorem to arbitrary initial
distributions with finite second moment. This needs conditioning the
deterministic-start bound and constructing a measurable mixture of the
drift-free laws; directly applying an eighth-moment bound to a random
initial state would impose an unnecessary eighth-moment hypothesis.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 11:07 Asia/Tbilisi.
