# A085 stage 2: a false screen-error contract with surviving finite certificates

## exact target, quantifiers, hypotheses and units

B17 lead v2 requests an adversarial audit of B17-KB4-CENSUS@1 and B17-KB5-CUTOFF@1, especially certlog.py's 2^-46 S floating error claim versus its 2^-40 S decision margin, exact fallback, and the 64-extremizer orbit. A071's three-bit grid was accepted in stage 1 and is not reopened. The updated board also supplies the completed A071/A082 five-bit census, so this stage audits its 40-bit integer lookup and coverage rather than rerunning it.

For Boolean witnesses, the measure is uniform, f takes signs, P(S)=fhat(S)^2, I_i=sum_{S containing i}P(S), B_i=H(S_i|S_-i), and all entropies use bits. Dimension is fixed at four, five or six; only named witnesses/orbits are generated. A generic prime-log screen test is explicitly a numerical helper test, not a Boolean FEI counterexample.

The helper's documented target is |computed sum - sum e_p log2(p)| < 2^-46 S, with S=sum |e_p| log2(p), integer coefficients |e_p|<2^50 and at most 600 terms. We refute that statement on an allowed 130-prime input in NumPy 2.4.3. We separately prove the existing 2^-40 S_computed sign decision safe on its intended matching-dimension domain of at most the first 600 primes. The source's actual four-bit comparisons have only 54 primes and satisfy even its stronger advertised bound.

## sources actually read, revisions and theorem locators

Read at stage start: BOARD.md supervisor snapshot 2026-10-13 21:34 UTC, B17 STREAM_NOTES.md v2 dated 2026-10-11 23:40 UTC, own STATUS.md and prior run conclusions. Protocol reread completely, revision 2026-10-11-execution-v2, unchanged from stage 1. Prior campaign/paper baseline readings remain context and are not new proof premises.

Read source originals without modification:

- B17 lead run 20261011T224300Z-claude-B17-erasure-census-affine-bridge: CLAIMS.json, code/certlog.py, code/census_n4.py, code/search_n56.py, code/write_records.py, out/census_n4.json. Critical locators: LinLog.float_screen; rational sign_form/enclose_form; census_n4.certify_max and the selected-coordinate/attainment loops.
- A071 run 20261011T233808Z-account05-A071-search-space-design: REPORT.md, CLAIMS.json, code/sparse_search.py, code/full_census.py, code/check_final.py and out/full_census.json. Critical locators: signed packet g(a,b), 96-to-40-bit outward rounding, seed lower comparison, anchored translation filters and integer quotient ceiling.
- A082 run 20261012T004123Z-account05-A082-finite-inequalities: REPORT.md, out/review_census.json, out/review_verdict.json. This prior independent full replay used different coefficient/log methods and has the same retained-mask hash as A071.
- A074 run 20261012T043949Z-account05-A074-independent-reproducer: REPORT.md and out/census_n4.json, carrying an independent unreduced selectable-erasure census and all 64 equality masks.
- B15 lead run 20261011T225100Z-claude-B15-erasure-countersearch: CLAIMS.json for the six-bit matching witness and finite lower cutoff.

All these bytes, original statements and helper versions are pinned in out/source_receipts.json by the finalizer. The audited certlog SHA256 is 1990ab0cd16537a6ae3f9d03bbcb1ca5c16db9f1a54590385dd0ec096fadb99f. Helpers are copied into THIS run before execution; source folders receive no import caches or output writes. No internet theorem or library log-error estimate is assumed.

## complete derivation or exact first unsupported line

### ERROR: the helper's unrestricted 600-term 2^-46 S bound

The exact integer coefficient vector is saved in out/small_failure_certificate.json. Its first coefficient, at prime 2, is 2^49; the other 129 coefficients lie in {1,...,4096}; the primes run through 733. Construct two identical rows in a Fortran-contiguous int64 array of shape (2,130). This satisfies both source assertions: max absolute coefficient <2^50 and last dimension <=600. LinLog(733) provides exactly these 130 prime constants. The multiplication result retains the strided reduction layout, and the observed source sum accumulates upward rounding errors.

Our independent rational log intervals certify

    8.0557 < computed value - exact prime-log sum < 8.0558,
    2^-46 S_exact < 8.0001.

The same strict violation holds if the advertised S is interpreted as the source-computed positive absolute sum, rather than the exact sum. Both computed hex value and complete rational endpoints are saved. The actual measured source error is approximately 8.05573538159, against a bound approximately 8.00000003236. Decimal displays are not the proof: the rational comparisons to 80557/10000, 40279/5000 and 80001/10000 are the certificate.

The construction tests all prefixes of one deterministic 600-coefficient row; 130 is its first failed prefix. A second execution uses the genuinely smaller 130-column helper and array, not a 600-column array with trailing zeros. This is the smallest tested failure in that construction, not a claim of global minimality over all floating inputs. The C-contiguous version gives a different, smaller error; the helper makes no layout restriction. The witness is a generic prime-log form, not asserted to arise from an actual Boolean spectrum.

First false source line: certlog.py, LinLog.float_screen docstring, 'integer entries <2^50 and <=600 terms ... differs ... by <2^-46*S.' No original Boolean inequality or finite constant is refuted. The returned sign in this positive witness is correct.

### HOLDS: the existing sign threshold and the actual four-bit error bound

Let u=2^-53. Each source log constant for the first 600 primes is checked against independently enclosed true log2(p), certifying relative error at most u. For matching-size integer coefficient vectors with |e|<2^50, float conversion is exact. Products and sums are normal and far from overflow in this domain. Under IEEE round-to-nearest, multiplication followed by any reduction tree of at most m-1 additions has standard elementary product-of-rounding-factors bound gamma_m=mu/(1-mu). This follows by multiplying factors (1+delta), |delta|<=u, and bounding the accumulated relative deviation by gamma_m; cancellation is handled by absolute term sums, not relative error in the result.

Writing T=sum e_p log2(p) and S=sum |e_p| log2(p), both the signed sum and the computed absolute sum obey

    |T_float-T| <= eta_m S,
    |S_float-S| <= eta_m S,
    eta_m = u+(1+u)gamma_m = (m+1)/(2^53-m).

At m=54, eta=55/(2^53-54)<2^-46, proving the advertised bound in the actual census domain, independently of contiguity or reduction order. At m=600, eta=601/(2^53-600)<2^-43. The exact rational inequality

    2^-40 (1-eta_600) > eta_600

means a source decision T_float>2^-40 S_float forces T>0; the negative case is identical. Thus weakening the advertised general error bound to 2^-43 S would fix its intended-domain contract while leaving every sign decision unchanged. No application should silently depend on pairwise summation when the API accepts other layouts. The matching-vector/prime-count and integer domain hypotheses must be stated; broadcast-mismatched arrays are outside this proved contract.

For the source's rational fallback, logarithms use a positive atanh series and a valid positive remainder; signed coefficient scaling swaps endpoints. Rounding at scale 2^320 encloses the already rigorous interval. It does NOT imply the interval width is at most 2^-320: the 90-term log remainder can dominate that rounding unit. The source correctly carries its true lower/upper endpoints and falls back to comparing products of integer prime powers if needed. Unique prime factorization proves zero iff all distinct-prime coefficients vanish. Its maximum-bigint guard raises an error rather than declaring an unresolved sign. Seven independent approximant forms exercise sign comparisons; at least three are screened as undecided and then correctly resolved by source sign_form. Exact zero is checked separately. No precision gap is found in this fallback logic.

### Four-bit comparison logic and equality-orbit scope

For N=16, W_s is an integer Walsh coefficient, q_s=W_s^2 and sum q=N^2=256. The exact prime-log numerator of B_i is sum over spectral pairs of [(a+b)log2(a+b)-a log2(a)-b log2(b)], and its influence denominator is L_i=sum_{s containing i}q_s. Entropy numerator is 2048-sum q_s log2(q_s). The decrement formula includes the correct restriction denominators and has constant term 512 at parent scale. Our direct physical restrictions confirm the reported decrement value on the attaining witness.

A floating argmin may select ANY relevant coordinate for a universal upper comparison: proving its ratio <=the target proves the minimum <=the target, even if it is not the exact argmin. For attainment, all relevant coordinates of the chosen maximizing witness must separately meet or exceed the target; the source does this. For extremizer classification, an exact zero for just the chosen coordinate alone is not enough. The missing logical step is supplied by orbit saturation: the known attaining orbit has 64 distinct tables, every one has its minimum at the target, and the certificate has exactly 64 zero selected-coordinate rows. Thus no other extremizer exists. We independently generate this orbit, then compare it AS A SET with A074's 64 masks from its separate complete census.

The 64 tables are point defects on three physical coordinates with one dummy coordinate: their minority support is an edge of the four-cube. There are 4*2^3=32 such negative supports and 32 complements. The H/I point-function orbit has 16 negative singletons and 16 complements. The aggregate B/I orbit has a three-point path in two coordinate directions, with unique degree-two center: 16*C(4,2)=96 negative supports and 96 complements. Our code generates the respective 64, 32 and 192 orbits and verifies the witness prime-log values stated by B17. For the latter two comparisons, source counts plus the known attaining orbit give the same saturation argument.

Range checks close a separate integer risk. Using v_p(m)<=8 for m<=256, mass sums and the source vector formulas bound entropy, erasure and decrement prime coefficients in magnitude by 4096, and the four-coordinate aggregate by 16384. The conservative comparison bound 2*1024*16384=33554432 is below 2^50 and int64 capacity. No overflow occurs before the helper's assertion in these actual forms. Zero masses contribute zero; irrelevant L_i=0 coordinates are omitted; the two constants are excluded. Max directly enumerated dimension remains four.

This is an independent audit of the census logic, screen, witnesses and orbit completion, not another execution of its 65,536-table job. The source's entire bundled upper census remains its original executed artifact; A074 independently supplies the selectable-erasure component. We issue a numerical-logic scope verdict, not a claim that A085 reproduced all four source maxima by a new full census.

### Five-bit cutoff, integer lookup and covering filters

For g=-1 exactly on {5,12,13}, our independent Walsh and direct character sums agree, inverse transform reconstructs every sign, and physical edge counts independently verify all influences. Coordinates {1,2,4} have I_i=3/16 and ratio

    K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89).

Coordinates {0,3} have I_i=1/16 and the stated higher ratio 16-(63/8)log2(3)+15log2(5)-(169/8)log2(13)+(85/8)log2(17). Exact intervals prove these are higher and K5>107/40>K4. This independently accepts B17-KB5-CUTOFF@1 without a finite-to-universal inference.

Our six-bit reconstruction has negative assignments {0,1,2,4,8,16,32,6,17,40}. Every coordinate ratio is certified >368/125>K5. Thus even the newer five-bit maximum is already an invalid all-dimensional constant. This is a finite scope obstruction, not unbounded H/I or a disproof of FEI.

For A071's newer five-bit certificate, W/2 has integer squares of total 256. We independently enclose every one of its 289 lookup entries G(a^2,b^2), 0<=a,b<=16, and prove its stored 40-bit upper integer bounds the true packet. Zero packets are exactly zero. The seed lower integer 2964159675584/2^40 is strictly below independently certified K5. Positive-denominator quotient ceilings preserve the upper ratio bound; taking the minimum of the coordinate upper bounds is valid for existential selection.

Each lookup entry is at most 512*2^40+1, because packet entropy <=a^2+b^2<=512 even for unrealizable table entries. Sixteen packets plus quotient-ceiling adjustment are at most 9007199254741264, well below 2^63. These integers can exceed the exact-double 2^53 threshold; the source keeps them as int64, so this creates no precision failure. Only floats printed for display are used.

Coverage filters commute in the required direction: output complement makes a nonempty minority support of size <=16; coordinate permutation orders its physical influences; translation preserves that ordered influence vector and can anchor a negative point at zero; choosing the least anchored translation preserves both properties. These are covering filters, not unique orbit labels. Bit swaps in the uint32 translation code are permutation of the 32 physical assignment bits; the masks retain both swapped halves. Enumeration uses uint64 arange before the safe uint32 cast and stops at 2^32, excluding that endpoint, so the last odd mask is 2^32-1 and no wrap introduces or drops a mask. There is no affine coordinate mixing.

The 640 five-bit extrema are exactly 32*C(5,2)*2; unique center proves no double count. A071 and A082's full independent runs both report 5,778,648 representatives and the same little-endian stream hash ac010403c1e2e329262b930668c4d34bf548c862cad687ebd9210579dd0c233b. We check these two saved artifacts agree but do not rerun their 2^31-mask census. Source/lookup/coverage audit HOLDS. The all-dimensional extrapolation remains unsupported and, at this exact constant, is explicitly refuted by the six-bit witness.

## executed validation with domain, arithmetic, commands and outputs

Frozen before jobs: FROZEN_SPEC.json and targeted RECHECK_SPEC.json. Commands from A085:

    python -X utf8 -u runs/20261013T213517Z-account05-A085-certificate-adversary/code/audit.py pilot
    python -X utf8 -u runs/20261013T213517Z-account05-A085-certificate-adversary/code/audit.py screen
    python -X utf8 -u runs/20261013T213517Z-account05-A085-certificate-adversary/code/audit.py math
    python -X utf8 -u runs/20261013T213517Z-account05-A085-certificate-adversary/code/audit.py recheck
    python -X utf8 -u runs/20261013T213517Z-account05-A085-certificate-adversary/code/finalize.py

Pilot: 54-prime screen audit, 167 exact counted checks, 0.1832 seconds. Main screen audit: 600 source log constants and 599 deterministic prefix tests, 2,402 checks, 25.1511 seconds. Mathematical audit: five named Boolean witnesses, orbit generation, 289 upper lookups and integer bounds, 563 checks, 0.1281 seconds. Final 130-column failure and fallback reproduction: 291 checks, 0.5113 seconds. NumPy version is 2.4.3. Timings are observed script runtimes, not billing/capacity claims.

An auxiliary first recheck incorrectly assumed that all low-order convergents would be undecided by the screen; some are correctly decided. The assertion was corrected to require either the independently correct sign or an undecided result, plus at least three actual undecided fallbacks. The original bound violation was already certified and unchanged. out/attempt_history.json records that local harness correction. This is not a failure of the mathematical certificate or a source repair.

Every exact claim uses integer Walsh/edge arithmetic, prime exponent forms, or rational log intervals. Logs independently use 64 positive atanh terms with floor/ceil error at scale 2^192, then divide the nonnegative reduced-log interval by positive ln2 before adding a signed integer exponent. Binary64 is used only to execute the implementation under test and is converted back to an exact rational for certification. No library logarithm decides a sign. Memory estimated <=100 MB, not measured; no job over 300 MB, no heavy job, no GPU, no automatic dimension escalation, no full census rerun and no outside write. Each discovered failure and completed mathematical batch was persisted immediately.

## proof dependencies and changed downstream conclusions

New narrow audit claim A085-CERTLOG-GENERAL-ERROR-BOUND-FAILURE@1 refutes only the helper's documented error budget and supplies a safe intended-domain replacement. B17-KB5-CUTOFF@1 receives an independent scoped acceptance preserving its original statement, hash and contributors. B17-KB4-CENSUS@1 receives a source-logic/range/orbit verdict with the explicit no-full-rerun limitation. A071-EXACT-FIVEBIT-ERASURE-SELECTION@1 receives a lookup/coverage audit corroborating A082's already completed independent full replay; it is not counted as a third full replay. No existing finite maximum or constant requires invalidation.

The new helper repair is an A085 contribution; A085 cannot independently approve a corrected helper version it contributes. A090/A094 should review it. Elementary entropy identities, character orthogonality, positive-series remainders, unique prime factorization and the elementary floating rounding-factor estimate are the proof inputs. Dependencies are source-bound and do not assume FEI or a universal stopping-tree theorem. Shared registries and original code remain unchanged. B20 should attach the source-hash-bound correction to consumers of the generic 600-term error claim; neither archive receipt nor local status establishes downstream adoption.

## one next mathematical action and independent reviewer

A090 primary/A094 alternate should reconstruct the 130-column error certificate and eta_m proof. B17 can correct the helper's general documentation to 2^-43 S on the explicitly matching <=600-prime integer domain while retaining its 2^-40 S threshold, or enforce a stronger reduction/layout contract with a proved bound. The next mathematical audit is a concrete A097/A064/A099 terminal-inclusive stopping certificate with affine-five leaves, checking the cumulative signed residual against one nonreused coordinate budget. This consumes the now audited finite leaf constants without attempting a larger census.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved in the assigned stage directory, along with CERTIFICATE_ADVERSARY.md, CERTIFICATE_FAILURE.json, frozen specs, scripts and exact outputs. Finalizer checks exact protocol field sets, preserved original hashes, nonempty certified intervals, strict error violation, orbit sets, finite-source hash agreement, local artifact sizes <20 MB and SHA256 readback. out/validation.json and out/manifest.json are the local receipts. STATUS.md is two lines, WORKLOG.md appends the dated stage and LEARNED.md retains prior lessons plus this failure and repair. Original source trees were read only. Independent review of the new audit claim, supervisor copy, brain ingestion, mirror verification and downstream helper correction remain unverified.

## Universal bridge

This stage moves the B17 certificate gate adjacent to C018 erasure selection and C019 certified terminal payment: it closes the numerical-screen, integer-range and orbit-scope audit for the named finite certificates, with one concrete 130-term helper-contract failure and a proof that all existing finite decisions remain safe. It adds no universal FEI constant; the six-bit witness still excludes the five-bit constant and no finite census pays unrestricted path debt. The unpaid step is a terminal-inclusive, nonreusing influence payment transporting arbitrary residuals into the certified leaves. NEXT audits that precise live stopping residual using the surviving constants, because the numerical gate is now resolved and repeating another finite extremum would leave the same universal obligation untouched.
