# Sidorenko research checkpoint: K5,5 minus C10

Date: 2026-10-02. Status: **No proof or counterexample found.**

The target H is the ten-vertex, fifteen-edge bipartite Möbius ladder, with
parts {i_0,...,i_4} and {j_0,...,j_4}, and edge i_a j_b when b-a is -1,0,1
modulo 5. The target inequality for a nonnegative symmetric graphon W is
t(H,W) >= (integral W)^15. This is a famous small unresolved case of
Sidorenko's conjecture, as recorded by Fox-Himwich-Mani-Zhou, EJC 32(3)
P3.38 (September 2025), and Benjamin Rossman's May 2025 preprint.

## Primary-source status

* https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/
  calls K5,5 minus C10 a notorious small open case (page two).
* https://users.cs.duke.edu/~br148/sidorenko-mobius.pdf is Rossman's *On
  Sidorenko's Conjecture for Bipartite Möbius Ladders*. The downloaded PDF and
  extracted text are in this directory. It identifies this target as the
  smallest open case and presents the transfer/spectral approach below.
* https://arxiv.org/abs/2606.15368 (Yuqi Zhao, June 2026) gives conjugacy
  averaging reductions and a 1-subdivision kernel result. It does not state a
  proof of the full conjecture or the Möbius-ladder case.
* Gaussian product inequalities are unsuitable as a fallback open target:
  https://arxiv.org/html/2609.20234v1 (Ouimet-Greaves, displayed submission
  July 2026) claims the full strong inequality for arbitrary positive
  exponents, with a detailed reciprocal-coordinate change-of-variables proof.

These sources give positive evidence for the Sidorenko target's open status,
but a bounded search cannot guarantee that every unpublished development has
been excluded.

## Transfer identity and precise spectral gap

For an n-state, uniform-measure symmetric host matrix W define

    M_(ij),(kl) = sqrt(W_ij W_kl) W_il W_kj.

Then t(H,W) = trace(M^5)/n^10. Rossman's Lemma 1.5 gives this exact identity
for all bipartite ladders. His Lemma 2.2 gives lambda_max(M) >= n^2(mean W)^3.
Thus trace(M^5) >= lambda_max(M)^5 would suffice for the target. The latter
inequality is not a general fact about entrywise nonnegative symmetric
matrices; negative eigenvalues must be controlled using the special product
structure of M. Rossman's Conjectures 3.2 and 4.2 propose pseudo-positive
spectra as one route. We have not proved those conjectures or the fifth-power
special case. The transfer reduction is already in this primary source and
must not be presented as new.

## Regular-host expansion

The general regular-host reduction is known. Normalize a regular host to
integral_y W(x,y)=1 and write U=W-1. Then integral_y U(x,y)=0 and U>=-1.
Expanding t(H,1+U), any selected-edge subgraph having a vertex of degree one
has integral zero. Since H is cubic, the remaining selected subgraphs have
degrees 0,2,3. Components containing only degree-two vertices are even cycles,
whose U-densities are nonnegative by the self-adjoint trace identity.

The operator identity U^k=W^k-1 follows from W1=1 and U1=0. Consequently
U^k(x,y)>=-1 for every positive integer k, because W is a positive Markov
kernel. It can control some odd cubic-core terms. For example, for the theta
graph with path lengths 1,3,3,

    t(theta_(1,3,3),U)
      = integral U(x,y) [U^3(x,y)]^2
      >= -integral [U^3(x,y)]^2
      = -t(C6,U).

The unresolved gap is how to control all terms whose cubic cores have four,
six, eight, or ten degree-three vertices, including the full H term, by the
available positive terms. No summation or domination argument has been found
that covers them. One cannot omit these terms or infer their signs from
cycle positivity.

## Rank-one perturbation enumeration

For W=1+x f tensor f, with integral f=0 and integral f^2=1, let
y=(integral f^3)^2. Every surviving selected subgraph with n2 vertices of
degree two and n3 of degree three contributes
x^(n2+3*n3/2) y^(n3/2). The exact degree counts over all 2^15 subsets are in
`rank1_degree_counts.json`. For x>=0 all surviving terms are nonnegative.
For x=-z, positivity gives 0<=z<=1 and
|integral f^3| <= z^(-1/2)-z^(1/2), so zy<=(1-z)^2. This suggests domination
of negative terms by the five C4 contributions. Such restricted-host results
are plausibly already covered by known two-state/log-supermodular methods;
we have not established novelty and did not use this as a solved target.

## Numerical work and its limits

`transfer_search.py` computes trace(M^5), its analytic gradient, and a
Sinkhorn diagonal scaling to regular hosts. It verifies the transfer density
against an independent O(n^5) formula obtained by integrating one color class
first, for n=2,3,4. It verifies all analytic gradients by finite differences.
These checks pass, including after the storage correction below.

* `spectral5_n5.json`: 60 deterministic multistart searches for
  log(trace(M^5))-5 log(lambda_max(M)), using initial log-entry standard
  deviations .3,1,2,4,8. No violation beyond floating-point roundoff was
  found; many minimizers tend toward rank one.
* `regular_sidorenko_n8.json`: 100 deterministic multistart searches for the
  regular 8-state Sidorenko ratio, up to 400 L-BFGS-B iterations each. No
  violation was found. The best displayed objective is about 8.74e-13.
  Some large-variance starts did not converge and stayed at positive values.

The original stored best regular-search matrix was the raw pre-scaling host.
It was corrected to the actual regularized matrix on 2026-10-02, and the
script now stores that matrix in future searches. Its maximum row-mean error
is approximately 5.3e-13. This correction does not change the objective
calculations used during optimization.

These are finite floating-point searches. They establish neither the target
inequality nor absence of counterexamples. No theorem should be claimed from
them.
