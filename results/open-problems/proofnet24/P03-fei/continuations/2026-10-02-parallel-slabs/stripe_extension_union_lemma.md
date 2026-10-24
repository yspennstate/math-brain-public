# Spectral entropy for finite disjoint unions with additive boundary

Date: 2026-10-02. **Candidate lemma; independent audit requested.**

This is an elementary entropy inequality. Together with the candidate
parallel-slab theorem in `stripe_extension_parallel_slabs_candidate.md`, it
extends FEI to unions of finitely many parallel intervals/rays separated
by gaps wider than twice the largest input weight. Positive component
widths are unrestricted. It does not settle arbitrary finite crossings.

All logarithms are base 2. Set \(e(t)=t\log_2(1/t)\), with \(e(0)=0\),
and \(L_e=\log_2e\).

## Entropy inequality for a disjoint union

Let \(E_1,\ldots,E_r\) be pairwise disjoint subsets of a uniform cube.
Define Boolean functions
\[
 g_j=1-2\mathbbm1_{E_j},\qquad
 f=1-2\mathbbm1_{\cup_jE_j}.
\]
Then
\[
 \boxed{H(f)\le r\sum_{j=1}^rH(g_j)
       +L_e(1+1/e)\sum_{j=1}^r\operatorname{Var}(g_j).}\tag{1}
\]

Proof. For a nonempty Fourier set \(S\),
\(\widehat f(S)=\sum_j\widehat g_j(S)\). Put
\[
 a=\widehat f(S)^2\in[0,1],\quad
 b_j=\widehat g_j(S)^2\in[0,1],\quad u=\sum_jb_j.
\]
Cauchy–Schwarz gives \(a\le r u\). We claim
\[
 e(a)\le r\sum_j e(b_j)+(L_e/e)u.\tag{2}
\]
If \(u=0\), the claim is immediate. If \(0<u\le1\), write \(a=t u\)
with \(0\le t\le r\). Then
\[
 e(a)=t e(u)-u t\log_2t
 \le r e(u)+(L_e/e)u
 \le r\sum_j e(b_j)+(L_e/e)u.
\]
The penultimate inequality uses \(e(u)\ge0\), and
\(\sup_{t>0}[-t\ln t]=1/e\). The last uses \(u\ge b_j\), since
\(u\log_2(1/u)=\sum_jb_j\log_2(1/u)\le\sum_j e(b_j)\).
If \(u>1\), simply \(e(a)\le L_e/e\le(L_e/e)u\), while all
\(e(b_j)\) are nonnegative. This proves (2).

Summing (2) over nonempty \(S\) gives
\[
 \sum_{S\ne\varnothing} e(\widehat f(S)^2)
 \le r\sum_j H(g_j)+(L_e/e)\sum_j\operatorname{Var}(g_j).
\tag{3}
\]
The empty-set term is at most \(L_e\operatorname{Var}(f)\), because
\(-(1-v)\ln(1-v)\le v\). Write \(p_j=\Pr(E_j)\) and
\(p=\sum_jp_j\le1\). Disjointness gives
\[
 \operatorname{Var}(f)=4p(1-p)
 \le4\sum_jp_j(1-p_j)=\sum_j\operatorname{Var}(g_j),
\]
since \(p^2\ge\sum_jp_j^2\). Combining this with (3) proves (1).
The estimate allows \(p>1/2\); no minority-label convention is needed.

## Exact influence additivity when components have no joining cube edge

Assume no edge of the cube joins \(E_j\) to \(E_\ell\) for distinct
\(j,\ell\). Then
\[
 I(f)=\sum_j I(g_j).\tag{4}
\]
Indeed, an edge either has both endpoints outside the union, both endpoints
in the same component, or one endpoint in exactly one component and the
other outside the union. In the last case it contributes exactly once to
both sides. There is no edge with both endpoints in different components.
This proves (4) coordinate by coordinate.

Consequently, if each \(g_j\) satisfies FEI with the same constant \(C\),
then by (1), (4), and \(\operatorname{Var}(g_j)\le I(g_j)\),
\[
 \boxed{H(f)\le\bigl(rC+L_e(1+1/e)\bigr)I(f).}\tag{5}
\]

## Parallel intervals separated by wide gaps

Let \(E_j=\{x:\sum_iw_ix_i\in J_j\}\), with pairwise disjoint
ordered intervals/rays \(J_j\), and put \(w_{\max}=\max_i|w_i|\).
If every gap between successive \(J_j\) has width strictly greater than
\(2w_{\max}\), no cube edge can join distinct \(E_j\), because the
score changes by at most \(2w_{\max}\) along any edge. Arbitrary endpoint
conventions are allowed under this strict separation.

Each individual \(g_j\) is a parallel slab or a halfspace. Therefore the
parallel-slab theorem implies (5) with \(C=C_{\rm slab}\). This includes
bounded finite-crossing functions with arbitrarily narrow positive
intervals, provided their negative separating gaps are sufficiently wide.
Complementing the function gives the corresponding result with the two
labels exchanged. There is no assertion that either label must satisfy
the gap condition for an arbitrary finite-crossing function.

The no-joining-edge hypothesis is necessary for the stated influence
identity. In general a coordinate can jump over a narrow separating gap
and join two positive components, contributing two units to the component
boundaries and zero to the union boundary. Such cancellation can be very
large; it cannot be omitted from the proof.
