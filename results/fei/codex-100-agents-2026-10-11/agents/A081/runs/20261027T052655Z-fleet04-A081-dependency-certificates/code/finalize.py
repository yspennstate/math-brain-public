from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];HOME=R.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
res=load(R/'out/EXACT_CERTIFICATE.json');val=load(R/'out/GRAPH_VALIDATION.json')
assert res['status']==val['status']=='PASS'
protocol=load(next((R/'out/intake').glob('*_EXECUTION_PROTOCOL.json')))
new=load(R/'out/NEW_NODES.json')
claims=[]
for n in new:
 c={k:n.get(k) for k in protocol['required_per_run']['claim_fields']}
 c.update(contributors=n.get('contributors',['A081']),proof_source=n.get('proof_source',n.get('proof_sources',[])),review_records=n.get('review_records',[]),supersedes=n.get('supersedes',[]),refutes=n.get('refutes',[]),next_consumers=['A011','A031','A085','A094','A099','A100','B17','B20'])
 # Graph hashes are explicitly statement-only; preserve typed original hashes there.
 claims.append(c)
save(R/'CLAIMS.json',claims)
next_action='A011/A050/A097/A099: construct a useful arbitrary-core original O(I) reference or fund required compatible admission from SAME unused original influence, retaining query KL, old U and all terminals. A085/A099 independently audit graph scope; A094 challenges local-floor payment.'
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-R-MISMATCH','attempt_id':'A081-resume-query-contraction-dependency-certificate','method':'Exact source-version split, complete finite-query divergence telescope, literal Boolean witness, rational prime-log replay and graph rejection fixtures',
 'mathematical_delta':f"Separated v5 terminal functional from full physical bill; pinned v6 inherited/vacuum repair and A031 exact-scope external review. {val['nodes']}-node DAG/{val['guard_count']} guards PASS; {res['assertions']} exact checks PASS. Universal supplier and local-floor query-loss payment remain OPEN.",
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'EXACT_ACCOUNTING_AUDIT_AND_CONDITIONAL_SCALAR_CERTIFICATE_FULL_FEI_OPEN',
 'claim_versions_used':['A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@5','A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@6','A094-A011-V5-PHYSICAL-QUERY-KL-LEDGER-GAP@1','A050-VACUUM-CALIBRATED-HEREDITARY-REFERENCE@1','A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT@1'],
 'claims_created_or_changed':[n['claim_id']+'@'+str(n['version']) for n in new],
 'source_artifacts':['REVIEW.md','PROOF_DEPENDENCIES.json','out/INTAKE_PINS.json','out/SOURCE_PINS.json','out/EXACT_CERTIFICATE.json','out/WITNESSES.json','out/GRAPH_VALIDATION.json','out/FROZEN_SPEC.json'],
 'next_consumers':['A011','A031','A050','A085','A094','A097','A099','A100','B17','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary-core initial influence-priced source or genuinely required compatible admission remains unproved','Original v5 rebuilt-local-floor physical-query contraction payment remains unpaid','A081 did not independently audit the whole v6 root envelope; separate A031 scoped review is pinned','Brain wake attachment lock timeout and stale context notes; affected notes not used as mathematical premises','Supervisor copying, canonical adoption, remote persistence and downstream use UNVERIFIED'],
 'packet_ids':['A081']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
formal=load(R/'out/FORMAL_STATUS.json') if (R/'out/FORMAL_STATUS.json').exists() else {'status':'NOT_RUN','reason':'No Lean certification claimed for graph/accounting audit'}
report=f'''# A081: dependency certificates after the physical-query correction

## exact target, quantifiers, hypotheses and units

Encode exact proof versions, hypotheses, source pins and unresolved leaves, and reject every proof cycle, including any passing through final FEI. The new mathematical audit concerns every finite fixed-target physical restriction tree with covering complete subprobability models of preserved mass s>0, actual signed same-target resets, full physical reaches, ghost mass and complete terminals. Information is in bits; influence is ordinary uniform-cube total influence. Full FEI remains OPEN. This explicit resume is later than the historical campaign end dates; no schedule or clock is extended.

## sources actually read, revisions and theorem locators

Machine AGENTS and full protocol {protocol['revision']}; current BOARD, B17 STREAM_NOTES v2 and A081 rolling/prior-stage files. The 36-file intake manifest records complete machine reads of the required canonical README, status, registries, packet/actions, campaign plan, supplemental campaign/claims/counterexamples/seed/mapping/sources and four context paper-text versions. These are baseline intake, not fresh audits of every paper or historical run. The prior 100-node A081 graph preserves earlier source-bound audits. Current proof reading: A011 v5/v6 exact CLAIMS and DERIVATION; A094 objection exact CLAIMS and DERIVATION sections1--2; A100 unchanged scoped reconstruction; A050/A096 exact interface claims; A031 exact v6 claim/review and proof evidence. Immutable snapshots and raw SHA256 pins are in out/INTAKE_PINS and out/SOURCE_PINS. One source requires explicitly recorded cp1252 decoding; its raw bytes are preserved. Read-only math-brain card claim_222dcbc67cb0e75c4bdea3e4e3981211a615008a4e57bce5337d4d0b9b000aca confirms the coordinate-supplier input is unproved; it is a lead, not a premise.

## complete derivation or exact first unsupported line

REVIEW derives delta=conditional-pair KL-(1/2)log2(Z0 Z1/s^2)>=0 and the finite identity CEroot+E=Hroot+Qloss+mean terminal D. The actual b>=12 dictator witness has denominator-minus-numerator epsilon(1-epsilon)(1-6epsilon)>0 and 1-Zclean Zedit=(1-Zclean)^2>0. This independently reconstructs A094's exact scoped objection: v5's terminal functional omits Qloss when identified with the root-plus-reset transaction bill. Its numerical functional inequality and reserve adequacy are not refuted. V6 changes descendants to inherited references with optional same-mass normalized-vacuum calibration; calibration charges are nonpositive, so its entire Qloss is contained in original root divergence. The exact conditional owner margin has coefficients 35751/23552 and18111/4096. The full physical root envelope is not freshly proved by A081; A031's unchanged exact-scope independent review is separately pinned. The first universal unpaid line is a useful arbitrary-core original O(I) source or required compatible admission, paid from SAME unused original influence. Original local-floor query-loss payment remains a distinct open leaf.

## executed validation with domain, arithmetic, commands and outputs

Commands, from this run: python -B -X utf8 code/intake.py; code/check.py; code/assemble.py; code/validate.py; code/finalize.py. Final arithmetic certificate: {res['assertions']} assertions, {res['one_query_reset_profiles']} one-query/reset profiles, {res['ghost_profiles']} ghost profiles, all278 labelled Boolean truth tables n0..3, mass1 and half, true-only and half-uniform references; PASS in{res['seconds']:.3f}s. A separate literal b12 permitted-family target checks all16384 truth values/8192 data fibers by exact Walsh arithmetic;53 b12..64 normalizer checks and exact scalar coefficients also PASS. Rational prime-log forms avoid floating equality tests. All-b and finite-tree conclusions use the displayed analytic algebra, not extrapolation from finite checks. The initial intake decode exception was repaired by recording the actual source codec. Initial frozen witness-only spec omitted the small-query replay domain; preliminary output is retained as PILOT, and the corrected full domain and code hash were frozen before the final replay. An early validator invocation raced graph creation and failed with FileNotFoundError; the sequential final run passes. These execution errors are not mathematical refutations. Formal status: {formal.get('status')}; no full FEI/ledger theorem is called Lean-certified. No heavy search, GPU, automatic dimension escalation, detached worker or shared-process intervention.

## proof dependencies and changed downstream conclusions

The graph extends100 to{val['nodes']} exact statement versions with{val['proof_edges']} proof edges. All{val['guard_count']} mutation fixtures reject: cycles/self-cycles, missing/duplicate versions, final-FEI promotion, supplier promotion, dropping hypotheses/units/query costs/old U, accepting the v5 bundle, changing v6 policy to local floors, and converting audited definitions or scope relations into proof acceptance. Refutation/supersession/policy changes are semantic relations outside the proof DAG. Source-declared dependencies remain verbatim beside the explicitly scoped graph edges. V5 survives only as a terminal-functional source claim; v6's repaired inherited/vacuum theorem is source-bound and conditional on its supplied source. At mass<1 calibration matches NORMALIZED vacuum shape; the actual vacuum reference mass is s*P(empty). This graph is an evidence/conditional dependency graph, not a claim that every stored node is independently accepted. No universal constant improves.

## one next mathematical action and independent reviewer

{next_action} This is the shortest unresolved assembly step; further optional inherited resets cannot buy an arbitrary-core initial source. A094/A086 contribute to the repaired version and are not designated as disinterested acceptors of its entire chain; A085/A099 should audit the integrated scope and source pins independently.

## actual persistence receipts or precise save blocker

The four required exact-schema protocol files, source snapshots, executable checkers, exact outputs, dependency graph and unresolved leaves are saved locally in this run. STATUS is two lines; WORKLOG and LEARNED are appended with the actual stage date. Final readback verifies hashes/schema equality, packet compatibility, all source pins and files below20MB. PERSISTENCE_RECEIPTS describes local bytes only; supervisor copies, canonical adoption, private remote mirrors, downstream mathematical use and publication remain UNVERIFIED. No git, mail, brain write, other-agent/shared-index/trading mutation, external deletion or detached child is performed. Wake degraded because attachment-lock timeout and stale context; mathematical premises come from the pinned campaign sources. Compute snapshot showed93% physical memory use and8.1GB free disk; bounded arithmetic was kept small and no other work was stopped.

## Universal bridge

C024 history transfer feeding C019 stopping-tree payment advances by an exact dependency correction: the omitted physical-query contraction is retained, and the inherited/vacuum repair is separated from the still-unpaid local-floor policy. The universal constant improvement is zero. C018 and the arbitrary-core original source/required compatible admission remain unpaid; a supplied source cannot be promoted to a construction or used in a cycle through FEI. NEXT attacks that precise universal supplier/admission bottleneck with complete old costs and terminals, rather than enlarging an optional reset family or repeating another isolated Boolean class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
state=f'STATE: A081 dependency audit saved: {val["nodes"]}-node DAG/{val["guard_count"]} guards and {res["assertions"]} exact checks PASS; v5 query-KL gap/v6 inherited repair separated; A031 scoped review pinned; FEI OPEN.\nNEXT: {next_action}\n'
(HOME/'STATUS.md').write_text(state,encoding='utf-8')
entry=f'\n{now} — A081 resume: pinned A011 v5/v6 and A094/A100/A031 evidence; reconstructed complete physical-query ledger and actual b12 witness. {res["assertions"]} exact checks and {val["guard_count"]} graph rejection fixtures PASS;110 nodes. Repaired intake codec, incomplete preliminary spec and validator-before-graph race; final replay sequential. Universal source and local-floor query-loss leaves OPEN. Local files saved; remote persistence unverified.\n'
with (HOME/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(entry)
lesson='\n2026-10-27 query-KL dependency lesson: CEroot+actual signed same-target resets=Hroot+reached physical-query contractions+mean complete terminal D. A011 v5 omitted the contraction only in its transaction interpretation; numerical terminal bound/reserve not refuted. V6 changes policy to inherited/normalized-vacuum descendants, making resets nonpositive and paying contractions inside original Droot. This does NOT pay original local floors or construct an arbitrary-core original source. At scalar mass s<1 only normalized shape has actual-vacuum matching; actual mass is s*P(empty). Exact affine owner coefficients35751/23552,18111/4096 are conditional on the independent root envelope. A031 exact-scope review is pinned separately; source definitions/refutation edges must never become circular proof premises.\n'
with (HOME/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(lesson)
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:(R/'out'/('ROLLING_'+name)).write_bytes((HOME/name).read_bytes())
# Exact schema and actual readback, independent of pretty-print order.
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(load(R/'PROGRESS.json'))==expected
assert load(R/'PROGRESS.json')==load(R/'PACKET_DELTA.json')
for c in load(R/'CLAIMS.json'):assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for manifest in ['out/SOURCE_PINS.json','out/INTAKE_PINS.json']:
 for pin in load(R/manifest):
  if not pin.get('missing'):assert sha(R/pin['snapshot'])==pin['sha256']
for name in protocol['required_per_run']['report_fields']:assert ('## '+name) in (R/'REPORT.md').read_text(encoding='utf-8')
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json']]
assert all(p.stat().st_size<20_000_000 for p in files)
receipts=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]
save(R/'out/PERSISTENCE_RECEIPTS.json',{'timestamp':now,'scope':'LOCAL_BYTES_ONLY; no remote verification','files':receipts})
for rec in receipts:assert sha(R/rec['path'])==rec['sha256']
save(R/'out/FINAL_READBACK.json',{'status':'PASS','protocol_schemas':'PASS','source_and_payload_hashes':'PASS','payload_files':len(receipts),'packet_delta_equals_progress':True,'rolling_status_lines':2,'file_limit_bytes':20_000_000,'FEI':'OPEN'})
print(json.dumps({'status':'PASS','run':str(R),'nodes':val['nodes'],'guards':val['guard_count'],'exact_assertions':res['assertions'],'payload_files':len(receipts),'FEI':'OPEN'}))
