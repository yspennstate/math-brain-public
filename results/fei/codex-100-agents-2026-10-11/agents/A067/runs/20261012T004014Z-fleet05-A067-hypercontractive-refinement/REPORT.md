# A067 stage 2: padding access with one retained-core reserve

## exact target, quantifiers, hypotheses and units

Pay access to Boolean leaves with U<=bI in C019, rather than assert hereditary support control. For every Boolean seed g on m>=1 coordinates, add r>=1 dummy coordinates and flip one physical vertex. In bits, every padding-only restriction tree that stops clean branches satisfies

    Q_pad <= 4 I_queried + (1+6/ln2) I_core.

The reserve is used once over the entire padding tree. If all terminal restrictions satisfy U<=bI, the complete ledger gives H<=(3+2b+6/ln2)I; for b=1 the constant is <14. A sufficient admission is the U condition for both the unedited seed g and the fully stripped edited seed F_0. This is a measurable Boolean-specific restriction certificate. It does not admit arbitrary core leaves. Full FEI remains open.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md (00:39 UTC), B14 STREAM_NOTES.md v2 (23:25 UTC), own STATUS.md, LEARNED.md and stage-1 proof/claim package were consumed before continuing. The lead's requested padding-strip limit and U stopping access are the direction followed. EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full and reloaded for schema checks. Campaign registries, plan, research-push seeds and the threshold/percolation text contexts read in stage 1 remain inherited background; no paper theorem is newly invoked as an unchecked payment.

New source-bound reads: A066 stage 2 (20261011T233317Z), DERIVATION.md Sections 1-5 and its two claim versions; A070 stage 2 (20261011T230551Z), DERIVATION.md Sections 5-6 and its hybrid claim; A088 (20261011T223053Z) review receipts for the stage-1 A067/A068 certificates; A070 acceptance of A069. The B14 lead's 20261011T224500Z neutralization REPORT.md/CLAIMS.json were also read. Exact source hashes are in out/SOURCE_MANIFEST.json.

The lead's asymptotic neutralization is compatible with this route, but its displayed continuity bound needs a small-eps qualification: n=1,N=2 makes its proposed eps greater than 1, outside h2's domain. That version was not independently accepted or used here. REVIEW_B14_QUEUE.md gives the exact source-bound caveat.

## complete derivation or exact first unsupported line

DERIVATION.md is the complete proof, including units and terminal obligations. Section 1 derives an exact entropy-drop formula from all signed Fourier coefficients. Section 2 uses Boolean coefficient granularity and a scalar second difference to prove the fixed-seed padding-node ratio tends to 4, with explicit bound 4Lp(|m+r-3|+m+3/(2ln2)). Section 3 proves every point-defect node has rate <=5, handling dimensions 1,2,3 exactly. Section 4 constructs U<=I stopping trees for dictator surgery and Maj3 tensor point defects; their complete ledger has rate 5. These known FEI classes are calibration of the access mechanism, not the main advance.

Section 5 proves a scope obstruction: for an even-dimensional quadratic bent seed at fixed padding r, the node rate grows with slope 2^(1-r) in seed dimension. The explicit m=2,r=2 rate already exceeds 5. This is not an unbounded H/I family.

Section 6 sums padding corrections before paying them. Expected queried influence is the same d at each surviving padding depth. The aggregate correction is at most (1+6/ln2)md; cube edge-connectivity and the exact one-vertex pivot change prove md<=I_core, including constant seeds. The terminal certificate and this single reserve combine into one coefficient on expected leaf influence. No reserve is renewed at descendants. Section 7 records finite edited-tribes tests. Their last-padding nodes can exceed rate 5, so even padding strips cannot inherit the point-defect rate for arbitrary seeds.

The first unsupported line for universal FEI is a dimension-independent payment of access inside an arbitrary active core to U-certified leaves, with the entire remaining entropy retained. An unmodified arbitrary seed is a positive-probability clean leaf of the padding tree; treating that leaf as paid would simply assume the missing theorem.

## executed validation with domain, arithmetic, commands and outputs

All computations were frozen before execution. FROZEN_SPEC.json uses helper 1.1 after a documented pilot repair, exact integer Walsh transforms and Fraction influence/U. Entropy uses rational intervals for logarithms via 20 positive atanh-series terms with a proved tail bound; bent checks use 32 terms. Every sign decision uses the rational interval, not the printed decimal. No job exceeded 100 MB estimated memory, so the >300 MB memory gate was not triggered. No dimension escalation, GPU, window or background job was used.

- code/check.py pilot: 9 cases, 196 assertions, 0.029 seconds. The original pilot found an attempted irrelevant-padding query on a clean tribes branch. The helper now queries only relevant coordinates; out/PILOT_REPAIR.md preserves the failure and correction.
- code/check.py full: 45 cases, 1,816 assertions, 0.286 seconds. Domains: dictator surgery n=2..10; Maj3 tensor point defects n=1..8; width-two edited tribes with two or three blocks and r=2..5; fixed dictator/AND2/Maj3/address2 seeds with r=2..6. Actual physical children, U leaves, queried and terminal influence, terminal entropy and telescopes were checked.
- code/check_bent.py: 60 compressed cases, 656 assertions, 0.276 seconds. Even m=2..40, r=2,3,4; direct truth-table reconciliation at m=2,4,6,8,r=2. Exact multiplicities and rational intervals validate the displayed Taylor error and complete padding reserve, without constructing a 2^40 truth table.
- code/check_reserve.py: every one of the 276 Boolean sign seeds on m=1,2,3, each with r=1..4: 1,104 cases, 17,301 assertions, 1.369 seconds. Included six constant seeds and 720 admitted U<=I trees. Core-influence reserve, actual seed/edited leaves and the full padding entropy telescope were independently checked from truth tables.
- code/tribes_witness.py: diagnostic replay of two already frozen width-two tribes cases, 114 assertions, 0.014 seconds. out/TRIBES_NODE_WITNESS.json records actual restricted truth tables, coordinate labels, rational I,U and entropy-drop intervals. The two-block example certifies a last-padding node rate >8; the three-block example exceeds 5. The exact integer inequalities 3^9>2^14 and 3^9*5^25<2^76 certify the dimension-three point-defect rate <5 and bent m=2,r=2 rate >5.

These five jobs performed 20,083 assertions, with overlapping cases counted as executions, not distinct functions. Final packaging verifies the eight finite tribes trees have all node rates <9 and all leaves U<=I; hence their finite complete ledgers give H<=9I. No all-width tribes theorem is claimed. Outputs retain rational endpoints and timings. Regenerate with python -X utf8 followed by the corresponding code path and pilot/full argument. The frozen specs contain exact domains, counts, memory estimates and runtime limits; no search is performed by code/finalize.py.

## proof dependencies and changed downstream conclusions

The padding reserve itself uses the exact singleton physical restriction identity C005 and elementary Boolean cube edge-connectivity, not hypercontractive smoothing. Conditional terminal payment uses the stage-1 A067 local coefficient-granularity theorem, already independently reconstructed by A088 and A070. C019 is used only for its exact physical entropy/influence telescopes. The conjectural universal erasure or stopping payment is not a dependency.

REVIEW_B14_QUEUE.md independently reconstructs A066-POSITIVE-RESTRICTION-HEAT-LEDGER v1, A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION v1, and A070-HYBRID-SCOPE-AND-THREE-REFERENCE-NOGO v1 at their stated scopes, without author repair. CLAIMS.json preserves their statements and adds A067 acceptance receipts. Central adoption is pending. These receipts reduce the local source-bound pending queue to the lead's neutralization candidate; the single coherent new padding-access candidate keeps that queue at two. No second new broad candidate is opened.

Downstream substitution: retain the one core reserve instead of a universal node rate. Fixed-seed padding stripping does converge to rate 4, but varying bent cores refute uniformity. The terminal U certificate is useful once access is separately paid. Consumers must keep that admission condition and must not extrapolate the finite tribes tests to arbitrary widths.

## one next mathematical action and independent reviewer

Extend the single-reserve ledger to two physical edits with shared active core, tracking reserve ownership through actual restrictions and keeping terminal entropy. This tests the first interaction absent from dummy-padding stripping and can address arbitrary core access; another isolated seed calculation cannot. A070 is the requested independent analytic reviewer, with A088/A094 for the exact coefficient and arithmetic reconstruction. Review is requested through artifacts only; no messages were sent.

## actual persistence receipts or precise save blocker

All four protocol files, proof, independent-review note, frozen specs, code and exact outputs are saved in this agent's run directory. out/SAVE_RECEIPT.json records actual sizes and SHA256 hashes, and out/SOURCE_MANIFEST.json binds the read-only inputs. code/finalize.py checks the protocol field sets and the byte-identical progress compatibility copy. The reviewed statements are preserved. Every artifact is below 20 MB. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. No shared index, other agent folder, brain database or git tree was modified. Supervisor copying, GitHub mirror verification and independent acceptance of the new claim are not claimed.

## Universal bridge

C019 advances by a universal payment for dummy-padding access: Q_pad<=4I_queried+(1+6/ln2)I_core for every Boolean seed, with one retained-core reserve. When actual terminal leaves obey U<=bI this closes the complete ledger at 3+2b+6/ln2; the fixed-seed node limit and rate-five stress trees are supporting certificates. What remains is access inside arbitrary active cores, or shared-core edits, without repeatedly spending retained influence or omitting leaf entropy. The next two-edit ownership calculation is the shortest extension toward that universal obligation because it tests the interaction that padding alone never exposes, rather than adding another already isolated FEI class.
