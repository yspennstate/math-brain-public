from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,t):p.write_text(t,encoding='utf-8',newline='')
def js(p,v):write(p,json.dumps(v,indent=2)+'\n')
direct=read(R/'out/DIRECT.json'); replay=read(R/'out/REPLAY.json'); lean=read(R/'out/LEAN.json'); mem=read(R/'out/MEMOK.json')
assert direct['status']==replay['status']=='PASS'
assert direct['node_states']==29160 and direct['query_edges']==75816
stmt=('For every even m>=4 and t>=0, use the original A025 bent three-core family with x-conditional flips at 0,e0, original physical two-bit controller pi=(1/2,1/4,1/4), common width-t point activation p=2^-t and delta=2^-m. Query x first, and then take any finite adaptive restriction tree on y,A,B, keeping balancing z and activation coordinates unqueried. At every cut T retain complete original terminal ancestry and conditional physical label weights. Let IT_T,HT_T be the full terminal averages, H_T the actual node entropy average, L_T=H_T-HT_T>=0, S_T=8IT_T-HT_T, and E_T=10(Pi_D+Pi_C)-(H_0-H_T), with query costs measured after x. Then A_T=S_T+E_T=S_0+2Pi_D+10Pi_C-L_0+L_T exactly. The same symmetric bank contracts: R_T<=R_0. On this family S_0>=p(3m+1+4t), R_0=p(3m-1+3t)delta/4, U_x=max(D_x-10d_x,0)<=pm delta/2 and L_0<=R_0+10p delta. The original delta/4 bank and delta/6 U_x allocations plus ONE additional loss buffer delta/4+10delta/(3m+1+4t) of the same S_0 total at most7/78, without renewal. Therefore A_T-R_T-U_x>=(71/78)S_0+2Pi_D+10Pi_C. Every remaining-controller completion is paid by R_T+10IC_T, including coincident labels, partially revealed controllers and zero-dimensional point cores. The full stopping policy obeys 10I(F)-H(F)>=2IT_T+(71/78)S_0. At the all-data final cut S_final=8p(1+t)-A(t) still collapses, but actual earned E_final>=4pm-L_0. This pays the exact A021 final-cut obstruction with ancestor credit; it does not refute its current-terminal-fraction counterexample or change the known family H<6I. General source admission, prescribed reference conversion and full FEI remain open; queries of z or activation bits are outside this specialization.')
consumers=['A021','A022','A023','A028','A029','A087','A094','Claude B05','B20']
claim={
 'claim_id':'A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO','version':3,'exact_statement':stmt,
 'hypotheses':['Actual uniform Boolean signs; bits entropy; even m>=4; t>=0 integer','Original physical labels and all siblings retained, using actual conditional weights after controller exposures','Root x query precedes the account; U_x remains an external old debit','Further adaptive queries may use y,A,B only; z and point activation remain unqueried','Signed earned E_T includes the returning-query U_y; U_y is not charged again outside E_T','Universal identity is conditional on source admission; quantitative admission is proved only on this family'],
 'statement_sha256':hashlib.sha256(stmt.encode()).hexdigest(),
 'contributors':['A025/account05 (original family)','A025/account03 (all-cut source and signed-credit transport)','A021 (root owner and final-fraction obstruction)'],
 'proof_source':{'run_id':R.name,'proof':'PROOF.md','source_review':'REVIEW_A021.md','validation':['out/DIRECT.json','out/SCALAR.json','out/REPLAY.json']},
 'proof_dependencies':[{'source':'A021 run20261014T075029Z/DERIVATION.md','version':2,'scope':'ANY-seed two-edit controller theorem at fair controls; explicit original x-owner','acceptance':'source-bound reconstruction of used clauses only'},{'claim_id':'A021-SAME-OWNER-PARTNER-CONTINUATION','version':1,'scope':'paid returned-query prefix and final-fraction obstruction','acceptance':'independently reconstructed in REVIEW_A021.md; no repair'},{'claim_id':'A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO','version':2,'scope':'original bank and singleton controller specialization','acceptance':'prior author proof, independently accepted by A021 at its used scope'}],
 'review_records':[], 'status':'AUTHOR_PROVED_AT_STATED_SCOPE_PENDING_INDEPENDENT_REVIEW',
 'supersedes':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@2 (strict history extension; previous local no-go retained)'],
 'refutes':[], 'first_unproved_line':None,'next_consumers':consumers}
js(R/'CLAIMS.json',[claim])
next_action='Change to prescribed inherited-reference conversion: consume A022 nonflat tensor profile with original Q and unused t/64 bank, or A028 fixed-conversion source; retain BOTH terminal references, signed old debit and SAME ancestor account.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B05','packet_id':'A025','gap_id':'A025-SAME-OWNER-MIXED-DATA-CONTINUATION','attempt_id':'stage7-all-mixed-cuts-ancestor-signed-credit',
 'method':'Exact adaptive conditional-expectation identity, one ancestor source admission, point-profile controller specializations, exhaustive finite physical-node census and independent direct DFT',
 'mathematical_delta':'Crossed A021 final-terminal-owner collapse with SAME ancestor S0 plus actual signed E_T; all adaptive y,A,B cuts paid, leaving >=71/78 original source after bank and old x debit; no current-terminal fraction renewal.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_PENDING_REVIEW_AND_SUPERVISOR_COPY',
 'mathematical_status':'AUTHOR_PROOF_AT_STATED_SCOPE; FULL_FEI_OPEN; LEAN_HELD_FRESH_ADMISSION_FAILED' if lean.get('status')=='HELD_FRESH_ADMISSION_FAILED' else 'AUTHOR_PROOF_AT_STATED_SCOPE; FULL_FEI_OPEN; NO_FORMAL_CERTIFICATION_ASSERTED',
 'claim_versions_used':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@2','A021-SAME-OWNER-PARTNER-CONTINUATION@1','A021 run20261014T075029Z DERIVATION@2, used clauses only'],
 'claims_created_or_changed':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@3'],
 'source_artifacts':['PROOF.md','REVIEW_A021.md','SEARCH_SPEC.json','REPLAY_SPEC.json','LEAN_SPEC.json','out/SOURCE_RECEIPTS.json','out/HELPER_PROVENANCE.json','out/PILOT.json','out/DIRECT.json','out/SCALAR.json','out/REPLAY.json','out/MEMOK.json','out/LEAN.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal source admission and prescribed reference-conversion payment remain unproved','Independent acceptance, downstream use and external copying pending','Fresh memok exit1 prevented optional formal compiler; no Lean certification' if mem['returncode'] else 'Formal proof not claimed without trusted compiler/source/axiom receipt'],
 'packet_ids':['A025']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report=R/'REPORT.md'; text=report.read_text(encoding='utf-8')
if lean.get('status')=='HELD_FRESH_ADMISSION_FAILED':
 text=text.replace('The requested scalar formalization is code/Transport.lean. Fresh\ncompute admission and the exact compiler/helper outcome are saved in\nout/MEMOK.json and out/LEAN.json. No formal certification is claimed\nwithout a trusted source/compiler/axiom receipt. Its statement is only\ninteger bookkeeping, not the Fourier proof. The mathematical rung\nhere is author-checked proof pending independent review.',
 'The requested scalar formalization is saved in code/Transport.lean.\nFresh memok admission returned1, so NO compiler was started. Exact\nadmission output and the formal hold are saved in out/MEMOK.json and\nout/LEAN.json. The formal claim remains unresolved; no Lean certification\nis claimed. Its statement is integer bookkeeping, not the Fourier proof.\nThe mathematical rung is author-checked proof pending independent review.')
text=text.replace('Exact results and\nassertion counts are in out/REPLAY.json.',f'The independent replay passed{replay["assertions"]} exact assertions in{replay["seconds"]:.4f}seconds;\nresults are in out/REPLAY.json.')
write(report,text)
state=f'STATE: A025 stage7: SAME ancestor plus signed query credit pays ALL adaptive y/A/B cuts; >=71/78 original reserve retained;{direct["assertions"]}+{replay["assertions"]} exact assertions PASS; final collapse crossed; review pending, FEI OPEN.\n'
write(A/'STATUS.md',state+'NEXT: Consume A022 original-Q/t64 nonflat profile or A028 prescribed conversion; pay actual reference cost from SAME unused ancestor credit, BOTH terminal debts and old debits retained; A021/A029/A087/A094 review.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat(); marker='stage7/account03-all-mixed-cuts'
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n'+stamp+' '+marker+': consumed A021 paid partner and fixed-third-fraction obstruction. Proved exact S_T+E_T=S0+2Pi_D+10Pi_C-L0+L_T and one-time loss-buffer/source admission; ALL adaptive y,A,B cuts retain >=71/78 ancestor surplus after bank and old Ux. Controller specializations include n0, coincident labels and exposed controllers. Corrected one-controller pivot normalization in draft to IC=eta before pilot. Pilot14889, production'+str(direct['assertions'])+', independent direct-DFT'+str(replay['assertions'])+' assertions PASS. Fresh memok exit'+str(mem['returncode'])+'; formal compiler held if nonzero. New entropy mechanism complete on family; next prescribed reference conversion, universal FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n2026-10-23 stage7: Current-terminal fractions fail at full-data collapse (A021 m46,t0), but SAME ancestor S0 plus actual SIGNED earned E_T survives. For any finite shared-data physical controller, with actual data/controller reached costs, S_T+E_T=S0+2Pi_D+10Pi_C-L0+L_T, L_T>=0; R contracts under both query kinds. On A025 family root R<=delta*S0/4, old Ux<=delta*S0/6, root L0<=(delta/4+10delta/(3m+1+4t))*S0; total<=7/78. Hence every adaptive y,A,B cut has capacity after R and Ux >=71S0/78. Returning Uy is already inside E_T and must NOT be charged again. Final data S=8p(1+t)-A(t) shrinks but E>=4pm-L0. One-fair-controller single-point pair has IC=eta, V=eta (not eta/2); paired distinct edits have IC=V=2eta. Source admission and actual inherited reference-conversion costs remain the universal gaps; entropy identity does not pay external resets. Production29160 states/75816 edges/361942 assertions plus independent32 direct-DFT assertions PASS; fresh formal admission failed, no Lean claim.\n')
proto=read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
pf=set(proto['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(progress)==pf and set(claim)==set(proto['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('# '+h in text for h in proto['report_fields'])
assert 'Universal bridge' in text.split('\n\n')[-1]
assert hashlib.sha256(stmt.encode()).hexdigest()==claim['statement_sha256']
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='ARTIFACT_CHECK.json':
  raw=p.read_bytes();assert len(raw)<20_000_000,str(p)
  files.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
js(R/'out/ARTIFACT_CHECK.json',{'status':'PASS','progress_keys':'exact','claim_keys':'exact','report_fields':'all seven, ending Universal bridge','compatibility':'byte-identical','statement_sha256':'PASS','files':files,'max_bytes':max(x['bytes'] for x in files),'independent_review':'PENDING','external_copy':'NOT_CLAIMED'})
print(json.dumps({'status':'PASS','claim':claim['claim_id']+'@3','files':len(files),'production_assertions':direct['assertions'],'independent_assertions':replay['assertions'],'formal':lean.get('status','unverified'),'max_file_bytes':max(x['bytes'] for x in files)}))
