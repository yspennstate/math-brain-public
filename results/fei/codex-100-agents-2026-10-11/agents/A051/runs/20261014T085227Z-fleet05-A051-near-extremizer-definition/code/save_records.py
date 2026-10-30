from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent.parent;A=R.parent.parent;B=A.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):(R/p).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
statement=('For finite uniform Boolean cubes and real K, b_K(n)=max_f(H(f)-K I(f)) is attained. '
'Whenever any K-violation exists, choose least essential dimension n and maximize D_K over all n-bit truth tables: '
'the chosen witness has positive deficit, all coordinates essential, every smaller Boolean phase and proper physical child nonviolating, '
'and every same-dimensional vertex edit nonimproving. For any Boolean f, entropy potential G_f=sum fhat(S)log2(fhat(S)^2)chi_S, '
'and vertex subset E of density delta, H(f^E)-H(f)>=4 E[1_E f G_f]-(8/ln2)delta, '
'and I(f^E)-I(f)=(2/2^n)sum_boundary(E)f(x)f(y). '
'If b_K(n)-D_K(f)<=epsilon, then sum_E f G_f <=(K/2)sum_boundary(E)f(x)f(y)+(2/ln2)|E|+2^n epsilon/4. '
'In particular exact selected witnesses obey f(x)G_f(x)+K p_f(x)<=Kn/2+2/ln2. '
'Proper-cut deficits retain the exact physical telescope and finite child cap b_K(n-|A|). '
'No infinite-dimensional optimizer, automatic reduction-invariance, paid-block selection or full FEI bound is asserted.')
claim={'claim_id':'A051-FINITE-VARIATIONAL-CRITICAL-SELECTION','version':1,'exact_statement':statement,
'hypotheses':['Finite uniform Boolean signs, entropy in bits, zero spectral potential terms defined as zero','Real K; epsilon>=0 for finite additive-deficit tolerance','Critical phase/child eligibility requires least essential dimension among all Boolean K-violators','Boundary edges undirected; vertex edits may retain the same dimension and are not physical restrictions'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['fleet05/A051'],
'proof_source':{'path':str(R/'VARIATIONAL_SELECTION.md'),'sha256':sha(R/'VARIATIONAL_SELECTION.md'),'locator':'Sections1--4'},
'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_NARROW_NECESSARY_CONDITION_EXACT_REPLAY_PENDING_INDEPENDENT_AGENT_REVIEW',
'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['claude/B11','A052','A055','A090','A094','B20']}
save('CLAIMS.json',[claim])
s52=B/'agents/A052/runs/20261014T044609Z-fleet05-A052-critical-source-structure'
s53=B/'agents/A053/runs/20261014T052310Z-fleet05-A053-near-tensor-perturbations'
s55=B/'agents/A055/runs/20261014T064016Z-fleet05-A055-extremal-obstruction-referee'
sources=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),B/'BOARD.md',B/'claude/B11/STREAM_NOTES.md',s52/'WEAK_CRITICAL_PROOF.md',s52/'CLAIMS.json',s53/'REPORT.md',s55/'PROOF.md',A/'runs/20261014T041948Z-fleet05-A051-near-extremizer-definition/code/save_records.py']
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
save('out/REVIEW_RECORDS.json',[{'claim_id':'A052-CRITICAL-WEAK-INFLUENCE-GIBBS-BANK','version':1,
'statement_sha256':'071f8d6e4c03af52dd754d3e2581a11f2b41074e518a160c60988b4a6f7402f0','reviewer':'fleet05/A051','verdict':'HOLDS_SECTIONS1_TO3_NEW_LOCALIZATION_AND_GIBBS_BANKS',
'review_source':str(R/'REVIEW_A052.md'),'review_sha256':sha(R/'REVIEW_A052.md'),'repair_supplied':False,'contributor_conflict_on_new_sections':False,
'scope_exclusion':'Section4 collision corollary has an A051-authored earlier premise; no fresh independent full-chain acceptance claimed','registry_adoption_verified':False}])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B11','packet_id':'A051','gap_id':'B11-UNIVERSAL-PROPER-BLOCK-SELECTION',
'attempt_id':'A051-stage6-finite-variational-selection','method':'Review compatible Gibbs banks; change mechanism to finite maximal-deficit selection and Boolean vertex-edit entropy curvature; exact all-edit certificates and separate direct-character replay',
'mathematical_delta':'Finite minimal witness selected with simultaneous all-vertex-cut constraints. Universal edit entropy bound has constant8/ln2; exact signed boundary influence; near-extremality error2^n epsilon/4; all child caps retained.140390 assertions PASS. No paid universal query.',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; supervisor mirror unverified','mathematical_status':'FINITE_EXTREMALITY_SELECTION_AND_NECESSARY_VARIATIONAL_CONSTRAINT_PROVED; UNIVERSAL_BLOCK_PAYMENT_AND_FEI_OPEN',
'claim_versions_used':['A052-CRITICAL-WEAK-INFLUENCE-GIBBS-BANK@1 sections1--3 independently reconstructed; section4 excluded from full-chain independence','A053 stage5 REPORT source receipt only','A055 stage5 PROOF admission context only'],
'claims_created_or_changed':['A051-FINITE-VARIATIONAL-CRITICAL-SELECTION@1','A052-CRITICAL-WEAK-INFLUENCE-GIBBS-BANK@1 scoped review'],
'source_artifacts':['VARIATIONAL_SELECTION.md','REVIEW_A052.md','out/FROZEN_SPEC.json','out/SUMMARY.json','out/SOURCE_MANIFEST.json','out/REVIEW_RECORDS.json'],
'next_consumers':['claude/B11','A052','A055','A090','A094','B20'],
'next_action':'Compare the signed vertex-cut constraint against actual parity-minus-refund pair cost on the same finite minimal witness with complete D+S_pair bank; preserve signed boundary and one influence owner.',
'stagnant_substantive_attempts':0,'blockers':['No bound relating entropy potential to an affordable actual pair/block','New narrow necessary-condition result awaits independent-agent review','Supervisor mirror/index adoption unverified'],'packet_ids':['A051']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(A/'STATUS.md').write_text('STATE: A051 stage6 saved: finite maximal-deficit minimal witness selected; all signed vertex-cut constraints proved with8/ln2 entropy error and exact boundary; epsilon error2^n epsilon/4;140390 exact checks PASS; scoped A052 Gibbs review; FEI OPEN.\nNEXT: A052/A055 compare Boolean signed-cut entropy potential with actual pair parity-minus-refund residual using SAME D+S_pair bank and one influence owner; A090/A094 review finite selection and curvature factors.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 08:52 UTC ('+R.name+'): Read BOARD/B11/status and A052 compatible Gibbs banks, A055 giant-component admission, A053 near-code exclusion. Independently reconstructed A052 new sections1--3, explicitly excluding authored-premise collision corollary from whole-chain review. Changed mechanism to finite maximal-deficit selection within least violating dimension. Proved universal entropy edit curvature bound8/ln2, exact signed boundary influence and all-set stationarity with explicit2^n epsilon/4 tolerance. Zeros handled by continuous derivative. Frozen n0..3 all278 tables,65808 edit pairs and K1..4;134376 pilot+6014 separate direct-character assertions PASS in1.363sec. Parity K3 analytically guards against applying stationarity to arbitrary roots. Saved proof, review, four schema files, receipts and rolling records. No universal block payment or external mirror claimed.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n- Stage6 finite extremality: if a K-violation exists, select least essential n, then maximum D_K over all n-bit Boolean tables. All smaller Boolean phases/children remain nonviolating and every same-dimension vertex edit is nonimproving. This is finite selection, not existence of an unbounded-dimension optimizer. Finite caps b_K(n) tensor-superadd and govern exact physical child transport.\n- Universal entropy edit bound: H(f^E)-H(f)>=4E[1_E f G_f]-(8/ln2)|E|/2^n, G_f=sum ahat log2(ahat^2)chi. Proof: -t^2log2(t^2)+3t^2/ln2 convex on[-1,1], including zero, then Parseval. Influence edit exact=(2/2^n)sum crossing-undirected-edge f(x)f(y).\n- Finite epsilon-extremality gives sum_E fG <=(K/2)signed_boundary+(2/ln2)|E|+2^n epsilon/4. Exact critical selected witness has fG+K pivotal_degree<=Kn/2+2/ln2 pointwise. Near-extremality must specify tolerance: singleton error vanishes only for epsilon=o(2^-n). Three-bit parity K3 violates this stationarity, hence Booleanity or root-hardness alone does not imply it.\n- Stage6 140390 exact assertions across all278 tables n0..3 and65808 ordered edit pairs PASS, with6014 separate-representation checks. A052 compatible Gibbs sections1--3 independently hold; no fresh independence claimed for its collision corollary using an A051 premise. Next unresolved link is entropy potential versus actual signed pair residual with the SAME critical child bank, not another root-only structural class.\n')
protocol=json.loads(sources[0].read_text())
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
report=(R/'REPORT.md').read_text();assert all('# '+v in report for v in protocol['required_per_run']['report_fields'])
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
summary=json.loads((R/'out/SUMMARY.json').read_text());assert summary['assertions']==140390
save('out/HANDOFF_CHECK.json',{'schema':'PASS','exact_assertions':140390,'byte_identical_delta':True,'rolling_lines':2,'independent_agent_review':'PENDING','mirror_verified':False})
files=[p for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save('out/ARTIFACT_MANIFEST.json',{'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'external_mirror_verified':False})
print(json.dumps({'status':'SAVED_SCHEMA_PASS','files':len(files),'claim_sha256':claim['statement_sha256']}))
