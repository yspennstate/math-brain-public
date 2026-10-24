# A080 B16: independent retained-KL review and partial-matching scaling obstruction

## exact target, quantifiers, hypotheses and units

Review B16-RETAINED-KL-SANDWICH@1 for every actual Boolean sign function on the uniform cube and every adaptive physical stopping tree, retaining arbitrary terminal entropy and influence. Then audit the scalable partial-matching extension of the finite B15 six-bit selectable-erasure obstruction. Entropies and logarithms are in bits. Dimensions are arbitrary in the proof; finite verification uses a separately frozen domain. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2; BOARD.md supervisor update 2026-10-13 21:24 UTC; B16 STREAM_NOTES.md v2 (2026-10-11 23:25Z), A080 direction and retained-KL statement; lead CLAIMS.json run 20261011T225600Z, B16-RETAINED-KL-SANDWICH@1; ISOSPECTRAL_SPLICING_CURATED.md node identities and retained-KL target (8.1). Prior-stage papers and baseline standards were retained as context, without claiming a fresh paper review.

Current input also includes A074 stage2 REPORT finite f6 certificate; A075 original REPORT and live 20261013T212622Z DERIVATION.md partial-matching spectrum, influence and restrictions; A078 stage2 CORE_TRANSPORT_PROOF.md; A089 stage2 RESULTS.md. Local source fingerprints for the primary inputs are in out/SOURCES.json. A075's concurrent draft is credited explicitly: this stage adds uniform asymptotics and the all-dimensional no-growth verdict, rather than claiming the family formulas as original. No external brain queries were needed.

## complete derivation or exact first unsupported line

REVIEW_LEAD.md reconstructs all six steps of the lead's version 1 and accepts it independently. For every stopping tree, Q_T+E H(leaf)<=H(root)<=Q_T+E H(leaf)+(3/ln2) M_T and M_T<=I(root)-E I(leaf). The minority mass is min(u^2,v^2), equivalently (|a|-|b|)^2/4 in child coefficients. Replacing it by an unoriented child difference would be incorrect. The lead's phrase 'tree selection is irrelevant for Q' means equivalence of existence of a universal bound up to the additive influence budget, not numerical independence of Q from query order. No repair to the formal claim was needed. Its majority-Lambda evidence was not accepted as an asymptotic theorem.

MATCHING_ASYMPTOTICS.md gives the complete separate derivation. For k matched pairs and l isolated coordinates, r=2k+l, a=1+3k+l, N=2^r; nonempty Fourier numerators are -2(a-4u-2v) with multiplicities binom(k,u)3^u binom(l,v), while the empty coefficient is replaced by 1-2a/N. Paired and isolated influences are 2(a-4)/N and 2(a-2)/N. Regular paired-row entropy deficits cost at most 16/(N ln2), or 8/(N ln2) for isolated rows. The exceptional constant row costs at most b(2r+log2 e), where b=4(a-c)^2/N^2. These bounds prove uniformly over all partial matchings that every relevant coordinate B_i/Inf_i tends to 2, with an explicit upper bracket below 11/5 at all r>=64. All nonconstant functions in the family satisfy H/I<=20, with uniform limit 4. The original f6 still has min_i B_i/Inf_i>368/125; that finite obstruction remains valid.

First unsupported universal line: supply an actual Boolean operation or family producing unbounded H/I, or prove the retained-Q tree bound uniformly. This stage supplies neither. It closes the proposed partial-matching scaling mechanism and reviews an exact universal identity without claiming a universal FEI inequality.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before search. Pilot: all 16 partial-matchings through r=6 and all 22 Boolean truth tables through n=2; PASS, 964 assertions, 0.036 seconds. Full: all 1,089 partial-matchings through r=64 and all 278 Boolean truth tables through n=3; PASS, 41,101 assertions, 73.931 seconds. Actual integer Walsh spectra, physical boundary influence and direct paired entropy checks run through r=10. Exhaustive adaptive complete-tree extrema are computed by dynamic programming for n<=3. Arbitrary stopping-tree scope is justified by analytic telescoping, not inferred from a finite census.

Commands, from the A080 folder:

`python -X utf8 runs/20261013T212642Z-account05-A080-universal-counterexample-standard/code/check.py --pilot`

`python -X utf8 runs/20261013T212642Z-account05-A080-universal-counterexample-standard/code/check.py`

All algebraic data use integers and Fraction. Logarithms use a positive 32-term atanh expansion after range reduction to [1,2), with tail bounded by 2 z^(65)/(65(1-z^2)); division uses certified ln2 endpoints and outward rounding to 2^-90. Output float values are display only. The code proves the finite strict rational comparisons using enclosure endpoints; the dimension-uniform conclusion follows from the analytic error bounds, not extrapolation. Frozen memory estimate 100 MB; no job exceeding 300 MB was planned, so the memok gate was not triggered. One job at a time; no automatic dimension escalation. Exact endpoints and per-dimension checkpoints are in out/VALIDATION.json and out/MATCHING_PARTIAL.json; compact counts in out/SUMMARY.json.

## proof dependencies and changed downstream conclusions

The sandwich review reconstructs the node entropy identities and physical tree telescoping directly, rather than relying on the lead's floating census. Its statement and version are preserved in CLAIMS.json with an added A080 acceptance record. The source's supplied statement hash does not match its observed UTF-8 exact_statement; proof_source preserves that supplied hash and records the discrepancy, while the local statement_sha256 fingerprints the unchanged exact text. This is a provenance correction, not a proof repair. The narrow matching theorem uses elementary Walsh orthogonality, physical edge counting and the reconstructed binary deficit inequality; it needs no unproved FEI assumption. A075's restriction closure introduces only partial matchings, point defects and constants, so there is no unpaid complex descendant hidden in the family.

A075/A074/A089 can retain the finite selection obstruction but should cease pursuing this specific enlargement as a divergent mechanism. Tensoring and dummy coordinates do not repair its bounded ratio, under the earlier A080 standard. This does not rule out distinct recentering, graph families, or composition mechanisms. New theorem: author proof complete, external independent review pending. Lead claim: independent local acceptance recorded. Shared registry adoption, downstream mathematical use and mirror verification are separate and unclaimed.

## one next mathematical action and independent reviewer

Require and audit an actual restriction/recentering or composition operation that changes the paired spectral profile and retains gain at every newly relevant coordinate, with all leaf entropy and influence paid; do not extend the partial-matching dimension census.

A075/A074/A089 are the source-bound consumers; request A092 or A088 to reconstruct the asymptotic row bounds and entropy/influence limit independently. No messages or other agents' folders were modified. This handoff is recorded locally for the supervisor.

## actual persistence receipts or precise save blocker

All four protocol files, proof notes, frozen specification, exact checker and outputs are saved in this run. STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPTS.json records SHA-256 and byte counts of run artifacts and rolling files; its own hash is excluded to avoid circularity. Every file is below 20 MB. Local persistence is complete; copying to GitHub, mirror verification and registry adoption await the supervisor. There is no local save blocker.

**Universal bridge:** This stage independently accepts the B16 retained-KL stopping-tree bridge adjacent to C018/C019, preserving the exact error (3/ln2) M_T and M_T<=I-E I(leaf); it does not reduce that universal constant. It additionally retires the scalable partial-matching route quantitatively: H/I converges uniformly to 4, all coordinate erasure ratios converge to 2, and every ratio is below 11/5 from dimension 64 onward, despite the finite six-bit ratio exceeding 368/125. What remains is a dimension-independent retained-Q payment or an actual Boolean divergent family. Auditing a new gain-changing operation with complete physical and terminal costs is the shortest next route because merely raising this family's dimension has now been proved unable to cross that universal gap.
