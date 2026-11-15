VERDICT: PROVED finite-cascade kernel invariance, yielding the regular hierarchical upper bound

The round 4 result survives independent checking, conditional on its
stated external theorem. The bounded literature search found no new
regular-ensemble solution. The fixed-degree cavity equality remains
unproved here.

New beyond round 4: [PROOF.md](PROOF.md) proves that every no-root finite
Ruelle-cascade trial in its equation (11) defines an invariant weak-kernel
law. The proof handles every bounded positive function of finitely many
sampled columns, including all finite cavity tilts. Successive marked
Poisson point processes preserve the cascade's weighted tree law; a
measure-preserving permutation of product column coordinates removes
the resulting branch relabeling. Biased sampled marks are explicitly
allowed.

This supplies the missing trial-space inclusion. For the hierarchical
infimum J_d(beta) defined in PROOF.md and cut pressure p_d(beta),

\[
 p_d(\beta)\le J_d(\beta),\qquad
 c_d\le J_d(\beta)/\beta.
\]

The general upper bound already appears in Viktor Harangi,
[*RSB bounds on the maximum cut*, arXiv:2506.21296v1,
Theorem 3.2](https://arxiv.org/html/2506.21296v1).
The contribution of this folder is the explicit invariant-law inclusion
and derivation in the earlier report's normalization, using Theorem 2.7
of Amin Coja-Oghlan and Will Perkins,
[*Spin systems on Bethe lattices*, arXiv:1808.03440v1](https://arxiv.org/html/1808.03440v1).
It is not a new numerical bound or a proof of the full cavity formula.

Checks: proved the Poisson intensity scaling directly; verified depths
one and two independently; matched cascade exponents to Harangi's
convention; tested asymmetric endpoint messages where the marks really
are biased; checked row and column map orientations, infinite cascade
summability, measurability, all constant shifts and the entropy error.
Details and the exact asymmetric test values are in [LOG.md](LOG.md).

Commands: read-only pwd, rg --files, cat and sed -n; primary papers
opened with the web search tool; local files written with apply_patch.
Read commands were launched with `nice -n 15 env OMP_NUM_THREADS=1`.
The sandbox rejected the priority change, so no research computation
or script was run. No git, subagents or writes outside this folder.

What failed or remains uncertain: no reverse comparison was obtained.
The external invariant-law theorem's full proof remains unaudited.
No degree-two extension or interchange of hierarchy infima with the
temperature limit is claimed. An initially truncated read was repeated
in smaller pieces. No mathematical counterexample was found in the
analytic checks. A final prose cleanup patch needed a context correction;
no mathematical change resulted.

Next worker: write Delta_d(beta)=J_d(beta)-p_d(beta)>=0. Equation (19)
of PROOF.md shows that the zero-temperature equality is equivalent to
Delta_d(beta)=o(beta). Seek cascade trials whose functional values are
within o(beta) of the invariant-law minimum. The upper-bound inclusion
is now proved; it does not establish that approximation or require
arbitrary invariant minimizers to be hierarchical.

Task: “take the NEXT checkable step on this problem, building on that work”
— T122, received 2026-11-15 approximately 08:23 +04 (Asia/Tbilisi).
