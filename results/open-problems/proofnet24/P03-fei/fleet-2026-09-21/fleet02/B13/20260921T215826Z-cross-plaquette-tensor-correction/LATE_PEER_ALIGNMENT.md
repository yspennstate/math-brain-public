# Late peer alignment — fleet01/B17 plaquette stability and fleet02/B18 Hodge handoff

After the main B13 report was committed, I read the newer compatible fleet01/B17 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B17/20260921T213535Z-plaquette-factorization-stability/REPORT.md`

and its `FOLLOWUP.md`.

The B17 report proves for the same Boolean cross-plaquette weight

\[
W_{A\mid B}=\sum_{i\in A,j\in B}p_{ij}
\]

the global Hamming stability

\[
\delta_{A\mid B}(f)\le W_{A\mid B}/4
\]

and a spectral-product Hellinger bridge.  Therefore the **Hamming-distance corollary** `Pr(c=-1)<=P/4` in the B13 main report independently overlaps B17's earlier completed theorem; it must not be presented as a new unique factorization result.  This addendum preserves provenance and makes no novelty claim.

The genuinely nonduplicate part of the present B13 derivation is the stronger **actual-anchor conditional code**.  It constructs one physical anchor branch `b_0` and majority signs with fibre errors `q_b` satisfying

\[
\boxed{\mathbb E_b\,2q_b\log_2(1/q_b)\le W_{A\mid B}/2,}
\]

hence

\[
\boxed{\mathbb E_b h_2(q_b)\le W_{A\mid B}/2.}
\]

B17's global `delta<=W/4` does not imply this distribution-sensitive conditional Shannon statement, and its open all-cut logarithmic conjecture concerns `W` versus the **single global optimum** `delta`.  Conversely the B13 conditional average does not settle that open conjecture because `q -> 2q log(1/q)` is concave: an upper bound on the average fibre cost does not lower-bound it by the cost at the averaged error.

The B17 follow-up also refutes the shortcut `W>=I(e)` for the nearest-product residual set.  The B13 proof does not use that false comparison: it applies Poincare separately to each signed A-edge ratio row `u_e` before choosing an anchor, then applies edge isoperimetry to each actual child-ratio function `R_{b,b_0}`.  Thus the proved conditional code survives the B17 counterexample without reopening the killed shortcut.

This distinction matters for the source-frontier application.  Fleet03/B13 gives one actual reveal block with defect-paid expected child centered influence.  The B13 anchor theorem now gives, for that same actual family of children, one genuine child `f_{a_0}` and a conditional inter-child sign code bounded by

\[
\sum_{i\in A_*}j_i\log_2(1/j_i)+2\mathcal D_{A_*}.
\]

That is the retained contribution of this run; the global Hamming stability endpoint is attributed to the already completed B17 result.

I also read the latest shared fleet02/B18 Hodge/R16 handoff.  It is an interface-C source-current result: the q=1/q=3 cross-degree Hodge companion survives at the needed obstruction scale while syndrome diagonalisation would kill it.  It is compatible with the present A/B physical factorisation code but does not pay the remaining Fourier Shannon transfer.  No C-interface credit is reused here.

**Full FEI remains OPEN.**
