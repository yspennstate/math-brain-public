# STRAT20: split 4+5

PROVED (replay_all.py, requiring all 46 stages PASS): split 4+5 satisfies T>=0 for every integer N>=9, with isolates or arbitrary lower components, and for a fixed graph padded to N->infinity. Two connected top carriers give T>0. In the selected-projector closure equality is exactly two equal edges and isolates. Every positive lower trace is strict. Lower component sizes need not be bounded by five.

PROVED (setup55.py): split 5+5 is set up below. OPEN: its connected endpoint signs outside inherited special cases. No complete disconnected D=2 theorem is claimed.

## Functional and inherited reductions

PROVED (inherited19/setup45.py; inherited19/inherited18/inherited17/lower_formula.py; symbolic45.py; audit45.py): normalize the common top eigenvalue to one, use C=C4 direct-sum C5 and the selected projector P=uu^T direct-sum vv^T, with unit zero-sum top vectors. Put k=N-2, M0=tr C/2, and

    h=sum_i P_ii C_ii,
    B=sum_ij P_ij (I-C)_ij^2,
    Y=-2 sum_(i<j) C_ij (P_ii+P_jj-2P_ij)
                         (2-C_ii-C_jj+2C_ij),
    X_k(m,h)=(m-1)/k^2 [2(k+1)(k-2)-4km+2(k+2)h].

PROVED (same scripts): for lower blocks D with s=tr D and M=M0+s/2,

    T*=2(tr C-tr C^2)+2(tr D-tr D^2)+2(k+2)B/k-Y+X_k(M,h),
    T=T*/M^2.

PROVED (inherited19/setup45.py and inherited four/five-part concavity and extreme certificates, all replayed by replay_all.py): the functional is separately concave on K_u x K_v, including fixed lower trace. The four-side connected endpoints are star4, path4 and rank<=2 A4 at scale zero or maximum. The five-side endpoints are star5, path5, fork5, rank<=2 A5 at scale zero or maximum, and the rank-three zero-edge scale endpoint covering all twelve support candidates. Disconnected endpoints reduce to the proved 3+5, 4+4 and smaller split classes with arbitrary lowers. Cross-block selected-projector entries do not contribute, and selections split by linearity.

PROVED (inherited19/setup45.py and moment arguments in inherited19/RESULT.md, audited by audit45.py): writing S_i=H_i-C_i and d_i=sum u_i^2(S_i)_ii gives

    M0=(7-tau)/2, 0<=tau<=5,
    h=31/20-d, 0<=B<=d<=11/20.

PROVED (same inherited moment argument): each selected diagonal moment is at least 1/2; the Schur product (H_i-S_i) o S_i is PSD and gives B_i<=d_i. Thus 0<=B5<=d5<=3/10, 0<=tau5<=3 for every five-part, and tau5<=2 when rank(A5)<=3. These bounds use no numerical spectra.

## All 24 connected endpoint families

PROVED (transfer45.py; symbolic45.py; inherited 2+5 certificates): use the complete edge+five-part theorem at k=5 as the reference. The failed draft comparison with a balanced three-part is not used. Keeping the five-part and its selection fixed, the lower increment at k=7 is

    Delta = 2(tr C4-tr C4^2)+(18/7)B4-Y4-(8/35)d5
      +X_7((tr C4+4-tau5)/2,h4+4/5-d5)
      -X_5((5-tau5)/2,13/10-d5).

PROVED (symbolic45.py): new functional minus old functional equals Delta+(8/35)(d5-B5). This identity cancels the five-part trace-square and Y terms exactly.

PROVED (transfer45.py): Delta>=1/100 for both four-rank scale endpoints and every five-part, and for either four-tree paired with every rank<=3 five-part. For the former use 0<=tau5<=3; for the latter use 0<=tau5<=2. Evaluate the affine d5 dependence at 0 and 3/10 and use degree-two Bernstein controls in tau5 divided by its upper bound. Every control is a matrix polynomial in the three nonnegative four-side gaps, or three positive four-tree fluxes, with rational PSD coefficient matrices. Exact symmetric elimination checks every matrix, including singular pivots. symbolic45.py reconstructs the Bernstein matrices exactly and independently audits their moment formula. transfer45_checks.json records counts, endpoints and the margin.

PROVED (same scripts and inherited concavity): the following table covers every ordered connected endpoint type. R4(0),R4(max) mean the two rank<=2 A4 scale endpoints; R5(0),R5(max) mean the analogous A5 endpoints; Z5 means the rank-three zero-edge endpoint.

| Four-side | star5 | path5 | fork5 | R5(0) | R5(max) | Z5 |
|---|---|---|---|---|---|---|
| PROVED: star4 | tree45.py | tree45.py | tree45.py | transfer45.py | transfer45.py | transfer45.py |
| PROVED: path4 | tree45.py | tree45.py | tree45.py | transfer45.py | transfer45.py | transfer45.py |
| PROVED: R4(0) | transfer45.py | transfer45.py | transfer45.py | transfer45.py | transfer45.py | transfer45.py |
| PROVED: R4(max) | transfer45.py | transfer45.py | transfer45.py | transfer45.py | transfer45.py | transfer45.py |

PROVED (inherited19/inherited18/inherited17/inherited16/verify_sos.py, verify_rank_three_algebra.py and padding_monotonicity.py, replayed by replay_all.py): the inherited rank<=3 five-part edge+five theorem has margin at least 1/400000. Hence the six four-tree/rank<=3-five endpoint families have T*>=4001/400000 at k=7. The twelve four-rank families have T*>=1/100 at k=7, using nonnegativity of the full inherited 2+5 theorem. Intermediate scales follow from separate concavity.

PROVED (algebra45.py; tree45.py; symbolic45.py): all six positive-flux tree pairs have positive-coefficient isolate numerators in the seven fluxes and z=k-7>=0, after clearing the positive denominator R4 R5 D4^2 D5^2 k^2. Here U_i=sign_i sum_(e incident i)x_e and w_ij=x_ij/(s_i+s_j) is the inherited complete tree chart. The direct 9-by-9 selected-projector polynomial agrees identically with each numerator.

| Four-tree | Five-tree | Terms | Smallest nonzero coefficient |
|---|---|---:|---:|
| PROVED (tree45.py): star | star | 38574 | 192 |
| PROVED (tree45.py): star | path | 27369 | 144 |
| PROVED (tree45.py): star | fork | 31689 | 144 |
| PROVED (tree45.py): path | star | 33426 | 144 |
| PROVED (tree45.py): path | path | 23715 | 144 |
| PROVED (tree45.py): path | fork | 27459 | 144 |

PROVED (tree45.py): each polynomial has positive witnesses at z^0 and z^2, recorded in tree45_checks.json. Thus every positive-flux tree pair is strict, including infinity. These coefficient margins are not uniform bounds on T*: trees may approach the two-edge equality boundary.

## Padding and infinity

PROVED (tree45.py): write a tree numerator as A0+A1 z+A2 z^2, z=k-7. Its quotient by k^2 is

    A2+(A1-14A2)r+(A0-7A1+49A2)r^2, r=1/k.

PROVED (same script): the negatives of its inverse-padding derivatives at r=0,1/7 are 14A2-A1 and A1-2A0/7. Both have nonnegative rational flux coefficients. The derivative is affine, so k=7 is hardest for all six tree pairs, including infinity.

PROVED (lower45.py): on the transferred endpoint domain M>=3/2. Indeed rank(A4)<=2 implies tr C4>=2, or rank(A5)<=3 implies tr C5>=2; the other selected carrier has trace at least one. With 1<=h<=31/20 and B<=d<=11/20, the inverse-padding derivative

    4B+(M-1)(-2-4M+2h)+8r(M-1)(h-1)

PROVED (same script): for 0<=r<=1/7 is at most

    4d+(M-1)(-22/7-4M+(22/7)h)
      =-299/140+(17/7)d-4a^2-a(439/70+(22/7)d) <= -4/5,
    M=3/2+a.

PROVED (the preceding certificates plus inherited concavity): every connected endpoint sign therefore holds for every k>=7 and infinity, with k=7 hardest. Only endpoint padding monotonicity is asserted or needed for the sign reduction.

## Arbitrary lower components

PROVED (lower45.py; inherited trace formula): define F_k(s) by omitting the nonnegative lower term 2 tr(D-D^2) from T*. Nontrivial lowers first occur at N=11, k=9. On r=N-9 lower vertices, a nontrivial component has at least one zero eigenvalue, so

    0<=s<=S=r-1=k-8,
    F_k(s)=(1-s/S)F_k(0)+(s/S)F_k(S)+s(S-s)/k.

PROVED (lower45.py): uniformly over the entire four/five top domain, without spending any isolate margin,

    F_k(k-8)-F_7(0)
      >= (4/k-4/7)d
        +X_k((k-1-tau)/2,31/20-d)
        -X_7((7-tau)/2,31/20-d) >= 1/4.

PROVED (same script): multiply the last difference minus 1/4 by 980k^2, set k=9+z and take d=0,11/20. On each tau interval [0,2], [2,4], [4,5], all three degree-two Bernstein controls have strictly positive rational coefficients in z. All eighteen controls and their exact reconstruction are recorded in lower45_controls.json. The coefficient of B is negative, so B<=d gives the indicated lower bound.

PROVED (lower45.py and the isolate theorem): interpolation gives

    T* >= s/(4(k-8))+s(k-8-s)/k > 0 for s>0.

PROVED (same script): at fixed lower collection the infinity increment over replacing it by isolates is 2 tr(D-D^2)+s>0. The fixed-graph infinity equality statement concerns padding by isolates; no equality classification for limits with growing lower mass is asserted.

## Equality and exact fixtures

PROVED (tree45.py; transfer45.py; lower45.py; inherited equality reductions, replay_all.py): every connected endpoint pair is strict. A zero in the concave reduction must use only zero extreme pairs. The disconnected reductions force one selected edge in each part and all other vertices isolated. For fixed selected vectors these edges are unique, so convex combinations yield no further zeros. This proves exactly the two-equal-edges equality set in the selected-projector closure; positive lower trace is strict. Extra top multiplicity in endpoint fixtures uses only the retained projector; no actual-D>2 theorem is claimed.

PROVED (symmetric45.py, independently checked by the original centered matrix definition): K4+K5 has

    M0=7/2,
    T*=(20k^2-129k+22)/(4k^2),
    T*_N9=99/196, T*_infinity=5,
    T_N9=99/2401, T_infinity=20/49,
    F_k(k-8)=(k-3)(31k+22)/(20k^2),
    F_9(1)=301/270, F_infinity=31/20.

PROVED (same script): a lower edge of eigenvalue one realizes the formal maximal endpoint at N=11 in the selected-projector closure, with normalized T=301/4320. This first maximal-trace clique check is positive.

| Equal-flux pair | T* at N=9 | T* at infinity | F_max at N=11 |
|---|---:|---:|---:|
| PROVED (symmetric45.py): star4 + star5 | 8237/12250 | 1979/2000 | 4064/3375 |
| PROVED (symmetric45.py): star4 + path5 | 31229/24696 | 2125/1008 | 70607/40824 |
| PROVED (symmetric45.py): star4 + fork5 | 7561/6720 | 8423/4800 | 375361/233280 |
| PROVED (symmetric45.py): path4 + star5 | 215531/220500 | 1139/750 | 536797/364500 |
| PROVED (symmetric45.py): path4 + path5 | 5069/3430 | 3323/1260 | 2342/1215 |
| PROVED (symmetric45.py): path4 + fork5 | 322631/235200 | 10963/4800 | 79171/43200 |

PROVED (same script): equal-flux means all edge fluxes equal one in the stated tree chart; these determine rational edge weights. symmetric45_checks.json records the full formulas, normalized margins and infinity maximal-trace values. Two equal edges have T*=T=0 identically with isolates.

## Split 5+5 setup and remaining scope

PROVED (setup55.py and inherited five-part concavity): separate K_u concavity transfers unchanged, including fixed lower trace. Its first k is 8 (N=10); nontrivial lowers first occur at k=10 (N=12), with cap S=k-9. Its moment bounds are

    M0=(8-tau)/2, 0<=tau<=6,
    h=8/5-d, 0<=B<=d<=3/5.

PROVED (setup55.py; inherited extreme inventory): each side has the six endpoint choices star5, path5, fork5, rank<=2 A5 at scale zero or maximum, and the rank-three zero-edge endpoint covering twelve supports. setup55_checks.json lists all 36 ordered / 21 unordered endpoint-pair types, the exact lower interpolation and a positive K5+K5 fixture. Disconnected endpoints reduce to now-proved 4+5 and smaller classes, including arbitrary lowers.

OPEN: connected 5+5 endpoint signs, padding, equality and maximal-lower-trace signs outside inherited S5=0 subcases. No new complete 5+5 family theorem is asserted; the positive clique fixture alone does not close a family.

PROVED (replay_all.py, retaining STRAT15's full cover as an inherited theorem premise): disconnected D=2 graphs with top split classes 2+2, 2+3, 2+4, 2+5, 3+3, 3+4, 3+5, 4+4 and now 4+5 permit arbitrary lower components. Triangle, four-vertex and five-vertex double carriers also permit arbitrary lowers. The general inherited S5=0 cases remain covered.

OPEN: the full disconnected D=2 statement with all component sizes at most five requires only the remaining connected 5+5 class, with isolates and arbitrary lowers, outside inherited special cases. A counterexample was not found; all newly certified domains are nonnegative by exact replay.

## Replay and resource record

PROVED (replay_all.py; source_hashes.json): every reused proof input is a byte-identical local copy with a recorded SHA-256. Replay uses this folder and installed Python libraries, with no external proof reads. All 39 inherited stages and seven new stages replay exactly, including the 252-matrix concavity certificates, rank classification, rational SOS, padding and lower reductions. Inherited receipt generation runs in a temporary local copy. The inherited setup45 receipt says signs OPEN at its historical stage; the new certificates above close them. STRAT15's full-cover theorem remains an inherited premise and is not rerun here. replay_summary.json hashes all proof inputs, this result, and generated certificate receipts.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

NUMERICAL: replay_summary.json records elapsed time, parent peak RSS and largest-child peak RSS, whose sum bounds aggregate replay RSS. Replay uses one compute child at a time, one numerical-library thread, an 850 MB child guard and 200 MB parent guard. No solver or subagent is used. Workspace artifacts are under 500 MB. The parent holds the coordination claim; the read-only source directories are unchanged.

Task: “STRAT20: T104 split 4+5 (a connected four-vertex carrier and a connected five-vertex carrier), with isolates and then with arbitrary lower components, every N >= 9; then set up 5+5 if time remains” — received 2026-11-13 18:40 +04.
