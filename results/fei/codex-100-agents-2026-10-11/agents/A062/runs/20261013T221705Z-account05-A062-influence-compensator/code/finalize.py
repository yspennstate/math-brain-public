from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
root=agent.parents[1]
registry=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((registry/'EXECUTION_PROTOCOL.json').read_text())
prior=agent/'runs/20261012T003951Z-account05-A062-influence-compensator'
old=json.loads((prior/'CLAIMS.json').read_text())[0]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj): (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
consumers=['A017','A061','A064','A065','A087','A094','A097','B13','B20']
statement=old['exact_statement']+' Extension: For every even t>=2, every single vertex sign flip of a quadratic bent t-core, with any coordinate character phase, has zero complete increasing-pair-order entry reserve at every C>=6. For every even k>=4, T_k=b_k with sign flips at zero and e_1+e_3 has zero complete paired-entry reserve at C>=6. At its first query both children retain one edit; the expensive character-mate child has zero reserve and the other child reserve is at most two bits. If the clean core and T_k are activated by r>=2k point controls and selected by a fair bit, then all control entry reserves vanish, Q_root=[D_selector-2C*2^(-r-k)]_+, Q_root<8*2^-k*psi(mu) and Q_root<=4*2^-k*I_root; at C=6, H<=(6+4*2^-k)I<=25I/4. Its exact initial influence is 2^-r[k/2+r(1-2^(-k/2)+2^(1-k))+(2k-2)2^-k]. Original all-node rarity and asymptotic conclusions are retained only for the original one-zero-edit selector family; they are not asserted for the new phase or two-edit families.'
hyp=['For original retained conclusions only: '+h for h in old['hypotheses']]+[
 'For the extension: actual Boolean signs; entropy bits; ordinary influences; C>=6',
 'Single-edited core: t even >=2, quadratic bent times an arbitrary coordinate character; sign flip at any physical vertex',
 'Two-edited core: canonical b_k, k even >=4, flipped at exactly 0 and e_1+e_3',
 'Complete increasing adjacent-pair physical tree, skipping irrelevant coordinates and ending at constants',
 'Activated-selector extension: r>=2k fresh point controls, fair fresh selector; selector then controls then paired data',
 'psi(mu)=mu log2(1/mu) for physical output minority; the new credit is a root bound, not a local rarity drift claim']
claim={'claim_id':old['claim_id'],'version':2,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A062; original target and Bellman convention B13; preceding scalar and empty-fiber credits retained'],
 'proof_source':{'extension':'DERIVATION.md','original_proof':str(prior/'DERIVATION.md'),'original_proof_sha256':sha(prior/'DERIVATION.md'),'validation':'out/EXACT_TREES.json'},
 'proof_dependencies':old['proof_dependencies'],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':old['claim_id'],'version':1,'scope':'extension retaining all original conclusions'}],
 'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
write('CLAIMS.json',[claim])
next_action='Extract terminal-inclusive two-child ownership for an arbitrary child-certified core with a sparsely edited character factor, retaining both grandchildren reserves; A087/A094 independently reconstruct phase correction and initial influence.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'G-R-MISMATCH','attempt_id':'A062-two-surviving-edits-1',
 'method':'phase-aware paired-query reserve induction, exact complete-tree reconstruction, scoped independent terminal-ownership review',
 'mathematical_delta':'All-phase arbitrary-position single-edited quadratic cores and canonical two-edited cores have Q_entry=0 at C>=6; two-edit activated selector Q_root/I<=4*2^-k; scoped A061 terminal clause independently reconstructed.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'SCOPED_OWNERSHIP_CORRECTION_PROVED; UNIVERSAL_C019_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A062-INFLUENCE-STOPPING-INTERFACE','version':1,'scope':'finite budget'}, {'claim_id':old['claim_id'],'version':1,'scope':'source-complete activation and isoperimetric proof incorporated; independent review pending'},{'claim_id':'A061-ARBITRARY-CORE-EDIT-ADMISSION','version':1,'scope':'terminal clause independently reviewed, not a premise'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':2}],
 'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_NOTE.md','FROZEN_SPEC.json','out/EXACT_TREES.json','out/TERMINAL_REVIEW.json','out/SOURCES.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Independent reserve-claim review pending; arbitrary-core two-child reserve ownership open; supervisor adoption and remote mirror unverified'],
 'packet_ids':['A062']}
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
sources=[(root/'BOARD.md','stage-start updated snapshot'),(root/'claude/B13/STREAM_NOTES.md','v2 complete source'),
 (registry/'EXECUTION_PROTOCOL.json','complete protocol'),(prior/'DERIVATION.md','previous activation, isoperimetry and original theorem'),
 (prior/'CLAIMS.json','retained version 1 exact statement'),(prior/'code/check_reserve.py','rational logarithm kernel'),(prior/'code/verify_tree.py','previous oracle representation'),
 (root/'agents/A061/runs/20261013T215821Z-account05-A061-entropy-process/PADDING_EDIT_PROOF.md','complete proof, scoped review section 5'),
 (root/'agents/A061/runs/20261013T215821Z-account05-A061-entropy-process/CLAIMS.json','v1 reviewed scope'),
 (root/'agents/A017/LEARNED.md','parallel incompatible-gradient fiber frontier'),(root/'agents/A064/LEARNED.md','local-rarity obstruction frontier')]
write('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':scope} for p,scope in sources])
write('out/REVIEW_SCOPE.json',{'reviewer':'A062','claim_id':'A061-ARBITRARY-CORE-EDIT-ADMISSION','version':1,'verdict':'HOLDS_AT_STATED_SCOPE','scope':'terminal H/I convex combination and exactly q*2^(1-r-q) queried dummy influence only','whole_bundled_claim_accepted':False,'proof':'REVIEW_NOTE.md','validation':'out/TERMINAL_REVIEW.json'})
(agent/'STATUS.md').write_text('STATE: A062 stage 3 complete locally: phase-aware single-edit and two-surviving-edit paired cores have Q*=0 at C>=6; activated two-edit root Q*/I<=4*2^-k; 1469 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: Extract terminal-inclusive ownership for arbitrary child-certified cores with a sparse edited character factor, retaining both grandchildren reserves; A087/A094 review phase correction and initial influence.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-13 22:17 UTC stage 3: Read updated board, B13 v2, own status and A061 arbitrary-core admission/terminal proof. Proved phase correction for every translated single edit; character phases preserve entropy but not influences. Two edits at 0 and e1+e3 leave both children edited; expensive mate owns its query payment, cheap mate reserve is absorbed by parent. All even k>=4 paired entry reserves vanish at C>=6. Activated selector root Q*/I<=4*2^-k, H<=25I/4. Frozen pilot 17 roots/158 assertions PASS; final 89 roots/1053 exact assertions PASS in 0.409s. Independently reconstructed only A061 terminal ownership clause, 64 cases/416 assertions PASS in 0.027s. Extended existing pending reserve candidate to v2 instead of opening another broad candidate. Saved protocol files and local receipts; full FEI, arbitrary-core ownership and independent review remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nEvery arbitrary-vertex single sign flip of an even quadratic bent core, with any coordinate character phase, has zero paired-order entry reserve at C>=6. Entropy is invariant under character multiplication; influence is not. An odd unmatched mate has influence delta_m or 1-delta_m; the expensive branch is locally paid and cannot be treated as another cheap branch. H(E4)=6-(27/16)log2(3)<7/2 settles the adverse-phase endpoint.\nFor two flips at 0 and e1+e3, both first-query children retain edits, but one is an expensive character-mate state with Q*=0. Parent Inf=1/2+4*2^-k pays the cheap-child reserve; complete paired entry Q*=0 for every even k>=4. Activated clean/two-edit selector root Q*/I<=4*2^-k, and exact I=p[k/2+r(1-alpha+2delta)+(2k-2)delta]. This is not an all-node rarity certificate for general phases or arbitrary edit sets.\nA061 arbitrary-core edit admission v1 terminal clause independently HOLDS: querying q padded labels spends exactly q*2^(1-r-q) and retains (1-2^-q)(H(g)-CI(g))+2^-q(H(g^v)-CI(g^v)). Cheap local directions do not certify the retained core. Full bundled admission/continuity claim was not accepted by this scoped review.\n')
final=json.loads((run/'out/EXACT_TREES.json').read_text()); review=json.loads((run/'out/TERMINAL_REVIEW.json').read_text())
assert final['assertions']==1053 and review['assertions']==416
assert final['failures']==review['failures']==0
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in required['progress_fields']}
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=(run/'REPORT.md').read_text()
for heading in required['report_fields']: assert '## '+heading in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert len((agent/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
 p=agent/name; receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/RECEIPTS.json',{'run_id':run.name,'schema_checks_passed':True,'local_persistence_verified':True,'independent_review':'PENDING','remote_mirror_verified':False,'files':receipts})
print(json.dumps({'schema_checks_passed':True,'exact_assertions':1469,'extended_claim_version':2,'full_fei':'OPEN','files_receipted':len(receipts)},indent=2))
