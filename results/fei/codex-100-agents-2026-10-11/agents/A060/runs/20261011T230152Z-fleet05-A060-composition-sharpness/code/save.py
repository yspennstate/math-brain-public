from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; HOME_TASK=R.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
CAN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,x):(R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads((CAN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
validation=json.loads((R/'out'/'validation.json').read_text(encoding='utf-8'))
assert validation['status']=='PASS'
statement=('For every r,d>=1, the fresh balanced rare-switch chain F_0=x_0, F_t=(1-A_r)F_(t-1)+A_r y_t, p=2^-r, q=1-p has '
'H=[q^2 log2(1/q^2)+2rp(2-p)](1-q^d)/p, I=1+r(1-q^d), B=r[phi(q^2,p^2)+2p-2p^2](1-q^d)/p, phi(u,v)=(u+v)h2(v/(u+v)). '
'The repeated concavity-root log D=sum_(t=1)^(d-1)q^(d-t)Lambda(F_t) is at least p d(d-1)q^(2d); the exact continuation L is zero. '
'For every a>=1 and even m>=2, F=b(y)-2A_a(z)1_(y=0), quadratic bent b, p=2^-a, delta=2^-m has I_W=2ap delta, I_data=m(1/2+2p delta), '
'and L-32p delta/(a ln2)<=B_W/I_W<=L with L=2(1-p)(m+2a-2+1/ln2)/a. '
'On a class closed under disjoint tensor powers, H<=CI+D0 with a fixed finite D0 implies H<=CI with the same multiplicative C.')
hyp=['uniform physical inputs; Boolean sign output','fresh disjoint input blocks for the chain','origin selector and data cells; even-dimensional paired quadratic bent function for the splice','H and B in bits; Lambda and D in nats','zero entropy terms by continuity; tensor conclusion requires tensor-closed class and fixed D0']
cid='A060-COMPOSITION-SHARPNESS-LEDGER'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,
'statement_sha256':sha(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()),
'contributors':['A060; A059 rare-switch family and divergence credited; B12 lead target'],
'proof_source':{'path':'PROOF.md','sha256':sha((R/'PROOF.md').read_bytes())},
'proof_dependencies':[{'source':'threshold_paper_38pp.txt','locator':'Proposition 7.1','scope':'composition interface, specialized spectra independently derived'},{'source':'A057 REPORT.md','locator':'derivation steps 2,3,6','scope':'root relaxation being tested; imported formula independently specialized'}],
'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
'refutes':['selector-only B_W<=K I_W for fixed K on arbitrary branches','depth-uniform bound on the specific repeatedly charged concavity log bank'],
'first_unproved_line':None,'next_consumers':['A019','A056','A057','A058','A059','A091','A090','A097','B20']}
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B12','packet_id':'A060','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A060-sharpness-01',
'method':'Exact spectra, conditional selector channel, independent rare-switch reconstruction, analytic bounds and tensor audit',
'mathematical_delta':'Exact chain B and zero continuation residual; factor-r correction to depth diagnostic; all-parameter bent-cell B_W/I_W enclosure and chi-square; scoped A059 independent reconstruction; additive scope pinned',
'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SHARPNESS_CONTROLS_PROVED_UNREVIEWED; UNIVERSAL_TRANSPORT_OPEN; FULL_FEI_OPEN',
'claim_versions_used':['threshold Proposition 7.1 local 38pp version','A057 root-relaxation v1 (specific specialization rederived)','A059 rare-switch obstruction v1 (independently reconstructed at scope)','X009 ERASURE_RIGIDITY sections 2-3 (a=1 recovered exactly)'],
'claims_created_or_changed':[cid+'@1','A059 rare-switch subclaim: local independent HOLDS reconstruction in REVIEW_A059.md'],
'source_artifacts':['PROOF.md','COMPOSITION_SHARPNESS.tex','CONSTANT_SCOPE.json','REVIEW_A059.md','code/check.py','out/validation.json','out/SOURCES.json'],
'next_consumers':claim['next_consumers'],
'next_action':'Evaluate recentered biased-descendant residual plus terminal entropy on the rare-switch control-first physical tree, assigning each charge once to local gate deficit; independent reviewer A091, alternate A090.',
'stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor adoption pending; universal data-side/physical-tree transfer unpaid'],
'packet_ids':['A060']}
write('CLAIMS.json',[claim]);write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('CONSTANT_SCOPE.json',{'units':{'H':'bits','B':'bits','Lambda':'nats','D':'nats'},'chain':{'fresh_selector':True,'balanced':True,'physical_input_disjointness':True,'branch_orthogonality':'rare-switch branch F_(t-1) versus fresh y: correlation zero; singleton physical selector-cube neighbours are not uniformly orthogonal','selector_energy_density':'p=2^-r tends to zero','actual_H':'<=6(I-1)','spurious_depth_cost':'D~p d^2; deficit epsilon=rp gives D~epsilon d^2/r'},'bent_cell':{'fresh_selector':True,'balanced_branches':False,'orthogonal_branches':False,'branch_correlation':'1-2delta','overlapping_Fourier_supports':True,'I_W':'2a p delta','I_data':'m(1/2+2p delta)','asymptotic':'fixed a: slope 2(1-2^-a)/a in m; a->infinity,m/a->lambda: 4+2lambda','what_fails':'selector-only payment','what_remains':'data-side influence may pay the small entropy cost; reserving and transferring it is unresolved'},'tensorization':{'additive_fixed_D':'erased for tensor-closed classes','H<=C(I-1)+D':'same multiplicative universal/tensor-closed coefficient as H<=CI','per_factor_D':'not erased','narrow_families':'chain family and single bent-splice family themselves not tensor closed; claim applies to their tensor closures'},'full_FEI':'OPEN'})
paths=[CAN/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/ERASURE_RIGIDITY.md','sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']]
paths += [BASE/'BOARD.md',BASE/'claude/B12/STREAM_NOTES.md']
paths += list((BASE/'context').glob('*.txt'))
paths += list((BASE/'agents/A057/runs').glob('*/REPORT.md'))+list((BASE/'agents/A059/runs').glob('*/REPORT.md'))+list((BASE/'agents/A059/runs').glob('*/PROOF.md'))
write('out/SOURCES.json',[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'scope':'Read scope described in REPORT.md; a hash does not assert complete audit.'} for p in paths])
expected_progress={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))==progress
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all(x in report for x in protocol['required_per_run']['report_fields'])
write('out/SCHEMA_CHECK.json',{'status':'PASS','progress_fields_exact':True,'protocol_annotation_normalization':'packet_ids (one primary ID, for compatibility) denotes key packet_ids, as explicitly required by protocol and user','claim_fields_exact':True,'report_fields_present':True,'packet_delta_equal':True,'assertions_in_mathematical_checker':validation['assertions']})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(HOME_TASK/'STATUS.md').write_text('STATE: A060 sharpness packet complete locally: exact chain H/I/B, redundant-log divergence and factor-r correction; multi-bit bent-cell bound; 839 exact checks PASS; review pending; full FEI OPEN.\nNEXT: A091/A090 review; test recentered control-first physical-tree charge against one local gate-deficit reserve, retaining data influence and terminal entropy.\n',encoding='utf-8')
with (HOME_TASK/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' A060: read protocol/live B12 directions; found A059 already proved repeated-log divergence, independently reproduced it and added exact chain B/zero continuation residual. Derived exact a-bit bent-cell channel and uniform bound. V1 792 checks; V2 839 checks PASS. Saved local artifacts; adoption/review pending. Full FEI OPEN.\n')
(HOME_TASK/'LEARNED.md').write_text('''# Durable facts from A060 stage 1

- Rare-switch chain p=2^-r,q=1-p: I=1+r(1-q^d), H=[q^2 log2(1/q^2)+2rp(2-p)](1-q^d)/p, B=r[phi(q^2,p^2)+2p-2p^2](1-q^d)/p. Every continuation L is exactly zero because the outer branches have disjoint data sectors.
- The relaxed root ledger adds D=sum q^(d-t)Lambda(F_t)>=p d(d-1)q^(2d). If dp->0, D~p d^2, H~4rpd. Gate deficit rp must not be confused with switch probability p. A059 originally proved the divergence; this stage independently verifies its rare-switch subclaim.
- Bent point flip on one a-bit cell: p=2^-a,delta=2^-m, m even>=2. I_W=2ap delta; I_data=m(1/2+2p delta). L=2(1-p)(m+2a-2+1/ln2)/a gives L-32p delta/(a ln2)<=B_W/I_W<=L for all parameters. a=1 recovers X009 exactly. Divergence requires tracking m relative to a; m/a bounded with a->infinity gives finite limit 4+2m/a.
- The bent branches are not balanced or orthogonal: correlation 1-2delta and means sqrt(delta),sqrt(delta)-2delta. Do not use this example against a theorem requiring those hypotheses.
- Fixed additive constants disappear under tensor powers only on tensor-closed classes. An overhead paid per factor does not. Narrow chain/splice families themselves need not be tensor closed.
- Exact FWHT/Fraction and rational prime-log coefficients provide entropy identities without numerical logarithms. 839 assertions passed; analytic arguments supply infinite claims. No full FEI conclusion follows.
- Next gap: map actual physical-query biased descendants and terminal entropy to a single-use local gate/data budget; formula weights are not physical reach probabilities.
''',encoding='utf-8')
files=list(R.rglob('*'))+[HOME_TASK/'STATUS.md',HOME_TASK/'WORKLOG.md',HOME_TASK/'LEARNED.md']
receipts=[]
for f in files:
 if f.is_file() and f.name!='PERSISTENCE.json':
  b=f.read_bytes();assert len(b)<20*1024*1024
  receipts.append({'path':str(f),'bytes':len(b),'sha256':sha(b)})
write('out/PERSISTENCE.json',{'saved_at_utc':now,'local_status':'READBACK_HASHED','review':'PENDING','supervisor_mirror':'PENDING_NOT_CLAIMED','mathematical_validation':validation['status'],'assertions':validation['assertions'],'files':receipts})
print(json.dumps({'status':'PASS','schema':'exact','files_hashed':len(receipts),'mathematical_assertions':validation['assertions'],'save_time_utc':now}))
