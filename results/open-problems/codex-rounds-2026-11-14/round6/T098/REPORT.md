VERDICT: PARTIAL volume-uniform exponential size tails for the first discarded blocks in diluted Ising chains

The round-5 simultaneous rotation survives an independent analytic audit
and a rerun of its computation. The new result proves its proposed next
step: a size tail for physically connected unions of discarded cells,
including oversized cells and mergers through shared frozen controls.
The full T098 stability problem remains open here.

Use the same Bernoulli-diluted model, bounded longitudinal-field density
rho, all-state first-flip threshold delta, and diameter cutoff ell>=2.
Let D be the discarded frozen sites and let E be the union of their full
support intervals I_f. Merge overlapping or touching intervals using
physical nearest-neighbor connectivity. For the component E_x containing
a specified site x, set E_x empty outside E. Put t=4 rho delta<1 and

\[
 \kappa=1-(1-p)^5(1-t)^3<1.
\]

Uniformly in chain length, for every integer n>=1,

\[
 \mathbb P(|E_x|\ge n)
 \le\min\{1,n\kappa^{\lfloor n/5\rfloor}\}.
\]

The probability of any block of size at least n in a chain of length L
is at most min(1,L kappa^floor(n/5)). No upper size cutoff on the discarded
cells is imposed. These are exponential size tails; their constants can
be weak when p is close to one.

The key input is conditional independence. Once the indicators, active
fields, and g,J are fixed, each frozen site's selection event depends
only on its own h_f. All other frozen longitudinal fields cancel from
its first-flip differences. Five consecutive frozen sites whose middle
three are retained leave their center outside every discarded cell.
Disjoint five-site separator events are independent conditional on g,J,
with probability at least (1-p)^5(1-t)^3.

The blocks also have vanishing site probability. With the round-5 bound

\[
 b=\min\{1,F_p(t)+p^{\ell-1}[\ell-(\ell-1)p]\},
\]

for every integer r>=1,

\[
 \mathbb P(x\in E)
 \le\min\{1,3[(2r+1)(1-p)b+2p^r]\}.
\]

Thus their density is O_p(b[1+log(1/b)]) as b tends to zero. Taking the
previous delta=epsilon^beta and logarithmic ell gives vanishing density
and an exponential size rate bounded away from zero at fixed p<1 as
epsilon decreases. These estimates concern every local state, with no
energy restriction.

[PROOF.md](PROOF.md) gives all steps and a sharper core estimate:
P(J subset core)<=M^2 lambda^|J|, where
M=(1-p)/(1-p4^s), lambda=p16^s+(1-p)max(t^s,4^(-s(ell-1))),
0<s<=1 and p16^s<1. This core estimate is useful when lambda<1.
The proof distinguishes cores from merged full support intervals.

Reproduce the checks here:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_round5.py > round5_stdout.txt 2> round5_stderr.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_clusters.py > cluster_stdout.txt 2> cluster_stderr.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_conditioning.py > conditioning_stdout.txt 2> conditioning_stderr.txt
```

All passed. The new exact-rational audit covers 29,523 ternary geometry
cases, 38,352 independent-marking majorant configurations, 1,512 core and
1,512 full-cell interval bounds, 2,520 full-cell cluster bounds, 4,032
rarity bounds, and three actual-field separator integrations. The majorant
is a rigorous upper comparison, not a simulation of MBL. The independent
Hamiltonian audit checks 64 sectors and 108 transition multisets through
dimension 128; maximum cancellation error is 8.88e-15. These matrix checks
use floating-point arithmetic, not certified intervals.

The three accepted runs each used under 51 MB RSS and under 1.4 seconds.
Actual nice value was 20 and all five numerical thread limits were one.
The only stderr is macOS's denial of a redundant nice adjustment. Full
commands, output, resource figures and checks are in [LOG.md](LOG.md),
[cluster_verification.json](cluster_verification.json),
[conditioning_verification.json](conditioning_verification.json), and
[simultaneous_verification.json](simultaneous_verification.json).
No earlier folder was modified.

What failed: no proof inequality or computation failed. Padding cores can
merge them: two singleton cores in a five-site frozen chain can produce
one full-cell block of length five. A core-only tail cannot be applied to
the full union without addressing this merger; the separator proof does.
The dependence-range approach would lose its size rate as ell grows.

What remains uncertain: these are the first discarded blocks. There is no
estimate for their growth under later rotations, the new active-label
gaps, or renormalized energy differences. Conditional independence of the
first selection events cannot be assumed at later stages. No exact l-bits
for the fully perturbed chain are constructed, and no novelty is claimed
for the elementary probability inequalities.

The bounded literature search found no newer unconditional solution.
John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains*,
[arXiv:1403.7837](https://arxiv.org/abs/1403.7837), retains its
level-attraction assumption. Francois Huveneers, *Many-body localization:
an introduction for mathematicians*,
[arXiv:2609.39462, Section 4.5](https://arxiv.org/html/2609.39462v1#S4.SS5),
discusses the unresolved high-probability extension. Both papers were
opened. The bounded search can miss unindexed work.

Next worker: exactly diagonalize H0+V_D inside its occupied components,
using the retained frozen spins as controls, and bound the spatial tails
of the conjugated quadratic interaction Q and remainder T. The core
estimate above controls these components, including active-only ones via
equation (20) of the proof. Identify explicitly which resulting transitions
have an unused independent field. Same-barrier quadratic terms can mix
active labels while preserving frozen spins, so those terms cannot be
discarded or treated as scalar energy shifts.

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, approximately 10:50 Asia/Tbilisi; completed about 11:06.
