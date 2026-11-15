OPEN — STRAT11, started 2026-11-13 09:26 +04.

OPEN: Task: “close the corner (r,a)=(1,1) of T104 5+1 region (11), N=6”. Read STRAT9/RESULT.md (11), STRAT10/RESULT.md and their formula, pressure-family, chart and covering implementations first. Neither source directory will be edited.

OPEN (coordination limitation): shared mesh hello, digest and claim all failed with “attempt to write a readonly database”; checklist working failed with PermissionError. A read-only SQLite inspection found no STRAT/codex_audit claims. No shared database or memory writes succeeded. Requested artifacts are confined to this task directory. No helpers, model workers, network calls or accelerated compute were started.

OPEN: Step 1 underway. Distinguish eigenframe coordinates, which contain a rotation redundancy at r=1, from coordinates for the rank-two gap matrix. The requested distance bound needs this distinction.

PROVED (step 1; verify_frame.py): exact eigenframe expansion through degree two saved in frame_expansion.json. With alpha=1-a and beta=1-r, L=11 alpha/10-beta/20. The eight active weight derivatives and beta>=0, 2alpha-beta>=0 are recorded. The pressure-family direction has L=11s/5. The eigenframe rotation theta has both L=0 and Q=0.

PROVED (step 2; verify_corner.py): for the seven physical rank-two gap-matrix coordinates h=(x,y,k,p,q,v,z), L=(-23x+y)/20. The eight active weight derivatives admit an exact rational left inverse. All 128 signed l1 dual inequalities have nonnegative rational Farkas multipliers, with c=1/6. This holds on the larger cone given by nonnegative active weight derivatives, hence on every cone remaining after the residual filters. There is no physical zero direction or negative direction.

PROVED (step 3; verify_corner.py): T is the rational invariant P/det(B^T B); the frame formula is matched independently. On the cube |h_i|<=1/100, det(B^T B)>=80, every Hessian entry of T is at most 27 in absolute value, and the combined Taylor/filter error is at most 32 ||h||_1^2. Therefore T>=||h||_1/12 on 0<||h||_1<=1/400 for every feasible graph, without invoking any residual filter. The matrix ball ||S-S0||_max<=1/20800 is contained in this chart neighborhood and has T>=||S-S0||_max/120. Exact rational constants are saved in remainder_certificate.json and matrix_ball_certificate.json.

OPEN: A literal ball about one eigenframe still cannot have the requested coercivity; the flat rotation is a coordinate redundancy. The new theorem uses graph-invariant distance. The global complement has not been covered.

PROVED (verify_filters.py): both active inherited moment records are strictly negative at P0; all 192 chart choices at its eight zero edges are strictly separated from all 47 old boxes. The certificate is filter_certificate.json. These exclusion filters are not missing active first-order inequalities.

PROVED (verify_rotation.py): rotation_obstruction.json gives an exact curve in region (11) with s=t^4, 0<t<=1/100, nonzero pure-rotation frame tangent, and T=o(frame-distance squared). Rational Bernstein controls check its rotated moment filters; the inherited family replay checks all remaining filters. Thus the full-eigenframe versions of the requested linear lower bound and quadratic positive definiteness are impossible, although local graph positivity is proved.

PROVED (verify_examples.py): three independent rational-frame calculations, including two with r<1, match the local invariant formula, every edge weight and the proved lower bound.

PROVED (verify_corner_faces.py): corner_face_boxes.json contains two rational boxes around the two canonical types of corner chart. They include the disconnected equality point and prove strict positivity on their connected feasible parts. This uses the Farkas theorem rather than a strictly positive ambient polynomial interval bound. All fifteen distinct labeled two-edge limits are enumerated.

OPEN (step 4): a read-only reuse of STRAT10's polynomial, Bernstein and feasibility machinery is refining the 5,244 inherited OPEN leaves. No source replay that writes to STRAT9/ or STRAT10/ is invoked. New accepted leaves and the overlay partition will be independently replayed. The saved local theorem does not imply positivity on the global complement.

PROVED (step 5; verify_frame.py, verify_corner.py): no negative linear direction exists on the outer admissible cone, hence none exists on the residual tangent cone. The conditional negative-direction counterexample search is not triggered. OPEN: this makes no claim about negative points far from the corner.

PROVED (verify_rotation.py): a permuted copy of the exact pressure curve stays at matrix distance >1/3 from the original labeled P0 while T tends to zero from above. A positive global-complement margin cannot be inferred by removing only one labeled ball. The theorem covers all fifteen permutations.

PROVED partial (step 4; verify_overlay.py): the exact 12,000-evaluation overlay replay passed. New leaves: 149 positive, 1,789 excluded, 10,062 splits, 13,368 OPEN. Combined partition: 100,479 nodes, 24,857 positive leaves, 12,015 exclusions, 50,239 splits, 13,368 OPEN. OPEN coordinate volume decreased exactly from 15467841/131072 to 3333609/32768. No whole overlay leaf reached the local-corner criterion. corner_cover.json, cover_summary.json and remaining_open_boxes.json retain all data. OPEN: full complement sign and full requested global closure.

PROVED (step 1 audit; verify_cone.py, verify_filters.py): completed the actual tangent-cone identification, including the strict endpoint-connectivity condition. The strict direction e=(1,1/10,0,1/10,0,0,0) has all active weight derivatives positive. Each of the fifteen endpoint-disconnection cuts is contained in a proper algebraic zero set, verified using exact unequal crossing D_ij values at a rational Cayley point. Density of their complement and strict filter inactivity show that every direction of the displayed linearized cone is an actual Bouligand tangent direction. tangent_cone_certificate.json records all rational premises; RESULT.md gives the density argument. The independent physical positivity theorem does not rely on that argument.

PROVED (replay_all.py): final sequential replay passed all nine checks. replay_all.out and replay_summary.json record the exact checks; timings are NUMERICAL only. Final source and local-input hash checks passed. The exact corner theorem is complete in physical matrix distance, including all fifteen permutations. OPEN: the full global complement, with 13,368 retained OPEN leaves; no claim of global closure or of a negative T counterexample.

OPEN: Shared brain/checklist/mesh updates remain unavailable under this sandbox's filesystem restrictions. Durable mathematical results and their exact replays are retained in this folder.

OPEN: Task: “close the corner (r,a)=(1,1) of T104 5+1 region (11), N=6” — 2026-11-13 09:26 +04 (workspace launch time). Local corner proved; global complement remains open.

OPEN: overlay 500 visits; {'split': 500}; frontier 5744.

OPEN: overlay 1000 visits; {'split': 1000}; frontier 6244.

OPEN: overlay 1500 visits; {'split': 1500}; frontier 6744.

OPEN: overlay 2000 visits; {'split': 2000}; frontier 7244.

OPEN: overlay 2500 visits; {'split': 2500}; frontier 7744.

OPEN: overlay 3000 visits; {'split': 3000}; frontier 8244.

OPEN: overlay 3500 visits; {'split': 3500}; frontier 8744.

OPEN: overlay 4000 visits; {'split': 4000}; frontier 9244.

OPEN: overlay 4500 visits; {'split': 4500}; frontier 9744.

OPEN: overlay 5000 visits; {'split': 5000}; frontier 10244.

OPEN: overlay 5500 visits; {'split': 5419, 'excluded': 80, 'positive': 1}; frontier 10582.

OPEN: overlay 6000 visits; {'split': 5759, 'excluded': 233, 'positive': 8}; frontier 10762.

OPEN: overlay 6500 visits; {'split': 6111, 'excluded': 374, 'positive': 15}; frontier 10966.

OPEN: overlay 7000 visits; {'split': 6533, 'excluded': 439, 'positive': 28}; frontier 11310.

OPEN: overlay 7500 visits; {'split': 6959, 'excluded': 504, 'positive': 37}; frontier 11662.

OPEN: overlay 8000 visits; {'split': 7230, 'excluded': 720, 'positive': 50}; frontier 11704.

OPEN: overlay 8500 visits; {'split': 7529, 'excluded': 914, 'positive': 57}; frontier 11802.

OPEN: overlay 9000 visits; {'split': 7903, 'excluded': 1016, 'positive': 81}; frontier 12050.

OPEN: overlay 9500 visits; {'split': 8232, 'excluded': 1164, 'positive': 104}; frontier 12208.

OPEN: overlay 10000 visits; {'split': 8669, 'excluded': 1214, 'positive': 117}; frontier 12582.

OPEN: overlay 10500 visits; {'split': 9097, 'excluded': 1279, 'positive': 124}; frontier 12938.

OPEN: overlay 11000 visits; {'split': 9377, 'excluded': 1489, 'positive': 134}; frontier 12998.

OPEN: overlay 11500 visits; {'split': 9727, 'excluded': 1634, 'positive': 139}; frontier 13198.

OPEN: overlay 12000 visits; {'split': 10062, 'excluded': 1789, 'positive': 149}; frontier 13368.
