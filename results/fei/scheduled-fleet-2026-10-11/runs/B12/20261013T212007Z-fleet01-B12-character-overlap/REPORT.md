# B12 / A058 — character-only overlap closure and a sharp shared-potential no-go

## Outcome

**PROVED proper overlap class; REFUTED the natural general shared-coordinate
potential; independent review pending.**

The previous A057 theorem allowed arbitrary interleaving only when activation
and source used disjoint physical blocks.  Its explicit remaining obstruction
was one coordinate that changes both objects simultaneously.  This run gives
the first exact positive class on that boundary.

Let a shared coordinate block `Y` be reused by arbitrarily many Boolean
factors

\[
 g_j=\chi_{R_j}f_j,
\]

where each residual `f_j` lives on its own disjoint block.  Then

\[
 \prod_jg_j=\chi_{R_1\triangle\cdots\triangle R_m}\prod_jf_j,
\]

and exactly

\[
 H\!\left(\prod_jg_j\right)=\sum_jH(f_j),\qquad
 I\!\left(\prod_jg_j\right)
 =|R_1\triangle\cdots\triangle R_m|+\sum_jI(f_j).
\]

Consequently, if every residual factor obeys FEI with constant `C`, the
overlapping product obeys FEI with the **same** constant `C`.  There is no
dependence on dimension, factor count, overlap count, reuse multiplicity,
depth, or cancellation count.  The selector corollary covers antipodal
endpoints `F=hb` when activation and source share an arbitrary character
core.

This is strictly outside fresh-selector orthogonality: the same physical bit
may appear in every factor, and even multiplicities cancel rather than being
charged repeatedly.

## Certified obstruction beyond the class

The most natural overlap correction to the A057 Doob potential is

\[
 \widetilde J=\mathcal E(a+hb)-\mathcal E(hb)+\mathcal E(b),
\]

which agrees exactly with the accepted disjoint potential.  It is not
restriction-monotone.  An explicit genuine three-bit Boolean triple has

\[
 \Delta_3\widetilde J
 =-\left(\frac54-\frac9{16}\log_2\frac{16}{9}\right)
 =-0.7830828133\ldots.
\]

For the same witness `D_3(F)=D_3(a)=D_3(b)=0`.  Hence no fixed correction by
the separate raw entropies of `a` and `b` can restore monotonicity.  This is a
four-channel shared-coordinate obstruction, not a dummy restriction and not a
non-Boolean relaxation.

## Verification

The checker directly reconstructed:

- 38,860 exhaustive character-overlap products;
- 5,000 deterministic pseudorandom products through 14 physical variables;
- 8,192 shared-potential decrements over every two-bit Boolean triple; and
- the exact three-bit negative witness.

All exact entropy and influence laws passed.  The two-bit potential happens
to be monotone, showing that three bits are necessary for this particular
countermechanism; this finite observation is not used in the theorem.

## Previous and new scope

- **Previous:** arbitrary query interleaving with disjoint activation/source
  blocks; no simultaneous shared query.
- **New:** unlimited simultaneous reuse when shared dependence is character
  only, with exact constant preservation at arbitrary depth.
- **Refuted extension:** monotonicity of the gauge-corrected shared Doob
  potential, even after adding separate endpoint raw entropies.
- **Still open:** non-character shared overlap, where a joint signed
  four-channel collision ledger is required.

Full FEI remains **OPEN**.

## Source pins

- owner control `2026-10-12.1`:
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- A057 disjoint interleaved theorem:
  `64e6c2db69a6a3b61b3b1ea63b7c80b8d7d4ea88`, core proof commit
  `ffa97db738c479d16888d5380950981ed38160ff`;
- preceding A056 spectral-sector theorem:
  `4a49db96f14feba190609a1fff09e52353bdc6d9`;
- open-problems head inspected before the run:
  `ed48e79876a2da66ddc63701e701271db11226c2`;
- Brain head inspected before the run:
  `84a1c1b7a8603fe8bc00dc797916aa6ac6a201ac`.

No external novelty claim is made.
