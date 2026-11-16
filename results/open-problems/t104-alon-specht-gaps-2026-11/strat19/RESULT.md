# STRAT19: split 3+5

PROVED (replay_all.py, requiring all 39 stages PASS): split 3+5 satisfies T>=0 for every integer N>=8, with isolates or arbitrary lower components, and for a fixed graph padded to N->infinity. Two connected simple top carriers give T>0. On the selected-projector closure the equality set is exactly two equal edges and isolates. Every positive lower trace is strict. Lower component sizes need not be bounded by five.

## Functional and inherited reductions

PROVED (inherited18/inherited17/lower_formula.py; audit35.py): normalize the common top eigenvalue to one. Let C=C3 direct-sum C5, P=uu^T direct-sum vv^T for selected unit top directions, k=N-2 and M0=tr C/2. Put

    h=sum_i P_ii C_ii,
    B=sum_ij P_ij (I-C)_ij^2,
    Y=-2 sum_(i<j) C_ij (P_ii+P_jj-2P_ij)
                         (2-C_ii-C_jj+2C_ij),
    X_k(m,h)=(m-1)/k^2 [2(k+1)(k-2)-4km+2(k+2)h].

PROVED (same scripts): for lower blocks D, s=tr D and M=M0+s/2,

    T*=2(tr C-tr C^2)+2(tr D-tr D^2)
       +2(k+2)B/k-Y+X_k(M,h),
    T=T*/M^2.

PROVED (inherited18/setup35.py; inherited18/inherited17/inherited16/concavity_certificate.py; inherited18/inherited17/inherited16/split34_reduction.py): for fixed selected top vectors the functional is separately concave on K_u x K_v, where K_u={A PSD, A entrywise nonnegative, A1=1, Au=0} and C=I-A. Fixed lower trace changes neither quadratic variation. The triangle reduces to its balanced corner C3=H3 or its zero-edge three-path corner. The five-part reduces to its extreme points. The 252-matrix five-part concavity certificate, including its 24 gap-order cones, is replayed exactly.

PROVED (inherited18/inherited17/inherited16/extreme_inventory.py; the face argument in the copied RESULT.md): the connected five-part extremes consist of the three trees, rank(A5)<=2, and rank(A5)=3 on twelve nonbipartite support candidates. All rank-three candidates are covered simultaneously below. Disconnected endpoints reduce to the inherited 2+5, 3+4 and smaller classes with arbitrary lowers. Cross-block selected-projector entries do not contribute; mixtures are handled by linearity.

## Moment bounds used in the comparisons

PROVED (inherited18/inherited17/lower_formula.py; transfer35.py; lower35.py; audit35.py): write S_i=H_i-C_i, with S_i PSD, S_i<=H_i, S_i1=S_i u_i=0. Let tau=sum tr S_i and d=sum_i P_ii(S3 direct-sum S5)_ii. Then

    M0=(6-tau)/2, 0<=tau<=4,
    h=22/15-d, 0<=B<=d<=7/15.

PROVED (same scripts and Schur product): for one selected unit top direction, its energy one is at most twice sum u_i^2 C_ii, so that diagonal moment is at least 1/2. Also B_i=u_i^T(S_i Hadamard-product S_i)u_i>=0 and

    (H_i-S_i) Hadamard-product S_i
       =diag(diag S_i)-S_i/i-S_i Hadamard-product S_i PSD.

PROVED (same scripts): evaluating the latter on u_i gives B_i<=d_i. For rank(A5)<=3, rank S5<=2, hence 0<=tau5<=2 and 0<=B5<=d5<=3/10. No numerical spectral bound is used.

## Rank-at-most-three five-parts: transfer of the existing SOS

PROVED (transfer35.py; symbolic35.py): for the three-path let l be its second eigenvalue. With positive fluxes a,b,

    D=(2a+b)(a+2b),  l=3ab/D,  0<l<=1/3,
    h3=1/2+l/6,
    B3=l^2(3-l)/(6(1-l)),
    2(tr C3-tr C3^2)-Y3=l(1-l)-6B3.

PROVED (symbolic35.py): these are polynomial identities after clearing positive denominators, including D-9ab=2(a-b)^2. The balanced triangle has trace two, h3=2/3 and B3=Y3=0, independently of its selected top direction.

PROVED (transfer35.py): compare the new k=6 functional with the inherited edge+five-part functional at k=5, leaving the five-part and its selected vector fixed. Their five-part trace-square and Y moments cancel. The B5 coefficient changes by -2/15, so B5<=d5 gives the following lower increments, where t=tau5 and d=d5:

    balanced:
      -2d/15+X_6((6-t)/2,22/15-d)
               -X_5((5-t)/2,13/10-d) >= 73/675;

    path:
      l(1-l)-(10/3)B3-2d/15
        +X_6((5+l-t)/2,13/10+l/6-d)
        -X_5((5-t)/2,13/10-d) >= 1/20.

PROVED (transfer35.py): the balanced difference is

    (-390dt-1230d+225t^2+317t+1099)/6750.

PROVED (same script): after subtracting 73/675 its two d-endpoints have nonnegative coefficients in t. For the path, multiply the difference minus 1/20 by 1-l>0, set l=u/3, t=2v and use the two d-endpoints 0,3/10. All 24 tensor Bernstein controls of degrees (3,2) on (u,v) in [0,1]^2 are strictly positive rationals. The smallest control is 1/100. transfer35_checks.json records every control and the exact reconstruction checks.

PROVED (inherited18/inherited17/inherited16/verify_sos.py; inherited18/inherited17/inherited16/verify_rank_three_algebra.py; inherited18/inherited17/inherited16/padding_monotonicity.py): the inherited 2+5 k=5 margin on rank(A5)<=3 is at least 1/400000. This uses the byte-identical rational_sos_2.json, exact coefficient reconstruction, 22 rational positive Gram witnesses, scale concavity and the inherited inverse-padding derivative bound. The S5=0 endpoint has margin 63/250. No new SOS solve is required.

PROVED (transfer35.py, together with that replay): the new path-corner margin is at least 20001/400000; the balanced-corner margin is at least 73/675+1/400000. These cover both rank-two scale endpoints, all intermediate scales, and every rank-three five-part, including all twelve support candidates.

## Three five-trees: six corner pairs

PROVED (algebra35.py; tree35.py; symbolic35.py): use the inherited positive-flux tree chart U_i=sign_i sum_(e incident i)x_e, w_ij=x_ij/(s_i+s_j). For each triangle corner and each five-tree, clearing the positive denominator R3 R5 D3^2 D5^2 k^2 yields only positive nonzero rational coefficients in the fluxes and z=k-6.

| Triangle | Five-tree | Isolate terms | Smallest coefficient | Max-lower terms |
|---|---|---:|---:|---:|
| PROVED (tree35.py): balanced | star | 858 | 144 | 858 |
| PROVED (tree35.py): balanced | path | 609 | 144 | 609 |
| PROVED (tree35.py): balanced | fork | 705 | 144 | 705 |
| PROVED (tree35.py): path | star | 5982 | 144 | 6006 |
| PROVED (tree35.py): path | path | 4239 | 144 | 4263 |
| PROVED (tree35.py): path | fork | 4911 | 144 | 4935 |

PROVED (tree35.py): every row has explicit positive witnesses at z^0 and z^2, recorded in tree35_checks.json. Hence every pair of positive-flux connected trees is strict, including infinity. The maximal-lower numerator uses k=8+z and likewise has only positive coefficients; its smallest nonzero coefficients are 600 for the balanced triangle and 320 for the three-path. These are cleared-polynomial coefficients, not uniform bounds on T*. Trees can approach the two-edge equality boundary.

PROVED (symbolic35.py): all twelve isolate/maximal-lower numerators agree identically with the direct eight-by-eight selected-projector construction as sparse rational polynomial identities. audit35.py independently checks the original centered matrix definition, padding and feasible lower edges at twelve rational fixtures.

## Padding and infinity

PROVED (tree35.py): if a tree-pair numerator at k=6+z is A0+A1 z+A2 z^2, its k-dependent quotient is, up to a positive constant denominator,

    A2+(A1-12A2)r+(A0-6A1+36A2)r^2,  r=1/k.

PROVED (same script): the negatives of its derivatives at r=0,1/6 are 12A2-A1 and A1-A0/3. Every coefficient is nonnegative in the fluxes. The derivative is affine in r, proving that k=6 is hardest and including k=infinity.

PROVED (transfer35.py): for rank(A5)<=3, every triangle in the full domain has M>=3/2, h=22/15-d>=1 and B<=d<=7/15. The inverse-padding derivative is

    4B+(M-1)(-2-4M+2h)+8r(M-1)(h-1).

PROVED (same script): on 0<=r<=1/6 it is at most

    4d+(M-1)(-10/3-4M+(10/3)h) <= -17/15.

PROVED (same script): putting M=3/2+a and h=22/15-d, the upper bound becomes

    -20/9+(7/3)d-4a^2-a(58/9+(10/3)d) <= -17/15.

PROVED (the preceding scripts and inherited concavity): every connected endpoint is hardest at k=6; therefore all isolate-only signs hold for every N>=8 and infinity. Separate concavity also gives the signs for all intervening triangle and five-part scales.

## Arbitrary lower components

PROVED (inherited18/inherited17/lower_formula.py; lower35.py): define

    F_k(s)=2(tr C-tr C^2)+2(k+2)B/k-Y+X_k(M0+s/2,h).

PROVED (same scripts): T*>=F_k(s), since the omitted term is 2 sum mu(1-mu)>=0. Nontrivial lower components require N>=10, k>=8, and 0<=s<=S=k-7. The exact interpolation identity is

    F_k(s)=(1-s/S)F_k(0)+(s/S)F_k(S)+s(S-s)/k.

PROVED (lower35.py): uniformly on the entire top domain,

    F_k(k-7)-F_6(0)
      >= (4/k-2/3)d
         +X_k((k-1-tau)/2,22/15-d)
         -X_6((6-tau)/2,22/15-d)
      >= 1/4.

PROVED (same script): multiply the last difference minus 1/4 by 144k^2, set k=8+z, and take d=0,7/15. Degree-two Bernstein controls in tau on [0,2] and [2,4] all have strictly positive rational coefficients in z, including the leading coefficients. All twelve controls are recorded in lower35_controls.json. The negative coefficient of B was bounded using B<=d; no isolate margin is spent.

PROVED (lower35.py and the isolate theorem): consequently

    T* >= s/(4(k-7))+s(k-7-s)/k > 0 if s>0.

PROVED (inherited18/inherited17/lower_formula.py): for a fixed lower collection the infinity increment over replacing it by isolates is 2(tr D-tr D^2)+s, strictly positive for s>0. Infinity equality here concerns fixed graphs padded by isolates; no classification of limits with growing lower mass is asserted.

## Equality and balanced fixtures

PROVED (tree35.py; transfer35.py; lower35.py; inherited equality arguments, replayed by replay_all.py): every connected endpoint pair is strict. At equality every extreme pair in the separate-concavity reduction must be an equality. The disconnected reductions force one selected edge in each part and all other vertices isolated. With selected vectors fixed these edges are unique, so convex mixtures cannot create other equalities. Thus the selected-projector closure has exactly two equal edges and isolates as its equality set. Positive lower trace is strict.

PROVED (symmetric35.py; independently the original matrix definition): the complete-top fixture K3+K5 has M0=3 and

    T* = 4(15k^2-83k+14)/(15k^2),
    T*_N8=56/135,  T*_infinity=4,
    T_N8=56/1215,  T_infinity=4/9.

PROVED (same script): at maximal lower trace,

    F_k(k-7)=2(k-3)(11k+7)/(15k^2),
    F_8(1)=95/96,  F_infinity=22/15.

PROVED (same script): at N=10 a lower edge of eigenvalue one realizes this formal endpoint in the selected-projector closure, giving normalized T=95/1176. This is a positive margin, not a counterexample. Extra top multiplicity in clique and endpoint fixtures is handled only with the selected projector; no actual-D>2 theorem is claimed.

| Triangle corner | Five-part fixture | T* at N=8 | T* at infinity |
|---|---|---:|---:|
| PROVED (symmetric35.py): balanced K3 | equal-flux star5 | 526/675 | 194/125 |
| PROVED (symmetric35.py): balanced K3 | equal-flux path5 | 2609/2268 | 673/252 |
| PROVED (symmetric35.py): balanced K3 | equal-flux fork5 | 17741/16200 | 11123/4800 |
| PROVED (symmetric35.py): balanced path3 | K5 | 148/243 | 88/27 |
| PROVED (symmetric35.py): balanced path3 | equal-flux star5 | 3142/6075 | 2738/3375 |
| PROVED (symmetric35.py): balanced path3 | equal-flux path5 | 7187/6804 | 1459/756 |
| PROVED (symmetric35.py): balanced path3 | equal-flux fork5 | 5077/5400 | 68107/43200 |

PROVED (same script): equal-flux means every positive edge flux is one in the stated tree chart. In particular the star and the three-path have equal edge weights; the five-path and fork use the rational weights determined by equal flux. symmetric35_checks.json also records normalized margins and all formal maximal-lower endpoint margins. Two equal edges have T*=T=0 identically.

## Split 4+5 setup

PROVED (setup45.py; inherited four- and five-part concavity certificates): separate K_u concavity is unchanged for the 4+5 split, including fixed lower trace. Its first k is 7. Nontrivial lowers start at k=9 with trace cap S=k-8; exact interpolation is verified. Its moments obey M0=(7-tau)/2, 0<=tau<=5, h=31/20-d, 0<=B<=d<=11/20.

PROVED (setup45.py and inherited extreme classification): the four-side endpoint choices are star4, path4, and rank-at-most-two A4 at scale zero or maximum. The five-side choices are star5, path5, fork5, rank-at-most-two A5 at scale zero or maximum, and the rank-three zero-edge scale endpoint covering twelve support candidates. Disconnected endpoints reduce to the now-proved 3+5, 4+4 and smaller split classes, with arbitrary lowers.

OPEN: the 24 connected 4+5 endpoint types listed in setup45_checks.json still need sign and padding certificates and their maximal-lower-trace certificates, outside inherited special subcases. No complete 4+5 sign theorem is claimed.

## Scope, replay and resources

PROVED (replay_all.py; with STRAT15's full cover retained as the inherited theorem premise): among disconnected D=2 graphs with components of at most five vertices, split 2+2, 2+3, 2+4, 2+5, 3+3, 3+4, 4+4 and now 3+5 permit arbitrary lower components. Triangle, four-vertex and five-vertex double carriers permit arbitrary lowers. The inherited general S5=0 cases remain covered.

OPEN: the full disconnected D=2 statement with component sizes at most five still requires connected split 4+5 and 5+5, with isolates or lower components, outside the already-proved S5=0 subcases.

PROVED (replay_all.py; source_hashes.json): replay uses this folder and installed Python libraries. Every reused proof input is a byte-identical local copy with a recorded SHA-256. All 32 inherited stages and seven new stages are replayed. Inherited receipt generation runs in a temporary local copy so pinned inputs remain unchanged. The STRAT15 full-cover theorem remains an inherited premise and is not rerun here. replay_summary.json hashes every proof module, pinned input, this result, and generated certificate receipt.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

NUMERICAL: replay_summary.json records elapsed time and the sum of parent and largest-child peak RSS, an upper bound on aggregate replay memory. Replay uses one compute child at a time, one thread per numerical library, an 850 MB child watchdog and a 200 MB parent watchdog; the enforced aggregate bound is below 1.5 GB. No solver, process pool, subagent, external proof read, or source-directory edit is required. Workspace proof artifacts are under 500 MB. The parent holds the coordination claim.

Task: “STRAT19: T104 split 3+5 (a connected three-vertex carrier and a connected five-vertex carrier), with isolates and then with arbitrary lower components, every N >= 8; then set up 4+5 if time remains” — received 2026-11-13 18:16 +04.
