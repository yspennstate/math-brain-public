# Round 449 current branch obligations after coverage split

Round 449 summarizes the state after the corrections in Rounds 438--448.

The spread-return branch now has a cleaner deterministic reduction:
\[
  \mathcal X^{\rm spr}_{j,K,p}
  \subseteq
  \mathcal X^{\rm rootdisj}_{j,\kappa,p}
  \cup
  \mathcal X^{\rm cov}_{j,K,\kappa,p}.
\]

The many-root branch has at least \(\kappa L_H\) pairwise time-disjoint root
return intervals.  Its remaining target is analytic:

1. delete the root intervals;
2. express reinsertion through the corrected \(Q\)-weighted annular transfer
   kernels \(A_{Q,u,\le L}^x\);
3. control the resulting endpoint weights by Schur, \(L^2\), or subset-cut
   estimates;
4. beat the residual density entropy at density \(\kappa\).

The few-root coverage branch has fewer than \(\kappa L_H\) root intervals
covering more than \(\delta L_H\) slab levels.  Its deterministic advantage is
that radial level choices have interval-cover entropy
\[
  \beta H(2\kappa/\beta)L_H+o(L_H),
\]
and deletion to same-sphere jump skeletons gives net defect gain at least
\[
  (2\delta-\kappa)L_H+O(1).
\]
The honest cost condition is therefore
\[
  \beta H(2\kappa/\beta)<(2\delta-\kappa)|\log Q|.
\]

However, Round 448 shows that this does not control vertex endpoints.  The
few-root branch also needs annular transfer/cut estimates, but for fewer,
longer intervals and with the radial coverage entropy already paid.

Thus the problem has not been solved.  The real current target is a unified
annular cut-energy estimate strong enough for:

* linearly many root intervals at density \(\kappa\); and
* fewer than \(\kappa L_H\) root intervals whose total radial coverage is at
  least \(\delta L_H\).

Failure of such an estimate should produce a concrete inverse object:
boundary subsets \(U,V\) in ball spheres with anomalously large truncated
exterior \(Q\)-weighted SAW energy.
