VERDICT: PARTIAL exact finite-box ratio criterion for cylinder convergence on Z³

The next step proposed in round 3 is complete. PROOF.md gives an exact
finite-box counterpart of the tree's survival-ratio criterion. It does not
prove that the required ratios converge at criticality on Z³, and T160
remains unresolved by this work.

For a fixed box B_m, retain the partition π of all boundary vertices and
the root induced by the interior open edges. Let h_(m,n)(π) be the
probability, over exterior edges, of a root-to-∂B_n connection after
identifying vertices according to π. The response uses the join with the
exterior connectivity partition, allowing any number of returns through
other interior components. Let π_star join every boundary vertex and the
root. Then the requested cylinder convergence is equivalent to convergence
of

    r_(m,n)(π) = h_(m,n)(π) / h_(m,n)(π_star)

for every fixed m and every realizable π.

This equivalence includes an exact finite-box law. If a_m(π) is the ordinary
product probability of π and ν_(m,π) is the interior law conditional on π,
then

    μ_n|E(B_m) = Σ_π [a_m(π) r_(m,n)(π) / Z_(m,n)] ν_(m,π),
    Z_(m,n) = Σ_π a_m(π) r_(m,n)(π).

The response at π_star is one. Its ordinary probability a_star is positive,
and a_star ≥ p^((2m+1)^3−1) by opening a fixed spanning tree. If

    D_m(n,l) = Σ_π a_m(π) |r_(m,n)(π)−r_(m,l)(π)|,

the proof gives

    D_m(n,l)/(2+1/a_star) ≤ TV(μ_n|E(B_m), μ_l|E(B_m))
                         ≤ D_m(n,l)/a_star.

The constants concern a fixed box and deteriorate as the box grows.
The argument works for every 0<p<1 and does not assume critical extinction.

One necessary correction to a simpler formulation is proved explicitly:
the root-connected boundary set alone does not determine the exterior
response. In B_1, two interiors with that same set have different responses
to ∂B_3 because an exterior path can return through another interior
component. Section 5 of PROOF.md gives integer coordinates and the positive
response-gap bound p^5(1−p)^823.

The earlier result was independently rechecked and holds. Fresh exact
population calculations and mixture identities agree with the preceding
tree proof. Its critical parameter, vertexwise critical extinction, spine
law, vanishing adjacent weight increments, and full interval of mixture
limits were also rederived analytically in LOG.md.

Reproduction commands, from this folder:

~~~sh
nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
~~~

Both exited 0. The new audit passed 41,760 direct BFS/partition-join
configuration comparisons across 36 finite graph/parameter/target models;
756 conditional atom formulas; 504 partition-mixture/inverse checks;
36 total-variation comparisons; and 768 independent normalization stress
checks. It also checked the actual cubic coordinates, edge counts by two
methods, and explicit spanning trees. Runtime was 0.322 seconds and peak
RSS 16,613,376 bytes. The earlier-result recheck took 0.028 seconds and
14,123,008 bytes, including 64 stage certificates. These are exact finite
checks, not simulation or full-box enumeration. Scripts use the standard
library, one thread, and 120-second alarms. Their inherited nice priority
was 20; the redundant nice request warned but retained that lower priority.
Exact outputs and audit details are saved in this folder.

The five-minute literature check located no verified solution of T160.
Opened sources were Deepan Basu and Artem Sapozhnikov,
[arXiv:1603.06884](https://arxiv.org/abs/1603.06884), whose construction
assumes quasi-multiplicativity; Shirshendu Chatterjee, Pranav Chinmay,
Jack Hanson, and Philippe Sosoe,
[arXiv:2502.10882](https://arxiv.org/abs/2502.10882), using
high-dimensional two-point asymptotics; Malo Hillairet,
[arXiv:2509.18852](https://arxiv.org/abs/2509.18852), concerning the planar
setting; and Zhenhao Cai and Jian Ding,
[arXiv:2412.05709](https://arxiv.org/abs/2412.05709), concerning GFF and
loop-soup models. This was a brief check, not an exhaustive review.

What failed or remains uncertain: the root-boundary-set reduction fails
as above. No contraction across lattice annuli, quasi-multiplicativity,
or asymptotic response-ratio estimate was obtained. The finite-box
criterion is a conditioning identity, with no claim of literature novelty.
It identifies the missing input rather than supplies it.

Next worker: for a fixed m, try to control the weighted oscillation
D_m(n,l) as n,l→∞ at p_c. The corrected state space is the full realizable
interior boundary partition with its root block. Convergence of the
conditioned marked exterior partition law would suffice, but the response
criterion only requires convergence of its finitely many connectivity
functionals. Start with an actual estimate for these ratios; do not repeat
the tree classification or infer convergence from compactness.

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 Nov 2026, approximately 04:58 Asia/Tbilisi.
