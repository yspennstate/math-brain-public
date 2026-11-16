PROVED (replay_all.py): T_N>=0 for the entire T104 5+1 class for every integer N>=7. The certificate also proves the formal target nonnegative for every real q=N-6>=1 and proves T_infinity>=0. Both full inherited replays and every new proof stage passed. Zero OPEN leaves remain in this class. No counterexample exists in this class.

PROVED (replay_all.py): More explicitly, let the graph have symmetric nonnegative edge weights of total weight one, one connected five-vertex component carrying the largest Laplacian eigenvalue lambda with multiplicity exactly two, and N-5 isolated vertices. Put H_N=I-J/N, G=lambda H_N-L and Pi equal to the orthogonal projector onto the top eigenspace. For every N>=7 the following quantity satisfies T_N>=0:

    X1=2(lambda tr G-tr(G^2)),
    X2=2N/(N-2) sum_ij Pi_ij G_ij^2,
    X3=(1-lambda)/(N-2)
          [2tr G-2N/(N-2) sum_i Pi_ii G_ii],
    2S5=2 sum_(i<j) omega_ij
          (Pi_ii+Pi_jj-2Pi_ij)(G_ii+G_jj-2G_ij),
    T_N=X1+X2+X3-2S5.

PROVED (replay_all.py): The complete region ledger is:

| Region | Exact replay |
|---|---|
| Connected endpoint with 0<r<=3/25 | Inherited verify_allN_ratio.py, with its exact moment and frame premises |
| Connected endpoint with a<=129/250, and larger ratio-dependent ceilings | Inherited prior_scale.py, verify_allN_cells.py, verify_extensions.py and verify_summary.py |
| Remaining connected zero-edge endpoints | Full canonical partition, three compactified controls or signed exclusions; verify_new.py |
| Corner and the nine equality limits | local_uniform.py and exact interval pullbacks in verify_new.py |
| Disconnected radial endpoints | Inherited prior_four.py, prior_triangles.py and verify_boundary.py, replayed by verify_new.py |
| Every admissible smaller scale on each frame and ratio | Inherited verify_algebra.py exact all-N radial identity |

PROVED (verify_target.py): Each six-dimensional leaf is extended over the entire closed interval 0<=u<=1/2. Thus the six-dimensional coordinate volume is 1152, and its compactified seven-dimensional product volume is 576. These are chart volumes, not graph probabilities or volumes in physical matrix coordinates.

PROVED (inventory.py): The requested non-all-N positivity frontier consists of 250 STRAT10 leaves, 48 STRAT11 overlay leaves, 7,702 STRAT12 leaves and 366 STRAT13 leaves: 8,366 total. There are also 17 STRAT13 collar leaves and the independent STRAT11 corner ball at its fifteen permutations. The existing all-N positives number 24,458 from STRAT10 and 101 from STRAT11. All leaf identities and rational boxes are listed in inventory.json.

PROVED (domain_audit.py): An additional audit is necessary because N=6 exclusions may use stronger ratio and scale premises. Of 20,277 excluded leaves, 19,273 transfer under the weaker all-N premises. The other 1,004 (nine STRAT10 scale exclusions and 995 STRAT12 exclusions) require new positivity or exclusion certificates. They are listed individually in domain_audit.json. The current discovery bank therefore targets 9,370 boxes.

PROVED (verify_target.py): In the shared chart write V_i, R=VV^T, M=V^TV, tau=tr(M), Delta=det(M), D=20t-tau and Qn=V adj(M) V^T. Put

    V1=(v1,z1), V2=(v2,z2),
    V3=(1-t-v1-v2,-z-z1-z2), V4=(t,0), V5=(-1,z).

PROVED (inherited verify_domain.py, replay_all.py): Every connected zero-edge endpoint has a canonical representative in

    [1,4] x [-1,0] x [-4,4] x [-1,1/2] x [-4,4] x [0,4],
    S=2R/D, lambda=10t/D, omega_ij=2(t+R_ij)/D, Q_S=Qn/Delta.

PROVED (verify_target.py): Define the following exact chart polynomials:

    Pi_n = Delta(5I-J)-5Qn,
    F2 = sum_ij (Pi_n)_ij R_ij^2,
    F1 = sum_i (Pi_n)_ii R_ii,
    E = sum_(i<j) (t+R_ij)
          (2Delta-(Qn)_ii-(Qn)_jj+2(Qn)_ij)
          (R_ii+R_jj-2R_ij),
    A = 10Delta(40t tau-8 tr(R^2))-80E,
    B = 16F2, Z=D-10t.

PROVED (verify_target.py): The exact quadratic C_N(q)=c0+c1 q+c2 q^2, q=N-6, has coefficients

    c0 = 16A+24B+Z(3920t Delta-160D Delta-48F1),
    c1 = 8A+10B+Z(1720t Delta-40D Delta-8F1),
    c2 = A+B+200Zt Delta.

PROVED (verify_target.py, verify_padding.py, inherited STRAT14/verify_targets.py):

    C_N(q)=10(q+4)^2 D^2 Delta T_N,
    T6=c0/(160D^2 Delta), C_N(-1)=2Cface.

PROVED (inherited verify_domain.py): D>0 and Delta>0 at every feasible rank-two normalized chart point, so these normalizations preserve signs.

PROVED (verify_target.py): target.json also records every expanded integer coefficient. For u=1/(q+1),

    H(u)=u^2 C_N(1/u-1)
        =c2+(c1-2c2)u+(c0-c1+c2)u^2.

PROVED (verify_target.py): Its degree-two Bernstein controls on [0,1/2] are c2, (c1+2c2)/4, and (c0+c1+c2)/4. The new certificates check the three positive-scaled targets c2/8, (c1+2c2)/8, and (c0+c1+c2)/8 independently with nonnegative rational Farkas multipliers. This proves the stronger statement for every real q>=1 whenever all three sign certificates hold. It includes u=0: T_infinity=c2/(10D^2 Delta). No interpolation over integer N is needed.

PROVED (verify_target.py): A second algebraic derivation gives the same sign implication directly:

    C_N(q)=C_N(1)+(q-1)C_N'(1)+(q-1)^2 c2.

PROVED (verify_target.py): Thus the three targets are precisely the shifted nonnegative power coefficients, as well as positive multiples of the compactified Bernstein controls.

PROVED (exact_bernstein.py, verify_new.py): If the three leaf residuals are p_j-sum_k lambda_jk g_k>0 for p=(C(1),C'(1),c2)/8, their extended multiplier is

    Lambda_k(q)=lambda_0k+(q-1)lambda_1k+(q-1)^2 lambda_2k >=0.

PROVED (verify_target.py): This combines the saved six-variable Bernstein certificates into an exact Farkas certificate over the extended variables for every real q>=1. In the u chart it is the corresponding Bernstein convex combination, with controls p2,p1/4,p0/4. Every exclusion is independent of q. Nonnegative products of edge or row constraints, when saved, are treated as additional nonnegative g_k. No seventh-dimensional numerical sampling or integer interpolation enters the proof.

PROVED (verify_padding.py, local_uniform.py): Set S to the physical rank-two five-vertex gap matrix, Pi=I-J/5-Q_S, lambda=(2+tr S)/4, K=sum_ij Pi_ij S_ij^2 and d=sum_i Pi_ii degree_i-lambda. Then

    T_N = T_infinity + Bp/(N-2) + Ep/(N-2)^2,
    Bp=4K+(1-lambda)(2d-4), Ep=4(1-lambda)d.

PROVED (local_uniform.py): The three physical Bernstein controls on 0<=1/(N-2)<=1/5 are T_infinity, T_infinity+Bp/10, and T_7. All 384 signed Farkas identities per equality chart (768 total), the Gram determinant SOS and the rational polynomial remainder bounds pass exactly. Physical chart coordinates h and orthogonal bases are those of STRAT13/collar_algebra.py. The uniform estimates are:

| Equality type | Linear norm constant | Remainder constant | Radius in ||h||_1 | Matrix ball radius | Bound for all real N>=7, including infinity |
|---|---:|---:|---:|---:|---|
| Two disjoint 1/2-edges and an isolate | 1/6 | 8 | 1/100 | 1/4000 | T_N >= ||S-S_P||_max/24 |
| Balanced 1/3-triangle and two isolates | 1/6 | 25 | 1/300 | 1/12900 | T_N >= ||S-S_P||_max/24 |

PROVED (local_uniform.py, verify_new.py): The chart bound is T_N>=||h||_1/12. Matrix extraction factors are 40 and 43; the forward factor is 2 in both cases. All constants and radii are rational and remain positive at infinity. The estimates hold at every vertex permutation, cover the STRAT11 corner ball, and include the nine STRAT13 equality centers (nodes 12091,12407,14175,15603,15773,19750,20736,21058,21550). Exact coefficients and left inverses are in local_uniform.json. All 17 inherited collar pullbacks passed the independent replay.

PROVED (local_uniform.py): For each of the three physical controls F_j, write F_j=L_j+R_j and each active weight as omega_i=g_i+R_i. The signed multiplier rows mu_sigma>=0 satisfy L_j=mu_sigma g+(1/6)sigma.h. The polynomial envelopes, including weight curvature, give

    |R_j|+sum_i mu_i^max |R_i| <= M ||h||_1^2,
    F_j >= ||h||_1/6-M||h||_1^2 >= ||h||_1/12.

PROVED (local_uniform.py): This uses actual nonnegative weights, not feasibility of their linearizations. Each homogeneous remainder of degree d is bounded by max_alpha(|p_alpha|/multinomial(d,alpha))||h||_1^d; the Gram determinant has its inherited exact sum-of-squares lower bound. Bernstein convex combination gives the same bound for all N>=7 and at infinity.

PROVED (unchanged STRAT14/replay_all.py and STRAT13/replay_all.py, invoked by replay_all.py): both full inherited replays passed. NUMERICAL elapsed 698.689172 seconds for STRAT14 and 1364.214888 seconds for STRAT13. The additional all-N ratio, cell, analytic and ceiling-summary premises also passed. Supplied source trees are pinned in source_hashes.json. replay_all.py runs byte-identical temporary copies of both complete replays; an operational runtime shim caps their pools at two without changing their programs or arithmetic.

PROVED (verify_new.py): All 9,370 input boxes are closed. Thirteen required refinement, producing eighteen positive leaves through five bisections. The new ledger has 9,289 positive leaves, 86 exclusions and 17 retained inherited collars. All 28,125 leaf residual certificates passed exact replay; the 25 unused partial-parent residuals were also checked. The complete canonical ledger is:

| Positive | Excluded | Collar | Split | OPEN |
|---:|---:|---:|---:|---:|
| 33,848 | 19,359 | 17 | 53,223 | 0 |

PROVED (verify_new.py, replay_all.py): verification.json records all exact volume sums, the local constants and all collar pullbacks. The total six-dimensional root volume is 1152. remaining_open_boxes.json contains an empty list. All 789 supplied files under STRAT14 and all 22 pinned new proof inputs are unchanged. source_hashes.json and proof_hashes.json pin the inputs. A separate stack traversal independently re-derived the same final counts and volume.

PROVED (replay_all.py): To replay from scratch, including byte-identical temporary copies of the complete STRAT14 and STRAT13 trees:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

PROVED (replay_all.py): All ten final stages passed. The first new-stage attempt correctly stopped on a module-name collision in spawned workers: it imported the old N=6 target and rejected its disagreement with a saved extended-target margin. The worker import path was fixed and check_spawn.py now checks it explicitly. No certificate data changed. The completed immutable inherited stages were retained after source-manifest checks; the corrected new stage was rerun in full with --resume. failed_replay_1.out and failed_replay_1.json preserve the rejected attempt. The default command above reruns every stage from scratch.

NUMERICAL: Recorded replay execution time, including the rejected attempt and successful retry, was 3452.320961 seconds (57 minutes 32.32 seconds). The successful new certificate stage took 1309.644491 seconds (21 minutes 49.64 seconds). Inherited full replays took 698.689172 and 1364.214888 seconds. Wall time across the replay and import correction was approximately 3707.08 seconds. replay_summary.json, replay_all.out and verification.json retain the measurements and PASS receipts.

NUMERICAL / operational: Discovery used two workers and single-thread numerical libraries; at most four compute workers overlapped during the complete task. New discovery's conservative two-worker-plus-parent memory bound was 993,910,784 bytes, new exact replay's was 814,129,152 bytes, and the STRAT14 replay's was 640,212,992 bytes. These include their respective bookkeeping allowances. Largest recorded refinement-process peak was 431,964,160 bytes. The sandbox denied ps, so a separate whole-session aggregate RSS sample is unavailable; these are per-phase bounds. No subagents, language-model workers, network calls, accelerated mode or unrelated systems were used. Shared mesh/checklist writes were denied; all new writes stayed in STRAT15 or temporary copies.

OPEN: The broader statement about every disconnected graph with components of size at most five does not follow just from this class and STRAT7 padding. STRAT7/RESULT.md explicitly limits its padding theorem to adding isolates. After removing the general S5=0 class, the combinations still lacking a complete proof from these results are:

- A four-vertex double carrier with lower nontrivial components other than a single edge; or a five-vertex double carrier with any nontrivial lower component.
- Split simple top carriers of sizes 2+3, 2+4 or 3+3 with an additional nontrivial lower component.
- Split simple top carriers of sizes 2+5, 3+4, 3+5, 4+4, 4+5 or 5+5, with or without lower components.

PROVED inherited scope (STRAT7/replay.py, as recorded in STRAT7/RESULT.md): a triangle double carrier and two edge carriers are covered with arbitrary lower components by S5=0. The four-vertex double carrier with at most one lower edge, and the split carrier pairs 2+3, 2+4 and 3+3 without further nontrivial components, are covered after adding arbitrary isolates. The new theorem adds the five-vertex double carrier with isolates only. No closure of the remaining combinations is asserted. The full STRAT7 replay is not rerun here; its smaller-carrier endpoint certificates needed by the new proof are replayed by verify_new.py.

Task: “STRAT15: close the T104 5+1 class for every N >= 7” — received 2026-11-13 12:44 +04 (workspace launch).
