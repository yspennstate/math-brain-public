# Independent review of union and nonmonotone random-chain extensions

Date: 2026-10-02. Reviewer: the separate all-LTF/strong-LTF proof author.
These are internal mathematical checks, not novelty certification or
external peer review. The two draft authors are different from this reviewer.

Reviewed files:

* `stripe_extension_union_lemma.md`.
* `stripe_extension_almost_symmetric_candidate.md`.

Both arguments pass a complete analytic review as written.

## Disjoint-union entropy

For each nonempty Fourier subset, the union coefficient is the sum of its
component coefficients. With squared component masses \(b_j\), total
\(u\), and union mass \(a\), Cauchy–Schwarz gives \(a\le ru\).
The scalar inequality
\[
 a\log_2(1/a)\le r\sum_j b_j\log_2(1/b_j)
                         +(\log_2e/e)u
\]
is valid in every regime: for \(0<u\le1\) split out \(a/u\), while for
\(u>1\) use the global maximum \((\log_2e)/e\) of entropy of a single
probability. Every \(b_j\) and \(a\) lies in \([0,1]\), so the sign
conditions are correct even when \(u>1\).

Summing nonconstant coefficients produces the component variances. The
empty coefficient contributes at most \((\log_2e)V(f)\). Disjointness
gives \(V(f)\le\sum_jV(g_j)\), since union density is \(\sum_jp_j\).
Thus the full entropy inequality, including its zero coefficient, follows.

No-joining-edge influence additivity is exact, coordinate by coordinate.
The hypothesis forbids exactly the edges that would count twice in
component boundaries but zero times in the union boundary. Parallel score
components separated by gaps strictly greater than \(2w_{\max}\) satisfy
this condition, regardless of endpoints. Combined with the audited
parallel-slab theorem, the stated finite-union FEI constant is correct.

## Random maximal chains

A uniform coordinate permutation makes each chain vertex uniform within
its layer and each successive chain edge uniform within its layer edge
set. This proves both the comparator layer-marginal identity and the exact
average influence identity \(\mathbb EI(g_\Pi)=I(f)\), for arbitrary
Boolean functions. No monotonicity is used or needed.

The difference \(f-g_\Pi\) is supported on the exceptional layers.
For disconnected exceptional layers, the induced layer adjacency path is
a union of blocks, each of length at most \(k\). Its adjacency norm is
at most \(2\cos(\pi/(k+1))\). The cube edge coupling between normalized
layers is \(\sqrt{(r+1)(n-r)}\le(n+1)/2\), so the band lemma's norm and
large-dimension Dirichlet inequality transfer without any contiguity
assumption. The elementary squared-triangle estimate yields
\(\mathbb EI(f-g_\Pi)\le4I(f)\), which is enough for the written bound.

For small dimension, two independent chains have average comparator
disagreement equal to \(\mathbb E\delta_\Pi\), because every layer gives
\(2q_r(1-q_r)\). Although the comparators are not nested,
\(|\mathbb Eg_\Pi-\mathbb Eg_{\Pi'}|\le2D(\Pi,\Pi')\) is always true.
Using \(D^2\le D\) gives
\(\operatorname{Var}_\Pi(\mathbb Eg_\Pi)\le2\mathbb E\delta_\Pi\).
Consequently \(\mathbb E\operatorname{Var}(f-g_\Pi)\ge2\mathbb E\delta_\Pi\),
and Poincare supplies the required disagreement bound. This addresses the
specific place where the earlier monotone proof's equality cannot be reused.

Averaging the established entropy perturbation inequality and symmetric
FEI gives exactly the written \(25+64(k+1)^2\) constant. Zero exceptional
layers and dimension zero are correctly separated.

For bounded total L1 weight deviation \(A\), a crossing can affect only
centers in an interval of length \(2A\), with Hamming center spacing 2.
The bound \(\lfloor A\rfloor+1\) uses closed intervals and remains valid
with attained crossing points. The resulting
\(k\le m(\lfloor A\rfloor+1)\) finite-crossing corollary follows.

## Optional sharpening, not needed for the audited draft

Let \(P_{\rm sym}\) be orthogonal symmetrization over coordinate
permutations, and let \(\mathcal L\chi_S=|S|\chi_S\) be the cube number
operator. Both commute. Since \(\mathbb Eg_\Pi=P_{\rm sym}f\),
\[
 \mathbb EI(f-g_\Pi)
 =2I(f)-2\langle f,\mathcal LP_{\rm sym}f\rangle
 =2[I(f)-I(P_{\rm sym}f)]\le2I(f).
\]
Substituting this exact identity in both large- and small-dimension
arguments proves \(n\mathbb E\delta_\Pi\le(k+1)^2I(f)\), giving the
optional constant \(25+32(k+1)^2\). For a single exceptional layer,
the induced adjacency is exactly zero, so
\(I(f-g_\Pi)=2n\delta_\Pi\) and \(n\mathbb E\delta_\Pi\le I(f)\),
which gives \(H(f)\le57I(f)\). These improvements should be separately
audited before replacing the draft's simpler constant.
