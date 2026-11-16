# STRAT17: lower components for seven-vertex split carriers

PROVED (replay_all.py, after all stages PASS): split 2+5 and split 3+4 satisfy T>=0 for every integer N>=7 with arbitrary lower components, each with spectrum strictly below the common top eigenvalue. In fact the lower component sizes need not be bounded by five. Actual connected simple top carriers give T>0. On the selected-projector closures described below the only equality is two equal edges and isolates. Any positive lower trace gives strict positivity, also when lower eigenvalues rise to one.

PROVED (double_increment.py; double_small_gap.py; replay_all.py, using the STRAT15 isolate theorem as an authorized black box): every five-vertex double carrier also permits arbitrary lower components, for every N>=7 and infinity. No new six-dimensional chart cover is used. Its closed equality set contains the two inherited types: two equal edges and isolates, or a balanced triangle and isolates. Positive lower trace is always strict.

## Formula and closures

PROVED (lower_formula.py; independent original-matrix audits in matrix_audit.py; byte-identical inherited16/algebra.py and inherited16/STRAT7/RESULT.md): normalize the common top eigenvalue to one before imposing total edge weight one. Let C be the top-carrier Laplacian on n0 vertices (n0=7 for either split, n0=5 for the double carrier); P is its selected rank-two top projector, P1=0, CP=P. Write D=diag(D1,...,Dj,0) for all lower blocks and additional isolates, with Laplacian spectra in [0,1]. Put k=N-2, M0=tr C/2, s=tr D and M=M0+s/2. Define

    B = sum_ij P_ij (I-C)_ij^2,
    h = sum_i P_ii C_ii,
    Y = 2 sum_(i<j) w_ij (P_ii+P_jj-2P_ij)
                         (2-C_ii-C_jj-2w_ij),
    X_k(m,h) = (m-1)/k^2 [2(k+1)(k-2)-4km+2(k+2)h].

PROVED (same scripts): the exact functional is

    T* = 2(tr C-tr C^2) + 2(tr D-tr D^2)
         +2(k+2)B/k + X_k(M0+s/2,h) - Y,
    T = T*/M^2,     lambda = 1/M.

PROVED (lower_formula.py; matrix_audit.py): lower blocks contribute zero to B, h and Y, increase M by s/2, and increase the spectral term by 2 sum mu(1-mu). Replacing the lower blocks by isolates at the SAME N gives

    Delta T* = 2(tr D-tr D^2) + s B_lower/(2k^2),
    B_lower = 2(k+1)(k-2)-4k(2M0+s/2-1)+2(k+2)h.

PROVED (lower_formula.py): if r=N-n0 and at least one lower component is nontrivial, then s<=r-1<=k-n0+1. With q=k-n0+1-s>=0,

    B_lower = 2k(n0-4M0+h)+4(h-1)+2kq.

PROVED (eigenvector energy identity, replayed in lower_formula.py): h>=1 for every selected rank-two top projector. For each selected unit eigenvector u,

    1 = sum w_ij(u_i-u_j)^2 <= 2 sum C_ii u_i^2;

PROVED (same): sum over its two orthonormal directions. The defect on an edge is w_ij(u_i+u_j)^2>=0.

PROVED (lower_formula.py and the selected-projector interpretation in inherited16/RESULT.md): the closure includes zero weights, disconnected top carriers, extra top eigenvectors within carrier blocks, and lower eigenvalues reaching one. P remains the original selected rank-two projector, extended by zero on lower blocks; it is never replaced by the full top projector when multiplicity rises. No actual-D>2 T104 assertion is made.

## One exact relaxation handles every lower family

PROVED (lower_formula.py): for fixed top C,P, varying a symmetric lower block by E has quadratic coefficient

    -2 tr(E^2) - (tr E)^2/k <= 0.

PROVED (same; the convex domain argument): its closed domain is the compact convex set of Laplacians D with 0<=D<=H_r; row sums are zero and off-diagonals nonpositive. A fixed component partition gives a product of such sets. Thus T* is strictly concave in the lower matrix. We use a stronger spectral relaxation than listing all extreme supports: 2 sum mu(1-mu)>=0 for every spectrum in [0,1], retain only the trace bound, and minimize the remaining scalar concave quadratic over a whole interval. This includes edges, paths, forks, stars, triangles, all low-rank families, and all larger supports at once. No unproved lower extreme-point inventory is used.

PROVED (lower_formula.py): define

    F_k(s) = 2(tr C-tr C^2)+2(k+2)B/k-Y+X_k(M0+s/2,h).

PROVED (same): for any S>0 and 0<=s<=S the exact identity is

    F_k(s) = (1-s/S)F_k(0)+(s/S)F_k(S)+s(S-s)/k,
    T* >= F_k(s).

PROVED (same): this reduces ANY NUMBER of lower components simultaneously to s=0 and s=S. It avoids adding components one at a time with a changing baseline. For either nominal seven-vertex split with nontrivial lowers, N>=9, k>=7 and S=k-6 is valid.

## Split endpoint comparison and the inherited margin

PROVED (split_endpoint_certificate.py): suppose a top endpoint has

    M0=(5-tau)/2,  h=c-d,
    0<=tau<=2,  0<=B<=d<=c-1,
    c=13/10 or 17/12.

PROVED (same): at S=k-6, for every real k>=7,

    F_k(S)-F_5(0)
      = (4/k-4/5)B
        +X_k((k-1-tau)/2,c-d)-X_5((5-tau)/2,c-d)
      >= (4/k-4/5)d
        +X_k((k-1-tau)/2,c-d)-X_5((5-tau)/2,c-d)
      >= 3/10.

PROVED (same): to replay the final inequality, multiply its difference from 3/10 by 1500k^2, put k=7+z, and take the two endpoints d=0,c-1. It is affine in d. Its degree-two Bernstein controls in tau/2 on [0,1] are strictly positive polynomials in z. The script reconstructs the Bernstein identity and checks every rational coefficient, twelve controls total. The z^2 coefficients are strictly positive, so infinity is included. No floating optimization enters this certificate.

PROVED (Schur product theorem and gap decomposition; audited at exact fixtures by matrix_audit.py): for each component gap S_i=A_i-J/ni, let D_i=diag(diag S_i). Since 0<=S_i<=H_ni,

    (H_ni-S_i) o S_i = D_i-S_i/ni-S_i o S_i >=0.

PROVED (same): selected top directions annihilate S_i and 1, giving 0<=B_i<=sum P_ii(S_i)_ii. Summing gives B<=d. The identity h=c-d and the energy bound h>=1 give d<=c-1.

PROVED (replay_all.py with the convex reductions in inherited16/RESULT.md): fixed lower blocks do not change any top-block quadratic variation. Indeed X_k(M+ell,h)-X_k(M,h) is affine in the varying top mass and moment. Thus the exact five-part and four-part concavity certificates, and the separate triangle-gap concavity certificate, apply unchanged.

PROVED (same): for split 2+5, reduce the five-part exactly as STRAT16 did. If rank A5<=3, set S5=A5-J5/5 and tau=tr S5<=2. Then M0=(5-tau)/2, h=13/10-d, B<=d<=3/10. The new comparison uses the unchanged inherited k=5 rank-at-most-three certificate (inherited16/verify_sos.py), whose endpoint margin is 1/400000; its zero-gap endpoint has margin 63/250. The inherited padding identity (inherited16/padding_monotonicity.py) gives F_k(0)>=F_5(0). Consequently

    T* >= F_5(0)+(3/10)s/(k-6) >= 1/400000

PROVED (same): at these endpoints. The old SOS margin is preserved in full; it is not subtracted to pay for the negative increment. The new lower-trace endpoint has an additional 3/10. Five-part rank-four connected extremes are the three trees. The bipartite sign Rayleigh bound gives tr C5<=5/2, hence M0<=7/4 and

    7-4M0+h >=1,    h>=1.

PROVED (lower_formula.py; split_endpoint_certificate.py): their increment is nonnegative, strictly positive for positive lower trace. Disconnected five-part extremes and mixed block selections reduce to inherited split 2+4, 2+3 or 2+2 with arbitrary lowers; those are replayed from inherited16/lower_components.py and inherited16/disconnected_certificate.py. Linearity in the selected projector handles block-selection mixtures.

PROVED (replay_all.py with inherited16/split34_reduction.py): for split 3+4, reduce the triangle to its balanced corner and zero-edge path corner, then the four-part to its extremes. If rank A4<=2, its gap rank is at most one and the triangle gap rank is at most one. Their total tau<=2 gives M0=(5-tau)/2 and h=17/12-d with B<=d<=5/12. The new comparison gives

    F_k(k-6) >= F_5(0)+3/10 >0.

PROVED (same): here F_5(0)>=0 is the unchanged exact isolate-only corner certificate in inherited16/split34_boundary.py. No quantitative old margin is spent. F_k(0)>=0 is also inherited. The exact trace interpolation proves positivity for every positive lower trace. Four-part tree endpoints have tr C4<=2 and the triangle has tr C3<=2; therefore M0<=2 and 7-4M0+h>=0. Their increment is nonnegative. Disconnected endpoints reduce to inherited split 3+3, 2+4 or 2+3, all with arbitrary lowers.

## Negative increments and equality

PROVED (matrix_audit.py): monotonicity of T* under adding lower edges is false even at feasible rational points with actual D=2. At N=9 let P_n project onto (1,-1,0,...,0), epsilon=1/100, and C_n=H_n-epsilon(H_n-P_n). For split 2+5 use C2=P2 and C5 as above; for split 3+4 use C3,C4. Add a lower edge with eigenvalue 99/100. The increments are respectively

    -975843/4900000,   -349173/1960000.

PROVED (same): the resulting full T* values are respectively 84843/98000 and 923967/980000, both positive. These exact fixtures invalidate the naive increment argument and do not invalidate T104. The original normalized definition is independently checked. The proof above concerns the sign of T*=M^2 T; normalization itself also changes under adding a lower block.

PROVED (replay_all.py, convex reductions and inherited equality ledger): both split closed classes have equality exactly at two equal edges and all remaining vertices isolated, including infinity. All positive lower traces give strict positivity at every reduced endpoint and hence throughout the concave top domains. With no lower trace the STRAT16 equality proof applies. Near the two-edge limit M0=1,h=1; for example M0<=5/4 implies 7-4M0+h>=3, so adding positive lower trace has strictly positive increment. Thus the isolate-only vanishing margin is never used to absorb a negative increment near equality.

PROVED (lower_formula.py): for any FIXED lower collection, at infinity

    Delta T*_infinity=2(tr D-tr D^2)+s,

PROVED (same): strictly positive when s>0. This also proves the infinity equality assertion directly, independently of unbounded trace-relaxation endpoints.

## Five-vertex double carrier: no new chart cover

PROVED (double_increment.py; double_small_gap.py; double_small_gap_audit.py; STRAT15 theorem copied in prior15/RESULT.md is a black-box premise): write C=H5-S, Q=H5-P, where Q is the rank-two orthogonal projector complementary to the selected top space. Diagonalize S on this space:

    S=a uu^T+b vv^T,  a>=b>=0,  tau=a+b<=2,
    M0=(4-tau)/2,     0<=a,b<=1.

PROVED (double_increment.py): the general increment coefficient is

    5-4M0+h = 2(tau-1)+(h-1).

PROVED (same): for tau>=1 its sign is nonnegative. For tau>1 and positive lower trace it gives strict positivity even in the closed lower spectral domain. At tau=1 use the following positive endpoint bound. The two equal edges and balanced-triangle equality centers both have tau=2, so the increment is positive throughout their sufficiently small neighborhoods whenever lower trace is positive.

PROVED (double_small_gap.py; matrix identities independently checked by double_small_gap_audit.py): now suppose 0<=tau<=1. Let e=tr(CS)=tau-a^2-b^2. For an edge put U=(u_i-u_j)^2 and V=(v_i-v_j)^2, and define

    J = sum_(i<j) w_ij (U+V)(aU+bV),
    L = (a-b)(1-a)^2+b(2-tau)^2.

PROVED (same): the identities CP=P and P=H5-Q give

    Y=4e-2J,    X1*-Y=-2e+2J,    B>=0.

PROVED (same; two weighted Cauchy inequalities): pointwise

    (U+V)(aU+bV)
      = (a-b)U^2+b(U+V)^2+(a-b)UV
      >= (a-b)U^2+b(U+V)^2.

PROVED (same): the weight sum is M0 and the two weighted first moments are

    sum w_ij U=1-a,    sum w_ij(U+V)=2-tau.

PROVED (same): hence J>=L/M0. This uses the actual nonnegative top edge weights and is valid on the entire closure; it does not impose linearized weight feasibility. The script checks the weighted pair-sum Cauchy identity exactly; the displayed sum-of-squares derivation is independent of the number of edges.

PROVED (same): with q_i=u_i^2+v_i^2 and F=sum q_i S_ii,

    h=8/5-4tau/5+F,
    F>=a sum u_i^4+b sum v_i^4>=tau/5,
    h>=8/5-3tau/5.

PROVED (same): the last step is ordinary Cauchy on five coordinates, sum u_i^2=sum v_i^2=1. No sharp moment polytope, numerical bound, or previous chart margin is required.

PROVED (lower_formula.py): for nontrivial lower components on r=N-5 vertices, k>=5 and 0<=s<=S0=k-4. The same exact trace interpolation reduces to s=0 and S0. At the latter endpoint M=(k-tau)/2. Since M-1>0, insert the lower bound for h into X_k. Writing z=1/k gives exactly

    X_k((k-tau)/2,8/5-3tau/5)
      = (3+2tau)/5 - tau(13+2tau)z/5
        -6(tau+2)(1-tau)z^2/5.

PROVED (double_small_gap.py): all subtracted coefficients are nonnegative for 0<=tau<=1, so k=5 is the hardest endpoint, including infinity. At k=5 it equals

    X=(3-tau)(21+4tau)/125.

PROVED (same): dropping the nonnegative B term therefore gives

    F_k(k-4) >= X-2e+2L/M0
              = N(tau,a)/(125(4-tau)),
    N(t,a)=1000a^3-1000a^2t+1000at-1000a
           +254t^3-757t^2+401t+252,
    t/2<=a<=t,   0<=t<=1.

PROVED (same): two exact polynomial identities prove N>=50/27:

    N(t,a)-N(1,a)=(1-t)R(t,a),
    R=1000(a-1/2)^2+40+(t-1/2)(376-254t),
    N(1,a)=1000(a-2/3)^2(a+1/3)+50/27.

PROVED (same): for 1/2<=t<=1 every displayed term is nonnegative. For 0<=t<=1/2 use

    N(t,a)-N(t,t)=1000(a-t)(a^2+t-1)>=0,
    N(t,t)-45=(1-2t)(207-185t-127t^2)>=0,
    207-185t-127t^2
      =331/4+185(1/2-t)+127(1/4-t^2)>0.

PROVED (same): thus N>=50/27 throughout, and 125(4-t)<=500 yields the uniform positive endpoint margin

    F_k(k-4)>=1/270.

PROVED (same; the STRAT15 isolate theorem): F_k(0)>=0 for every real k>=5 and infinity. Combining this black-box statement with the exact trace identity gives, for tau<=1 and finite k,

    T* >= s/[270(k-4)] + s(k-4-s)/k >0   if s>0.

PROVED (same): tau>=1 was already covered by the increment comparison, and tau=1 has the new strict bound. At infinity a fixed positive lower collection gives increment 2(tr D-tr D^2)+s>0 directly. This closes the ENTIRE five-double lower-component class without rerunning or extending STRAT15's 9,370-box cover. Arbitrary lower component sizes are allowed.

PROVED (matrix_audit.py): a connected rational double-carrier example with tau=1/50 and a lower 99/100 edge has Delta T*=-250899/1250000 but full T*=691053/1250000>0. The new endpoint bound supplies the missing argument despite the negative increment.

PROVED (replay_all.py and STRAT15's inherited equality theorem): the five-double selected-projector closure has exactly the two equality types already present with isolates: two equal edges, and a balanced triangle, up to permutation and normalization. Any positive lower trace is strict. The balanced-triangle limit must be retained here; it is excluded only from the split classes by their persistent second top carrier. No actual connected five-vertex double carrier is an equality graph.

## Optional split 4+4 setup

PROVED (split44_setup.py; inherited16/prior_concavity4.py): fix both unit top vectors u,v and the product K_u x K_v of the two four-part convex domains. T* is separately concave in each block by the unchanged four-part quadratic certificate. The first padding size is N=8, k=6+z. Exact matrix fixtures independently check both quadratic variations against the inherited formula. Each block reduces to its two trees, rank-at-most-two A4 boundaries, or disconnected extremes.

PROVED (the now-closed smaller split classes with lowers): disconnected 4+4 extremes reduce to 3+4 or 2+4 with additional isolates or lower components and are therefore covered. OPEN: all connected endpoint-pair families still require their full signs: tree/tree, tree/rank-at-most-two, rank-at-most-two/rank-at-most-two. No complete 4+4 theorem is claimed.

## Scope and replay

PROVED (replay_all.py plus the stated STRAT15 black-box premise): among disconnected D=2 graphs with component sizes at most five, arbitrary lower components are now allowed for split 2+2, 2+3, 2+4, 2+5, 3+3, 3+4, triangle double carriers, and four-vertex double carriers. Five-vertex double carriers are now covered with arbitrary lower components as well. General S5=0 cases remain covered.

OPEN: precisely the split pairs 3+5, 4+4, 4+5, 5+5 with isolates or lower components, after removing already-covered S5=0 cases. Thus the full disconnected D=2 statement with components of size at most five remains OPEN. The optional 4+4 fixed-vector setup is recorded above.

PROVED (replay_all.py): replay reads only this folder. source_hashes.json pins every byte-identical inherited input. replay_summary.json hashes all proof scripts, data inputs, provenance statements and this result. STRAT16 is replayed as seventeen individual exact stages. STRAT15 is a theorem black box: only its statement and receipt are copied; its full cover is neither rerun nor claimed to have been replayed.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

NUMERICAL: final runtime, child peak RSS, parent peak RSS and their conservative aggregate upper bound are recorded in replay_summary.json. Replay is sequential, with one compute child at a time, single-thread libraries, and a 1 GB child peak watchdog. No solver, subagent, accelerated mode, external database mutation, or outside-folder mutation is used. The parent holds the coordination claim for this workspace.

Task: “STRAT17: T104 lower components for the five-vertex classes” — received 2026-11-13 15:57 +04; resumed 16:09 +04.
