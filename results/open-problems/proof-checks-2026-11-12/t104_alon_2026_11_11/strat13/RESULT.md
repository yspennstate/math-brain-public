PROVED (replay_all.py): all nine retained STRAT12 boxes are closed, and T6>0 throughout STRAT9 region (11) at N=6, under every hypothesis stated below. Zero OPEN leaves remain. No counterexample exists in this region. All 18 replay stages passed, including the complete STRAT12 replay and every original-cover leaf. All 522 supplied inherited files are unchanged.

PROVED (verify_collars.py): both physical equality types satisfy

    T6(S) >= ||S-S_P||_max / 24 > 0

on the feasible punctured closed matrix ball, with the following rational radii. At its center T6=0 and the carrier is disconnected.

| Equality type | Radius | Local chart radius ||h||_1 | Remainder constant |
|---|---:|---:|---:|
| Two disjoint edges of weight 1/2, one isolate | 1/15360 | 1/384 | 32 |
| Triangle with weights 1/3, two isolates | 1/27864 | 1/648 | 54 |

PROVED (verify_collars.py): the nine exact centers, in coordinate order (t,v1,z1,v2,z2,z), are as follows. Write s=sqrt(5) and q=sqrt(15), with positive square roots. All coefficients, expansions, and interval comparisons are exact. The complete degree-two expansions of T6, the polynomial target, and every active inherited constraint at every center are in local_certificates.json, under algebraic_chart_expansions. An entry [alpha,[A,B]] denotes the coefficient A+B*sqrt(d) of the displacement monomial of multi-index alpha; omitted coefficients vanish.

| Original node | Exact center | Type |
|---|---|---|
| 12091 | (3/2,-1,s/2,-1,-s,s/2) | Two edges |
| 12407 | (4,-1,q/3,-1,-q,q/3) | Triangle |
| 14175 | (4,-1,s,-1,-s,s) | Two edges |
| 15603 | (4,-1,q/3,-1,q/3,q/3) | Triangle |
| 15773 | (4,-1,-s,-1,-s,s) | Two edges |
| 19750 | (4,-1,-q/3,-1,-q/3,q) | Triangle |
| 20736 | (3/2,-1,-s,-1,s/2,s/2) | Two edges |
| 21058 | (4,-1,-q,-1,q/3,q/3) | Triangle |
| 21550 | (4,-1,-s,-1,s,s) | Two edges |

PROVED (verify_collars.py): writing delta for displacement from the center, the original-chart linear terms of T6 are the following. Each full expansion is this term plus the exact quadratic form in local_certificates.json and O(||delta||^3).

| Node | Linear term of T6 |
|---|---|
| 12091 | (22 delta_t+5 delta_v1-s delta_z1+11 delta_v2+8s delta_z2-s delta_z)/15 |
| 12407 | (96 delta_v2+31q delta_z2)/180 |
| 14175 | -(3 delta_t+s delta_z1+s delta_z)/10 |
| 15603 | -8(delta_t+delta_v1+delta_v2)/15-31q(delta_z1+delta_z2+delta_z)/180 |
| 15773 | (-3 delta_t+s delta_z1+s delta_z2)/10 |
| 19750 | -31q delta_z/180 |
| 20736 | (22 delta_t+11 delta_v1+8s delta_z1+5 delta_v2-s delta_z2-s delta_z)/15 |
| 21058 | (96 delta_v1+31q delta_z1)/180 |
| 21550 | -(3 delta_t+s delta_z2+s delta_z)/10 |

PROVED (verify_collars.py): the physical charts remove the eigenframe rotation redundancy at the repeated eigenvalue. In the vertex orders saved by point_bank() in collar_boxes.py, take the orthogonal zero-sum bases

    edges:    U=(-4,1,1,1,1), W=(0,1,-1,-1,1),
              X=(0,1,1,-1,-1), Y=(0,1,-1,1,-1);
    triangle: U=(3,3,-2,-2,-2), W=(1,-1,0,0,0),
              X=(0,0,1,-1,0), Y=(0,0,1,1,-2).

Put nu=U.U, nw=W.W, h=(x,y,k,p,q,v,z), and

    B=(U+pX+qY, W+vX+zY),
    K=[(1+x)/nu  k/nu; k/nu  (1+y)/nw],
    S=B K B^T, Q_S=B(B^T B)^(-1)B^T,
    lambda=(2+tr(S))/4, omega_ij=lambda/5+S_ij.

PROVED (verify_collars.py): these are coordinates on the rank-two symmetric zero-sum matrix manifold near S_P. In basis (U,W,X,Y), extract the upper block K and the lower-left block A of the coefficient matrix of S. Then H=A K^(-1) recovers the four transverse coordinates. The rank-two Schur complement identity reconstructs S=BKB^T. Positive definiteness of K and positivity of det(B^T B) are checked throughout the derivative cube |h_i|<=1/100.

PROVED (verify_collars.py): in the two-edge chart, T6=L+Q2+O(||h||_1^3), where

    L=(-23x+y)/20,
    Q2=-283x^2/320-3xy/32-3y^2/320-2k^2/5
       -91(p^2+q^2)/100-7(pz+qv)/5-59(v^2+z^2)/20.

The active edge order is (01,02,03,04,12,13,24,34), using zero-based labels. Their linear terms are

    (-3x+y-4k-4p-4q)/20,
    (-3x+y+4k-4p+4q)/20,
    (-3x+y+4k+4p-4q)/20,
    (-3x+y-4k+4p+4q)/20,
    (x-2y+p-5z)/10, (x-2y+q-5v)/10,
    (x-2y-q+5v)/10, (x-2y-p+5z)/10.

PROVED (verify_collars.py): in the triangle chart,

    L=23x/80-443y/240,
    Q2=-193x^2/320+97xy/96-593y^2/320-4k^2/45
       -409p^2/1200-409q^2/400-281v^2/80-843z^2/80.

The seven active edges are (01,02,03,04,12,13,14). Their linear terms are

    (7x-9y)/20,
    -3x/20+y/20-k/15+p/10+q/10+v/2+z/2,
    -3x/20+y/20-k/15-p/10+q/10-v/2+z/2,
    -3x/20+y/20-k/15-q/5-z,
    -3x/20+y/20+k/15+p/10+q/10-v/2-z/2,
    -3x/20+y/20+k/15-p/10+q/10+v/2-z/2,
    -3x/20+y/20+k/15-q/5+z.

PROVED (verify_collars.py): for both charts the physical connectedness determinant is

    kappa=det(lambda I-S|range(S))
         =-3x^2/16+5xy/8-3y^2/16-(nw/nu)k^2+O(||h||_1^3),

where nw/nu=1/5 for two edges and 1/15 for a triangle. Its constant and linear terms vanish. In the zero-edge coordinates, kappa=4*connected/D^2. The rank and ratio inequalities are strictly positive at all nine centers; all other vanishing chart constraints have their exact linear and quadratic terms recorded in local_certificates.json. Thus the active edge curvature, rather than the connectedness determinant alone, controls the first-order sign of T6.

PROVED (verify_collars.py): let g be the active edge linearizations and A their Jacobian. In both charts A has rank seven. Rational left inverses J and nonnegative multipliers mu satisfy JA=I and mu A=DL, with

    edges:    mu=(9/4,9/4,9/4,9/4,1/2,1/2,1/2,1/2);
    triangle: mu=(21/4,31/18,31/18,31/18,31/18,31/18,31/18).

For every one of the 128 sign vectors sigma in each chart, mu_sigma=mu-sigma^T J/6 is nonnegative and mu_sigma A=DL-sigma^T/6. Consequently g>=0 implies L>=||h||_1/6. This is a statement in physical coordinates, with no free rotation direction.

PROVED (verify_collars.py): the nonlinear estimate uses actual nonnegative weights, not a linearized feasible cone. Write T6=P/d, d=det(B^T B). Orthogonality gives

    d=nu*nw+nw*nx*p^2+nw*ny*q^2+nu*nx*v^2+nu*ny*z^2
      +nx*ny*(pz-qv)^2 >= nu*nw,

where nx=X.X and ny=Y.Y. Exact coefficient envelopes bound all Hessian entries of T6 and the active weights on |h_i|<=1/100. If mu_i^max bounds the signed Farkas multipliers, the Taylor integral remainder obeys

    |R_T|+sum mu_i^max |R_omega_i| <= M ||h||_1^2,
    M=32 (edges), M=54 (triangle).

Substitution of the actual weights into the signed identities yields

    T6 >= ||h||_1/6-M||h||_1^2 >= ||h||_1/12

for ||h||_1<=1/(12M). The exact unrounded constants, derivative envelopes, Gram identities, and rational multiplier matrices are saved and recomputed. No optimization result or floating comparison is a premise.

PROVED (verify_collars.py): for epsilon=||S-S_P||_max<=1/1000, coefficient extraction bounds ||h||_1<=40 epsilon for edges and <=43 epsilon for triangles. The saved rational determinant bounds justify inversion of K. Taking epsilon<=1/15360 or <=1/27864, respectively, puts h inside its collar. Conversely the exact entry derivative bound gives epsilon<=2||h||_1 on the derivative cube. This proves T6>=epsilon/24 in each physical ball. Connectedness excludes h=0.

PROVED (verify_collars.py): the physical expression is checked two ways: against the inherited frame formula, and independently against the six-vertex matrix definitions used by zero_face.py. The zero-edge polynomial target certified by STRAT12 is 20 D^2 Delta T6; all three factors outside T6 are strictly positive on the feasible set. The local rational and algebraic expansions therefore concern the same target sign as the inherited Bernstein certificates.

PROVED (verify_collars.py): collar_cover.json is the final physical-ball partition. Every accepted local leaf lies wholly inside the stated max-entry ball about its own S_P. The nine boxes minus these balls are covered by strict STRAT12 Bernstein positivity or exclusion certificates. The partition contains 366 positivity leaves, 216 exclusions and 17 ball leaves, with 590 split nodes and maximum additional depth 72 from the nine supplied depth-16 leaves. There are zero OPEN leaves. The exact input chart volume 189/134217728 is preserved. collar_chart_cover.json preserves the earlier, less refined collar partition; the final proof uses collar_cover.json.

PROVED (verify_collars.py): the second remainder derivation cancels the linear term in the polynomial numerator, bounding (P-dL)/d and each omega_i-g_i directly by rational coefficient envelopes. It gives constants 1533221743435914585899/50000000000000000000<32 and 5891344851651791485819/112500000000000000000<54, independently auditing the quotient-Hessian argument. NUMERICAL: the first independent physical-ball replay took 17.793482 seconds; its final pass inside the full replay took 14.991479 seconds.

PROVED (replay_all.py): the full region (11) theorem is T6>0 under every hypothesis below. Normalize the total carrier edge weight to one. Let u,w in R^5 be orthonormal and zero-sum, a>=b=ar>0, lambda=(2+a(1+r))/4, and

    L5=lambda(I-J/5)-a uu^T-ar ww^T,
    omega_ij=lambda/5+a u_i u_j+ar w_i w_j,
    D_ij=-1-r-20(u_i u_j+r w_i w_j),
    E=2/max(3-r,max_(i<j) D_ij).

Pad the carrier by exactly one isolated vertex, so N=6. The remaining hypotheses of STRAT9 region (11) are:

1. 3/20<r<=1, every omega_ij>=0, and the five-vertex carrier is connected.
2. max(14/25,V6(r))<a<=E and a<2/(3-r).
3. P6^*(a,r,A,B,C)<0 and P6^*(E,r,A,B,C)<0.
4. The true endpoint at scale E is connected.
5. At that endpoint, for every zero edge, both edge orders as chart positions {4,5}, every permutation of the other three vertices, and either common sign of the second column, the chart lies outside every closed box in STRAT12/STRAT11/STRAT9/face_boxes.json.

PROVED (replay_all.py): here A=sum u_i^4, B=sum w_i^4, C=sum u_i^2 w_i^2. V6(r) is the maximum applicable scale ceiling in the inherited moment_cells.json. P6^* is the maximum applicable pointwise N=6 lower polynomial over records in moment_cells.json and allN_optimized_cells.json, evaluated by cells.lower_value and cells.vector_from_record in STRAT12/STRAT11/STRAT9. These are the original (11) definitions; the theorem does not silently replace them with the later residual (R10).

PROVED (replay_all.py): T6 is the inherited expression with c=3 and beta=(1-lambda)/4. Equivalently define d=sum u_i^3, e=sum u_i^2 w_i, f=sum u_i w_i^2, h=sum w_i^3, and m=A+rB+(1+r)C. Then

    T6=9/80+a*(11m-2(1+r))/8+a^2*(H+R),
    H=[100(1+r)m-1600(A+r^2 B)-1280(1+r^2)C-640rC
       +415(1+r^2)-66r]/320,
    R=3d^2+3r^2 h^2+(1+4r)e^2+(r^2+4r)f^2+2(1+r)(df+rhe).

PROVED (replay_all.py): at the true endpoint, connectedness supplies a zero-edge chart in the canonical root. Original-cover scale exclusions have their moment-cell premises replayed; direct positive leaves have strictly positive rational margins. STRAT11 overlays that cover, STRAT12 closes all but nine leaves, and the new ball partitions close those nine. For an inward scale t=a/E<1, the exact radial identity

    T6(a,ar)=(1-t^2)*9/80+a(1-t)*L6+t^2*T6(E,rE),
    L6=(11m-2(1+r))/8>=3(1+r)/32>0,

transfers strict positivity to the original graph. The endpoint itself is strictly positive by the finite cover. This conclusion is for N=6, five-vertex carriers with the stated gap representation and one isolate. OPEN: the corresponding N>=7 regions and larger carriers are not settled by this run.

PROVED (replay_all.py): the complete exact replay passed. Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py`. The driver runs the unmodified STRAT12 replay in a temporary byte-identical copy, then replays every original STRAT10 accepted cover leaf and its scale premises, and finally verify_collars.py. All supplied STRAT10, STRAT11 and STRAT12 files are fingerprinted before and after; output files are written outside the supplied trees.

PROVED (replay_all.py): the final combined canonical-root partition has 32,925 positive leaves, 20,277 exclusions and 17 physical-ball leaves, with 53,218 split nodes and zero OPEN leaves. The identity leaves=splits+1 gives 53,219 leaves. Its exact chart volume remains 1152. These are chart-coordinate counts and volumes, not counts or volumes of feasible graphs. remaining_open_boxes.json contains an empty list.

NUMERICAL: full inherited-plus-collars replay took 1093.231151 seconds (18 minutes 13.23 seconds). The STRAT12 stage took 290.432750 seconds; the additional original-cover leaf replay took 670.670126 seconds. replay_summary.json, strat12_replay_summary.json, original_cover_verification.json and collar_verification.json record the timings and exact ledgers. Largest recorded discovery-worker peak RSS was 224,952,320 bytes; the inherited Bernstein replay parent peak was 155,893,760 bytes, and the outer driver peak was 103,727,104 bytes. Discovery used two workers; the inherited exact stage used four. No subagents or language-model workers were started. The sandbox denied priority changes and aggregate process enumeration; per-process RSS readings and governor snapshots are operational measurements, not an exhaustive simultaneous memory trace.

PROVED (replay_all.py, verify_collars.py): all target sign decisions use Fraction/integer arithmetic or exact SymPy rationals in the physical charts and the quadratic fields Q(sqrt(5)), Q(sqrt(15)) in the original charts. Numerical LPs propose coefficients only; every accepted coefficient bank is checked again exactly. NumPy object arrays arrange exact integer Bernstein operations. Timing and RSS floats have no proof role.

Task: “close the last 9 OPEN leaves of T104 5+1 region (11), N=6, by local collar bounds at the disconnected equality limits” — received 2026-11-13 11:05 +04 (workspace launch).
