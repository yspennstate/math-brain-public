VERDICT: PARTIAL specialized the regular invariant-kernel variational principle and proved an explicit temperature error; hierarchical equality remains open

The earlier Erdős–Rényi deduction survives independent rechecking,
conditional on its stated external theorems. The bounded recent-literature
search found no advance beyond the earlier reports that settles the
regular hierarchical formula. No complete external solution is asserted.

New beyond round 3: [PROOF.md](PROOF.md) specializes Theorem 2.7 of
Amin Coja-Oghlan and Will Perkins, *Spin systems on Bethe lattices*,
[arXiv:1808.03440v1](https://arxiv.org/html/1808.03440), to binary
antiferromagnetism. It gives the exact regular-ensemble value as a
zero-temperature limit of an optimization over invariant kernel laws.
That is an existing broader variational principle, not the claimed
Mézard–Parisi hierarchy restriction. The deduction explicitly checks POS,
strictly subunit edge weights, spin-prior normalization and concentration.

For integer d>=3, let Phi_d(beta) denote the minimum defined in PROOF.md.
For every beta,L>0 the result includes

\[
 0\leq c_d-\left[\frac d2+
       \frac{\Phi_d(\beta+L)-\Phi_d(\beta)}L\right]
 \leq \frac{\log2}{L}\log(1+L/\beta)\leq\frac{\log2}\beta.
\]

The entropy proof needs no differentiability of the limiting pressure
and no exchange of temperature limits with infima. The invariant spaces
depend on temperature. This explicit error is an elementary refinement
of the temperature passage, not a numerical evaluation of c_d.

The opened paper's HTML Potts specialization displays an edge-term sign
inconsistent with its general equation (2.12). The proof uses (2.12);
edge-weight scaling and direct finite-graph differentiation check its
minus sign. This does not invalidate the external general theorem.

Commands: read-only pwd, rg --files, ls, cat, sed -n, date; primary papers
opened with the web search tool; local files written with apply_patch.
[LOG.md](LOG.md) records the searches and checks. No research computation,
script, git operation, subagent or write outside this folder was used.

What remains unproved: equality of the invariant-kernel minimum with
the finite-hierarchy regular cavity infimum. General invariant laws and
arbitrary cascade trials cannot simply be identified; arbitrary cascade
trials have not been shown invariant. The cited external general theorem
has not been independently audited in full. Degree 2 is outside its
d>=3 hypothesis; no extension to that case is claimed here.

What failed: the regular theorem did not supply the hoped-for
hierarchical identification. Its extra structural requirement remains
the obstruction; no numerical optimization was attempted.

Next worker: start with equation (11) of PROOF.md. Establish the regular
hierarchical interpolation upper bound with exactly that normalization,
then seek the matching lower bound by controlling the invariant kernel
minimizer's structure. Even an o(beta) comparison of the two optimized
pressures suffices for the zero-temperature target; (9) already controls
the temperature passage. Merely replacing a Poisson count by d in the
old proof supplies no such lower bound.

Task: “take the NEXT checkable step on this problem, building on that work”
— T122, received 2026-11-15 approximately 04:55 +04 (Asia/Tbilisi).
