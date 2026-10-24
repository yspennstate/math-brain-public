The deliverable is an exact obstruction to a stronger observable compactness bridge. P0003 remains unproved, with current openness UNKNOWN. The primary source of the assigned fixed-length question is Grimmett arXiv:2205.07318v1, Question 2.2, page 3; the chordal critical-fugacity source is a related route, not a proved equivalent formulation.

Read ATTEMPT.md for the self-contained mathematics, SOURCE_STATUS.json for source scope and uncertainty, CLAIMS.jsonl for the seven exact claim rows, and MEASUREMENTS.json with verify_obstruction.py for the bounded reproduction. The DRAFT has six cards and seven justified relations in bundle_001.json, with complete supporting ends in RELATIONS.jsonl. Its submission, review, ingestion, and retrieval states are tracked separately in BRAIN_LIFECYCLE.json.

Referee w404: please independently check these four points before a mathematical KEEP:

1. Boundary contributions turn the vertex identity into BJ=-b; compatibility is zero total prescribed flux per component, and the affine dimension is |E|-|V|+c, including isolated vertices.
2. The six-edge field H=delta/(v_{j+1}-v_j) cancels at every face vertex and vanishes at every boundary midpoint. Constant boundary data 1 give F=1+H with sup norm 2.
3. The value difference 1 at midpoint separation sqrt(3)delta/2 rules out locally uniform convergence to any continuous function near the limiting face center. These arbitrary fields are not asserted to be actual SAW observables.
4. The f bounded-face cycle vectors span the homogeneous kernel; f added linear tests suffice and fewer cannot. The existence argument uses a=-(C^T C)^(-1)C^T J_0. These extra tests are not asserted for the path sum.

w404 already saved an independent KEEP for the abstract homogeneous kernel (CLAIMS.jsonl row S1.P0003.w402.002) at ~/brain_workers/w404/REVIEW_PACKET.md, line 7 as initially read. That receipt applies only to its stated finite-graph result. The expanded boundary solvability, explicit oscillation construction, and minimal-constraint result require their own verdicts. No account or served-model setting is inferred from worker IDs, and no two-account consensus is claimed.

The exact experiment passed on meshes 1/2, 1/3, 1/5, 1/9, 1/17: 2,448 vertex equations and 216 boundary values had zero errors. Sup norm was 2, oscillation 1. A wrong-sign perturbation broke two equations on every mesh, while constant fields had zero oscillation. Rational incidence nullities were 1, 7, 19. This is neither a formal proof receipt nor a general proof-audit benchmark.

The single hardest gap is a mesh-independent modulus and orientation consistency for the actual normalized observable. A target proof additionally needs the curve-limit arguments and a justified passage to the assigned fixed-length free-endpoint law. No unsupported independence or multiplication of conditional bounds is used.

Hook proposal and review patches are local: HOOK_PROPOSAL.jsonl and patches/02_math_hook.diff. The worker-folder restriction keeps that proposal out of the shared hooks directory until a permitted reviewer applies it. Its fire case is claiming compactness from the local equation, sup bound and boundary trace; its silent case is using the identity only for the connective constant.

NEXT: w404 independently derive the six-edge mode and minimal face-constraint lemma and record KEEP/FIX/DROP per claim; the validating coordinator may integrate only the appropriately reviewed draft material.

Checkpoint: w404 now also independently KEEPS the six-edge mode/noncompactness construction (REVIEW_PACKET.md:8 and P0003-W404-REVIEW-402-02) and Lemma 4 (REVIEW_PACKET.md:9). The full review request and w403 proof-path relay were delivered as msg-6b24c92d83, recipient active. Expanded boundary-flux compatibility and final draft card/edge audit remain pending.
