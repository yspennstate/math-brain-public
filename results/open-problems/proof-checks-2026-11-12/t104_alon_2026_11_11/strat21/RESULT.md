# STRAT21: split 5+5

PROVED (replay_all.py, requiring every stage PASS): split 5+5 satisfies T>=0 for every integer N>=10, with isolates or arbitrary lower components, and under padding of any fixed graph to N->infinity. Both connected top carriers give T>0. In the selected-projector closure equality is exactly two equal edges and isolates. Every positive lower trace is strict. Lower component sizes need not be bounded by five.

PROVED (the same replay, retaining the inherited STRAT15 full-cover theorem as a premise): this closes the disconnected D=2 statement with all components of at most five vertices. OPEN: T104 in general, including actual top multiplicity D>2 outside the selected-projector closure and top carriers with six or more vertices.

## Functional, domain and inherited reduction

PROVED (inherited20/setup55.py; inherited20/audit45.py; audit55.py): normalize the common top eigenvalue to one, write C=C5 direct-sum C5 and P=uu^T direct-sum vv^T for unit zero-sum selected top vectors. With k=N-2, M0=tr C/2, put

    h=sum_i P_ii C_ii,
    B=sum_ij P_ij (I-C)_ij^2,
    Y=-2 sum_(i<j) C_ij (P_ii+P_jj-2P_ij)
                           (2-C_ii-C_jj+2C_ij),
    X_k(m,h)=(m-1)/k^2 [2(k+1)(k-2)-4km+2(k+2)h].

PROVED (inherited20/inherited19/inherited18/inherited17/lower_formula.py; audit55.py): for lower blocks D of trace s and M=M0+s/2,

    T*=2(tr C-tr C^2)+2(tr D-tr D^2)+2(k+2)B/k-Y+X_k(M,h),
    T=T*/M^2.

PROVED (inherited20/setup55.py and the inherited concavity, moment and extreme-classification scripts replayed by replay_all.py): separate K_u concavity holds, also at fixed lower trace. Each five-side has the six endpoint choices star5, path5, fork5, R5(0), R5(max), and Z5. R5 denotes rank<=2 A5 at the two scale endpoints. Z5 denotes the rank-three zero-edge scale endpoint covering all twelve support candidates. Disconnected endpoints reduce to the proved 4+5 and smaller classes with arbitrary lowers. The moment bounds are

    M0=(8-tau)/2, 0<=tau<=6,
    h=8/5-d, 0<=B<=d<=3/5.

PROVED (the same inherited moment scripts): on either side 0<=B_i<=d_i<=3/10; rank(A_i)<=3 implies tau_i<=2 and tr C_i>=2. The general five-side has tau_i<=3 and tr C_i>=1. The first isolate k is 8, and nontrivial lowers first occur at k=10, with trace cap k-9. Cross-block projector terms do not contribute; general selections reduce by linearity to split selections.

## Transfers and all endpoint families

PROVED (transfer55.py; symbolic55.py; rank3_pair55.py): retain the second five-part with moments (tau5,d5,B5), compare to the proved edge+five theorem at k=5, and define

    Delta=2(tr C1-tr C1^2)+(5/2)B1-Y1-(3/10)d5
       +X_8((tr C1+4-tau5)/2,h1+4/5-d5)
       -X_5((5-tau5)/2,13/10-d5).

PROVED (those scripts): new functional minus old functional equals Delta+(3/10)(d5-B5). This cancels every retained-side trace-square and Y term exactly. For R5(0) and R5(max) against any five-part, Delta>=1/100 using tau5<=3. For each of the three five-trees against any rank<=3 five-part, Delta>=1/100 using tau5<=2. Affine d5 dependence is evaluated at 0 and 3/10; the three degree-two Bernstein controls in tau5/tau_max have rational PSD coefficient matrices in four nonnegative gaps or four positive tree fluxes. Exact symmetric elimination checks every matrix, including zero pivots. The full moment matrices and Bernstein reconstructions are independently audited in symbolic55.py.

PROVED (inherited20/inherited19/inherited18/inherited17/inherited16/verify_sos.py and the inherited rank-two and padding certificates): the retained rank<=3 edge+five theorem has margin >=1/400000. Hence each tree/rank<=3 transferred pair has T*>=4001/400000 at k=8. Each pair with an R5 endpoint has T*>=1/100 at k=8. Intermediate scales follow from separate concavity.

PROVED (rank3_certificate55.py; rank3_target55.py; rank3_sos55.json): a stronger tied-edge/single-five bound at a rank-three zero-edge endpoint is

    F25(C5,u; k=5) >= 1/5.

PROVED (those scripts and the inherited canonical chart audit): in the inherited six-variable zero-edge Gram chart S=R/T, T=5t, the certified four-by-four target on 1-perpendicular is

    2 T^2 [ F25 operator +4S -(1/5)I ].

PROVED (rank3_certificate55.py): this target is a matrix SOS with one free matrix block of dimension 52, nine edge-constraint matrix blocks of dimension 28, and six scalar box blocks of dimension 7. Every Gram entry is an integer over 80,000,000,000. Each Gram equals an integer-factor product plus a strictly diagonally dominant positive residual. All polynomial coefficients and all integer residual inequalities replay exactly. Since Su=0, the added 4S term vanishes on the selected vector. The inherited chart bounds and nonnegative edge constraints are replayed, so this covers all twelve support candidates and their feasible limits. audit55.py independently checks the target against the original centered functional on two rational rank-three fixtures.

PROVED (rank3_pair55.py): for two Z5 sides, let p=tau1, q=tau2 and d=d1,e=d2. The new functional equals the sum of the two tied-edge/single-five k=5 functionals, plus f and (3/10)(d+e-B1-B2), where

    4000 f = -495dp+625dq-1590d+625ep-495eq-1590e
              +300p^2-1000pq+561p+300q^2+561q+234.

PROVED (rank3_pair55.py): for 0<=p,q<=2, f decreases in d,e, so its minimum uses d=e=3/10. At that corner,

    4000(f+9/50)=300(p-q)^2+200(p+q)
                  +400[p(1-q/2)+q(1-p/2)] >=0.

PROVED (rank3_certificate55.py; rank3_pair55.py): the last pair therefore has T*>=2/5-9/50=11/50 at k=8.

PROVED (the named scripts): all 36 ordered / 21 unordered connected endpoint-pair types are covered by this symmetric table.

| Side | star5 | path5 | fork5 | R5(0) | R5(max) | Z5 |
|---|---|---|---|---|---|---|
| PROVED: star5 | tree55.py | tree55.py | tree55.py | transfer55.py | transfer55.py | transfer55.py |
| PROVED: path5 | tree55.py | tree55.py | tree55.py | transfer55.py | transfer55.py | transfer55.py |
| PROVED: fork5 | tree55.py | tree55.py | tree55.py | transfer55.py | transfer55.py | transfer55.py |
| PROVED: R5(0) | transfer55.py | transfer55.py | transfer55.py | transfer55.py | transfer55.py | transfer55.py |
| PROVED: R5(max) | transfer55.py | transfer55.py | transfer55.py | transfer55.py | transfer55.py | transfer55.py |
| PROVED: Z5 | transfer55.py | transfer55.py | transfer55.py | transfer55.py | transfer55.py | rank3_pair55.py |

## Trees, padding and infinity

PROVED (algebra55.py; tree55.py; symbolic55.py): all six unordered positive-flux tree pairs have positive rational coefficient numerators in eight fluxes and z=k-8>=0, after multiplication by the positive denominator R1 R2 D1^2 D2^2 k^2. The inherited complete chart is U_i=sign_i sum_(incident e)x_e and w_ij=x_ij/(s_i+s_j). The sparse numerator is audited by exact local five-by-five contractions and the universal ten-by-ten direct-sum moment and denominator identities, without expanding terms that cancel between blocks.

| Pair | Terms | Smallest nonzero coefficient |
|---|---:|---:|
| PROVED (tree55.py): star/star | 245340 | 192 |
| PROVED (tree55.py): star/path | 174126 | 144 |
| PROVED (tree55.py): star/fork | 201582 | 144 |
| PROVED (tree55.py): path/path | 123579 | 144 |
| PROVED (tree55.py): path/fork | 143067 | 144 |
| PROVED (tree55.py): fork/fork | 165627 | 144 |

PROVED (tree55.py): positive witnesses at z^0 and z^2 give strict positivity at finite k and infinity. These coefficient margins are not uniform bounds on T*: trees can approach the two-edge equality boundary. Writing a numerator A0+A1 z+A2 z^2 and r=1/k gives

    numerator/k^2=A2+(A1-16A2)r+(A0-8A1+64A2)r^2.

PROVED (tree55.py): 16A2-A1 and A1-A0/4 have nonnegative rational flux coefficients. These are the negatives of the inverse-padding derivative at r=0 and r=1/8. The derivative is affine, hence k=8 is hardest.

PROVED (lower55.py): all transferred endpoint pairs satisfy M>=3/2. Using 1<=h<=8/5 and 0<=B<=d<=3/5, for 0<=r<=1/8 their inverse-padding derivative is at most

    4d+(M-1)(-3-4M+3h)
      =-21/10+(5/2)d-4a^2-a(31/5+3d) <=-3/5,
    M=3/2+a.

PROVED (tree55.py; transfer55.py; rank3_pair55.py; lower55.py; inherited concavity): all endpoint signs extend to every real k>=8 and fixed-graph infinity, with k=8 hardest. Concavity gives the isolate theorem for every integer N>=10. Endpoint padding is all that is required; no padding assertion for every interior selection is needed.

## Arbitrary lower components

PROVED (lower55.py; inherited20/setup55.py and lower_formula.py): omit the nonnegative 2 tr(D-D^2) term and call the resulting functional F_k(s). On r=N-10 lower vertices a nontrivial component uses at least one zero eigenvalue, so

    0<=s<=S=r-1=k-9,
    F_k(s)=(1-s/S)F_k(0)+(s/S)F_k(S)+s(S-s)/k.

PROVED (lower55.py): uniformly over the full five/five moment box, without using any isolate margin,

    F_k(k-9)-F_8(0)
      >=(4/k-1/2)d+X_k((k-1-tau)/2,8/5-d)
                       -X_8((8-tau)/2,8/5-d) >=1/4,
    k>=10.

PROVED (lower55.py): multiply the last difference minus 1/4 by 320k^2 and set k=10+z. At d=0,3/5 and on tau intervals [0,2], [2,4], [4,6], all eighteen reconstructed degree-two Bernstein controls have strictly positive rational z coefficients. The least coefficient is 144; lower55_controls.json records every control. The coefficient of B in the comparison is negative, so B<=d gives the stated lower bound.

PROVED (lower55.py and the isolate theorem): interpolation yields

    T* >= s/[4(k-9)] + s(k-9-s)/k >0 for s>0.

PROVED (lower55.py): at fixed lower collection, the infinity increment over replacing it by isolates is 2 tr(D-D^2)+s>0. The equality statement at infinity concerns fixed-graph padding. No equality classification is asserted for graph sequences with growing lower mass; normalized T may tend to zero as total mass grows.

## Equality and exact fixtures

PROVED (replay_all.py; tree55.py; transfer55.py; rank3_certificate55.py; rank3_pair55.py; lower55.py and inherited equality reductions): every connected endpoint pair is strict. Equality in the concave reduction can use only zero extreme pairs. The disconnected reductions force one selected edge in each side, all remaining vertices isolated. For fixed selected vectors each such edge is unique, so their convex combinations add no equality cases. Thus the selected-projector closure has precisely two equal edges and isolates as its zero set; positive lower trace is strict.

PROVED (symmetric55.py, checked independently against the original centered definition): K5+K5 has

    M0=4,
    T*=6(5k^2-37k+6)/(5k^2),
    T*_N10=9/16, T*_infinity=6,
    T_N10=9/256, T_infinity=3/8,
    F_k(k-9)=2(k-3)(4k+3)/(5k^2),
    F_10(1)=301/250, F_infinity=8/5.

PROVED (symmetric55.py): a lower edge with eigenvalue one realizes the first maximal endpoint at N=12 in the selected-projector closure, with normalized T=602/10125. Formal trace-maximal endpoints are limits if all lower eigenvalues must be strictly below one. Their nonnegative replay proves all feasible strict-lower cases.

| Equal-flux pair | T* at N=10 | T* at infinity | F_max at N=12 |
|---|---:|---:|---:|
| PROVED (symmetric55.py): star/star | 63/80 | 138/125 | 8449/6250 |
| PROVED (symmetric55.py): star/path | 229/160 | 70013/31500 | 1516211/787500 |
| PROVED (symmetric55.py): star/fork | 146321/115200 | 44863/24000 | 21427/12000 |
| PROVED (symmetric55.py): path/path | 40/21 | 421/126 | 1241/525 |
| PROVED (symmetric55.py): path/fork | 103991/57600 | 301183/100800 | 954671/420000 |
| PROVED (symmetric55.py): fork/fork | 16163/9600 | 6323/2400 | 194803/90000 |

PROVED (symmetric55.py): equal-flux means all eight chart fluxes equal one, which gives rational edge weights. The receipt records full formulas and normalized isolate margins. Two equal edges have T*=T=0 identically with isolates. Clique fixtures have extra top multiplicity and use only the retained rank-two projector; they make no actual-D>2 claim.

## Replay, resource record and remaining scope

PROVED (replay_all.py; source_hashes.json): reused proof inputs are byte-identical local copies with recorded SHA-256. Replay reads no external proof files. It runs the 46 inherited exact stages in a temporary local copy, then the new exact stages, including all coefficient, integer SOS, universal polynomial, original-definition and fixture audits. The inherited STRAT15 full-cover theorem remains a premise and is not rerun. replay_summary.json hashes all proof inputs, this result and generated receipts. No solver or numerical package is required by exact replay beyond installed SymPy.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

NUMERICAL: replay_summary.json records wall time and peak RSS with an aggregate upper bound. Exact replay uses one compute child at a time, one library thread, an 850 MB child guard and a 200 MB root guard. Sparse SOS discovery used one solver process, with a measured 564,690,944-byte peak after an initial larger ansatz was stopped by its memory guard. Discovery is excluded from proof replay. Workspace artifacts remain below 500 MB. The parent holds the coordination claim. No subagents or edits to source workspaces were used.

PROVED (replay_all.py, with the stated inherited theorem premise): all disconnected D=2 split classes with top carriers of size at most five, and the inherited double-carrier classes on at most five vertices, now permit arbitrary lower components. Consequently the disconnected D=2 statement for components of at most five vertices has no remaining open class. OPEN: T104 beyond that statement, including actual D>2 outside the selected-projector closure and six-or-more-vertex top carriers. No general T104 theorem is claimed.

Task: “STRAT21: T104 split 5+5 (two connected five-vertex carriers), with isolates and then with arbitrary lower components, every N >= 10” — started 2026-11-13 20:39 +04.
