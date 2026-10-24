# B12 / A056 — spectral-sector composition theorem

## Outcome

**AUTHOR-PROVED PROPER-CLASS THEOREM; INDEPENDENT REVIEW PENDING.**

The prior B12 run paid the complete tensor obstruction only for one explicit
outer pair whose influence grew linearly with tensor depth.  This run removes
that influence-density hypothesis completely.

For arbitrary Boolean endpoints `u,v`, an arbitrary Boolean selector `h` on a
fresh disjoint block, and

\[
 F=u\ \text{on }h=-1,\qquad F=v\ \text{on }h=+1,
\]

let `r=Pr[h=+1]<=1/2`, `delta=4r(1-r)`, and
`beta=Pr[u!=v]`.  The exact sector decomposition gives

\[
 H(F)\le(1-r)H(u)+rH(v)+\beta H(h)
       +2\delta h_2(\beta)+8\beta h_2(r).
\]

Together with edge isoperimetry and the exact identity

\[
 I(F)=(1-r)I(u)+rI(v)+\beta I(h),
\]

this proves: whenever `u,v,h` each obey FEI with the same constant `C`,

\[
 \boxed{H(F)\le(C+8)I(F).}
\]

The additive tax is independent of dimension, bias, endpoint disagreement,
support size, endpoint influence density, and correlation gap.

## Mathematical movement

- **Previous class:** one tensorized endpoint pair plus a point-defect
  selector, with a direct support-count payment and a positive linear outer
  influence density.
- **New class:** every ordered Boolean endpoint pair and every Boolean selector
  on fresh disjoint physical blocks.
- **Previous bound:** `H(F_k)<=(1728/595)I(F_k)` only on the complete tensor
  no-go family.
- **New bound:** universal one-node closure `C -> C+8`, with no parameter
  dependence and no endpoint width term.
- **Mechanism:** the coefficient identity
  `(qu_T+rv_T)^2+4qr((v_T-u_T)/2)^2=qu_T^2+rv_T^2`, followed by a coherent
  Jensen--Shannon/Holevo bound and product-entropy payment.

This is a real extension beyond finite numerical survival: the proof is
all-dimensional and analytic.  It also handles low-influence outer functions
and dummy-coordinate padding, which the preceding support argument could not.

## Controls

`CHECK.py` exhaustively checked 76,176 genuine Boolean triples (all endpoint
pairs through two variables against all selectors through three variables),
plus 20,000 deterministic pseudorandom triples through four variables per
block.  It verified the exact influence identity, sector chain rule bounds,
coherent-mixture bound, scalar product inequality, isoperimetric payments, and
the final `C+8` theorem.  The minimum observed sector slack was zero and the
largest observed additive tax ratio was `2`, below the proved `8`.

Finite controls are corroborative only; the theorem is proved in `PROOF.md`.

## Exact remaining gap

Full FEI remains **OPEN**.  Naive recursion of the theorem costs `8` per
composition depth.  For a changing adaptive hierarchy one must telescope the
explicit local reserves

\[
 2\delta_v h_2(\beta_v)+8\beta_vh_2(r_v)
\]

with one source-influence/terminal-reserve budget, and then handle overlapping
physical variables.  This directly mirrors the changing reverse-collision
reserve in A057; the present theorem identifies a bounded, Boolean-realizable
replacement reserve but does not yet prove its one-use sum.

## Review and source pins

No independent review of this theorem was observed.  Requested reviewers are
A091, A090, and A094.

- owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- fixed-source coherent-kernel theorem and changing-reserve obstruction,
  `e4cddfa3e7e6895ac94a069abeaa9d894671ce92`;
- independently accepted child-only tensor no-go,
  `88270c6634d96ee594a03845900a2445b019294a`;
- preceding joint tensor payment,
  `701e4eeea065b39e98667b0fe8a0be19a89e12ff`;
- concurrent positive point-defect GU transfer inspected,
  `a5c11c83a81621b9479b3b196df600f0870b0210`.

No literature-priority or full-FEI claim is made.
