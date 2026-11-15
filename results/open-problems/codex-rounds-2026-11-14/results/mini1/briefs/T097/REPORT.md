VERDICT: PARTIAL a capacity-based lattice reduction and a relative one-arm crossover lower bound

For the lattice GFF with simple-random-walk Green covariance, PROOF.md proves
the finite-scale inequality

    p_R(h+t) >= Phi(Phi^{-1}(p_R(h))-t sqrt(cap(B_R))),
    cap(B_R) <= (28R-1/R)/3.

Here p_R(h) is the lattice probability of connecting 0 to the sup-norm sphere
of radius R at level h. The capacity coefficient is optimal over all
increasing events measurable on the box, as witnessed by half-spaces.
Optimality for the connection event is not asserted.

The resulting checkable consequences are:

- If theta(h_*-t)=t^{beta+o(1)} and p_R(h_*)=R^{-rho+o(1)} with finite
  nonnegative exponents, then beta >= 2 rho.
- Combining the comparison with Stephen Muirhead's existing density theorem
  gives p_R(h_*) >= R^{-2-epsilon} for every epsilon>0 and all sufficiently
  large R. No existence of rho is required.
- Let L_rel(t) be the first integer R for which
  p_R(h_*+t)<=p_R(h_*)/2. Then L_rel(t) is finite and
  L_rel(t)>=c t^{-2}/log(1/t) for small t. A logarithmic exponent for this
  particular radius, if it exists, is at least 2.

This is a proved reduction using standard Gaussian methods. Novelty is not
established. It does not settle any of the requested exact lattice exponents.

The external input is Stephen Muirhead, *Percolation of strongly correlated
Gaussian fields II. Sharpness of the phase transition*,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2 and
1.10. In this dimension they give theta(h_*-t)>=c_q t^q for every q>4;
using q=4 itself would be unjustified. LITERATURE.md records the opened
sources. The new November paper
[arXiv:2611.05357](https://arxiv.org/abs/2611.05357) concerns cable clusters
in the high-dimensional regime, so does not settle this lattice question.

The literature search took less than ten minutes. No numerical computation
or data file was needed. Exact numerical command: none. Read-only orientation
used commands prefixed with `OMP_NUM_THREADS=1 nice -n 15`; the sandbox denied
the priority change, and no numerical workload followed. Mathematical outputs
are the proofs in PROOF.md. AUDIT.md records two derivations of the comparison,
an independent Hölder check of the exponent calculations, and two exact
calculations of the energy constant. LOG.md records the steps and searches.

What failed: the comparison alone does not yield a constant-factor
`L_rel(t)>=c t^{-2}` bound; the normal-tail loss grows at that proposed scale.
It does not equate L_rel with a two-point or crossing correlation length.
It does not rule out critical percolation, establish exponent existence,
or transfer cable exponents to the lattice. The literature check cannot
certify that these elementary consequences have not appeared elsewhere.

Next worker: seek a connection-event-specific improvement of the score bound
in PROOF.md section 2, or prove a comparison between L_rel and a chosen
correlation length. Either would address a missing step; merely substituting
cable exponents would not. A sharper density lower bound in (12) would also
improve the unconditional one-arm bound immediately.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
first recorded local time 21:16:48 +04 (Asia/Tbilisi).
