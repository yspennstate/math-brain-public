OPEN: The full 5+1 inequality is not closed. This write-up gives larger proved regions, a corrected radial reduction, exact certificates, and an explicit remaining continuous region. No numerical result is used as a proof.

PROVED: For a connected five-vertex carrier with both top eigenvalues and one isolated vertex (N=6), T>=0 holds in each of the following regions:

    every admissible scale if 0<b/a<=3/20;
    every admissible frame and ratio if a<=14/25;
    the larger ratio-dependent scale regions in the table below;
    every frame passing any saved pointwise moment bound, at its
        actual scale or at its true radial endpoint;
    every frame whose true radial endpoint has a chart in one of
        the 47 rational face boxes;
    every frame whose true radial endpoint is disconnected.

PROVED: After adding further isolated vertices, for every integer N>=6 the corresponding regions include

    every admissible scale if 0<b/a<=3/25;
    every admissible frame and ratio if a<=64/125;
    the all-N scale regions in the table;
    all 47 face boxes and their inward radial rays;
    the pointwise all-N moment bounds and disconnected endpoints.

PROVED: These are rational scale ceilings, not estimated optima. The intervals include their endpoints. The first two rows are superseded where the full ratio-strip theorem applies. Replay: verify_small_ratio.py, verify_allN_ratio.py, verify_cells.py, verify_allN_cells.py, verify_coverage.py.

| Ratio r=b/a | N=6 scale ceiling | Ceiling for every N>=6 |
|---|---:|---:|
| [0,1/10] | 66/125 | 66/125 |
| [1/10,1/5] | 71/125 | 71/125 |
| [1/5,3/10] | 119/200 | 119/200 |
| [3/10,2/5] | 76/125 | 3/5 |
| [2/5,1/2] | 76/125 | 74/125 |
| [1/2,3/5] | 603/1000 | 289/500 |
| [3/5,7/10] | 119/200 | 563/1000 |
| [7/10,4/5] | 293/500 | 547/1000 |
| [4/5,9/10] | 287/500 | 53/100 |
| [9/10,1] | 14/25 | 64/125 |

PROVED: The r=0 entries are auxiliary limiting calculations; the actual D=2 stratum has r>0. The certificate files are moment_cells.json and allN_optimized_cells.json. allN_cells.json contains another ten valid, slightly weaker truncations.

PROVED: Exact frame formula and the radial reduction

PROVED: Let u,w be orthonormal zero-sum vectors in R^5, a>=b=ar>0, s=a+b, lambda=(2+s)/4, Q=uu^T+ww^T, and Pi_5=I-J/5-Q. Embed Pi_5 into N coordinates by adding zero rows and columns. The carrier Laplacian and weights are

    L_5=lambda(I-J/5)-a uu^T-b ww^T,
    omega_ij=lambda/5+a u_i u_j+b w_i w_j.

PROVED: Write

    A=sum u_i^4, B=sum w_i^4, C=sum u_i^2 w_i^2,
    d=sum u_i^3, e=sum u_i^2 w_i,
    f=sum u_i w_i^2, h=sum w_i^3,
    m_r=A+rB+(1+r)C,
    L6=[11m_r-2(1+r)]/8,
    H6=[100(1+r)m_r-1600(A+r^2 B)-1280(1+r^2)C
          -640rC+415(1+r^2)-66r]/320,
    R6=3d^2+3r^2 h^2+(1+4r)e^2+(r^2+4r)f^2
          +2(1+r)(df+rhe).

PROVED: The padded expression is exactly

    T6(a,ar)=9/80+a L6+a^2(H6+R6).                     (1)

PROVED: This uses c=3 and beta=(1-lambda)/4. An all-N formula is implemented in frame.py: retain X1 and S5 from the carrier, take X2=2N K/(N-2), and use

    hdiag=4/5-2s/5+a(A+C)+b(B+C),
    X3=(1-lambda)[2(N-1)(N-4)lambda-4(N-2)+2N hdiag]
            /(N-2)^2,
    K=a^2 A+b^2 B+2abC-(a^2+b^2)/5
        -a^2(d^2+e^2)-2ab(e^2+f^2)-b^2(f^2+h^2).

PROVED: verify_algebra.py independently expands the ordered-pair expression for S5, reconstructs X1,X2,X3, and matches (1) and the all-N formula as polynomial identities over the rationals. This is a universal algebraic certificate, separate from finite numerical checks.

NUMERICAL: numerical_check.py compared 1,200 random admissible frames at N=6,7,10 with the read-only STRAT7/terms.py: 3,600 comparisons, seed 9131311, maximum absolute discrepancy 1.8096635301390052e-14. The minimum sampled T was 0.11465090468595591. These values are formula audits, not lower bounds. Full output: numerical_check.json.

PROVED: Define

    D_ij=-1-r-20(u_i u_j+r w_i w_j),
    Dmax=max(3-r,max_(i<j) D_ij), E=2/Dmax.

PROVED: All admissible scales on this ray lie in 0<a<=E, because omega_ij=1/10-aD_ij/20 and a<=lambda is equivalent to a<=2/(3-r). The selected projector is fixed. The old identity (R1) does not hold verbatim: T6(0)=9/80, even though this endpoint uses a selected rank-two projector inside a larger eigenspace. Since A+C,B+C>=1/4,

    L6>=3(1+r)/32>0.

PROVED: For every N>=6, write T_N(a,ar)=C_N+a L_N+a^2 H_N. Both C_N and L_N are strictly positive; verify_algebra.py checks their numerators coefficient by coefficient after substituting N=6+z, A+C=1/4+v and B+C=1/4+w. For t=a/E the correct identity is

    T_N(a,ar)=(1-t^2)C_N+a(1-t)L_N+t^2 T_N(E,rE).    (2)

PROVED: Thus nonnegativity at the true far endpoint proves every smaller scale, with strict positivity at smaller scales. At the endpoint either a=lambda and the carrier disconnects, or an edge weight is zero. At a=lambda and 0<r<1, the carrier has rank three, hence two components: 4+1 or 3+2. At r=1 its rank is two; the two nonzero eigenvalues are both one, and the graph is a balanced triangle plus isolates or two equal edges plus isolates. The STRAT7 four-vertex and triangle certificates are copied locally as prior_four.py and prior_triangles.py. The balanced-top-triangle plus lower-edge case and the rank-two equality graphs are checked by verify_boundary.py. These cover every disconnected far endpoint after any number of isolates. No second face reduction is assumed.

PROVED: Moment inequalities and rational cells

PROVED: Every frame belongs to the following rational moment polytope, including the A/B swaps of the additional inequalities:

    7/30<=A,B<=13/20, 0<=C<=3/10,
    1/4<=A+C,B+C<=4/5,
    4/5<=A+B+2C<=7/5, 2C<=A+B,
    (3/2)A+C<=27/25, 2A+C<=11/8,
    3A+C<=81/40, 4A+C<=107/40,
    A-C<=5/8, 2A-C<=51/40, 3A-C<=77/40.              (3)

PROVED: The diagonal contraction ||diag Z||^2<=(3/5)||Z||_F^2 for symmetric Z with Z1=0 and tr Z=0 gives the upper bounds 13/20,3/10,7/5. Apply it to uu^T-(I-J/5)/4, (uw^T+wu^T)/sqrt(2), and Q-(I-J/5)/2. The bounds involving 4/5 and 2C<=A+B follow from Q<=I-J/5 and squared norms; A+B+2C>=4/5 is Cauchy-Schwarz. verify_elementary.py checks the contraction constants. The lower bounds 7/30 and 1/4 have exact ordered-cone scalar and matrix certificates in verify_moments.py and moment_lower_matrices.json. The seven extra bounds have local Pólya coefficient certificates, replayed by verify_polya_moments.py: 5,445 rational 3-by-3 matrices, all seven principal minors checked. The redundant bound 2A+C<=7/5 is retained in that replay. moment_polytope.py enumerates all triple intersections exactly, giving 33 vertices.

PROVED: For each (alpha,beta) in {(1,1),(1,0),(0,1),(1,-1)}, put

    m=alpha(A+rC)+beta(C+rB),
    q=alpha^2 A+2alpha beta C+beta^2 B,
    S=a(alpha+beta r-m)-lambda(alpha+beta)/5,
    N_ab=a[alpha^2 d^2+2alpha beta e^2+beta^2 f^2]
           +ar[alpha^2 e^2+2alpha beta f^2+beta^2 h^2].

PROVED: Exact weighted first and second moment identities, weighted variance, and Cauchy-Schwarz give, for arbitrary rational tangents t,v,

    N_ab >= a[2tm-(1+r)t^2]
             -lambda(alpha^2+beta^2-q)/5+vS-v^2/2.    (4)

PROVED: This includes negative alpha beta. Also, with

    N_r=d^2+(2+r)e^2+(1+2r)f^2+rh^2,
    J_r=(d+f)^2+r(e+h)^2,

PROVED: the nonnegative weighted determinant squares give a(J_r-N_r)>=-2lambda/5. The Bessel bounds are d^2+e^2<=A-1/5, f^2+h^2<=B-1/5, e^2<=C and f^2<=C. All edge identities and every residual coefficient are matched independently by verify_cell_identities.py.

PROVED: A record gives four nonnegative directional multipliers theta, a nonnegative theta_d and four nonnegative Bessel penalties z1,...,z4. Subtract their theta N_ab/a from R6, add theta_d(N_r-J_r), and add the Bessel square penalties. Require the two blocks in (d,f) and (e,h) to be PSD. Before subtracting the directional terms they are

    [3+z1, 1+r-theta_d;
     1+r-theta_d, r^2+4r+2r theta_d+z2+z4],

    [1+4r+2theta_d+z1+z3, r(1+r)-r theta_d;
     r(1+r)-r theta_d, 3r^2+z2].

PROVED: cells.py implements the subtraction explicitly. If these blocks are PSD, (4) gives an exact lower polynomial P6(a,r,A,B,C): start with 9/80+aL6+a^2H6, subtract a^2[z1(A-1/5)+z2(B-1/5)+(z3+z4)C] and 2a lambda theta_d/5, then add a theta times (4) for each direction. This polynomial is linear in the three moments and of degree at most two in each of a,r.

PROVED: Each record's residual blocks are checked throughout its ratio interval by their three quadratic Bernstein control matrices and rational diagonal/determinant tests. The scalar bound is checked at every moment vertex: take its three Bernstein controls in a, then the exact quadratic minimum in r, including an interior critical point when present. All saved margins are positive rationals. The proof uses no floating solver. The inherited small-scale region a<=11/25 is replayed locally by prior_scale.py; together these certificates cover down to a=0. The multipliers remain valid pointwise at any admissible scale, even outside a record's saved scale interval.

PROVED: For the all-N extension let k=N-2=4+z. Write B_j(a,r,A,B,C), j=0,1,2, for the three noncubic coefficients of k^2 T_N in z, as implemented in padding.base_coefficients. Then the exact identity is

    k^2 T_N=sum_(j=0)^2 z^j[B_j+c_j a^2 R6]+zk a^2 E_r,
    (c_0,c_1,c_2)=(16,8,1),
    E_r=d^2+(1+2r)e^2+(2r+r^2)f^2+r^2h^2>=0.       (5)

PROVED: verify_algebra.py checks (5) identically. Replacing a^2R6 in every coefficient by the same cell lower bound gives padding.lower_coefficients. Checking all three coefficient polynomials by the preceding vertex/Bernstein method proves the cell for every z>=0. verify_allN_cells.py checks both banks, including all recorded exact margins. This proves the all-N column of the table.

PROVED: Full small-ratio strips

PROVED: Order u decreasingly, put p=-u_1u_5 and v=u_1+u_5. Then p>=1/5, and projection of e_1+e_5 onto span(u,w) gives

    1+20w_1w_5 <= 7-5v^2=:kappa <=7.

PROVED: Consequently the weight on this extreme-u pair implies

    a<=2/D(r), D(r)=20p-1-r kappa,
    D(r)>=3-7r>0 for the certified strips.           (6)

PROVED: Write H6+R6=P+rQ+r^2 R_w. Completing a square gives

    R_w >= R_* =83/64-75B/16-193C/48,
    R_w-R_*=3(h+e/3)^2+f^2+(C-e^2)/3>=0.

PROVED: At scale 2/D(r), multiply the lower radial value by D(r)^2. The resulting quadratic in r is

    Phi6(r)=(9/80)D(r)^2+2D(r)L6
                 +4[P+rQ+r^2 R_*].                (7)

PROVED: For an ordered nonzero zero-sum U, use

    U_i=sum_(j=1)^4 [(5-j) if i<=j, else -j] z_j,
    z_j>=0, t=||U||^2, W=K_U xi, n=||W||^2,
    (K_U)_1j=U_5-U_j, (K_U)_jj=U_1-U_5,
    (K_U)_5j=U_j-U_1, j=2,3,4.

PROVED: These columns span {1,U} perpendicular. At rho=3/20, each of the three degree-two Bernstein controls of t^3 n^2 Phi6 on [0,rho] has the exact decomposition

    sum_(|nu|=10) z^nu m(xi)^T G_nu m(xi),
    m=(xi1^2,xi1 xi2,xi1 xi3,xi2^2,xi2 xi3,xi3^2),
    every rational 6-by-6 G_nu is PSD.              (8)

PROVED: small_ratio_certificate.json gives all 858 matrices. verify_small_ratio.py independently reconstructs (7) from frame.py, homogenizes its normalized moments, matches every coefficient of (8), and checks PSD by exact symmetric elimination. Nonnegative Bernstein controls prove Phi6>=0 on the whole strip. Equations (2),(6),(7) prove T6>=0 at every actual admissible scale. The auxiliary scale in (6) need not itself be a feasible graph: (7) uses only frame inequalities, so no weight inequality is being applied at an infeasible auxiliary graph.

PROVED: Apply the same construction to each normalized radial polynomial B_j/c_j+a^2R6 from (5). Their constant and linear coefficients are positive by verify_algebra.py; the same square completion applies. At rho=3/25 all nine Bernstein controls have exact rational SOS decompositions. allN_ratio_certificate.json contains 2,574 matrices. verify_allN_ratio.py reconstructs and matches every coefficient, checks every PSD matrix, and also matches its j=0 polynomial with the independent N=6 construction. Thus (5) is nonnegative for every N>=6 and every actual admissible scale when r<=3/25.

PROVED: Exact zero-face boxes

PROVED: Relabel any zero edge as {4,5}. The rational chart is

    V1=(v1,z1), V2=(v2,z2),
    V3=(1-t-v1-v2,-z-z1-z2), V4=(t,0), V5=(-1,z),
    M=V^T V, R=VV^T, tau=tr M, Delta=det M,
    D=20t-tau, g_ij=t+R_ij,
    Qnum=V adj(M)V^T, Pnum=Delta(5I-J)-5Qnum.

PROVED: The face domain is exactly t>0, Delta>0, g_ij>=0, with g_45=0. There

    lambda=10t/D, gap matrix=2R/D,
    omega_ij=2g_ij/D, Pi_5=Pnum/(5Delta),
    a=[tau+sqrt(tau^2-4Delta)]/D,
    b=[tau-sqrt(tau^2-4Delta)]/D.                    (9)

PROVED: The matrix 5t(I-J/5)-R is a nonnegative graph Laplacian, giving M<=5tI, tau<=10t and D>=10t>0. The carrier is connected exactly when det(5tI-M)>0. Also 1/4<=t<=4 and the other coordinates have absolute value at most four, since ||V_i||^2<=4t. Every rank-two-gap zero-edge graph has this chart: factor gap/lambda=YY^T, rotate so Y4=(x,0), x>0, set t=5x^2 and V=sqrt(5t)Y. The zero edge forces V5's first coordinate to be -1; zero column sums determine V3.

PROVED: Set Qdiff_ij=(Qnum)_ii+(Qnum)_jj-2(Qnum)_ij, Rdiff_ij=R_ii+R_jj-2R_ij, and k=N-2. The exact polynomial is

    Cface_N=10k^2 D^2 Delta T_N
      =10k^2 Delta[40t tau-8tr(M^2)]
       +16Nk sum_ij(Pnum)_ij R_ij^2
       +(D-10t){[200(N-1)(N-4)+320N]t Delta
                   -40k D Delta-8N sum_i(Pnum)_ii R_ii}
       -80k^2 sum_(i<j)g_ij(2Delta-Qdiff_ij)Rdiff_ij. (10)

PROVED: zero_face.py checks the projector/normalization identities and independently checks the N=6 specialization using the original six-by-six G and trace definitions. Its coefficients in N-6 have respectively 1,255,1,255,1,253 terms. face_intervals.py evaluates those three coefficients with exact rational inclusion arithmetic.

PROVED: face_boxes.json gives 47 rational boxes in coordinate order (t,v1,z1,v2,z2,z). Throughout each box, t,Delta,D and all three coefficients of (10) are strictly positive. Thus every feasible graph in a box has T_N>0 for every N>=6. The boxes may include nonfeasible coordinates; positivity there only strengthens the inclusion certificate. verify_boxes.py replays every lower bound, encloses the exact rational-frame witnesses using rational square-root intervals, and independently matches three center evaluations with the expanded polynomial. Thirty-five witnesses miss all of the original ten N=6 moment-cell tests. This count refers specifically to moment_cells.json; it is not a measure of the continuous residual region.

PROVED: Remaining region specified exactly

PROVED: Let C be the finite collection of records in moment_cells.json and allN_optimized_cells.json. For a record whose closed ratio interval contains r, define

    P_6^c(x,r,A,B,C)=cells.lower_value(...),
    P_N^c(x,r,A,B,C)=sum_(j=0)^2 (N-6)^j
         padding.lower_coefficients(...)[j]/(N-2)^2.

PROVED: The arguments are the frame moments, scale x, ratio r and the exact multiplier vector from cells.vector_from_record(c). These are explicit rational polynomials, with positive constant denominators. They are valid lower bounds at any actual feasible scale x whenever the record's ratio interval contains r. Let P_N^* be their maximum. Let V6(r) be the maximum saved ceiling in moment_cells.json at that ratio, and Vinf(r) the maximum ceiling in allN_optimized_cells.json.

OPEN: For N=6, the continuous region still requiring a covering proof is the following explicit intersection:

    u,w orthonormal and zero-sum;
    3/20<r<=1, all omega_ij>=0, carrier connected;
    max(14/25,V6(r))<a<=E, a<2/(3-r);
    P_6^*(a,r,A,B,C)<0 and P_6^*(E,r,A,B,C)<0;
    the true endpoint at E is connected;
    for every zero edge at that endpoint, every relabeling of that
      edge in either order as {4,5}, every permutation of the other
      three vertices, and either common sign of the second column,
      the chart point lies outside every box in face_boxes.json. (11)

PROVED: Every case outside (11) is covered by one of the proved sufficient conditions. Chart membership in (11) is a finite exact exclusion, using the explicitly listed closed rational boxes and (9). In particular any counterexample must lie in (11). This does not assert a sign inside (11).

OPEN: For each N>=7 the corresponding residual region is (11) with r>3/25, a>max(64/125,Vinf(r)), and both P_6^* tests replaced by P_N^*. The same chart exclusions and connectivity conditions apply. This describes only five-vertex carriers plus isolates, not graphs with larger active components.

PROVED: The gap in these covering arguments is nonempty. residual_witness.json gives

    U=(10,0,0,0,-10), W=(-100,80,60,60,-100),
    u=U/||U||, w=W/||W||, r=41/50, a=525/866.

PROVED: residual_witness.py checks connectivity, nonnegative weights, a zero edge, a negative value of every saved pointwise cell lower bound, and exclusion from every face box in all 24 chart choices. Its exact value is T6=2219640933/6719605760>0. This proves a gap in the uniform covering certificates, not a counterexample; the individual rational point itself has its displayed exact sign certificate. The continuous target (11) is not adjusted by subtracting isolated exact checks.

OPEN: The full sign theorem on (11), a complete equality classification, and coverage for all five-vertex carriers at arbitrary scale remain unproved here. The rho=4/25 N=6 strip attempt left two unresolved quartic coefficient forms; rho=1/5 left thirteen. The all-N rho=3/20 attempt left two. These are incomplete certificates, not disproofs of the inequalities. Discovery and partial candidate files are excluded from exact replay.

PROVED: Replay and scope

PROVED: From this folder run

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay_all.py

PROVED: The driver runs every exact certificate sequentially, records individual .out transcripts and replay_summary.json, and updates LOG.md after each check. Exact replay requires SymPy and the Python standard library, with no optimizer. Discovery uses NumPy/SciPy and single-thread Clarabel solely to choose Gram matrices or multipliers; exact rational acceptance decides which records are certificates. All writes are local, source folders were read-only, and no network or language-model workers were used. Exact replay is sequential with a 1 GiB RSS guard; discovery used at most two simultaneous single-thread jobs. Numerical reference checks are run separately with numerical_check.py.

NUMERICAL: The completed exact replay had peak resident memory 99.125 MiB. Timings and measured memory are in replay_summary.json; these resource measurements are distinct from the exact inequality certificates.

PROVED: Task: “Prove T >= 0 for the 5+1 case at N = 6, beyond a <= 11/25.” Received 2026-11-13 at approximately 04:46 +04.
