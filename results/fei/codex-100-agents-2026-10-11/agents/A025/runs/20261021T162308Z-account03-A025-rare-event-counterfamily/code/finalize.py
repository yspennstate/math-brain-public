from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def write(p,t): p.write_text(t,encoding='utf-8',newline='')
def js(p,v): write(p,json.dumps(v,indent=2)+'\n')
stmt=('For every even m>=4 and t>=0, on A025\'s bent-seed three-core family with x-conditional point edits at 0,e0, original controller weights (1/2,1/4,1/4), common point activation p=2^-t and delta=2^-m: query x and then y0 only in x=0. The second query has d=p(1/2+delta) and D<5d. The complete new remaining symmetric bank is R_new=p(3m-3+3t)delta/4. The genuine full terminal surplus S_new=8 IT_new-HT_new is at least p(3m+1+4t). The inherited old bank bound R_old=p(3m-1+3t)delta/4 and first-query debit U=max(D_x-10d_x,0)<=p*m*delta/2 obey R_old<=(delta/4)S_new, U<=(delta/6)S_new and R_new+U<=(5delta/12)S_new, without reissuing either original booking. A direct coincident-label single-edit controller proof pays every new terminal continuation at rate10, and the complete policy obeys 10 I(F)-H(F)>=2 IT_new+(1-5delta/12)S_new. At the next history x=0,y0=0, the y1 query has d=p delta, true spectral erasure B/d>=3/2+m/4 and released_R/d=3/2. Thus for every finite K,lambda>=0 an even m>4K+6(lambda-1) still refutes ONLY the local rule D<=K d+lambda released_R with no unused terminal surplus. The original family has H<6I and is not an FEI counterexample; no universal selected-policy or stopping-route refutation follows.')
claim={
 'claim_id':'A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO','version':2,
 'exact_statement':stmt,
 'hypotheses':['Uniform actual Boolean signs; entropy in bits; m>=4 even; t>=0 integer','Original three cores and original pi retained through data histories, even when two conditioned labels coincide','Second query is y0 in x=0; rebound query is y1 in x=0,y0=0','All siblings, controller probabilities, full terminal entropies and activation-direction bank capacity retained','The local rule being refuted excludes genuinely unused terminal surplus'],
 'statement_sha256':hashlib.sha256(stmt.encode()).hexdigest(),
 'contributors':['A025/account05 (original construction)','A025/account03 (continuation and rebound)','A021 (inherited explicit x-owner subclause)'],
 'proof_source':{'run_id':R.name,'proof':'PROOF.md','source_review':'REVIEW_A021.md','certificates':['out/DIRECT.json','out/SCALAR.json','out/REPLAY.json']},
 'proof_dependencies':[{'source':'A021 run20261014T075029Z/DERIVATION.md','version':2,'scope':'final x-query U bound and explicit original debit fractions; elementary two-controller mixture entropy bound','acceptance':'independently reconstructed in REVIEW_A021.md, exact scope only'}],
 'review_records':[], 'status':'AUTHOR_PROVED_AT_STATED_SCOPE_PENDING_INDEPENDENT_REVIEW',
 'supersedes':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@1 (strict extension; original local no-go unchanged)'],
 'refutes':['Same explicit all-constant LOCAL release-price rule after one paid intervening data query; no indexed universal source theorem refuted'],
 'first_unproved_line':None,
 'next_consumers':['A021','A023','A028','A029','A087','A094','Claude B05','B20']}
js(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B05','packet_id':'A025',
 'gap_id':'A025-SAME-OWNER-MIXED-DATA-CONTINUATION',
 'attempt_id':'stage6-paid-second-query-partner-rebound',
 'method':'Analytic exact edge/bank identities, signed single-edit row refund, complete terminal support certificate; integer Fourier and direct-DFT reproduction',
 'mathematical_delta':'Consumed A021 original x-owner; SAME original debit fractions survive second y0 data query; full coincident-label controller continuation paid at10; next y1 query restores unbounded local release-price obstruction.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_PENDING_SUPERVISOR_COPY_AND_REVIEW',
 'mathematical_status':'SCOPED_PROOF_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN; LEAN_RUNTIME_UNVERIFIED',
 'claim_versions_used':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@1','A021@2 final explicit x-owner subclause, source-bound review only'],
 'claims_created_or_changed':['A025-THREE-CORE-DATA-RELEASE-PRICE-NOGO@2'],
 'source_artifacts':['PROOF.md','REVIEW_A021.md','SEARCH_SPEC.json','REPLAY_SPEC.json','out/SOURCE_RECEIPTS.json','out/DIRECT.json','out/SCALAR.json','out/REPLAY.json','out/LEAN.md'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Pay next rare y1 query at x=0,y0=0 from one explicitly UNUSED portion of SAME S_new, retaining old U, opposite y0 child and all terminal bills.',
 'stagnant_substantive_attempts':0,
 'blockers':['No universal admission for arbitrary terminal surplus or arbitrary mixed histories','Independent review and downstream use pending','Lean bookkeeping attempt RUNTIME_UNVERIFIED; no formal certification'],
 'packet_ids':['A025']}
js(R/'PROGRESS.json',progress); js(R/'PACKET_DELTA.json',progress)
write(A/'STATUS.md','STATE: A025 stage6: SAME old x-debits survive paid second y0 query; full coincident-label continuation paid at10; y1 rare ratio rebounds;837+12 exact checks PASS; scoped review pending, FEI OPEN.\nNEXT: Pay x=0,y0=0 y1 query from SAME unused S_new with old U and opposite y0 sibling retained; A021/A029/A023/A028/A087/A094 review.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n'+stamp+' stage6/account03: consumed A021 explicit x-owner subclause. Proved paid y0 query and transport of original delta/4+delta/6 bookings to complete new surplus; proved needed coincident-label single-edit controller continuation. Next y1 query restores B/d>=3/2+m/4. Production837 and independent direct-DFT12 assertions PASS. Lean scalar attempt RUNTIME_UNVERIFIED; no certification. Source reading initially hit non-UTF8 paper text; explicit source decoding recorded. FEI remains OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n2026-10-21 stage6: On original three-core family after x=0, y0 query has d=p(1/2+delta), D<5d, full remaining R=p(3m-3+3t)delta/4. Complete three-leaf S_new>=p(3m+1+4t) retains both original delta/4 and delta/6 debit fractions, total<=5/192, without renewal. Distinct edits become coincident labels: prove singleton continuation separately (V=3eta/4, Hplus=V(2n+2), R=nV, IC=eta gives bill<R+6IC). At x=0,y0=0 partner y1 is seed-dummy: d=p delta, B/d>=3/2+m/4, release/d=3/2. Thus one paid data exposure does not guarantee every later query is paid. Next must retain same old U and opposite sibling. Lean check runtime unverified, prose proof only, independent review pending.\n')
protocol=json.loads((Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')).read_text(encoding='utf-8'))['required_per_run']
expected=set(protocol['progress_fields']); expected.remove('packet_ids (one primary ID, for compatibility)'); expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['claim_fields'])
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
receipts=[]
for p in R.rglob('*'):
 if p.is_file():
  assert p.stat().st_size<20_000_000,str(p)
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
js(R/'out/ARTIFACT_CHECK.json',{'status':'PASS','protocol_keys':'exact','compatibility_copy':'byte-identical','claim_digest':'PASS','max_file_bytes':max(x['bytes'] for x in receipts),'files':receipts,'independent_review':'PENDING','external_copy':'NOT_CLAIMED'})
print(json.dumps({'status':'PASS','files':len(receipts),'claim':claim['claim_id']+'@2','max_file_bytes':max(x['bytes'] for x in receipts),'source_receipts':len(json.loads((R/'out/SOURCE_RECEIPTS.json').read_text(encoding='utf-8')))}))
