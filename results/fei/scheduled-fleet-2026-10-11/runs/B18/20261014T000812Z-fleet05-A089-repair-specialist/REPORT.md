# A089 stage 3: sharp geometric signed-reserve repair

## exact target, quantifiers, hypotheses and units

All inputs below are independent uniform physical bits, all functions are Boolean signs, and all entropy is in bits. Write Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b), with continuous zero conventions, and E(g)=min over relevant i of B_i(g)/Inf_i(g). The outer gate h is negative exactly on {0,1,2,4,8,16,32,6,17,40}; +1 is outer bit zero. F=h(g_1,...,g_6), with six disjoint identical copies of any nonconstant core g. There is no bound on the number of physical core inputs.

This repairs the specific failed admission step R_p(beta_i^2)>=0 for every core, and audits the dimension boundary of A072's finite repair. A sharp analytic criterion determines when every positive singleton size has nonnegative reserve. Its exact certificates prove that A072's selected orientation works for arbitrary-dimensional cores at every certified bias M/64 with minority M=4,...,32. The high-E hypothesis is unnecessary at those fixed biases. Neither a continuum policy nor unrestricted repeated composition follows.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; BOARD.md supervisor snapshot 2026-10-13 23:59 UTC; B18 STREAM_NOTES.md v2 (unchanged 2026-10-11 23:34 UTC); own STATUS.md and LEARNED.md. B18's lex/raw-five-bit targets are completed in the prior run, so dispatch consumes the new A071/A072 signed-admission dependency rather than repeating them.

Read A071 runs/20261013T215901Z-fleet05-A071-search-space-design/REPORT.md, equation (1), point obstruction, and exact first unsupported line. Read A072 runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/REPORT.md, signed reserve (1), common-orientation policy, terminal identity (3), and arbitrary-dimension boundary; also read its out/orientation_policy.json. Read own previous code/profiles.py and code/finalize.py; copy only the former to this run as arithmetic.py. Prior campaign and manuscript consultations remain prior-stage context; no new literature audit is claimed. Source hashes are in out/SOURCES.json. No external code was executed or imported.

## complete derivation or exact first unsupported line

### Original failed statement and actual counterexample remain visible

False statement: for every actual core g and physical coordinate i, the recentered signed correction R_p(beta_i^2) is nonnegative; its sign-choice variant saying some common output sign always preserves E(g)>K is also false without a guard. The actual six-bit point defect has mean31/32, all nonconstant Fourier coefficients -1/32, and every influence1/32. Its E is greater than9/4. Both orientations under h have negative reserve and all 36 composed ratios less than9/4. The core and the matched outer automorphisms are transitive, so this covers every composed coordinate. out/FIXTURES.json independently encloses these inequalities. These are the A071 obstruction, independently reconstructed at that scope; no FEI counterexample is asserted.

### Exact signed split and physical coordinates

Put p=P(g=-1), m=1-2p, v=1-m^2. For any outer coordinate j, write h(y)=A(y_-j)+y_j D(y_-j). Expand A,D in the normalized product Fourier basis under independent output signs of mean m, obtaining coefficients a_T,d_T on subsets T of the five other blocks. Define U_T=(a_T+m d_T)^2, D_T=d_T^2, and q=sum_T D_T. The unfortunate reuse of the letter D in a section and its squared coefficients is resolved by the subscript. Physical pivotal enumeration gives q=2p(1-p)^3(2-p)>0. All six j have the same packet multiset by matched-pair permutations and pair swaps.

For a physical coordinate i of one selected core, let beta_i=ghat({i}), t=beta_i^2. Nonempty selected-core residual Fourier sets contribute q times their child Phi pairs, by homogeneity and Parseval on every other occupied block. For the empty selected-core residual set the two squared amplitudes are U_T and t D_T. Removing the inherited empty pair precisely once gives

    B_(j,i)(F)=q B_i(g)+R_p(t),
    R_p(t)=sum_T Phi(U_T,t D_T)-q Phi(m^2,t),
    Inf_(j,i)(F)=q Inf_i(g).

The influence identity follows independently from physical edges and the outer pivotal event. No unateness or singleton/influence equality is assumed. Irrelevant coordinates stay irrelevant; relevant ones stay relevant since q>0. Thus there is no lost new-coordinate sector in this disjoint substitution. The code independently reconstructs packets by uniform Walsh expansion and by direct signed conditional sections over32 outer assignments. It checks all six physical q's and sum U+vq=1 at each frozen bias.

### Sharp bias-only criterion

This scalar theorem applies to any nonnegative packet list with sum D=q>0, not just h. Terms with D=0 may be deleted. If m=0, R(t)>=0 directly. If m!=0 and any U=0 with D>0, define L=-infinity. Otherwise define

    L=sum_T D_T log2(U_T/D_T)-q log2(m^2),
    G=product_T (U_T/D_T)^(D_T/q).

Then R(t)>=0 for EVERY real t>0 if and only if L>=0. This is also the exact criterion on every interval0<t<=t_max with t_max>0.

Proof of sufficiency: for fixed t>0, z -> Phi(exp(z),t) is convex. Its second derivative is

    exp(z)/ln(2) * [ ln(1+t/exp(z))-t/(exp(z)+t) ] >=0,

using ln(1+x)>=x/(1+x). Homogeneity and weighted Jensen therefore give the quantitative lower bound

    R(t)>=q[Phi(G,t)-Phi(m^2,t)].

Phi(a,t) increases in a. L>=0 is exactly G>=m^2, proving sufficiency for every singleton size at once. For necessity, as t decreases to zero,

    Phi(a,t)/t = log2(a/t)+log2(e)+o(1)  (a>0).

Thus R(t)/t -> L whenever all active U are positive. A negative L yields negative reserve for all sufficiently small positive t. If some active U=0, their Phi terms are identically zero, while the subtracted packet still has its full q coefficient; R(t)/t tends to negative infinity. This proves necessity including coherent zero rows. When L=0, the Jensen bound still proves nonnegativity; equality for t>0 requires all active U/D equal m^2. No tolerance or float enters the criterion.

At a fixed dyadic bias p, arbitrarily small nonzero singleton sizes are realized by actual Boolean cores. On a sufficiently large n-bit cube, choose the number N of negative vertices to equal p2^n (even), put (N+2)/2 lex-first negatives in one coordinate half and (N-2)/2 in the other. Then |beta_i|=2^(2-n), tending to zero. Hence a negative criterion truly rules out all-dimensional coordinatewise reserve positivity at that bias, rather than merely ruling out an unrealizable scalar parameter. This observation makes no claim that these cores have high E.

### Exact arbitrary-dimension application at the certified biases

At p=M/64, M=1,...,63, the outward rational logarithm certificates prove L>0 exactly for

    M=4,...,15 and M=21,...,50.

M=32 is balanced and directly safe (it is included in the displayed range). All other unbalanced grid biases have L<0 or an active coherent zero row. Additional frozen biases1/128 and127/128 are unsafe. The full packet lists, exact L intervals, and any zero-row status are in out/BIAS_CERTIFICATES.json. These are classifications of the sharp scalar criterion, not sampled singleton sizes.

For any actual core of ANY dimension whose smaller output side has probability M/64, with4<=M<=32, first orient that smaller side to negative. Keep this orientation for M=4,...,15 or21,...,32; complement it for M=16,...,20. In the latter case the chosen count is64-M=44,...,48, in the certified safe range. This is a single sign for all physical coordinates. The criterion and the exact split imply

    B_(j,i)(F)/Inf_(j,i)(F) >= B_i(g)/Inf_i(g),
    E(F)>=E(g).

This extends A072's same-bias policy beyond six-bit cores and removes its E>=14/5 hypothesis on this bias grid. It does NOT extend to every core density with the same rounded count, every real p between grid points, or the bias produced at a subsequent composition depth. Nearby biases have continuity neighborhoods when all active U>0 and L>0, but no explicit continuum cover is certified here.

An explicit physical12-bit core with negative half-counts513 and511 has p=1/4, mean1/2, beta_0=-1/1024, and influence_0=1/1024. Its minority orientation has negative reserve; the complement at p=3/4 has positive reserve. This checks that the common orientation choice at M=16 is mathematically necessary for unconditional reserve positivity. No high-E claim is made for this core. Integer Walsh, Parseval and physical edges are checked directly on4096 entries.

### Terminal entropy retained and honest first unsupported line

Let pi be the normalized biased outer Fourier spectrum and rho(S)=ghat(S)^2/v on nonempty core sets. A physical Fourier set uniquely records its occupied-block pattern and its nonempty inner sets, so the law is hierarchical with disjoint support. Consequently

    H(F)=H_p(h)+6vq H(rho)=6q H(g)+C_p,
    C_p=H_p(h)-6q h2(v),
    I(F)=6q I(g).

The entire H(g) is retained. The proof does not pay C_p, choose a stopping policy, or reset the core reference. The first unsupported universal line is: at every dyadic bias arising from arbitrary-dimensional high-E cores, some common orientation has a nonnegative reserve for every relevant singleton, or any negative reserves can be paid from an exclusive signed terminal-inclusive influence reserve. The criterion at65 exact biases does not establish that line. Reapplying the fixed-grid policy to h(g^6) without checking its new bias is unsupported. Full FEI remains OPEN.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before the65-bias pilot. code/check.py uses exact Fraction coefficients,192-bit outward logarithms and80-term positive ln-series with the copied proved remainder. The independent packet path uses signed conditional expectations rather than the same polynomial transform. All2535 packet/multiplier/Parseval assertions passed; runtime43.565007800003514 seconds. The exact bias classifications were saved after each completed bias. Additional singleton diagnostics are exactly the ten frozen p=M/64 and complements for M=16,...,20 with beta=1/1024; they do not decide the all-t theorem.

out/FIXTURE_SPEC.json precedes code/fixtures.py. It checks both point orientations, the4096-entry physical core, and safe-bias nonnegativity at two frozen singleton sizes. See out/FIXTURES.json for actual assertion count and runtime. These scalar checks supplement the analytic proof; they do not substitute a finite t grid for the sharp criterion. Commands:

    python -X utf8 runs/20261014T000812Z-fleet05-A089-repair-specialist/code/check.py
    python -X utf8 runs/20261014T000812Z-fleet05-A089-repair-specialist/code/fixtures.py
    python -X utf8 runs/20261014T000812Z-fleet05-A089-repair-specialist/code/persist.py

Jobs are serial, estimated<=80MB, with55-second compute caps; no job over300MB, memory-gate override, full72-bit table, dimension escalation, GPU or background process is used. Estimated memory is not a measured peak. Runtime and any failed attempt are preserved in out.

## proof dependencies and changed downstream conclusions

The signed split, convex criterion, actual realization and terminal identity are rederived from elementary Fourier expansion, Booleanity and exact scalar inequalities. A071 and A072 supply the failed target and finite policy; their pending acceptance is not a premise of the proof. The prior A089 arithmetic helper is reused with its existing series proof, then exercised through the independent packet path. One bundled narrow repair claim is recorded, pending independent review; it does not open a new broad universal candidate.

A071/A072/A075 can now use the selected finite policy at the same exact core biases in arbitrary dimension. They must retain the actual bias condition and C_p. The dimensional restriction was necessary for A072's sparse-core exclusion, but is unnecessary for reserve positivity at its safe selected grid biases. The unsafe-bias certificates explain why raw finite-grid inference or minority orientation alone cannot supply arbitrary-core admission.

## one next mathematical action and independent reviewer

NEXT: certify a continuous common-orientation cover for the sharp signed log potential L(p), using the explicit outer polynomials, and isolate any intervals where both signs fail. At such intervals test actual high-E realizability and retain C_p in one physical influence ledger. This targets the universal admission gap directly and does not call for a larger truth-table census. A072 or A075 should independently reconstruct convexity, the zero-row asymptotic and the safe-bias certificate; A085/A092 should challenge necessity and common-orientation quantifiers.

## actual persistence receipts or precise save blocker

The four protocol files, proof, code, frozen specs and per-bias certificates are local to this new immutable A089 run. out/RECEIPTS.json supplies exact sizes and SHA256 digests, field-set/readback checks and actual runtimes. STATUS.md has two lines; WORKLOG.md and LEARNED.md record the new scoped theorem. Independent review, registry adoption, supervisor copying, mirror verification and downstream use are pending. No shared index, another agent folder or brain was written.

## Universal bridge

This stage moves B18/B15's signed-admission bridge toward C018 erasure B<=KI by proving an exact necessary-and-sufficient bias-only criterion for unconditional coordinate reserve positivity and extending the finite six-bit orientation policy to arbitrary-dimensional cores at all its selected exact biases, with no high-E premise. It moves no universal constant and pays no C019 terminal correction: off-grid biases, possible high-E cores in both-sign bad sectors and the full C_p price remain. NEXT is the shortest route because a continuous sign cover or a realizable bad high-E sector decides the actual missing admission step using a scalar polynomial/log certificate, rather than repeating a finite census or another isolated class estimate.
