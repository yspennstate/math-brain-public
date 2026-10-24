# B19 / A094 independent review — canonical bilinear-root GU theorem

**Target:** `B01-A003-CANONICAL-BILINEAR-ROOT-GU-v1`, local author run
`20261013T102835Z-account01-B01-canonical-bilinear-root-gu-a003`.  The
reviewed `REPORT.md` has SHA-256
`02c2db06ade333bfa8d76e1505ad177dbd38227c5a8e0539c69313cd52d7573f`;
the reviewed `PROOF.md` has SHA-256
`e76f85e21b16acb314fe287d837fa621ee7147abd125485be4d85d0920b5449a`.

**Verdict:** **ACCEPTED AT THE DECLARED CANONICAL ROOT SCOPE.**  The
apparently natural extension of the same `5/2` constant to arbitrary
invertible bilinear matrices is **REFUTED** by an exact three-bit witness.
Restriction closure and full FEI remain **OPEN**.

## Accepted statement

For every \(r\ge1\), all affine phases \(a,b,c\), and
\[
 P(x,y)=(-1)^{x\cdot y+a\cdot x+b\cdot y+c}
        (1-2\mathbf1_{\{y=0\}}),
\]
the normalization and physical-input calculation are
\[
 H(P)=2r,\qquad U(P)=I(P)=r,
\]
and the upper-set restriction charge satisfies
\[
 G(P):=\sum_i\left(U(P)-\mathbb E U(P|_{z_i})\right)
 \le \frac52 I(P).
\]
The same bound holds for finite disjoint products of these displayed roots.
The constant is independent of rank, affine phase, number of matched
centres, and number of disjoint blocks.

## Independent proof audit

The point defect changes only the Fourier layer \(\alpha=a\) by twice the
original coefficient magnitude, so it flips signs while leaving every
squared coefficient equal to \(2^{-2r}\).  This gives \(H=2r\) and \(U=r\)
with exact probability normalization.

Every physical \(x_i\) and \(y_i\) has influence \(1/2\).  On the exceptional
\(y_i\)-edge \(\{0,e_i\}\), the point defect reverses the pivotality
condition but does not change its count.  Hence \(I=r\).

Each \(y_i\)-restriction has mean child potential \(r-1\), giving charge
one.  Each \(x_i\)-restriction reduces to a uniform graph with exact charge
\[
 1+2^{-r}C_{r-1}(|a'|),
\]
where
\[
 C_d(h)=d-h-\sum_{j<h}{h\choose j}
 \log_2(1-2^{-(d-j)}).
\]
The source bound \(C_d(h)\le2^d\) is valid: the cases \(d\le3\) are direct,
and for \(d\ge4\), \(-\log_2(1-z)\le2z\) yields
\(C_d(h)\le d+2(3/2)^d\le2^d\).  Thus each \(x_i\) charge is at most
\(3/2\), proving \(G\le5I/2\).  Exact tensor factorization makes
\(U,H,I,G\) additive on disjoint products.  No proof repair was required.

## Independent verification and scope falsifier

`CHECK_REVIEW.py` was written without importing the author checker.  It
reconstructed exact rational Walsh squares, physical influences, all
one-coordinate children, and the closed charge formula for every affine
orientation through rank four; it also tested the scalar inequality for
every \(0\le d\le256\).  All 41,349 checks passed.  The largest enumerated
canonical ratio was
\[
 G/I=2.301879687409855
\]
at \(r=3,a=b=111_2\), below \(5/2\).

The same checker then tested an invertible non-monomial physical bilinear
form.  For \(r=3\), matrix rows \((111,101,011)_2\), \(a=111_2\), \(b=0\),
the squared spectrum is still uniform and \(I=3\), but exact rational
outward log intervals certify
\[
 G/I>2.709116536420773115549284>5/2,
\]
with \(G-5I/2>0.627349609262319346647853\).  Therefore the accepted theorem
must retain the matched physical form \(x\cdot y\); Fourier equivalence under
an invertible basis change is not enough because upper-set caps and physical
restriction charges are basis-sensitive.  This is a scope falsifier, not an
FEI counterexample.

## Primary-literature comparison

O'Donnell--Tan's composition theorem treats disjoint input blocks with a
biased outer hypothesis; it supports disjoint tensorization but does not
provide a shared-variable or arbitrary-basis transfer.  Potapov's 2026
plateaued-function theorem already covers the root's flat-spectrum FEI
endpoint, but not the upper-set restriction functional \(G\).  Thus no FEI
novelty claim is credited to the flat root; the accepted advancement is the
explicit canonical-root GU payment at all ranks.

## Movement and remaining gap

**Previous accepted nearby class:** the restriction-closed one-centre
partial-star/point-defect class had \(G\le14I\).

**New accepted class:** arbitrary-rank matched full bilinear roots and their
disjoint products satisfy \(G\le(5/2)I\).  This adds unboundedly many matched
bilinear centres at the root and improves the constant there.

**Still unpaid:** the root class is not restriction closed.  Repeated
\(x\)-restrictions create positive codimension and unequal exceptional-layer
masses.  The source's cap formula is an exact reduction, not a uniform
payment.  The next mathematical step is to evaluate the complete signed
coordinate charge from that formula and prove a constant uniform in rank and
codimension, or produce a genuine growing-ratio falsifier.  No universal
GU', \(U\le KI\), or full FEI conclusion follows.

## Source pins and routing

- Control revision `FULL-FEI-ONLY-20261012`, revision 2026-10-12.1,
  commit `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- O'Donnell--Tan, *A composition theorem for the Fourier
  Entropy-Influence conjecture*, arXiv:1304.1347.
- Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean
  Plateaued Functions*, arXiv:2609.21563, posted 2026-09-18.

Route the exact-scope acceptance and falsifier to B01, B05, B18, and B20.
