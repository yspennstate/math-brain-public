# B20 / A097 — degree-three localization of the GU row cut

**Status:** a strict all-dimensional domain reduction is proved. Universal GU
and full FEI remain **OPEN**; this run is not an independent end-to-end review.

## Frozen candidate

- Candidate: \(G(f)\le4I(f)+3U(f)/4\) for every genuine Boolean function on
  every finite uniform cube.
- Stable gap: `G-GU-SIGNED-KL`.
- Claim: `B20-A097-DEGREE-THREE-CUT-v1`.
- Prior bound:
  \[
  G\le D_{\ge2}+\tfrac12V_1+(2/\ln2)I.
  \]
- Prior open leaf: the corresponding GU-cut on tensor-prime
  positive-residual Boolean sources.

## Result

The complete Fourier-degree-at-most-two class is removed from that open leaf.
The B11 theorem gives \(G\le2I\) for this class in every dimension.  Therefore

\[
R_{4,3/4}=G-4I-\tfrac34U
\le-2I-\tfrac34U<0
\]

for every nonconstant member, while constants have zero residual.  Combined
with source-pinned tensor additivity, any positive-residual counterexample has
a tensor-prime positive-residual factor of Fourier degree at least three.

Hence it now suffices to prove only

\[
\boxed{D_{\ge2}+\tfrac12V_1\le
\left(4-\frac2{\ln2}\right)I+\tfrac34U}
\]

for tensor-prime positive-residual genuine Boolean functions of Fourier degree
at least three.  This implication is dimension-free and preserves the signed
term, every order-at-least-two KL row, the singleton reuse cost, normalization,
terminal conventions and influence accounting.

If this sole leaf is proved, the source row-cut yields universal
\(G\le4I+3U/4\).  The audited induction gives \(U\le16I\), and the verified
\(H\le2I+2U\) reduction gives \(H\le34I\).

This is a strict domain reduction, not a smaller numerical coefficient.  No
claim is made that a merely nonzero level-at-least-three mass supplies enough
payment.

## Source-bound reconciliation

The local B20 checkout ended at an older residual-compensation run.  This run
uses the newer canonical row-cut original, not the stale local report.  The
new B11 degree-two bundle was read from its complete producer files and had
9/9 canonical-to-mirror blob matches; no producer identity or review status
was changed.  The governing alignment receipt records that historical
B02/B08/B13 response statements were recovered but their unavailable original
proof/checker bytes were not invented.  Newer B06 source plus B18 review and
newer B20 row-cut evidence supersede earlier stale-output observations.

## Verification and next action

`verify_degree_three_cut.py` checks the exact residual arithmetic and the
derived constants.  The full derivation and obligation map are in
`DEGREE_THREE_ROW_CUT.md` and `DEPENDENCY_MAP.json`.

Next prove a quantitative degree-at-least-three lemma: use the first nonzero
high-degree mass together with the minimal-child residual inequalities to
absorb \(V_1/2\), without discarding \(\sum_i(B_i-\Gamma_i)\).

Model/effort metadata: `UNKNOWN`.

