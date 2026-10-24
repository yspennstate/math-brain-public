# C0059: second serious attempt, 2026-10-12

## Starting gap and two new approaches

The original attempt left the need for an almost-sure finite-energy flow on the actual dual Boltzmann map. Perimeter scaling and FPP nonexplosion do not control current routing.

1. **Exact trace-network reduction, followed by a long-range comparison.** Subdivide dual edges and eliminate face centers. This replaces huge dual degrees by bounded total conductance on a network of primal edge midpoints, with long-range edges inside each face. Seek a comparison with a transient long-range model, or a recurrence theorem for the resulting dependent conductances.
2. **Bounded-degree planar face fillings.** Replace large face stars by bounded-degree planar disks and try to transfer recurrence from planar local limits, or obtain a recurrent counterexample. This requires a terminal-resistance comparison uniform in the number of terminals. There is no such estimate established here; merely replacing stars by boundary cycles is demonstrably insufficient.

Approach 1 is pursued below. It produces an exact reformulation and a quantitative obstruction to the simplest neighbouring recurrence theorem. It does not solve C0059.

Brain queries were for the gap itself: effective resistance/harmonic measure/independent overlap, then star mesh/Schur complement/Dirichlet/long-range percolation/Berger, then Berger's named transience and recurrence theorem. Retrieved cards gave general electrical and Schur-complement hints, no theorem applicable to the Boltzmann dual. These queries and subsequent literature checks are in LITERATURE.md.

## 1. Exact midpoint network

Fix an infinite connected locally finite dual multigraph G=m-dagger, with unit edge conductances. Each vertex f is a primal face, with degree d_f counting incidences; a loop counts twice. Write e for an original edge and x_e for its new midpoint. Replace e by its two half-edges, each of resistance 1/2 (conductance 2). The subdivided network H has vertex classes face centers and midpoints. For a loop, there are two parallel half-edges from its midpoint to the same face center. For every e, the total half-edge conductance incident to x_e is exactly 4.

Let m_fe be the number of incidences of e with face f: 0, 1 or 2. Thus sum_f m_fe=2 and sum_e m_fe=d_f. Define a network K on the midpoint vertices, with conductance between distinct e,e' given by

    C(e,e') = sum_f [2 m_fe m_fe' / d_f].                 (1)

The finite sums range only over faces incident to e and e'. It is useful to keep each face contribution as a separate parallel edge, and to expand repeated incidences into labeled ports. Combining parallel conductances gives exactly (1).

K is connected and locally finite: paths in G yield paths between its edge midpoints through the cliques at shared vertices, and each midpoint is adjacent to only the finitely many edges incident to its at most two face centers. Its weighted degree satisfies

    c_K(e) = sum_f 2 m_fe (d_f-m_fe)/d_f <= sum_f 2m_fe = 4.       (2)

The combinatorial degree is not bounded. A face with five distinct boundary edges creates a K_5 clique. Thus bounded conductance is not a bounded-degree planar-network recurrence hypothesis.

## 2. Dirichlet identity, with all constants

For a degree-d face with incidence-port potentials u_1,...,u_d and center potential z, its contribution to the energy of H is

    E_star(u,z) = 2 sum_i (u_i-z)^2.

Let ubar=(sum_i u_i)/d. Expanding squares and using sum_i(u_i-ubar)=0 gives

    E_star(u,z) = 2 sum_i (u_i-ubar)^2 + 2d(z-ubar)^2.

Also

    sum_{i<j}(u_i-u_j)^2 = d sum_i(u_i-ubar)^2,

since the sum over all ordered pairs expands to 2d sum_i u_i^2 - 2(sum_i u_i)^2. Therefore

    min_z E_star(u,z) = (2/d) sum_{i<j}(u_i-u_j)^2.        (3)

This is the clique energy with each labeled port pair given conductance 2/d. Identifying repeated midpoint ports in (3) gives (1); terms between equal midpoint ports vanish. There is no replacement of electrical conductance 2/d by unit conductance.

For finitely supported midpoint potentials u, setting every center to the average of its incidence potentials gives finitely supported potentials on H. Indeed only finitely many face centers meet the finite support. Summing (3) is therefore legitimate; no infinite matrix inverse is needed. Conversely every finitely supported H potential restricts to a finitely supported midpoint potential and has energy at least its K energy.

For any fixed midpoint x_0, minimizing over finite-support functions equal to 1 at x_0 gives the same capacity in H and K. Capacity zero is the standard electrical criterion for recurrence; positive capacity is the criterion for transience. This already proves H and K have the same recurrence type.

The exact finite identity underlying (3), without division by d, is

    d sum_i (u_i-z)^2
      = (1/2) sum_{i,j}(u_i-u_j)^2 + (sum_i u_i-dz)^2.     (4)

It is formalized over rational potentials for every finite index set in StarMeshCheck.lean. Its verification status is recorded below; the real-valued proof is the explicit square expansion above.

## 3. Constructive flow lifting, and its reverse

We also need to know that this trace is useful for upper resistance bounds, rather than an illicit short-circuit comparison.

Consider a clique current j_ij=-j_ji at a degree-d face, with b_i=sum_j j_ij. Then sum_i b_i=0. Its energy is

    E_clique(j) = (d/2) sum_{i<j} j_ij^2.

The minimum-energy clique current with these port divergences is

    j*_ij=(b_i-b_j)/d.

Its divergence is b_i, because sum_j b_j=0. Its energy is (1/2)sum_i b_i^2 by the pair-variance identity. To check minimality fully, write j=j*+k. Every row divergence of k is zero, and

    sum_{i<j}(b_i-b_j)k_ij = sum_i b_i sum_j k_ij = 0.

Expanding the energy proves

    E_clique(j) = (1/2)sum_i b_i^2 + (d/2)sum_{i<j}k_ij^2.

Send current b_i from port i toward the center. The center has zero divergence; each port has exactly its previous divergence b_i. Since each half-edge resistance is 1/2, this star current has energy (1/2)sum_i b_i^2 <= E_clique(j).

Performing this replacement independently at every face lifts a conserved unit flow on K to H with no increase in energy. If conductances from different faces or repeated incidence pairs have first been combined, split their currents proportionally to their conductances: j_l=(c_l/sum c_l)j. The summed energy is j^2/(sum c_l), exactly the original combined-edge energy. Thus there is no aggregation loss. At each original midpoint the two half-edge currents conserve current, except at the chosen source midpoint. Away from that source, the two halves can be combined into an original dual edge with unit resistance and unchanged energy.

For the reverse direction, start with an H flow whose only source is a midpoint. At each center conservation says sum_i b_i=0. Replace its star current by j* as above; energy is exactly preserved and midpoint divergences agree. All operations are face-local, on finitely many ports. Tonelli applies to the nonnegative energy sum, so finite-energy flows remain finite-energy flows in either direction.

Sources at a dual vertex and a neighbouring midpoint can be interchanged by adding a unit current on their connecting half-edge, which has finite energy 1/2. The inequality (s+t)^2<=2s^2+2t^2 shows finite energy stays finite. This takes care of source placement; no root face was incorrectly identified with a random high-degree face.

Consequently, almost-sure transience of the requested Boltzmann dual is **equivalent** to almost-sure transience of the exact network (1). This is a reformulation valid for every individual locally finite map, not just an averaged comparison.

## 4. A second exact check: the Markov trace

SRW in H alternates between midpoints and centers. From midpoint e it chooses a center f with probability m_fe/2, and then chooses midpoint e' with probability m_fe'/d_f. The two-step transition is therefore

    Q(e,e')=(1/2) sum_f m_fe m_fe'/d_f.                   (5)

It is symmetric, and sum_e' Q(e,e')=(1/2)sum_f m_fe=1. Off the diagonal, 4Q(e,e')=C(e,e'). Holding probabilities are harmless: removing them gives the random walk associated to C and preserves recurrence type. In this infinite connected graph Q(e,e)<1 at every midpoint, since an isolated midpoint component would contradict connectivity. A geometric number of holding steps is finite almost surely at each visit.

At centers, the analogous two-step chain is (I+P_G)/2: choosing an incidence of an original edge and then one of its two endpoint incidences either stays at the center or makes the original SRW step. This holds for loops as well as multiple edges. Laziness preserves recurrence. Midpoint and center visits have the same recurrence classification in the irreducible H chain. Thus (5) independently confirms the recurrence equivalence, including the constants and loop conventions.

## 5. The recurrent comparison graph, and the sharp distortion

Let M be the medial multigraph: its vertices are primal edge midpoints, and every primal face contributes a cyclic list of unit-conductance edges between consecutive incidence ports. A degree-2 face contributes two parallel edges between its distinct midpoints; repeated equal ports give loops. Every medial vertex has four incidence corners, so its degree is four counting multiplicity, or at most four after loops are removed. M is connected and planar.

For the critical Boltzmann map, M is almost surely recurrent. Here is the precise reduction to a known theorem. The source's Theorem 8 gives local convergence of finite Boltzmann maps with root face perimeter 2; after gluing the two root-face edges their root edge is uniform among oriented edges (as explicitly noted on PDF p. 90 in the primal recurrence proof). Taking medials makes that root a uniform medial vertex. Taking medial neighbourhoods is continuous at locally finite embedded maps: each radius-r medial exploration uses only finitely many adjacent incidence corners, whose primal endpoints lie within a finite primal neighbourhood. Each finite medial is planar and of maximum degree four. The Benjamini-Schramm bounded-degree planar-limit recurrence theorem therefore applies. The root-face gluing or restoration affects only finitely many medial edges/vertices and does not alter recurrence of the infinite connected graph. This application uses the source's local-limit theorem and the standard Benjamini-Schramm theorem; it is not a new proof of those theorems.

For one degree-d face, write

    E_M,f(u)=sum_{i=0}^{d-1}(u_{i+1}-u_i)^2,
    E_K,f(u)=2sum_i(u_i-ubar)^2,

with cyclic indices. Adjacent differences satisfy

    (u_i-u_{i+1})^2 <= 2[(u_i-ubar)^2+(u_{i+1}-ubar)^2].

Summing proves E_M,f <= 2E_K,f. For an upper bound, every pair difference can be expressed along a cyclic path of length at most d; Cauchy-Schwarz bounds it by d E_M,f. There are d(d-1)/2 pairs, so (3) gives E_K,f <= d(d-1)E_M,f <= d^2 E_M,f. These inequalities remain true for repeated incidence ports.

The exact best upper constant on unrestricted port potentials is

    A_d = 1/[2 sin^2(pi/d)] ~ d^2/(2pi^2).                (6)

Proof. The real sine/cosine modes, equivalently the unitary finite Fourier basis, diagonalize the cyclic quadratic form. For frequency k!=0, its eigenvalue is |exp(2pi i k/d)-1|^2=4sin^2(pi k/d); the mean-zero clique form has eigenvalue 2. The smallest nonzero cycle eigenvalue is 4sin^2(pi/d), so the maximum ratio is (6). The mode u_i=cos(2pi i/d) attains the ratio; the same computation applies at d=2, where the cyclic multigraph has two parallel edges. This proves sharpness and not merely a numerical trend.

If face degrees were uniformly bounded by D, summing the rough estimate would give E_K<=D^2 E_M. Recurrence of M would then imply recurrence of K: choose finitely supported test potentials with value 1 at the root and M energy tending to zero; the K energies also tend to zero. This recovers a bounded-face sufficient condition, but the source types a<5/2 have unbounded face support and it gives no C0059 special case.

In the present range, bounded total conductance (2) cannot replace the missing uniform comparison. The face contribution spreads its bounded rate over many distant ports. Its effect on slowly varying boundary data grows as d^2. No finite-moment comparison was silently made.

## 6. Attempted applications of neighbouring theorems

### Long-range transience

Noam Berger, *Transience, Recurrence and Critical Behavior for Long-Range Percolation*, Commun. Math. Phys. 226 (2002), 531-558, DOI 10.1007/s002200200617, arXiv:math/0110296v3. Theorem 1.4, PDF p. 3, gives transience on a percolating independent Z^2 long-range cluster when 2<s<4 (and recurrence when s>=4). It is a lead, not a solution to C0059.

K has none of the necessary verified inputs: its vertex set is a random recurrent medial graph rather than Z^2; its cliques correlate many edges; the 2/d conductances are not unit percolation bonds; and polynomial face degree alone does not give a Euclidean or medial-distance jump exponent. No stochastic domination, rough embedding or uniform finite-energy routing comparison to that independent percolation model has been constructed. Assigning s from a by dimensional analogy would be a conjecture, not a theorem.

### Random-conductance recurrence

The same paper's Theorem 1.9, PDF p. 5, says a recurrent bounded-degree graph with iid positive edge conductances is almost surely recurrent. Could face clique currents be pushed onto M and this theorem used instead? The comparison above gives the explicit candidate upper-conductance network W: every cyclic edge contributed by face f is assigned conductance d_f^2. Summing E_K,f<=d_f^2 E_M,f gives E_K<=E_W. Therefore **recurrence of W would imply recurrence of K**, and hence produce a counterexample to the transience conjecture, or even disprove it throughout a parameter range.

But the W conductances are not iid marks sampled on a fixed recurrent graph: the entire d_f-cycle receives the same multiplier. Unconditionally, face-sharing edges inherit the same random degree. Conditional on the full embedded and face-colored medial map, these weights are fixed, generally nonidentical values rather than an iid common-law assignment. Deterministic conditional values are of course trivially independent; that fact does not satisfy the identical-distribution hypothesis or remove the dependence between weights and graph geometry. Theorem 1.9 therefore does not apply. No recurrence proof for W is provided. In fact E_K<=E_W is an upper energy comparison; a transient W would tell us nothing about K.

The forward transience route likewise needs a genuine lower network comparison. Wiring or contracting a face cycle would lower resistance, and would not prove K transient. Replacing conductance 2/d clique bonds by unit bonds would increase conductance and also have the wrong direction for a transience upper-bound proof.

### The actual discovery law has still heavier tails

To check whether a moment estimate could rescue the weighted-medial comparison, use the actual infinite-map peeling transitions rather than the bare increment law nu. Source Definition 17 and Proposition 22 (PDF pp. 49-51) give, conditional on half-perimeter ell and the explored past,

    P(C_k | past) = nu(k-1) h^up(ell+k-1)/h^up(ell),

where C_k reveals a new degree-2k face. The exact function is h^up(r)=2r 4^(-r) binomial(2r,r), so h^up(r)~(2/sqrt(pi))sqrt(r). For every allowed a, nu(k-1)~b k^(-a) with b>0 (b=1/4 for the source's type 2; b=p_q cos(a pi) for 2<a<5/2). At each fixed finite ell,

    P(C_k | past) ~ [2b/(sqrt(pi) h^up(ell))] k^(-(a-1/2)).      (7)

Let D=2k on C_k and D=0 on a gluing event. For every p>0, the tail comparison with a p-series gives

    E[D^p | past] < infinity  iff  p < a-3/2.                 (8)

Proof: the summands for large k are between two positive constants times k^(p-a+1/2). Their sum converges exactly when p-a+1/2<-1. Finitely many initial k do not affect convergence; equality gives logarithmic divergence. This is conditional on each finite history, not a uniform-in-ell asymptotic assertion. In particular **even the conditional first moment of a newly revealed face degree is infinite for every a in [2,5/2)**. The mean of nu for a>2 should not be confused with that different discovery distribution.

This excludes the simplest proposed argument based on the expected d^2 cost of replacing every discovery by a cyclic network: its one-step distortion expectation is already infinite. It does not exclude a tailored random flow that assigns very small currents to costly faces, and infinite expectation by itself does not imply almost-sure infinite energy.

Face degrees are also unbounded almost surely, not just allowed by the weight support. For fixed k>=2 with q_k>0, h^up is increasing since h^up(r+1)-h^up(r)=h^down(r)>0. Hence at every active peeling step P(C_k|past)>=nu(k-1)>0. Iterated conditional expectation bounds the probability of avoiding C_k for r consecutive steps, after any deterministic step N, by (1-nu(k-1))^r. Let r tend to infinity; that avoidance probability is zero. Taking a countable union over N shows C_k occurs infinitely often almost surely. Each C_k discovers a distinct face. Finally take the countable intersection over the unbounded set of k with q_k>0. Thus there are infinitely many faces of arbitrarily large degree for every requested source type. This conclusion uses the genuine Boltzmann peeling law.

## 7. Computation, formalization and hostile audit

`star_mesh_checks.py` completed the following finite checks, saved in `star_mesh_checks.json`:

- Exact Fraction arithmetic for 19 degrees d=2,...,20 verifies (4), the minimum clique-current formula, divergence preservation and the energy inequality for arbitrary currents including circulations.
- Nine cosine-mode examples d=2,3,4,8,16,32,64,128,256 verify the distortion formula numerically. At d=256 the ratio is about 3320.2592, already excluding any fixed comparison constant.
- Four connected finite multigraphs, including loops and parallel edges, independently construct H's Laplacian, compute its Schur complement, and compare (1). Maximum numerical entry discrepancy is below 9e-16. Midpoint-to-midpoint effective resistances agree within 1e-10. All weighted degrees satisfy (2).

These are algebra and network tests, not simulations of the Boltzmann map and not numerical evidence for C0059 transience.

`StarMeshCheck.lean` proves the finite pair-variance and star-mesh identities over the rationals, with arbitrary finite index sets. The final `lake env lean <full problem-folder path>/StarMeshCheck.lean` run from ~/lean_verify exited 0; transcript in `star_mesh_lean.log`. It used a 3600-second timeout, narrow Mathlib imports, no sorry and no native_decide. An initial attempt failed to factor constants out of finite sums; that tactic issue was corrected before the successful kernel check. The probability, infinite-network and planar-limit arguments are not Lean formalizations.

Hostile-referee checklist:

- A dual loop has two incidence ports; repeated midpoint entries are counted with multiplicity, not treated as distinct physical vertices.
- Half-edge conductance is 2, not 1. Clique conductance is 2/d, not 1/d or 1.
- Weighted-degree bound is not a combinatorial-degree bound, and K is not asserted planar.
- Infinite elimination is justified by compact-support variational identities and local current conversion, not by an unbounded infinite-matrix inverse.
- All Kirchhoff identities hold locally at finite-degree vertices; no unproved limiting current is assumed.
- The root source is moved along a finite-resistance edge explicitly.
- The medial graph is a local limit rooted at a uniform medial vertex after the finite root identification. The recurrence theorem is cited with its bounded-degree hypothesis checked.
- The d^2 loss is attained by a concrete finite mode, not merely an overly pessimistic estimate.
- Both comparison directions and both independence failures are stated explicitly.
- Neither a uniformly bounded-face map nor an independent long-range percolation graph is claimed to satisfy the requested heavy-tail Boltzmann law.
- The conditional discovery distribution (7) is not the bare perimeter-increment law. Its moment threshold is a-3/2, and all statements about divergent moments are kept separate from almost-sure energy claims.
- Conditioning on the full embedded medial map makes its assigned degree weights deterministic, not an iid common-law sample on a fixed graph. No false conditional-dependence argument is used.

## Remaining gap after the second attempt

C0059 is now equivalently a transience problem for (1), a correlated face-clique network of total conductance at most four over an almost-surely recurrent medial graph. To prove transience, establish a finite-energy unit flow in this exact kernel, or a lower comparison to a transient network with verified geometry and conductances. To disprove it, establish recurrence of K for an actual allowed q; recurrence of the correlated dominating W would suffice, but has not been shown. The exponent a alone has not been converted into either of these estimates.

Verdict: PARTIAL. No complete proof, counterexample under the Boltzmann law, or matching literature solution was obtained.
