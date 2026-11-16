PROVED: Partial result for the remaining connected n=5, D=2 stratum. The entire stratum is not closed. The radial reduction to a zero-weight face is correct. New exact certificates enlarge the uniform scale region to a<=103/200, give 176 rational moment cells and 47 rational boxes directly on the zero-weight face, improve the full equal-gap interval, and give stronger frame-dependent sufficient conditions. The explicit remaining region is specified below. Every new certificate has a replay script; numerical discovery is separate from verification.

PROVED: The equal-gap endpoint is the unique real root G in (551/1000,69/125) of

    6272 G^3 - 2989 G^2 - 1034 G + 427 = 0.

NUMERICAL: G is approximately 0.551713118178820. The previous equal-gap endpoint was approximately 0.549144427709494. These decimal values are descriptive; the theorem uses the isolated algebraic root.

PROVED: Notation and the radial reduction

PROVED: Let u,w be orthonormal vectors in the zero-sum subspace of R^5. Set b=ar, 0<r<=1, lambda=(2+a+b)/4, Q=uu^T+ww^T, Gmat=a uu^T+b ww^T, and Pi=I-J/5-Q. The edge weights are omega_ij=lambda/5+(Gmat)_ij. Here Gmat is a matrix; the scalar G above is the new equal-gap endpoint. The notation omega distinguishes edge weights from the frame vector w. Let

    A=sum u_i^4, B=sum w_i^4, C=sum u_i^2 w_i^2,
    d=sum u_i^3, e=sum u_i^2 w_i,
    f=sum u_i w_i^2, h=sum w_i^3.

PROVED: In the notation of the supplied results,

    T(a,ar)/a = L(r)+a H(r),
    L(r)=L_u+r L_w,
    H(r)=P+r Q0+r^2 R_w,
    L_u=14(A+C-1/5)/9, L_w=14(B+C-1/5)/9,
    P=58/45-40A/9-34C/9+8d^2/3+2e^2/3+2df,
    Q0=2(A+B-2/5)/9-8C/9
        +10(e^2+f^2)/3+2df+2he,
    R_w=58/45-40B/9-34C/9+8h^2/3+2f^2/3+2he.

PROVED: The previous bound A+C,B+C>=1/4 gives L(r)>=7(1+r)/90>0. Define

    D_ij=-1-r-20(u_i u_j+r w_i w_j),
    Dmax=max(3-r, max_(i<j) D_ij),
    a_end=2/Dmax.

PROVED: Indeed,

    omega_ij=1/10-a D_ij/20,
    a<=lambda iff a<=2/(3-r).

PROVED: Thus all admissible scales on this frame and ratio form the interval 0<a<=a_end. At its far end, either a=lambda, in which case the graph is disconnected, or at least one weight is zero. The projector Pi stays fixed throughout this ray, including its endpoint. For 0<a<=a_end,

    T(a,ar)=a(1-a/a_end)L(r)
             +(a/a_end)^2 T(a_end,r a_end).                 (R1)

PROVED: Consequently nonnegativity on the full ray is equivalent to nonnegativity at its far end. Sufficiency follows from (R1), and necessity follows from continuity. This checks the proposed reduction, including the positive limiting value of T/a at a=0. The already proved disconnected theorem handles every endpoint of the first type. An endpoint of the second type is covered whenever any of the new sufficient conditions below holds there; (R1) then covers every smaller scale on that ray.

PROVED: The original radial deformation does not justify repeatedly adding zero edges. On a zero face its zero weight immediately becomes positive when the scale decreases. A second face reduction requires a different deformation and a new proof. None is assumed here.

PROVED: New moment inequalities

PROVED: In addition to (13) of PREVIOUS_RESULT.md, every frame satisfies K=A+B+2C>=4/5 and each of the following bounds, together with its A/B swap:

    inequality                 multiplier power
    (3/2)A+C <= 27/25           4
    2A+C <= 7/5                4
    2A+C <= 11/8               14
    3A+C <= 81/40              9
    4A+C <= 107/40             9
    A-C <= 5/8                7
    2A-C <= 51/40             6
    3A-C <= 77/40             6.                            (M1)

PROVED: K>=4/5 follows from sum_i(u_i^2+w_i^2)=2 and Cauchy-Schwarz. The finite rational certificates for the other inequalities are as follows. Order a nonzero zero-sum vector U decreasingly and write

    U_i=sum_(j=1)^4 [(5-j) if i<=j, otherwise -j] z_j,
    z_j>=0, t=U^T U, q=sum U_i^4, ell=sum z_j.

PROVED: Put Delta_U=U_1-U_5>0. For j=2,3,4 define the columns of K_U by

    (K_U)_1j=U_5-U_j,
    (K_U)_jj=Delta_U,
    (K_U)_5j=U_j-U_1,

PROVED: with every other entry zero. These columns span the space orthogonal to 1,U. Every nonzero vector W in that space is K_U xi. Let n=W^T W. To prove c-kappa A+sigma C>=0, expand

    ell^m [(c t^2-kappa q) K_U^T K_U
            +sigma t K_U^T diag(U_i^2) K_U].                (M2)

PROVED: For each record in polya_upper_bounds.json use sigma=-1; for each record in polya_lower_bounds.json use sigma=+1. The record supplies kappa,c,m. Every coefficient matrix in z is positive semidefinite. Thus (M2) is positive semidefinite for z>=0. Its quadratic form divided by ell^m t^2 n is exactly c-kappa A+sigma C, proving the claimed bound. The normalizing factors are positive. Interchanging u,w proves the swapped bounds.

PROVED: verify_polya_moments.py reconstructs all eight polynomials and checks all seven principal minors of each of the 5,445 rational 3-by-3 coefficient matrices. This is a complete exact certificate, without a solver. The redundant bound 2A+C<=7/5 is retained to document its smaller certificate. The other inequalities in (M1), their swaps, K>=4/5, and the old inequalities define a rational polytope with 33 vertices. moment_bounds.py enumerates its vertices by exact triple intersections; enhanced_vertices.json records them. Every triple is checked against every inequality, so no candidate intersection is accepted by a tolerance. Boundedness and the active-constraint characterization of vertices show that the enumeration is exhaustive.

PROVED: Stronger bounds from nonnegative weights

PROVED: Write q_i=Q_ii and use the notation

    s=a+b, F=a(A+C)+b(B+C), K=A+B+2C,
    N_a=a(d^2+2e^2+f^2)+b(e^2+2f^2+h^2),
    J_a=a(d+f)^2+b(e+h)^2,
    Z=sum_i (Gmat)_ii q_i^2,
    S=s-F-2lambda/5.

PROVED: Ordered-pair expansion, using the zero sums and orthogonality, gives

    2 sum_(i<j) omega_ij Q_ij = S,
    2 sum_(i<j) omega_ij Q_ij^2
        =N_a-Z+lambda(2-K)/5,
    2 sum_(i<j) omega_ij(q_i q_j-Q_ij^2)
        =J_a-N_a+2lambda/5.                              (W1)

PROVED: The weights sum to one. Their variance inequality therefore implies

    2 sum omega_ij Q_ij^2 >= S^2/2.

PROVED: Also q_i q_j-Q_ij^2=(u_i w_j-w_i u_j)^2>=0, and weighted Cauchy-Schwarz with weights (Gmat)_ii gives Z>=F^2/s. Consequently

    N_a >= max(0,F^2/s-lambda(2-K)/5+S^2/2),
    J_a >= max(0,F^2/s-lambda(4-K)/5+S^2/2),
    J_a-N_a >= -2lambda/5.                              (W2)

PROVED: The second bound follows by combining the first inequality before its maximum with the last line. Thus both old lower bounds gain S^2/2. verify_new_bounds.py checks the identities (W1) by symbolic ordered-pair summation and verifies the residual identities used below.

PROVED: Let B0 denote (3) without its cubic contribution R. The old exact identity

    R=(5b/3-a)N_a+s J_a
       +(8/3)(a-b)[a d^2+s e^2+b f^2]

PROVED: immediately gives a stronger sufficient condition whenever r>=3/5:

    B0+(5b/3-a)max(0,F^2/s-lambda(2-K)/5+S^2/2)
       +s max(0,F^2/s-lambda(4-K)/5+S^2/2) >= 0.           (W3)

PROVED: This condition uses the actual frame moments and remains valid beyond all uniform scale ceilings in this report.

PROVED: Rational cells with positive-semidefinite cubic residuals

PROVED: Define

    f_r=A+rB+(1+r)C,
    H0=2(1+r)[f_r-(1+r)/5]/9+4(1+r^2)/3
       -14(A+r^2 B)/3-4(1+r^2+r/3)C,
    N_r=d^2+(2+r)e^2+(1+2r)f^2+r h^2,
    J_r=(d+f)^2+r(e+h)^2.

PROVED: Then T/a=L+a H0+a R_r, where R_r=R/a^2. Its two quadratic blocks, in (d,f) and (e,h), are respectively

    [8/3, 1+r; 1+r, 2r(r+5)/3],
    [2(1+5r)/3, r(1+r); r(1+r), 8r^2/3].

PROVED: The Bessel inequalities give

    d^2+e^2<=A-1/5, f^2+h^2<=B-1/5,
    e^2<=C, f^2<=C.                                    (W4)

PROVED: For the first inequality, project u^2-(1/5)1 onto the orthonormal vectors u,w; the second is its swapped version. For the last two, apply Cauchy-Schwarz to u and the coordinatewise product uw, and then to w and that product.

PROVED: Choose nonnegative theta_n,theta_j,theta_d,z1,z2,z3,z4 and set x=theta_n-theta_d, y=theta_j+theta_d. If both matrices

    [8/3-x-y+z1, 1+r-y;
     1+r-y, 2r(r+5)/3-x(1+2r)-y+z2+z4],

    [2(1+5r)/3-x(2+r)-yr+z1+z3, r(1+r)-yr;
     r(1+r)-yr, 8r^2/3-xr-yr+z2]                       (C1)

PROVED: are positive semidefinite, then (W4) and (W1) bound the cubic contribution from below. For arbitrary rational tangents t0,v0 put

    Ztan=a[2t0 f_r-(1+r)t0^2],
    Vtan=v0 S-v0^2/2,
    penalty=z1(A-1/5)+z2(B-1/5)+(z3+z4)C.

PROVED: The exact lower bound is

    T/a >= P_cell(a,r,A,B,C)
      =L+a H0+(theta_n+theta_j)Ztan
       -lambda[theta_n(2-K)+theta_j(4-K)+2theta_d]/5
       +theta_n Vtan-a penalty.                         (C2)

PROVED: To verify the signs, subtract xN_r+yJ_r from R_r and add z1(d^2+e^2)+z2(f^2+h^2)+z3e^2+z4f^2. This is exactly the sum of the two quadratic forms (C1). Next write xN_a+yJ_a=theta_n N_a+theta_j J_a+theta_d(J_a-N_a), apply the first strengthened bound in (W2), the old valid bound J_a>=Z-lambda(4-K)/5, and the last line of (W2). Finally use

    F^2/s>=Ztan, S^2/2>=Vtan.

PROVED: This yields (C2), with no optimization hypothesis. In particular, each saved multiplier tuple gives a sufficient condition P_cell>=0 for the actual moments at any positive scale, provided its ratio lies in the tuple's ratio interval. The saved scale ceiling is only a uniform guarantee over the entire moment polytope.

PROVED: strong_moment_cells.json gives 88 adjacent ratio cells of width 1/100 on [3/25,1]. Each scale interval starts at 443/1000. Every cell's multipliers, tangents, penalties and minimum are rational. enhanced_moment_cells.json gives further cells using the 33-vertex polytope. The precise list of all ceilings is in these files; the replay output gives combined interval summaries. The first collection alone proves a<=58/125 for all 0<r<=1: its smallest ceiling is 58/125, and the prior ratio-strip theorem handles r<=3/25.

PROVED: Here is how a complete cell is checked. Each entry in (C1) is quadratic in r. For a matrix polynomial M on [l,h], its three degree-two Bernstein control matrices are

    M(l), 2M((l+h)/2)-(M(l)+M(h))/2, M(h).

PROVED: Positive semidefiniteness of all three implies positive semidefiniteness of M throughout the interval, since the Bernstein basis is nonnegative and sums to one. Each 2-by-2 control matrix is checked by its two diagonal entries and determinant, using rational arithmetic. The right side of (C2) is affine in a, linear in A,B,C, and quadratic in r. It is enough to inspect both scale endpoints, every moment vertex, and the ratio endpoints plus any interior critical point of each scalar quadratic. Every inspected value is nonnegative.

PROVED: moment_bounds.py implements these exact checks. verify_strong_cells.py replays the first 88 cells; verify_all_cells.py re-enumerates both polytopes, replays both final collections and computes their combined scale coverage. discover_moment_cells.py uses one-thread Clarabel only to choose candidate multipliers, repairs them rationally, and exports a cell only after the exact check succeeds. Floating solver output alone is never accepted.

PROVED: Directional variance cells

PROVED: There is additional information in the same weighted-variance argument. For any real alpha,beta define

    p_ij=alpha u_i u_j+beta w_i w_j,
    k_ab=alpha^2 A+2alpha beta C+beta^2 B,
    m_ab=alpha(A+rC)+beta(C+rB),
    N_ab=a[alpha^2 d^2+2alpha beta e^2+beta^2 f^2]
         +b[alpha^2 e^2+2alpha beta f^2+beta^2 h^2],
    Z_ab=sum_i(Gmat)_ii(alpha u_i^2+beta w_i^2)^2,
    S_ab=alpha a+beta b-a m_ab-lambda(alpha+beta)/5.

PROVED: Exact pair expansion gives

    2 sum omega_ij p_ij=S_ab,
    2 sum omega_ij p_ij^2
        =N_ab-Z_ab+lambda(alpha^2+beta^2-k_ab)/5.

PROVED: Weighted variance and weighted Cauchy-Schwarz give

    N_ab >= a m_ab^2/(1+r)
            -lambda(alpha^2+beta^2-k_ab)/5+S_ab^2/2.    (D1)

PROVED: This inequality remains valid when alpha beta<0; N_ab need not itself be nonnegative. For each direction (alpha,beta) in {(1,1),(1,0),(0,1),(1,-1)}, choose a nonnegative multiplier theta and rational tangents t0,v0. Multiply the tangent lower bound in (D1) by theta. Subtract the corresponding theta N_ab/a from R_r, add theta_d(N_r-J_r) and the four Bessel penalties from (W4), and require the resulting two 2-by-2 blocks to be positive semidefinite. The resulting lower bound is

    P_direction=L+a H0-a penalty-2lambda theta_d/5
      +sum_directions theta {
          a[2t0 m_ab-(1+r)t0^2]
          -lambda(alpha^2+beta^2-k_ab)/5
          +v0 S_ab-v0^2/2 }.                            (D2)

PROVED: All residual matrices and the polynomial (D2) are implemented explicitly in directional_bounds.py. verify_directional_bounds.py verifies the arbitrary-alpha,beta edge identities symbolically, then matches every residual coefficient. verify_directional_cells.py checks each saved matrix control and scalar quadratic minimum using only rational arithmetic. Like (C2), (D2) is linear in moments, affine in scale and quadratic in ratio, so the same exhaustive cell verification applies.

PROVED: discover_directional_cells.py optimizes tangents through perspective cones rather than a grid. For each direction it introduces theta,q,c,v,d with theta*c>=q^2 and theta*d>=v^2. Their scalar expression is linear. The rational export uses t0=q/theta and v0=v/theta, recomputes c=theta*t0^2 and d=theta*v0^2 exactly, and accepts only a tuple that passes rational replay. Zero multipliers are handled separately. The floating conic solver has one thread; it is not needed by the verifier. The final collection is directional_moment_cells.json.

PROVED: The final collections contain 88 base cells, 44 enhanced-polytope cells, and 44 directional cells. verify_all_cells.py has replayed all 176. Their combined coverage includes the following rectangles; each extends down to a=0 using the earlier small-scale theorem:

    ratio interval        uniform scale ceiling
    [3/25,1/5]            103/200
    [1/5,2/5]             68/125
    [2/5,3/5]             289/500
    [3/5,4/5]             57/100
    [4/5,9/10]            561/1000
    [9/10,19/20]          277/500
    [19/20,1]             549/1000.                       (D3)

PROVED: The individual cell files often give higher ceilings than these coarser rectangles. The least combined ceiling is 103/200. Together with the old exact ratio strip 0<r<=3/25, this proves T>=0 for every admissible frame whenever a<=103/200. The prior 3/25 quartic SOS has also been independently replayed in this run; prior_quartic_replay.out records the exact coefficient match and all 286 rational PSD tests.

PROVED: A larger full equal-gap interval

PROVED: At a=b=g use K=A+B+2C and S=g(9/5-K)-1/5. The given equal-gap identity is

    45T/g=70K-28+g(112-190K+30N+90J),

PROVED: where N=N_a/g and J=J_a/g. Both are nonnegative. Applying (W2), either using only N's bound or both N's and J's bounds, gives

    45T/g >= PN(K,g)
      =15gK^2+(73-187g)K+106g-34+15S^2,
    45T/g >= PNJ(K,g)
      =60gK^2+(82-178g)K+70g-70+60S^2.                 (E1)

PROVED: Let G be the isolated cubic root stated at the beginning and put

    k*=(59G-11)/(5(19G-7)).

PROVED: Exact rational isolation gives 551/1000<G<69/125 and 123/100<k*<5/4. If p(g)=6272g^3-2989g^2-1034g+427 and k(g)=(59g-11)/(5(19g-7)), direct polynomial division gives

    PN(k(g),g)=6(g-1)p(g)/[5(19g-7)^2],
    PNJ(k(g),g)=24(g-1)p(g)/[5(19g-7)^2].             (E2)

PROVED: Hence both vanish at (k*,G). On 4/5<=K<=k*, PN(K,G) decreases: its K derivative is

    30K G(1+G)-54G^2-181G+73,

PROVED: which is at most -5499527/500000 using the rational enclosures above. On k*<=K<=7/5, PNJ(K,G) increases: its derivative is

    2[60K G(1+G)-108G^2-77G+41],

PROVED: which is at least 143287609/2500000. Thus PN(K,G)>=0 on the first interval and PNJ(K,G)>=0 on the second. To extend this algebraic assertion to every smaller g, differentiate the polynomials in g. For 4/5<=K<=k*,

    dPN/dg=15K^2-187K+106
            +30(9/5-K)[g(9/5-K)-1/5]
           <=-34+30(69/125-1/5)<0.

PROVED: Here 15K^2-187K+106 decreases on this K interval, and 0<9/5-K<=1. For k*<=K<=7/5, put k0=123/100 and h0=9/5-k0=57/100. Then

    dPNJ/dg=60K^2-178K+70
             +120(9/5-K)[g(9/5-K)-1/5]
            <=60k0^2-178k0+70
                +120h0[(69/125)h0-1/5]<0.

PROVED: The quadratic first part decreases for K<=7/5, and the second part has the stated upper bound whether its bracket is positive or negative. Both polynomials therefore decrease in g on their respective K intervals for 0<=g<=G. Their nonnegativity at G implies their nonnegativity at the actual g. Apply (E1) only at that actual admissible graph to obtain T>=0. This avoids assuming that a frame feasible at a smaller scale remains feasible at G. verify_equal_gap.py checks root uniqueness, (E2), and all rational derivative bounds in both variables.

PROVED: Exact coordinates on the zero-edge face

PROVED: Fix the zero edge {4,5}. Use six real coordinates t,v1,z1,v2,z2,z and the five row vectors

    V_1=(v1,z1), V_2=(v2,z2),
    V_3=(1-t-v1-v2,-z-z1-z2),
    V_4=(t,0), V_5=(-1,z).

PROVED: Put

    M=V^T V, R=VV^T, N=tr M, Delta=det M,
    D=20t-N, g_ij=t+V_i.V_j,
    Qnum=V adj(M) V^T,
    Pnum=Delta(5I-J)-5Qnum.

PROVED: The face domain is exactly t>0, Delta>0 and g_ij>=0 for all i<j. On this domain,

    lambda=10t/D, Gmat=2R/D,
    omega_ij=2g_ij/D, Q=Qnum/Delta,
    Pi=Pnum/(5Delta), g_45=0.                         (F1)

PROVED: The matrix 5t(I-J/5)-R is the Laplacian with weights g_ij, so it is positive semidefinite. Therefore M<=5t I, N<=10t and D>=10t>0. The weights in (F1) sum to one. Positivity of Delta gives two positive gaps. Their values are

    a=[N+sqrt(N^2-4Delta)]/D,
    b=[N-sqrt(N^2-4Delta)]/D.

PROVED: The graph is connected exactly when det(5t I-M)>0. The inequalities also imply 1/4<=t<=4 and every other coordinate has absolute value at most four: each row satisfies ||V_i||^2<=4t, and ||V_5||^2=1+z^2. Thus this is a bounded rational chart apart from its excluded lower-rank boundary.

PROVED: To see that the chart is exhaustive, factor Gmat/lambda=YY^T with two columns and Y^T1=0. The zero weight says Y_4.Y_5=-1/5, so Y_4 is nonzero. Rotate the two columns so Y_4=(x,0), x>0. Set t=5x^2 and V=sqrt(5t)Y. Then V_4=(t,0), the first coordinate of V_5 is -1, and zero column sums determine V_3 from the other rows. Trace normalization gives exactly lambda=10t/D. This constructs the chart from every zero-edge graph on the stratum.

PROVED: Define Rdiff_ij=R_ii+R_jj-2R_ij and Qdiffnum_ij=(Qnum)_ii+(Qnum)_jj-2(Qnum)_ij. The exact polynomial whose nonnegativity would settle this whole face is

    Cface=45 D^2 Delta T
      =Delta[1800t N-360tr(M^2)]
       +120 sum_ij (Pnum)_ij R_ij^2
       +(D-10t)[60N Delta-20 sum_i(Pnum)_ii R_ii]
       -360 sum_(i<j) g_ij(2Delta-Qdiffnum_ij)Rdiff_ij. (F2)

PROVED: Its denominator is positive on the face domain. zero_face.py constructs its 1,254 coefficients exactly and checks the normalization, projector identities, and equality with the trace formula. This is an exact reduction to a polynomial inequality, not a positivity certificate for all 1,254 terms. The new moment and cell certificates prove (F2)>=0 on the portions they cover, and (R1) extends their conclusions to the corresponding rays.

PROVED: Forty-seven exact boxes directly on the face

PROVED: zero_face_boxes.json contains 47 closed rational boxes in the coordinate order (t,v1,z1,v2,z2,z). On every box, rational inclusion arithmetic proves

    t>0, Delta>0, D>0, Cface>0.                       (F3)

PROVED: Therefore T>0 on the admissible portion of every box, including its zero edge {4,5}. All permutations of vertices and the common reflection (z1,z2,z)->(-z1,-z2,-z) preserve the assertion. Equation (R1) proves T>0 on every smaller positive point of a ray whose endpoint is in one of these boxes. The other weights need only be nonnegative at the point being considered; the certificate bounds the numerator on the entire box and then intersects it with the admissible face domain.

PROVED: The boxes were chosen around exact connected endpoints outside every general moment-cell test (C2),(D2). Forty-six enclosed endpoints also fail the strengthened nonlinear test (W3), where it applies. All five enclosed equal-gap endpoints lie above 69/125, so the cubic equal-gap theorem does not cover them. Thus the face boxes provide additional coverage beyond the uniform and moment-cell regions, including further portions of the large equal-gap region. They do not cover the whole face.

PROVED: Here is the exact interval certificate construction. A closed interval [l,h] has rational endpoints. Addition and subtraction use endpoint sums and differences; multiplication uses the minimum and maximum of the four endpoint products. Squaring uses zero as the lower bound if the interval contains zero, otherwise the smaller endpoint square. Evaluate the matrix expression (F2) by these operations, setting g_45 identically to zero. The file stores the lower endpoints for Delta,D,Cface; each is strictly positive. Since every operation encloses all values of the corresponding expression, (F3) follows by induction over the calculation. face_intervals.py implements only these rational operations. verify_face_boxes.py recomputes all 47 bounds and compares them exactly with the saved values. It also checks three degenerate-box evaluations independently against all 1,254 polynomial coefficients from zero_face.py.

PROVED: The exact endpoints enclosed by the boxes are recorded in residual_rays.json. For an endpoint, select a zero edge and relabel its vertices as 4,5. If Y Y^T=Gmat/lambda, the intrinsic chart coordinates satisfy

    t=5(Gmat)_44/lambda,
    v_i=5(Gmat)_i4/lambda,
    z_i=5 det(Y_4,Y_i).

PROVED: With u=U/sqrt(U.U), w=W/sqrt(W.W), the last coordinate is

    z_i=5 sqrt[ab/(lambda^2 (U.U)(W.W))]
             (U_4 W_i-W_4 U_i).

PROVED: All factors except one common square root are rational. source_chart encloses that square root with integer square-root arithmetic and checks its two rational endpoints by squaring. The verifier proves that this enclosure lies within the saved box. Thus the connection from an exact frame to its box uses no floating approximation. discover_face_boxes.py enlarged each uniform coordinate half-width by rational binary search before exporting the final verified box.

PROVED: Genuine enlargement and exact witnesses

PROVED: rational_ray_witnesses.json contains ten integer pairs U,W with sum U=sum W=U.W=0, a rational ratio r, and the rational zero-weight endpoint a_end. The normalized frame is u=U/sqrt(U.U), w=W/sqrt(W.W). All entries of Gmat and Q, all edge weights, all quadratic cubic-moment combinations, T, and the new bounds are rational. verify_rational_witnesses.py checks each witness independently. Every one is connected, has a zero weight, lies above the previous A0,A1,443/1000,W thresholds, fails the old moment sufficient condition and, where applicable, the old weight-moment sufficient condition, but satisfies a new cell bound. These are exact examples in the old unresolved region.

PROVED: The finite search tested 7,968 nonzero integer frames. Seventy-six endpoints passed all old unresolved-region filters; seventeen of those were covered by the then-available new cell bounds, and ten were saved. These are counts for that finite search, not a measure of the continuous region. The exact witnesses, rather than a sample percentage, certify genuine enlargement.

PROVED: With all final moment cells, 29 of the same 76 endpoints are covered by those tests. The remaining 47 are enclosed by the direct face boxes. This finite bank is now covered completely; it supplies no assertion that the continuous remaining region is covered.

NUMERICAL: Unsuccessful approaches

NUMERICAL: sextic_endpoint_certificate.py retained the actual extreme-u pair and the full R_w. At r=1/5 it certified 440 of 455 coefficient forms and left fifteen unresolved; at r=3/20 it certified 450 and left five unresolved. The selected extreme-u pair need not be the limiting edge. The incomplete JSON files are retained but are not certificates of either ratio strip.

NUMERICAL: A sample of 100,000 zero-edge endpoints found no positive fixed-frame tangent curvature, and one million frame/edge curvature evaluations also found none. A normalized-concavity SOS attempt certified 419 of 455 coefficient forms and left 36 unresolved. This does not prove a second face reduction. No inference from that sampler or incomplete SOS is used above.

PROVED: A further exact equal-gap experiment used a rotated basis with d=0. Such a basis exists because sum u_i^3 changes sign under u->-u. In that basis A<=1/2: Newton identities give e3=0 and sum u_i^4=(sum u_i^2)^2/2-4e4. The real-rooted polynomial with roots u_i has an even derivative with four real roots, so e4>=0. A conditional rational cell proves g<=551/1000. This is weaker than the cubic endpoint G and is not used to enlarge the final region. verify_equal_gap_rotation.py replays its Newton identities and cell certificate.

PROVED: What remains

PROVED: Let V(r) be the largest scale ceiling in strong_moment_cells.json, enhanced_moment_cells.json and directional_moment_cells.json whose closed ratio interval contains r. Let P_*(x,r,A,B,C) be the maximum of their lower bounds (C2),(D2) at scale x, using all multiplier records valid at that ratio. The lower bounds are valid outside their saved scale intervals too; those intervals only describe uniform coverage. For completeness define

    c_r=max(0,1-7r)(9+r)/24,
    A0(r)=14(1+r)/[34+52r-22r^2+12c_r],
    Ai(r)=min { L_v(r)/[-H0_v(r)+c_r C_v] :
                v in Vi, H0_v(r)-c_r C_v<0 }, i=1,2.

PROVED: V1 is the old nineteen-vertex polytope and V2 is the enhanced thirty-three-vertex polytope. An empty minimum is infinity. These are sufficient thresholds by the same vertex argument as the previous result. Define W(r) as the largest ceiling of a closed ratio cell in STRAT5/weight_moment_cells.json containing r, and zero if there is none.

PROVED: Every case still unproved by the old and new sufficient conditions must satisfy all of the following:

    3/25<r<=1, connected, a<2/(3-r),
    a>max(A0(r),A1(r),A2(r),W(r),V(r),103/200),
    if r=1, then a>G,
    min_(i<j) omega_ij < (lambda-a)/5,
    L(r)+a[H0(r)-c_r C]<0,
    P_*(a,r,A,B,C)<0,
    P_*(a_end,r,A,B,C)<0,
    if r>=3/5, the strengthened expression (W3) is negative
        both at a and at a_end.

PROVED: In addition, for every zero edge at the actual far endpoint, no chart obtained by relabeling that edge as {4,5} in either order, permuting the other three vertices, and choosing either common sign of the z coordinates belongs to any of the 47 boxes in zero_face_boxes.json. This is a finite explicit box-membership exclusion. If any such chart belonged to a box, (F3) and (R1) would prove the case.

PROVED: Here a_end=2/Dmax is given explicitly in (R1). If P_* at a_end were nonnegative, (R1) would cover the actual scale even if it failed a current-scale test. Likewise the true endpoint is already covered when it is disconnected. The unresolved endpoint therefore has at least one zero weight and is connected. Equations (F1),(F2), together with the failed sufficient conditions just listed, give an explicit six-variable version of the remaining face problem. No universal sign for Cface on that residual domain has been proved.

PROVED: Replay commands, from this folder

    python3 replay_all.py

PROVED: The individual replay commands are

    python3 verify_polya_moments.py
    python3 verify_new_bounds.py
    python3 verify_directional_bounds.py
    python3 verify_equal_gap.py
    python3 zero_face.py
    python3 verify_strong_cells.py
    python3 verify_directional_cells.py
    python3 verify_all_cells.py
    python3 verify_rational_witnesses.py
    python3 verify_face_boxes.py
    python3 verify_equal_gap_rotation.py

PROVED: Fraction-based cell and witness verification uses the Python standard library. Polynomial construction, root isolation and moment-matrix verification additionally use SymPy. NumPy, SciPy and Clarabel are needed only for certificate discovery; all solver settings use one thread. No network or language-model workers were used, and all writes were confined to this folder and its existing subdirectory.

PROVED: Task: “Prove T >= 0 on the rest of the connected n = 5, D = 2 stratum” — received 2026-11-13, approximately 03:18 +04.
