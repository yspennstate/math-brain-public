from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];TEAM=AGENT.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def write(p,s):p.write_text(s,encoding='utf-8')
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=json.loads((RUN/'out'/'CHECK.json').read_text(encoding='utf-8'))
data=json.loads((RUN/'out'/'DATA_CHECK.json').read_text(encoding='utf-8'))
pilot=json.loads((RUN/'out'/'PILOT.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and check['cases']==546
assert data['status']=='PASS' and data['data_queries']==804 and data['controller_continuations']==2
assert pilot['nodes']>0
statement=('For any actual uniform Boolean controller-only stopping tree whose Fourier-square laws at every node factor as p_v(c,u,z)=pbar_v(c,u)k(z|u) with one fixed normalized conditional kernel k, and whose complete references use that same k, every actual controller entropy decrement, physical queried influence, conditional-erasure KL, branch-outcome KL and signed Bayes-to-chosen-child reset equals its quotient counterpart. Full cross-entropy is quotient cross-entropy plus L_v=E H(k(.|U)); L_root=E L_leaf, so all terminal spectator entropy is retained once. A previously certified quotient controller price transfers unchanged, without asserting the quotient spectra are Boolean. Matching source/reference conditionals is necessary and sufficient for zero omitted conditional KL. Common independent Boolean factors in every core including fallback satisfy the hypothesis; a certified factor entropy/influence bill is charged once. At any fresh uniform query outside spectator block Z, DeltaL=I(branch;S_Z|T)-I(S_i;S_Z|T), hence [DeltaL]_+<=2 Inf_i(f)/ln(2). If source/reference likelihood p/q is a positive function of retained quotient frequency T on their whole support, actual coherent transport produces Bayes children with matching conditional spectator laws and no extra conditional KL reset; the quotient reset and terminal debts remain. The actual first-data-query h3 example has correction 1-(3/8)log2(3)>0, so unchanged controller cancellation does not extend to arbitrary data queries. Full FEI and arbitrary nonmatching conditional-reference payment remain open.')
hyp=['Actual Boolean sign on a finite independent uniform cube; entropy/KL bits',
     'Fresh deterministic singleton tree and original ambient coordinate labels; all terminal functions retained',
     'Controller-only transfer requires one hereditary actual conditional spectral kernel k(z|u), normalized on source/reference rows',
     'Every chosen full reference is the normalized quotient reference lifted by that same k, with source dominated by reference',
     'Quotient price transfer requires its own valid certificate; quotient marginals are not automatically Boolean',
     'Data-query KL extension additionally requires retained-frequency measurable likelihood ratio; the entropy-drift bound itself does not']
claim={'claim_id':'A050-COMMON-CONDITIONAL-KERNEL-REPAIR','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A050'],
 'proof_source':['PROOF.md','code/check.py','out/CHECK.json','out/FIXTURES.json','code/data_query.py','out/DATA_CHECK.json'],
 'proof_dependencies':[],'review_records':[],'status':'SCOPED_SIGNED_REFERENCE_REPAIR_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING',
 'supersedes':[],'refutes':['Exploratory extension of fixed-spectator entropy cancellation unchanged through an arbitrary data query'],
 'first_unproved_line':'Without retained-frequency likelihood sufficiency, pay changed conditional-reference reset and the certified quotient/core decrement with both full terminal profiles from one unused signed child/control budget.',
 'next_consumers':['A048','A092','A038','A039','A064','A091','A087','B10','B20']}
js(RUN/'CLAIMS.json',[claim])
write(RUN/'out'/'STATUS_BEFORE.txt',(AGENT/'STATUS.md').read_text(encoding='utf-8'))
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B10'/'STREAM_NOTES.md',
 AGENT/'runs'/'20261014T004109Z-fleet05-A050-repair-with-scope'/'PROOF.md',
 AGENT/'runs'/'20261014T004109Z-fleet05-A050-repair-with-scope'/'code'/'check.py',
 TEAM/'agents'/'A048'/'runs'/'20261014T022727Z-fleet05-A048-tensor-stress'/'REPORT.md',
 TEAM/'agents'/'A048'/'runs'/'20261014T022727Z-fleet05-A048-tensor-stress'/'PROOF.md',
 TEAM/'agents'/'A048'/'runs'/'20261014T022727Z-fleet05-A048-tensor-stress'/'CLAIMS.json',
 TEAM/'agents'/'A092'/'runs'/'20261014T020903Z-fleet05-A092-counterexample-referee'/'REPORT.md',
 TEAM/'agents'/'A092'/'runs'/'20261014T020903Z-fleet05-A092-counterexample-referee'/'PROOF.md',
 TEAM/'agents'/'A092'/'runs'/'20261014T020903Z-fleet05-A092-counterexample-referee'/'CLAIMS.json',
 TEAM/'agents'/'A047'/'runs'/'20261014T015314Z-fleet05-A047-boundary-search'/'PROOF.md',
 TEAM/'agents'/'A038'/'runs'/'20261014T022516Z-fleet05-A038-occupancy-term-audit'/'REPORT.md',
 TEAM/'agents'/'A039'/'runs'/'20261014T025407Z-fleet05-A039-projection-under-restrictions'/'REPORT.md']
js(RUN/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
report=f'''# A050 stage 4: common conditional-kernel repair, then one data query

## exact target, quantifiers, hypotheses and units

Repair the signed common-row reference interface exposed by A048's common-factor labelled-reserve obstruction and A092's zero-injection bank obstruction. Uniform actual Boolean signs, complete normalized Fourier references, Shannon bits and physical influence. Fresh deterministic stopping trees, original labels, actual nonconstant terminals. This is a scoped repair of a failed interface, not a new broad FEI potential. Full FEI remains OPEN.

Hypothesis: along a controller prefix, actual p_v(c,u,z) and every reference q_v(c,u,z) share ONE fixed conditional spectator law k(z|u). This preserves normalized controller/KL accounting at the quotient's exact price. The necessary-and-sufficient reference-level zero-correction condition is agreement of source/reference conditional laws; the hereditary fixed-k condition is a sufficient tree hypothesis. A first data query can change k: its positive entropy drift is universally <=2 Inf_i/ln(2). Its conditional KL transport is closed under the additional retained-frequency likelihood-ratio condition. The quotient needs its own certificate; no Boolean quotient is assumed.

## sources actually read, revisions and theorem locators

BOARD read at entry, supervisor 2026-10-14 03:35 UTC, full unchanged B10 lead notes v2 2026-10-11 23:31Z, and own STATUS. Full protocol execution-v2 was reread. Prior campaign/registry/paper context remains prior-stage provenance; no new literature theorem is used. The lead's original essential-bias tax task was completed earlier; dispatch consumes useful new objections rather than repeats that retired mechanism. No disagreement with its scoped-repair direction.

New sources: A048 run 20261014T022727Z REPORT/PROOF/CLAIMS, especially common-factor sensitivity and signed cancellation; A092 run 20261014T020903Z REPORT/PROOF/CLAIMS, especially its prescribed witness bank and retained residual; A047 run 20261014T015314Z PROOF, coordinate-resolved deletion and remaining bank gap; A038 run 20261014T022516Z REPORT and A039 run 20261014T025407Z REPORT, owned reset and rare-family projection deficit. Actual source bytes are hashed in out/SOURCE_RECEIPTS.json. Own previous exact log primitives are reused transparently; no peer checker is replayed. A048/A092 export independent unchanged acceptance of A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1. No old run or shared registry is rewritten.

## complete derivation or exact first unsupported line

PROOF Sections 1-3 give the complete normalized conditional-kernel/KL chain, source/reference support conventions, actual coherent branch kernel, signed reset identity, and terminal entropy martingale. Controller entropy, erased information, branch KL, reset and cross-entropy increments equal quotient increments exactly. The same conditional spectator entropy is carried to terminals once. A common physical factor in EVERY branch, including fallback, is a useful sufficient condition. Section 4 states admitted and excluded intended applications; Section 5 gives the actual first-data-query failure of unchanged cancellation.

Section 6 proves DeltaL=I(branch;Z|T)-I(S_i;Z|T), hence its positive part <=2 Inf_i/ln(2). If p/q=r(T) on all source/reference rows, actual Bayes children retain the actual child conditional spectator law and incur no additional conditional KL reset. This permits an explicit data/controller continuation on h2(C)*h3(U,Z), with a nontrivial positive controller reference different from the source. Any valid quotient data-query rate K transfers at rate K+2/ln(2), charging that SAME query budget once. An arbitrary KL reset or an uncertified quotient bill is not paid by the entropy lemma.

Admitted: A048's y and y*h_n common-factor application, including fallback y; arbitrary common independent Boolean factors with their entire terminal entropy retained; controller-only conditional kernels that depend on retained U-frequency; row-collinear AND-sign shared cores that have no Boolean one-bit quotient. Known quotient class certificates transfer with no controller surcharge. Excluded: A092's +1/parity/AND branches under the tested data split, whose conditional spectator laws differ; arbitrary data exposure without the extra correction; and arbitrary post-exposure reference replacement without a sufficient likelihood ratio or an explicitly paid conditional KL. We do not restore standalone history-bank or labelled-release payment.

FIRST UNSUPPORTED universal line: without the retained-frequency likelihood condition, price the changed conditional-reference reset and the eligible quotient/core decrement jointly with both full terminals from one unused signed child/control budget. No universal FEI constant is improved by the scoped normalization theorem.

## executed validation with domain, arithmetic, commands and outputs

Controller spec out/FROZEN_SPEC.json was saved before search. Final helper v1.1; initial pilot selected constant quotient cores and had no controller nodes, so it was strengthened before the main run. Final pilot: 16 cases, 32 controller nodes, {pilot['assertions']:,} assertions PASS in {pilot['runtime_seconds']:.3f}s. Main: {check['cases']} cases, {check['nodes']} controller nodes, {check['assertions']:,} exact assertions PASS in {check['runtime_seconds']:.3f}s. Domain: all 16 ordered one-bit quotient-core pairs times all 16 two-bit Boolean spectators times two controller policies (512); m=1..3,n=1..5 common-factor families with character/AND-sign spectators (30); two admitted conditional-row examples; two boundary certificates. Largest materialized cube n=10, no symmetry reduction or automatic growth. Runtime cap 180s, memory estimate 100 MB.

Separately frozen out/DATA_QUERY_SPEC.json: all 278 Boolean tables through n=3 at each relevant dimension's selected coordinates (804 queries), plus two matched-reference post-data controller continuations at n=5. Pilot: 12 queries, 120 assertions PASS in 0.003s. Main: {data['data_queries']} data queries, {data['controller_continuations']} continuations, {data['assertions']:,} assertions PASS in {data['runtime_seconds']:.3f}s. This explicitly verifies positive entropy-drift payment and nontrivial zero conditional-reference reset. Runtime cap 60s, memory estimate 50 MB.

Commands from this run: `python -X utf8 code/check.py --pilot`; `python -X utf8 code/check.py`; `python -X utf8 code/data_query.py --pilot`; `python -X utf8 code/data_query.py`. Integer Walsh transforms and direct physical pivotal edges independently agree. Fraction arithmetic checks normalization, full/quotient spectra and references, both Bayes children, root/leaf KL and actual physical influences. Exact pointwise rational likelihood factorizations certify the KL chain; no floating equality or independence of log atoms is assumed. Integer-log vectors and directed rational atanh bounds certify entropy identities and JS signs. Strict first-data correction is 1-(3/8)log2(3)>0 by 3^3<2^8. All-dimensional statements follow from the analytic proof, not finite extrapolation. No job expected over 300 MB was launched, so no memok-gated job was necessary; peak memory was not measured. No GPU, background job or process was left running.

## proof dependencies and changed downstream conclusions

The new claim is self-contained in PROOF; proof_dependencies=[] because its normalization, chain, scalar JS and transport are rederived. A048-COMMON-FACTOR-LABEL-RESERVE-OBSTRUCTION@1 and A092's prescribed-bank audit identify failed application targets, not premises supplying a universal payment. Their full tensor/ownership interfaces are not independently accepted by this stage. A047's product extension is context only; this theorem remains uniform. Previous active-label repair is observed accepted at scope, with no enlarged bank claim.

Downstream substitution: common-factor overlap does not invalidate a controller theorem if its complete reference shares the actual common conditional kernel. Carry factor entropy once and preserve signed resets. After a data query, pay only the positive conditional-entropy change at <=2/ln(2) per unit queried influence; test retained-frequency likelihood sufficiency before calling the child reference inherited. If that test fails, retain the conditional KL as a named unpaid debt. Do not replace it by a labelled variance release, a root occupancy amount or a standalone history bank.

## one next mathematical action and independent reviewer

NEXT: on A038/A039's actual exposed priority query where retained-frequency likelihood sufficiency fails, compute the exact conditional-kernel KL remaining after the paid entropy drift, and charge it to one certified signed child/core slack while retaining both terminal profiles. Primary reviewer A092, alternate A048; A038/A039/A064/A091 consume the source-compatible substitution. No messages sent; source-bound local handoffs only.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS, identical PACKET_DELTA, PROOF, code and both frozen validation outputs are saved here. STATUS remains two lines; WORKLOG/LEARNED append this stage. out/ARTIFACT_RECEIPTS.json records actual local hashes/sizes, including rolling files. All files below 20 MB. Schema fields and compatibility equality are checked during finalization. Local save complete; independent review, supervisor mirroring and downstream use remain unverified.

Universal bridge: This stage advances C024 history transfer and C019 stopping-tree payment by closing common-conditional-kernel controller transport at zero extra controller price, retaining all spectator/terminal entropy exactly once, and paying a first data query's positive conditional-entropy drift at 2/ln(2) times its physical influence. Under retained-frequency likelihood sufficiency it also closes the extra conditional KL reset, including an actual data/controller continuation. The remaining bridge is the nonmatching conditional-reference KL plus eligible quotient/core terminal payment from one signed exclusive reserve. NEXT addresses that precise missing term on the existing exposed-priority objection rather than counting a new tensor class or retrying the already false separate-bank payment.
'''
write(RUN/'REPORT.md',report)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B10','packet_id':'A050',
 'gap_id':'C024-SIGNED-COMMON-ROW-REFERENCE-TRANSFER','attempt_id':'A050-stage4-conditional-kernel-and-first-data-query',
 'method':'Normalized common conditional spectral kernel; exact signed Bayes/reset transport; paid conditional entropy drift; retained-frequency likelihood criterion',
 'mathematical_delta':'Controller full/quotient accounts equal under hereditary matched conditional kernel; actual data-query positive entropy drift <=2 Inf/ln2; sufficient retained-frequency likelihood ratio yields no extra conditional KL; full terminal entropy preserved once.',
 'deliverable_status':'COMPLETE_LOCAL_SAVE_REVIEW_PENDING','mathematical_status':'SCOPED_REPAIR_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':['A048-COMMON-FACTOR-LABEL-RESERVE-OBSTRUCTION@1 (objection consumed)','A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1 (prior accepted scope)'],
 'claims_created_or_changed':['A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1'],
 'source_artifacts':['PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/FIXTURES.json','out/DATA_QUERY_SPEC.json','code/data_query.py','out/DATA_CHECK.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Price remaining conditional-kernel KL on A038/A039 exposed priority query from one certified unused signed child/core slack; preserve both complete terminals; A092/A048 review.',
 'stagnant_substantive_attempts':0,
 'blockers':['Nonmatching conditional-reference reset, quotient certificate eligibility and joint terminal/slack ownership remain universal gaps.','Independent review, mirrors and adoption pending.'],
 'packet_ids':['A050']}
js(RUN/'PROGRESS.json',progress);js(RUN/'PACKET_DELTA.json',progress)
write(AGENT/'STATUS.md','STATE: A050 stage4 proved matched conditional-kernel transport and paid positive data drift<=2 Inf/ln2; 546 controller cases + 804 data queries + 2 continuations PASS; review pending; FEI OPEN.\nNEXT: A092/A048 review; price nonmatching conditional-kernel KL on A038/A039 exposed priority query from one owned signed child slack with both terminals.\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{stamp} — Stage4 {RUN.name}: consumed A048 common-factor reserve and A092 zero-injection bank objections, preserving negative cancellation. Proved normalized matched conditional-kernel repair, necessary/sufficient zero conditional-KL criterion, same-price controller inheritance and one terminal spectator bill. First physical data query changes conditional entropy; proved positive drift<=2 Inf/ln2 and retained-frequency likelihood condition for zero extra Bayes conditional reset. Exact non-Boolean quotient caveat retained. Main {check["cases"]} cases/{check["assertions"]} assertions in {check["runtime_seconds"]:.3f}s; supplemental 804 queries +2 actual continuations/{data["assertions"]} assertions in {data["runtime_seconds"]:.3f}s PASS. Initial constant-core pilot strengthened to 32 actual controller nodes. No checker failed. Arbitrary changed conditional KL and eligible quotient/core payment remain open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('''\nStage4 durable repair: actual p_v(c,u,z)=pbar_v(c,u)k(z|u) and complete q_v=qbar_v k with one hereditary normalized k preserve every controller entropy/physical-influence/Bayes-erasure/outcome/signed-reset account exactly. CEfull=CEquot+E H(k), and that last bill is carried to terminals once. Common independent factors in EVERY branch including fallback satisfy the condition, with their own certified entropy/influence price; arbitrary shared-data +1/parity/AND branches do not. Quotient spectra can be non-Boolean, so require a real supplier certificate. At a fresh query outside Z, conditional spectator drift is I(branch;Z|T)-I(S_i;Z|T); its positive part<=2 Inf_i/ln2. This pays entropy, not arbitrary reset KL. If p/q=r(T) on all source/reference rows, inherited Bayes children match actual conditional spectator laws and extra conditional KL is zero; quotient reset/terminal debts remain. The h2-controller*h3-data matched-reference example realizes one data/controller continuation with nonzero source KL 4-log2(15), zero data erasure/outcome/reset, and full terminal bills. Unchanged cancellation at first h3 data query fails by exact positive correction 1-(3/8)log2(3). NEXT: nonmatching conditional KL from one owned signed child slack, not labelled reserve or standalone history-bank funding.\n''')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for title in protocol['required_per_run']['report_fields']:assert title in report
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']+[AGENT/x for x in ('STATUS.md','WORKLOG.md','LEARNED.md')]
for p in files:assert p.stat().st_size<20_000_000
js(RUN/'out'/'ARTIFACT_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)])
print(json.dumps({'status':'SAVED_SCHEMA_AND_HASH_CHECKED','controller_cases':check['cases'],'data_queries':data['data_queries'],'continuations':data['controller_continuations'],'files':len(files)}))
