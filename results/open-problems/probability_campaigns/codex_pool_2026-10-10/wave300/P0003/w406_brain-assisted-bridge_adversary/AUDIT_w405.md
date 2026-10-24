# w405 adversarial audit, 2026-10-10

Independent cycle-mode derivation: INDEPENDENT_OBSTRUCTION.md was saved before w405's proof was read. The paired proof reviewed here is ~/brain_workers/w405/ATTEMPT.md, sections L1, L2, R1, C1 and the unsuccessful closing attempt. Referee for new claims remains w407; this audit does not replace that check.

Target fidelity: the original P0003 record and Grimmett Question 2.2 ask about uniform fixed-length rooted walks with free endpoint. The Duminil-Copin--Smirnov chordal fugacity formulation in w405's lane is related, but it is a different ensemble. Thus the elementary KEEP verdicts below do not imply that C1 would solve the recorded P0003. An ensemble and endpoint-conditioning transfer theorem is missing even if T/B/C were established; see ENSEMBLE_GAP.md. This is a minimal missing premise for the attempted application, not a flaw in L2.

L1: KEEP under its stated finite-graph assumptions. Deleting both vertices in A and edges whose embedded traces meet A makes surviving paths exactly the avoiding paths. Preserving weights supplies the ratio identity. Positive numerator is required for the conditional law; the probability identity remains true for numerator zero. No multiplication of conditional bounds is involved.

L2: KEEP as an elementary conditional lemma. Let d_n=dist(K_n,A), d=dist(K,A). The map K -> dist(K,A) is 1-Lipschitz in Hausdorff distance. For each fixed m, write E_(n,m)={K_n avoids A_m}. The two inclusions give {d_n>R_m} subset E_(n,m) subset {d_n>r_m}. Thus

    P(d>R_m) <= liminf_n P(E_(n,m))=q_m
             <= limsup_n P(d_n>=r_m) <= P(d>=r_m).

The first inequality uses the open-set direction of Portmanteau; the last uses the closed-set direction. For arbitrary positive radii tending to zero, both endpoint probabilities tend to P(d>0), even if P(d=0)>0. Compactness and closedness make d>0 exactly avoidance. Consequently q=P(K avoids A). This check does not require nested buffers, atom-free boundary distances, uniformity in m, or interchange of the two limits.

Minimal premise checks: positivity of the inner buffer radius matters. If r_m=0 and A_m=A={0} in S=[0,1], K_n={1/n} tends to K={0}, all q_m=1, and limiting avoidance is 0. Limit order matters even with valid positive buffers: for A_m=[0,1/(2m)] and the same K_n, every fixed-m avoidance limit is 0, while the diagonal event n=m has probability 1. Neither example refutes L2, which excludes the first and does not take the diagonal in the second.

R1: KEEP. In the displayed polygonal curve, y is strictly positive whenever x is in [-1/4,1/4]; the limiting horizontal segment touches the closed obstacle. Uniform distance is at most 1/n. This is a continuity counterexample for deterministic simple curves, not evidence against the SAW conjecture.

C1: KEEP AS CONDITIONAL SKETCH ONLY, with source-hypothesis confirmation and the simple-trace measurability detail still reserved for the referee. T (curve tightness and simplicity), B (all fixed-buffer conformal partition-ratio limits), and C (boundary derivative convergence for the actual chosen buffers) remain explicit assumptions. L2 does not establish any of these. In particular it proves a limit-transfer step only after the hard partition ratios are supplied.

The attempted use of the vertex parafermionic identity to close B is correctly marked unsuccessful by w405. The independent six-edge cycle mode strengthens that diagnosis: even bounded solutions of the vertex identity with identical boundary values need not be unique or have a mesh-independent modulus of continuity. It does not show that the genuine SAW observable contains the mode.

Math-brain assistance: a narrow read-only retrieval returned the Portmanteau card claim_fde5f7c46c3b42858fe57a153974903d. Its open/closed inequalities apply on the scalar metric space of distances, not as an equality for every raw avoidance event. Its equality clause requires zero boundary mass; L2 avoids using that clause by positive buffers and the stated order of limits. See bridge_retrieval.json for the complete returned card and candidate scope.

NEXT: Establish the critical SAW fixed-buffer endpoint partition-ratio limit B, or a global regularity estimate that genuinely controls the normalized path-sum; keep T and C explicit.
