# A075 stage 2 — sparse matching pattern closed in every dimension

## exact target, quantifiers, hypotheses and units

Following B15 v2, turn the six-bit witness into a Boolean family and decide analytically whether its selectable true erasure grows. For k,l>=0 let r=2k+l, let M be k disjoint coordinate pairs, and set

    A_(k,l)={0,e_1,...,e_r} union {e_i+e_j : {i,j} in M},
    f_(k,l)=1-2*1_A on the uniform physical r-cube.

There are l unmatched coordinates. Characters are (-1)^(x dot S), N=2^r, p(S)=fhat(S)^2, B_i=H(S_i|S_-i), d_i=Inf_i, and E(f)=min_(d_i>0) B_i/d_i. All entropy units are bits. Coordinate permutations, input reflections, output negation and dummy padding preserve the corresponding erasure ratios. General affine variable changes are not used.

The all-dimensional result is sharp, including physical descendants: every relevant coordinate of every member of the restriction closure of these matching functions satisfies

    B_i <= K6 d_i,
    K6=16/3-(21/8)log2(3)+(95/24)log2(5)
                 -(121/24)log2(11)+(65/24)log2(13)
       =2.9444953038718586... .                                  (1)

Equality occurs precisely at the six-variable, three-pair matching root (up to the stated symmetries/dummies), for all six coordinates. In particular the supremum of E and of B/I on this hereditary class is K6. Perfect matching roots f_(k,0) have E->2 and H/I->4. Thus this pattern is not an unbounded-ratio Boolean counterfamily. Separate root bounds show arbitrary graph-edge variants and padded monotone paths also have E<=2+o(1), uniformly as dimension grows. Those separate root estimates are not silently promoted to a hereditary tree theorem or full FEI.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 21:24 UTC, B15 STREAM_NOTES.md v2 (2026-10-11 23:25 UTC), own STATUS/LEARNED and the complete execution protocol/2 revision 2026-10-11-execution-v2. Read B15 lead CLAIMS.json, B15-LKSTAR-FAILS-N5-N6@1 and its composition calibration, A071 stage2 REPORT.md (exact five-bit maximum and 640 path extremizers), A072 stage2 REPORT.md (exact six-bit prime-log expression), A074 stage2 REPORT.md (independent finite witness reconstruction), and A089 stage2 REPORT.md (raw five-bit recursion bounded and continuity failure for newly relevant coordinates). A074's path was found by file inventory after one guessed directory was absent. No other agent's code was executed or imported.

Prior-stage protocol/paper/source consultation is retained. The threshold and percolation class theorems are context, not premises. This stage uses the exact six-bit witness and the newly classified five-bit path geometry rather than repeating any all-function census. All source bytes/hashes and consultation scopes are saved in out/SOURCE_RECEIPTS.json. Source identities C005/ERASURE_REDUCTION are re-derived where used. Novelty is not claimed. This is the lead-directed closure of an existing witness mechanism; it introduces no broad universal candidate despite the pending-claim cap.

## complete derivation or exact first unsupported line

### Spectrum, physical influence and exact erasure formula

Put a=|A|=1+3k+l. On a Fourier index S, let u be the number of matched pairs intersecting S and v the number of isolated coordinates in S. For one pair the indicator character sum contribution is t_i+t_j+t_i*t_j, where t_i=(-1)^(1_(i in S)): it is 3 when neither coordinate occurs and -1 otherwise. Each isolated coordinate contributes 1 or -1. Therefore

    L_(u,v)=a-4u-2v,
    multiplicity C(k,u)3^u C(l,v),
    fhat(empty)=1-2a/N, fhat(S)=-2 L_(u,v)/N for S!=empty.       (2)

The empty index is the one exceptional element of the (u,v)=(0,0) class. A paired physical direction has exactly two internal A-edges, 0--e_i and e_partner--(e_i+e_partner). An isolated direction has one internal edge. Thus the respective crossing-edge counts are a-4 and a-2. If t_i is 2 for paired and 1 for isolated directions, put delta_i=a-2t_i; then

    d_i=2 delta_i/N, fhat({i})=-2 delta_i/N.                   (3)

The second identity also follows from counting A points with bit i=1. Irrelevant directions are omitted; low-dimensional constant cases cause no division.

Write Phi(x,y)=(x+y)log2(x+y)-x log2(x)-y log2(y), using continuous zero conventions. Let G(x,y) denote the same expression on unnormalized masses. The paired-coordinate residual packets, with u counting the OTHER k-1 pairs and v counting the l isolated coordinates, have weight C(k-1,u)3^u C(l,v). They are

    (4L^2,4(L-4)^2), partner absent;
    (4(L-4)^2,4(L-4)^2), partner present,
    L=a-4u-2v.                                                (4)

For u=v=0 in the first packet replace 4L^2 by (N-2a)^2. The paired B_i is the weighted sum of G over (4), divided by N^2. For an isolated coordinate use u=0..k, v=0..l-1, weight C(k,u)3^u C(l-1,v), and packets (4L^2,4(L-2)^2), with the identical empty-packet replacement. These formulas are exact finite logarithmic sums in parameters; no large-dimensional truth table is required. Pair swaps/pair permutations and isolated-coordinate permutations prove there are at most two physical coordinate orbits.

### Actual restriction closure

If all fixed bits are zero, surviving intact pairs remain pairs, and a broken pair leaves its free member isolated. This gives another A_(k',l'). If exactly one fixed bit is one, belonging to coordinate j, the only negative residual points are 0 and possibly e_partner(j), provided that partner is free. This is a point defect with at most one dummy coordinate. If exactly two fixed ones form a matching pair, only the zero residual point is negative; otherwise the residual is constant +1. Three fixed ones also force +1. Full negative residual cubes in very small dimensions are constants -1. Further restrictions of a point defect are point defects or constants, with dummy coordinates unchanged. This proves the complete hereditary classification, for simultaneous assignments as well as one-step slices.

### All-dimensional cutoff and sharp certificate

For ANY Boolean sign with negative side size a, let q0=(1-2a/N)^2 and q_i=fhat({i})^2. Every erasure packet satisfies Phi(x,y)<=x+y. All packets except the empty remainder therefore contribute at most 1-q0-q_i. Moreover

    Phi(x,y)<=y log2(e(x+y)/y),

by x log2(1+y/x)<=y/ln2. Since q0+q_i<=1,

    B_i <= 1-q0-q_i+q_i log2(e/q_i).                         (5)

For (3), q_i=4delta_i^2/N^2. Using 1-q0<=4a/N, log2(e)<3/2, and dropping negative logarithms gives

    B_i/d_i <= 2a/delta_i+(2delta_i/N)(2r+3/2).

Here delta_i>=r-3 and delta_i<=a<=1+3r/2. Also 2a/delta_i=2+4t_i/delta_i<=2+8/(r-3). Consequently for r>3,

    B_i/d_i <= U(r)=2+8/(r-3)+(3r+2)(2r+3/2)/2^r.           (6)

At r=13, U=240651/81920<368/125<K6. It decreases thereafter. The rational term decreases directly. For P(r)=(3r+2)(2r+3/2),

    2P(r)-P(r+1)=6r^2-(7/2)r-23/2>0 for r>=13,

so P(r)/2^r decreases. The positivity follows already at 13 and from its positive derivative. No asymptotic extrapolation is needed to rule out equality in r>=13.

The finite remaining parameters 1<=r<=12 have only 48 nonzero-dimensional (k,l) pairs, at most two coordinate orbits per pair. Exact packets (4) and outward logarithm intervals certify every relevant orbit strictly below K6, except (k,l)=(3,0), whose exact rational prime-log form equals (1). There are six equality coordinate rows; the saved certificate verifies equality symbolically, not by overlapping intervals. Parameters r<=9 were reconciled against full signed truth tables, integer Walsh transforms, direct physical edges and all 350 single-coordinate children. The additional r=10,11,12 cutoff consists of only 19 compressed parameter pairs and 33 coordinate orbits. It closes a proved finite-to-infinite cutoff, not a census of arbitrary functions.

Point-defect descendants in s variables have d=2^(1-s),

    B_i/d = 2-2d+Phi((1-d)^2,d^2)/d
          <=2+d(2s-4+log2 e).                               (7)

For s=1 erasure is zero. For s=2 the rough bound is <11/4. For s>=3 the term 2^(1-s)(2s-5/2) is largest at s=3, so (7)<23/8<368/125. Dummy coordinates are irrelevant. This completes (1) on every physical descendant and proves sharpness globally within the stated class. This is an all-dimensional theorem supplied by exact finite certificates plus an analytic tail; the finite passing domain is never itself called universal.

It also gives a terminal-inclusive restriction payment. On ANY physical stopping tree starting in this class,

    sum_v w_v B_(i_v)(f_v) <= K6 [I(f)-E I(f_leaf)].

Indeed every descendant belongs to the classified closure and I telescopes by the ordinary physical influence identity. From Delta_i H=B_i+JS_i and JS_i<=(2/ln2)d_i,

    H(f)<=E H(f_leaf)+(K6+2/ln2)[I(f)-E I(f_leaf)].           (8)

This retains all terminal entropy and never reuses an ancestral coordinate's influence. Complete restriction trees have constant leaves, giving H<=(K6+2/ln2)I on the class. This is a scoped payment, not an improvement to an all-Boolean constant; the stronger point is the sharp erasure bottleneck and hereditary closure.

### Perfect matching limits, not a conjecture counterfamily

For l=0, r=2k, a=3k+1 and delta=a-4, every coordinate is interchangeable, so E=B_i/d_i. A scalar consequence of the C005 entropy bound is

    x^2+y^2-Phi(x^2,y^2) <= (|x|-|y|)^2/ln2.                (9)

To reconstruct it, set z=(x^2-y^2)/(x^2+y^2) and use

    ((1+z)ln(1+z)+(1-z)ln(1-z))/2 <= 1-sqrt(1-z^2).

Both sides vanish at zero; their derivatives obey atanh(z)<=z/sqrt(1-z^2) on [0,1], and evenness handles negative z. Substituting gives (9). In (4), partner-present packets have equal masses, while partner-absent amplitude differences have absolute value at most 8/N. There are N/4 such packets; omit the exceptional empty packet and sum the remaining deficits. Their total is at most 16/(N ln2). Therefore

    2a/delta-2(a^2+delta^2)/(delta N)-8/(delta ln2)
       <= E(f_(k,0))
       <= 2a/delta+(2delta/N)(2r+3/2).                       (10)

Both endpoints tend to 2. This proves E->2 and excludes divergence without relying on the frozen k=2..32 scan. The scan's maximum is at k=3, and (1) independently proves that maximum for all k.

For completeness let T=1-q0=4a/N(1-a/N). Every nonempty coefficient has integer numerator -2L, |L|<=a. Thus

    T(2r-2-2log2 a) <= H(f) <= T(2r-2+1/ln2),

where the empty entropy is nonnegative and <=T/ln2. Divide by I=2r delta/N. Since a/delta->1, a/N->0 and log(a)/r->0, both bounds tend to 4. Consequently H/I->4. The entropy-to-influence growth and local erasure behavior are different quantities: neither diverges here.

### Quarantine the adjacent sparse mechanisms

The same mass bound (5) rules out graph-edge extensions as a large-dimensional erasure mechanism. For any simple graph G on n physical coordinates, set A={0,all e_i,all edge pairs}. Then a=1+n+e, and a direction of degree d_i^G has singleton coefficient -2delta_i/N and influence 2delta_i/N, delta_i=a-2(1+d_i^G). Choose a minimum-degree vertex. Since d_min<=2e/n,

    delta>=a-2-4e/n>=a(1-4/n)>0 for n>4.

Hence, uniformly over ALL simple graphs,

    E(f_G)<=2+8/(n-4)+(n^2+n+2)(2n+3/2)/2^n.                (11)

This tends to 2 from above and is <368/125 already at n=16: its value there is 551825/196608. The polynomial tail decreases for n>=16 because 2Q(n)-Q(n+1)=2n^3-(5/2)n^2-(15/2)n-8>0 for Q(n)=(n^2+n+2)(2n+3/2). Thus no graph in any dimension >=16 beats the existing six-bit witness. Dimensions <=15 are bounded by elementary granularity (every relevant influence>=2^(1-n)) and B_i<=h2(d_i)<=d_i log2(e/d_i), yielding E<31/2. No exact small-graph extremizer beyond our frozen domain is claimed. Root graph estimates do not supply arbitrary descendant payment after missing singleton points or shifted support occur.

For the five-bit pattern, let P_(n,m) have negative side {0,e1,e1+e2,...,e1+...+e_m}, 0<=m<=n. Its size is a=m+1. Each active direction i<=m has one internal edge, so d_i=2(m-1)/N and singleton numerator -2c_i with c_i=2i-m-1. Every outside direction has d_i=2a/N and singleton numerator -2a. If m<n choose an outside direction. Equation (5) gives

    E(P_(n,m))<=2+2(n+1)(2n+3/2)/2^n.                       (12)

If m=n>=2 choose a middle active coordinate with |c_i|<=1. With q_i=0 or 4/N^2, (5) gives

    E(P_(n,n))<=2+4/(n-1)+2(2n+3/2)/((n-1)2^n).            (13)

Both bounds tend to 2 uniformly over path length/padding. For n>=10 their maximum is <368/125, with the two cutoff values 2521/1024 and 22571/9216. Monotonicity follows from the positive differences of the quadratic tails (for (12), 2P(n)-P(n+1)=4n^2-n-8) and the decreasing rational term in (13). The m=0 point-defect cases are included in (12); m=n=1 is constant. For n<=9, granularity gives E<19/2. Thus padded/long paths cannot give unbounded erasure either. The original f5 is a translated/permuted member with (n,m)=(5,2). Equations (11)-(13) are root upper bounds, not equality limits, and do not close universal selection.

### First unsupported line and changed mechanism

The sparse matching route is now resolved; its natural graph/path extensions also cannot grow E with dimension. The first unsupported universal line is a uniform payment for arbitrary Boolean descendants, including residual support geometry that is not polynomially sparse and biases produced by composition. Equations (1), (8), (11) and (13) cannot be substituted for that missing quantifier.

NEXT changes mechanism to the biased signed-collision admission ledger with the TRANSITIVE six-bit seed as outer gate and an arbitrary level-one-carrying inner core. Raw biased recursion of f6 is a calibration, not the universal target: fixed-gate read-once class results already explain why closing that recursion alone would be insufficient. A089 already closed raw f5 recursion by finding a cheap path through two coordinate types, so that mechanism is not repeated. The six-bit matching gate is transitive; identical disjoint recursion remains transitive on all leaves, leaving one coordinate orbit and preventing the same cheap-orbit selection escape. If p is the probability of a child output encoded as bit 1, its exact minority-output probability and one outer physical derivative probability are

    alpha(p)=(1-p)^4(1+4p-2p^2),
    q(p)=2p(1-p)^3(2-p).

These follow by counting zero, singleton and matching-pair inputs and the boundary patterns. They give only output bias/influence; the unsigned mean recursion cannot pay true erasure. The next mathematical action is to insert this gate in the unequal-mean signed-fiber collision ledger for an arbitrary inner Boolean g, retaining the changing empty row, inherited B_i(g), every newly relevant coordinate and full terminal H(g). The concrete open payment is a normalized collision reserve that is charged once to physical influence without assuming the inner FEI bound. Raw f6 profiles can falsify the proposed reserve but cannot prove its universal validity. No all-depth erasure/admission claim for this new mechanism is made here.

## executed validation with domain, arithmetic, commands and outputs

Every computation had a frozen specification saved before execution. FROZEN_SPEC.json fixes all r<=9 partial matchings (30 pairs including r=0), every physical coordinate and both children, point defects s=1..9, and compressed perfect matching roots k=2..32 (dimensions 4..64). Only truth tables through nine bits are enumerated; larger roots use O(r^2) packet classes. No symmetry is used for direct validation; the proved paired/isolated symmetry reduces compressed certificates.

TAIL_CUTOFF_SPEC.json adds r=10,11,12 after the analytic r>=13 cutoff was derived. Its exact count is 19 parameter pairs, 33 coordinate orbits. The initial count was mistakenly written 34; the first execution stopped on that bookkeeping assertion before saving a certificate, the spec/code count was corrected, and the unchanged domain was rerun. This is neither an entropy failure nor a hidden change of search range.

STRUCTURAL_EXTENSION_SPEC.json fixes all 1100 labelled graphs on n=0..5 and all 55 paths 0<=m<=n<=9 to validate (11)-(13). It is not a search for a graph maximum. No larger truth-table scan follows automatically.

Commands from A075, all Python UTF-8:

    python -X utf8 runs/20261013T212622Z-account05-A075-search-to-theorem-bridge/code/check_matching.py
    python -X utf8 runs/20261013T212622Z-account05-A075-search-to-theorem-bridge/code/certify_cutoff.py
    python -X utf8 runs/20261013T212622Z-account05-A075-search-to-theorem-bridge/code/check_structural.py
    python -X utf8 runs/20261013T212622Z-account05-A075-search-to-theorem-bridge/code/save_stage.py

The three successful mathematical outputs record respectively 9908, 350 and 21533 exact assertions, total 31791. Observed mathematical runtimes were 0.5981, 0.0288 and 0.8053 seconds. All 350 direct physical children were reconciled with the signed parent-packet restriction formula. The sharp tail checker reuses definitions from the pinned local helper prefix; it does not import another agent's code or rerun the old finite tests. Exact certificates/output files are saved as each phase completes, including incremental matching-root profiles.

Logarithms use 192-bit outward integer arithmetic, range reduction z=2^e u, 1<=u<=2, and 80 terms of the atanh series. For t=(u-1)/(u+1)<=1/3, the positive remainder is <=2*3^(-161)/(161*(1-1/9)). Each power multiplication and series division rounds outward. The independently enclosed positive ln2 is divided with lower numerator/upper denominator and upper numerator/lower denominator, then the exact dyadic exponent is added. Coefficient signs select the correct log endpoints. Small log arguments are prime-factorized for exact seed equality; large arguments remain explicit integer logarithms with rigorous intervals, avoiding infeasible trial factorization. Decimal profiles are display only and decide no sign. Memory estimates were <=50 MB, no >300 MB job was expected, no GPU/background task or dimension escalation occurred. No new tests are needed after these mathematical checks pass; final validation checks metadata and persistence only.

## proof dependencies and changed downstream conclusions

Elementary Walsh expansion, exact physical edges, homogeneity of Phi, the scalar log inequality and the reconstructed C005 bound are the mathematical premises. The seed matches A072-UNIFORM-ERASURE-WITNESSES@1 exactly, but that certificate's computed spectrum is not a premise: (2)-(4) reconstruct it from the family. A071's n5 optimality proof is context and is not rerun. No unreviewed all-dimensional claim is assumed.

A074 can now reconstruct a complete parameterized hereditary theorem rather than another witness. A072 can use (2)-(4) to validate future descendant engines. B15/A071 should retire perfect-matching/graph/padded-path dimension escalation as an unbounded E mechanism; finite graph improvements in dimensions <16 remain possible but are a separate, bounded target. A026/A028 receive the sharp terminal-inclusive class ledger (8), not a universal replacement. A089/B15 can apply their coherent biased-fiber interface to the transitive f6 raw recursion. No shared index or other agent folder was modified. One bundled scoped mechanism-closure claim is recorded, pending independent reconstruction.

## one next mathematical action and independent reviewer

Derive the normalized signed-collision reserve for transitive f6 composed with an arbitrary level-one-carrying inner g at its actual output bias; keep the inherited B_i(g), changing empty row, newly relevant coordinates and terminal H(g). Use raw f6's single-orbit profile only to test the proposed reusable transfer, not as another class endpoint. This is a substantive mechanism change after the sparse support route was analytically closed. Independent reviewers: A074 for the compressed matching/descendant certificate, A092 for the all-dimensional cutoff and structural upper bounds; A089/A091 for the next unequal-mean composition interface. Handoff occurs through saved artifacts; no external message was sent.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved under the requested run, together with DERIVATION.md, three frozen specs, code and exact outputs. Rolling STATUS.md (two lines), WORKLOG.md and LEARNED.md are updated. out/MANIFEST.json records bytes and SHA256 hashes, and protocol field sets/statement hashes are checked by save_stage.py. Local save/readback is claimed; independent acceptance, registry adoption, supervisor copy, Brain ingestion, mirror verification and publication are not. All writes remain inside A075.

## Universal bridge

This stage moves C018's selectable-erasure target by closing the entire matching witness mechanism: its sharp all-dimensional hereditary constant is exactly K6, every coordinate and physical descendant is paid, and perfect matching E tends to 2 while H/I tends to 4. It also rules out graph-edge variants in n>=16 and padded paths in n>=10 as improvements over that seed, using uniform analytic bounds rather than finite absence of failures. The scoped stopping ledger retains all terminal entropy, but no universal Boolean payment or unbounded H/I family is obtained. What remains is true-erasure payment through non-sparse, biased actual residuals. NEXT targets the signed-collision admission reserve for an arbitrary inner core using transitive f6 as calibration, retaining the inherited erasure, newly relevant coordinates and full terminal H(g); its single-orbit recursion can expose a false payment that the five-bit cheap-orbit path missed. That attacks an unpaid reusable transfer toward universal selection and changes mechanism instead of closing another fixed-gate class or repeating a sparse census.
