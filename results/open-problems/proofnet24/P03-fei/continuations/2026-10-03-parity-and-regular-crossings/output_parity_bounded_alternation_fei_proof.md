# Output parity and bounded alternation on ascending paths

Date: 2026-10-02. **Complete derivation; independent audit pending.** This
is a separate corollary of the internally audited
[bounded ascending-path support theorem](bounded_ascending_path_support_fei_proof.md).
It leaves that proof unchanged. No historical-priority or novelty claim
is certified, and full Boolean FEI remains open.

## Statement

Let \(g:\{-1,1\}^n\to\{-1,1\}\). Suppose that, on **every ascending
cube path**, the values of \(g\) change sign on at most \(m\) edges,
where \(m\ge0\) is an integer. An ascending edge changes one coordinate
from \(-1\) to \(+1\). Paths can start and end at arbitrary vertices;
they need not be maximal. Choose any \(T\subseteq[n]\), and put
\[
 h(x)=\chi_T(x)g(x),\qquad q=n-|T|.
\]
With base-two Fourier entropy and physical flip influence,
\[
 \boxed{H(h)=H(g)\le
 4\cot^2\!\left(\frac{\pi}{2(m+q+2)}\right)I(h).}
\tag{1}
\]
The exact influence on the right is
\[
 \boxed{I(h)=|T|+I(g)-2\sum_{i\in T}I_i(g).}
\tag{2}
\]
Only for \(T=[n]\) does this specialize to \(I(h)=n-I(g)\).
In particular, full output parity gives
\[
 H(g)\le4\cot^2\!\left(\frac{\pi}{2(m+2)}\right)[n-I(g)].
\tag{3}
\]
These inequalities are FEI statements for \(h\). They do not assert
an ordinary influence bound \(H(g)\le C_m I(g)\) for the original
bounded-alternation function. For example, the latter would include
general monotone Boolean functions when \(m=1\), an unresolved case.

Dimension zero and constant \(h\) have zero entropy and satisfy (1)
directly. If \(m=0\), every vertex can be reached from the bottom
vertex by an ascending path, so \(g\) is constant. Then \(h\) is a
parity function up to a global sign, and its entropy is zero.

## Constant-output path counting

Consider an ascending path on which \(h\) is constant, with \(j\)
edges. Every coordinate is flipped at most once on that path. Write
\(j_T\) for its number of edges whose coordinate lies in \(T\), and
\(j_{\bar T}\) for the other edges.

On a \(T\)-edge, \(\chi_T\) changes sign. Since \(h=\chi_Tg\)
does not change there, \(g\) must change sign. On a non-\(T\) edge,
\(\chi_T\) does not change; constancy of \(h\) requires that \(g\)
also does not change. Thus **the number of sign changes of \(g\) on
this entire path is exactly \(j_T\)**. The hypothesis gives
\(j_T\le m\), and distinctness of the flipped coordinates gives
\(j_{\bar T}\le q\). Consequently
\[
 j\le m+q.
\]
The path has \(j+1\le m+q+1\) vertices. This argument applies to
each label class of \(h\), including paths starting or ending inside
the cube. There is no assumption that such paths use every coordinate.

Apply the bounded-support theorem with
\(k=m+q+1\). Its constant is
\(4\cot^2(\pi/[2(k+1)])\), exactly the constant in (1).

## Fourier and influence identities

Walsh multiplication by parity translates Fourier indices:
\[
 \widehat h(S)=\widehat g(S\mathbin\triangle T).
\]
This permutes the squared coefficient masses and proves \(H(h)=H(g)\).
For a coordinate \(i\notin T\), multiplying by \(\chi_T\) preserves
whether an \(i\)-edge is pivotal, so \(I_i(h)=I_i(g)\). For
\(i\in T\), it reverses that condition, so
\(I_i(h)=1-I_i(g)\). Summing these identities proves (2), with the
usual empty-set conventions. No assumption of monotonicity is needed
for either identity.

## Monotone scalar scores and endpoint conventions

Suppose first that \(w_i\ge0\), and
\(g(x)=F(\sum_iw_ix_i)\). Assume \(F\) is constant on the open
intervals between at most \(m\) distinct retained crossing points.
At each retained point its left and right labels are opposite, and the
point itself is assigned one of those two adjacent labels. Redundant
points at which there is no sign jump are omitted; isolated point
anomalies with equal adjacent labels are not being counted as one
crossing under this convention.

Along an ascending cube path, the score is nondecreasing. A retained
crossing can produce at most one sign change in the sequence of labels,
including when a score lands exactly at the crossing. Each nonconstant
step therefore crosses at least one as-yet-unpassed sign jump, and there
are at most \(m\) such jumps in total. Thus the path hypothesis holds
and (1) applies. This covers arbitrary spacings and biases of the
crossings, not only separated crossings or slabs.

If \(w_i=0\), the score, and hence \(g\), does not change on that
coordinate's edges. Such coordinates may be retained in the statement;
they are included in \(q\) if absent from \(T\), or contribute exactly
one each to \(I(h)\) if included in \(T\). For a sharper statement,
one may delete these irrelevant coordinates from \(g\) before choosing
\(T\) and applying (1). This deletion preserves \(H(g)\) and \(I(g)\),
but changing \(T\) can change \(h\); it is not a claim that a parity
coordinate can be deleted from an already specified \(h\).

For arbitrary signed weights, flip coordinates with negative weights.
The resulting score has nonnegative weights and the argument above
applies in the corresponding cube orientation. Coordinate sign flips
preserve entropy and every physical coordinate influence. They change
\(\chi_T\) only by a global sign after transforming variables, which
also preserves entropy and influence. Thus the same conclusion holds
for signed scores in this oriented sense. An arbitrary function's path
hypothesis must be checked in the chosen orientation; it is not invariant
under unspecified changes of order.

If one instead permits isolated point anomalies, their contribution to
the scalar variation must be counted correctly. An anomalous label with
equal left and right labels can cause **two** sign changes when the
path visits the point and then leaves it. Counting both in the total
variation gives a valid \(m\); simply counting anomalous locations as
one crossing does not justify (1).

## A sharper elementary bound for parity of unate functions

There is a stronger statement when \(g\) is unate. If \(|T|\ge2\),
then
\[
 \boxed{H(\chi_Tg)\le(q+2)I(\chi_Tg).}
\tag{4}
\]
For full parity this gives, in every dimension,
\[
 \boxed{H(\chi_{[n]}g)\le2I(\chi_{[n]}g),}
\tag{5}
\]
and the constant 2 is optimal. This elementary refinement is stated
without any novelty claim.

After coordinate sign flips, assume \(g\) is monotone increasing. For
each coordinate, conditioning on the other coordinates gives
\[
 I_i(g)=\mathbb E[g(X)X_i].
\]
Put \(t=|T|\), \(s=\sum_{i\in T}I_i(g)\), and
\(a=\sum_{i\notin T}I_i(g)\ge0\). Then
\[
 s=\mathbb E\left[g(X)\sum_{i\in T}X_i\right]
 \le M_t:=\mathbb E\left|\sum_{i=1}^tX_i\right|\le\sqrt t,
 \qquad I(h)=t-s+a\ge t-M_t.
\]
The entropy of any probability law on \(2^n\) Fourier indices is at
most \(n=t+q\). For \(t=2\), direct binomial calculation gives
\(M_2=1\), so \(H(h)/I(h)\le q+2\). For \(t=3\),
\(M_3=3/2\), so
\((q+3)/(3/2)\le q+2\). For \(t\ge4\),
\(t-\sqrt t\ge t/2\), and therefore
\[
 \frac{H(h)}{I(h)}\le\frac{t+q}{t/2}
 \le2+\frac q2\le q+2.
\]
This proves (4). Full parity with \(n\ge2\) has \(q=0\), proving
(5). When \(n=0\) or \(n=1\), every Boolean function has a single
nonzero Fourier coefficient and zero entropy, so (5) holds there too.
The coordinate flips used for unateness affect \(h\) only by relabeling
vertices and a global sign, so they preserve the statement.

For sharpness in (5), take in dimension two
\(g(x)=-1\) only at \((-1,-1)\), and \(g(x)=1\) at the other
three vertices. This is monotone; all four squared Fourier coefficients
equal \(1/4\), so \(H(g)=H(h)=2\). Also \(I(g)=1\), hence full
parity gives \(I(h)=2-I(g)=1\). Its ratio is exactly 2.

## Scope and verification

The general theorem supplies a dimension-independent FEI bound for
\(h\) whenever both \(m\) and the number \(q\) of missing parity
coordinates are bounded. The bounded-alternation hypothesis includes
arbitrary monotone functions for \(m=1\), whereas their full parity
outputs have the stronger optimal constant (5). For scalar scores it
also covers any fixed finite number of genuine crossings with arbitrary
spacing and the stated endpoint conventions.

This does not prove ordinary FEI for arbitrary-spacing three-crossing
score functions \(g\), or for all monotone functions. Equation (3)
controls the complementary influence \(n-I(g)\), not \(I(g)\).

The [author checker](verify_output_parity_bounded_alternation.py) and
[report](output_parity_bounded_alternation_checks.json) cover every one
of the 65,814 Boolean functions through dimension four and every parity
subset for each, plus 96 scalar-score functions through dimension twelve.
The total is 1,051,466 function/parity pairs. Path counts, integer Fourier
permutations, and influence identities are exact; entropy inequalities
use a numerical tolerance of \(3\cdot10^{-11}\). The scalar cases
include attained crossing points assigned either adjacent label,
24 cases with zero-weight coordinates, and 96 checks of coordinate
orientations. The optimal ratio 2 in (5) is verified exactly on the
displayed two-dimensional example.

Independent analytic audit is pending. Finite verification is
supplementary; historical priority, novelty, and external peer review
remain unverified. The sole theorem input for (1) is the linked
bounded-support proof, which fully credits the classical
Haagerup–de la Harpe operator inequality it uses.
