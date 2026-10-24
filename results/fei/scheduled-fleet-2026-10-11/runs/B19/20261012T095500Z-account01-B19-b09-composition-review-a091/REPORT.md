# B19 / A091 — B09 product-biased restriction and composition review

**Primary packet:** A091, composition referee  
**Reviewed object:** B09 run `20261011T195500Z-account01-B09-biased-restriction-uncertainty`  
**Verdict:** main lemma accepted; exact tensor transfer accepted; broad composition transfer not accepted; endpoint lower-bound repair proved by reviewer and pending fresh review  
**Full FEI:** **OPEN**.

## Accepted source claims

For every finite Boolean function under an interior product measure and every
physical revealed block `A`, the exact definitions in the B09 source satisfy

\[
L_A=M_A+J_A,\qquad J_A=I(Z;T)\ge0,
\]

and

\[
J_A\le M_A+\sum_{i\in A}
\left[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right].
\]

The proof's normalization, branch probabilities, tensor orthogonal matrix,
maximum-entry constant, and Maassen--Uffink rearrangement all reconstruct
exactly.  No repair was needed for this theorem.

The separately repaired two-bit interval certificate remains valid at its
finite scope: for the displayed AND sign gate at `p=1/8,q=1/4`,
`J_A-M_A>0.1195` bits.  This refutes only the tax-free biased helper, not FEI.

## New endpoint-sharpness result

The original report inferred endpoint necessity from the asymptotics of an
upper bound, which was insufficient.  A genuine Boolean lower-bound family
repairs that implication.

For `g(X,Y)=(-1)^(XY)`, reveal `X`, let `P(X=1)=p`, and fix
`P(Y=1)=q<1/2`.  Exact biased Fourier calculation gives

\[
J-M=\bigl(4q(1-2q)+o(1)\bigr)p\log_2(1/p).
\]

At `q=1/4`,

\[
J-M=\left(\frac12+o(1)\right)p\log_2(1/p).
\]

Thus no universal `O(p)` correction can replace the rare logarithmic tax.
The proved B09 tax has leading coefficient `1`, so its endpoint order is sharp
and its coefficient is within a factor two of this explicit lower bound.
This repaired corollary is new work by the reviewer and is therefore
`AUTHOR_PROVED_PENDING_A085_A090_REVIEW`.

## Composition scope correction

The B09 `M,J,Delta` ledger is exactly additive for product functions on
disjoint variable sets with aligned revealed blocks.  It is not shown to be a
cocycle for arbitrary Boolean composition.  O'Donnell--Tan's theorem composes
a biased `FEI+` functional under disjoint inner variable sets and explicit
gate/child hypotheses; it does not automatically provide the missing
single-use interface for this restriction tax.

Therefore the section-5 prose that decomposable gates create no new violation
“beyond their factors” is **not accepted at general-composition scope**.
Shared variables are outside both accepted transfers.

## Verification

The independent checker did not reuse the original B09 scripts.  It passed
5,643 deterministic assertions covering:

- every Boolean truth table through three variables;
- three nonuniform bias vectors per dimension;
- every nonempty physical revealed block;
- exact ledger normalization and the proved uncertainty inequality;
- disjoint exact-product additivity;
- the one-parameter AND endpoint family through `p=2^-50`.

Maximum ledger identity error was `6.661e-16`; the analytic proofs, not the
finite tolerances, establish the all-parameter claims.

## Sources and next step

- Original B09 report: commit
  `adb671ffcda143fa68347806bb96e8c305621a7d`, blob
  `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
- Repaired finite certificate: report/check/output blobs
  `c3adb486c8ca9f7a35f384ee82942eef66bd64be`,
  `0a6917feb25ab0e1cc0703c4c134b299c6e3243f`, and
  `d3db5bd09e009eb3f4f4d3572ccba9b6e6ce3239`.
- O'Donnell--Tan, arXiv:1304.1347, checked 2026-10-12.
- Maassen--Uffink, Phys. Rev. Lett. 60 (1988), 1103--1106.

The next unpaid step is a dimension-independent, nonreusing payment of
`M_A+Delta_A` through arbitrary changing-gate hierarchies, including reused
addresses and shared physical variables.  Full FEI remains open.

