# STRAT16: split 2+5, split 3+4 and lower components

PROVED (replay_all.py): the complete 2+5 and 3+4 split classes satisfy T>0
when both carriers are connected and simple at the top, every N>=7, and
infinity. Their auxiliary closures have T>=0, with equality exactly at two
equal edges and isolates. The combined exact replay is recorded below. No
counterexample exists in either class. The balanced-triangle-only limit
is excluded below. Four-vertex double carriers and split 2+3,2+4,3+3
also permit arbitrary lower components, as proved below.

## Functional and domain

PROVED (algebra.py; exact_audit.py audits the original matrix definitions):
give the five-vertex Laplacian C top eigenvalue one and the external edge
weight 1/2 before normalization. For a selected unit zero-sum top vector u
put A=I5-C, k=N-2=5+z, z>=0, and

    M=(1+tr C)/2,   h=1/2+sum_i u_i^2 C_ii,
    B=sum_ij u_i u_j A_ij^2,
    Y=2 sum_(i<j) w_ij (u_i-u_j)^2 (2-C_ii-C_jj-2w_ij).

PROVED (algebra.py; exact_audit.py): STRAT7 formula (1) specializes to

    T*=2(tr C-tr C^2)+2(k+2)B/k
       +(M-1)/k^2 [2(k+1)(k-2)-4kM+2(k+2)h]-Y.       (1)

PROVED (exact_audit.py, with the derivation of STRAT7 formula (1)):
lambda=1/M, T=T*/M^2. The edge contributes zero to X1*, B and Y, and
1/2 to h. Isolates contribute zero. At infinity,

    T*_infinity=2(tr C-tr C^2)+2B+2(M-1)-Y.

PROVED (concavity_certificate.py; exact_audit.py): for fixed u the domain is

    K_u={A=A^T, A PSD, A entrywise nonnegative, A1=1, Au=0}.

PROVED (same scripts): it is compact and convex. Its elements give
Laplacians C=I-A with spectrum in [0,1]. The actual class has connected C
and ker A=span(u). The auxiliary closure also includes disconnected C and
larger kernels. On that closure P always means the selected rank-two
projector uu^T plus the external edge contrast. It is not replaced by the
full top projector when multiplicity rises above two. No actual-D>2
version of T104 is asserted.

## Concavity

PROVED (concavity_certificate.py): for E1=Eu=0, p_i=u_i^2, d=diag E,
m=tr E/2, the quadratic coefficient is

    Q=-2 tr E^2+(-2+4/k) sum_ij u_i u_j E_ij^2
      +4 sum_i p_i(E^2)_ii-2 p^T E d
      +m/k^2 [-4k m+2(k+2)p^T d].

PROVED (concavity_certificate.py): order an unnormalized U decreasingly,
write U_i=sum_(j=1..4)(5-j if i<=j else -j)x_j, x_j>=0, and R=U^TU.
The 5-by-3 spanning matrix K, columns j=2,3,4, has

    K_1j=U5-Uj, K_jj=U1-U5, K_5j=Uj-U1,

PROVED (concavity_certificate.py): all other entries zero. Its columns
span {1,U} perpendicular, so E=K V K^T, with symmetric 3-by-3 V and six
coordinates. The matrix of -R k^2 Q has 252 polynomial coefficient
matrices. Seven raw matrices are indefinite; on each of the 24 orderings
of the four gaps substitute largest=a+b+c+d, next=b+c+d, next=c+d,
smallest=d. All 252 matrices on every cone are exactly PSD by rational
symmetric elimination, including singular pivots. Hence T* is concave
for every real k>=5 and at infinity. Failure of the raw coefficient test
was certificate insufficiency, not failure of concavity.

## Extreme points

PROVED (extreme_inventory.py; the face argument here): at rank r, let Q
span range(A) intersect 1-perpendicular. A is extreme exactly when

    V -> ((Q V Q^T)_ij : i<j, A_ij=0)

PROVED (extreme_inventory.py; face argument): is injective on symmetric
(r-1)-by-(r-1) V. Every two-sided perturbation stays in the PSD face and
vanishes at entrywise zero constraints; conversely a kernel element gives
a small two-sided perturbation. There are r(r-1)/2 free directions.
Diagonals cannot vanish: PSD would force a zero row, contradicting A1=1.

PROVED (rank_two_certificate.py): rank one is J5/5. At rank two,

    A=J5/5+g vv^T,  v^T1=0, ||v||=1,
    0<=g<=1/(5p), p=max(-v_i v_j)>=1/5.

PROVED (rank_two_certificate.py): the extreme rank-two endpoint has
g=1/(5p). For every selected u perpendicular to 1,v, T*>0 throughout
this entire boundary for k>=5 and infinity. Endpoint matrices have 252
and 858 raw PSD coefficient matrices. Positive definite pure-axis
coefficients prove strictness; concavity gives intermediate g.

PROVED (extreme_inventory.py): connected rank-four extreme points have
at most four edges, hence are the star, path or fork. For positive edge
fluxes x_e set s_i=sum_(e incident to i)x_e, choose alternating signs,

    U_i=sign_i s_i,        w_ij=x_(ij)/(s_i+s_j).

PROVED (tree_certificate.py): these give every weighted five-vertex tree
with top eigenvalue one. The edge-cut equations give the converse; the
signless-Laplacian Perron theorem identifies the top vector. The fixed-U
tree weights are unique, so these points are extreme. Clearing the
positive denominator R k^2 product_e(s_i+s_j)^2 gives respectively
846, 597, 693 nonzero coefficients, all positive, with witnesses at z^0
and z^2. Thus all three families have T*>0, including infinity.

PROVED (extreme_inventory.py): connected rank-three extreme points have
at most seven edges. They are not bipartite, because connected bipartite
Laplacians have simple top eigenvalues. There are twelve support
candidates: four each with five, six and seven edges. Their complete
representatives are in extreme_graphs.json. The injectivity criterion,
not support count alone, decides extremality within these families.

PROVED (extreme_inventory.py): more explicitly, the five-edge candidates
are a triangle with two leaves at one vertex, a triangle with leaves at
different vertices, a triangle with a two-edge tail, and C5. The six-edge
candidates are a diamond with a leaf at a degree-three vertex, a diamond
with a leaf at a degree-two vertex, two triangles sharing one vertex,
and the house graph. The seven-edge candidates are K5 minus, respectively,
a three-edge star, a triangle, a four-vertex path, and a disjoint
three-vertex path plus edge. All omitted vertices in the complements
are isolated.

PROVED (verify_sos.py; verify_rank_three_algebra.py;
padding_monotonicity.py): all rank-three A are strictly positive, covering
all twelve support candidates at once, as follows.

PROVED (verify_rank_three_algebra.py): write A=J5/5+S, S PSD, S1=Su=0,
rank S<=2, 0<=S<=H5. Set tau=tr S, v=tr S^2, d=diag S, D=diag(d),
C=S o S, and z=1/k. On a selected unit u the functional is u^T F(z)u,
where

    F=F0+Bp z+Ep z^2,
    F0=(3+3tau/5-2v)I-2D-2diag(Sd)+4diag(diag S^2)-2C,
    Bp=4C+(3-tau)(tau-47/10)I-(3-tau)D,
    Ep=(3-tau)(3I/5-2D).

PROVED (padding_monotonicity.py): put Q=(H5-S)oS=D-S/5-C PSD. Since
tau<=2, D>=0 and 4I/5-D>=0, the exact identity

    F'(z)=-g(tau)I-(1+tau)(4I/5-D)-4S/5-4Q
          -4z(3-tau)D-(6/5)(3-tau)(1/5-z)I,
    g(tau)=3/50+(213/50)(2-tau)+(2-tau)^2

PROVED (padding_monotonicity.py): gives F'(z)<=-3I/50 on 0<=z<=1/5.
Thus N=7 is the hardest padding size; it suffices to certify that endpoint.

PROVED (verify_rank_three_algebra.py; verify_sos.py): by concavity in the
scale of S it suffices to take S=0 and the first zero-edge endpoint.
For the latter write S=VV^T/(5t), with rows

    V1=(x,y), V2=(v,w), V3=(1-t-x-v,-z-y-w),
    V4=(t,0), V5=(-1,z).

PROVED (verify_rank_three_algebra.py): choose a pair with most negative
gap inner product, rotate the larger-norm member to V4, reflect z>=0 and
order the remaining x coordinates. Nonnegative edge numerators
g_ij=t+(VV^T)_ij and the zero row sums give the complete root box

    [1,4] x [-1,0] x [-4,4] x [-1,1/2] x [-4,4] x [0,4].

PROVED (verify_rank_three_algebra.py): the row identities
sum_(j!=i)g_ij=4t-(VV^T)_ii imply t<=4 and |y_i|<=4. The norm ordering
t^2>=1+z^2 gives t>=1. Also x_i>=-1 from g_i4>=0; sorting and
sum_(i=1..3)x_i=1-t give x1<=0, x2<=1/2. No chart point is omitted.

PROVED (verify_sos.py): let K0=(e1-e5,...,e4-e5). The exact certificate is

    50t^2 K0^T [F(1/5)+S] K0
      = I4/100 + sum_free Z_j^T G_j Z_j
        +sum_(9 edges) g_ij Z_ij^T G_ij Z_ij
        +sum_(6 coordinates) (x_i-a_i)(b_i-x_i) Z_i^T G_i Z_i.

PROVED (verify_sos.py): all 22 rational Gram matrices are positive
definite. Their PSD witnesses are integer triangular factors with strictly
diagonally dominant positive residuals; every polynomial coefficient is
reconstructed exactly. The saved certificate is rational_sos_2.json.
No solver status, floating eigenvalue or rounding tolerance enters replay.
The added S vanishes on selected u. Since ||u||^2<=5||u[1:4]||^2 and
t<=4, the zero-edge endpoint has T*_7>=1/400000. The S=0 endpoint has
T*_7=63/250. Concavity and monotonicity therefore prove strict positivity
on all rank-at-most-three A, for all k>=5 and infinity.

## Disconnected extremes

PROVED (disconnected_certificate.py plus STRAT7's padded statements): a
4+1 five-part uses the 4+2 split theorem; a 3+1+1 five-part uses the 3+2
triangle-corner theorem. For a 3+2 five-part, selecting its edge gives
S5=0. Selecting its triangle leaves an additional lower edge, whose free
eigenvalue has extreme endpoints zero and one. Mixtures of the two block
selections give convex combinations of these functionals: cross-block
projector entries contribute zero to (1).

PROVED (disconnected_certificate.py): write triangle gap g in [0,1],
M=(3-g)/2, h=(7-g)/6, lower-edge eigenvalue t in [0,1]. Adding that edge
changes T* by 2t(1-t) plus t/(2k^2) times

    2(k+1)(k-2)-4k(2M+t/2-1)+2(k+2)h.

PROVED (disconnected_certificate.py): with t=1-q, k=5+z this bracket is

    7/3+31z/3+2z^2+(53/3+11z/3)g+(10+2z)q > 0.

PROVED (disconnected_certificate.py): thus the zero lower-edge endpoint
reduces to STRAT7's 3+2 case and a positive lower edge increases T*.
Other partitions select edges and have S5=0. STRAT7's X1,X2,X3>=0
argument also holds for a selected rank-two top projector on a larger
top space. Equality in this disconnected five-part closure requires
exactly two equal edges and isolates.

PROVED (disconnected_certificate.py; prior_triangles.py): this extends
further. Add arbitrary lower components on r vertices, with unnormalized
trace s, their spectra in [0,1], and at least one nontrivial component.
Then s<=r-1<=k-4. The full increment is

    2(tr L_lower-tr L_lower^2)
      +s/(2k^2) [2(k+1)(k-2)-4k(2M+s/2-1)+2(k+2)h].

PROVED (disconnected_certificate.py): set s=k-4-q and k=5+z. The bracket is

    7/3+z/3+(53/3+11z/3)g+(10+2z)q > 0.

PROVED (disconnected_certificate.py): the spectral first term is
nonnegative, and any positive lower trace makes the second term positive.
Hence split 2+3 allows arbitrary lower components, even without a size-five
restriction, for N>=7 and infinity. Equality still requires two equal edges
and all other vertices isolated.

## Optional 3+4 extension

PROVED (prior_concavity4.py; split34_reduction.py): fix the selected unit
top vector of the four-part and its convex K_u as in STRAT7. The quadratic
variation (5) is unchanged by replacing the fixed external edge by a fixed
triangle: every second variation is supported in the four-part. Thus the
unchanged six-cone rank-four concavity certificate applies. On the triangle
write L3=H3-g vv^T with its selected top direction perpendicular to 1,v.
For m=(sum v_i^3)^2<=1/6, the coefficient of g^2 is

    -5/3-1/(6k)+1/(3k^2)+4(1-1/k)m
      <= -1-5/(6k)+1/(3k^2)<0.

PROVED (split34_reduction.py): this identity is independent of the other
component's mass and diagonal moment. Strict separate concavity reduces
the triangle to g=0 and its zero-edge endpoint g=1/(3p). The former is a
balanced triangle with a retained rank-one selection; its contribution is
orientation independent. The latter is a path, parametrized by positive
fluxes a,b:

    U3=(a,-a-b,b), w01=a/(2a+b), w12=b/(a+2b).

PROVED (split34_trees.py): the four-part's rank-three connected extremes
are its star and path. For those two tree types and the two triangle
corners, clearing the positive denominator R4 R3 D4^2 D3^2 k^2 gives
135, 927, 117, 801 nonzero coefficients, all positive. Strict witnesses
occur at both k=5 and infinity.

PROVED (split34_boundary.py): rank-at-most-two four-parts are
J4/4+c vv^T. At c=0 and c=1/(4p), paired with the balanced/path triangle
corners, the polynomial 2-by-2 matrices have respectively 84,198,588,1386
coefficient matrices, all exactly PSD. Positive definite pure gap/flux
axis coefficients prove strictness, including infinity. The denominator
is ||V||^4 k^2 D3^2 R3 H^2, with H=1 or 4(-Vmax Vmin)>0, and selected
top vectors are represented by the same 4-by-2 K as STRAT7.

PROVED (prior_triangles.py; split34_reduction.py;
disconnected_certificate.py): disconnected four-part extremes reduce to
the two-triangle theorem, its 3+2 edge boundary, or an additional lower
edge. Cross-block top selections give convex combinations. The new lower
component comparison handles the additional edge. The two-triangle
certificate and its leading-k coefficients have equality only when both
carriers degenerate to edges. Strict separate concavity and the unique
zero extreme pair therefore prove the full 3+4 class with isolates, with
the same two-edge equality set in the auxiliary closure.

PROVED (split34_audit.py): every new tree and boundary construction is
independently checked against the original normalized selected-projector
matrix definitions at rational fixtures and several padding sizes.
prior_concavity4.py and prior_triangles.py are byte-identical copies of
the supplied STRAT7 scripts; replay_all.py checks this before execution.

## Further lower-component extensions

PROVED (lower_components.py): four-vertex double carriers and split
2+4,3+3 also allow arbitrary lower components, not merely isolates. For
any fixed carrier graph on n0 vertices with mass M and selected moment h,
let the added lower Laplacian have trace s. At least one lower component
gives s<=r-1<=k-n0+1. Write q=k-n0+1-s>=0. The exact increment is

    Delta T*=2(tr L_lower-tr L_lower^2)+s/(2k^2) B_lower,
    B_lower=2k(n0-4M+h)+4(h-1)+2kq.

PROVED (lower_components.py): the spectral first term is nonnegative.
At the following nonzero convex-reduction endpoints, h>=1 and the
coefficient n0-4M+h has a positive lower bound:

| Carrier endpoint | Lower bound |
|---|---:|
| Four-vertex double carrier, gap g=gmax | 1/4 |
| Split 2+4, rank-two four-part at g=gmax | 1/8 |
| Split 2+4, four-part tree | 1 |
| Split 3+3, at least one nonzero gap corner | 5/9 |

PROVED (lower_components.py): for the first row, gmax>=1/2, q4=sum v_i^4
>=1/4 and h=3/2-3g/4+gq4 give

    n0-4M+h=-1/2+(5/4+q4)g >=1/4,
    h-1=(1-g)/2+g(q4-1/4)>=0.

PROVED (lower_components.py): for split 2+4 let a=sum u_i^2 v_i^2<=1/4.
Then h=5/4-ga>=1 and n0-4M+h=-3/4+(2-a)g>=1/8 at gmax>=1/2.
At the tree endpoints the bipartite sign Rayleigh quotient gives
tr L4<=2, hence M<=3/2. Also the top eigenvector identity and
(u_i-u_j)^2<=2(u_i^2+u_j^2) give h>=1, proving the third row.

PROVED (lower_components.py): for two triangle corners let G=g1+g2.
If G>0, then G>=2/3 and G<=2, so h=4/3-G/6>=1 and
n0-4M+h=-2/3+11G/6>=5/9. The remaining zero-gap corners have S5=0.
Even after maximal lower trace, their X3 brackets are respectively

    four-double: k+2+2kq,
    split 2+4: 5k/2+1+2kq,
    split 3+3: 8k/3+4/3+2kq,

PROVED (lower_components.py): all strictly positive for k>=5. The fixed
gap concavity coefficients are independent of lower mass. The four-part
Ku concavity certificate is also unchanged by fixed lower blocks.
Disconnected four-part extremes reduce to the proved 2+3 theorem with
arbitrary lower components or to S5=0. Thus endpoint comparison and the
same convex reductions prove all three extensions. Every positive lower
trace gives strict positivity; at infinity the increment is exactly
2(tr L_lower-tr L_lower^2)+s>0. Equality requires all lower vertices
isolated. The inherited four-double equality analysis is independently
checked at infinity in lower_components.py. Its finite theorem is
replayed from the byte-identical prior_four.py copy of STRAT7.

## Equality and scope

PROVED (replay_all.py, convex reduction): every member of compact K_u is
a finite convex combination of extreme points. Concavity and the exact
boundary certificates give nonnegativity. Only the two-edge graph can
be a zero extreme point; for fixed u it is unique. Hence any zero convex
combination is that same graph. Actual connected five-parts give T>0.
PROVED (normalization (1)): the balanced-triangle-only graph
cannot be a limit of this class. Since tr C<=4, M<=5/2 and the external
normalized edge weight is 1/(2M)>=1/5, independently of the padding.
This positive isolated edge persists in every limit.

OPEN: for the broader disconnected D=2 statement with components of size
at most five, the remaining combinations are exactly these unclosed
classes, after removing the proved S5=0 cases:

- Five-vertex double carriers with any nontrivial lower component.
- Split pairs 2+5,3+4 with additional nontrivial lower components.
- Split pairs 3+5,4+4,4+5,5+5, with or without lower components.

PROVED (replay_all.py plus the cited inherited results): split 2+2 and
balanced-triangle double carriers permit arbitrary lower components by
S5=0. Split 2+3,2+4,3+3 and four-vertex double carriers now permit arbitrary
lower components by the increment lemmas and convex reductions. Split
2+5,3+4 and five-vertex double carriers permit isolates. In particular the
disconnected D=2 statement with every component of size at most three is
closed for N>=7. No closure of the OPEN combinations is asserted.

PROVED inherited scope (STRAT7/RESULT.md; ../STRAT15/RESULT.md): split
2+3,2+4,3+3 with isolates; four-vertex double carriers with at most one
lower edge; five-vertex double carriers with isolates; general S5=0.
STRAT15 was read only and was not copied.

## Replay

PROVED (replay_all.py): all seventeen exact stages passed. Replay with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

PROVED (replay_all.py): this invokes only exact certificates, including
the saved rational SOS certificate and the three byte-identical STRAT7
copies. It runs no discovery or numerical solver. replay_summary.json
records every PASS and the hashes of all proof inputs; each stage also
has a .replay.out file.

NUMERICAL: the final replay took 59.235993 seconds. Peak child RSS was
86,016,000 bytes and parent peak RSS was 18,087,936 bytes. The workspace
occupied about 4.5 MB at the final audit. Discovery used at most two solver
workers; exact replay is sequential. No subagents were used. No STRAT7
or STRAT15 source was edited. The full inherited STRAT15 proof was not
rerun; its statement is used only in the broader scope ledger.

NUMERICAL operational limit breach: two dense SOS attempts reported
individual ru_maxrss peaks 3,290,120,192 and 3,292,807,168 bytes before
termination. They overlapped briefly; no aggregate peak was sampled.
This exceeded the requested 2.5 GB limit. The next dense attempt was
stopped at 2,133,540,864 bytes. The smaller block ansatz now has a rapid
guard. The successful sparse solve peaked at 1,626,324,992 bytes; its slow
qdldl predecessor peaked at 1,361,068,032 bytes and stopped at its own
900-second guard. Sandbox denial prevented earlier termination, so they
overlapped; aggregate RSS was not sampled. Discovery now uses an exclusive
workspace lock to prevent this overlap. No numerical attempt is a proof.

Task: “STRAT16: T104 split simple top carrier 2+5 ... plus isolated vertices,
every N >= 7” — received 2026-11-13 14:34 +04 (workspace launch).
