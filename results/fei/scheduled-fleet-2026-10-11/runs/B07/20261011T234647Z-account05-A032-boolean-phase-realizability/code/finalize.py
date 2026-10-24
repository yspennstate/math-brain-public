import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];RUN=ROOT.name
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2),encoding='utf-8')
base=Path(r'~\brain_workers\FEI100_20261011')
canonical=Path(r'~\mop_fei100\reports\fei-2026-10-11')
lead=base/'claude'/'B07'/'runs'/'20261011T230024Z-claude-B07-two-address-census'
pins=[(base/'BOARD.md','Board snapshot at stage start23:39UTC; all stream entries inspected'),(base/'claude'/'B07'/'STREAM_NOTES.md','B07 v2 dated23:45UTC; full notes read'),(canonical/'EXECUTION_PROTOCOL.json','Protocol v2 fully read in stage1; unchanged schema reused'),(lead/'CLAIMS.json','Full source statements and exact proof locators read'),(lead/'code'/'b07_lead_checks.py','Conditional product test and finite slice-census code read'),(base/'agents'/'A034'/'runs'/'20261011T223816Z-account05-A034-phase-energy-transfer'/'REPORT.md','Full restricted theorem and admission/tensor guards read'),(base/'agents'/'A088'/'runs'/'20261011T223053Z-account05-A088-booleanity-referee'/'REPORT.md','Full independent review report read; accepted stage1 A032 scope recorded')]
dump('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'reading_scope':scope} for p,scope in pins])
pure=json.loads((ROOT/'out'/'pure_exact_certificate.json').read_text())
full=json.loads((ROOT/'out'/'full_exact_certificate.json').read_text())
validation=json.loads((ROOT/'out'/'slice_direct_verification.json').read_text())
catalogue=json.loads((ROOT/'out'/'mixed_slices_m4.json').read_text())
covers=json.loads((ROOT/'out'/'mixed_cover_results.json').read_text())
assert full['status']==validation['status']=='PASS' and catalogue['status']==covers['status']=='COMPLETE'
dump('BOOLEAN_REALIZABILITY.json',{'schema':'A032-two-address-n6/1','status':'EXACT_FINITE_TARGET_CLOSED_PENDING_REVIEW','bound':'Cstar=16/3-(3/2)log2(3)','pure_bound':'12/5','all_mixed_bound':'2','nontrivial_mixed_masks_completed':len(covers['groups_completed']),'slice_records':catalogue['slice_records_mod_global_sign'],'full_certificate':'out/full_exact_certificate.json','actual_boolean_witness':'out/maximizer_truth_table.json','mathematical_frontier':'all-dimensional heavy-row/common-phase payment remains open'})
statement='For every Boolean function F on at most six independent uniform physical bits and every distinguished pair A of bits such that each positive-probability conditional spectral law of S_(A^c) given S_A is a product law, H(F)<=Cstar I(F), where Cstar=16/3-(3/2)log2(3). The constant is attained by a three-variable point defect containing both addresses, with remaining coordinates dummy. On the subclass in which every physical data point has exactly one nonzero partial address Fourier slice (pure configurations), H(F)<=12I(F)/5, attained with four essential variables. On the subclass with all four slices of magnitude1/2 at every data point, H(F)<=2I(F) in every data dimension. A normalized non-Boolean product spectrum with six marginals1/16 has H/I>4, so the finite Boolean bound is not generic probability algebra.'
claim={'claim_id':'A032-TWO-ADDRESS-N6-CERTIFICATE','version':1,'exact_statement':statement,'hypotheses':['F is a real Boolean sign on a finite uniform physical cube','A consists of two distinct physical coordinates','Conditional squared Fourier spectra are product laws; zero-mass address labels omitted','Full finite bound requires at most six variables; the all-mixed bound is explicitly dimension-independent','H is in bits; I is total physical influence, equivalently expected spectral degree'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A032'],'proof_source':['COMPLETENESS.md','MIXED_COMPLETENESS.md','NON_BOOLEAN_CONTROL.md','code/pure_product.py','code/mixed_product.py','code/mixed_cover.py','code/certify_full.py','out/pure_exact_certificate.json','out/full_exact_certificate.json','out/maximizer_truth_table.json'],'proof_dependencies':[],'review_records':[{'reviewer':'A032 author','method':'Independent direct character-sum validation of45088 rows, exhaustive5^8 slice pilot with2208 product slices lifted, physical-edge influence and direct full64-entry truth table reconstruction','verdict':'PASS; external independent review not yet performed'}],'status':'EXACTLY_CERTIFIED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A031','A033','A034','A035','A078','A079','A088','A094','B07-lead']}
dump('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B07','packet_id':'A032','gap_id':'G-PHASE-COND','attempt_id':'A032-TWO-ADDRESS-N6-02','method':'Complete product-amplitude slice admission with coupled five-valued phase compatibility; objective-preserving complementary-pair search; rational logarithm certificates','mathematical_delta':'The six-variable two-address conditional-product class has sharp constant16/3-(3/2)log2(3), extending the lead N<=5 endpoint. Pure configurations have sharp12/5 through six variables, all-mixed configurations obey2 in every dimension, and the normalized non-Boolean product control violates the finite bound. No all-dimensional two-address or FEI bound is proved.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'N6_ENDPOINT_CLOSED; ALL_DIMENSIONAL_G-PHASE-COND_AND_FULL_FEI_OPEN; REVIEW_PENDING','claim_versions_used':[],'claims_created_or_changed':['A032-TWO-ADDRESS-N6-CERTIFICATE@1'],'source_artifacts':['REPORT.md','CLAIMS.json','BOOLEAN_REALIZABILITY.json','COMPLETENESS.md','MIXED_COMPLETENESS.md','NON_BOOLEAN_CONTROL.md','SEARCH_SPEC.json','MIXED_SPEC.json','MIXED_SPEC_V2.json','MIXED_RESUME_SPEC.json','VERIFY_SPEC.json','out/full_exact_certificate.json','out/maximizer_truth_table.json','out/mixed_slices_m4.json','out/mixed_cover_results.json','out/slice_direct_verification.json','out/SOURCE_RECEIPTS.json','out/VALIDATION_RUNTIME_NOTE.md'],'next_consumers':['A034','A035','A079','A088','A094','B07-lead'],'next_action':'Use the complete n=6 common-mixed-mask catalogue to test a dimension-independent heavy-row admission lemma controlling sum_J w_J N_J by H(w)+E|J|, where N_J counts nonfair nondeterministic spectral marginals; retain address entropy, full conditional entropy and the tensor/vacuous-embedding guards. Do not automatically enumerate n=7.','stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A032']}
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)
report='''# A032 stage2: sharp six-variable two-address endpoint

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

    python -X utf8 code/pure_product.py --m 1 2 3 --seconds60
    python -X utf8 code/pure_product.py --m 4 --seconds180
    python -X utf8 code/cover_search.py --m 1 2 3 4 --seconds180
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
'''
# Preserve literal executable command spacing in the report.
report=report.replace('--seconds60','--seconds 60').replace('--seconds180','--seconds 180')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A032 stage2 complete: sharp two-address conditional-product constantCstar=16/3-(3/2)log2(3) certified through six variables; pure12/5; full common phases checked; review pending; full FEI OPEN.\nNEXT: A088/A094 review; test a dimension-independent weighted nonfair-row admission on the complete mixed-mask catalogue, retaining address/conditional entropy and tensor/vacuous guards.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+': Stage2 completed. Mixed v2 admitted45088 product rows;690 nontrivial masks complete after checkpointed180.223s job plus12.247s resume. All68 objectives exactly certified below/equalCstar;64-entry maximizer direct Walsh/physical influence PASS. Catalogue verification141.544s exceeded its estimated60s (recorded), independent5^8 pilot6.582s PASS. One new bundled finite claim saved, external review pending; no universal FEI conclusion.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''

## Stage2: two-address admission

- Lead/A088 independently accepted stage1 admission at stated scope; no need to repeat it. Current two-address benchmark is the3-bit defect Cstar=16/3-(3/2)log2(3), not40/17.
- Exact finite result: every two-address conditional-product Boolean function on at most6 bits obeysH<=Cstar I; equality is attained. Pure configurations instead have sharp12/5 through6 bits. All-mixed configurations haveH<=2I in every dimension.
- Pointwise address admission: h_J=2g_J must be either a single occupied+/-2 or four occupied+/-1 with negative product. The common mixed mask must coincide across rows; its joint sign XOR is constant modulo globals. Separate row admission is not enough.
- Integer product-spectrum slices have magnitudes c times primitive pair products. For five-valued integer h, c divides2P, max coefficient<=2P and norm<=4P^2. Gauge origin/basis phases by physical translation plus global sign, then restore every translation. This gives a complete small-rank template engine without5^16 brute force.
- n=6 catalogue:45088 rows modulo global sign,692 masks (690 nontrivial),68 objective signatures;67 strict and one exact benchmark equality. Different direct transforms and5^8 pilot validate the engine. No uniqueness or full truth-function count is claimed.
- A normalized six-bit product spectrum with marginal1/16 hasH/I>4 despite all conditional laws being product; its inverse is not Boolean. Common five-valued phase admission is essential.
- Scalar v1 timed out; batched tiny int64 transforms reduced the same domain to6.476s. Checkpoint complementary-pair jobs by completed mask. Preserve budget overruns honestly: direct validation took141.544s against an estimated60s; mathematical result remains checked, no rerun solely for runtime.
- NEXT is a genuinely Boolean all-dimensional heavy-row admission/payment with address and conditional entropy retained; a seventh-variable census would not itself close the universal bridge.
''')
protocol=json.loads((canonical/'EXECUTION_PROTOCOL.json').read_text())
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
dump('out/SCHEMA_CHECK.json',{'status':'PASS','progress_fields':'exact, descriptive packet_ids suffix normalized','claim_fields':'exact','packet_delta':'identical','full_certificate':'PASS','maximizer':'EXACT_BOOLEAN_AND_RATIO_VERIFIED'})
receipts=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']
assert all(row['bytes']<20_000_000 for row in receipts)
dump('out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED','run':str(ROOT),'files':len(receipts),'max_file_bytes':max(row['bytes'] for row in receipts),'mathematical_status':'N6_SHARP_ENDPOINT_CLOSED; FULL_FEI_OPEN'}))
