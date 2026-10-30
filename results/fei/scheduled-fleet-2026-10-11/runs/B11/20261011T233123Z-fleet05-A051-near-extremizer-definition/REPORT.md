# A051 / B11 stage2: exact composition descent and universal squeeze

## exact target, quantifiers, hypotheses and units

The lead's v2 target is phi(f)=min_A L_A/I_A on iterated point-defect compositions in dimensions6..9, where A ranges over nonempty proper physical blocks with I_A>0, L_A=H(f)-E H(f_a), and I_A=sum_(i in A)Inf_i(f). Report phi/(H/I), and identify a first composition with phi>4.54 if present. All functions are actual uniform-cube Boolean signs; entropy is in bits; the full block is excluded and constants are never divided by influence.

The frozen census comprises all1,150 unordered read-once NAND formula shapes with6..9 distinct literal leaves and arbitrary internal arity>=2. Each gate is a point defect. Seven separately defined repeated-variable seed/hybrid controls cover the literal lower-bound-family ambiguity. Scope is formula shapes and these exact controls, not all Boolean functions or all recursive lower-bound compositions. No dimension36 or larger search was started.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot2026-10-11 23:29 UTC, B11 STREAM_NOTES v2 (23:3xZ), my prior STATUS/LEARNED and previous proof. Read the lead's20261011T230100Z REPORT, especially R5/R6 and its requested next experiment. A053's saved claim confirms source-bound analytic review of prior A051 claims. This stage advances the lead-directed universal block-descent frontier rather than repeating the original existence packet. Protocol remains2026-10-11-execution-v2, with its seven report fields, fourteen claim fields and eighteen progress fields used exactly.

Consulted A080 FEI_DISPROOF_STANDARD.md for the corrected seed scope and corroboration only. Verified the seed definitions against primary [Hod, arXiv:1711.00762, Section1.2, PDF page3](https://arxiv.org/pdf/1711.00762). The two corrected six-bit and two eight-bit formulas have repeated variables; their balanced recursive self-compositions exceed9 bits. The stronger asymptotic lower-bound coefficient H/(I-1) is not their finite H/I or phi. The source paper's best-bound displays and limit theorems are not proof dependencies. A080's pending finite Hod certificate is not used. out/SOURCE_MANIFEST.json gives actual local-byte hashes, source locators and the primary URL. Failed arXiv HTML fetches were replaced by the readable primary PDF; no external store was modified.

## complete derivation or exact first unsupported line

UNIVERSAL_DESCENT_SQUEEZE.md contains a self-contained all-dimensional argument: reveal all but a least-influential bit. Every child has zero Fourier entropy, so phi(f)<=H(f)/(I-min_i Inf_i)<=n(H/I)/(n-1). At a function attaining the finite-dimensional ratio maximum M_n, all proper children have ratio<=M_n, hence every block has L_A>=M_n I_A. Therefore M_n<=K_desc(n)<=n M_n/(n-1). No all-dimensional optimizer is assumed. It follows that K_desc(n) tends to C_* in the extended real sense, and bounded block-descent is equivalent in finiteness to FEI. The lead's proposed phi/(H/I)<=1.33 check is automatic for n>=4, so it is not diagnostic evidence of a paid universal restriction rule. This is a specific mathematical disagreement about interpreting the experiment, not rejection of the lead's phi>4.54 target.

COMPOSITION_CERTIFICATES.md proves the formula enumeration, exact block-orbit reduction, entropy vector representation and rational-log enclosures. Every orbit minimum and finite maximum is certified. The census has117,240 block orbits representing470,340 labelled proper blocks. Every phi upper endpoint is strictly below227/50=4.54. The exact dimensional maxima display as4.3198821089,4.1919153810,4.2044382917,4.3104363691 for n=6,7,8,9. Thus there is no first composition exceeding4.54 in this frozen family. Point defects maximize at6,7, but a four-bit double-NAND module combined with literal leaves maximizes at8, and two such modules plus a literal maximize at9. An eight-bit three-level complete binary NAND tree has exactly phi/(H/I)=8/7, showing the pointwise squeeze factor is sharp at that dimension. All seven named seed controls also have phi<4.54; their exact values and minimizing blocks are saved.

First unsupported line: infer a uniform absolute bound for K_desc(n) for arbitrary Boolean functions from this finite composition census or from the squeeze. The squeeze contains the unbounded/unpaid M_n. There is no such inference, no proof of FEI, and no lower-bound-family disproof. These are two narrow, source-complete supporting claims; their independent acceptance is pending.

## executed validation with domain, arithmetic, commands and outputs

Each job was frozen before execution. out/FROZEN_PILOT.json and FROZEN_CENSUS.json cover the two-case pilot and exact1150-formula census; FROZEN_SEEDED_PILOT.json and FROZEN_SEEDED_FULL.json cover labelled reproduction. Memory estimates were80 MB, below the300 MB memok gate; observed peak memory was not measured. One substantive job ran at a time. Every file is below20 MB; no automatic dimension increase, GPU, git, external messages or persistent background worker.

Commands from A051:

    python -X utf8 runs\20261011T233123Z-fleet05-A051-near-extremizer-definition\code\descent_compositions.py pilot
    python -X utf8 runs\20261011T233123Z-fleet05-A051-near-extremizer-definition\code\descent_compositions.py full
    python -X utf8 runs\20261011T233123Z-fleet05-A051-near-extremizer-definition\code\check_seeded_and_replay.py pilot
    python -X utf8 runs\20261011T233123Z-fleet05-A051-near-extremizer-definition\code\check_seeded_and_replay.py full
    python -X utf8 runs\20261011T233123Z-fleet05-A051-near-extremizer-definition\code\aggregate_certificates.py

The two pilot jobs completed in0.119 and0.034 seconds. The full census passed140,692 assertions in154.8 seconds, below the1200-second frozen limit. The separate full checker passed4,927 assertions on2,984 labelled blocks in1.756 seconds, below its300-second limit. It uses direct physical truth-table projection and direct integer Walsh sums against FWHT, independently of formula simplification and orbit reduction. All influence, entropy vectors, expected child costs, ratio comparisons and tie checks are exact Fraction/integer/symbolic arithmetic. Rational atanh enclosures and signed interval sums certify logarithmic inequalities; floats only display certified endpoints. The second checker shares the proved log enclosure, so it is not an independent log implementation. AGGREGATE_CERTIFICATES.json certifies global comparisons, frozen counts, all threshold signs, and the exact8/7 sharpness expression. The finite checks do not substitute for the all-dimensional proof in the squeeze note.

## proof dependencies and changed downstream conclusions

The squeeze proof is elementary and independent of pending B11 recentering or biased-block claims. It uses finite optimizer existence, re-proved within the note. The computation uses only actual truth tables, exact Fourier/physical-edge calculations, and proved rational log bounds. Named gate definitions are sourced to Hod; no literature asymptotic theorem is assumed to certify these values. The exact finite sharpness comparison depends on the new squeeze claim and the complete block certificates, with an acyclic dependency.

A052 and the lead can discard phi/(H/I)<=1.33 as a discriminating composition test: the exact universal ceiling is already n/(n-1). They can use the eight-bit sharp example to calibrate any stronger pointwise comparison. The all-dimensional equality in the limit makes clear that block selection must provide a paid structural estimate beyond the ratio reformulation. The finite non-point-defect extrema at8,9 are concrete next controls for recentered beta_A selection. A053/A055's hidden-tensor and activation guards remain intact. No shared claim index was edited and no pending claim is promoted to independently accepted status.

## one next mathematical action and independent reviewer

Next mathematical action: derive a paid small/pivot-block inequality using conditional recentring beta_A on actual dimension-critical witnesses, and challenge it with the saved eight/nine-bit non-point-defect extrema and the repeated-variable balanced seed recursion; retain terminal entropy. This attacks the first unpaid universal selection line directly. Merely increasing the NAND census or checking phi/(H/I) against the automatic dimension factor cannot do so. A090 is the primary independent reviewer; A094 is alternate/second. Review should reconstruct the co-singleton/finite-optimizer squeeze, formula/block orbit completeness and rational signs independently from the definitions.

## actual persistence receipts or precise save blocker

Saved locally in this stage's A051 run directory: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, UNIVERSAL_DESCENT_SQUEEZE.md, COMPOSITION_CERTIFICATES.md, three computation/checker scripts plus record writer, all four frozen specs, per-case exact orbit certificates, full/pilot summaries, seeded/direct-replay certificates, aggregate certificate and source manifest. out/RECEIPTS.json records hashes/lengths and schema checks after generation. STATUS.md, WORKLOG.md and LEARNED.md are current. Every write stays within A051. Supervisor copying, remote mirror verification, independent acceptance and downstream adoption are pending; local replay is not external review.

## Universal bridge

This stage moves C019's universal proper-block descent frontier by the exact dimensionwise squeeze M_n<=K_desc(n)<=n M_n/(n-1), proving asymptotic equality with the full-FEI extremal ratio and correcting the automatic phi/(H/I) experiment, while1,150 exact composition certificates rule out phi>4.54 in the frozen6..9-bit NAND family and identify sharp/non-point-defect controls. The move is a quantitative equivalence and calibration, not a new influence payment: no absolute bound on either extremal sequence is obtained. What remains is a fixed-K paid block rule on arbitrary dimension-critical witnesses, including the conditional spectral entropy and physical channel. NEXT targets the recentered pivot payment on those witnesses because it addresses that exact universal debt; a larger isolated formula census or the already automatic ratio comparison would not shorten the route to full FEI.
