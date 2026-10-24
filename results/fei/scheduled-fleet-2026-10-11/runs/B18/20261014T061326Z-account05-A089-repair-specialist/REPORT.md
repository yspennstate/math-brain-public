# A089 stage 5: physical child-slack ownership and a retained-debit continuation

## exact target, quantifiers, hypotheses and units

All functions are actual Boolean signs on finite uniform physical cubes; all entropies are in bits. S_K(f)=K I(f)-H(f) denotes a checked surplus, not a conjecturally available bank. Let h be negative on {0,1,2,4,8,16,32,6,17,40} and J(x)=-h(x xor1). Let g be the six-bit sign negative exactly on {0,1,2}. Form the actual36-bit function F=k(g^6), k=h or J, on disjoint copies. Query surviving inner coordinate i=0 or2 in block j=0 or1. These eight tags are alternative one-query prefixes, not eight debits simultaneously assigned to one owner.

Result: the four J alternatives have a certified K=4 child owner; the four h alternatives have one at K=9/2. After the other five core slacks pay each child's complete outer correction, the positive FULL query excess uses less than2/5 of the queried-child mean surplus. Its exact largest fraction among the eight alternatives is the J/block0/inner2 value, strictly between1/3 and2/5. A second physical query on that case's nonconstant core child preserves the old debit and pays old+new debit with less than3/5 of its grandchild surplus. The constant queried-core first child remains in the ledger with reach1/2 and selected-owner debit0; its full composed terminal retains all other cores and is nonconstant.

The generic owner rule below is proved for arbitrary independent cores and any fixed outer gate. Availability is an explicit hypothesis checked in these actual cases. No arbitrary-core surplus, universal FEI bound or full stopping-tree payment is asserted.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision2026-10-11-execution-v2; BOARD.md supervisor snapshot2026-10-14 06:12 UTC; B18 STREAM_NOTES.md v2 unchanged since2026-10-11 23:34; own STATUS. The lead's original lex/raw-five-bit tasks and our previous entropy ledger are completed. Board dispatch now supplies an actual non-flat physical-query boundary; composition-cycle growth has been closed by A075/A080/A071/A072, so it is not repeated.

Read A075 run20261014T034311Z REPORT and its output containing PROOF Section7: independent acceptance of A089-PAID-MODERATE-PREFIX-AND-COMPLETE-TERMINAL-LEDGER@1, source hash94622215e92cb75779b98dd3ad3292be1670dac5816298852c945cce272bbc01. Its new all-word theorem is context, not a premise or a new acceptance here. Read A072 run20261014T044904Z REPORT, INDEPENDENT_PROOF.md and NEXT_INTERFACE.md equations(A)-(B), plus its eight saved boundary records and boundary_validation.json. These explicitly request an unused child owner for positive Delta C. Own prior192-bit arithmetic is the only executable helper reused. Source hashes are in out/SOURCES.json. Earlier campaign/paper consultations remain previous-stage context; no fresh literature audit is claimed. No other agent's code was imported or executed.

## complete derivation or exact first unsupported line

### Failed statement and counterexample kept visible

The tested A089 extension in FROZEN_SPEC.json was: ALL eight A072 cases can use a dedicated queried-child S4 owner, completely unused after the other five core slacks pay every child outer C. This is false. The first all-eight run failed at h/block0/inner0. More decisively its actual36-bit parent has

    S4(h(g^6))<0,

with exact enclosing endpoints in out/FAILED_OWNER.json and a display approximately-0.099323980511. Its actual core S4(g)>0 (display0.147523348632), but six inherited core surpluses do not cover the full outer C (display0.239657982609). Core certification cannot be mistaken for complete composition certification. The original helper and failure are preserved in out/FAILED_HELPER_v1.py and FIRST_OWNER_FAILURE.md. The two positive-J pilot cases passed and remain valid. The explicit repair raises only h's rate to9/2; it does not erase the failed rate4 statement or attribute it to A072.

The earlier false unguarded reserve statement also remains in the campaign: the actual six-bit point defect has E>9/4 but both common-sign compositions under h have E<9/4. Our prior independently checked certificate is source-pinned. The current theorem uses actual terminal slack rather than assuming those reserves always have a favorable sign.

### Exact physical-query decomposition

For any outer Boolean gate k and independent cores g_l, let p_l=P(g_l=-1), v_l=4p_l(1-p_l), and q_l be the weighted outer pivotal probability. The unique occupied-block Fourier law gives

    H(F)=sum_l q_l H(g_l)+C(p),
    I(F)=sum_l q_l I(g_l),
    C(p)=H_p(k)-sum_l q_l h2(v_l).                    (1)

Query an actual uniform physical bit i in block j. Let superscripts b=0,1 denote its two children. Their true weights are1/2. Then q_j^b=q_j and average q_l^b=q_l for l!=j, because q_l is affine in p_j. Consequently

    Inf_(j,i)(F)=q_j Inf_i(g_j),
    Delta H(F)=q_j Delta H(g_j)+Delta C,
    Delta C=C(p)-average C(p^b).                     (2)

These identities retain every other core and both queried-core children, including constants. The mixed-bias coefficient computation uses raw multiaffine coefficients c_T=sum_(U superset T) khat(U) product_(l in U-T)(1-2p_l) and masses product_(l in T)v_l*c_T^2. It avoids divisions by v_l. At p_l=0 it still reconstructs the actual gate at all64 sign points by the full multiaffine Taylor identity; degenerate spectral masses vanish exactly. Direct weighted outer edge enumeration independently gives all six q_l. Actual inner Walsh transforms and edges establish the core/child data.

### Exact owner rule, including possible outer-cost deductions

For a proposed rate K, assume the relevant actual core surpluses are certified. In each child define

    A_b=q_j S_K(g_j^b),
    M_b=sum_(l!=j) q_l^b S_K(g_l)-C(p^b).

The COMPLETE child slack is A_b+M_b. Set U_b=A_b-max(0,-M_b); require U_b>=0. This pays any remaining outer cost from the selected child first, then identifies its unused part. The remaining other-owner amount is max(M_b,0), so child slack equals U_b+max(M_b,0) exactly. In our repaired cases M_b>0, hence U_b=A_b and the entire selected-child surplus is unused at admission.

Let e=Delta H(F)-K Inf_(j,i)(F)>0 and B=average U_b. A payment exclusively from this unused queried-child owner exists iff e<=B. This is the strongest exact rule for that prescribed owner: no allocation can average more than the available B. When B>0 and e<=B, choose theta=e/B and book D_b=theta U_b. Then average D_b=e, the remaining child owner is(1-theta)U_b, and all other-owner amounts remain untouched. The full parent slack is

    S_K(F)=average S_K(F^b)-e
           =average[(U_b-D_b)+max(M_b,0)]>=0.        (3)

Every complete terminal entropy is already present in these S_K values; none is removed to create the bank. The source identity (2) shows that e includes BOTH inherited core-query excess and Delta C. Paying only a positive curvature would leave a second debt unpriced.

### Eight exact feasible alternatives and their sharp fraction

Use K4 for J and K9/2 for h. For every one of the eight tagged queries, the independent certificates prove:

- every actual core and child has nonnegative S_K;
- M_0,M_1>0, so other cores pay each child outer correction before the selected owner is admitted;
- the FULL e is strictly positive;
- e<(2/5)B, hence at least3/5 of the selected mean owner remains;
- each full child and the full parent have nonnegative S_K.

The last parent inequality follows analytically from(3) and is also directly enclosed as an implementation check. The two positive Delta C cases are J/block0/inner0 and J/block0/inner2; the other six curvatures are negative. This agrees with A072 after independent reconstruction. All eight source full query decrements exceed4 times influence; increasing h's certified composition rate does not change that source assertion.

The exact minimum uniform fraction cap for these eight alternatives is lambda_*=e/B for J/block0/inner2, with e and B defined by(2)-(3), the explicit actual functions and rational biased spectra in out/CASES.json. Its outward interval is disjoint above all other fractions and proves1/3<lambda_*<2/5. Thus it is a defined exact entropy/logarithm ratio, not a rounded guessed constant; any smaller uniform fraction fails at this case. The sharpness is only for these rates, cases and prescribed unused owner. No optimal universal K or universal fraction is claimed.

### Carry the SAME booked debit through one more actual query

Select the root J/block0/inner2 alternative. Its bit0 child has the five-bit core g5 negative on{0,1,2}; its bit1 queried core is constant. The bit1 FULL composed function remains nonconstant and retains the other five core bills; CONTINUATION.json includes that unchanged full terminal explicitly. Let e1 be the root excess. Since only the nonconstant core child's selected slack is positive, the proportional allocation books D0=2e1 there and D1=0 on the constant-core branch. This is the actual reach-weighted debit: each root child has reach1/2.

Now query surviving inner coordinate0 in the nonconstant child, leaving the other five cores unchanged. Let U_parent=q_0 S4(g5), incoming remainder U_parent-D0, and U'_b=q_0 S4(g5^b), B'=average U'_b. Each new M'_b is again strictly positive, checked directly. Let e2 be this physical query's FULL rate4 excess. The certificate proves

    e2>0, D0+e2<(3/5)B'.                            (4)

Old debit is not reset: distribute it as D_old,b=D0 U'_b/B', and new debit as D_new,b=e2 U'_b/B'. Their conditional averages are EXACTLY D0 and e2. Each grandchild has unconditional reach1/4, while the unchanged root constant branch retains reach1/2 and debit0. At least2/5 of the grandchild selected owner survives both debits.

The no-renewal algebra is particularly explicit. Core slack transport gives

    B'-U_parent=q_0[Delta H(g5)-4 Inf_0(g5)],
    e2=q_0[Delta H(g5)-4 Inf_0(g5)]+Delta C2.

Subtracting, the actual remaining mean selected bank obeys

    B'-D0-e2=(U_parent-D0)-Delta C2.                (5)

The inherited core excess cancels precisely once; it is not booked again as a new outer allowance. The entire old D0 stays in the equation. Identity(5) is proved algebraically, and its independently calculated interval diagnostic encloses zero. The full child outer costs remain paid by the other owners throughout this prefix. out/CONTINUATION.json records every terminal, booked debit, reach and positive margin. This closes the supplied constant-child case through a second non-flat physical query, rather than merely postulating an owner at its first root.

### Honest first unsupported universal line

The owner rule is conditional and exact. What is NOT proved is that every arbitrary retained rare core or every deeper mixed physical history admits these unused U_b and positive M_b at one fixed K. The next data query must carry the current D_old+D_new, complete terminal laws and other-owner remainders; it cannot renew S4 as though no debit had occurred. Shared-data substitutions and uncontrolled ancestor-bank reuse are also outside this theorem. No C018 bound, full C019 stopping-tree theorem or full FEI result follows. Full FEI remains OPEN.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the original two-case positive-J pilot:429 exact predicates passed in0.5064683 seconds. The first all-eight job failed at the h owner condition; its helper/counterexample are preserved. REPAIR_SPEC.json preceded the explicit K9/2 h repair: all eight alternatives and16 children passed1466 exact predicates in1.0028035 seconds. No automatic threshold or dimension escalation was used. SHARP_PAYMENT_AND_REVIEW.json independently compares the eight fractions, reconstructs the failed parent and checks source curvature/excess scope:35 additional exact predicates, runtime0.1578141 seconds.

CONTINUATION_SPEC.json preceded the single additional adaptive prefix. The successful continuation checks the same old debit and all grandchild outer/core certificates, with actual structural and explicit interval predicate counts in CONTINUATION.json. Its initially copied integer counter snapshot was corrected to read the live engine count; this changed no mathematical result. Identity-overlap diagnostics are not substitutes for the algebraic proofs above. All decisions use Fraction/int and192-bit outward logarithm bounds with80 positive atanh terms and a proved geometric tail. Floats occur only in explanatory displays.

Commands from A089:

    python -X utf8 runs/20261014T061326Z-account05-A089-repair-specialist/code/check.py --pilot
    python -X utf8 runs/20261014T061326Z-account05-A089-repair-specialist/code/check.py
    python -X utf8 runs/20261014T061326Z-account05-A089-repair-specialist/code/certify.py
    python -X utf8 runs/20261014T061326Z-account05-A089-repair-specialist/code/continue_owner.py
    python -X utf8 runs/20261014T061326Z-account05-A089-repair-specialist/code/persist.py

The core/child Walsh and physical edges,64-point outer inverse, Parseval, six pivotal marginals, affine q transport and exact physical influence decrement precede entropy comparisons. No full36-bit table is attempted. Job caps55 seconds; estimated<=100MB, unmeasured peak; no job expected above300MB, memok override, GPU, background process or n escalation. Cases and certificates were saved as completed; failed attempts are not counted as accepted.

## proof dependencies and changed downstream conclusions

The new owner rule and actual certificates are rederived from actual Fourier/physical identities and scalar Shannon entropy. They have no unreviewed universal premise. A072's eight boundary sign and full-K4-excess clauses are independently reconstructed here, with an explicit scoped review artifact; its cycle theorem is not re-reviewed. A075's independent acceptance of our stage4 ledger is consumed as review evidence only, not as a proof premise or a reason to discard initial entropy.

A072/A075 can replace the missing owner in the two positive-J cases by this checked, unused queried-child S4 bank, including inherited query excess and the constant terminal. Four J alternatives work at4; the h alternatives require the explicit9/2 certificate here. They cannot extend the failed all-eight rate4 statement or sum the eight alternative debits against one owner. The actual second query preserves the ancestor debit, so downstream work has a specific nonzero incoming account rather than another fresh-root test. New narrow repair remains pending independent review.

## one next mathematical action and independent reviewer

NEXT: expose one further surviving active coordinate in the nonconstant J grandchild, carrying its existing proportional old-plus-new debit and the complete other-owner remainder; test condition(5) against the SAME owner. Then identify the first actual signed row condition permitting this transport for arbitrary non-flat children. A072/A075 should independently reconstruct the child-owner allocation and constant-child reaches; A074/A092 should challenge the h rate4 counterexample and sharp eight-case fraction. Do not repeat paid composition words or reset the now-nonzero child debit.

## actual persistence receipts or precise save blocker

All four protocol files, proof, code, frozen specs, exact per-case outputs, continuation and the failed owner are saved inside this new A089 run. out/RECEIPTS.json gives sizes/hashes, schemas, source pins, delta equality and actual successful runtimes/counts. STATUS.md has two lines; WORKLOG.md and LEARNED.md are current. Independent review of the new repair, shared adoption, supervisor copy, remote mirror verification and downstream use remain pending. No other agent/shared/brain tree was written, and no git or external messaging was used.

## Universal bridge

This stage moves C019's physical stopping-tree/child-surplus payment bridge at the exact boundary named by A072: it supplies an unused actual queried-child owner for eight non-flat one-query alternatives (J at4, h at9/2), with a sharp finite fraction below2/5, and carries the SAME booked debit through a second physical query at combined fraction below3/5, retaining the constant leaf and all other terminal bills. It moves no universal FEI constant; the original all-eight rate4 owner assertion is refuted by an actual negative parent slack. What remains is uniform eligibility and transport for arbitrary retained rare/non-flat cores and deeper histories. NEXT attacks that ownership constraint with the already-booked descendant account, which is shorter than another isolated class bound or a fixed-seed cycle search already closed by the team.
