from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
old=R.parent/'20261026T193525Z-fleet04-A063-information-revelation'
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
prior=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))[0]
cid=prior['claim_id']; cons=['A061','A062','A064','A065','A087','A094','B13 lead']
statement=prior['exact_statement']+' In addition, for all nonempty disjoint physical blocks U,V and a new selector y, let F=(-1)^(y parity(U) parity(V)), d=1+|U|+|V|>=3. The ORIGINAL nonproduct reference Q has mass1/2 on vacuum and1/14 on each of the seven other atoms in span({y},U,V), zero elsewhere. For every adaptive physical query policy and stopping cut with actual transported references, fair zero-source extension, and NO resets, the sum of all reached erasure KL E and outcome KL O plus expected FULL terminal H and K is at most c=9/16+(7/16)log2(14)<9/4-1/64. The SAME original4I=d account pays that bill and any old debit omega<=I with residual>3(d-3)/4+1/64. At a selector-first cut the sparse rank-two child inherits (4/19,5/19,5/19,5/19), genuinely different from its uniform actual source, and all its continued physical histories are paid. Original product admission instead fails at the root under allowed old debit I, because every influence is1/4 and M=d h2(1/4)>3I; this is NOT a full FEI disproof. All version1 claims retain their original separate hypotheses.'
claim={
 'claim_id':cid,'version':2,'exact_statement':statement,
 'hypotheses':['uniform physical cube, base-two entropy/KL','version1 bent/inherited-reference and dense/sparse selector hypotheses preserved separately','new source family: F=(-1)^(y parity(U) parity(V)), U,V nonempty disjoint and y new','new ORIGINAL template: vacuum1/2, seven nonvacuum atoms1/14, no retroactive conversion from a spent product source','new policy: all adaptive physical queries and stopping; retain actual reference; no product resets; fair zero-source extension','full physical weighted E/O and both H/K terminals; old debit <= SAME original S/4','root product obstruction uses allowed old debit omega=I'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A063'],
 'proof_source':[str(old/'PROOF.md'),'PROOF.md sections1-4','out/main.json','out/independent.json'],
 'proof_dependencies':[cid+'@1'],
 'review_records':[{'reviewer':'A063','kind':'author analytic proof, full finite-history rational certificate, separate direct-character/edge implementation; not independent agent acceptance','artifacts':['out/main.json','out/independent.json'],'scope':'new original template source and all no-reset physical cuts; version1 unchanged; no Lean certificate'}],
 'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[cid+'@1'],'refutes':[],
 'first_unproved_line':None,'next_consumers':cons}
write(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B13','packet_id':'A063','gap_id':'G-R-MISMATCH',
 'attempt_id':'A063-original-nonproduct-eight-atom-inherited-deficient-v2',
 'method':'refute SAME4I original-product extension at root; supply explicit vacuum-plus-uniform-sector nonproduct original template and retain actual inherited sparse reference; exact full E/O/terminal stopping checks',
 'mathematical_delta':'Non-source-equal rank-deficient child paid from SAME original4I for all parity-block widths/all no-reset physical orders, with oldquarter/full E/O/H/K and reserve>1/64; original product extension fails at root; sharp marginal-rate guard. Main3630+independent168 exact assertions PASS; FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES; REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[cid+'@1'],'claims_created_or_changed':[cid+'@2'],
 'source_artifacts':['REPORT.md','PROOF.md','SEARCH_SPEC.json','code/template_audit.py','code/independent.py','code/IntegerCertificates.lean','out/pilot.json','out/main.json','out/independent.json','out/ADMISSION.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':cons,
 'next_action':'A087/A094 reconstruct explicit original CE and non-source-equal sparse transport. Price ONE necessary structured reference change outside the fixed eight-atom class from SAME unused original balance, or supply an original Booleanity-based vacuum/structured-sector CE=O(I). Do not repeat retained-history extension or mandatory-product assumption.',
 'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary-core influence-priced original template and necessary compatible return remain unpaid','Independent agent review of v1 and new v2 pending','Lean held: memok exit1 commit free6.1GB<8.0GB; scalar sources UNCOMPILED','Brain self-care stale/degraded; no affected personal note is evidence','Checklist working lock failure; completion registration attempted separately','Remote supervisor adoption unverified; no git or shared research mutations authorized'],
 'packet_ids':['A063']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
for name,code in [('pilot.json','template_audit.py'),('main.json','template_audit.py'),('independent.json','independent.py')]:
    result=json.loads((R/'out'/name).read_text(encoding='utf-8'))
    assert result['status']=='PASS' and result['script_sha256']==sha(R/'code'/code)
sources=[protocol_path,old/'PROOF.md',old/'CLAIMS.json',Path(r'BOARD.md'),Path(r'claude\B13\STREAM_NOTES.md'),Path(r'agents\A062\runs\20261027T081750Z-fleet04-A062-influence-compensator\REPORT.md')]
write(R/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
(A/'STATUS.md').write_text('STATE: Original nonproduct8-atom source pays non-source-equal rank-deficient child, ALL no-reset histories SAME4I/oldquarter/full E/O/H/K, reserve>1/64; original product4I fails at root; exact3630+168 PASS; review pending; FEI OPEN.\nNEXT: A087/A094 review v2 template/physical-chain; fund ONE necessary return beyond fixed8-atom class or ORIGINAL Booleanity-based structured-sector CE=O(I) from SAME unused owner; no renewed admission.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': '+R.name+': Extended v1 at actual non-source-equal deficient child: F=(-1)^yUV original Q=(1/2,1/14x7), complete CE c<9/4-1/64, SAME4I plus oldquarter/fullE/O/H/K for ALL retained physical histories. Original-product4I fails root M>3I; exact guard27<32. Actual sparse predicted=(4/19,5/19x3). Main3630/71queries/27states and direct-character168 PASS; pilot406 PASS. Memok exit1 commit6.1GB; Lean not launched. Checklist working lock failed. Full FEI OPEN; broader original supplier/independent review unpaid.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-27: For cubic parity-block phase (-1)^yUV, every physical influence1/4, actual spectrum(9/16,1/16x7). Original product full CE=M=d*h(1/4)>3I, so SAME original4I cannot also pay allowed oldquarter at root. Explicit ORIGINAL nonproduct template vacuum1/2, others1/14 pays full CE c=(9+7log2(14))/16<9/4-1/64 via14^28<2^107. Retaining actual references pays ALL adaptive physical E/O+terminalH/K from this ONE original source; bank4I oldquarter retains>1/64 for every width. Selector-first sparse inherited=(4/19,5/19x3), not source-equal, rank deficient for>=3data; optional product fee is positive but not necessary. Do not retroactively substitute this source into an already-spent product account. General original-template supplier remains unpaid; FEI OPEN.\n')
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='BUNDLE_MANIFEST.json':
        assert p.stat().st_size<20_000_000
        manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write(R/'out/BUNDLE_MANIFEST.json',manifest)
print(json.dumps({'status':'PASS','claim_version':2,'claim_fields':len(claim),'progress_fields':len(progress),'bundle_files':len(manifest),'scalar_certificates':{'27_lt_32':27<32,'14_pow28_lt_2_pow107':14**28<2**107}}))
