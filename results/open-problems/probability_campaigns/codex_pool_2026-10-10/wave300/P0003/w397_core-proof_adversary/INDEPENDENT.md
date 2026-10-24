# Independent derivation, saved before reading the paired prover

Date: 2026-10-10. Target: P0003. Author: w397. Reviewer: w398, pending.

The exact target and primary-source versions are being recovered separately. This finite lemma is independent of a current-open-status assertion and does not claim to describe an actual SAW observable.

Let an embedded honeycomb graph have edge midpoints p. Consider the homogeneous local identity

    sum_{p adjacent to v} (p-v) F(p) = 0

at each interior vertex v. Fix any hexagonal face wholly inside the domain. Write its vertices in counterclockwise order as v_0,...,v_5, with v_6=v_0, and let p_j=(v_j+v_{j+1})/2. All six edges have length delta. Define

    H(p_j) = delta/(v_{j+1}-v_j),  j=0,...,5,
    H(p) = 0 on every other edge midpoint.

At v_j the only nonzero terms are

    (p_{j-1}-v_j) H(p_{j-1}) = -delta/2,
    (p_j-v_j) H(p_j) = delta/2.

They cancel exactly. At every other vertex all incident values vanish. Thus H satisfies every homogeneous interior identity and vanishes on the domain boundary. Consequently, if F is any solution with prescribed boundary values, F+cH is another solution with precisely the same boundary values, for every complex c.

For a regular hexagon, |H(p_j)|=1 and |H(p_{j+1})-H(p_j)|=1. The distance between those adjacent midpoints is sqrt(3)*delta/2. Taking faces centered at a fixed interior point as delta tends to zero gives a uniformly bounded family of solutions, with zero boundary values, that is not equicontinuous on any compact neighborhood of that point. A uniform limit to a continuous function would force these adjacent differences to tend to zero, so these fields have no such locally uniform convergent subsequence.

This proves that this local relation, even with fixed boundary data and a uniform magnitude bound, does not imply uniqueness or the locally uniform compactness needed to identify a holomorphic scaling limit. It does NOT prove that the true SAW observable fails to converge: its definition by walk sums may impose additional constraints. The missing premise must control those additional constraints quantitatively.

A useful reformulation is to orient each edge e=(u,w), let d_e=w-u and J_e=d_e F(p_e)/2. The local identity is the complex incidence equation div J=0. A circulation around any interior cycle produces a homogeneous mode. This reformulation requires no independence, probability estimate or continuum limit.

NEXT: Verify the exact local identity and target ensemble in the primary papers, then audit the paired proof for a step that suppresses these circulation modes without an additional estimate.
