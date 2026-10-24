# exact target, quantifiers, hypotheses and units

A064 / B13, global debt potential, assigned run 20261011T224431Z-account05-A064-global-debt-potential. All functions are Boolean signs on finite uniform cubes; Fourier coefficients are normalized; entropy, KL and logarithms are in bits. Total influence is ordinary physical influence. A fair physical restriction tree queries only fresh coordinates, with decisions determined by revealed history and an independent seed, and stops within n reveals. The actual Boolean restriction at a node is g_v, the queried influence d_v, and its entropy decrement D_v=H(g_v)-avg H(children). Branch probabilities are physical, not spectral.

The global payment condition has the sign convention

    D_v <= C d_v + Q_v - E[Q_child | v].

The first deliverable is a boundary-complete finite-tree payment theorem. The explicit successful potential is the terminal-corrected reserve

    Q_v = H(g_v) - E[H(g_terminal) | v].

It has exact drift D_v, nonnegative values and zero terminal values, but can grow on a rare branch. Its initial resource bound is proved independently for arbitrary-core point activations, Q0<=8 times the exclusive queried control influence, retaining the full arbitrary terminal entropy. On the unbounded family of activated arbitrary bent point-splice cores, both control-first and selector-first initial bounds are proved, respectively <=8 and <=9 times queried influence, with separately certified terminal entropy below 3 times terminal influence. These give class certificates H<=8I and H<=9I; the second is weaker than A023's direct H<=8I result and is a certificate for this potential and tree order, not a new better FEI constant.

The three lead-prescribed candidates are tested at actual selector roots: c*eta log(1/eta), c*I_remaining log(1/pi), and CI-H. The first two have all-fixed-constant no-gos for their stated formulas. The third has a sign obstruction and fails even when parent and children already satisfy the chosen FEI constant. None of these failures is a complete-tree total-debt falsifier or an FEI counterexample.

# sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 was read in full. README, CURRENT_STATUS, claim and obstruction registries, packet status, stream actions and the campaign plan were inspected. A064's contract is at plan lines 916-920; it requires explicit initial and terminal bounds, the complete KL rebate, coherent squared-amplitude terms, B05 tests and no reused credit. BOARD.md was read at stage start, snapshot 2026-10-11 22:37 UTC. B13/STREAM_NOTES.md v1, 2026-10-11 22:30Z, gives the three candidate directions and prohibits redoing the baseline telescope or A065's total-debt interpretation. Direction (c) has the sign issue described below; it is recorded in STATUS.md as required.

Original archived B05 report, run 20261011T193057Z-account01-B05-rare-restrictions, sections 2-7, source commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b: accepted sparse selector obstruction and packet lower bound. Earlier B19 and B09 reports were loaded for source navigation; B09 uncertainty is not used as a premise. Supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were inspected; source inventory was loaded. The mathematical passages used are BLOCK_RESTRICTION_IDENTITY equations (4),(10), ISOSPECTRAL_SPLICING sections 2-3, and LOG_ALLOCATION sections 4-5. C019 is the target bridge. No external provenance or novelty claim is made.

A062 FAIR_TREE_INFLUENCE_PROCESS.tex was read in full: one-step influence conservation, exact same-tree stopping interface and dimension-limit boundary guard. A087 REPORT.md was inspected at its source-bound acceptance records for A061 and A062. It independently accepted their baseline process interfaces; this stage uses their accepted finite-tree scope only. A023 REPORT.md, sections 2,4-6, supplies the new arbitrary-bias activation bound and both sparse tree orders. Its direct bound is reconstructed algebraically here and separately checked through all cores through n=3, so its unreviewed status is not concealed as an accepted premise. This stage builds the potential using that mathematical direction rather than repeats its KL search.

Supplied threshold 38pp text: Proposition 7.1 (exact composition), Proposition 8.9 (balanced activation), Corollary 8.10 (rarity retains full FEI). Threshold 29pp earlier text: Proposition 7.1 and introduction. Percolation 30pp text: introduction, Theorem 3.2 local guards and Fourier coefficients; alternate 31pp introduction and theorem map. These establish scope and normalization; no percolation or threshold gate admission is used for arbitrary cores. Whole-file loading/hash receipts are in out/SOURCE_RECEIPTS.json; they are not claims of auditing all unrelated results. Source text replacement characters were present in PDF extraction and did not affect the algebra reconstructed from explicit Walsh coefficients.

# complete derivation or exact first unsupported line

## Payment theorem and terminal correction

Let B=E sum d and L_I=E I(terminal) on the same finite tree. If an adapted integrable Q satisfies the displayed payment condition, E Q0<=K B, and

    E[H(terminal)-Q_terminal] <= L L_I,

then

    H(f) <= (C+K) B + L L_I <= max(C+K,L) I(f).

Indeed sum_{s<t}(D_s-Cd_s)+Q_t is a supermartingale. Finite expectation summation gives E sum D<=CB+E Q0-E Q_terminal. Add the retained terminal entropy, and use the exact nonreusing influence split I(f)=B+L_I. The potential may be signed at intermediate nodes. A sufficient leaf condition is Q_terminal>=0 with H(terminal)<=L I(terminal). If the weaker root condition E Q0<=K I(f) is all that is proved, the corresponding conclusion is H<= [K+max(C,L)]I; it does not give the sharper queried-budget constant. This distinction prevents using a terminal influence account once for the reserve and again for the leaf.

For any fixed finite tree define A_v=E[H(terminal)|v], Q_v=H(g_v)-A_v. A is a martingale. Thus Q_v-avg Q_child=D_v, and Q_terminal=0. The erasure plus JS identity makes D_v>=0, so backward induction proves Q_v>=0. The same backward induction shows this is the unique exact-drift solution with zero leaves. Its construction is general, but Q0=H(f)-E H(terminal) is not automatically linearly paid. With complete constant leaves and a universal Q0<=KI, that initial assertion would be FEI itself. No such bound is assumed.

This is a remaining-bill reserve; it need not decrease pathwise. Its entire expected terminal value is exactly zero for the finite trees below. No dimension limit, uniform-integrability shortcut or almost-sure disappearance of unpaid core entropy is invoked.

## Exact spectral minority/KL bill and coherence

At a node let x_T,y_T be the two actual child Fourier coefficients, q_T=(x_T^2+y_T^2)/2, m_T=(|x_T|-|y_T|)^2/4, M=sum m_T, and nu=m/M for M>0. Exactly

    D = M log(1/M) - M KL(nu||q) + R_B + JS(x^2,y^2),
    R_B = sum_T (q_T-m_T) log[q_T/(q_T-m_T)].

Zero-mass terms contribute zero, including M=0. The two remainders satisfy R_B<=M/ln2 and JS<=2M/ln2. The first follows from -(1-t)ln(1-t)<=t; the second follows from the scalar comparison between the JS contribution and half the squared Hellinger distance, as reconstructed in A062 and the source ISO section 3. M<=d, but M need not equal the signed queried mass d. M is also different from the physical output minority eta tested below.

The reserve drift is this entire D. Therefore Q0 equals the physically weighted sum of these exact bills, with each node's mu log(1/mu) and own-reference KL rebate included once. No KL value from one node is credited to another node with a changed reference. Branch probabilities multiply complete bills and are never substituted for spectral packet probabilities.

For the arbitrary-bias activation proof below, coherent constant-frequency terms remain explicit: m^2 log(m^2), a^2 log(a^2), and (1-pa)^2 log((1-pa)^2). They are the actual squared Fourier coefficients after recombination, not entropy of an incoherent label mixture. This includes the requested alpha^2 log(alpha^2) endpoint terms.

## Explicit arbitrary-core activation reserve and initial bound

Let g be any Boolean core, m=Eg, a=1-m in [0,2], r>=1, p=2^-r, and F=1+A_r(g-1) with fresh point controls. Query controls until the first mismatch, or stop at g after r matches. At an active node with s remaining controls, u=2^-s, set

    Q_s = H(1+A_s(g-1)) - u H(g).

All inactive leaves and the final core have Q=0. Conditional survival to the core is u, so this is precisely the general terminal correction. Its drift is D and it is nonnegative. Exclusive queried influence is B_ctrl=rpa, while expected terminal entropy and influence are pH(g), pI(g).

The actual Walsh coefficients give, with 0log0=0,

    Q_r = 2rpa(2-pa) + p m^2 log(m^2)
          -(p-p^2)a^2 log(a^2) -(1-pa)^2 log((1-pa)^2).

This follows by separating nonempty data packets, empty-data nonempty-control packets and the empty coefficient; no mean sign is discarded. The m term is nonpositive. The final term is <=2pa/ln2. For a>=1 the a term is nonpositive; for 0<a<1 it is at most 2pa[a log(1/a)]<=2pa/(e ln2). Therefore

    Q_r <= [4+2(1+1/e)/ln2] rpa < 8 rpa.

The a=0 case is exactly zero. The last strict constant is proved by the rational lower bounds ln2>56/81 from its atanh expansion and e>65/24 from its exponential expansion; 2*(81/56)*(1+24/65)<4. Negative means, m=0, a=2 and the last-layer sign change are all included. This reconstructs A023 section 4, credited as the source direction; it is not a new claim about the activation entropy identity itself.

If g has an independently proved H(g)<=L I(g), payment gives H(F)<=max(8,L)I(F). Without it the exact pH(g) is retained and unpaid. The threshold paper's activation equivalence explains why arbitrary core entropy cannot be dropped merely because p is tiny.

## Both query orders on an unbounded bent-splice family

Let b be any bent function on even k>=4 bits, v any vertex, delta=2^-k, b'=b-2b(v)1_v, and g the fair physical selector between b and b'. Activate g with arbitrary r>=1 fresh controls. This is an unbounded family in both k and r; r=2k with quadratic b and v=0 is B05.

Bent flatness gives I(b)=k/2 and |Eb|=sqrt(delta). Point-flip edge counting gives Ibar=(I(b)+I(b'))/2>=k/2-kdelta>=7k/16; I(g)=Ibar+delta. Also H(g)<=k+1<=5k/4, so H(g)<=20I(g)/7<3I(g). The activation parameter a=1-Eg lies in [11/16,21/16]. Thus control-first has Q0<=8rpa, zero terminal reserve and terminal entropy <=3pI(g), yielding H<=8I.

For selector-first, first query the physical selector at the root, then use the above control-first trees in its two children. Leaves are constant, b or b'. Root d=pdelta. The signed Fourier allocation is lambda=d[log(1/d)-KL(nu||q)]<=d log(1/d); the full decrement is <=lambda+3d/ln2. Therefore

    D_selector <= pdelta(r+k+3/ln2) <= rpa.

For the second bound use delta<=1/16, kdelta<=1/4, r>=1, 1/ln2<81/56, and 1/16+1/4+243/896<11/16<=a. The actual root potential is D_selector+avg(Q_G,Q_H). Child reserves average to <=8rpa, so Q0<=9rpa<=9B, B=rpa+pdelta. The expected terminal entropy is <=pk; its expected influence is pIbar>=7pk/16, so it is separately certified below 3. This yields H<=9I on this order.

The selector bill and descendant control bill receive disjoint allowances of one and eight times B_ctrl, within the declared nine-times reserve. The terminal data account pIbar is separate. Control-first has no independent selector bill and keeps its entire entropy in the core leaf. The terminal correction accounts for this difference exactly. No coordinate's initial influence is silently pledged to two bills without the stated extra factor.

For products of disjoint components the same Q values add: Fourier entropy and influence add, conditional terminal entropy adds, and a query affects only its component. Thus these certificates retain unbounded component count without a depth factor. This extension is elementary tensor additivity, not a solution for shared controls.

## Candidate failures and first unsupported universal line

Full formulas, all-fixed-constant proofs and exact certificates are in POTENTIAL_OBSTRUCTION_TESTS.md. For c=1,C=4, both unactivated k=4 and B05 k=4,r=8 selector roots refute all three named candidates. The actual parent and both children satisfy H<4I in each test.

Physical-minority rarity has drift O(pdelta^2), while D>=(1-delta)(k-2)pdelta. Hence for any fixed c,C its drift cannot absorb B05's k*d term. The explicit history candidate Q=c I_remaining*depth has Q0=0 and average first-child potential c(I-d), so it gives a negative right side at the sparse selector for sufficiently large k when c>0. The c=0 case is the false local D<=Cd bound. These are failures of the specified candidates, not assertions about every nonlinear history potential.

CI-H has drift Cd-D and the requested inequality holds iff D<=Cd. This is the specific sign disagreement with the lead's third candidate. The opposite sign H-CI satisfies the exact drift equation but has an unpaid universal root bound. It does not provide an independent FEI proof.

In the B05 finite certificate, Q_root/(rpa) is in (4.38709653,4.38709654). On the first control match the actual reserve grows by a quantity in (0.08565966,0.08565967) bits, while the mismatch child has Q=0. The exact identity Q_root-avg Q_child=D proves the expected control despite the growing branch.

First unsupported universal line: there exists, for every Boolean f, a physical stopping tree whose terminal-corrected reserve has Q0<=K times its exclusive queried influence with a universal K and whose actual leaves have a uniform entropy/influence certificate. Neither the existence of such a tree nor a universal reserve estimate is proved here. Arbitrary-core activation pays only its control reserve and leaves pH(g) visible.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json was saved before the search. Helper A064-debt-v1; no randomness, symmetry reduction, GPU or automatic dimension escalation. All 278 raw Boolean truth tables through n=3 including dimension zero; all coordinate influence and signed-debt drift identities; all 276 positive-dimensional cores activated at r=1,2,3 (828 activation cases); exactly two named selector witnesses k=4,r=0,8. Largest table has 13 inputs. Estimated memory 40 MB, maximum runtime 60 seconds; no heavy job or memory gate was needed.

Command from A064:

    python -X utf8 runs\20261011T224431Z-account05-A064-global-debt-potential\code\check.py

Result: 4,105 exact assertions PASS, observed runtime 1.1197596000274643 seconds. Integer FWHT and Fraction arithmetic compute actual spectra and influences; exact entropy equalities compare rational prime-log vectors. This does not assume prime-log independence: equal vectors are sufficient certificates of equality. Every failure sign and activation initial-bound sign is certified by rational outward logarithm intervals, not floating values. Logarithms use dyadic normalization and 32 terms of the atanh expansion with tail <=2*z^65/[65*(1-z^2)], followed by signed interval multiplication and positive-denominator division. All exact interval endpoints are saved in out/VALIDATION.json; displayed decimals are only summaries.

The checker separately certifies the parent and child H<4I inequalities at the failure nodes and the strict reserve increase on the active branch. The all-dimensional initial-bound signs and all-fixed-constant candidate failures are supplied by the analytic proofs above. The finite computations are not extrapolated to arbitrary Boolean functions.

Source loading command: python -X utf8 runs\20261011T224431Z-account05-A064-global-debt-potential\code\read_sources.py. An earlier one-line navigation command had a literal-newline SyntaxError and was replaced by this script; it produced no mathematical result and modified no protected tree.

# proof dependencies and changed downstream conclusions

Accepted A061-FAIR-TREE-PROCESS v1 and A062-INFLUENCE-STOPPING-INTERFACE v1, with source-bound A087 acceptance, supply only the finite physical identities. Scalar minority/KL algebra and the explicit reserve proof are given here. A023's direct arbitrary-bias entropy estimate is credited and reconstructed rather than imported as independently accepted. The archived B05 lower packet bound is an accepted obstruction, also reproduced analytically in the candidate no-go. Neither B09 uncertainty nor an unreviewed universal payment hypothesis is used.

New downstream interface: A065 can distinguish terminal-corrected exact remaining bills from its minimal nonnegative Bellman envelope; A029/A037 can see the exact sign and terminal correction needed for slack transfer; A077 has an explicit growing-path reserve with every pH(core) terminal term present. All three prescribed candidate formulas now have source-realizable failure nodes. B13's A061/A062 claims had already received A087 independent acceptance at stated scope, so this stage adds one consolidated candidate package, pending independent review, rather than opening a third unreviewed broad route.

# one next mathematical action and independent reviewer

Next: take two point-subcube control events sharing a nonempty physical core block, with a common certified data core, and compute the exact terminal-corrected reserve for their union. Assign each shared queried influence to one declared event account, and derive the correction to the disjoint activation bound; do not sum the two independent event budgets. Freeze two private control widths and one shared width first, retaining (Pr(union))H(core) as the terminal term. This is the shortest extension because all independent control bills, both selector orders and their terminal costs are already paid, while shared ownership is the next unpaid universal mechanism.

Independent reviewers: A087 for finite-tree signs, labelled influence ownership and terminal boundary; A094 for all-fixed-constant no-go and arbitrary-bias endpoints. Review requested through saved handoff metadata only; no external message was sent.

# actual persistence receipts or precise save blocker

Saved locally: REPORT.md, GLOBAL_DEBT_POTENTIAL.tex, POTENTIAL_OBSTRUCTION_TESTS.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/check.py, code/read_sources.py, code/finalize.py, frozen spec, exact validation, source hashes, schema check and persistence receipts. STATUS.md, WORKLOG.md, LEARNED.md are current in A064. All writes remain inside A064. No git, external messaging, brain mutation, other-agent mutation or deletion was performed. Supervisor copy, mirrors, external review and actual downstream use remain unverified. out/PERSISTENCE_RECEIPTS.json records actual byte hashes of the completed files.

**Universal bridge:** This stage advances C019 stopping-tree payment by constructing a terminal-corrected reserve with exact KL-containing drift, independently paid initial control resource and zero terminal reserve on arbitrary-core activations, plus both-order certificates on the unbounded bent-splice family. The reserve demonstrably grows on an actual rare branch without violating expected payment. It also eliminates the three specified minority/history/slack candidate formulas and fixes the sign convention. The universal initial reserve bound and certified terminal admission remain open; arbitrary pH(core) is not erased. The shortest next route is the shared-control union ownership correction, because it addresses the first nonadditive influence account beyond the already paid disjoint activation mechanism rather than adding another isolated class bound.
