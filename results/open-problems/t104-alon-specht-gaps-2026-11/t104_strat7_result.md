PROVED: Partial resolution of disconnected N = 6, D = 2

PROVED: The full requested theorem has not been established. Every disconnected
six-vertex graph with D = 2 is covered below except a connected five-vertex
component carrying both top eigenvalues, together with one isolated vertex.
There is also a proved region in that remaining case. No counterexample was
found. The numerical searches do not resolve the remaining region.

PROVED: The following classes satisfy T >= 0, including all their boundary
graphs with actual top multiplicity exactly two:

    4+2, whether the four-vertex component contributes one or two top eigenvalues;
    4+1+1;
    3+3;
    3+2+1;
    3+1+1+1;
    2+2+2;
    2+2+1+1.

PROVED: In all these proved classes, equality occurs precisely at the balanced
triangle of edge weight 1/3 with three isolated vertices, and at two edges of
weight 1/2 with two isolated vertices. These are also equality examples for the
full problem. Exclusion of further equality examples in the unresolved 5+1
region has not been proved.

PROVED: Every theorem for a fixed graph above remains true after adding any
number of isolated vertices, so it holds for the indicated classes on every
N >= 6. This is not a proof for every disconnected graph on arbitrary N:
larger active components and additional inactive components are not covered.
There is one general additional class: S5 = 0 implies T >= 0 for every N
on the D = 2 stratum, regardless of component sizes.

NUMERICAL: Discovery runs

NUMERICAL: explore.py uses seed 131107 and 3,000 attempted samples for each
spectral mode. For a double carrier of size m it constructs

    L_m = I_m - J_m/m - U diag(g) U^T,

where U has m-3 orthonormal zero-sum columns, 0 < g_i < 1, and rejects negative
edge weights. The two top eigenvalues are one before normalization. For split
carriers, independently generated connected components are divided by their
individual top eigenvalues, then assembled and normalized. Inactive components
have their top eigenvalues strictly below one. These constructions cover both
ways to obtain D = 2; sampling is not exhaustive.

NUMERICAL: optimize.py adds 80 SLSQP starts per nontrivial mode, with all solver
and BLAS thread counts set to one. Cayley coordinates preserve the double
carrier's eigenspace constraints. Split carriers are rescaled separately.
polish_numerical.py repairs the small negative weight residuals of raw double
carrier iterates by adding a uniform complete graph inside the carrier, which
preserves its repeated top eigenvalue. The following are retained feasible
numerical quotients, not certified minima or lower bounds:

    structure / origin                sampler minimum     polished local-search value
    5+1, both in 5                    0.26837746          0.120223283793
    4+2, both in 4                    0.25182646          0.057198555815
    4+2, split                        0.21045808          0.179487549770
    4+1+1, both in 4                  0.09853999          0.057198192550
    3+3, both in one triangle         approximately 1     S5 = 0
    3+3, split                        0.15804468          0.157894839543
    3+2+1, both in triangle            approximately 1     S5 = 0
    3+2+1, split                      0.17948724          0.179487286785
    3+1+1+1                           undefined            X1+X2+X3 = T = 0
    2+2+2                             approximately 1     S5 = 0
    2+2+1+1                           undefined            X1+X2+X3 = T = 0

NUMERICAL: The 5+1 local-search candidate is approximately a triangle with two
leaves attached at one triangle vertex, with the sixth vertex isolated:

    w01 = w02 = 0.10337423, w12 = 0.36022389,
    w03 = 0.21651290, w04 = 0.21651474.

NUMERICAL: The smallest retained quotient is approached by a triangle with a
pendant vertex and two isolates. Up to relabeling, its edges are approximately

    w02 = w23 = 0.14914829, w12 = 0.33200761, w03 = 0.36969581.

NUMERICAL: In 4+2 with a double carrier the inactive edge tends to zero. In the
4+2 split search the four-vertex carrier tends to a three-vertex path plus an
isolate, with path edges 2/7 each and the other top edge 3/7. The 3+2+1 split
search approaches the same limit. In 3+3 split, both components tend to paths
with their four edges all 1/4. Full matrices, terms, spectra, and parameters are
in numerical.json, optimized.json and polished.json. Raw optimized.json is
retained for transparency; use polished.json for the repaired candidates.

PROVED: A component formula valid for every padding size

PROVED: It is convenient to give the graph top eigenvalue one before imposing
edge sum one. Write L0 for this unnormalized Laplacian, M = tr(L0)/2 for its
edge mass, P for its rank-two top projector, and A = I-L0 on the nonisolated
vertices. Use A = I on any isolated positions when needed. Put

    B = sum_ij P_ij A_ij^2,
    h = sum_i P_ii (L0)_ii,
    Y = 2 sum_(i<j) w_ij (P_ii+P_jj-2P_ij)
                          (2-(L0)_ii-(L0)_jj+2(L0)_ij),
    k = N-2.

PROVED: The following are the original quantities multiplied by M^2:

    X1* = 2[tr L0 - tr L0^2],
    X2* = 2(k+2) B/k,
    X3* = (M-1)/k^2 [2(k+1)(k-2) - 4kM + 2(k+2)h],
    2S5* = Y.                                                   (1)

PROVED: To derive (1), first use the normalized graph and write
A_lambda = lambda I-L. Since P1=0 and P A_lambda=0,

    tr(G(P o G)) = sum_ij P_ij (A_lambda)_ij^2.

PROVED: The two terms from subtracting lambda J/N vanish, by P A_lambda=0
and P1=0. Furthermore

    X1 = 2[2lambda-tr L^2],
    sum_i P_ii G_ii = 2(N-1)lambda/N - sum_i P_ii L_ii,
    X3 = (1-lambda)/(N-2)^2
           [2(N-1)(N-4)lambda - 4(N-2) + 2N sum_i P_ii L_ii].

PROVED: Edge differences annihilate J, giving the displayed Y. Substitute
lambda = 1/M and L = L0/M to obtain (1). Thus T and T* have the same sign.

PROVED: Positivity when S5 vanishes

PROVED: X1 >= 0 because every Laplacian eigenvalue lies in [0,lambda]. X2 >= 0
by the Schur product theorem. Also X3 >= 0 on every D = 2 stratum. Here is a
proof of this last assertion that does not assume a component classification.
For orthogonal zero-sum unit vectors u,v,

    sum_i u_i^2 v_i^2 <= (N-2)/(2N).                         (2)

PROVED: If Z is symmetric with Z1=0 and tr Z=0, put y=diag Z and H=I-J/N.
Then <Z,H diag(y) H>=||y||^2 and
||H diag(y) H||_F^2=(N-2)||y||^2/N. Cauchy-Schwarz proves
||diag Z||^2 <= (N-2)||Z||_F^2/N. Take
Z=(uv^T+vu^T)/sqrt(2) to obtain (2). Apply (2) to each top basis vector and
each eigenvector of G to get

    sum_i P_ii G_ii <= (N-2) tr G/N.

PROVED: Since D=2 implies 2lambda <= tr L = 2, beta >= 0, and X3 >= 0 follows.
Consequently S5=0 proves T>=0. This covers a balanced triangle carrying both
top eigenvalues, with arbitrary lower components, and two edge carriers with
arbitrary lower components: on top carrier edges the G difference is zero;
on all other edges the P difference is zero.

PROVED: In this class T=0 forces every nonzero Laplacian eigenvalue to equal
lambda, by X1=0. Actual D=2 then implies rank L=2 and lambda=1. A nonnegative
graph of rank two is either a three-vertex component or two edge components.
The former must have L=I_3-J_3/3; the latter must have both edges 1/2. This
also proves the stated equality descriptions whenever the remaining proofs
reduce to this class.

PROVED: One four-vertex component carrying both top eigenvalues

PROVED: Before normalization its Laplacian and projector are

    L4 = I4-J4/4-g vv^T,   P4 = I4-J4/4-vv^T,
    sum v_i=0, ||v||=1, 0<g<=1,
    w_ij = 1/4+g v_i v_j.

PROVED: Allow an additional inactive edge of Laplacian eigenvalue t in [0,1].
The actual case has t<1; t=1 is used only as an endpoint of an auxiliary
polynomial with the selected rank-two projector kept fixed. For no edge take
t=0. Put q=sum v_i^4, m=(sum v_i^3)^2, p=max(-v_i v_j). Then

    q>=1/4, m<=q-1/4, p>=1/4, 0<=g<=1/(4p),
    M=(3-g+t)/2,
    h=3/2-3g/4+gq,
    X1*=2[g(1-g)+t(1-t)],
    B=g^2(q-1/4-m),
    Y=2g[(5-4q)/4+g(-2+4q-3m)].                         (3)

PROVED: The bounds on q,m are Cauchy-Schwarz. If alpha=max v and
eta=-min v, then p=alpha eta and
sum_i(alpha-v_i)(eta+v_i)=4p-1>=0. The most negative pair product gives
g<=1/(4p). The formulas in (3) follow by expanding pairs, using sum v=0 and
sum v^2=1; exact_audit.py independently checks them against the original
matrix definitions at rational fixtures.

PROVED: Substitute (3) into (1). The coefficient of t^2 is -(2k+1)/k<0.
The coefficient of g^2 increases with m, so using m<=q-1/4 bounds it above by

    -[8k^2 q-2k^2+4kq+k+8q-6]/(4k^2)<0,   k>=4.

PROVED: To see the strict sign, put q=1/4+v with v>=0; the numerator becomes
8k^2 v+4kv+2k+8v-4>0. Therefore T* is separately strictly concave in g,t.
Its minimum on [0,1/(4p)] x [0,1] is at one of the four corners.

PROVED: four_vertex_certificate.py checks these corners exactly as follows.
Permute a nonzero zero-sum V decreasingly and write

    V=(3x+2y+z,-x+2y+z,-x-2y+z,-x-2y-3z), x,y,z>=0.
    R=sum V_i^2, ph=-V1 V4,
    q=sum V_i^4/R^2, m=(sum V_i^3)^2/R^3,
    gmax=R/(4ph), k=4+u, u>=0.

PROVED: After clearing positive denominators, the four corner polynomials
have respectively 3,3,75,84 nonzero coefficients. The first, second and
fourth have no negative coefficient. The third has five negative coefficients
before refinement. On each of the six orderings of x,y,z substitute the
largest=A+B+C, middle=B+C, smallest=C. Every resulting coefficient is
nonnegative. The script reconstructs all coefficients with rational SymPy
arithmetic and asserts these signs; it does not use floating eigenvalues.
This proves (3) gives T>=0 for all N>=6.

PROVED: The t=1 corner is strictly positive. At the only possibly vanishing
corner, t=0,g=gmax, the refined numerator has strictly positive pure B^6
and C^6 coefficients at u=0. Thus it vanishes only when just one of x,y,z
is nonzero. The corresponding v has p=1/4 and gmax=1. Strict concavity then
forces t=0,g=1, giving exactly rank-two Laplacians and the two equality
graphs described above. In particular a genuinely connected four-vertex
carrier gives T>0.

PROVED: Two triangle carriers, including triangle + edge + isolate

PROVED: On each triangle contributing one top eigenvalue, write

    L3=I3-J3/3-g vv^T,  P3=I3-J3/3-vv^T,
    w_ij=1/3+g v_i v_j,
    p=max(-v_i v_j), m=(sum v_i^3)^2.

PROVED: Zero sum and unit norm in three coordinates give

    sum v_i^4=1/2,
    1/3<=p<=1/2,
    m=9p^2(1/2-p), 0<=g<=1/(3p).

PROVED: For the second triangle use gap h and parameters p2,m2; call the
first p1,m1. Then (1) becomes

    M=(4-g-h)/2,
    h_diagonal=4/3-(g+h)/6,
    X1*=2[g(1-g)+h(1-h)],
    B=g^2(1/6-m1)+h^2(1/6-m2),
    Y=g+h-6g^2 m1-6h^2 m2.                                 (4)

PROVED: triangle_certificate.py proves strict separate concavity in g,h by
checking the exact coefficients. Thus it suffices to check the four corners
g in {0,1/(3p1)}, h in {0,1/(3p2)}. Put

    p1=(2+3x)/(6(1+x)), p2=(2+3y)/(6(1+y)), k=4+u,
    x,y,u>=0.

PROVED: After clearing positive denominators the corner polynomials have
3,12,12,45 terms, all with nonnegative rational coefficients. The endpoint
p_i=1/2 follows by continuity, or by the leading coefficients in x,y.
This proves the result. The only zero corner is p1=p2=1/3,g=h=1, which is
two top edges plus isolated vertices. All other actual triangle carriers
give strict positivity. Taking the second triangle at this edge boundary
proves the 3+2+1 split case as well, with arbitrary further isolates.

PROVED: The 4+2 split case

PROVED: Give the edge eigenvalue one before normalization and let u be the
unit zero-sum top eigenvector of L4. Keep P4=uu^T and the edge's rank-one
projector fixed throughout the following convex reduction. Define

    K_u={A4: A4 is symmetric positive semidefinite,
               A4 is entrywise nonnegative, A4 1=1, A4 u=0}.

PROVED: Every relevant graph gives A4=I4-L4 in K_u. Conversely, an element
of K_u is stochastic and positive semidefinite, so its spectrum lies in
[0,1], and I4-A4 is a nonnegative graph Laplacian with selected top u.
The auxiliary functional always uses the selected rank-two projector, even
where the actual top multiplicity increases on the boundary.

PROVED: The functional T* in (1) is concave on K_u for N>=6. Here is the
certificate and its construction. For a symmetric variation E of L4 with
E1=Eu=0, put p_i=u_i^2, d=diag E, mE=tr E/2 and
B_E=sum_ij u_i u_j E_ij^2. The quadratic part of T* in this direction is

    Q(E)=-2 tr E^2 + [2(k+2)/k-4] B_E
          +4 sum_i p_i(E^2)_ii -2 p^T E d
          +mE/k^2[-4k mE+2(k+2)p^T d].                    (5)

PROVED: One way to derive (5) is the identity, valid for L P=P and P1=0,

    S5*=2B+sum_i P_ii[2d_i-d_i^2-(Wd)_i-2 sum_j w_ij^2].

PROVED: Expand it to second order, using delta W_ij=-E_ij off the diagonal.
The quadratic bracket simplifies to 2(E^2)_ii-(E diag E)_i. The X1, X2 and
X3 quadratic contributions in (1) give the remaining terms in (5).

PROVED: To verify Q<=0, order the unnormalized U as in the four-vector cone
above, put R=||U||^2, Delta=U1-U4, and define a 4-by-2 matrix K, with columns
j=2,3, by

    K_1j=U4-Uj, K_jj=Delta, K_4j=Uj-U1,

PROVED: with other entries zero. The columns span {1,U} perpendicular, so
every variation has E=K V K^T for a symmetric 2-by-2 matrix V. Substitute
u=U/sqrt(R), k=4+z into -R k^2 Q. It is a quadratic form in
(V11,V12,V22) whose matrix coefficients are rational polynomials in the
three cone coordinates and z. concavity_certificate.py refines into the
same six ordered subcones and checks all 84 coefficient matrices per
subcone. Each matrix is positive semidefinite, checked by every principal
minor. Thus -Q>=0, proving concavity.

PROVED: The extreme points of K_u suffice. If rank A4<=2, write
A4=J4/4+g vv^T, with 0<=g<=1/(4p). If rank A4=3, its positive-definite
face subject to the row-sum constraint has dimension three: its range is
the three-dimensional space u perpendicular, and imposing A4 1=1 leaves
a free symmetric operator on the other two dimensions. Unless at least
three off-diagonal entries vanish, a nonzero two-sided perturbation within
that face preserves all the constraints, contradicting extremality.
Diagonals cannot vanish in K_u because a zero diagonal of a PSD matrix
forces its whole row to vanish, contradicting its row sum. Thus a connected
rank-three extreme point has at most three edges, hence is a tree.
Disconnected extreme points reduce to (4) or to S5=0.

PROVED: There are two tree types. Their positive parameters and top vectors,
before normalization, can be chosen as follows:

    star: u proportional to (-x-y-z,x,y,z), x,y,z>0,
          w01=x/(2x+y+z), w02=y/(x+2y+z), w03=z/(x+y+2z);

    path: u proportional to (x,-x-y,y+z,-z), x,y,z>0,
          w01=x/(2x+y), w12=y/(x+2y+z), w23=z/(y+2z).

PROVED: These follow directly from L4 u=u. For the path, the middle-edge
cut gives x+y>x and y+z>z. Conversely the displayed alternating-sign
eigenvectors are the top eigenvectors by Perron-Frobenius applied to the
signless Laplacian of the connected bipartite tree. Add the edge of weight
1/2. tree_certificate.py substitutes these rational matrices into (1), sets
k=4+z0 and clears positive denominators. The two numerators have 126 and
108 nonnegative coefficients, respectively, and are strictly positive for
positive tree parameters.

PROVED: For the rank-at-most-two boundary, let U be the unnormalized gap
vector, R=U^T U, v=U/sqrt(R), and K the above 4-by-2 spanning matrix.
For any unit selected a perpendicular to 1,v, the functional is a^T F a,
where, with M=(4-g)/2,

    F=[2g(1-g)+(M-1)/k^2{2(k+1)(k-2)-4kM+5(k+2)/2}] I4
       +2(k+2)g^2/k (v o v)(v o v)^T
       -2(k+2)g(M-1)/k^2 diag(v_i^2)
       -2g Lap[(1/4+g v_i v_j)(v_i-v_j)^2].             (6)

PROVED: Here Lap denotes the weighted Laplacian with the indicated edge
weights. split_boundary_certificate.py forms k^2 R^2 K^T F K, clears all
known denominators before expansion, and checks its concavity in g and
its endpoints g=0, R/(4ph). The three checks have 84,84,198 coefficient
matrices, all 2-by-2 and PSD by rational principal minors. Pure-axis
coefficient matrices at k=4 are positive definite, proving both endpoints
strictly positive at every nonzero cone point. Concavity gives T*>0 on
this boundary.

PROVED: A compact finite-dimensional convex set is the convex hull of its
extreme points. Concavity, the tree certificates, (6), the disconnected
reductions, and (4) therefore prove T>=0 throughout K_u, hence in 4+2 split.
For equality, only disconnected rank-two-Laplacian extreme points can
contribute. Their selected u is an edge contrast; with this u fixed there
is just one such zero extreme point. Thus a zero convex combination is
that same graph, giving two equal edges and isolates. This completes every
component structure in the initial list.

PROVED: A formula and a certified region for the remaining 5+1 case

PROVED: On the five-vertex carrier use the notation of the supplied previous
results: orthonormal zero-sum u,v, internal gaps a>=b>0, s=a+b,
lambda=(2+s)/4, Pi=I5-J5/5-uu^T-vv^T. Thus

    w_ij=lambda/5+a u_i u_j+b v_i v_j,
    a<lambda for a connected carrier,
    0<a<2/(3-r), r=b/a in (0,1].

PROVED: Write

    A=sum u_i^4, B=sum v_i^4, C=sum u_i^2 v_i^2,
    d=sum u_i^3, e=sum u_i^2 v_i, f=sum u_i v_i^2, h=sum v_i^3,
    F=a(A+C)+b(B+C), k2=a^2+b^2,
    K=a^2 A+b^2 B+2ab C-k2/5
          -a^2(d^2+e^2)-2ab(e^2+f^2)-b^2(f^2+h^2).

PROVED: The five-vertex expression supplied in PREVIOUS_RESULT_STRAT4.md is

    T5=(14+2s)(F-s/5)/9+4k2/3
         -14(a^2 A+b^2 B)/3-4(k2+ab/3)C+R5,
    R5=8a^2 d^2/3+8b^2 h^2/3
         +2a(a+5b)e^2/3+2b(b+5a)f^2/3+2s(adf+bhe).

PROVED: Appending one isolated vertex changes this to the exact identity

    T6=T5-K/3+(1-lambda)(162+169s-260F)/720.             (7)

PROVED: This follows from (1), since X1 and S5 stay fixed, X2 changes by
-K/3, and the five-vertex diagonal moment is
sum_i Pi_ii L_ii=4/5-2s/5+F. Equation (7) supplies a convenient reduced
formula but does not itself prove the sign: the -K/3 term is nonpositive.

PROVED: The total cubic contribution in (7) is

    R6=3a^2 d^2+3b^2 h^2+(a^2+4ab)e^2+(b^2+4ab)f^2
          +2s(adf+bhe)
       =3a^2[d+s f/(3a)]^2+3b^2[h+s e/(3b)]^2
          +(2a^2+10ab-b^2)e^2/3
          +(-a^2+10ab+2b^2)f^2/3.

PROVED: Since f^2<=C, this is at least -a^2 c_r C, where it suffices to use

    c_r=(1-10r)/3 for 0<=r<=1/10, and c_r=0 for 1/10<=r<=1.

PROVED: The following elementary moment polytope contains all such frames:

    1/5<=A,B<=13/20, 0<=C<=3/10,
    A+C,B+C<=4/5, A+B+2C<=7/5, 2C<=A+B.

PROVED: The lower bounds are Cauchy-Schwarz. The diagonal contraction
argument used in (2), now with N=5, applied to uu^T-H/4,
(uv^T+vu^T)/sqrt(2), and uu^T+vv^T-H/2 gives the three sharper upper
bounds 13/20,3/10,7/5. The other bounds follow from uu^T+vv^T<=H or from
sum(u_i^2-v_i^2)^2>=0.

PROVED: scale_certificate.py enumerates this polytope's 16 vertices exactly.
It substitutes each vertex into the noncubic part of (7), adds the above
lower bound for R6, and writes the polynomial in the degree-two Bernstein
basis for a/(11/25). It checks each coefficient's quadratic minimum in r
on [0,1/10] and [1/10,1], by rational endpoints and the interior critical
point when applicable. All minima are strictly positive.

PROVED: The same certificate covers N>=6 after adding further isolates.
Set k=N-2=4+z. Replace -K/3 in (7) by [2(k+2)/k-10/3]K and use (1) for
X3. The cubic contribution increases from R6 by

    (1-4/k)[a^2(d^2+e^2)+2ab(e^2+f^2)+b^2(f^2+h^2)]>=0.

PROVED: After multiplying the lower bound by k^2, every coefficient in z
passes the same Bernstein/quadratic checks. Consequently a five-vertex
double carrier with a<=11/25 has T>0 after padding to every N>=6.

NUMERICAL: A stronger moment LP using cubic Gram bounds and nonnegative
weighted-square identities was attempted in moment_lp.py. It still gives
negative lower bounds at many larger-gap points. Those LP optima are not
graphs and are not counterexamples. No sign conclusion follows there.

PROVED: Certificate replay and limits

PROVED: Every certificate above is constructed from the displayed formulas.
The scalar certificates expand rational polynomials and check coefficient
signs; the matrix certificates additionally check every principal minor of
each rational coefficient matrix. All principal minors nonnegative is the
exact PSD criterion for a real symmetric matrix. No SDP, floating solver,
or numerical eigenvalue sign test enters these proofs.

PROVED: Run all certificates, sequentially, with

    PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 python3 replay.py

PROVED: This runs four_vertex_certificate.py, triangle_certificate.py,
concavity_certificate.py, split_boundary_certificate.py, tree_certificate.py,
scale_certificate.py, and exact_audit.py. Their .out files retain the exact
checks. replay.py reports elapsed time and peak resident memory and asserts
a 900 MiB guard. SymPy and Python's standard library suffice for the exact
proof replay. exact_audit.py independently evaluates the original matrices
at rational fixtures and several padding sizes; those finite fixtures audit
the formulas, while the universal certificates and derivations prove them.

NUMERICAL: To replay discovery and the reference checks:

    PYTHONDONTWRITEBYTECODE=1 python3 explore.py
    PYTHONDONTWRITEBYTECODE=1 python3 optimize.py
    PYTHONDONTWRITEBYTECODE=1 python3 polish_numerical.py
    PYTHONDONTWRITEBYTECODE=1 python3 moment_lp.py

NUMERICAL: These scripts require NumPy and SciPy, set solver/BLAS thread
counts to one, and use terms.py as a numerical reference only.

PROVED: What remains for the original six-vertex request is precisely this
unresolved part of 5+1:

    a connected five-vertex carrier with top multiplicity two;
    0<r=b/a<=1;
    11/25<a<2/(3-r);
    all ten weights lambda/5+a u_i u_j+b v_i v_j nonnegative.

PROVED: The existing moment formulas and sufficient bounds may certify
individual points in that region, but no proof covering the whole region
is supplied here. The full N=6 theorem, its full equality classification,
and the extension to every disconnected graph for every N>=6 remain open
in this work. The results above do not assert otherwise.

PROVED: Task: “Prove T >= 0 for every DISCONNECTED weighted graph on N = 6
vertices with D = 2. Then, if the method allows, extend it to every N >= 6.”
Received 2026-11-13 at approximately 03:26 +04.
