# exact target, quantifiers, hypotheses and units

A055 / B11, stage 2, run 20261013T212502Z-fleet05-A055-extremal-obstruction-referee. Follow the lead's activation target: for every fixed nonconstant uniform-cube Boolean core g, compute the proper-block minimum phi(F_r) as rarity p=2^-r tends to zero, derive the actual and R2 singleton prices, and identify the exact first failed criticality comparison on a frozen genuine example. Also distinguish fixed-core rarity from C013's amplified balanced arbitrary-seed reduction. Entropy is in bits. A proper block excludes the full physical cube and requires positive erased influence; its data portion may be all original data coordinates. Constants are not divided by influence. Universal FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-13 21:24 UTC; B11 STREAM_NOTES.md v2, 2026-10-11 23:3xZ; own STATUS, LEARNED and WORKLOG. Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2, and refreshed CURRENT_STATUS's scope. The lead directs A055 to activation phi and R2 as rarity tends to zero. This is followed, while consuming the newer board corrections: A051's automatic squeeze, A052's singleton-collapse obstruction, and A053's refutation of unconditional own-ratio continuity inference.

Read B11 lead run 20261011T230100Z REPORT and CLAIMS R1/R2/R5/R6. Read A051 stage 20261011T233123Z REPORT, CLAIMS and UNIVERSAL_DESCENT_SQUEEZE; A052 stage 20261012T003906Z REPORT, CLAIMS and SINGLETON_COLLAPSE; A053 stage 20261012T014744Z REPORT and CLAIMS. A054's latest run has no new mathematical report in the listed folder; its prior paid-component interface remains context. These paths and local byte hashes are recorded in out/SOURCE_MANIFEST.json. Reviews below are explicit about accepted analytic scope and unreplayed bundled counts.

The prior A055 stage's activation spectrum and two-point proof were consumed and rederived. Current threshold Proposition 8.9/Corollary 8.10, already source-pinned in stage 1, is the C013 balancing/activation baseline; it is not counted as new progress. No new literature-priority claim, remote readback or percolation premise is used. All new statements have direct derivations on disk.

# complete derivation or exact first unsupported line

DERIVATION.md is the complete proof, with CRITICAL_CLASS_EMBEDDINGS.tex as the concise interface. With h=(1-g)/2, c=1-Eg and raw indicator entropy decrement Lambda_B(h), the new all-proper-block limit is

    lim_r phi(activate(g,r)) = min(4, min_B Lambda_B(h)/E_B(h)).

Every mixed data/control block is represented exactly by a labelled data subset and the cardinality of its fresh control subset. A uniform remainder proves that minimizing control cardinalities may grow with r without invalidating the limit. The displayed explicit error is 2 delta_floor(r/2)/d0+(30+2delta_r)/(rc), delta_t=(8t+19)2^-t. This closes the fixed-core limit, not the unbounded raw-indicator payment. Fixed-core H/I tends to 4; C013 retains arbitrary ratios by simultaneous core amplification.

The exact control singleton depends only on d=p(1-Eg): its actual normalized decrement tends to 4, while its R2 upper price tends to 2+2/ln2. Exact data-singleton pair formulas retain the shifted empty-core row. For the standard g_m=z f^(tensor m), r_m=ceil(2log2(m+1)) family, beta_z=p_m(Ef)^(2m) and the erasure-pair expression proves phi(F_m)->0. Its H/I still tends to the original seed ratio. A violated fixed threshold eventually fails R2 at z itself. The terminal entropy p_m m H(f) and terminal influence p_m m I(f) remain explicit and unpaid; cheap root descent is compatible with FEI-hard terminal cores.

For the three-bit point-defect seed and C=2, r=1 passes every singleton averaged criticality comparison and every R2 singleton test, while the mixed balancing-bit/control block already fails by p D_C(seed)>0 and has exact phi=2. An individual balancing-bit child nevertheless already violates C at r=1, with deficit >13/32: averaged root tests do not certify individual children. At r=2, both balancing and control singleton R2 tests fail, with certified normalized gaps approximately 2.085256295171 and 0.026706867692. The first-failure order concerns detection by these root inequalities on this frozen seed, C and r=1,2 boundary, not the first existence of a violating child or a universal ordering of blocks. The supporting exact expressions and interval endpoints are in out/FIRST_FAILURE.json.

REVIEWS.md independently accepts A051-PROPER-BLOCK-DESCENT-SQUEEZE v1. It accepts only the analytic substatement and explicit tensor controls of A052's bundled singleton-collapse claim; the 1,150-case counts are not promoted by this review. The first unsupported universal line remains an absolute paid joint conditional-entropy/child-slack estimate on genuine all-descendant critical sources. The activation wrappers themselves are not hard critical obstructions, and no universal FEI constant is obtained.

# executed validation with domain, arithmetic, commands and outputs

Specifications were frozen before each execution. The original v1 full sweep stopped at an overly wide interval nonnegativity assertion after its pilot passed: separately bounding ln(2^r-1) and r ln2 lost shared cancellation. v2 fixed this by collecting powers of two exactly before enclosing rational residual logarithms near one. Its repetitive large-r all-small-core sweep was deliberately stopped; it did not issue a full certificate. The last captured checkpoint was 720 roots at 284.19 helper seconds. These events are preserved in out/REPAIR_NOTE.md and FULL_V2_ABORTED.json. The successful manually narrowed v3 domain is not mislabeled as the original 2,448-root coverage.

Commands from A055:

    python -X utf8 runs\20261013T212502Z-fleet05-A055-extremal-obstruction-referee\code\rare_descent.py pilot
    python -X utf8 runs\20261013T212502Z-fleet05-A055-extremal-obstruction-referee\code\rare_descent.py full
    python -X utf8 runs\20261013T212502Z-fleet05-A055-extremal-obstruction-referee\code\rare_descent.py replay
    python -X utf8 runs\20261013T212502Z-fleet05-A055-extremal-obstruction-referee\code\first_failure.py

Successful pilot v2: two cores, six activated roots, 228 candidate block orbits and 276 assertions, 0.089258 helper seconds. Successful full v3: all 270 labelled nonconstant cores through n=3 at r=1,2,3,4, plus two fixed balanced tensor cores at r=1,2,3,4,6,8,16,32. This is 272 cores, 1,096 roots, 38,408 exact candidate intervals and 25,154 assertions, helper runtime 58.639182 seconds. Replay PASS: 542 roots, all 11,756 labelled proper blocks, 101,410 assertions, 55.451808 seconds. Boundary PASS: 230 assertions, including 30 exact phi lower comparisons, 0.025179 seconds. Full/replay/boundary total is 126,794 assertions. Every root certificate was saved separately immediately under out/cases; all are below 20 MB. Six symbolic balanced-tensor records at m=1,2,4,8,16,32 use exact genuine Boolean product formulas without enumerating their large cubes. Complete counts/runtimes are copied into out/VALIDATION_SUMMARY.json from their actual outputs.

Replay checks physical child truth tables against compressed activation formulas for all 270 small cores at r=1,2 and both balanced fixtures at r=1, every labelled proper block. Spectrum pairing independently checks every relevant/nonrelevant data singleton and representative control, using exact Walsh coefficients and physical-edge influences. The boundary helper certifies exact zero singleton residuals as zero log expressions, strict failures as rational interval signs, and phi=2 by every block's exact lower comparison. It does not use a floating tolerance at the equality boundary.

Arithmetic is integer FWHT/physical edges, Fraction coefficients and rational log atoms. Powers of two are combined algebraically before a 24-term atanh enclosure with an explicit sign-aware tail; residual arguments have |z|<=1/3. Phi's value is enclosed by minima of all candidate lower and upper endpoints. A least-upper-endpoint witness is saved; uniqueness or exact tie classification is not asserted. Tiny negative lower/midpoint values in some zero-price enclosures are rounding-enclosure width, not a mathematical negative entropy decrement; true L is nonnegative by the proved block identity. Floats are display/runtime metadata only. Proofs, not finite checks, establish all dimensions and limits. Resource estimates were 90 MB (20 MB for boundary), peak RAM unmeasured; no expected >300 MB job, GPU, automatic dimension escalation or concurrent substantive job was started.

# proof dependencies and changed downstream conclusions

The new A055 bundled theorem is self-contained: activation Fourier coefficients, physical restriction/edge averaging, raw partial-Fourier entropy expansion, elementary scalar entropy bounds, and the two-point centered JS proof reproduced in REVIEWS.md. Existing C013 formulas are baseline calibration. A051's analytic squeeze is reviewed independently; A052's analytic distributional statement is reviewed at substatement scope. Neither pending finite NAND counts nor an unproved FEI endpoint is a mathematical premise.

A051/B11 lead receive the closed all-block rarity limit; A052 receives the exact shifted-empty-row R2 formulas and a genuine mixed-block failure missed by all singleton tests at r=1. A001/A021/A027/A028 receive a source-bound terminal-inclusive activation ledger. A053's equality-boundary warning is respected: no blanket own-ratio phi inequality is asserted. B20 should distinguish the fixed-core limit from the amplified C013 diagonal limit and retain p m D_C(seed) after tag exposure. Local reviews and claims are saved for adoption; no shared indices were changed.

# one next mathematical action and independent reviewer

Next: use the saved A052 NAND case 0006, mask 48, to separate its actual joint-channel cancellation from the singleton surrogate with individual terminal deficits retained, and seek a fixed-K payment on genuinely child-certified sources. This consumes a named existing false-negative block instead of expanding the completed activation family. A090 should reconstruct the uniform mixed-block limiting argument and the exact boundary independently. A094 should challenge the C013 phi->0 reduction and its terminal debt, and review the exact logarithm range-reduction repair.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, DERIVATION.md, CRITICAL_CLASS_EMBEDDINGS.tex, EXTREMAL_SCOPE_VERDICTS.json, REVIEWS.md, code, all frozen specs, saved successful/unsuccessful validation records and source/hash manifests are local to this A055 run. The final writer verifies all protocol field sets and every saved artifact hash/size; out/RECEIPTS.json is the local persistence receipt. STATUS.md, WORKLOG.md and LEARNED.md are current. Supervisor copy, remote mirror, registry adoption, independent acceptance of the new theorem and downstream use remain pending. No git, mail, brain writes, other-agent folder edits or external publishing occurred.

# Universal bridge

This stage moves B11's proper-block descent target feeding C019 by closing the all-block rare-activation limit with a uniform remainder, deriving exact actual/R2 singleton prices, and proving that C013's arbitrary-seed preserving wrappers have phi tending to zero rather than forming hard critical obstructions. The exact positive terminal deficit p m D_C(seed) remains; no absolute universal payment constant improves. What remains is joint-channel/conditional-entropy payment on genuinely all-child-certified sources. NEXT targets the existing NAND false-negative joint block because the easy activation root and its unpaid arbitrary terminals are now explicitly separated; another activation census or a geometry-only class bound would not close that universal bridge.
