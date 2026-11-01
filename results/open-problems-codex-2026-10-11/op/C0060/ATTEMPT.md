# C0060: resolved in the literature

Date: 2026-10-11.

## Exact question and source hypotheses

Let S be the infinite discrete skeleton of the Sierpinski gasket and E = S × Z, with nearest-neighbor Cartesian product edges and natural unit conductances. For random interlacements at level u on E, let V^u be the vacant set and

u_* = inf {u ≥ 0 : P(V^u contains an infinite connected component) = 0}.

The question is whether u_* > 0. The preliminary book (30 December 2013), §10.3 p. 81, says exactly: “As an example, in the case of random interlacements on the graph G × Z, where G is the discrete skeleton of the Sierpinski gasket, it is still not known whether the corresponding parameter u_* is strictly positive”; it refers to Sznitman (2012), Remark 5.6(2). The natural conductances are confirmed in that remark. This is the infinite gasket, not a fixed finite gasket times Z.

## Published theorem and complete application

Use Drewitz–Prévost–Rodriguez, *Geometry of Gaussian free field sign clusters and random interlacements*, PTRF 192, 625–720 (2025), DOI 10.1007/s00440-024-01285-1; first online 2024; arXiv:1811.05970v3 (2024).

Their Theorem 1.2 assumes (p0), polynomial volume growth (V_alpha), two-sided Green function bounds (G_beta), and weak sectional isoperimetry (WSI). It states there exists a number tilde u > 0 such that for each 0 < u ≤ tilde u a coupling Q^u of random subsets I,V,K exists with:

1. I has the interlacement-set law at level u, and V has the vacant-set law at level u.
2. K is independent of I.
3. Almost surely, I intersect K contains an infinite connected component and I intersect K is a subset of V.

The graph E is explicitly their example G2 in (1.4). Corollary 3.9 asserts that every graph in (1.4), with unit conductances and a suitable distance, satisfies all four assumptions; it specifically proves this for G2 using Propositions 3.5 and 3.7. Thus Theorem 1.2 applies without an unverified geometric assumption.

Fix 0 < u ≤ tilde u. By property 3, an infinite connected component C of I intersect K is a connected subset of V almost surely. The connected component of V containing any vertex of C contains C and is therefore infinite. By property 1 the marginal distribution of V is exactly the law of V^u. Consequently P(V^u has an infinite connected component) = 1. This holds for every 0 < u ≤ tilde u. At u=0 the vacant set is the whole infinite connected graph. Hence no level u in [0,tilde u] lies in the defining zero-percolation set for u_*. Its infimum is at least tilde u (also if that defining set were empty). Therefore u_* ≥ tilde u > 0. This settles C0060 affirmatively. QED, invoking the published theorem and its verified example corollary.

## Hostile-referee checks

- Exact graph: (1.4) explicitly names the discrete Sierpinski gasket times Z, with unit weights. No substitution of a carpet or finite approximation is involved.
- Exact model: Theorem 1.2 concerns random-interlacement vacant sets, not merely Gaussian free field clusters.
- Every hypothesis: Corollary 3.9 includes (WSI); this essential condition is not inferred from transience alone.
- Parameter restriction: Sznitman (2012) required ν ≥ 1. The newer Theorem 1.2 has no such restriction, and explicitly discusses this gasket example immediately after its statement.
- Metric: the newer proof uses an anisotropic product metric. Corollary 3.9 gives alpha = log(45)/(2 log 2), beta = log(5)/log(2); the difference is log(9/5)/(2 log 2) > 0. The gasket factor's exponents are log(3)/log(2) and log(5)/log(2). These distinct uses of alpha must not be conflated. The earlier heuristic's isotropic capacity exponent is not a theorem used here.
- Meaning of coupling: although the auxiliary I has interlacement law, it need not be the actual complement of coupled V. The inference uses the theorem's explicit inclusion and correct marginal law only.
- Provenance: downloaded primary PDF explicitly says it resolves Sznitman's final Remark 5.6(2), which is precisely the book's reference.
- Bibliography: Crossref confirms journal volume 192, pages 625–720, print 2025, first online 15 June 2024. Distinguish these dates from the 2018 preprint.

No new proof of the deep theorem, simulation, or Lean verification is claimed. The user's status-first instruction requires ending once a published resolution is verified. The argument above is the full deduction of the requested result from the cited published theorem. There is no remaining gap in that application.
