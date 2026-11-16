PROVED (replay_all.py): T>=0 for every connected five-vertex graph at D=2, after the standard normalization of total edge weight to one. All 5,272 original STRAT8 OPEN leaves are closed. All 17 full-replay stages passed, including the unchanged STRAT8 replay, every new certificate and the required STRAT4-6 premises. No counterexample exists on this stratum. Zero OPEN leaves remain.

PROVED (verify_targets.py): Let C_N(q) denote the STRAT10 polynomial, with q=N-6. On the shared chart,

    C_N(-1)=2 Cface,
    C_N(q)=10(N-2)^2 D^2 Delta T_N,
    T5=Cface/(45 D^2 Delta),
    T6=C_N(0)/(160 D^2 Delta).

PROVED (verify_targets.py): These are coefficient identities, not numerical agreement. Cface has 1,254 integer terms and coefficient gcd 80. The new Bernstein target is P=Cface/80, so T5=16P/(9D^2 Delta). Equivalently T5-T6=(32Cface-9C_N(0))/(1440D^2 Delta). The five-vertex target is exactly the all-N polynomial at N=5, with its appropriate normalization; positivity for N=6 by itself gives no sign implication for N=5.

PROVED (verify_targets.py, STRAT8/zero_face.py, STRAT8/verify_domain.py): The Gram chart, canonical root, zero-edge normalization, graph weights, projector identities, orientation, ordering, degree, spectral, rank and connectedness polynomials transfer unchanged. The centered translation, rational Bernstein conversion, signed Farkas residual construction, and quadratic-field arithmetic transfer unchanged as algorithms. The physical chart bases, coordinate extraction, and removal of eigenframe rotation transfer unchanged. The target, positivity multipliers, tangent bounds and remainder constants require new computations. STRAT10's stronger residual premises r>3/20 and a>14/25 cannot be imposed here. The new data use r>3/25 and a>103/200. Exclusion certificates using only common constraints can transfer, but no inherited N=6 sign certificate is accepted without checking it against the n=5 polynomials.

PROVED (verify_targets.py): In coordinate order (t,v1,z1,v2,z2,z), put

    V1=(v1,z1), V2=(v2,z2),
    V3=(1-t-v1-v2,-z-z1-z2), V4=(t,0), V5=(-1,z),
    M=V^T V, R=VV^T, tau=tr M, Delta=det M, D=20t-tau.

PROVED (STRAT8/zero_face.py, STRAT8/verify_domain.py): At a feasible point S=2R/D, lambda=10t/D, omega_ij=2(t+R_ij)/D and Q=V adj(M)V^T/Delta. Every zero-edge graph has a canonical chart in

    [1,4] x [-1,0] x [-4,4] x [-1,1/2] x [-4,4] x [0,4].

PROVED (verify_targets.py): The new constraints are orientation, the two order inequalities, x3>=-1, the five row-degree bounds, the nine nonzero edge polynomials, two diagonal spectral bounds, connected=det(5tI-M), rank=Delta, and ratio=784Delta-75tau^2. Strict constraints are safely relaxed to weak inequalities inside the Farkas multipliers. On any box where 103D-200tau>=0 is proved throughout, the residual premise a>103/200 also implies

    40000(tau^2-4Delta)-(103D-200tau)^2 >= 0.

PROVED (verify_targets.py): The historical key scale14 in the reused certificate interface denotes this n=5 polynomial, with threshold 103/200. It is omitted whenever its whole-box guard is not proved. All stronger moment filters defining the original STRAT6 residual are omitted. The new cover therefore proves a larger endpoint region than the requested residual.

PROVED (verify_local.py): The local physical coordinates are h=(x,y,k,p,q,v,z), with

    B=(U+pX+qY, W+vX+zY),
    K=[(1+x)/nu, k/nu; k/nu, (1+y)/nw],
    S=B K B^T, Q=B(B^T B)^(-1)B^T,
    lambda=(2+tr S)/4, omega_ij=lambda/5+S_ij,
    nu=U.U, nw=W.W.

PROVED (verify_local.py): The two orthogonal zero-sum bases are

    edges: U=(-4,1,1,1,1), W=(0,1,-1,-1,1),
           X=(0,1,1,-1,-1), Y=(0,1,-1,1,-1);
    triangle: U=(3,3,-2,-2,-2), W=(1,-1,0,0,0),
              X=(0,0,1,-1,0), Y=(0,0,1,1,-2).

PROVED (verify_local.py): For two edges the linear term is L=(-16x+2y)/15. In active edge order (01,02,03,04,12,13,24,34), its positive multipliers are (2,2,2,2,1/3,1/3,1/3,1/3). For the triangle, L=(46x-242y)/135. In active edge order (01,02,03,04,12,13,14), its positive multipliers are (136/27,128/81,128/81,128/81,128/81,128/81,128/81). local_certificates.json contains both exact quadratic expansions, every derivative matrix, left inverse J and remainder envelope.

PROVED (verify_local.py): For all 128 sign vectors sigma in each chart, mu_sigma=mu-c sigma^T J is nonnegative and satisfies mu_sigma A=DL-c sigma^T, with c=1/10 for edges and c=1/6 for the triangle. On |h_i|<=1/100 the Gram determinant has the exact lower bound

    det(B^T B)=nu*nw+nw*nx*p^2+nw*ny*q^2
       +nu*nx*v^2+nu*ny*z^2+nx*ny*(pz-qv)^2 >= nu*nw.

PROVED (verify_local.py): Exact quotient-Hessian bounds give

    |R_T|+sum mu_i^max |R_omega_i| <= M ||h||_1^2,
    M=26 for edges, M=50 for the triangle.

PROVED (verify_local.py): A second derivation bounds the polynomial remainder after canceling the linear term and independently verifies these same constants. Substituting the actual nonnegative weights into the signed identities gives the following bounds; linearized feasibility is not assumed.

| Type | Bound in physical chart | Chart radius |
|---|---|---|
| Two edges | T5 >= ||h||_1/20 | ||h||_1 <= 1/520 |
| Triangle | T5 >= ||h||_1/12 | ||h||_1 <= 1/600 |

PROVED (verify_local.py): Coefficient extraction recovers this chart from every nearby rank-two zero-sum matrix. The extraction factors ||h||_1/||S-S_P||_max are bounded by 40 and 43 respectively; conversely ||S-S_P||_max<=2||h||_1. Thus the explicit closed matrix balls satisfy

| Type | Bound | Radius in maximum absolute entry norm |
|---|---|---|
| Two disjoint 1/2-edges and an isolate | T5 >= ||S-S_P||_max/40 | 1/20800 |
| Balanced 1/3-triangle and two isolates | T5 >= ||S-S_P||_max/24 | 1/25800 |

PROVED (verify_local.py): The bounds are strict away from the disconnected center. They apply at all fifteen two-edge centers and all ten triangle centers by permutation. The specified STRAT11 corner r=a=1 is a two-edge physical center. Free eigenframe rotation changes no physical matrix and supplies no additional zero type.

PROVED (verify_limits.py): The following nine exact canonical centers lie in original STRAT8 OPEN leaves. Write s=sqrt(5), q=sqrt(15), choosing positive square roots.

| STRAT8 node | Exact center (t,v1,z1,v2,z2,z) | Type |
|---|---|---|
| 12437 | (3/2, -1, 1/2*s, -1, -s, 1/2*s) | edges |
| 12643 | (4, -1, 1/3*q, -1, -q, 1/3*q) | triangle |
| 13871 | (4, -1, s, -1, -s, s) | edges |
| 14683 | (4, -1, 1/3*q, -1, 1/3*q, 1/3*q) | triangle |
| 14814 | (4, -1, -s, -1, -s, s) | edges |
| 17328 | (4, -1, -1/3*q, -1, -1/3*q, q) | triangle |
| 17952 | (3/2, -1, -s, -1, 1/2*s, 1/2*s) | edges |
| 18124 | (4, -1, -q, -1, 1/3*q, 1/3*q) | triangle |
| 18548 | (4, -1, -s, -1, s, s) | edges |

PROVED (verify_limits.py): At every center P=0, all weak domain constraints are nonnegative, Delta>0 and connected=0. Their physical weights are exactly the two types listed above. Thus no strictly positive P-sum lambda*g or strictly positive -sum lambda*g can hold on a closed box containing a center, even if products of nonnegative constraints are allowed. These are disconnected equality points, not counterexamples.

PROVED (verify_jets.py): chart_expansions.json records the full exact degree-two expansions of T5, P and all active constraints at every center. All operations and sign comparisons use rational pairs A+B*sqrt(d), never floating square roots.

PROVED (verify_partition.py): The final bank certificates.json has 8,227 positivity leaves, 3,729 exclusions and 14 plane-chart collar leaves, with 6,698 bisections and maximum additional depth 73. It has no OPEN leaf. Every terminal decision passed both exact acceptance and the independent full partition replay. A positivity leaf checks P-sum lambda*g>0. An exclusion checks -sum lambda*g>0. Each collar checks an exact interval pullback into the proved physical chart radius.

PROVED (replay_all.py, verify_partition.py): The final canonical-root ledger is 32,929 positive leaves, 13,937 exclusions, 14 collars, 46,879 splits and zero OPEN leaves. The root coordinate volume is 1152. These counts and volumes describe chart boxes, not counts or volumes of feasible graphs.

PROVED (verify_partition.py, verify_local.py, verify_targets.py, verify_limits.py): The nine displayed centers are all target zeros and all obstructions to the requested strictly signed ambient forms on the feasible residual closure in the original OPEN boxes. Outside their collars the finite subdivision supplies a strict positivity or exclusion certificate. Here feasible residual closure means nonnegative edge weights and the weak inequalities r>=3/25 and a>=103/200, in the original OPEN boxes; rank stays positive. A strict positivity leaf cannot contain a target zero, and an exclusion cannot contain a point satisfying its weak premises. A collar zero must be its exact physical center. The coordinate recovery identities in verify_targets.py show uniqueness of its canonical chart when z>0, as at all nine centers. No enumeration of polynomial zeros on infeasible portions of the raw boxes is asserted.

PROVED (verify_radial.py, prior/STRAT4/exact_audit.py): If u,w are orthonormal zero-sum vectors, b=ar and lambda=(2+a+b)/4, set

    D_ij=-1-r-20(u_i u_j+r w_i w_j),
    E=2/max(3-r,max_(i<j)D_ij).

PROVED (verify_radial.py): On this fixed frame and ratio the exact identity is

    T(a,ar)=a(1-a/E)L+(a/E)^2 T(E,rE),
    L=(14/9)[A+rB+(1+r)C-(1+r)/5] >= 7(1+r)/90 > 0,
    A=sum u_i^4, B=sum w_i^4, C=sum u_i^2 w_i^2.

PROVED (prior/STRAT6/RESULT.md, verify_radial.py): The admissible scale interval is 0<a<=E. At E the carrier is disconnected or at least one edge weight is zero. Nonnegativity at E therefore proves nonnegativity at every smaller scale, strictly at every positive inward scale. This covers endpoints with multiple zero edges without any additional genericity hypothesis.

PROVED (replay_all.py): Full theorem: for every symmetric nonnegative system of five-vertex edge weights with sum_(i<j)omega_ij=1, connected carrier, and largest Laplacian eigenvalue lambda of multiplicity exactly D=2, the T104 quantity satisfies T>=0. More explicitly, let H=I-J/5, S=lambda H-L_G, where L_G is the Laplacian, Q the range projector of S, and Pi=H-Q. Then S has two positive eigenvalues a>=b>0, lambda=(2+a+b)/4, and

    X1=2(lambda tr S-tr(S^2)),
    X2=(10/3)sum_ij Pi_ij S_ij^2,
    X3=(1-lambda)/3 [2tr S-(10/3)sum_i Pi_ii S_ii],
    2S5=2sum_(i<j)omega_ij (Pi_ii+Pi_jj-2Pi_ij)
                              (S_ii+S_jj-2S_ij),
    T=X1+X2+X3-2S5 >= 0.

PROVED (replay_all.py): The complete proof combines the following exhaustive regions. All required original replay inputs have been copied locally under prior/; the supplied source trees are unchanged.

| Endpoint region | Proof and exact replay |
|---|---|
| Disconnected endpoint, any ratio | STRAT4: prior/STRAT4/isolated_certificate.py and exact_audit.py; the full symbolic reductions are also checked by verify_disconnected.py. The only equality types are the balanced triangle plus two isolates and two 1/2-edges plus an isolate. |
| Connected endpoint, 0<r<=3/25 | STRAT5: prior/STRAT5/verify_quartic_certificate.py quartic_ratio_matrices_3_25.json; its rank-one base is prior/STRAT4/rank_one_certificate.py, and moment premises are prior/STRAT5/verify_moments.py. |
| Connected endpoint, r>3/25 and a<=103/200 | STRAT5's a<=443/1000 cells and STRAT6's 176 cells: prior/STRAT5/verify_cells.py and prior/STRAT6/replay_all.py. |
| Connected endpoint, r>3/25 and a>103/200 | Original STRAT8 canonical partition, replayed unchanged, plus verify_partition.py and the local bounds in verify_local.py. This includes the entire requested residual and more. |
| Every smaller admissible scale on each frame and ratio | Exact radial identity verify_radial.py and the original STRAT6 reduction. |

PROVED (replay_all.py): The complete exact replay passed. Run from this folder:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

PROVED (replay_all.py): The driver first runs STRAT8 in a temporary byte-identical copy, then all new certificates, physical bounds, exact equality witnesses, jets and partition leaves, and then the prior certificates needed for the full theorem. It checks supplied source fingerprints and new proof-input fingerprints before and after. Mathematical signs use integers, Fraction or exact SymPy rationals. NumPy object arrays arrange exact integer tensor arithmetic; SciPy/HiGHS is used only during discovery. Exact replay needs Python, SymPy and NumPy.

NUMERICAL / operational: Discovery used two workers, one thread each, with measured conservative worker-plus-parent peak 759,480,320 bytes before bookkeeping allowance. No subagents, language-model workers, network calls, accelerated execution or trading processes were used. Shared mesh/checklist registration, claims and updates were denied by the read-only sandbox. All new writes are confined to this isolated STRAT14 workspace or temporary replay copies; no supplied source tree is edited.

PROVED (replay_all.py): All 597 files in the supplied STRAT8 and STRAT13 trees, all 150 prior snapshot files and every pinned new proof input are unchanged. replay_all.out records all stages; replay_summary.json records PASS for every stage. partition_verification.json records the exact combined ledger. remaining_open_boxes.json contains an empty list. source_hashes.json, prior_hashes.json and proof_hashes.json pin the inputs. No mathematical case remains OPEN in the connected five-vertex D=2 stratum.

PROVED (verify_partition.py): The new exact leaf volumes are positivity 18164166358976442012794499/302231454903657293676544, exclusion 35007585492480377682394953/604462909807314587353088, and collars 945/604462909807314587353088. Their sum is 30937023/262144, the entire original OPEN coordinate volume. The global volume remains 1152. A second independent stack traversal re-derived all counts and these volume sums after the full replay.

NUMERICAL: Complete replay time 606.217232 seconds (10 minutes 6.22 seconds); STRAT8 183.532537 seconds; new partition 404.851108 seconds. Conservative replay process-memory bound, including 128,000,000 bytes for bookkeeping, was 611,082,240 bytes. The maximum recorded discovery worker-plus-parent bound was 759,480,320 bytes; adding the same allowance gives 887,480,320 bytes, below the 2,500,000,000-byte cap. Individual process peaks are operating-system measurements; timings and RSS have no mathematical proof role. Discovery and partition replay used two workers, and all other replay stages were sequential.

Task: “STRAT14: close T104 connected n = 5, D = 2 (the STRAT8 residual)” — received 2026-11-13 11:52 +04 (workspace launch).
