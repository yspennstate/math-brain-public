# C0017: a quantitative obstruction to an unmarked boundary bridge

Author: w414. Date: 2026-10-10. Author proof; independent review pending. No novelty claim. C0017 is not solved here.

## Exact working target and prior attempt

For a bounded Jordan domain D with four distinct boundary points a,b,c,d in positive order, critical independent bond percolation on mesh-delta square-lattice approximations, with correctly converging marked boundary arcs, should have a limiting ab-to-cd crossing probability given by Cardy's formula. Separately, the primal/dual Dobrushin exploration between two correctly converging boundary marks should converge modulo increasing reparametrization to chordal SLE(6). Boundary conditions and marked prime ends are part of the hypotheses. The intake's source is Garban--Steif, arXiv:1102.5761, Chapter II Section 4; the intake alone does not establish an equivalence of these two target clauses.

An exact normalization of the crossing target is the Cardy--Carleson triangle form: conformally map D to an equilateral triangle of side one, mapping a,b,c to its successive corners. The image of d lies on the c-to-a side. The predicted limit for the ab-to-cd crossing is the Euclidean distance x from the image of c to the image of d. Garban--Steif Theorem II.2 states this calibration for triangular site percolation. The same value for square-lattice bond percolation is the conjectural target, not a consequence proved here. The explicit historical open sentence is on printed p.24 of arXiv v3, rather than the intake's p.26 locator.

The 2026-09-07 attempt C0017-A001 sought a Smirnov-type square-lattice observable and stopped at missing discrete analytic information. Its claims are author-only and cannot be promoted by a source hash check. Later primary preprints arXiv:1112.2017v5 and arXiv:2409.03235v6 claim SLE(6) convergence; the former explicitly records critical comments and a promised clean proof. Neither is audited in this packet. Current openness: UNKNOWN.

My proposed bridge to stress-test is **B**: if Jordan lattice domains approximate a fixed Jordan domain in closure Hausdorff distance, boundary Hausdorff distance, area, and unmarked Caratheodory convergence, and their four marked boundary points converge in Euclidean distance, then critical crossing probabilities agree asymptotically with those in the canonical approximation of the limit domain. B is a deliberately stronger auxiliary assertion, not the target's legitimate marked-domain hypothesis. The results below refute B.

## Lemma 1: exact series-corridor factorization

Let G be a finite graph consisting of disjoint chamber graphs L and R, joined only by a simple path e_1,...,e_k from vertex u in L to vertex v in R. The k-1 interior path vertices belong to neither chamber and have no other incident edges. Source terminals S are in L and sink terminals T are in R. Every edge is independently open with probability p, 0<p<1, and there are no external or cross-chamber identifications. Write q_L=P(S connects to u within L), q_R=P(v connects to T within R). Then

    P(S connects to T in G) = p^k q_L q_R <= p^k.

Proof: each e_i is a bridge separating S from T. Any crossing must use all k, and must reach its endpoints inside the two chambers. Conversely, these three events concatenate into a crossing. They depend respectively on the mutually disjoint edge sets E(L), {e_i}, E(R), so product Bernoulli independence gives the equality. This is not a multiplication of conditional per-row estimates. The bound is sharp over this class: take S={u}, T={v}, so both chamber events are certain. It also holds with arbitrary dependence within chambers if the three edge families are independent and corridor edges remain independent Bernoulli(p).

## Lemma 2: domains with four geometric convergence properties and vanishing crossings

Let n>=81 be an integer, t=floor(sqrt(n)), a=t, b=2t+1, k=b-a=t+1, and m=floor(n/2). Let Q=(0,1)^2. Form K_n as the union of three closed rectangles:

    [0,a/n] x [0,1],
    [b/n,1] x [0,1],
    [a/n,b/n] x [(m-1/2)/n,(m+1/2)/n].

Let D_n be the interior of K_n. It is a bounded simply connected Jordan polygon: the chambers have positive widths, the corridor has positive height, their overlaps at the two gates have positive-height interior neighborhoods, and the resulting polygon has one simple boundary and no holes. Keep the distinct marks

    A=(0,1), B=(0,0), C=(1,0), D=(1,1),

in positive cyclic order. Arc AB is the entire left side; arc CD is the entire right side. All four marks are fixed in Euclidean coordinates.

Use the induced nearest-neighbor square-lattice graph G_n on the vertices of n^{-1} Z^2 lying in K_n. The three geometric rectangles give exactly these vertices (written in unscaled integer coordinates):

    x<=a, all 0<=y<=n;
    x>=b, all 0<=y<=n;
    a<x<b, only y=m.

There is only one chain from the left chamber to the right chamber. It contains exactly k=b-a horizontal edges. Lemma 1, with source x=0 and sink x=n, gives

    P_{1/2}(AB connects to CD in G_n) <= 2^{-(floor(sqrt(n))+1)} -> 0.

Every n-edge straight horizontal path at y=m also shows the positive lower bound 2^{-n}; this positivity is not used for the limit.

The convergence statements follow directly:

1. Since K_n is contained in [0,1]^2, and every removed point can move horizontally to a chamber, d_H(K_n,[0,1]^2)<=k/(2n).
2. Every added inward boundary segment has x<=b/n and hence distance at most b/n from the square boundary. Missing square-boundary pieces on y=0 or y=1 are within k/(2n) of their retained endpoints. Thus d_H(partial D_n,partial Q)<=b/n.
3. Area(Q minus D_n)=k(n-1)/n^2 ->0. The number of removed lattice vertices is exactly (k-1)n=t n, a fraction t n/(n+1)^2 ->0.
4. Take basepoint z_0=(1/2,1/2). Every compact subset of Q has x-coordinate bounded away from zero and eventually lies entirely in the right chamber (b/n,1)x(0,1). All D_n are contained in Q. Therefore their unmarked Caratheodory kernel at z_0 is exactly Q, for the full sequence and every subsequence.

This is a connected induced-graph construction with a fixed critical parameter, a simply connected Jordan domain at each n, fixed distinct Euclidean marks, and convergence of both domains and their entire boundaries. The obstruction persists despite all four convergence properties.

## Lemma 3: quantitative collapse of the marked prime ends

Let f_n be the normalized Riemann map from the unit disk to D_n, f_n(0)=z_0 and f_n'(0)>0. Jordan boundary extension makes f_n^{-1}(A) and f_n^{-1}(B) well-defined and distinct at each finite n. They nevertheless approach one another on the unit circle.

The gate Sigma_n={b/n} x [(m-1/2)/n,(m+1/2)/n] separates z_0 in the right chamber from the whole left chamber. Let J_n be the boundary arc going from the upper gate endpoint along the upper corridor wall, around the left chamber through A and B, and back along the lower corridor wall to the lower gate endpoint. Brownian motion from z_0 cannot exit on J_n before crossing Sigma_n. Up to its first visit to the gate it lies in the right rectangle; consequently

    omega_{D_n}(z_0,J_n)
      <= P_{z_0}(first hit of the line x=b/n is in Sigma_n)
      <= 1 / (pi n (1/2-b/n)) <= 4/(pi n).

The middle estimate is the elementary half-plane Poisson kernel s/[pi(s^2+(y-1/2)^2)] with s=1/2-b/n, integrated over an interval of length 1/n. The first-event comparison is valid because any exit through the other three sides of the right rectangle exits D_n; it cannot later produce an exit on J_n. For n>=81, b/n<=1/4.

Conformal invariance of Brownian harmonic measure says that the unit-circle arc f_n^{-1}(J_n) has angular length 2 pi omega_{D_n}(z_0,J_n). Since it contains both marked preimages,

    |f_n^{-1}(A)-f_n^{-1}(B)| <= 8/n ->0.

For the square's normalized Riemann map f, f^{-1}(A) and f^{-1}(B) are distinct. Thus these domains do not converge as marked prime-end quadrilaterals, even though the four marks have not moved in Euclidean distance. This is the missing hypothesis in B, demonstrated quantitatively rather than inferred from a crossing probability.

## Consequence and legitimate repair

The canonical critical square crossing probabilities are uniformly positive by the classical square-lattice RSW theorem (Garban--Steif Theorem II.1), whereas the G_n probabilities tend to zero. Hence B fails. This refutes a proposed approximation bridge, not C0017. No claim that RSW identifies Cardy's value is made.

A repaired bridge must control the marked prime ends, or impose boundary regularity sufficient to preserve them. Convergence of interior conformal maps by itself does not control the four boundary preimages; Lemma 3 gives an explicit failure.

## Single hardest remaining gap

For the legitimate C0017 target, identify the law of a subsequential critical square-lattice crossing/interface limit in a nondegenerate correctly marked Jordan domain as Cardy's/SLE(6), with full-sequence convergence. Nothing in the series-corridor calculation or the half-plane estimate provides that identification. Tightness, RSW, numerical symmetry, or a source receipt does not close it.

NEXT: Have w416 check the series separation, geometric/kernel limits, harmonic-measure comparison, and precise scope of the refuted bridge; then submit only labeled draft counterexample material for coordinator integration.

## Saved finite controls

Command: `python -X utf8 ~/brain_workers/w414/check_boundary.py`. Result: PASS, 38,496 exhaustively enumerated configurations in 1.237533 seconds including a fresh resource check (82.8 percent CPU; 2,913,062,912 available memory bytes). Six exact identities at p=1/3,1/2,2/3 matched their products. A 2-by-2 edge square has crossing probability 43/64, the two-edge neck control has 1/4, and adding a bypass vertex gives 1/2, invalidating the old neck bound as intended. The n=81 member has 5,995 vertices, 11,745 edges, 729 deleted vertices, and ten single-edge separating cuts. MEASUREMENTS.json distinguishes exact finite counts from evaluated analytic bounds. These checks do not certify the universal geometric or harmonic-measure proof and do not prove C0017.
