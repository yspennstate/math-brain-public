PROVED: Five vertices, top multiplicity two

PROVED: The formula for T is derived below. The inequality T >= 0 is proved for every disconnected graph on this stratum, with equality precisely at the balanced triangle with two isolated vertices and at two equal disjoint edges with one isolated vertex. For arbitrary frames it is proved on an explicit region in (g1,g2), including g1 <= 4/11 and, when g1=g2=g, the interval g <= 7/16. A uniform near-D3 region 0<g2/g1<=1/3000 is also proved. A further sufficient condition uses the actual frame moments.

NUMERICAL: The smallest quotient found in 14,400 full-stratum optimization starts is

    T/(X1+X2+X3) = 0.0202763515094560301327873177728729744...

NUMERICAL: This is the estimated global infimum, not a proved global lower bound. It occurs at a triangle with a pendant vertex and one isolated vertex. Its minimum within that one-parameter family is characterized exactly below. In particular, C5 is not the global minimizer of this quotient. The unrestricted connected stratum remains open.

PROVED: Notation and trace formulas

PROVED: Put a=g1, b=g2, s=a+b, H=I-J/5, and Q=uu^T+ww^T. Then

    0 < b <= a <= lambda <= 1,   lambda=(2+s)/4,
    Pi=H-Q,   G=a uu^T+b ww^T,
    w_ij=lambda/5+G_ij.

PROVED: The bounds a,b <= lambda follow from L >= 0. The bound lambda <= 1 follows from tr L=2 and the two top eigenvalues. All formulas below use total edge weight one.

PROVED: Define the frame moments

    A=sum u_i^4,       B=sum w_i^4,       C=sum u_i^2 w_i^2,
    d=sum u_i^3,       e=sum u_i^2 w_i,
    f=sum u_i w_i^2,   h=sum w_i^3,
    O1=sum u_i^3 w_i,  O2=sum u_i w_i^3,
    q_i=u_i^2+w_i^2,   p_i=Pi_ii=4/5-q_i,
    F=sum q_i G_ii=a(A+C)+b(B+C),   k2=a^2+b^2.

PROVED: In terms of these moments the complete closed form is

    K=a^2 A+b^2 B+2ab C-k2/5
      -a^2(d^2+e^2)-2ab(e^2+f^2)-b^2(f^2+h^2),

    X1=2[lambda s-k2],
    X2=(10/3)K,
    X3=(1-lambda)/3 [2s-(10/3)sum p_i G_ii]
      =(1-lambda)/9 [10F-2s],

    S5=(lambda/5)[6s-5a(A+C)-5b(B+C)]
       +a^2(-2+4A-3d^2)+b^2(-2+4B-3h^2)
       -3ab(e^2+f^2)
       -s[a(df+2e^2-2C)+b(he+2f^2-2C)],

    T=X1+X2+X3-2S5.                                      (1)

PROVED: O1 and O2 have coefficient zero. This cancellation uses both u.w=0 and the zero sums. Thus (1) is a closed form in the requested moments, with no omitted dependence on the odd fourth moments.

PROVED: Here is a derivation from the definitions, independently of numerical checks. The trace formulas are

    X1=2[lambda tr G-tr G^2],
    X2=(10/3) sum_ij Pi_ij G_ij^2,
    X3=(1-lambda)/3 [2 tr G-(10/3)sum_i Pi_ii G_ii],
    S5=sum_{i<j} w_ij tau_ij gamma_ij,
    tau_ij=2-(u_i-u_j)^2-(w_i-w_j)^2,
    gamma_ij=a(u_i-u_j)^2+b(w_i-w_j)^2.

PROVED: In the expression for X2, expand Pi_ij=delta_ij-1/5-u_i u_j-w_i w_j. The diagonal contribution is a^2 A+b^2 B+2ab C; the constant contribution is -k2/5. The remaining two terms are

    -a^2(d^2+e^2)-2ab(e^2+f^2)-b^2(f^2+h^2).

PROVED: For X3, sum Pi_ii G_ii=(4/5)s-F. For S5, write U_ij=u_i-u_j and W_ij=w_i-w_j. The following pair sums give every term in (1):

    sum U_ij^2=5,              sum W_ij^2=5,
    sum U_ij^4=5A+3,           sum W_ij^4=5B+3,
    sum U_ij^2 W_ij^2=5C+1,
    sum u_i u_j U_ij^2=-1,    sum w_i w_j W_ij^2=-1,
    sum u_i u_j W_ij^2=0,     sum w_i w_j U_ij^2=0,
    sum u_i u_j U_ij^4=3d^2-4A,
    sum w_i w_j W_ij^4=3h^2-4B,
    sum u_i u_j W_ij^4=3f^2,
    sum w_i w_j U_ij^4=3e^2,
    sum u_i u_j U_ij^2 W_ij^2=df+2e^2-2C,
    sum w_i w_j U_ij^2 W_ij^2=he+2f^2-2C.                (2)

PROVED: Every sum in (2) is over i<j. To verify them, expand the summand, take half the ordered sum over i,j, and replace each separated factor by the corresponding moment. Diagonal terms vanish because a difference is present. For example, the last-but-one ordered expansion gives df+2e^2-2C; terms containing sum u, sum w or sum uw vanish. exact_audit.py implements exactly this symbolic summation rule and verifies all fifteen identities with rational arithmetic. Substituting w_ij=lambda/5+a u_i u_j+b w_i w_j proves (1).

PROVED: A useful reduced formula and a general region

PROVED: Define

    R=(8/3)a^2 d^2+(8/3)b^2 h^2
      +(2/3)a(a+5b)e^2+(2/3)b(b+5a)f^2
      +2s(adf+bhe).

PROVED: Equation (1), after collecting terms, is equivalently

    T=(14+2s)/9 (F-s/5)+(4/3)k2
      -(14/3)(a^2 A+b^2 B)-4(k2+ab/3)C+R.              (3)

PROVED: The cubic contribution has the square completion

    R=(8/3)a^2[d+3s f/(8a)]^2
      +(8/3)b^2[h+3s e/(8b)]^2
      +(7b-a)(b+9a)f^2/24
      +(7a-b)(a+9b)e^2/24.                            (4)

PROVED: Consequently R >= 0 if b/a >= 1/7. For all 0<b<=a, put

    c=(a-7b)_+ (9a+b)/24,   x_+=max(x,0).

PROVED: The second residual coefficient in (4) is nonnegative. The possibly negative first residual term is at least -c f^2. Cauchy-Schwarz gives f^2=(sum (u_i w_i)w_i)^2 <= C, so R >= -c C. Thus the following sufficient condition proves T >= 0 for any admissible frame:

    (14+2s)/9 (F-s/5)+(4/3)k2
      -(14/3)(a^2 A+b^2 B)-[4(k2+ab/3)+c]C >= 0.      (5)

PROVED: There is also a region requiring no frame information. Let r=b/a and define

    D(r)=34+52r-22r^2+(1-7r)_+(9+r)/2,
    A0(r)=14(1+r)/D(r).

PROVED: Every graph on the stratum with a <= A0(r) has T >= 0. In particular, a <= 4/11 suffices for every r, and A0(1)=7/16.

PROVED: To prove this, q_i<=4/5 follows from Q<=H, and A,B>=1/5 follows from Cauchy-Schwarz. Therefore

    s/5 <= F <= 4s/5.

PROVED: The exact nonnegative remainder

    (14/3)a F-[(14/3)(a^2 A+b^2 B)+4(k2+ab/3)C]
      =(14/3)b(a-b)B+(2/3)(a-b)(a+6b)C >= 0

PROVED: and C<=F/s imply, with kappa=14a/3+c/s and delta=(14+2s)/9-kappa,

    T >= delta F-(14+2s)s/45+(4/3)k2.                 (6)

PROVED: If delta>=0, use F>=s/5. Since c<=3a^2/8, the result is

    T >= (a^2/15)(6-14r+20r^2)-c/5
      >= (97/600)a^2 > 0.

PROVED: The last inequality uses 6-14r+20r^2=20(r-7/20)^2+71/20. If delta<0, use F<=4s/5 in (6). This gives

    T >= (a/15)[14(1+r)-a D(r)] >= 0,

PROVED: as asserted. Finally A0(r)>=4/11: after clearing positive denominators the difference is proportional to 70r+102r^2 for r<=1/7, and to 18-54r+88r^2 for r>=1/7. The first is nonnegative and the second has positive leading coefficient and negative discriminant. This completes the proof of the region.

PROVED: A uniform region near the D=3 boundary

PROVED: For every graph on the stratum,

    0 < b/a <= 1/3000  implies  T >= 2a/2025 > 0.       (N1)

PROVED: The proof uses a certificate for the continuous b=0 boundary while retaining the chosen rank-two Pi. This boundary functional is not the D=3 functional with its full three-dimensional top projector. Fix any orthonormal zero-sum u,w and use Pi=H-uu^T-ww^T throughout this section.

PROVED: First, for every feasible rank-one gap a>0, the boundary functional satisfies

    T(a,0) >= a/81.                                   (N2)

PROVED: To prove (N2), let p=max(-u_i u_j). The residue sum sum(max u-u_i)(-min u+u_i)=5p-1 gives p>=1/5; also p<=1/2. Rank-one weight nonnegativity is equivalent to a<=amax=2/(20p-1). Formula (3) shows that T(a,0)/a is affine in a. At a=amax it equals

    2E/[9(20p-1)],
    E=140p(A+C)-28p-47A-41C+13+24d^2+6e^2+18df.        (N3)

PROVED: The exact certificate below gives E>=1/2 for every orthonormal zero-sum pair. Thus (N3) is at least 1/81. At a=0, interpreted as a limit, T(a,0)/a=(14/9)(A+C-1/5)>=7/540>1/81. Here is a short elementary bound for this last step. If the positive coordinates of u have sum S and number k, Cauchy-Schwarz on the two signs gives S^2<=k(5-k)/5<=6/5. Hence (sum |u_i|)^2<=24/5. Holder's inequality gives 1=(sum u_i^2)^3 <= (sum |u_i|)^2 A, so A>=5/24. Affine interpolation now proves (N2).

PROVED: The following fully specified matrix certificate proves E>=1/2. Order a nonzero zero-sum five-vector U decreasingly and write

    U=sum_{j=1}^4 z_j rho_j,   z_j>=0,
    (rho_j)_i=5-j for i<=j, and -j for i>j.

PROVED: This is the entire ordered cone, with z_j=(U_j-U_{j+1})/5. Put

    t=U^T U,   q=sum U_i^4,   d0=sum U_i^3,
    p0=-U_1 U_5,   Delta=U_1-U_5>0.

PROVED: Define a 5-by-3 matrix K, with columns indexed j=2,3,4, by

    K_1j=U_5-U_j,   K_jj=Delta,   K_5j=U_j-U_1,
    all its other entries zero.

PROVED: Each column is orthogonal to 1 and U. Every vector W orthogonal to 1,U has the form W=K xi: its three middle coordinates determine xi_j=W_j/Delta, and the two orthogonality equations determine its first and last coordinates. Define

    R0=K^T K,
    C0=K^T diag(U_i^2)K,
    F0=K^T diag(U_i)K,
    e0=K^T (U_i^2)_i,
    alpha=140p0 q-28p0 t^2-47qt+13t^3+24d0^2,

    M=alpha R0+(140p0 t-41t^2)C0+6t e0 e0^T+18t d0 F0
      -(1/2)t^3 R0.                                  (N4)

PROVED: Homogenizing (N3), for u=U/sqrt(t), w=W/||W||, gives

    E-1/2 = xi^T M xi / (t^3 ||W||^2).

PROVED: Expand M=sum_{|nu|=8} z^nu M_nu. There are 165 coefficient matrices, all symmetric 3-by-3 rational matrices. Every principal minor of every M_nu is positive: rank_one_certificate.py computes the matrices by exact polynomial expansion and verifies all 1,155 principal minors. Thus M_nu is positive semidefinite, M is positive semidefinite for z>=0, and E>=1/2. The exported file rank_one_matrices.json records twice each matrix as integers. recheck_matrices.py independently rechecks every principal minor using standard-library integer determinants and compares the coefficient sum to (N4) at twenty integer cone points. The script, the construction (N4), and the minor test are an exact rational certificate a reader can rerun; no floating-point eigenvalue test enters this argument. This proves (N2).

PROVED: We next compare a feasible rank-two graph to a feasible rank-one graph with the same u and Pi. Write p=max(-u_i u_j), choose a pair attaining p, and use w_i w_j<=1/2 in its weight constraint. This gives

    a(20p-1)<=2+11b.

PROVED: Therefore a0=2a/(2+11b) is rank-one feasible. The moment formula has the form

    T(a,b)=a L_u+b L_w+a^2 P+ab Q0+b^2 R,
    L_u=(14/9)(A+C-1/5),   L_w=(14/9)(B+C-1/5),
    P=(2/9)(A+C-1/5)+4/3-(14/3)A-4C
      +(8/3)d^2+(2/3)e^2+2df,
    Q0=(2/9)(A+B+2C-2/5)-(4/3)C
       +(10/3)(e^2+f^2)+2df+2he,

PROVED: with R obtained from P by swapping u and w. The uniform bounds

    0<=L_u,L_w<=1,   |P|,|R|<=5,   |Q0|<=6            (N5)

PROVED: follow as follows. We already have A+C,B+C<=4/5. Bessel's inequality applied to u^2-(1/5)1 and the orthonormal vectors u,w gives d^2+e^2<=A-1/5; similarly f^2+h^2<=B-1/5. Also d^2<=A-1/5, and f^2<=C by Cauchy-Schwarz, so 2|df|<=d^2+f^2<=A+C-1/5<=3/5; in the same way h^2<=B-1/5 and e^2<=C give 2|he|<=h^2+e^2<=B+C-1/5<=3/5. In P, the sum of the nonnegative terms excluding 2df is at most 46/15, and (14/3)A+4C<=56/15. Thus |P|<=65/15<5; the same holds for R. Finally

    |Q0| <= 4/15+(4/3)C+(13/3)(e^2+f^2)+d^2+h^2
          <= 4/15+(4/3)C+(13/3)(A+B-2/5)
          <= 82/15 < 6,

PROVED: using A+B+2C<=8/5. This proves (N5).

PROVED: If b/a<=1/3000, then b<=1/3000. Since p>=1/5, the same weight inequality gives a<=(2+11b)/3<27/40. Also

    a-a0<=11ab/2<=(297/80)b,
    a+a0<=27/20,
    a0>=(499/500)a.

PROVED: Equations (N5) yield

    |T(a,b)-T(a0,0)|
      <=[1+5(a+a0)](a-a0)+b+6ab+5b^2
      <=[(31/4)(297/80)+1+81/20+1/600]b < 34b.

PROVED: Combining this with (N2) proves

    T(a,b)>=(499/40500)a-34b
           >=[499/40500-34/3000]a=2a/2025,

PROVED: which is (N1). The use of the actual weight constraint in the comparison to a0 is essential to this proof.

PROVED: Equal gaps and rotation invariance

PROVED: If a=b=g, set Q=uu^T+ww^T and define the basis-independent quantities

    K0=sum_i Q_ii^2=A+B+2C,
    N=sum_ij Q_ij^3=d^2+3e^2+3f^2+h^2,
    J=(diag Q)^T Q(diag Q)=(d+f)^2+(e+h)^2.

PROVED: Then

    T=(g/45)[70K0-28+g(112-190K0+30N+90J)].            (7)

PROVED: The displayed expressions in Q show directly that rotating (u,w) leaves (7) unchanged. N,J>=0, and 4/5<=K0<=8/5: the lower bound is Cauchy-Schwarz with sum Q_ii=2; the upper bound follows from Q_ii<=4/5 and sum Q_ii=2. If 0<g<=7/19, (7) gives T>=(g/45)(28-40g)>0. If 7/19<=g<=7/16, it gives T>=(g/45)(84-192g)>=0. This is an independent short proof of the equal-gap interval above. More generally, the actual value of K0 proves T>=0 whenever

    70K0-28+g(112-190K0) >= 0.                         (8)

PROVED: Condition (8) can cover frames beyond g=7/16; it is the equal-gap specialization of a moment bound, not a claim for all equal-gap frames. For example, a constant-diagonal rank-two Q has K0=4/5 and satisfies (8) for every g<=7/10.

PROVED: Every graph with an isolated vertex

PROVED: Suppose vertex 5 is isolated. Its zero-sum contrast with the other four vertices is a gap eigenvector of eigenvalue lambda. Choose

    u=(1,1,1,1,-4)/sqrt(20),   a=lambda,
    w=(v_1,v_2,v_3,v_4,0),   sum v_i=0,   sum v_i^2=1.

PROVED: If the gaps agree this choice is permitted by rotation. Otherwise the zero Laplacian eigenvalue forces the larger gap to equal lambda. The trace gives b=3lambda-2, so lambda=(2+b)/3 and 0<b<=1. On the four nonisolated positions,

    w_ij=lambda/4+b v_i v_j,
    Pi=I_4-J_4/4-vv^T.

PROVED: Put q=sum v_i^4, m=(sum v_i^3)^2, and p=max_{i<j}(-v_i v_j). Direct substitution into the trace formulas gives

    X1=2b(lambda-b),
    X2=(10/3)b^2(q-1/4-m),
    X3=(1-lambda)/3[(5/3)lambda-b/2+(10/3)bq],
    2S5=2b[(lambda/4)(5-4q)+b(-2+4q-3m)],

    T=[20+(276q-73)b+(161-708q+432m)b^2]/162.           (9)

PROVED: These formulas follow by the same ordered-pair expansions as (2), with four coordinates. They can also be checked by substituting the displayed Pi and weights. The u contribution is constant on these four coordinates and cancels from edge differences.

PROVED: We have q>=1/4 and m<=q-1/4, the latter by applying Cauchy-Schwarz to v and v^2-(1/4)1. Thus the quadratic coefficient in (9) satisfies

    161-708q+432m <= 53-276q <= -16.

PROVED: Therefore (9) is a strictly concave quadratic in b. Write alpha=max v_i>0 and beta=-min v_i>0. Then p=alpha beta and

    sum_i (alpha-v_i)(beta+v_i)=4p-1 >= 0.

PROVED: Nonnegative weights give

    p>=1/4,   b <= bmax=2/(12p-1) <= 1.                (10)

PROVED: It suffices by concavity to check (9) at b=0 and b=bmax. The first value is 10/81>0. The second is

    T(bmax)=E/[9(12p-1)^2],
    E=96m+160p^2+368pq-124p-188q+45.                   (11)

PROVED: Here is a complete coefficient certificate for E>=0. Permute the coordinates of an arbitrary nonzero zero-sum four-vector V into decreasing order and write

    V=(3x+2y+z, -x+2y+z, -x-2y+z, -x-2y-3z),
    x,y,z>=0.

PROVED: This representation holds with x=(V1-V2)/4, y=(V2-V3)/4 and z=(V3-V4)/4. Let R0=sum V_i^2, P3=sum V_i^3, P4=sum V_i^4 and ph=-V1 V4. Upon normalizing v=V/sqrt(R0), E=Eh/R0^3, where

    Eh=96P3^2+160ph^2 R0+368ph P4
       -124ph R0^2-188P4 R0+45R0^3.

PROVED: Define

    h0(X,Y)=48X^4+47X^3Y-20X^2Y^2-28XY^3+24Y^4,

    M=332x^3+416x^2y+124x^2z+268xy^2+162xyz+124xz^2
      +184y^3+268y^2z+416yz^2+332z^3.

PROVED: The exact identity is

    Eh/2048=xy h0(x,y)+zy h0(z,y)
            +96xz(x^4+z^4)+92x^2z^2(x-z)^2
            +144x^3z^3+xyz M.                         (12)

PROVED: All terms on the right are nonnegative. For the only terms whose sign is not immediate, if X=Y+t with t>=0 then

    h0(Y+t,Y)=48t^4+239t^3Y+409t^2Y^2+265tY^3+71Y^4;

PROVED: if Y=X+t with t>=0 then

    h0(X,X+t)=24t^4+68t^3X+40t^2X^2+19tX^3+71X^4.

PROVED: These expansions prove h0>=0 throughout the nonnegative quadrant. The exact identities (11), (12), and both expansions are checked in isolated_certificate.py using integer/rational polynomial arithmetic. This proves the theorem for every isolated-vertex graph, using the weight constraint (10).

PROVED: In (12), Eh=0 only when precisely one of x,y,z is positive. These three rays give p=1/4 and bmax=1. Strict concavity and T(0)>0 then show that T can vanish only at b=1, lambda=1. The graph has Laplacian rank two. A nonnegative five-vertex graph of rank two has three components: either a three-vertex component or two two-vertex components, with the remaining vertices isolated. A three-vertex component with both positive eigenvalues equal to one has Laplacian I_3-J_3/3, hence is the balanced triangle. Two edge components each have eigenvalue one precisely when both edge weights are 1/2. Both graphs have T=0 by (9).

PROVED: The remaining disconnected case, component sizes three and two

PROVED: A disconnected graph without isolated vertices has component sizes three and two. If the three-vertex component contributes both top eigenvalues, its Laplacian is lambda(I_3-J_3/3), and the edge component has a smaller eigenvalue. On triangle edges gamma_ij=0; on the two-vertex edge tau_ij=0. Thus S5=0 and T>=0 because X1,X2,X3>=0.

PROVED: To justify this last general positivity assertion, X1=2[a(lambda-a)+b(lambda-b)]>=0; X2>=0 by the Schur product theorem applied to Pi and G; and X3=(1-lambda)(10F-2s)/9>=0 from lambda<=1 and F>=s/5.

PROVED: Otherwise one top eigenvalue comes from each component. On the three-vertex component the two positive eigenvalues are lambda and mu<lambda. Set b=lambda-mu and again a=lambda, lambda=(2+b)/3. Its weights and top projector are

    w_ij=lambda/3+b v_i v_j,   sum_{i=1}^3 v_i=0,
    sum v_i^2=1,   Pi_3=I_3-J_3/3-vv^T.

PROVED: On the two-vertex component L=lambda(I_2-J_2/2) and Pi=I_2-J_2/2. The gap eigenvector for a=lambda is constant on each component, with squared entries 2/15 on the triangle component and 3/10 on the edge component. Let m=(sum v_i^3)^2. Since sum v_i^4=1/2 for three zero-sum unit coordinates, the trace terms reduce to

    X1=2b(lambda-b),
    X2=(10/3)b^2(1/6-m),
    X3=(1-lambda)(5lambda+13b)/27,
    2S5=b lambda-6b^2 m,
    T=[10+196b-314b^2+648b^2 m]/243.                  (13)

PROVED: For completeness, the identity sum v_i^4=1/2 follows by squaring v1v2+v1v3+v2v3=-1/2: its cross term is 2v1v2v3(sum v_i)=0. The pair expansions giving (13) are (2) with three coordinates. The constant gap vector has zero difference inside each component. Its contribution to sum Pi_ii G_ii is (13/30)lambda; the v contribution is b/6. This proves the X3 formula as well.

PROVED: Write alpha=max v_i, beta=-min v_i, and p=alpha beta. The third coordinate is beta-alpha, so

    1/3 <= p <= 1/2,
    (alpha-beta)^2=1/2-p,
    m=9p^2(1/2-p).

PROVED: The lower bound for p follows from sum (alpha-v_i)(beta+v_i)=3p-1>=0. The upper bound follows from 1=2(alpha^2+beta^2-alpha beta)>=2p. The cubic identity uses sum v_i^3=3v1v2v3. Nonnegative weights give p<=P=(2+b)/(9b).

PROVED: If 0<b<=4/7, discard m>=0 in (13). The remaining numerator 10+196b-314b^2 is concave and positive at both endpoints of [0,4/7] (values 10 and 954/49), hence positive throughout. If 4/7<=b<1, then P is in [1/3,1/2], and the function 9p^2(1/2-p) decreases on that interval. Thus m>=9P^2(1/2-P), giving

    T >= 2(1-b)(143b^2-3b-32)/(243b) > 0.             (14)

PROVED: The quadratic in (14) is increasing for b>=4/7 and equals 636/49 there. This proves (14). The endpoint b=1 would give mu=0, so the three-vertex component would not be connected. It is already covered by the isolated-vertex theorem. This completes the proof for all disconnected graphs and the equality classification stated at the beginning.

PROVED: The numerical minimizing family, exactly specified

PROVED: For any l>3, put D0=l^2-l-3 and assign the following edges, with vertex 4 isolated:

    w_01=w_03=A0=(l-2)/D0,
    w_02=B0=l(l-3)/(2D0),
    w_13=C0=(l-2)(l-1)/(2D0),
    all other weights zero.                           (15)

PROVED: These weights are positive on the four specified edges and 2A0+B0+C0=1. The spectrum is

    0, 0, mu, lambda, lambda,
    lambda=l(l-2)/D0,   mu=2(l-3)/D0,
    g1=lambda,   g2=(l^2-4l+6)/D0.

PROVED: Indeed, the antisymmetric vector on vertices 1,3 has eigenvalue A0+2C0=lambda. On vectors equal at vertices 1,3, the two nonzero quotient eigenvalues satisfy t^2-(3A0+2B0)t+4A0 B0=0, whose roots are the displayed lambda and mu. Their difference is (l^2-4l+6)/D0>0, proving exact top multiplicity two.

PROVED: Substitution into (1), or direct rational evaluation of the matrices, gives

    T=2(l-3)(3l^4-43l^3+215l^2-406l+297)
      /[9(l^2-4l+6)D0^2],

    X1+X2+X3=2(l-3)(21l^4-133l^3+413l^2-748l+621)
      /[9(l^2-4l+6)D0^2],

    R(l)=T/(X1+X2+X3)
        =(3l^4-43l^3+215l^2-406l+297)
         /(21l^4-133l^3+413l^2-748l+621).              (16)

PROVED: The denominator is positive for l>3, since X1>0 there. Writing t=l-3, the derivative numerator of R is

    18[28t^6+140t^5-31t^4-1250t^3-3282t^2-3960t-1638].

PROVED: In descending order its nonzero coefficients have one sign change. Descartes' rule, the negative value at t=0, and the positive leading coefficient show that it has exactly one positive root t*. The derivative is negative before that root and positive after it. Consequently the exact minimum of (16) over this entire family is R(3+t*). This is a proved algebraic characterization; no claim of global optimality on other frames follows from it. sparse_family.py recomputes the matrices and formulas in exact arithmetic before the high-precision root solve.

PROVED: There is also a simple rational witness that C5 does not minimize the quotient globally. Take l=32/5 in (15): w_01=w_03=110/789, w_02=272/789, w_13=99/263, with all other edges zero. Its spectrum is 0,0,170/789,704/789,704/789 and its quotient is 55411/2732767<1/40. For C5, a low frame is u_i=sqrt(2/5)cos(2pi i/5), w_i=sqrt(2/5)sin(2pi i/5), and g=1/sqrt(5). The sums of its first and third harmonics vanish, giving K0=4/5 and N=J=0. Equation (7), together with X1+X2+X3=(4g/9)(5-2g), gives R_C5=(7-2sqrt(5))/(25-2sqrt(5))>1/10; the last inequality is equivalent to sqrt(5)<5/2. exact_audit.py verifies the rational witness directly from its matrices.

NUMERICAL: At the root, an 80-digit calculation gives

    l = 6.39420521365477735675378586490147705762343725708025...
    lambda = 0.892218900441913962345893312208755438868709755434...
    g1 = lambda,
    g2 = 0.676656701325741887037679936626266316606129266302...
    mu = 0.215562199116172075308213375582489122262580489132...
    T = 0.009450252588299694721686384259778457894327897942...
    X1+X2+X3 = 0.466072635596818186714472197496955132367897465780...
    R = 0.02027635150945603013278731777287297441336755083825...

NUMERICAL: The worst point's weights, rounded to fifteen places after the decimal, are

    edge    weight
    01      0.139535543610109
    02      0.344587234363879
    03      0.139535543610109
    04      0.000000000000000
    12      0.000000000000000
    13      0.376341678415902
    14      0.000000000000000
    23      0.000000000000000
    24      0.000000000000000
    34      0.000000000000000

PROVED: Formula (15), with l=3+t*, specifies the point exactly and makes the sum of weights exactly one. The displayed decimals are rounded; independently rounding weights need not preserve an exact repeated eigenvalue. The algebraic construction is the polish onto the stratum.

NUMERICAL: Checks and global search

NUMERICAL: check_formula.py builds 5,000 feasible graphs from random frames and gaps. It checks weight nonnegativity, sum of weights, the full Laplacian spectrum, and exact-two multiplicity to floating-point precision. It evaluates (1), the original S1,...,S5 definitions, and the independent sum over an orthonormal top basis and the two low eigenvectors. Maximum absolute discrepancies were 1.6653345369377348e-15 (closed versus trace) and 8.881784197001252e-16 (closed versus pair sum). The largest top split was 8.881784197001252e-16; the smallest sampled weight was 0.000026467863378398793.

NUMERICAL: The full optimization uses G=a uu^T+ar ww^T, lambda=(2+a+ar)/4. Thus the double eigenvalue is built into every evaluation. Ten edge nonnegativity constraints and lambda-a>=0 are imposed explicitly. SLSQP uses ftol=3e-13, at most 500 iterations per start, a>=1e-7, r>=1e-7, and X1+X2+X3>=1e-9. Candidates are retained only with constraint residual >=-2e-10 and denominator >1e-8. These cutoffs, finite start counts, and local optimization are limitations of the global numerical claim.

NUMERICAL: There were 400 starts at seed 41713 and 4,000 at seed 89117 using five Givens angles, plus 10,000 starts at seed 110713 using six Cayley coordinates. The Cayley parametrization uses a skew matrix Z and U=B(I-Z)^(-1)(I+Z)[:,0:2], where B is a fixed orthonormal basis of 1-perp. Givens runs start from uniform angles; Cayley runs start from Gaussian coordinates. One third of starts emphasize small gap ratios, and one eighth are perturbations of the current best point. The two parametrizations give independent coordinate charts for the search. All three runs returned the same sparse family, up to permutations and numerical tolerance. Raw minima were lower than the polished value by about 5e-13 because of tiny negative edge residuals; they are not reported as feasible exact minima. Individual records and complete progress outputs are retained here.

NUMERICAL: A separate 2,400-start scan used 300 starts at each fixed ratio r=0,0.001,0.01,0.1,0.25,0.5,0.75,1. The r=0 run is explicitly a boundary experiment, not a member of the exact-D=2 stratum. At r=1 the minimum found was 0.123143062495506, the C5 value to search precision. These scans do not prove the remaining equal-gap case.

NUMERICAL: boundary_checks.py additionally tested 23,000 frames: 8,000 near each equality graph at perturbation scales 0.1 down to 1e-6, and 7,000 at gap ratios 1e-2 down to 1e-10. No smaller quotient appeared. near_rank_one_checks.py tested the proved near-D3 inequalities on 20,000 feasible random frames with b/a<=1/3000. These samples corroborate the proofs and do not enlarge the proved regions.

PROVED: The quotient is undefined at the two equality graphs. This causes no ambiguity in T>=0. Indeed, X1,X2,X3>=0; their sum can vanish only if X1=0, hence a=b=lambda=1. The rank-two component argument above then gives precisely the balanced triangle and the two equal disjoint edges, and direct substitution gives all three X terms and T equal to zero. Numerical minimization of the quotient is understood on its positive-denominator domain.

PROVED: Reproduction and remaining question

PROVED: The exact identities and certificate can be rerun with Python 3, SymPy, NumPy, SciPy, and mpmath:

    python3 exact_audit.py
    python3 isolated_certificate.py
    python3 rank_one_certificate.py
    python3 recheck_matrices.py
    python3 sparse_family.py

NUMERICAL: The numerical checks and searches can be rerun with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_formula.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 minimise.py 41713 400
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 minimise.py 89117 4000
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 minimise_cayley.py 110713 10000
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 regions_scan.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 boundary_checks.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 near_rank_one_checks.py

PROVED: These proofs settle every disconnected graph and the stated regions for arbitrary connected graphs. They do not establish T>=0 for connected frames that fail (5), lie above a=A0(b/a), and have b/a>1/3000. In particular, the full equal-gap region beyond g=7/16 is not settled unless its moments satisfy (8) or another proved sufficient condition. Global optimality of the numerical quotient value is also unproved.

PROVED: Task: “n = 5, D = 2” — received 2026-11-13 at approximately 01:31 +04 (the launch time recorded in this folder).
