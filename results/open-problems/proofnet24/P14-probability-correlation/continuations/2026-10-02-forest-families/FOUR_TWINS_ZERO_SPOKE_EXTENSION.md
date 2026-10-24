# Four-twin H2 formula with an arbitrary common neighborhood

This is a continuity corollary of `FOUR_TWINS_ARBITRARY_CORE_H2.md`.
Its theorem and original audit files are unchanged.

Allow a_v>=0 rather than requiring every a_v>0. Assume each component of H
contains at least one vertex with a_v>0. This is precisely the condition that
M=L_H+4diag(a) is positive definite, or equivalently that the graph obtained
by attaching the four terminals to their common weighted neighborhood is
connected. At least one a_v is positive, so d=sum a_v>0.

**Corollary.** The identical formulas H_0=H_1=0 and

\[
 H_2=\frac1{64}\sum_{u,v}a_u a_v
       (4d\operatorname{adj}(M)_{uv}-\det M)^2
\]

hold in this setting. Moreover H_2>0 exactly when at least two a_v are positive.
In that case the two marked matching edges are strictly negatively correlated
for sufficiently large common activity scale lambda.

**Proof.** Replace every a_v by a_v+epsilon, epsilon>0, leaving the core edge
conductances fixed. Every coefficient of the finite forest Rayleigh polynomial
is a polynomial in the conductances, including the a_v. The adjugate expression
is also a polynomial. Taking epsilon downward to zero in the already proved
coefficient identities proves all three displayed formulas.

Put Q=4diag(sqrt(a)) M^{-1}diag(sqrt(a)) and u=sqrt(a)/sqrt(d). The positive
definiteness of M implies that Q has rank equal to the number of positive a_v.
Also Qu=u because M*1=4a. The same Frobenius-norm derivation gives
H_2=d^2(det M)^2 ||Q-uu^T||_F^2/64. It is strictly positive if Q has rank at
least two. If its rank is one, Q=uu^T, since Qu=u, and H_2=0. In that case all
four terminals have only one common neighbor and the two marked edges are
independent: the two triangles meeting at that neighbor are separate graph
blocks, attached to the rest of the core only through that vertex.

Thus the four terminals may have any identical common neighborhood, with
arbitrary nonnegative common spoke conductances. Complete adjacency to every
core vertex is not required.

## Unbounded bipartite corollary

Take G=K_{m,s}+{e,f}, where m>=4, s>=2, and e,f are two disjoint matching edges
within the m-side. All original bipartite edge conductances are one. Treat the
m-4 unmarked vertices of that side as additional core vertices. Thus the core
is H=K_{m-4,s}, the s hubs have a_v=1, and the m-4 extra terminals have a_v=0.
The four marked endpoints have the required common neighborhood.

Put k=m-4. In the order hubs followed by extra terminals,

\[
 M=\begin{pmatrix}mI_s&-J_{s,k}\\-J_{k,s}&sI_k\end{pmatrix},\qquad
 \det M=4m^{s-1}s^k,\qquad d=s.
\]

On the s supported vertices, Q has eigenvalue one on the constant vector and
4/m on its (s-1)-dimensional orthogonal complement; its other k eigenvalues
are zero. Consequently

\[
 \boxed{H_2=4(s-1)s^{2m-6}m^{2s-4}>0.}
\]

The Rayleigh polynomial's leading surviving degree is 2(m+s)-6. This corollary
has no bound on m or s. It concerns the added matching pair, rather than the
three actual bipartite edge-pair types, so it does not replace or extend the
all-fugacity bounded-width theorem about edges of K_{m,s} itself.

## Exact checks

`twin_core_zero_spoke_audit.py` imports the independent full-partition audit
and exercises four cases with zero spoke activities: connected path cores,
unequal weights, two disconnected anchored core components, and the bipartite
core K_{2,3}. Every complete Rayleigh polynomial has H_0=H_1=0 and its H_2
matches both the rooted-component moment formula and the adjugate sum of
squares exactly. The K_{2,3} case corresponds to m=6,s=3 and gives
H_2=209952, agreeing with the displayed bipartite formula. Results are in
`twin_core_zero_spoke_audit_results.json`.

As before, this is a restricted theorem, not a proof of Kahn's general forest
conjecture; mathematical novelty remains unconfirmed.
