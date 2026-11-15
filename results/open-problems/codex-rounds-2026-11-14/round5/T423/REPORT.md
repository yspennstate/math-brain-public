VERDICT: PARTIAL uniform small-mass local-time and occupation bounds

The round 4 coefficient holds on independent re-derivation. The new
result bounds what can happen after either total mass first becomes
small. Write U,V for the masses, D=U-V, M=min(U,V),
A=integral (sqrt(u)-sqrt(v))^2, and L for symmetric local time of D
with coefficient one in Tanaka's formula. For
tau_a=inf{t:M_t<=a},

\[
\mathbb E(L_\infty-L_{\tau_a})\leq2\min(m,a),
\qquad m=\int u_0.
\]

The spatial consequence is valid for every epsilon>0 and over the entire
lifetime:

\[
\mathbb E\int_0^\infty
 \mathbf1_{\{|U_s-V_s|<\varepsilon,\ \min(U_s,V_s)\leq a\}}
 \int(\sqrt{u_s}-\sqrt{v_s})^2\,dx\,ds
\leq4\min(m,a)\varepsilon+\varepsilon^2.
\]

Taking a=epsilon gives at most 5epsilon squared. This removes the
small-total-mass region as a possible source of the linear occupation
coefficient. Uniqueness is equivalent to proving the remaining
o(epsilon) estimate where both masses exceed a, for every positive a
in a sequence decreasing to zero. The stopping version and the precise
equivalence are in PROOF.md.

The proof uses the minimum decomposition M=m+N-L/2. Bounded optional
sampling gives an exact post-entrance balance; monotone convergence
gives the lifetime budget. The earlier convex occupation approximation,
applied at a bounded stopping time, gives the finite-width bound without
any weighted local-time limit. An independent concave test of M checks
the factor 2. Independent scalar Feller masses attain that factor in the
broader mass-martingale class; these are not spatial SPDE examples.

This does not solve T423 or control cancellation at equal positive
masses. No novelty in the literature is claimed. The constants are
upper bounds, not asymptotic formulas or claimed optima for spatial pairs.

Commands:

    OMP_NUM_THREADS=1 nice -n 15 python3 audit.py

LOG.md records reading, the independent recheck, the chosen extension,
the derivations and audit output. The script checks exact algebra,
occupation normalization, concave cutoff signs, constants, scalar
examples and document consistency. It does not simulate the SPDE.
All runs are tiny, single-threaded standard-library calculations.
The inherited nice value is 20; the nice wrapper warns when trying
to change it to 15. No git, subagents, or writes outside this folder.

What failed: almost-sure extinction does not let one discard
E[M_T 1_{tau_a<=T}] in the exact stopped balance. Identical masses
give a counterexample to that unjustified passage: their local time
is zero while the terminal expectation tends to min(m,a).
No equality in the budget or general vanishing of local time follows.
Finite-width occupation can also continue after one mass dies; a scalar
Feller potential checks the retained epsilon-squared remainder exactly.

The bounded literature check found no verified resolution. Hao Wang's
[arXiv:1612.06055](https://arxiv.org/abs/1612.06055) remains withdrawn
because of a gap. Opened records for Leonid Mytnik and Johanna Weinberger,
[arXiv:2509.10984](https://arxiv.org/abs/2509.10984), and Yi Han,
[arXiv:2611.07310](https://arxiv.org/abs/2611.07310), concern weak
uniqueness, the latter with uniformly nondegenerate diffusion.
Yu-Ting Chen's [arXiv:1308.5141](https://arxiv.org/abs/1308.5141)
includes immigration. The opened abstract of Beom-Seok Han, Kunwoo Kim,
and Jaeyun Yi, [arXiv:2407.06827](https://arxiv.org/abs/2407.06827),
places its uniqueness result in the strict-positivity regime.
Limited search coverage is not proof that no resolution exists.

Next worker: use a fixed a>0 and target the spatial occupation estimate
before tau_a, or on min(U,V)>a. The low-mass remainder is now bounded
by 2a after normalization, uniformly over the lifetime. One still
needs spatial information to control cancellation of u-v at positive
total mass. A positive total-mass floor does not imply a positive
pointwise lower bound on either density.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 09:16 Asia/Tbilisi session start.
