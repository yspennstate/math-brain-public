# C0017: independent boundary obstruction

2026-10-10. Author w415. This derivation was saved before reading w414's proof. Referee: w416; independent check pending. Current openness of C0017 is UNKNOWN. No solution or novelty claim is made.

The recovered intake statement (problems.jsonl, line 17, source garban_steif_noise_2012) asks for critical independent square-bond conformal invariance at p=1/2, including Cardy's crossing formula and convergence of exploration interfaces to SLE(6). The working fixed-domain formulation uses a bounded Jordan domain with four distinct cyclic boundary marks, a canonical lattice approximation preserving marked prime ends, and free crossing boundary conditions. For the separate interface clause use Dobrushin primal/dual boundary conditions and convergence modulo increasing reparametrization. No equivalence of these clauses is assumed. A claim uniform over every marked Jordan domain at each delta is stronger and false under the explicit discretization below.

## Independent counterexample: changing the domain with the mesh

Use free boundary conditions and the graph induced by the vertices of delta Z^2 in the closed rectangle. Mark its four corners in cyclic order; the crossing connects its left and right vertical sides. Define

    D_delta = (0, 2 delta) x (-delta/2, delta/2).

The closed rectangle contains exactly three vertices: (0,0), (delta,0), (2 delta,0). It contains exactly two bonds. Thus a left-to-right open crossing occurs if and only if both bonds are open. At p=1/2 these distinct bond variables are independent, and the crossing probability is exactly 1/4 for every positive delta. No conditional-product argument is used.

The conformal shape is always a rectangle of horizontal aspect ratio 2. Let C(x) denote Cardy's function in the cross-ratio convention for which

    C(x) = [integral_0^x t^(-2/3)(1-t)^(-2/3) dt] / B(1/3,1/3),
    r = K(1-x)/K(x),
    K(m) = integral_0^(pi/2) (1-m sin(theta)^2)^(-1/2) dtheta.

For r=2, the classical quadratic elliptic transformation gives x=(sqrt(2)-1)^4. To check the convention, at r=1 one has x=1/2 and C(x)=1/2. Applying the descending Landen transformation to m=1/2 doubles K(1-m)/K(m) and gives the stated x. The analytic identities are made explicit in the appendix below and remain obligations for the independent referee.

Here is a purely algebraic upper bound, with no simulation. Since sqrt(2)>140/99, and (17/99)^2 < 1/32, we have 0<x<1/32. By symmetry of the beta integrand,

    B(1/3,1/3) = 2 integral_0^(1/2) t^(-2/3)(1-t)^(-2/3) dt
                 >= 6 (1/2)^(1/3).

The numerator is at most 3 x^(1/3)(1-x)^(-2/3). Consequently

    C(x) <= (1/2)(2x)^(1/3)(1-x)^(-2/3)
           < (8/961)^(1/3) < 1/4,

where the final inequality is equivalent to 512<961. The approximation error for this family is bounded below by the positive constant 1/4-(8/961)^(1/3), at every mesh. This refutes

    sup over all marked Jordan rectangles Q of |P_delta(H_Q)-Cardy(Q)| -> 0.

It does not refute a limit for each fixed Q: here delta/height(D_delta)=1, so the domain never has a fine lattice approximation relative to its own scale. A missing necessary premise is that mesh is small relative to the domain and relevant boundary features; a proof may instead keep the marked domain fixed. Normalizing diameter alone is not asserted sufficient for general Jordan families with necks or colliding marked points.

## Second, disjoint obstruction: RSW alone does not set the Euclidean metric

Smirnov's triangular-site theorem (0909.4499v1, Corollary 2) supplies the base model. Apply A_s(x,y)=(s x,y), s>1, to every embedded vertex and edge, preserving the independent p=1/2 site colors. Crossing probabilities in Q equal those in A_s^(-1)Q. For axis-aligned rectangles the usual fixed-aspect RSW bounds persist, with constants depending on s and the aspect ratio; full-sequence crossing limits in fixed Jordan quadrilaterals persist by pullback.

Write F(r) for the base model's limiting horizontal crossing probability in a rectangle of width/height r. Cardy's function is strictly decreasing in r, F(1)=1/2 and F(r)+F(1/r)=1. The stretched model's horizontal crossing limit in the unit square is F(1/s)>1/2 and its vertical crossing limit is F(s)<1/2. Rotation of the marked square by pi/2 is conformal and exchanges these events. Thus the stretched model is not Euclidean conformally invariant, despite independence, planarity, FKG, criticality, RSW and unique crossing limits.

This only defeats a bridge that omits control of the effective metric or isotropy. The stretched lattice is triangular-site, not square-bond, and lacks the target's pi/2 symmetry. It cannot refute the original C0017 conjecture or a bridge with additional hypotheses establishing the correct metric.

## Sources checked before paired-proof access

- Smirnov, Critical percolation in the plane, https://arxiv.org/html/0909.4499v1, Theorem 1 and Corollary 2: triangular-site crossing limit. Domain-dependent constants appear in Lemma 2.2.
- Schramm, Conformally invariant scaling limits, https://arxiv.org/pdf/math/0602151: primary open-problem source recovered, exact relevant problem location pending.
- Tsai--Yam--Zhou, https://arxiv.org/abs/1112.2017v5: primary metadata describes a preliminary version and critical comments. This is a proof claim, not a validation receipt.
- Zhou, https://arxiv.org/abs/2409.03235: a primary claimed square-bond proof; acceptance and correctness have not been established here.

## Verification appendix added after independent saving and paired-proof access

Cardy equation (8) in hep-th/9111026v1 is C(x). A Schwarz--Christoffel map from the upper half-plane with consecutive prevertices 0,x,1,infinity has adjacent side lengths

    integral_0^x [t(x-t)(1-t)]^(-1/2) dt = 2 K(x),
    integral_x^1 [t(t-x)(1-t)]^(-1/2) dt = 2 K(1-x).

These follow by t=x sin(theta)^2 and t=x+(1-x)sin(theta)^2. Take [0,x] and [1,infinity] as the two vertical sides whose connection is measured. Hence horizontal width/height is K(1-x)/K(x), without importing Cardy's different intermediate elliptic parameter convention.

For the exact aspect-2 value write L(k)=K(k^2), k=1/sqrt(2), and a=(1-k)/(1+k)=(sqrt(2)-1)^2. DLMF 19.8.12 gives L(k)=(1+a)L(a). Applying that same descending transformation to sqrt(1-a^2), whose complementary modulus is a, gives L(sqrt(1-a^2))=(1+k)L(k), because (1-a)/(1+a)=k. Therefore

    K(1-a^2)/K(a^2) = (1+k)(1+a) = 2.

This verifies x=a^2=(sqrt(2)-1)^4 in the stated convention.

The bounded foreground verifier was run once under a fresh task-local arithmetic gate. Six exact induced-graph cases at delta=1,1/2,1/1024 and aspects 1,2 agree with the derived probabilities. Three rational inequalities passed. The numerical aspect-2 Cardy value is 0.17564689380065532, producing difference 0.07435310619934468 from 1/4; the analytic positive gap bound displays as 0.04733028049087784. Floating-point values are illustrations, not interval certificates or formal proofs. MEASUREMENTS.json records the command and CPU/wall cost.

ADVERSARY_VERDICT.md separately checks w414's corridor/prime-end proof and returns a scoped KEEP. The missing marked-prime-end premise is quantitatively verified in that peer argument. Our own new claims remain pending w416.

NEXT: w416 independently checks claims 002/003; coordinator reviews the draft concepts without promoting them to a solution of C0017.
