from pathlib import Path
import json,hashlib,datetime
BASE=Path(__file__).resolve().parents[1];AGENT=BASE.parents[1];ROOT=AGENT.parents[1]
A7=ROOT/'agents/A007/runs/20261014T043228Z-fleet05-A007-root-normalization'
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
FOREST=PROTO.parent/'source_material/reductions/paper/forests.tex'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):(BASE/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
proto=json.loads(PROTO.read_text(encoding='utf-8-sig'))
original=next(x for x in json.loads((A7/'CLAIMS.json').read_text(encoding='utf-8')) if x['claim_id']=='A007-RETAINED-OWNERSHIP-TAIL-AND-ROOT-BUDGET')
claim=json.loads(json.dumps(original))
claim['review_records'].append({'reviewer':'A015','verdict':'HOLDS_AT_ORIGINAL_DOWNSTREAM_SCOPE_NO_REPAIR','proof_source':str(BASE/'REVIEW_A007.md'),'validation':str(BASE/'out/EXACT_CHECK.json'),'method':'Independent coefficient/path recurrence and exact multinomial damping; reconstruct tail integration, general K tangent and root/factorial signed budget','reviewer_supplied_substantive_repair':False,'upstream_authorship_disclosure':'A015 authored the upstream occupation envelope/size law; this downstream review is not a second independent acceptance of that upstream artifact or its full dependency chain','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
claim['status']='INDEPENDENTLY_RECONSTRUCTED_DOWNSTREAM_SCOPE_LOCAL_ADOPTION_PENDING'
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':proto['revision'],'run_id':BASE.name,'stream':'B03','packet_id':'A015','gap_id':'G-J-COST','attempt_id':'A015-stage5-tail-scope-and-joint-credits',
 'method':'Review settled full-support posterior tail; exact actual-Boolean arbitrary-support tail falsifier plus retained root/factorial and original queue-sector certificate',
 'mathematical_delta':'A007 tail/general-budget v1 independently holds downstream with upstream A015 authorship disclosed. Arbitrary-support ownership tail fails on OR_n: conditional mean >=.5log2 ceil(n/2), positive-spectrum pointwise witness n8192. Same activated prime reference gives J1=s!/n^s*2^(-(s-1)/5) and exact Q_star, refunding full-set nlogn labels to linear cost; no whole-sector payment inferred.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS',
 'mathematical_status':'FULL_SUPPORT_TAIL_CLOSURE_ADOPTED_GENERAL_TAIL_TRANSPLANT_REFUTED_JOINT_UNIVERSAL_PAYMENT_OPEN',
 'claim_versions_used':['A007-RETAINED-OWNERSHIP-TAIL-AND-ROOT-BUDGET@1','A007-DISTRIBUTED-CORE-COMPONENT-LIFT@1'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'Added downstream no-repair review with upstream authorship disclosure; no new broad candidate'}],
 'source_artifacts':[str(BASE/'REVIEW_A007.md'),str(BASE/'SCOPE_AND_CREDITS.md'),str(BASE/'out/EXACT_CHECK.json'),str(BASE/'out/PILOT_REPAIR.md')],
 'next_consumers':['A007','A008','A009','A086','A094','B03','B20'],
 'next_action':'Test joint label/K/root/factorial controller budget at first private-to-shared incidence change under fixed feasible reference, all spectral sectors and inherited nonconstant core cost retained.',
 'stagnant_substantive_attempts':0,
 'blockers':['General joint expected budget and inherited base physical-location cost remain unpaid','Scope diagnostic independent review and supervisor adoption unobserved'],
 'packet_ids':['A015']}
save('PROGRESS.json',progress);(BASE/'PACKET_DELTA.json').write_bytes((BASE/'PROGRESS.json').read_bytes())
sources=[(ROOT/'BOARD.md','Stage-start snapshot and follow-up middle chunks; final saved source bytes hashed'),(ROOT/'claude/B03/STREAM_NOTES.md','Complete v2'),(AGENT/'STATUS.md','Inherited stage-4 status before update'),(PROTO,'Complete protocol v2'),(A7/'REPORT.md','Complete'),(A7/'POSTERIOR_TAIL.md','Complete downstream tail proof'),(A7/'GENERAL_BUDGET.md','Complete general signed budget'),(A7/'CLAIMS.json','Complete statement/version/hash'),(FOREST,'Inherited original baseline from prior stages, not newly reread')]
save('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in sources])
full=json.loads((BASE/'out/EXACT_CHECK.json').read_text(encoding='utf-8'));pilot=json.loads((BASE/'out/PILOT.json').read_text(encoding='utf-8'))
assert full['status']==pilot['status']=='PASS'
assert (full['assertions'],pilot['assertions'])==(11020,3340)
assert (full['general_records'],full['root_credit_records'],full['ordered_tail_records'])==(944,1372,2485)
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert set(progress)=={f.split(' (')[0] for f in proto['required_per_run']['progress_fields']}
assert all(claim[f]==original[f] for f in ['version','exact_statement','hypotheses','statement_sha256'])
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+f in report for f in proto['required_per_run']['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
(AGENT/'STATUS.md').write_text('STATE: A015 stage 5 complete: A007 full-support tail/root budget independently HOLDS downstream; arbitrary-support tail false on OR_n, joint stars refund growing labels; 14,360 exact checks PASS; FEI OPEN.\nNEXT: A007/A008/A086 review; test SAME joint label/K/root/factorial budget at first private-to-shared incidence change, retaining every spectral sector and inherited core cost.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 stage 5 ('+BASE.name+'): consumed A007 full-support tail closure and reconstructed whole downstream tail/general budget with A015-authored premise disclosure, no repair. General-support ownership bound refuted by actual OR_n prime table (forced log|T|, conditional average >=.5logceil(n/2)); symbolicn8192 tail fails by6^5<8192. Exact same-table one-control J=s!/n^s*2^(-.2(s-1)) and full original Q_star show factorial/root refunds reduce full-set nlogn labels to linear, while empty-core labels/all-sector ledger remain. Exact K envelope gap bounded gamma(2-loge). Finalpilot3340+full11020=14360 assertions PASS; preserved expected control-sign pilot correction and superseded checks, excluded from totals. All files saved. Next joint-incidence test, not repeat settled tail.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nFull-support tail CLOSED by A007-RETAINED-OWNERSHIP-TAIL-AND-ROOT-BUDGET@1, reconstructed downstream by A015 with own upstream-envelope authorship disclosed: multinomial*A<=1, finite-N label depletion and moment sum C_s<=6^(s-1) give E_eta ownershipH<=5log2(6)<13, and Psi_dist<=(1-b)log2(6)I_core. Inherited pR_g and full entropy overhead remain. No more full-support tail search.\nArbitrary-support tail transplant is false even on exact singleton primes of OR_n: ownership forced, H=log|T|, normalized nonempty spectral mean >=.5logceil(n/2); positive full-set n8192 contradicts transplanted6-tail. This is no FEI counterfamily. For one selected fresh control, K_s=slog s-(s+1)log((s+1)/2), Z=s2^(-gamma(s-1)); reviewed general envelope gap gamma[2-(s+1)log(1+1/s)] is bounded, so growing K cannot just be discarded.\nOn SAME OR_n activated prime table, beta1/n: root credit2^(s-1) and s! actual chronological stars give J1=s!/n^s*2^(-(s-1)/5). Exact conditioned selected Q_star=s!/[24D\'n^s s^2(s+1)] [alpha/(4(1+alpha))]^(s-1), alpha2^-6/5,D\'=(1+1/(4n))^n-1. Full-set negative log is O(n) with all queue factors retained; empty-control L0=n^-s and all other spectral sectors still unpaid by this pointwise result. General missing feature is joint expected label/K/ownership payment minus root/factorial credits, not uniform ownership concentration.\n')
files=[p for p in BASE.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[AGENT/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
save('out/RECEIPTS.json',{'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'protocol_fields':'PASS','progress_packet_identical':(BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes(),'source_statement_preserved':True,'upstream_authorship_disclosed':True,'diagnostic_independent_review':'PENDING','mirror':'UNVERIFIED'})
assert all(sha(Path(r['path']))==r['sha256'] for r in json.loads((BASE/'out/RECEIPTS.json').read_text(encoding='utf-8'))['files'])
print(json.dumps({'persistence':'PASS','files':len(files),'assertions':full['assertions']+pilot['assertions'],'run':str(BASE)}))
