# STRAT18: split 4+4

PROVED (replay_all.py, all stages must PASS): split 4+4 satisfies T>=0 for every integer N>=8, with isolates or arbitrary lower components, and for fixed graphs padded to N->infinity. Lower component sizes need not be bounded by five. Two connected simple four-vertex top carriers give T>0. On the selected-projector closure, equality occurs exactly at two equal edges and isolates. Every positive lower trace gives strict positivity, including when lower eigenvalues reach one in the closure.

## Functional and reduction

PROVED (inherited17/lower_formula.py; inherited17/matrix_audit.py; symbolic44.py; audit44.py): normalize the common top eigenvalue to one. For the two top blocks C=C4 direct-sum C4', let P=uu^T direct-sum vv^T, where u,v are their selected unit top directions. Put k=N-2, M0=tr(C)/2 and

    h=sum_i P_ii C_ii,
    B=sum_ij P_ij (I-C)_ij^2,
    Y=-2 sum_(i<j) C_ij (P_ii+P_jj-2P_ij)
                         (2-C_ii-C_jj+2C_ij),
    X_k(m,h)=(m-1)/k^2 [2(k+1)(k-2)-4km+2(k+2)h].

PROVED (same scripts): if D contains all lower components, s=tr D and M=M0+s/2, then

    T*=2(tr C-tr C^2)+2(tr D-tr D^2)
       +2(k+2)B/k-Y+X_k(M,h),
    T=T*/M^2.

PROVED (inherited17/split44_setup.py; inherited17/inherited16/prior_concavity4.py; inherited17/lower_formula.py): fixing u,v gives separate concavity on K_u x K_v, where K_u={A PSD, A>=0 entrywise, A1=1, Au=0}, C4=I-A. Fixed lower blocks do not change either quadratic variation. This holds for k>=6 and infinity.

PROVED (the inherited face argument, replayed through inherited17/inherited16/extreme_inventory.py; inherited17/RESULT.md): an extreme A of rank r has r(r-1)/2 independent face directions to constrain. On four vertices, connected rank-three extremes therefore have at most three edges and are the star or path. The other connected cases have rank at most two. Disconnected extremes reduce to the already-proved 3+4, 2+4 or smaller split classes with arbitrary lowers. Projector mixtures over disconnected blocks are handled by linearity; cross-block projector entries do not contribute to the functional.

## Exact connected endpoint certificates

PROVED (algebra44.py; tree44.py; symbolic44.py): for a four-tree, assign positive fluxes x_e and alternating vertex signs. With s_i=sum_(e incident i) x_e, the unnormalized top vector and weights are

    U_i=sign_i s_i,   w_ij=x_ij/(s_i+s_j).

PROVED (same scripts; inherited tree parametrization): this covers every weighted four-tree with top eigenvalue one. Let R=U^T U and D=product_e(s_i+s_j)>0. For two trees, the exact denominator is R1 R2 D1^2 D2^2 k^2. At k=6+z, z>=0, the three numerators have respectively 6,048 (star/star), 5,238 (star/path), and 4,536 (path/path) nonzero rational coefficients, all positive. The minimum nonzero coefficients are respectively 192, 144, and 144. Each has positive coefficients at z^0 and z^2. tree44_checks.json records explicit strict witnesses and their margins. Thus T*>0 for every pair of positive-flux trees, including infinity; no uniform positive margin is asserted as the trees disconnect toward equality.

PROVED (algebra44.py; boundary44.py; symbolic44.py): a rank-at-most-two four-part is

    C4=H4-g VV^T/R,   R=V^T V,
    V=(3x+2y+z,-x+2y+z,-x-2y+z,-x-2y-3z),
    x,y,z>=0, R>0, 0<=g<=R/(4p), p=-V1 V4>0.

PROVED (same scripts; inherited separate concavity): the scale g reduces to 0 and R/(4p). At the latter endpoint, C4=H4-VV^T/(4p); cancelling R before expansion keeps the certificate small. K, with columns indexed j=2,3, has K1j=V4-Vj, Kjj=V1-V4, K4j=Vj-V1 and spans {1,V}-perpendicular. K has full column rank whenever R>0, including tied ordered coordinates. At g=0, allowing V to vary covers every selected top direction.

PROVED (boundary44.py): after subtracting 1/100 from T*, clearing the positive denominators, and setting k=6+z, every rational coefficient matrix is PSD. Mixed tree/boundary coefficients are 2x2; boundary/boundary coefficients are 4x4 on the tensor product of the two K-coordinate spaces. Exact symmetric elimination handles zero pivots. No floating eigenvalue or solver is used.

| Pair | Scale endpoints | PSD coefficient matrices | T* margin |
|---|---:|---:|---:|
| PROVED (boundary44.py): star/boundary | 0; max | 810; 3,780 | 1/100 |
| PROVED (boundary44.py): path/boundary | 0; max | 702; 3,276 | 1/100 |
| PROVED (boundary44.py): boundary/boundary | 0/0; 0/max; max/max | 108; 504; 2,352 | 1/100 |

PROVED (symbolic44.py): for every one of the ten connected endpoint types, both the isolate numerator and maximal-lower-trace numerator agree identically with the direct eight-by-eight selected-projector construction. All twenty identities are checked as sparse rational polynomials in the gap/flux coordinates, selected-vector coordinates and padding. audit44.py independently checks the original centered, normalized matrix definition at rational fixtures, including a feasible lower edge.

## Padding and infinity

PROVED (padding44.py): every connected endpoint is hardest at k=6. Write its cleared matrix polynomial at k=6+z as A0+A1 z+A2 z^2. Up to its positive, k-independent denominator, the functional matrix at r=1/k is

    A2+(A1-12A2)r+(A0-6A1+36A2)r^2.

PROVED (same script): the negative derivative at r=0 and r=1/6 is respectively 12A2-A1 and A1-A0/3. Both have exactly PSD rational coefficient matrices for all ten endpoint types. The derivative is affine in r, so these endpoint checks prove monotonicity throughout 0<=r<=1/6, including infinity. The separate scale and top-domain concavity reductions then prove all isolate-only signs.

## Arbitrary lower components

PROVED (inherited17/lower_formula.py; lower44.py): let

    F_k(s)=2(tr C-tr C^2)+2(k+2)B/k-Y+X_k(M0+s/2,h).

PROVED (same scripts): T*>=F_k(s), since the omitted lower spectral term is 2 sum mu(1-mu)>=0. Nontrivial lowers require N>=10, k>=8. Their trace satisfies 0<=s<=S=k-7. The exact identity is

    F_k(s)=(1-s/S)F_k(0)+(s/S)F_k(S)+s(S-s)/k.

PROVED (lower44.py; Schur product argument in inherited17/RESULT.md): put S_i=H4-C_i, tau=sum tr S_i, d=sum_i P_ii(S_1 direct-sum S_2)_ii. Then

    M0=(6-tau)/2, 0<=tau<=4,
    h=3/2-d, 0<=B<=d<=1/2.

PROVED (same scripts): the last inequalities follow from h>=1 and (H4-S_i) Hadamard-product S_i=diag(diag S_i)-S_i/4-S_i Hadamard-product S_i PSD. The selected top directions annihilate S_i and 1.

PROVED (lower44.py): for every such top pair, every real k>=8, and the corresponding infinity endpoint,

    F_k(S)-F_6(0)
     >= (4/k-2/3)d
        +X_k((k-1-tau)/2,3/2-d)
        -X_6((6-tau)/2,3/2-d)
     >= 3/10.

PROVED (same script): multiply the final difference by 144k^2 and set k=8+z. It is affine in d. At d=0,1/2, use degree-two Bernstein controls on tau in [0,2] and [2,4]. All twelve controls have strictly positive rational coefficients in z, including their z^2 coefficients. lower44_controls.json records them. This comparison applies to the entire top domain and preserves the step-one margin in full.

PROVED (same scripts plus the isolate theorem above): consequently

    T* >= (3s)/(10(k-7)) + s(k-7-s)/k > 0 if s>0.

PROVED (tree44.py): the three tree/tree maximal-trace endpoints also have direct positive-coefficient certificates (6,075, 5,265, and 4,563 terms). They independently check the endpoint signs without the comparison argument.

PROVED (inherited17/lower_formula.py): for any fixed lower collection, the infinity increment over replacing it by isolates at the same N is 2(tr D-tr D^2)+s, strictly positive for s>0. Infinity equality refers to padding a fixed graph; no classification of limits with growing lower mass is asserted.

## Equality and symmetric checks

PROVED (tree44.py; boundary44.py; inherited17 equality theorem; the fixed-vector concavity reductions): all connected endpoint pairs are strict. At any equality, every extreme pair used by separate concavity must itself be an equality. The inherited disconnected theorem forces one selected edge in each four-part, all other vertices isolated. With u,v fixed, these selected edges are unique; convex mixtures do not introduce another equality. Thus the full selected-projector closure has exactly two equal edges and isolates as its equality set. Positive lower trace is always strict.

PROVED (symmetric44.py; independently the original matrix definition): two balanced squares, each with edge weight 1/4 before mass normalization, have M0=2 and

    T*=(5k-14)/(2k),   T*_8=4/3,   T*_infinity=5/2,
    T_8=1/3,          T_infinity=5/8.

PROVED (same script): hence the balanced square pair is not an equality or near-zero symmetric fixture. Two balanced stars have T*_8=5/9 and T*_infinity=7/8. The two balanced K4 selected-projector closure has T*_8=4/9 and T*_infinity=4. Two equal edges have T*=T=0 identically. symmetric44_checks.json also records their normalized margins. Extra top multiplicity in the K4 fixture belongs only to the selected-projector closure; no actual-D>2 theorem is claimed.

## Split 3+5 setup

PROVED (setup35.py; inherited17/inherited16/concavity_certificate.py; inherited17/inherited16/split34_reduction.py): split 3+5 starts at k=6. The triangle reduces to its balanced corner or positive-flux three-path corner. With its selected vector fixed, the five-part reduces through the unchanged K_u concavity certificate. Exact matrix fixtures check the five-part quadratic variation, and the triangle-gap quadratic coefficient is checked independently of all other-block moments. Fixed lower trace leaves both concavity arguments unchanged.

PROVED (same scripts; inherited extreme inventory): the remaining connected five-part families are the three trees, rank-at-most-two A5, and rank-three A5 (twelve support candidates). Disconnected five-parts or triangle corners reduce to inherited 2+5 or 3+4 classes with arbitrary lowers. Nontrivial lowers have the same trace cap S=k-7, k>=8.

OPEN: for 3+5, both triangle corners paired with each of those connected five-part families still require sign certificates, as do their maximal-trace lower endpoints. This file claims a setup, not a new 3+5 theorem.

## Scope and replay

PROVED (replay_all.py; the inherited STRAT15 black-box premise stated in inherited17/RESULT.md): among disconnected D=2 graphs with components of at most five vertices, split 2+2, 2+3, 2+4, 2+5, 3+3, 3+4 and now 4+4 allow arbitrary lower components. Triangle, four-vertex and five-vertex double carriers also allow arbitrary lowers. General S5=0 cases remain inherited.

OPEN: the full disconnected D=2 statement with components of at most five vertices still requires split 3+5, 4+5 and 5+5, with isolates or lower components, outside already-covered S5=0 subcases.

PROVED (replay_all.py; source_hashes.json): replay uses only this folder and installed Python libraries. Every reused input is a byte-identical local copy pinned by SHA-256. The inherited seventeen STRAT16 stages and seven STRAT17 stages are replayed in a temporary local copy so their generated receipts do not change the pinned inputs. STRAT15's full cover is an inherited theorem premise; it is not rerun here. replay_summary.json hashes every proof input, this result, and the generated certificate receipts.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

NUMERICAL: elapsed time and peak memory are recorded in replay_summary.json after replay. Computation is sequential with one compute child at a time, one thread per numerical library, an 850 MB child watchdog and a 200 MB parent watchdog. No solver, process pool, subagent, network access or external-state mutation is required. Source folders STRAT17, STRAT16 and STRAT15 remain read-only. The parent holds the workspace coordination claim.

Task: “STRAT18: T104 split 4+4 (two connected four-vertex top carriers), with isolates and then with arbitrary lower components, every N >= 8; then split 3+5 if time remains” — received 2026-11-13 16:34 +04.
