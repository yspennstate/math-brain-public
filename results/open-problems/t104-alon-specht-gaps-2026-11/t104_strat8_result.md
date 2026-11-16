OPEN: T>=0 on the full residual region of STRAT6 remains unproved.

PROVED: This work gives new exact six-dimensional face boxes, an exact partition of the entire canonical chart with an explicitly retained OPEN frontier, and an additional theorem on a pendant subface. The global partition has 24,702 nonnegative leaves, 10,208 excluded leaves and 5,272 OPEN leaves; its exact replay is described below.

PROVED: The local collection face_boxes.json contains 43 closed rational boxes with Cface>0 throughout each box. They cover 34 exact connected zero-weight endpoints satisfying every residual filter in STRAT6. Every one of these endpoints misses all previous moment certificates, the strengthened nonlinear sufficient condition where applicable, and all 47 previous face boxes under every permitted chart symmetry. Thus the new local certificates enlarge the previously proved region. Certificates: face_boxes.json and exact_witnesses.json. Replays: verify_boxes.py, exact_witnesses.py, witness_residual.py.

NUMERICAL: All 34 supplied frames remain positive after moving to their actual first zero-weight endpoints. The minimum projected T is approximately 0.0134757681 at r=0.791. The maximum discrepancy between the independent terms(W) reference and the trace formula is below 1.8e-15; the expanded face polynomial agrees within 7.5e-15. These floating evaluations are in frame_evaluations.json and are reproduced by inspect_frames.py. They are not used in any proof. In particular, q in the supplied JSON is not T, and its small values must not be read as exact bounds.

NUMERICAL: The supplied a_end field agrees with the spectral ceiling 2/(3-r), to the displayed input precision.

PROVED: The actual zero-weight endpoint for a fixed frame is obtained from Dmax=max(3-r,max_{i<j}[-1-r-20(u_i*u_j+r*w_i*w_j)]) and a_end=2/Dmax. The numerical projection uses this formula after recentering and QR orthonormalization. The integer witnesses instead satisfy the zero sums and orthogonality exactly; their endpoints are rational and require no QR operation. The endpoint formula and radial identity (R1) are the given STRAT6 theorem.

PROVED: For completeness the face chart and quantity are as follows. Set x=(t,v1,z1,v2,z2,z) and

    V1=(v1,z1), V2=(v2,z2),
    V3=(1-t-v1-v2,-z-z1-z2), V4=(t,0), V5=(-1,z).
    M=V^T V, R=V V^T, N=tr M, Delta=det M, D=20t-N,
    g_ij=t+V_i.V_j, Qnum=V adj(M) V^T,
    Pnum=Delta(5I-J)-5Qnum.

PROVED: The admissible zero-edge face is exactly t>0, Delta>0 and g_ij>=0 for i<j. Its normalized data are

    lambda=10t/D, Gmat=2R/D, omega_ij=2g_ij/D,
    Q=Qnum/Delta, Pi=Pnum/(5Delta), g_45=0.

PROVED: The definitions of T in these data are

    X1=2(lambda tr Gmat-tr(Gmat^2)),
    X2=(10/3) sum_ij Pi_ij (Gmat_ij)^2,
    X3=((1-lambda)/3)[2tr Gmat-(10/3)sum_i Pi_ii Gmat_ii],
    2S5=2sum_{i<j}omega_ij
                (Pi_ii+Pi_jj-2Pi_ij)(Gmat_ii+Gmat_jj-2Gmat_ij),
    T=X1+X2+X3-2S5.

PROVED: Put Rdiff_ij=R_ii+R_jj-2R_ij and Qdiff_ij=(Qnum)_ii+(Qnum)_jj-2(Qnum)_ij. The integer polynomial being certified is

    Cface=45D^2 Delta T
      =Delta[1800tN-360tr(M^2)]
       +120sum_ij(Pnum)_ij R_ij^2
       +(D-10t)[60NDelta-20sum_i(Pnum)_ii R_ii]
       -360sum_{i<j}g_ij(2Delta-Qdiff_ij)Rdiff_ij.

PROVED: zero_face.py is copied from STRAT6 without changing its polynomial. It checks the projector, total-weight and numerator identities exactly. Cface has 1,254 nonzero integer coefficients, total degree 8, individual degrees at most 6, and coefficient gcd 80. The factor 45D^2 Delta is positive on the face domain. The exact identity, rather than agreement at floating points, connects every certificate below to T.

PROVED: All zero edges and their boundary cases are covered by a single bounded canonical root. Choose any zero edge, call its endpoint with the larger diagonal of Gmat vertex 4 and the other vertex 5, rotate the two-column Gram factor so V4=(t,0), reflect the second coordinate so z>=0, and order the other three vertices by first coordinate. Every admissible face graph has at least one such chart. The resulting closed root box is

    t in [1,4], v1 in [-1,0], z1 in [-4,4],
    v2 in [-1,1/2], z2 in [-4,4], z in [0,4].             (B)

PROVED: To construct a chart from a graph, factor Gmat/lambda=Y Y^T with two columns and zero column sums. A zero edge gives Y4.Y5=-1/5, so Y4 is nonzero. Rotate so Y4=(s,0), s>0, set t=5s^2 and V=sqrt(5t)Y. This gives V4=(t,0), the first coordinate of V5 equal to -1, and the stated V3 by the zero sums. The normalization 4lambda=2+a+b then gives lambda=10t/(20t-N). Swapping the two zero-edge endpoints, permuting the other three rows and reflecting the second coordinate gives the canonical choices above. This is an exhaustive construction, rather than an assumption about which charts the numerical frames visited.

PROVED: Here are exact bounds proving exhaustiveness of (B). The zero-sum rows give the g-weighted Laplacian

    Lg=5t(I-J/5)-R,
    sum_{j!=i}g_ij=4t-||V_i||^2.

PROVED: Since g_ij>=0, Lg is PSD and every degree on the right is nonnegative. Thus M<=5tI and N<=10t, which also gives D>=10t>0. Vertex 4 has degree t(4-t), so t<=4. Vertex 5 has squared row norm 1+z^2. Choosing the larger-diagonal endpoint gives t^2>=1+z^2, hence t>=1. For i=1,2,3, g_i4=t(1+x_i)>=0 gives x_i>=-1 and sum x_i=1-t. After x1<=x2<=x3,

    -3x1=(t-1)+(x2-x1)+(x3-x1)>=0,
    1-2x2=(t-1)+(x1+1)+(x3-x2)>=0.

PROVED: Consequently -1<=v1<=0 and -1<=v2<=1/2. Finally ||V_i||^2<=4t<=16 gives |z1|,|z2|,|z|<=4. Reflection supplies z>=0. These arguments include ties and additional zero weights. verify_domain.py replays the Laplacian, degree, ordering and norm identities; zero_face.py replays the Gram chart identities. This proof supplies the required coordinate bounds rather than assuming a numerical sampling range.

PROVED: The exact necessary conditions used to discard root boxes are g_ij>=0, 4t-||V_i||^2>=0, x3>=-1, x1<=x2<=x3, t^2>=1+z^2, M00,M11<=5t, Delta>0,

    det(5tI-M)>0,
    784Delta-75N^2>0.                                  (E)

PROVED: The determinant in (E) characterizes connectedness because both eigenvalues of M are at most 5t. The last inequality is equivalent to r>3/25: if the eigenvalues are mu1>=mu2>0, Delta/N^2=r/(1+r)^2, and (3/25)/(1+3/25)^2=75/784. A rational interval upper endpoint below zero for a non-strict condition, or at most zero for a strict condition, excludes the whole box from the residual domain. Further boxes may be discarded by the already proved a<=103/200 theorem. For c=103/200 put X=cD-N and H=N^2-4Delta. If D>0, X>=0 and X^2>=H throughout a box, then a=(N+sqrt(H))/D<=c wherever the face domain holds. Every exclusion is replayed using rational inclusion arithmetic in cover_face.necessary; no floating feasibility test is accepted.

PROVED: The sign certificates use P=Cface/80. For a rational box select a common denominator S so its center is c/S and its half-width vector is h/S, with integer c,h. The coefficients B_alpha in

    S^8 P((c+y)/S)=sum_alpha B_alpha y^alpha

PROVED: are integers, constructed by binomial translation. On |y_i|<=h_i an odd-power monomial has range [-h^alpha,h^alpha]; an all-even monomial has range [0,h^alpha]. An exact lower bound for the translated polynomial is therefore

    B_0
      -sum_{alpha with an odd entry}|B_alpha|h^alpha
      +sum_{alpha!=0 all-even, B_alpha<0}B_alpha h^alpha. (I)

PROVED: Multiplying (I) by 80/S^8 gives the saved Cface lower bound. centered_bounds.py performs all these operations with Python integers and Fractions. Induction over binomial translation and interval addition proves inclusion. Each local box has a strictly positive saved bound; a global positive leaf needs only a nonnegative bound. Graph feasibility is required only at the actual point, so these certificates are valid even when the surrounding box includes inadmissible points. Delta>0 and D>0 at that point follow from the domain proof above. verify_boxes.py also checks every local box center independently against the factored matrix expression in face_intervals.evaluate, using exact rational arithmetic.

PROVED: Some global leaves use a stronger one-coordinate Bernstein certificate. For a chosen normalized centered coordinate y=2s-1, the exact degree-n conversion is

    y^k=sum_{i=0}^n beta_ki binom(n,i)s^i(1-s)^(n-i),
    beta_ki=sum_{j=0}^{min(k,i)}
               binom(k,j)2^j(-1)^(k-j)binom(i,j)/binom(n,j).

PROVED: Apply this conversion to the integer centered polynomial, absorbing each h_i into its coefficient. Each Bernstein control is then an integer or rational polynomial in the other five normalized coordinates. The signed monomial bound (I) supplies a lower bound for each such control. Nonnegative control lower bounds prove nonnegativity on the whole six-dimensional box, by the nonnegative partition of unity of the Bernstein basis. axis_bernstein.py checks all 28 conversion identities for 0<=k<=n<=6 symbolically. A leaf using this method stores its axis and every control lower bound, all rechecked by verify_cover.py.

PROVED: The adaptive global certificate global_cover.json is a binary tree rooted at (B). Every internal node bisects a specified coordinate at its rational midpoint. Every leaf is positive, excluded, or OPEN. Induction over these bisections proves the union of all closed leaves equals (B). verify_cover.py reconstructs every box, rejects unreachable or repeated nodes, rechecks every accepted sign or exclusion, and checks the exact sum of leaf volumes equals the root volume 1152. Positive and OPEN leaf boxes are also exported explicitly as positive_partition_boxes.json and open_boxes.json. Floating priorities select work order only; each terminal decision is an exact rational computation. A successful partition replay is not a claim that OPEN leaves are positive.

PROVED: The final global tree has 40,181 internal bisections and 40,182 terminal boxes: 24,702 with Cface>=0, 10,208 excluded by exact necessary conditions or the inherited small-scale theorem, and 5,272 OPEN. Sixteen of the positive leaves use one-coordinate Bernstein controls; the rest use (I). All 80,363 nodes are retained in global_cover.json. A second discovery pass examining 40,000 additional child boxes reduced the OPEN frontier only from 5,692 to 5,288; the subsequent Bernstein pass removed sixteen more. These finite counts describe this partition, not a measure of admissible graphs or a proof on its OPEN part.

OPEN: Positivity on the 5,272 remaining terminal boxes is unproved. They are not omitted or silently treated as infeasible.

PROVED: There is an additional exact theorem on a lower-dimensional face. Suppose some vertex has precisely one neighbor and, in the Gram matrix Gmat, its row vector is collinear with that neighbor's row vector; equivalently, after labeling the pendant vertex 4 and its neighbor 3, (Gmat)_33*(Gmat)_44-(Gmat)_34^2=0. Label a nonneighbor 5. This is the subface

    v1=v2=-1, z1+z2+z=0.

PROVED: More generally the theorem holds on its admissible closure. Write the three nonneighbor second coordinates as y1,y2,y5, with sum zero, and set

    K=y1^2+y2^2+y5^2,
    J=y1^3+y2^3+y5^3,
    A=-21t^6+231t^5-1115t^4+3715t^3-8490t^2+10884t-5544,
    B=-(6t^4-78t^3+355t^2-847t+414)/2,
    E=-7(3t^2-9t+23)/4, F=12(t^2-3t+6).

PROVED: Exact substitution in Cface gives

    Cface/80=K[A+BK+EK^2]+FJ^2.                         (P1)

PROVED: Since M00=2(t^2-3t+6)<=5t, (4-t)(2t-3)>=0, so 3/2<=t<=4. Rank two gives K>0. Up to a permutation and common sign the zero-sum triple is a,b,-a-b with a>=b>=0 and a+b>0. Define

    v=(a-b)/(a+b),
    h=(a+b)^2(1+v)/(2(t+1)).

PROVED: Then 0<=v<=1 and 0<h<=1; the latter bound is exactly the strongest nonneighbor-edge constraint a(a+b)<=t+1. Substitution into (P1), after dividing by K>0, gives

    (1+v)^2(3+v^2) Cface/(80K)=P(t,v,h),
    P=A(1+v)^2(3+v^2)
      +B(t+1)h(1+v)(3+v^2)^2
      +E(t+1)^2h^2(3+v^2)^3
      +(9/2)F(t+1)^2h^2(1-v^2)^2.                     (P2)

PROVED: Let q2 be the coefficient of h^2 in P. The rational Bernstein controls on [3/2,4]x[0,1] are nonnegative for A, -q2 and P(t,v,1). There are respectively 7, 35 and 49 controls, all stored in pendant_certificate.json. Controls for A and -q2 are strictly positive; those for P(t,v,1) include zeros on the boundary. Since a Bernstein basis is nonnegative and sums to one, these sign claims follow exactly. Finally

    P(t,v,h)=(1-h)P(t,v,0)+hP(t,v,1)-q2 h(1-h)>=0.

PROVED: This proves T>=0 on the stated entire pendant subface, including its further zero-edge boundaries whenever Delta>0. pendant_certificate.py reconstructs (P1), (P2), the concavity identity and all 91 rational controls; it needs no solver. No theorem about the full pendant face is asserted.

NUMERICAL: A broader attempted pendant-face bound minimized freely over the centered cubic moment, subject only to relaxed spectral constraints. It was negative at 4,207 of 10,000 sampled relaxed points. This failed relaxation is neither a graph counterexample nor a proof. explore_pendant.py and pendant_symbolic.txt retain the calculation; it is not used in any certificate.

PROVED: Here is an explicit definition of the inherited endpoint residual R6 used below. For the normalized eigenframe set A=sum u_i^4, B=sum w_i^4, C=sum u_i^2 w_i^2, K=A+B+2C, f_r=A+rB+(1+r)C and

    L=(14/9)[f_r-(1+r)/5],
    H0=2(1+r)[f_r-(1+r)/5]/9+4(1+r^2)/3
        -14(A+r^2B)/3-4(1+r^2+r/3)C,
    c_r=max(0,1-7r)(9+r)/24,
    A0(r)=14(1+r)/(34+52r-22r^2+12c_r),
    Ai(r)=min_{v in V_i, H0_v-c_r*C_v<0}L_v/(-H0_v+c_r*C_v), i=1,2.

PROVED: An empty minimum is infinity. V1,V2 are the exact 19- and 33-vertex moment polytopes reconstructed by moment_bounds.vertices(False/True). Let V(r) be the largest ahi in strong_moment_cells.json, enhanced_moment_cells.json and directional_moment_cells.json with rlo<=r<=rhi. Let W(r) be the largest ahi in prior_weight_moment_cells.json at that ratio, or zero if none. Let Pstar(a,r,A,B,C) be the maximum applicable STRAT6 lower bound computed by rational_rays.cell_bound and directional_bounds.lower_value over those three new moment-cell files. The full definitions and proofs of those bounds are the inherited STRAT6 result; their implementations and all multiplier data are copied here.

PROVED: Put lambda=(2+a(1+r))/4, S=a(1+r-f_r)-2lambda/5, and

    ZN=a*f_r^2/(1+r)-lambda(2-K)/5+S^2/2,
    ZJ=a*f_r^2/(1+r)-lambda(4-K)/5+S^2/2,
    NL=L+aH0+(5r/3-1)max(0,ZN)+(1+r)max(0,ZJ).

PROVED: R6 consists of admissible fixed-frame far endpoints with a zero weight, connected, and satisfying

    3/25<r<=1, a<2/(3-r),
    a>max(A0(r),A1(r),A2(r),W(r),V(r),103/200),
    if r=1, a>Gstar,
    L+a(H0-c_r C)<0,
    Pstar(a,r,A,B,C)<0,
    if r>=3/5, NL<0,
    every zero-edge chart misses the old 47 closed boxes
        in prior_face_boxes.json.

PROVED: Gstar is the unique root in (551/1000,69/125) of 6272g^3-2989g^2-1034g+427. At these endpoints a=a_end, so the two scale tests at a and a_end in STRAT6 coincide. Its remaining condition min omega_ij<(lambda-a)/5 is automatic because min omega_ij=0 and connectedness gives lambda>a. Thus this definition is exactly the inherited residual restricted to the endpoints requested in this task. witness_residual.py checks all these conditions for each of the 34 saved rational endpoints, using exact arithmetic.

PROVED: The remaining region can be specified without approximation. Let R6 be the inherited endpoint residual defined explicitly above, equivalently the endpoint restriction of STRAT6/RESULT.md, section “What remains.” Let B_local be the union of the 43 closed boxes in face_boxes.json, B_pos the union in positive_partition_boxes.json, and B_open the union in open_boxes.json. Given a graph in R6, let C_all be its finite set of zero-edge charts obtained by choosing any zero edge, either endpoint order, any permutation of the other three vertices and either common second-coordinate reflection. Let C_can be those charts that obey the endpoint-diagonal choice, sorted first coordinates and nonnegative z used for (B). The new unresolved set is precisely the part of R6 for which

    c not in B_local for every c in C_all,
    c not in B_pos for every c in C_all,
    no c in C_all has v1=v2=-1 and z1+z2+z=0.            (R)

PROVED: Each c in C_can for a graph satisfying (R) belongs to B_open. The partition proof supplies this implication; no excluded leaf can contain a point in R6. Because closed leaves share boundaries, (R) explicitly excludes B_pos even if a point also belongs to B_open. There are no unstated genericity assumptions: points with two or more zero weights are included by the same chart, tests and partition, or by the pendant theorem. The set (R), with the finite JSON box lists, is an exact residual description.

OPEN: Cface>=0 on all of (R) remains unproved. No numerical minimum, successful finite bank, or positive coordinate volume is being substituted for that missing theorem. The original residual task is therefore only partially resolved.

PROVED: By the given radial identity (R1), every proved endpoint above proves T>=0 along its entire admissible fixed-frame, fixed-r ray. Strict endpoint positivity also gives strict positivity at every positive interior scale.

PROVED: Final replay command, from this folder:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

PROVED: Proof replay requires the Python standard library and SymPy. NumPy is used only by inspect_frames.py and the numerical reference, and is unnecessary for exact replay. Prior STRAT6 scripts/data used for witness comparison have been copied locally; no prior folder is modified. All writes remain in this folder; no network or language-model workers were used. The final exact verification is recorded in verification.json, cover_verification.json and replay.out. provenance.json records hashes of the unchanged inherited files.

PROVED: The completed replay passed every certificate above, reconstructed all 80,363 tree nodes, and checked exact coordinate-volume sum 1152. Its 27 recorded artifact hashes were checked again after completion. The full remaining set is (R), with every OPEN box explicitly retained in open_boxes.json. The positive leaves are listed in positive_partition_boxes.json. These results do not establish the universal inequality on (R).

NUMERICAL: Runtime measurements for the complete exact replay: approximately 211.57 seconds and peak resident memory 151,764,992 bytes (144.734375 MiB). Certificate discovery used no worker pools, at most two overlapping scientific Python processes, and single-thread BLAS settings. The full replay used one process. No network or language-model workers were used; all task writes were confined to this folder.

PROVED: Task: “Prove T >= 0 on the residual region of STRAT6” — received 2026-11-13, approximately 04:46 +04.
