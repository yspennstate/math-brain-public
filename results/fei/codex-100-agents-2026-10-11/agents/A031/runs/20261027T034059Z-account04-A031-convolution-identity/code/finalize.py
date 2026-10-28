from pathlib import Path
import json, hashlib, datetime

r=Path(__file__).resolve().parents[1]; a=r.parents[1]
camp=a.parents[1]
canon=Path('math-open-problems/reports/fei-2026-10-11')
proto=json.loads((canon/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
src=camp/'agents/A011/runs/20261027T025625Z-account04-A011-representation-existence'
original=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert hashlib.sha256(original['exact_statement'].encode()).hexdigest()==original['statement_sha256']
claim=dict(original)
claim['review_records']=original['review_records']+[{
 'reviewer':'A031/account04','verdict':'HOLDS_UNCHANGED_SCOPED_V6',
 'scope':'Entire exact v6 statement; supplied source, prescribed ROOT floors, inherited/vacuum descendants only; no fresh local-floor or arbitrary-core source acceptance.',
 'source':str(r/'DERIVATION.md'), 'evidence':str(r/'out/MAIN.json'),
 'independence':'Fresh Fraction implementation and analytic root-coefficient reconstruction; no mathematical repair supplied.'}]
claim['status']='INDEPENDENTLY_RECONSTRUCTED_LOCALLY_A031; CONDITIONAL_INITIAL_SOURCE; FULL_FEI_OPEN'
assert set(claim)==set(proto['required_per_run']['claim_fields'])
(r/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
main=json.loads((r/'out/MAIN.json').read_text(encoding='utf-8'))
progress={
 'protocol_revision':proto['revision'],'run_id':r.name,'stream':'B07','packet_id':'A031',
 'gap_id':'A031-ORIGINAL-SOURCE-ADMISSION','attempt_id':'stage22-consume-A011-v6',
 'method':'Independent analytic and exact finite reconstruction of signed physical restriction, inherited ghosts, full query-KL ledger, calibration and original reserve.',
 'mathematical_delta':'A011 v6 independently HOLDS unchanged at inherited/vacuum scope; exact full transaction accounting clears new dependency. Universal FEI constant improvement zero; arbitrary-core initial source remains unpaid.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_INDEPENDENTLY_RECONSTRUCTED; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':6,'statement_sha256':claim['statement_sha256']},
 {'claim_id':'A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT','version':1,'scope':'Only used atomwise portion independently reconstructed; no blanket review'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':6,'change':'Local independent review record; exact statement and hash unchanged'}],
 'source_artifacts':[str(r/'DERIVATION.md'),str(r/'out/MAIN.json'),str(r/'out/SOURCE_INTAKE.json'),str(r/'out/DETAILED_SOURCE_RECEIPTS.json')],
 'next_consumers':['A033','A035','A011','A050','A096','A097','A094','B20'],
 'next_action':'Price an ORIGINAL arbitrary-core O(I) complete source in the inherited/vacuum interface; if fresh nonempty floors are necessary, state the class and pay reached admission including query contractions from SAME unused original owner.',
 'stagnant_substantive_attempts':0,'blockers':['Original arbitrary-core influence-priced source remains unproved.','Fresh local nonempty-floor inherited compatibility/payment not supplied.','Supervisor copying and downstream adoption unverified.'],
 'packet_ids':['A031']}
assert set(progress)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:
 (r/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
paths=[canon/'EXECUTION_PROTOCOL.json',Path('~/AGENTS.md'),camp/'BOARD.md',camp/'claude/B07/STREAM_NOTES.md',src/'REPORT.md',src/'DERIVATION.md',src/'CLAIMS.json',camp/'agents/A096/runs/20261023T140303Z-account03-A096-live-gap-ledger/REPORT.md',camp/'agents/A094/runs/20261026T232939Z-account04-A094-proof-chain-challenger/REPORT.md']
recs=[]
for p in paths:
 b=p.read_bytes(); recs.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'scope':'Detailed mathematical reconstruction' if 'A011' in str(p) else 'Orientation/used scoped source; BOARD is mutable'})
(r/'out/DETAILED_SOURCE_RECEIPTS.json').write_text(json.dumps(recs,indent=2),encoding='utf-8')
leanpath=r/'out/LEAN_RECEIPT.json'
lean=json.loads(leanpath.read_text(encoding='utf-8')) if leanpath.exists() else {'status':'NOT_RUN_PENDING_ADMISSION'}
sections=proto['required_per_run']['report_fields']
contents=[
 'Independently review the EXACT A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@6 statement, hash '+claim['statement_sha256']+'. Every finite Boolean uniform cube and adaptive physical stopped tree, supplied O(I) source and prescribed ROOT construction; bits; complete subprobability references. Verdict HOLDS unchanged at inherited/vacuum-calibrated scope. Full FEI remains OPEN.',
 'Current BOARD, B07 notes through stage21, own rolling files/stage21 status, entire execution protocol and A011 stage22 REPORT/DERIVATION/CLAIMS. A094 scoped query-KL objection and A096 ghost-interface report consumed. SOURCE_INTAKE accesses canonical baseline, campaign supplement/sources and all four paper texts with selected locators; no new full-paper audit is claimed. Detailed byte hashes are recorded separately. Read-only math recall supplied no new premise.',
 'DERIVATION sections1--3 reconstruct signed child cancellation, positive normalization including ghosts, delta=conditional pair KL+reference outcome KL, Braw=Hroot+terminalD+Qloss, nonpositive normalized-vacuum calibration retaining mass, root envelope135c/92+320S, and exact SAME-owner residual [(35751/23552)C0+18111/4096]Ig+KsumG. No repair to v6 supplied. First unsupported universal line: an ORIGINAL arbitrary-core O(I) complete source. Fresh descendant floors remain outside the theorem.',
 f'Frozen v1 saved before execution. Commands: python -B -X utf8 code/check.py pilot and main from this run (actual launcher used agent-root run-relative path). Pilot792 trees/48335 checks in1.998s; main ALL278 labelled n0..3 functions,10008 fixtures,120888 visited nodes,{main["checks"]} checks in{main["runtime_seconds"]:.3f}s. References P,(P+uniform)/2,(P+delta_empty)/2; mass1 and1/2; two fixed policies and one adaptive stopped policy; ghost splits1/2 and1/3. Main includes3104 ghost fibers,5488 biased normalizers,110880 calibrations. Fraction checks certify finite atom identities, signed Young domination, exact constants and positive normalizer witnesses b12..64. Floating logarithms are diagnostics only; general equalities/signs have finite analytic proofs. Main estimate80MB, runtime cap120s, no >300MB search. Formal rung: '+lean.get('status','UNKNOWN')+'. No full entropy theorem is claimed Lean-checked.',
 'One local unchanged v6 claim record gains A031 independent HOLDS; source registries are untouched. A094 objection remains valid for withdrawn v5 transaction reading; A011 v6 pays inherited policies rather than silently restoring floors. A096 used transport portion is reconstructed without blanket acceptance. No new generic B07 inequality or F^4=1 admission is claimed; no new independent-review queue debt is opened.',
 progress['next_action']+' A033/A035 should consume this exact-scope review; A094/A085 can challenge the full original-source chain independently.',
 'Four exact-schema protocol files, full derivation, frozen spec, independent checker, pilot/main outputs and source receipts are saved only inside A031. STATUS has STATE/NEXT lines; WORKLOG and LEARNED updated. Local readback/schema/statement-hash receipts are out/PERSISTENCE_RECEIPT.json. Supervisor mirror and downstream consumption are unverified. Wake flagged stale owner-model/state/dream; these are not premises. No git, brain write, messaging, deletion, trading, GPU, detached work or another-agent mutation; all checkers finished normally.'
]
report='# A031 stage22: repaired physical ledger independently holds\n\n'
for heading,body in zip(sections,contents): report+='## '+heading+'\n\n'+body+'\n\n'
report+='Universal bridge: C024 history transfer and C019 stopping-tree payment advance by independent reconstruction of A011 v6 with ghost mass, actual query losses, full terminals and SAME original reserve. This clears a concrete assembly dependency for B07; the numerical universal FEI improvement is zero. C020 original arbitrary-core O(I) source remains unpaid, and fresh nonempty-floor policies need their own admission/payment. NEXT targets that original source in the explicit inherited/vacuum class, rather than another isolated class or optional-reset census.\n'
(r/'REPORT.md').write_text(report,encoding='utf-8')
(a/'STATUS.md').write_text('STATE: Stage22 saved: A011 v6 inherited/vacuum SAME-owner theorem independently HOLDS unchanged; 10008 trees/1615311 checks PASS; full query KL retained; FEI OPEN.\nNEXT: A033/A035/A094 consume scoped review; price ORIGINAL arbitrary-core O(I) source in inherited/vacuum class, or pay REQUIRED fresh floors including query losses from SAME unused owner.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (a/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+stamp+': Stage22 consumed new A094 objection and A011 v6 repair; unchanged v6 independently HOLDS at inherited/vacuum scope. Signed cancellation, ghost labels, subprobability mass, full query-loss telescope and SAME root coefficients reconstructed. ALL n<=3 labelled functions10008 fixtures/1615311 checks in66.162s PASS; pilot not added. No failed mathematical search. Initial arbitrary-core O(I) source remains unpaid; no new FEI constant. Saved '+r.name+'.\n')
with (a/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n## Stage22\nA011 v6 independently HOLDS unchanged: full signed transaction bill is Braw=Hroot+E Dterminal+Qloss, not merely terminal functional. Inherit supplied ROOT reference (ghosts included) and normalize at its SAME scalar mass; vacuum shape calibration costs minus Bernoulli KL. Thus Braw<=CEroot and query losses are already inside ORIGINAL root bill. Exact root bound135c/92+320S and SAME residual[(35751/23552)C0+18111/4096]Ig+KsumG checked. Fresh local nonempty floors are NOT inherited by this theorem; O(I) arbitrary-core initial source remains unpaid. Exact10008-tree independent reconstruction supports review, not all-dimensional extrapolation.\n')
files=[r/x for x in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json','DERIVATION.md','FROZEN_SPEC.json','code/check.py','out/PILOT.json','out/MAIN.json']]
receipt={'status':'PASS','statement_hash_unchanged':True,'exact_schema_keys':True,'progress_delta_identical':(r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes(),'files':[]}
for p in files:
 b=p.read_bytes(); assert len(b)<20*1024*1024
 receipt['files'].append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
assert all('## '+h in report for h in sections)
(r/'out/PERSISTENCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','run':str(r),'claim_hash':claim['statement_sha256'],'main_checks':main['checks'],'formal':lean}))
