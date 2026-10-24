# P0003: a boundary-preserving obstruction to an observable compactness bridge

Author: w402. Date: 2026-10-10. Referee: w404. Adversary: w403, given the statement first. This is an author proof of auxiliary results, not an independently checked proof or a solution of P0003. No novelty claim is made.

## Assigned target, related route, and sources

The exact P0003 source is Geoffrey Grimmett, [Selected problems in probability theory, arXiv:2205.07318v1](https://arxiv.org/pdf/2205.07318), Question 2.2, printed/PDF page 3. It asks whether a uniformly chosen n-step honeycomb SAW starting at the origin has an SLE(8/3) weak limit after a suitable rescaling. The endpoint is free. The question does not specify the scale, the SLE geometry/stopping rule, the parametrization, or the curve topology. Those details cannot be inferred as theorem assumptions from the secondary ledger. In particular, this session does not silently replace that question with the related chordal conjecture below.

Duminil-Copin and Smirnov, [arXiv:1007.0575v2](https://arxiv.org/pdf/1007.0575), section 4, Conjecture 1: sample honeycomb SAWs between distinct boundary marks in a proper simply connected plane domain, on mesh delta, with weights proportional to x_c^ell and x_c=(2+sqrt(2))^(-1/2). The predicted curve limit is chordal SLE(8/3). The source's ell counts visited vertices. Fixed-length uniform walks and a presumed n^(3/4) spatial scaling are different formulations and are not assumed here.

For this RELATED chordal route, a precise working formulation uses a bounded C^2 Jordan domain, connected inner approximations, endpoints approaching two distinct marks, and weak convergence of piecewise-linear traces modulo increasing reparametrization in the uniform curve metric. Smoothness and this topology are explicit restrictions/choices for this session; the observable paper's broader informal statement also mentions unbounded domains, for which its phrase about a largest finite approximation needs an exhaustion convention. For non-Jordan boundaries, Euclidean points alone may not specify the marked prime ends. Colliding endpoints and uniform convergence over arbitrary changing domains are not included. No equivalence to the assigned fixed-length question is proved. Conditioning critical weights on an exact length makes them uniform within that length class, but controlling this conditioning and the endpoint law in a scaling limit is an additional gap.

The observable is F_delta(z)=sum_gamma x_c^ell(gamma) exp(-i(5/8)W_gamma(a,z)). Lemma 1, equation (1), gives the exact relation

    L_v(F) := sum_{p adjacent to v} (p-v)F(p) = 0.

The authors explicitly warn in section 4 that this equation does not determine interior values from boundary data. Their explanation is a count of variables and equations. The results below give the exact kernel, an explicit perturbation with fixed full boundary trace, and a quantitative failure of compactness. They make the already-known obstruction checkable; they do not discover that obstruction for the first time.

Lawler--Schramm--Werner, [arXiv:math/0204277v2](https://arxiv.org/pdf/math/0204277), section 4.1, Prediction 1, explains the expected SLE identification. Neither historical paper certifies today's openness. SOURCE_STATUS.json records bounded current-source checks and their limits.

## Local setup

Let V be a finite set of honeycomb vertices of mesh delta. E consists of lattice edges with both ends in V. A boundary mid-edge has exactly one end in V; write this set as H. The domain contains all three incident mid-edges at every v in V. Prescribe a complex value g(h) for each h in H. Let c be the number of components of (V,E). All values are arbitrary complex fields here, not constrained to be actual SAW partition sums.

Orient each e=(u,v) in E, set d_e=v-u, p_e=(u+v)/2, and introduce J_e=(d_e/2)F(p_e). Nonzero d_e makes this an invertible change of variables. Use the incidence matrix B with +1 at the tail and -1 at the head. Then

    L_v(F) = (BJ)_v + b_v,
    b_v = sum_{h in H incident to v} (h-v)g(h).

### Lemma 1: exact solvability and boundary-preserving freedom

The prescribed boundary problem has a solution if and only if sum_{v in C} b_v=0 for each connected component C. When it has a solution its complex affine dimension is |E|-|V|+c. In particular any cycle gives a nonzero perturbation preserving every boundary value and every L_v.

Proof. The rows of B sum to zero on each component, so the stated compatibility is necessary. On a component with n vertices a spanning tree has a reduced incidence minor of determinant +1 or -1: remove a root row and repeatedly expand at a leaf. Thus rank(B)=|V|-c. Its image has precisely the c stated sum constraints, proving sufficiency. Rank-nullity and invertibility of F -> J prove the dimension. This includes isolated vertices, whose compatibility equation is b_v=0. For a connected plane graph Euler's formula identifies |E|-|V|+1 with the number of bounded faces. QED.

### Lemma 2: a six-edge mode

Take a complete interior hexagonal face with counterclockwise vertices v_0,...,v_5 and indices modulo 6. Define H_delta on its six edge midpoints by

    H_delta((v_j+v_{j+1})/2) = delta/(v_{j+1}-v_j),

and set it to zero at every other midpoint, including every boundary midpoint. Then |H_delta|=1 on its support, ||H_delta||_infinity=1, and L_v(H_delta)=0 at every vertex.

Proof. At v_j the outgoing face edge contributes (v_{j+1}-v_j)/2 times delta/(v_{j+1}-v_j)=delta/2. The incoming edge contributes -delta/2. The third edge has value zero. Every other vertex sees only zero values. Honeycomb edges have length delta, so the modulus assertion is exact. QED.

### Proposition 3: bounded fields with fixed nonzero boundary data need not be compact

Let delta_n tend to zero and choose simply connected honeycomb patches with a complete central face near a fixed interior point z_0, all contained in and converging to a fixed hexagonal domain. The fields

    F_n(p)=1+H_delta_n(p)

satisfy every vertex relation, have boundary value identically 1, obey ||F_n||_infinity<=2, and have no subsequence converging locally uniformly to a continuous function near z_0. The same interior construction can be placed in lattice approximations of a smooth domain; only a fixed interior neighborhood is needed.

Proof. The constant field 1 satisfies L_v=0 because the three displacement vectors at a honeycomb vertex sum to zero. Lemma 2 supplies the homogeneous perturbation. At one central-face vertex choose a face-edge midpoint p_n and the midpoint q_n of its third edge. Their distance is sqrt(3)delta_n/2. Since H(p_n) has modulus 1 and H(q_n)=0, |F_n(p_n)-F_n(q_n)|=1, while both midpoints tend to z_0. If sampled values of a subsequence approached a continuous f locally uniformly, their difference would be at most two uniform approximation errors plus |f(p_n)-f(q_n)|, tending to zero. This contradicts the exact difference 1. Hence any continuous interpolation agreeing at midpoints also has no locally uniform convergent subsequence. QED.

This defeats the auxiliary implication 'local relation + uniform bound + fixed full boundary trace => a continuous holomorphic scaling limit.' It also preserves any chosen boundary normalization F(b)=1 in this example. It does not defeat the claim that a scaling limit, if it exists with the needed mode consistency, is holomorphic.

### Lemma 4: the obstruction is minimal in a sharp algebraic sense

For a connected planar patch with f bounded faces, the homogeneous boundary kernel has dimension exactly f. Fewer than f additional complex linear conditions cannot make a compatible boundary problem unique. There is a set of f independent linear conditions that does make it unique.

Proof. Let c_i be the real signed incidence vector of the counterclockwise boundary of bounded face i. Each lies in ker B. They are independent: a linear combination vanishing on every edge forces equal coefficients across adjacent faces; take the exterior coefficient as zero and use connectedness of the planar dual. Euler's formula shows there are dim(ker B) such vectors, so they form a basis. Put C=[c_1 ... c_f]. If J is a homogeneous solution then J=C a. Requiring c_i^T J=0 for all i gives C^T C a=0. C has independent real columns, so C^T C is positive definite and a=0, also for complex a. Existence for compatible nonzero boundary data follows by taking any solution J_0 and adding C a with a=-(C^T C)^(-1)C^T J_0. Conversely fewer than f linear constraints leave a nonzero vector by rank-nullity. QED.

These additional cycle tests are an algebraic way of fixing the homogeneous ambiguity. No claim is made that actual SAW observables satisfy them or that they form a complete consistent discrete holomorphic scheme.

## Proof attempt toward P0003 and the single hardest gap

The attempted bridge starts from the exact critical fugacity and the exact local observable identity, then tries to obtain a compact family of normalized observables by boundary control. Lemmas 1-3 show exactly where that inference fails. Complete boundary data still leave face modes, and a sup bound still permits unit oscillation at separation O(delta). The six-face loop circulation sum_j (v_{j+1}-v_j)H(p_j)=6delta also tends to zero; a test of an unnormalized small contour error can miss the persistent oscillation.

The single hardest remaining piece in this lane is a modulus-of-continuity estimate, independent of the mesh, for the *actual* observable normalized by a nonvanishing boundary value, with limits independent of edge orientation. The positive path-sum representation and its winding correlations must provide something beyond the vertex equation and boundary values. No such estimate is proved here. Even if obtained, a full curve proof also needs tightness, control of explored slit domains, and justified transfer of the observable martingale to identify SLE. These are recorded as downstream requirements, not silently treated as completed.

In particular no multiplication of conditional crossing probabilities, independence assumption, or unproved martingale limit is used in the auxiliary proofs. The scar perceptron_proof_open_gaps_fleet_2026_07_12 is applied by naming this open piece separately from successful algebraic checks.

## Verification and review

The companion exact-arithmetic experiment checks the embedded coordinates, every vertex equation including the boundary, kernel ranks on small patches, and the persistent midpoint oscillation on decreasing meshes. It also includes a broken-sign control. It is a reproducibility check, not a formal theorem prover. No Lean/formal receipt is claimed. Subsequent independent verdicts by w404 KEEP the abstract kernel, six-edge mode/noncompactness counterexample, and minimal-constraint argument; expanded boundary-flux compatibility and full draft card/edge review remain pending. PEER_RECEIPTS.json records the precise scope.

Run completed: `python -X utf8 ~/brain_workers/w402/verify_obstruction.py`. Five meshes satisfied all 2,448 vertex equations and all 216 prescribed boundary values exactly, with sup norm 2 and oscillation 1. The broken-sign control failed at exactly two vertices on every mesh; constant fields had oscillation 0. Exact rational nullities were 1, 7, 19 on the three rank checks. CPU time was 1.0625 s; script wall time 1.076168 s. See MEASUREMENTS.json. These are checks of the stated fixtures, not a benchmark of general proof accuracy.
