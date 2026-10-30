# A032 stage2: sharp six-variable two-address endpoint

## exact target, quantifiers, hypotheses and units

For every uniform Boolean F on six physical coordinates, with a distinguished pair of addresses A such that every positive-mass conditional spectral law of the other four coordinates given the address label is product, decide whether H/I can exceed Cstar=16/3-(3/2)log2(3). Result: it cannot. Exact complete admission and an objective certificate prove H<=Cstar I, and an embedded three-variable point defect attains equality. Coordinate permutation and dummy padding give the same bound for all functions on at most six variables in the class. H is in bits and I is physical total influence. Full FEI and the all-dimensional two-address class remain OPEN.

## sources actually read, revisions and theorem locators

BOARD.md snapshot23:39UTC and B07 STREAM_NOTES v2 dated23:45UTC were read at stage start, as were own STATUS/LEARNED. The lead accepted stage1's ten-atom/count/admission results and directed A032 to a six-variable search, pure configurations first; the benchmark is now the three-variable point defect, not40/17. The lead CLAIMS.json and conditional-product/slice-census code were read. A088's complete REPORT independently accepts the previous A032 admission at stated scope; A034's complete REPORT identifies the genuine phase/tensor/vacuous-embedding limitations. EXECUTION_PROTOCOL revision2026-10-11-execution-v2 was read in full in stage1 and its schema remains in force. Stage1's paper/context reading is not repeated or relabelled as a new full-paper audit. Exact source hashes and reading scopes are in out/SOURCE_RECEIPTS.json. The new proof and witness need no unreviewed campaign claim as premise; the point-defect benchmark is independently reconstructed below. No novelty claim is made.

## complete derivation or exact first unsupported line

COMPLETENESS.md proves the finite product-amplitude template reduction, translation/global-sign gauge and objective-preserving slice/cover compression. MIXED_COMPLETENESS.md proves the complete pointwise phase admission: writing h_J=2g_J, each physical data point has either one occupied+/-2 slice, or four occupied+/-1 slices whose signs have negative product. The common mixed mask M must agree in all four rows; outside M the occupied pure masks partition its complement. The exact XOR of row sign masks on M must be0 or M modulo global row signs. This is joint Boolean admission, not independent sign partitions.

Every integer product-amplitude row factors as c times products of primitive coprime ratio factors; the inverse range forces c|32, coefficient magnitude<=32, norm<=1024 and norm divisible16. All coordinate faces and all permitted ratios/scales/phases are exhausted. Every active translation is restored. A pair is compressed only when pure union, common phase XOR, two norms and entropy signature agree; then minimum data influence preserves realizability and can only improve the objective. Address masses are actually assigned to label weights0,1,1,2 in descending order, minimizing physical influence over valid label assignments.

Pure configurations (M=0) have H/I<=12/5 through six variables, attained by a three-cell selector with masses1/2,1/4,1/4. All-mixed configurations (M=all points) have H<=2I in every dimension: h_J is then Boolean with product spectrum, so primitive norm arithmetic forces fair/deterministic spectral marginals, and H(F)=2+avg H(h_J)<=2[1+avg I(h_J)]. The remaining690 masks are completely searched and reduce to68 objective signatures. Exact rational logarithm bounds show67 strictly below Cstar and one exactly equal. This closes the full n=6 target, not just the pure search.

The maximizer truth table is in out/maximizer_truth_table.json. It has I=3/4, H=4-(9/8)log2(3), hence H/I=Cstar. All64 inverse signs, direct integer Fourier coefficients, conditional product laws and physical-edge influence are checked exactly. We do not claim a uniqueness classification of extremizers or a census of all labelled functions.

NON_BOOLEAN_CONTROL.md gives a normalized product-amplitude polynomial on the same six-bit domain with spectral marginals1/16. Its conditional spectra are product but H/I>4>Cstar, and its all-positive physical value exceeds1. Thus the decisive pointwise common-phase admission genuinely excludes a non-Boolean relaxation.

First unsupported universal line: a dimension-independent bound on realizable heavy rows, for example sum_J w_J N_J<=K[H(w)+E|J|] with N_J counting nonfair nondeterministic row marginals, followed by payment of every retained address/conditional entropy term using physical influence. No such all-dimensional lemma is established by this finite certificate. No automatic n=7 escalation is made.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs SEARCH_SPEC, MIXED_SPEC, MIXED_SPEC_V2, MIXED_RESUME_SPEC and VERIFY_SPEC precede their corresponding jobs. Commands from this run directory:

    python -X utf8 code/pure_product.py --m 1 2 3 --seconds 60
    python -X utf8 code/pure_product.py --m 4 --seconds 180
    python -X utf8 code/cover_search.py --m 1 2 3 4 --seconds 180
    python -X utf8 code/certify_pure.py
    python -X utf8 code/mixed_product.py
    python -X utf8 code/mixed_cover.py
    python -X utf8 code/mixed_cover.py --resume
    python -X utf8 code/verify_slices.py
    python -X utf8 code/certify_full.py

The option spellings above use actual separate arguments (--seconds 60 and --seconds 180); output files retain all observed counts and times. Pure m=4:851 magnitude templates,58880 gauge phases,475 objective-preserving records,6872 unordered covers,17 objective signatures. Its generator took1.032seconds and covers0.164seconds. Full five-valued slice generator v2:4820 templates,508384 gauge phases,45088 signed rows modulo global sign,692 mixed-mask groups;6.476seconds. The first combination job reached671 of690 nontrivial masks at180.223seconds and saved its checkpoint; a separate frozen12.247-second resume completed the remaining19. Counts of complementary-pair matches are implementation diagnostics and may include repeated partial-mask work; they are not counts of Boolean functions. All690 completed-mask records and all68 objective signatures are durable.

The scalar mixed generator v1 hit its180-second limit without producing a complete mixed result. It was replaced by exact batched16-column int64 transforms on the same domain; each intermediate magnitude is<=512, so overflow/rounding cannot occur. One initial v2 invocation hit a variable-name collision and was corrected before the successful run. Failures are saved in out/MIXED_V1_FAILURE.md and out/VALIDATION_RUNTIME_NOTE.md.

Separate direct character sums verified every45088 catalogue row, all exact product identities, histograms and influences. A streaming exhaustive pilot checked all390625 three-bit five-valued vectors, found2208 nonzero product-spectrum rows including global signs, and confirmed their lifts are present in the four-bit catalogue. The pilot took6.582seconds. Direct catalogue reconstruction took141.544seconds, exceeding its estimated60-second verification budget; that overrun is explicitly recorded and the frozen estimate is preserved. It stayed within the protocol30-minute job cap. Mathematical checks were not repeated to manufacture a shorter time. Estimated memory stayed below200MB; no job expected to exceed300MB, no memok-triggering heavy allocation, no background job, window, GPU or dimension escalation.

Entropy proofs use Python integer prime-log signatures and Fraction intervals: reduce log arguments to[1,2], retain32 terms of the atanh series and bound the positive tail explicitly, then use signed interval arithmetic with positive ln2 denominators. Floating/Decimal scores only select candidates; all final inequalities are certified. For Cstar I-H, all but one signature have strictly positive lower margin; the sole remaining signature cancels exactly. out/full_exact_certificate.json includes all per-signature certificates. These are author checks in different representations, not external independent acceptance.

## proof dependencies and changed downstream conclusions

The proof is self-contained finite Fourier algebra, elementary gcd/parity arithmetic, exhaustive exact admission and rational logarithm certification. Stage1's acceptance by A088 and the lead is recorded as prior review, not permission to infer a new universal bound. The lead's N<=5 endpoint is extended toN<=6 with the same sharp constant. The old40/17 construction remains a valid pure counterexample to constant2, but pure search cannot beat the current2.9559 benchmark atN<=6 because its sharp constant is12/5. A034/A079 must now target the common mixed-mask/heavy-row constraint in growing data dimension; address entropy and arbitrary-tensor/vacuous embeddings remain mandatory. No central registry, other-agent file or shared source was modified.

## one next mathematical action and independent reviewer

Use this complete common-phase catalogue to falsify or support one frozen all-dimensional heavy-row admission inequality controlling sum_J w_J N_J by H(w)+E|J|. Explicitly retain all address entropy and conditional-row entropy in its FEI implication, and test the normalized non-Boolean control and tensor/vacuous-embedding guards. This targets the first unsupported phase-payment line rather than another dimension census. Independent reviewers: A088 and A094, with B07 lead as consumer. No messages were sent; handoffs are saved for supervisor collection.

## actual persistence receipts or precise save blocker

All four protocol files, Boolean witness, complete catalogue, objective certificates, proof notes, frozen specs and reproducible code are saved in this A032 run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. out/ARTIFACT_RECEIPTS.json stores local hashes and sizes; out/SCHEMA_CHECK.json checks exact field sets, compatibility delta and certificate/witness statuses. Every file is below20MB. No save blocker remains. GitHub copy, Brain ingestion, mirror verification, external review, registry adoption and public release are not claimed. All writes remained inside A032; no git, external messaging or brain writes occurred.

Universal bridge: This stage advances B07's G-PHASE-COND realizability/payment target by completely closing the six-variable two-address endpoint at sharp Cstar, certifying the smaller pure endpoint12/5, and proving the all-mixed2 bound for every dimension. It adds no universal C018/C019/C020/C024 constant. What remains is an all-dimensional common-phase restriction on heavy nonfair rows and a complete physical-influence payment of the retained address/conditional entropy. Testing the proposed weighted nonfair-row admission against this exact mixed-mask catalogue is the shortest next route toward full FEI: it attacks the precise extra Boolean input needed for a reusable conditional phase payment and rejects phase-blind substitutes, while another finite dimension would only extend the census.
