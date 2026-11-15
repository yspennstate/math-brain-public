VERDICT: PARTIAL volume-uniform simultaneous first rotation for truncated good cells in diluted Ising chains

The round-4 local inverse and cubic remainder survive an independent audit.
The new result fills its proposed next step: an exact simultaneous rotation
with a remainder bounded in a per-site interaction norm, uniformly in chain
length and active-block Hilbert-space dimension. The full T098 problem
remains open here.

Keep the diluted Ising Hamiltonian H0 of the previous reports, and add
V=sum_f epsilon_f X_f at frozen sites, with |epsilon_f|<=epsilon. Retain a
generator only when all its first-flip denominators have magnitude at least
delta and its support interval I_f has physical diameter at most ell.
Write V_R,V_D for the retained and discarded perturbations and A=sum_R A_f.

Group each active block into one tensor factor and keep frozen singletons as
separate factors. Each generator touches at most five factors; each factor
belongs to at most three generator supports. The interaction norm is the
maximum, over physical sites x, of

\[
 \sum_{S\ni x}e^{\mu\operatorname{diam}S}\|\Phi(S)\|.
\]

Supports are assigned as unions of those factors. Let alpha be this norm
for the generator interaction. With C=sqrt(8/3),

\[
 \alpha\le3e^{\mu\ell}C\epsilon/\delta,\qquad q=10\alpha.
\]

For q<1, the proof constructs interactions Q,T satisfying the exact identity

\[
 e^A(H_0+V)e^{-A}=H_0+V_D+Q+T,
 \quad Q=\tfrac12[A,V_R]+[A,V_D],
\]
\[
 \|Q\|_\mu\le\epsilon q,\qquad
 \|T\|_\mu\le\frac{\epsilon q^2}{1-q}.
\]

Here Q,T in the Hamiltonian identity denote the sums of their interaction
terms. The norm bound also gives an exponential physical-diameter tail for
the remainder. No volume-uniform bound on the global operator norm of A is
assumed. The proof includes a sharper estimate when V_D=0 and an independent
integral derivation of the remainder constant. See [PROOF.md](PROOF.md).

At a specified frozen site, the probability its generator is discarded is
at most

\[
 \min\{1,F_p(4\rho\delta)+p^{\ell-1}[\ell-(\ell-1)p]\},
\]

with F_p the preceding report's capped geometric resonance bound. Taking
delta=epsilon^beta, 0<beta<1, ell proportional to log(1/epsilon), and mu=1/ell
makes this probability tend to zero and gives
||T||_(1/ell)=O(epsilon^(3-2 beta)), uniformly in volume. The decay length
ell grows in this choice. These estimates cover all states, without an
energy restriction.

Reproduce both checks from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_previous.py > previous_stdout.txt 2> previous_stderr.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_simultaneous.py > simultaneous_stdout.txt 2> simultaneous_stderr.txt
```

The prior-result audit passed 12 Sylvester/spectral comparisons with
interlaced, degenerate, and separated sectors; largest inverse residual
5.04e-17. The extension audit passed 2,046 structural masks, 4,572 exact
rational path-majorant checks, 60 exact recurrence checks, 324 exact cutoff
probabilities, and 27 exact geometric-tail checks. It also passed 67 matrix
cases through dimension 128, eight orders each, three direct matrix-integral
checks, and five scalar-integral checks. The largest direct-conjugation
versus eight-order-series error was 3.72e-14. The matrices are floating-point
audits, not certified intervals.

The final extension run used 42,663,936 bytes peak RSS and .598 seconds.
Both scripts verified nice 20; all five numerical thread limits were one.
stderr contains only macOS's redundant nice-adjustment denial. Full data:
[previous_audit.json](previous_audit.json),
[simultaneous_verification.json](simultaneous_verification.json), and
[LOG.md](LOG.md). No numerical run failed and no earlier folder was modified.

The bounded literature search found no newer unconditional solution.
John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains*,
[arXiv:1403.7837](https://arxiv.org/abs/1403.7837), retains the level-attraction
assumption. Francois Huveneers, *Many-body localization: an introduction for
mathematicians*, [arXiv:2609.39462, Section 4.5](https://arxiv.org/html/2609.39462v1#S4.SS5),
discusses the remaining high-probability problem. Both sources were opened.
An unindexed paper could have been missed. No literature novelty is claimed
for the elementary interaction inequalities.

What failed: no proposed inequality or numerical check failed, but a
single-barrier cubic commutator estimate still cannot be applied independently
to every barrier. A resonant three-site example has
||[A,V_D]||=1.8798750857549214e-5, so omitting the bad-site quadratic term
would be wrong. The simultaneous estimate includes it. A direct norm
estimate using ||sum A_f|| would grow with volume; the interaction estimate
avoids that loss.

What remains uncertain: this does not control the new active-label gaps,
renormalized denominators, or growth of resonant regions. In particular,
the bound on T does not justify a second rotation or exact conserved l-bits.

Next worker: prove a size tail for connected clusters of discarded cells,
using the cutoff to obtain local dependence and conditioning on g,J if
needed. This would turn the fixed-site rarity estimate into a rare-block
estimate. Specify the physical connectivity and include oversized cells;
do not assume independence of neighboring good events. The new-gap problem
would still remain after that step.

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, approximately 08:15 Asia/Tbilisi.
