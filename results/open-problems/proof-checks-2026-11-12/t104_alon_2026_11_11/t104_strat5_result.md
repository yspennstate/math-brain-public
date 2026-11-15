PROVED: Partial result for the connected n = 5, D = 2 stratum. The whole remaining region is not closed. The new results are: the uniform strip 0 < b/a <= 3/25; the uniform scale bound a <= 443/1000; a larger, explicitly defined moment region; forty exact rational cells for 3/5 <= b/a <= 1; the equal-gap interval g <= (209+3 sqrt(305))/476; and all frames whose radial endpoint is disconnected. These results hold for every admissible frame, including connected graphs with some zero weights. The cases not covered are specified at the end.

NUMERICAL: The equal-gap endpoint above is approximately 0.549144427709494. The previous equal-gap endpoint was 7/16. The new ratio strip replaces the previous 1/3000 strip. Neither the numerical searches nor the unsuccessful certificate searches below prove the full inequality.

PROVED: Notation follows PREVIOUS_RESULT.md. Set r=b/a, s=a+b, K0=A+B+2C, F=a(A+C)+b(B+C), and lambda=(2+s)/4. Write the reduced formula (3) there as T=B0+R, where

    B0=(14+2s)(F-s/5)/9 + 4(a^2+b^2)/3
       -14(a^2 A+b^2 B)/3 -4(a^2+b^2+ab/3)C.

PROVED: For a fixed frame, the same formula is

    T(a,b)=a L_u+b L_w+a^2 P+ab Q0+b^2 R_w,
    L_u=14(A+C-1/5)/9,  L_w=14(B+C-1/5)/9,
    P=58/45-40A/9-34C/9+8d^2/3+2e^2/3+2df,
    Q0=2(A+B+2C-2/5)/9-4C/3
       +10(e^2+f^2)/3+2df+2he,

PROVED: where R_w is P with u,w interchanged. In particular, T(a,ar)/a is affine in a. This elementary radial fact is used below. The symbols R and R_w are different: R is the cubic contribution in the previous reduced formula, and R_w is the coefficient of b^2 in the radial polynomial.

PROVED: Additional moment bounds

PROVED: Every frame satisfies

    7/30 <= A,B <= 13/20,        0 <= C <= 3/10,
    A+C,B+C <= 4/5,             A+C,B+C >= 1/4,
    A+B+2C <= 7/5,              2C <= A+B.             (13)

PROVED: Here is an elementary proof of the upper bounds that improve the previous result. If Z is symmetric, Z1=0 and tr Z=0, let y=diag Z. Then sum y=0 and

    <Z,H diag(y) H>=||y||^2,
    ||H diag(y) H||_F^2=(3/5)||y||^2.

PROVED: The second identity follows from H_ii^2=16/25 and H_ij^2=1/25 for i!=j. Cauchy-Schwarz gives ||diag Z||^2 <= (3/5)||Z||_F^2. Apply this successively to Z=uu^T-H/4, Z=(uw^T+wu^T)/sqrt(2), and Z=Q-H/2. Their squared Frobenius norms are 3/4, 1, and 1. Their squared diagonal norms are A-1/5, 2C, and K0-4/5. This gives A<=13/20, C<=3/10 and K0<=7/5; interchange u,w for B. The bounds A+C,B+C<=4/5 follow from Q<=H. The last inequality in (13) is the sum of (u_i^2-w_i^2)^2>=0.

PROVED: The remaining lower bounds have small exact coefficient certificates. Order a nonzero zero-sum vector U decreasingly and write

    U=sum_(j=1)^4 z_j rho_j,  z_j>=0,
    (rho_j)_i=5-j if i<=j, and -j otherwise.

PROVED: This represents the whole ordered cone, because z_j=(U_j-U_(j+1))/5. Put t=||U||^2, q=sum U_i^4 and Delta=U_1-U_5. Define the 5-by-3 matrix K, indexed by j=2,3,4, by

    K_1j=U_5-U_j,   K_jj=Delta,   K_5j=U_j-U_1.

PROVED: All other entries vanish. Its columns are orthogonal to 1,U, and every W orthogonal to 1,U has the unique form K xi: the three middle coordinates give xi_j=W_j/Delta. Define R0=K^T K and C0=K^T diag(U_i^2)K. The scalar polynomial q-(7/30)t^2 has no negative coefficient in z. The matrix polynomial

    (q-t^2/4)R0+t C0

PROVED: has 84 coefficient matrices, one for each monomial of degree six; every one is positive semidefinite. On normalizing u=U/sqrt(t), w=W/||W||, its quadratic form divided by t^2||W||^2 is A+C-1/4. This proves the lower bounds in (13), including their versions with u,w interchanged. moment_explore.py constructs these polynomials using exact arithmetic. verify_moments.py independently matches all coefficients and checks the exported matrices by exact rational symmetric elimination. The data are in moment_lower_matrices.json. This is a finite rational certificate, not a floating eigenvalue test.

PROVED: A larger scale region

PROVED: Let V be the 19 vertices of the rational polytope (13), recorded in moment_vertices.json. For v=(A,B,C) in V define

    f_v(r)=A+rB+(1+r)C-(1+r)/5,
    L_v(r)=14 f_v(r)/9,
    c_r=(1-7r)_+(9+r)/24,
    H_v(r)=2(1+r)f_v(r)/9+4(1+r^2)/3
           -14(A+r^2 B)/3-[4(1+r^2+r/3)+c_r]C,
    A1(r)=min_(v in V, H_v(r)<0) L_v(r)/[-H_v(r)].    (14)

PROVED: An empty minimum in (14) means infinity. Every frame with a<=A1(r) has T>=0. Indeed, the previous square completion gives R>=-a^2 c_r C. Thus T/a is bounded below by the linear function of (A,B,C) whose vertex values are L_v+a H_v. Its minimum over the polytope occurs at a vertex, and L_v>=7(1+r)/90>0. This proves the assertion. The polytope is bounded; a vertex must have three independent active constraints, since otherwise a small displacement in both directions preserves all its constraints. Enumerating all such triples therefore finds every vertex. moment_region.py does this with exact rational solves; verify_cells.py repeats the enumeration independently using standard-library fractions and determinants.

PROVED: Some exact values of the sufficient threshold A1 are

    r       A1(r)
    0       448/1067
    1/10    415520/945851
    1/7     12887/28799
    1/4     3220/7033
    1/2     1162/2439
    3/4     1652/3403
    1       5/11.

PROVED: The value at r=0 is a boundary calculation. These are sufficient thresholds from this polytope, not optimal thresholds for genuine frames. verify_cells.py also checks exactly that every vertex inequality is nonnegative at a=443/1000 for r in [3/25,1], splitting at r=1/7. Each polynomial is quadratic in r, so endpoints and an interior quadratic minimum suffice. Affinity in a and positivity at a=0 cover every smaller a. Together with the next theorem this proves the uniform bound a<=443/1000 for every 0<r<=1.

PROVED: The ratio strip 0<r<=3/25

PROVED: Let alpha=max u_i, beta=-min u_i, p=alpha beta and v=alpha-beta. The residues (alpha-u_i)(beta+u_i)>=0 sum to 5p-1, so p>=1/5. Also p<=1/2 by 2alpha beta<=alpha^2+beta^2<=1. At a pair attaining -u_i u_j=p, projection of e_i+e_j onto span(u,w) gives

    (u_i+u_j)^2+(w_i+w_j)^2 <= 6/5.

PROVED: Consequently k_actual=1+20w_i w_j <= k=7-5v^2, and the weight constraint gives

    a[D0-r k_actual]<=2,  D0=20p-1.                  (15)

PROVED: In particular k_actual<=7, sharpening the previous coefficient 11. We also have v^2<=9/20. To see this, change the sign of u if necessary so that v>=0. The other three coordinates sum to -v and are each at least -beta. Hence beta>=v/3, and Cauchy-Schwarz gives

    1 >= (beta+v)^2+beta^2+v^2/3 >= 20v^2/9.

PROVED: It follows that 19/4<=k<=7. The coefficient R_w has the lower bound

    R_* = 58/45-40B/9-299C/72,                      (16)
    R_w-R_* = (8/3)(h+3e/8)^2+(2/3)f^2
              +(3/8)(C-e^2) >= 0.

PROVED: Here e^2<=C is Cauchy-Schwarz. Define the following quadratic in r for a fixed frame:

    Phi(r)=(9/2){(D0-rk)(L_u+r L_w)
                    +2(P+rQ0+r^2 R_*)}.             (17)

PROVED: This quadratic is concave. Its r^2 coefficient is (9/2)(-k L_w+2R_*), and (13), (16) imply

    -k L_w+2R_* <= 73/18-(565/36)(B+C)-(7/12)B
                <= 73/18-565/144-49/360
                 = -1/240.

PROVED: Phi(0)=E>=1/2 by the exact rank-one certificate (N3),(N4) in PREVIOUS_RESULT.md and the supplied rank_one_certificate.py. The new endpoint statement is

    Phi(3/25)>=0 for every orthonormal zero-sum u,w.   (18)

PROVED: Here is a complete finite certificate for (18). Use the ordered-cone U and K above, W=K xi, t=||U||^2 and n=||W||^2. Homogenize (17) at r=3/25:

    M(z,xi)=t^3 n^2 Phi(3/25).

PROVED: This is a polynomial homogeneous of degree ten in the four z variables and degree four in the three xi variables. Write m(xi)=(xi_1^2,xi_1xi_2,xi_1xi_3,xi_2^2,xi_2xi_3,xi_3^2). The file quartic_ratio_matrices_3_25.json supplies 286 rational matrices G_nu such that the exact identity is

    M(z,xi)=sum_(|nu|=10) z^nu m(xi)^T G_nu m(xi),
    G_nu positive semidefinite for every nu.          (19)

PROVED: The records contain a positive rational scale, a positive integer denominator and a symmetric integer matrix. Their product specifies G_nu exactly. verify_quartic_certificate.py reconstructs the left side from the radial coefficients L_u,L_w,P,Q0,R_* rather than the generator's E expression, matches every polynomial coefficient exactly, and checks all 286 matrices by rational symmetric elimination. Its successful output is saved in verify_quartic_certificate.out. SymPy and Python's standard-library fractions suffice to replay the proof; no SDP solver is needed. The generating program quartic_ratio_certificate.py uses a single-threaded floating SDP only to discover candidate matrices, then repairs their coefficients rationally and verifies positive semidefiniteness exactly before exporting them. Thus (19) proves (18).

PROVED: Concavity, Phi(0)>0 and (18) give Phi(r)>=0 on [0,3/25]. To finish the passage from (17) to T, put D=D0-r k_actual. For this interval, D>=3-7r>0. Equation (15) gives a<=2/D. At the radial endpoint a=2/D, the exact identity is

    T(a,ar)/a = 2 E_r/(9D),
    E_r=(9/2){D(L_u+r L_w)+2(P+rQ0+r^2 R_w)}
        >= Phi(r)>=0.

PROVED: The inequality uses k_actual<=k, L_u,L_w>=0 and (16). At the other endpoint, a=0 interpreted as a limit, T/a=L_u+rL_w>=7(1+r)/90>0. Since T/a is affine in a, it is nonnegative for the actual admissible a. This proves the entire new ratio strip.

NUMERICAL: The same quartic coefficient construction succeeds at r=1/10 and r=3/25. It does not produce certificates at r=123/1000, 31/250 or 1/8: respectively 1, 3 and 5 coefficient forms remain unresolved. These failures concern this particular lower bound and coefficient decomposition; they are not counterexamples to T>=0. Their outputs and partial matrices are retained. Earlier quadratic-matrix versions, retained as ratio_certificate.py and enhanced_ratio_certificate.py, certify r<=123/2000 and r<=367/5000. The quartic certificate supersedes those strip widths.

PROVED: Two useful inequalities from the edge weights

PROVED: Define

    N_a=a(d^2+2e^2+f^2)+b(e^2+2f^2+h^2),
    J_a=a(d+f)^2+b(e+h)^2,
    Z=sum_i G_ii q_i^2.

PROVED: Direct ordered-pair expansion gives

    2 sum_(i<j) w_ij Q_ij^2 = N_a-Z+lambda(2-K0)/5,
    2 sum_(i<j) w_ij q_i q_j = J_a-Z+lambda(4-K0)/5. (20)

PROVED: Every summand on the left is nonnegative. Weighted Cauchy-Schwarz, with weights G_ii>=0 and sum_i G_ii=s, gives Z>=F^2/s. Therefore

    N_a >= max(0,F^2/s-lambda(2-K0)/5),
    J_a >= max(0,F^2/s-lambda(4-K0)/5).               (21)

PROVED: The exact cubic identity

    R=(5b/3-a)N_a+s J_a
       +(8/3)(a-b)[a d^2+s e^2+b f^2]               (22)

PROVED: shows that, when r>=3/5, one can replace R in T=B0+R by (5b/3-a) times the first lower bound in (21), plus s times the second. This is also a new sufficient condition using the actual frame moments, valid beyond the uniform regions in this report. weight_moment_audit.py checks (20),(22) exactly by symbolic ordered-pair summation.

PROVED: Forty rational cells near equal gaps

PROVED: weight_moment_cells.json records forty adjacent ratio intervals of width 1/100 covering [3/5,1]. Each record gives a scale interval [4/11,a_hi], nonnegative rational multipliers theta_n<=5r_lo/3-1, theta_j<=1+r_lo, and a rational tangent t0. The following smaller rectangles summarize their coverage; the full file gives the larger individual ceilings.

    ratio interval          scale ceiling
    [3/5,7/10]              12/25
    [7/10,4/5]              99/200
    [4/5,9/10]              103/200
    [9/10,19/20]            53/100
    [19/20,99/100]          27/50
    [99/100,1]              109/200.

PROVED: Every smaller positive scale is covered too, because the previous result already proves a<=4/11. Here is the precise cell inequality. Set f=A+rB+(1+r)C, k0=A+B+2C, lambda=(2+a(1+r))/4, and let L_v,H_v be (14) with c_r=0. The tangent inequality

    F^2/s = a f^2/(1+r) >= a[2t0 f-(1+r)t0^2]

PROVED: and (21),(22) give T/a >= P_v(a,r), where

    P_v=L_v+a H_v
        +theta_n{a[2t0 f-(1+r)t0^2]-lambda(2-k0)/5}
        +theta_j{a[2t0 f-(1+r)t0^2]-lambda(4-k0)/5}.

PROVED: This is linear in the moment variables and affine in a. For every vertex v, it is quadratic in r. Each cell's certificate checks its minimum at the two a endpoints, and at the two r endpoints and any interior quadratic minimum. All checks use rational arithmetic, and all reported minima are nonnegative. verify_cells.py uses only standard-library fractions to enumerate the vertices again, verify every coefficient/multiplier bound, and replay these minima. Its successful output is verify_cells.out. Floating linear programs were used only to select multipliers; they do not enter the proof.

PROVED: A sharper equal-gap interval

PROVED: If a=b=g, write K=K0, N=d^2+3e^2+3f^2+h^2 and J=(d+f)^2+(e+h)^2. Then N_a=gN, J_a=gJ, F=gK and lambda=(1+g)/2. Equations (21) imply

    gN >= gK^2/2-(1+g)(2-K)/10,
    gJ >= gK^2/2-(1+g)(4-K)/10,

PROVED: as well as N,J>=0. Substitution into formula (7) of PREVIOUS_RESULT.md gives each of the two lower bounds

    45T/g >= P_N(K,g)=15gK^2+(73-187g)K+106g-34,
    45T/g >= P_NJ(K,g)=60gK^2+(82-178g)K+70g-70.

PROVED: Set k*=(sqrt(305)-5)/10 and g*=(209+3sqrt(305))/476. Both polynomials vanish at (K,g)=(k*,g*). We have 6/5<k*<5/4 and 1/2<g*<1. At g=g*, P_N decreases for 4/5<=K<=k*, because its derivative is at most 73-(299/2)g*<0. Thus P_N>=0 on that interval. On k*<=K<=7/5, the derivative of P_NJ is at least 82-34g*>0, so P_NJ>=0 there. At g=0, the corresponding expressions are 73K-34>0 and 82K-70>0 on these respective intervals. Affinity in g now proves T>=0 for every 0<g<=g*. The exact vanishing identities are checked in weight_moment_audit.py. This is a complete one-variable proof, independent of the rational cell ceilings.

PROVED: Connected graphs inherited from disconnected radial endpoints

PROVED: There is another region with no small-gap restriction. If

    u_i u_j+r w_i w_j >= -1/5 for every i<j,          (23)

PROVED: then T>=0 for every admissible a. Indeed, set a*=2/(3-r), b*=r a*. At this endpoint lambda*=a*, and its edge weights are a*[1/5+u_i u_j+r w_i w_j], which are nonnegative by (23). Its Laplacian has kernel containing 1,u, hence is disconnected. Its two top eigenvalues are exactly lambda*, so the disconnected theorem in PREVIOUS_RESULT.md applies. Affinity of T(a,ar)/a between a=0 and a=a* proves the assertion. More precisely,

    T >= (7/45)(a+b)(lambda-a) > 0                  (24)

PROVED: for connected graphs satisfying (23). The equality 1-a/a*=2(lambda-a) gives (24). Condition (23) is equivalent to w_ij>=(lambda-a)/5 for all pairs. Thus every connected graph obtained from a proved disconnected frame by adding a uniform complete graph is covered. In particular, this covers the family approached by the positive-floor quotient searches; it also covers connected examples with gaps well outside the scale and ratio regions above.

NUMERICAL: Connected margin measurements

NUMERICAL: connected_search.py ran 1,000 SLSQP starts at each floor epsilon=1e-3 and 1e-6, with seeds 131113 and 131114. Six Cayley coordinates construct an orthonormal zero-sum frame, with a,b optimized under all ten weight constraints, lambda-a>=0, and a positive denominator. The previous sparse family plus a complete graph seeds the known low basin; other starts are random or perturb a retained candidate. Bounds, tolerances, complete endpoint records and frames are in the script and connected_floor_*.json. The raw retained quotients are 0.0379814199843 and 0.0202946479864; the raw floor residuals are about -1.2e-11 and -9.6e-12. These are local-search values, not global lower bounds.

NUMERICAL: polish_connected.py scales both gaps slightly toward the complete graph, with a 2e-12 weight cushion. The saved polished_best records have every computed weight strictly above its required floor. The original trace formulas agree with the moment formulas to better than 1e-12, the spectra have the constructed repeated top eigenvalue to rounding, and the frame orthogonality errors are recorded. This numerical repair does not turn a floating point frame into an exact rational certificate.

PROVED: Separate exact connected witnesses avoid that issue. Starting with l=32/5 in the previous rational sparse family, put w_e=(1-10epsilon)w_e^0+epsilon on all ten pairs. All weights are at least epsilon, the total is one, the gaps are multiplied by 1-10epsilon and lambda gains 5epsilon after that scaling. Thus exact top multiplicity two is preserved and the graph is connected. rational_connected_family.py evaluates the matrices using rational arithmetic and obtains

    epsilon       exact quotient
    1/1000        3035108992/79790990305
    1/1000000     1571443463992/77430760925305.

NUMERICAL: These exact quotients are approximately 0.0380382419168 and 0.0202948214019. As epsilon tends to zero, the quotient tends to the previous family's value at l=32/5. The same construction at its algebraic minimizing parameter tends to 0.020276351509456. Thus connected graphs with all weights positive can approach that disconnected value. No larger uniform connected quotient bound is established by these measurements.

PROVED: What remains

PROVED: For the regions proved here, define W(r) as the largest a_hi among cells in weight_moment_cells.json whose closed ratio interval contains r, and put W(r)=0 outside [3/5,1]. Every case not covered by these results or the previous theorems must satisfy all of the following conditions:

    the graph is connected;
    3/25 < r <= 1 and a < 2/(3-r);
    a > max(A0(r), A1(r), 443/1000, W(r));
    if r=1, then a > (209+3sqrt(305))/476;
    min_(i<j) w_ij < (lambda-a)/5;
    the previous moment sufficient condition (5) fails;
    when r>=3/5, the sufficient bound B0+(5b/3-a)max(0,Z_N)
        +s max(0,Z_J) is negative, where
        Z_N=F^2/s-lambda(2-K0)/5,
        Z_J=F^2/s-lambda(4-K0)/5.

PROVED: This is an explicit description of the part left by the certificates, not a proof of failure there. In particular, the full equal-gap interval above g*, and substantial connected portions at intermediate ratios and large a, remain open. Global optimality of the quotient is also open.

PROVED: Exact proof replay, with Python 3 and SymPy, is

    python3 moment_explore.py
    python3 verify_moments.py
    python3 verify_quartic_certificate.py quartic_ratio_matrices_3_25.json
    python3 weight_moment_audit.py
    python3 verify_cells.py
    python3 rational_connected_family.py

PROVED: The prior rank-one base certificate can be replayed with the supplied rank_one_certificate.py. The new SOS endpoint can be regenerated, if desired, with python3 quartic_ratio_certificate.py 3/25; regeneration additionally uses NumPy, SciPy and Clarabel, with solver threads fixed to one. The saved rational certificate requires none of those floating solvers for verification.

PROVED: Task: “close the rest of the connected n = 5, D = 2 stratum” — received 2026-11-13 at approximately 02:19 +04.
