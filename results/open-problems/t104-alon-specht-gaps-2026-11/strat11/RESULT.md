PROVED (verify_corner.py): The physical corner is closed. Write S=a uu^T+ar ww^T and S0=u0 u0^T+w0 w0^T, where u0=(-4,1,1,1,1)/sqrt(20), w0=(0,1,-1,-1,1)/2. Every feasible graph satisfies

    0 < ||S-S0||_max <= 1/20800  =>  T6 >= ||S-S0||_max/120 > 0.

PROVED (verify_corner.py, verify_corner_faces.py): This statement holds without imposing any residual filter, and at all fifteen permutations of the labeled two-edge limit graph. The distance is the maximum absolute matrix entry. T6(S0)=0; this disconnected graph is outside (11).

OPEN: The complement of these neighborhoods in STRAT9 region (11) is not covered. A replayed refinement adds 149 positive leaves and 1,789 exclusions, but leaves 13,368 OPEN leaves. No full sign theorem or counterexample is claimed.

PROVED (verify_frame.py): In eigenframe coordinates alpha=1-a, beta=1-r, and Cayley rotation/transverse coordinates (theta,p,q,v,z), the exact Taylor expansion is T6=L+Q+O(3), where

    L = 11 alpha/10-beta/20,
    Q = -79 alpha^2/80-alpha beta/16-3 beta^2/320
        -17(p^2+q^2)/25-7(pz+qv)/5-3(v^2+z^2).

PROVED (verify_frame.py): Let U0=(-4,1,1,1,1), W0=(0,1,-1,-1,1), X=(0,1,1,-1,-1), Y=(0,1,-1,1,-1), and E=(U0,W0,X,Y). The frame chart is obtained from E by the D-orthogonal Cayley matrix (I+H/2)(I-H/2)^(-1), D=diag(20,4,4,4), with

    H = [ 0       -theta/5   -p/5   -q/5 ]
        [ theta    0        -v     -z   ]
        [ p        v         0      0   ]
        [ q        z         0      0   ].

PROVED (verify_frame.py): Normalize its first two columns by sqrt(20) and 2. The pressure family has first-order direction alpha=2s, beta=theta=q=v=z=0, p=s, giving L=11s/5. Eight active edge derivatives are listed in frame_expansion.json. Their nonnegativity implies 2alpha-beta>=0; beta>=0 is the active ratio constraint. Consequently L>=0, and L=0 forces alpha=beta=p=q=v=z=0. Theta remains free. Both L and Q vanish on this rotation line; the graph itself is fixed there. There is no negative tangent direction and no positive definite quadratic form on this eigenframe face.

PROVED (verify_filters.py): At the specified frame the inherited moment tests are strictly negative, the scale ceilings are strictly below one, and all 192 zero-edge chart choices are strictly separated from every one of the 47 old boxes. Thus these filters impose no further first-order restriction in a sufficiently small frame neighborhood. Carrier/endpoint connectivity and the strict a<lambda condition have boundary at P0.

PROVED (verify_cone.py, verify_filters.py): The actual Bouligand tangent cone C of (11) in this frame chart is exactly beta>=0 together with the eight nonnegative active weight derivatives in frame_expansion.json; theta is free. The scale inequality 2alpha-beta>=0 is redundant, since 2alpha-beta=5(g01+g02+g03+g04). Here is the sufficiency argument, including the strict endpoint condition. Add epsilon times e=(1,1/10,0,1/10,0,0,0) to any vector in that cone. All eight weight derivatives, beta, and 2alpha-beta are then strictly positive. For sufficiently small t, the chart point t(d+epsilon e) has every weight positive and satisfies all locally inactive filters.

PROVED (verify_cone.py): The endpoint can be chosen connected by an o(t) perturbation. A disconnected endpoint has all crossing D_ij equal for at least one nontrivial vertex cut: all crossing weights are zero there. For each of the fifteen cuts, tangent_cone_certificate.json gives two crossing D_ij with unequal rational values at a point of the Cayley chart. The witness has Cayley parameter p=1/1000, equivalently pressure parameter s=20p/(20-p^2); its normalization identity is checked exactly. Thus each disconnection condition lies in a proper algebraic zero set in the rational Cayley coordinates. Their finite union has empty interior. Its complement intersects every sufficiently small strict feasible neighborhood, so choose the perturbation there. First send t to zero and then epsilon to zero (or take a diagonal sequence). This realizes every vector of the displayed cone as a tangent direction. Necessity follows by differentiating the active inequalities. The local physical certificate below also holds on a larger cone and does not depend on this density argument.

PROVED (verify_corner.py): Remove the rotation redundancy using h=(x,y,k,p,q,v,z),

    B = (U0+pX+qY, W0+vX+zY),
    K = [ (1+x)/20  k/20      ],   S=B K B^T,
        [ k/20      (1+y)/4   ]
    Q_S = B(B^T B)^(-1)B^T,  lambda=(2+tr S)/4,
    omega_ij=lambda/5+S_ij.

PROVED (verify_corner.py): These are coordinates on the rank-two symmetric zero-sum matrix manifold near S0. For any nearby rank-two S, its coefficient matrix in E has upper block K; the lower-left block times K^(-1) recovers the four transverse coordinates. Rank two gives the Schur complement identity, hence S=BKB^T. At first order the eigenframe chart maps to x=-alpha, y=-alpha-beta, k=0 with the same p,q,v,z; theta is redundant at r=1.

PROVED (verify_corner.py): The exact linear term in this chart is L_h=(-23x+y)/20. In edge order (01,02,03,04,12,13,24,34), the eight active weight derivatives g are

    (-3x+y-4k-4p-4q)/20,
    (-3x+y+4k-4p+4q)/20,
    (-3x+y+4k+4p-4q)/20,
    (-3x+y-4k+4p+4q)/20,
    (x-2y+p-5z)/10, (x-2y+q-5v)/10,
    (x-2y-q+5v)/10, (x-2y-p+5z)/10.

PROVED (verify_corner.py): tangent_certificate.json gives a rational left inverse J with J Dg=I, and

    L_h = (9/4)(g01+g02+g03+g04)+(1/2)(g12+g13+g24+g34).

PROVED (verify_corner.py): For all 128 sign vectors sigma, the saved Farkas multiplier row lambda_sigma=lambda-(1/6)sigma^T J is nonnegative and satisfies lambda_sigma Dg=DL_h-(1/6)sigma^T. Therefore

    g>=0 => L_h >= ||h||_1/6.

PROVED (verify_corner.py): Put d=det(B^T B). Its exact SOS identity is

    d=80+16(p^2+q^2)+80(v^2+z^2)+16(pz-qv)^2 >=80.

PROVED (verify_corner.py): With tau=tr S, M=sum_i (Q_S)ii Sii, and q=diag Q_S, the following invariant expression is matched algebraically to STRAT10/frame.py (and hence to its inherited original-expression derivation):

    T6=9/80+(11M-2tau)/8
       +[100tau M-320 sum_i Sii^2-1280 sum_i (Q_S)ii(S^2)ii
          +448 tr(S^2)-33tau^2]/320
       +sum_ij (Q_S)ij Sij^2+2 q^T S diag(S).

PROVED (verify_corner.py): T6=P/d with P a rational polynomial. On the full cube |h_i|<=1/100, d>=80 and every entry of Hess(T6) has absolute value <=27. The eight edge Hessian bounds and exact unrounded constants are in remainder_certificate.json. If mu_i bounds all Farkas multipliers for edge i, the combined second-order remainder satisfies

    |R_T|+sum_i mu_i |R_omega_i| <=32 ||h||_1^2.

PROVED (verify_corner.py): This accounts for the curvature of the feasible set: actual nonnegative weights need not have nonnegative linearizations. Substituting actual weights into the 128 identities gives

    T6 >= ||h||_1/6-32||h||_1^2 >= ||h||_1/12
        whenever 0<||h||_1<=1/400.

PROVED (verify_corner.py): For epsilon=||S-S0||_max<=1/20800, coefficient extraction gives |x|+|y|+|k|<=76epsilon/5 and |p|+|q|+|v|+|z|<=36epsilon; hence ||h||_1<=52epsilon<=1/400. Conversely, derivative bounds on the gap-matrix entries give epsilon<=10||h||_1. This proves the matrix-ball assertion at the start. matrix_ball_certificate.json replays every rational comparison.

PROVED (verify_rotation.py): A bound by distance to a single eigenframe is impossible on (11), even after allowing second order. rotation_obstruction.json uses the pressure parameter s=t^4 and the rational D-orthogonal rotation

    c(t)=(tu-t^2)/(tu+t^2),  tu=20+4t^8,
    U'=c(t) U + tu*t W/(tu+t^2),
    W'=-4t U/(tu+t^2)+c(t) W.

PROVED (verify_rotation.py): Their norms are tu and 4, their projector is unchanged, and their rotated moment filters have rational Bernstein certificates for 0<t<=1/100. All other filters are replayed through the inherited pressure-family certificate. The exact squared distance of w(t) to w0 is 4t^2/(tu+t^2)>=t^2/9, whereas T/t^2 tends to zero. Thus neither a strictly positive linear nor a strictly positive quadratic lower bound in full frame distance can hold. The physical matrix bound above resolves the corner positivity question despite this redundancy.

PROVED (verify_corner_faces.py): corner_face_boxes.json gives two rational chart boxes, centered at the limit-chart types (4,-1,-sqrt(5),-1,-sqrt(5),sqrt(5)) and (3/2,-1,-sqrt(5),-1,sqrt(5)/2,sqrt(5)/2). The centers are enclosed with rational square-root bounds, and corner_boxes.py pulls each whole box into the local theorem. T is nonnegative on their feasible parts and strictly positive on connected graphs. These boxes contain equality points, so they cannot be certified by a strictly positive ambient polynomial lower bound.

PROVED (verify_examples.py): Independent exact rational-frame evaluations match the new invariant formula and lower bound at three endpoints, including r<1.

PROVED (verify_frame.py, verify_corner.py): Step 5 is not triggered: the tangent cone has no direction with L<0. OPEN: absence of a negative tangent direction does not settle the complement.

PROVED (verify_rotation.py): Removing only the one labeled matrix ball does not produce a uniform positive margin. Swap vertices 0 and 1 in the pressure family. Every condition of (11) is invariant under this permutation. The certificate proves ||S-S0||_max>1/3 while T tends to zero from above. Therefore the proposed sampling-based justification for step 4 is false for a single labeled P0. The local theorem above covers all fifteen symmetric copies; it does not assume that the remaining complement has a positive margin.

PROVED partial (verify_overlay.py): Step 4 reuses STRAT10/cover_face.py, centered_bounds.py, axis_bernstein.py and zero_face.py without editing those folders. corner_boxes.py adds the local positivity predicate. corner_cover.json is an exact partition overlay on the 5,244 inherited OPEN leaves. The run evaluated 12,000 overlay nodes, accepting 149 positive leaves and 1,789 excluded leaves and splitting 10,062 nodes. It left 13,368 OPEN leaves, each listed with rational bounds in remaining_open_boxes.json.

PROVED partial (verify_overlay.py): The combined partition has 100,479 nodes: 50,239 split nodes, 24,857 positive leaves, 12,015 excluded leaves and 13,368 OPEN leaves. No overlay leaf was small enough for whole-box acceptance by the corner predicate. The local theorem and corner_face_boxes.json still remove their feasible connected subsets, including every point of the specified physical balls, independently of this ledger. The larger OPEN count reflects refinement; the exact OPEN coordinate volume falls from 15467841/131072 to 3333609/32768. These are chart volumes, not volumes of admissible graphs or of the residual.

PROVED partial (verify_overlay.py): The overlay replay verifies the inherited partition topology and source hash, and recomputes every new positive and exclusion certificate. The inherited 24,708 positive and 10,226 excluded leaf certificates retain their STRAT10 dependencies; this run does not claim to have rerun all of those old leaf sign tests. The new corner theorem, filter checks, exact example values, rotation obstruction and new leaves are independently replayed here.

OPEN: The remaining sign problem is (11) outside the union of the fifteen proved physical corner neighborhoods and the inherited/new positive sets. Every remaining point has a canonical chart in an OPEN leaf of the combined ledger. OPEN leaves can contain infeasible points and points already proved by a different chart or by the local theorem. No claim is made that they are all feasible or that a positive uniform margin has been established on this complement.

PROVED (replay_all.py): Replay from this folder with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py`. The scripts use exact rational polynomial identities, rational interval arithmetic and rational Bernstein controls; no floating tolerance is used for a PROVED sign. Numerical timings in replay_summary.json have no proof role. verify_provenance.py pins the source snapshot and local replay inputs. Source folders are unchanged. No subagents, language-model workers, network access or accelerated execution were used.

PROVED (replay_all.py): The final one-pass replay passed all nine checks: provenance, frame expansion, inactive filters, actual tangent-cone premises, physical Farkas/remainder theorem, independent exact examples, rotated/permuted residual obstructions, corner face boxes, and partition overlay. replay_summary.json and replay_all.out record the run. OPEN: the global sign on the retained complement remains unproved.

OPEN: Task: “close the corner (r,a)=(1,1) of T104 5+1 region (11), N=6” — received 2026-11-13 09:26 +04 (workspace launch time).
