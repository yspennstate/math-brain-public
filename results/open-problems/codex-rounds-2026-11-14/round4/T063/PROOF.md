# Two flux constraints and simultaneous torus limits

Fix six-vertex weights a=b=1 and c>0. All logarithms are natural. At a vertex write (r,s,b,t) for the left, right, bottom and top edge directions, with 1 meaning right or up. The allowed labels satisfy

\[
r+b=s+t.
\tag{1}
\]

Give the two labels with r unequal to s weight c, and the other four labels weight 1. Adjacent labels agree on their shared edge. Let X be the resulting compact space of allowed configurations on the plane. For a translation-invariant probability measure \(\nu\) on X, put

\[
\mathcal P_c(\nu)=h(\nu)+\mathbb E_\nu\log w_0,
\qquad
p_c=\sup_\nu\mathcal P_c(\nu),
\tag{2}
\]

where h is the entropy per vertex of the six-letter vertex process. The all-right, all-up configuration has pressure zero, so

\[
0\le p_c\le\log 6+\max(0,\log c)<\infty.
\tag{3}
\]

On the labelled N-column, L-row torus, let \(Z(N,L;n,m)\) be the partition function with exactly n right arrows on every vertical cut and m up arrows on every horizontal cut. Both counts are conserved by (1). Let \(\pi_{N,L;n,m}\) be its Gibbs law, extended periodically to the plane.

**Theorem.** Define

\[
H=2\min(n,L-n),\qquad W=2\min(m,N-m).
\tag{4}
\]

If W,H are at least 2, the sector is nonempty and

\[
\boxed{\log Z(N,L;n,m)\ge WHp_c-3(W+H)\log 2.}
\tag{5}
\]

Suppose \(N_j,L_j\to\infty\), \(n_j/L_j\to1/2\), and \(m_j/N_j\to1/2\). There is no restriction on \(N_j/L_j\). Then

\[
\frac{\log Z(N_j,L_j;n_j,m_j)}{N_jL_j}\longrightarrow p_c.
\tag{6}
\]

Every local subsequential limit of these laws is a translation-invariant, zero-slope gradient Gibbs measure with \(\mathcal P_c=p_c\). In particular, it minimises specific free energy among all translation-invariant allowed arrow laws. If that minimiser is unique, the whole sequence converges locally to it.

## 1. A finite-rectangle entropy bound

For a rectangle R, let \(H_\nu(R)\) be the Shannon entropy of its vertex labels. The six-letter alphabet and subadditivity give

\[
h(\nu)=\lim_{k\to\infty}\frac{H_\nu([0,k)^2)}{k^2}
=\inf_{a,b\ge1}\frac{H_\nu([0,a)\times[0,b))}{ab}.
\tag{7}
\]

Here is a direct justification. Tile a large square of side k by a-by-b rectangles, leaving at most O((a+b)k) uncovered vertices. Subadditivity and translation invariance bound its entropy by the number of tiles times the entropy of one rectangle, plus the number of uncovered vertices times log 6. After division by k squared, this bounds the limsup by every rectangle entropy density. Taking square tiles shows that the limsup is at most the infimum of the square densities. The liminf is at least this infimum by definition. The limit therefore exists; it is bounded above by every rectangle density, and its defining square sequence gives the reverse inequality needed for (7).

Let \(Z_{\mathrm{free}}(A,B)\) sum weights of all fillings of an A-column, B-row rectangle, including boundary arrows. The finite marginal of any allowed law is supported on these fillings. Nonnegativity of its relative entropy with respect to the finite Gibbs law gives

\[
H_\nu(R)+AB\,\mathbb E_\nu\log w_0
\le\log Z_{\mathrm{free}}(A,B).
\]

Using (7) and taking the supremum over \(\nu\) yields

\[
ABp_c\le\log Z_{\mathrm{free}}(A,B)
\quad\text{for every }A,B\ge1.
\tag{8}
\]

## 2. Four rectangles balance both fluxes

This section re-establishes the earlier reflection inequality with both fluxes recorded. For a boundary assignment \(\beta\), let \(Z_\beta\) be the rectangular partition sum. There are at most \(K=2^{2A+2B}\) boundary assignments and

\[
Z_{\mathrm{free}}(A,B)=\sum_\beta Z_\beta.
\]

Reflection in a vertical axis followed by reversal of all arrows, denoted \(F_x\), transforms a vertex to

\[
(r,s,b,t)\mapsto(s,r,1-b,1-t).
\]

Reflection in a horizontal axis followed by reversal of all arrows, denoted \(F_y\), transforms it to

\[
(r,s,b,t)\mapsto(1-r,1-s,t,b).
\]

Coordinates are reflected as well. Both transformations preserve (1) and the weight, and they commute.

Take four independent fillings U,V,Q,S with the same boundary assignment \(\beta\). Form the array

\[
\begin{matrix}
F_y(Q)&F_yF_x(S)\\
U&F_x(V).
\end{matrix}
\tag{9}
\]

At the lower vertical internal seam both lists are the right boundary of \(\beta\). At the left horizontal internal seam both lists are its top boundary. Applying \(F_y\) to the first seam and \(F_x\) to the second verifies the other two internal seams. The left and right outer edges agree: in the lower half they are copies of the left boundary of \(\beta\), and in the upper half they have the identical \(F_y\) transformation. The bottom and top outer edges agree by the corresponding statement for the bottom boundary and \(F_x\). Thus identifying outer edges gives a labelled 2A-by-2B torus.

On its outer vertical cut, the upper list of horizontal arrows is the complemented reverse of the lower list. Its right-arrow count is B. On the outer horizontal cut, the right list of vertical arrows is the complemented reverse of the left list. Its up-arrow count is A. Summing (1) over a full column or row shows that these flux counts hold on every corresponding cut.

The construction is injective: cut at the prescribed block boundaries and undo the reflections to recover the four fillings and \(\beta\). The image weight is the product of the four input weights. Therefore

\[
Z(2A,2B;B,A)\ge\sum_\beta Z_\beta^4
\ge K^{-3}Z_{\mathrm{free}}(A,B)^4.
\tag{10}
\]

The second inequality is Holder's inequality, \((\sum z_i)^4\le K^3\sum z_i^4\). Combining (8) and (10), and writing W=2A, H=2B, gives

\[
\log Z(W,H;H/2,W/2)
\ge WHp_c-3(W+H)\log 2.
\tag{11}
\]

For an independent check of the coefficient: \(3\log K=6(A+B)\log2=3(W+H)\log2\). Applying Cauchy-Schwarz twice, first to \(\sum z_i\) and then to \(\sum z_i^2\), also gives the exponent three in (10).

## 3. Insert rows and columns

Start with any torus in the sector of (11), with W,H as in (4). Its horizontal flux is H/2 and its vertical flux is W/2.

First insert L-H rows at a prescribed horizontal seam. If \(n\le L/2\), then H=2n; give every new horizontal arrow direction 0. If \(n\ge L/2\), then H=2(L-n); give every new horizontal arrow direction 1. When \(n=L/2\) there are no inserted rows, so either convention gives the same result.

For each column, extend its original vertical seam arrow straight through the new rows. Every inserted vertex has r=s and b=t and hence weight 1. The horizontal flux is

\[
H/2+0\,(L-H)=n\quad(n\le L/2),
\]

or

\[
H/2+(L-H)=L-H/2=n\quad(n\ge L/2).
\]

Every newly introduced horizontal cut has the same up-arrow count as the original seam, namely W/2; thus the vertical flux is unchanged.

Next insert N-W columns at a prescribed vertical seam. Give every vertical arrow in these columns direction 0 if \(m\le N/2\), and direction 1 if \(m\ge N/2\). Extend each horizontal seam arrow straight across the new columns. Every new vertex again has r=s and b=t, so it is allowed and has weight 1, including where the inserted rows meet the inserted columns.

The horizontal flux stays n: each new vertical cut copies the old seam list. The vertical flux becomes W/2 in the first case, and W/2+N-W in the second case. These are m, respectively because W=2m or W=2(N-m).

All original vertices retain their incident arrows. Deleting the prescribed inserted columns and then the prescribed inserted rows recovers the original labelled torus. This gives a weight-preserving injection, so

\[
Z(N,L;n,m)\ge Z(W,H;H/2,W/2).
\tag{12}
\]

The source sector is nonempty: for example choose horizontal direction constant along each of its rows with H/2 rows of each direction, and vertical direction constant along each column with W/2 columns of each direction. Then r=s and b=t everywhere. Equations (11) and (12) prove (5).

## 4. Entropy upper bound along a local limit

Write \(\pi_j=\pi_{N_j,L_j;n_j,m_j}\) and

\[
q_j=\frac{\log Z(N_j,L_j;n_j,m_j)}{N_jL_j},
\qquad e_j=\mathbb E_{\pi_j}\log w_0.
\]

The sector condition is invariant under all torus translations, so \(\pi_j\) is translation invariant. The finite Gibbs identity is

\[
q_j=\frac{H(\pi_j)}{N_jL_j}+e_j.
\tag{13}
\]

Here \(H(\pi_j)\) is the entropy of all vertex labels on the fundamental torus. Vertex labels determine all arrows, so this is also the entropy used in the Gibbs identity.

Fix k. When both dimensions exceed k, tile the fundamental rectangle by disjoint k-by-k squares. The uncovered remainder has size at most k(N_j+L_j). Subadditivity, translation invariance and the alphabet bound give

\[
q_j\le
\frac{H_{\pi_j}([0,k)^2)}{k^2}+e_j
+k\left(\frac1{N_j}+\frac1{L_j}\right)\log6.
\tag{14}
\]

The coefficient of the block entropy has been increased to \(1/k^2\), which is permissible because entropy is nonnegative.

Suppose a subsequence converges locally to \(\nu\). It is an allowed translation-invariant law: both properties are closed conditions on the product space. Entropy of a fixed finite marginal is continuous, since \(-x\log x\) is continuous at x=0 as well as elsewhere. The energy observable is bounded and local for fixed c>0. Passing to the limit in (14) and then taking k to infinity gives

\[
\limsup_j q_j\le h(\nu)+\mathbb E_\nu\log w_0
=\mathcal P_c(\nu)\le p_c.
\tag{15}
\]

## 5. Simultaneous limits

Put

\[
\alpha_j=\left|2n_j/L_j-1\right|,
\qquad\beta_j=\left|2m_j/N_j-1\right|.
\]

Then \(H_j/L_j=1-\alpha_j\) and \(W_j/N_j=1-\beta_j\). The finite bound gives

\[
q_j\ge(1-\alpha_j)(1-\beta_j)p_c
-\frac{3(W_j+H_j)\log2}{N_jL_j}.
\tag{16}
\]

Both \(\alpha_j,\beta_j\) tend to zero. Also

\[
\frac{W_j+H_j}{N_jL_j}\le\frac1{L_j}+\frac1{N_j}\longrightarrow0.
\]

Consequently \(\liminf q_j\ge p_c\). This uses only that both dimensions diverge, not an aspect ratio bound.

The space of probability laws on the finite-alphabet configuration space is compact for local convergence. If \(\limsup q_j>p_c\), choose a subsequence with \(q_j>p_c+\varepsilon\) for some positive \(\varepsilon\), and then choose a further locally convergent subsequence of \(\pi_j\). Equation (15) gives a contradiction. Thus (6) holds. For every locally convergent subsequence, equations (15) and (6) give

\[
p_c\le\mathcal P_c(\nu)\le p_c,
\]

which proves specific free-energy minimality.

The arrow means vanish in the limit. Indeed translation invariance on each finite torus gives right-arrow probability \(n_j/L_j\) and up-arrow probability \(m_j/N_j\) at each corresponding edge. These converge to 1/2. To see the height interpretation explicitly, put height on faces so that crossing a horizontal edge upwards gives increment \(2h_e-1\), and crossing a vertical edge rightwards gives increment \(1-2v_e\), where \(h_e,v_e\) are its direction bits. The sum around the dual square surrounding a vertex is \(2(r+b-s-t)=0\). Thus heights exist up to an additive constant, and both mean coordinate increments are zero under \(\nu\).

## 6. The local Gibbs rule survives the sector constraints

Fix a finite rectangle R of vertices. For sufficiently large N_j and L_j, it embeds without overlap in the torus and there exist a vertical cut and a horizontal cut disjoint from all arrows incident to R. Any replacement of the filling of R with the same boundary arrows leaves both those cuts unchanged. By flux conservation, it therefore leaves both sector labels unchanged.

Conditioning on the exterior arrows on the finite torus, the allowed fillings of R in the sector are consequently exactly the usual allowed fillings with the given boundary arrows. Their relative probabilities under \(\pi_j\) are their products of vertex weights. Denote this finite conditional kernel by \(\gamma_R\). It depends only on the finitely many boundary arrows, and its denominator is positive for every boundary arising from an allowed configuration. Thus, as a function on X, \(\gamma_R f\) is a bounded local continuous function whenever f is a bounded local function. Conditioning on the entire exterior of the periodically extended plane configuration is not used at finite j.

For any bounded local f and any bounded local g depending only on exterior arrows, the finite laws satisfy

\[
\mathbb E_{\pi_j}[gf]=\mathbb E_{\pi_j}[g\,\gamma_R f]
\]

once all supports embed without overlap. Local convergence passes this identity to \(\nu\). Taking f to be indicators of fillings in R and extending from exterior cylinder indicators g to all bounded exterior-measurable g by the monotone class theorem yields the Gibbs conditional law in R. Every finite region lies in a rectangle, so these rectangle identities imply the Gibbs rule on arbitrary finite regions as well. Under the height representation this is the gradient Gibbs property. No variational principle from the literature is needed for this conclusion.

Finally, if the translation-invariant pressure maximiser is unique, every local subsequential limit equals it. Compactness then gives convergence of the full sequence. This conclusion is conditional on uniqueness; neither zero mean slope nor pressure maximality alone establishes it.

## 7. The original single-flux ensemble

Let

\[
Z^{(1)}(N,L;n)=\sum_{m=0}^N Z(N,L;n,m),
\]

and let \(\pi^{(1)}_{N,L;n}\) be its Gibbs law. This is exactly the ensemble of the earlier cylinder theorem before taking its inner limit. Set \(W_N=2\lfloor N/2\rfloor\), and keep \(H=2\min(n,L-n)\). For N,H at least 2, selecting the single term \(m=\lfloor N/2\rfloor\) in this sum and applying (5) gives

\[
\log Z^{(1)}(N,L;n)\ge W_N H p_c-3(W_N+H)\log2.
\tag{17}
\]

If N,L tend to infinity and n/L tends to 1/2, then \(W_N/N\to1\) and H/L tends to 1. Thus (17) gives the same lower pressure limit \(p_c\). The entropy proof in Sections 4–5 applies to this translation-invariant finite Gibbs ensemble verbatim, because (13) holds for any restricted finite Gibbs law. Therefore

\[
\frac{\log Z^{(1)}(N,L;n)}{NL}\longrightarrow p_c,
\]

and every local subsequential limit maximises (2). The local Gibbs proof in Section 6 also applies: a bounded replacement preserves the one prescribed flux.

These limits have zero mean slope as well. The horizontal mean bit is n/L. For the vertical mean bit, the map \(F_x\) preserves the single horizontal-flux sector and all weights, while it complements vertical arrows. Translation invariance together with this symmetry makes their mean bit exactly 1/2 on every finite torus. The height increments defined in Section 5 thus have zero mean in the limit.

This proves the earlier free-energy conclusion for arbitrary simultaneous N,L limits, without an inner infinite-cylinder limit. As before, uniqueness of the maximiser would imply convergence of the entire sequence, but is not proved here.

## Scope and checks

The preceding argument extends the earlier cylinder theorem to simultaneous torus limits with one or both fluxes specified. It applies to every fixed c>0, including c>2, and makes no assertion of uniqueness or Gaussian fluctuations. Extreme sectors with W=0 or H=0 are excluded from (5); a near-balanced sequence eventually avoids them. Odd target dimensions cause no problem because the balanced source has even dimensions and the inserted strips can have arbitrary integer widths.

`check_two_flux.py` independently enumerates torus edge assignments and exact partition polynomials. It reproduces all 348 small gluing images from the earlier proof with both fluxes verified, checks 2296 insertion images including their explicit left inverses, and makes 60 coefficientwise partition comparisons. Six small shapes are also enumerated by an independent all-edge search. These finite checks verify conventions and small cases; the proof above establishes arbitrary sizes and every positive c.
