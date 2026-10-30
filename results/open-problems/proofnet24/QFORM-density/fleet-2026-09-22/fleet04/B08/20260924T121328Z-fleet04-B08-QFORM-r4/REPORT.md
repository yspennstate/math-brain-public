# fleet04/B08 — bilateral bank-grid localization of the diffuse-carrier survivor

Run: \`20260924T121328Z-fleet04-B08-QFORM-r4\`

Status: **ESSENTIAL_STEP_APPLIED / NEW HYBRID REDUCTION / FULL QFORM OPEN**

The full universal three-eigenvalue density conjecture remains open, and continuity remains separate. All coordinate sets below are subsets of the original independent product coordinates. No independence after spectral rotation, moment hypothesis, support hypothesis, CLT, arbitrary-joint coarea bound, or conditional-density supremum is used.

## 1. Source-pinned state

The Claude source is
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md\`
at the current default branch, rooted at the required source commit
\`e5f71d79eff325201dd0274053d20268ce65b837\`, with the later Claude-review corrections retained.

The completed fleet01/B08 input used at an equation is
\`yspennstate/math-open-problems@93ac74d786812e147208df894a5cfed31b14b7fb\`.
Its r49 theorem supplies, in the only primitive edge-capped diffuse survivor, one literal crossing
\[
D=A[S\setminus\{k\},T]
\]
and four-bank partitions
\[
S\setminus\{k\}=H_1\sqcup H_2\sqcup H_3\sqcup H_4,\qquad
T=K_1\sqcup K_2\sqcup K_3\sqcup K_4
\]
such that at least three row banks and at least three column banks satisfy
\[
\|D[H_i,:]\|_F\ge \eta L,\qquad
\|D[:,K_j]\|_F\ge \eta L,
\tag{1}
\]
where
\[
\sigma=\frac12\sqrt{\frac{67}{800}}
       =0.14469796128487783\ldots,\qquad
\eta=\frac{\sigma}{8}
     =0.01808724516060973\ldots .
\tag{2}
\]
The same source gives
\[
s_2(D)\ge \sigma L.
\tag{3}
\]
If (3) fails, fleet01/B08 r48 instead yields the inductive exit
\[
\|p_Q\|_\infty\le \frac{C}{\sigma L}
=\sqrt{\frac{3200}{67}}\frac{C}{L}
<6.911\,\frac{C}{L}.
\tag{4}
\]
Thus (1)--(3) are the actual remaining primitive branch, not assumptions imposed on the original theorem.

## 2. New localized/diffuse grid theorem

### Theorem — \`QFORM-BILATERAL-FOURBYFOUR-GRID-MATCHING-v1\`

Under (1)--(3), there are two pairs
\[
(i_1,j_1),\ (i_2,j_2)\in\{1,2,3,4\}^2
\]
with \(i_1\ne i_2\) and \(j_1\ne j_2\) such that
\[
\boxed{\;
\|D[H_{i_r},K_{j_r}]\|_F
\ge \frac{\eta}{2}L
=0.009043622580304865\ldots\,L,
\quad r=1,2.
\;}
\tag{5}
\]

#### Proof

For every good column bank \(K_j\), the row banks partition all rows of \(D\), hence
\[
\sum_{i=1}^4\|D[H_i,K_j]\|_F^2
=\|D[:,K_j]\|_F^2
\ge \eta^2L^2.
\]
Therefore some \(i\) satisfies
\[
\|D[H_i,K_j]\|_F\ge \frac{\eta}{2}L.
\tag{6}
\]
Choose one such cell for each of the at least three good column banks. Symmetrically, for each of the at least three good row banks choose a column \(j\) for which (6) holds.

Form the bipartite graph whose row vertices are \(H_1,\ldots,H_4\), whose column vertices are \(K_1,\ldots,K_4\), and whose selected edges are these cells. The graph meets at least three distinct row vertices and at least three distinct column vertices. If it had matching number one, every two selected edges would intersect; a bipartite graph with pairwise-intersecting edges is a star, so all selected edges would share one vertex. That is impossible because the selected edges meet at least three vertices on both sides. Hence the graph has a matching of size at least two, giving (5). \(\square\)

This is an original-coordinate localized certificate extracted from the diffuse carrier. The two blocks in (5) use disjoint source variables on both sides.

## 3. Volume and ridge certificates on the same matrix

The same surviving matrix \(D\) now simultaneously carries:

1. the order-two volume certificate
\[
\boxed{\;
e_2(D^TD)^{1/4}\ge
\sqrt{s_1(D)s_2(D)}
\ge \sigma L;
\;}
\tag{7}
\]

2. six bank-ridge certificates from (1), each at scale
\[
\boxed{\eta L=\frac{\sigma}{8}L;}
\tag{8}
\]

3. the two disjoint localized cell certificates (5), each at scale
\[
\boxed{\frac{\eta}{2}L=\frac{\sigma}{16}L.}
\tag{9}
\]

Equation (7) is exact because
\[
e_2(D^TD)=\sum_{a<b}s_a(D)^2s_b(D)^2
\ge s_1(D)^2s_2(D)^2.
\]

This comparison also identifies the remaining analytic gap. Neither (7) nor (5) forces positive third compound:
\[
e_3(D^TD)
\]
may still vanish when \(D\) has rank two. Large Frobenius mass in two disjoint grid cells does not by itself prevent determinant cancellation through the other two cells of the corresponding \(2\times2\) bank rectangle. Thus the existing marginal-free third-compound density theorem cannot yet be invoked from (5) alone.

## 4. Exact next implication

The diffuse/localized hybrid is reduced to the following source-coordinate endpoint:

> A literal crossing \(D\) has \(s_2(D)\ge\sigma L\), order-two volume at scale \(\sigma L\), three row-bank and three column-bank ridge certificates at scale \(\sigma L/8\), and a size-two matching of disjoint bank cells at scale \(\sigma L/16\). Prove that either the target's retained same-bank curvature creates a fixed third compound, or one matched cell and that curvature form a physical finite-carrier/pair-completion receiver.

This is strictly narrower than the earlier six-bank carrier statement: the crossing energy has now been localized into two disjoint row-column packets. The remaining task must use the retained curvature or nonzero modulation; deleting the complementary coefficient tail, rotating the product law, or treating (7) as an order-three volume bound would be invalid.

## 5. Integrity

- Full universal density theorem: **OPEN**.
- Counterexample: **none produced**.
- Full-target continuity: **OPEN**.
- The inductive branch (4) is not called a stand-alone proof.
- The grid theorem is deterministic and sign-free.
- No scheduler, notification, repository visibility, or task-state mutation was made.
