from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]; root=agent.parents[1]
registry=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((registry/'EXECUTION_PROTOCOL.json').read_text())
prior=agent/'runs/20261014T044820Z-fleet05-A062-influence-compensator'
old=json.loads((prior/'CLAIMS.json').read_text())[0]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj): (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
consumers=['A030','A038','A039','A057','A064','A087','A091','A094','B13','B20']
extension=(' Further shared-data tagged graft: for every finite Boolean seed a(z), arbitrary Boolean u(x),v(x) on the same shared data cube and fresh independent sign w, let M=(u+v)/2+w(u-v)/2, F=(u+v)/2+w*a(u-v)/2 and t=Pr[u!=v]. Exactly H(F)=H(M)+t H(a); seed queries have D_F=t D_a,d_F=t d_a; data queries have D_F=D_M,d_F=d_M=(d_u+d_v)/2 and zero drift of t*r_a. Given nonnegative C_a- and C_M-priced own-history potentials with zero constant leaves on declared finite trees, arbitrary finite adaptive interleavings respecting both trees and postponing w until the seed tree reaches its zero-reserve constant leaf have nonnegative potential R=t*r_a+r_M at price max(C_a,C_M). Their complete least reserve is at most R_root; at equal prices Q_C(F)<=t Q_C(a)+Q_C(M). Any finite stopped budget retains actual terminal H-R. For three-bit u negative at0 and v negative at0,2, querying data bit0 has t=1/8 and child t=1/4,0, while the independent-core mean-product proxy is5/16 with child mean1/4, producing false release1/16. Three-bit point-defect seed local debt at price4 exceeds1/8; tensor L copies and prescribe one untouched-coordinate query per copy first to obtain Q_4>=L ell. Thus the fake inherited-reserve release grows at least L ell/16 whereas actual release0. A030 independent-core transport is not refuted; tag-exposed collisions, arbitrary initial reserve payment and full FEI remain open.')
statement=old['exact_statement']+extension
hyp=['For retained version-4 conclusions only: '+h for h in old['hypotheses']]+[
 'New extension: finite uniform independent seed/data/tag blocks; two Boolean cores may share arbitrary physical data; bits entropy and ordinary influence',
 'Declared finite own-history seed and actual paired-profile trees, with nonnegative priced potentials zero at complete constant leaves; initial independent randomness fixed first',
 'Adaptive interleaving respects both trees; each shared data coordinate queried once; w postponed until the seed tree reaches its zero-reserve constant leaf, then sign-translated consistently',
 'Same supplied reserves and actual terminal functions are retained; no dimension-independent initial reserve bound or tag-exposed collision price assumed',
 'Tensor obstruction is a prescribed-policy reserve/accounting witness only, not an unbounded H/I Boolean family']
claim={'claim_id':old['claim_id'],'version':5,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A062; retained source credits unchanged; independent-core mismatch transport credited to A030'],
 'proof_source':{'extension':'DERIVATION.md','retained_version_4_proof':str(prior/'DERIVATION.md'),'retained_version_4_proof_sha256':sha(prior/'DERIVATION.md'),'retained_source_chain':old['proof_source'],'validation':'out/EXACT_SHARED.json'},
 'proof_dependencies':old['proof_dependencies'],'review_records':[],
 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':old['claim_id'],'version':4,'scope':'retain previous conclusions; extend actual-disagreement/profile reserve graft to shared data'}],
 'refutes':old['refutes']+['Replacing Pr[u!=v] by (1-Eu Ev)/2 for shared physical core data and treating its data-query drift as real inherited controller-reserve release'],
 'first_unproved_line':None,'next_consumers':consumers}
write('CLAIMS.json',[claim])
next_action='At the explicit unequal shared-core frontier, expose w while the seed is unfinished; derive and price the signed Fourier collision with the carried controller/profile reserves and both actual child terminal references. A087/A094 review general tagged graft.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'G-R-MISMATCH','attempt_id':'A062-shared-profile-graft-1',
 'method':'exact fresh-tag spectral sectors, actual joint-disagreement indicator martingale, nonnegative finite Bellman graft; unequal-core proxy obstruction and scoped independent transport review',
 'mathematical_delta':'General shared-core tagged graft Q_C(F)<=t Q_C(a)+Q_C(M); t actual disagreement is harmonic at shared-data queries. Independent-core proxy creates false release1/16 at an actual unequal non-flat query, amplified by tensor seed reserve. A030 independent-block harmonic transport independently HOLDS at stated scope.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'EXACT_SHARED_DATA_GRAFT_PROVED; FALSE_PROXY_EXTENSION_REFUTED; UNIVERSAL_C019_AND_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':4,'scope':'retained prior results/source chain; independent acceptance pending'},{'claim_id':'A030-CONDITIONAL-TWO-CORE-CONTROLLER-TRANSFER','version':1,'scope':'actual independent-core mismatch and inherited-controller data martingale only; independently reconstructed here; no bundled theorem used'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':5}],
 'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_NOTE.md','FROZEN_SPEC.json','out/EXACT_SHARED.json','out/TRANSPORT_REVIEW.json','out/SOURCES.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Independent reserve-candidate review pending; tag-exposed collision and universal initial reserve price open; supervisor adoption/mirror verification unconfirmed'],
 'packet_ids':['A062']}
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
sourceA030=root/'agents/A030/runs/20261014T032502Z-fleet05-A030-restriction-plateau-tests'
sources=[(root/'BOARD.md','stage-start board snapshot'),(root/'claude/B13/STREAM_NOTES.md','v2 lead direction'),(registry/'EXECUTION_PROTOCOL.json','complete protocol'),
 (prior/'DERIVATION.md','retained version4 proof'),(prior/'CLAIMS.json','retained v4 exact scope/source chain'),
 (agent/'runs/20261014T015800Z-fleet05-A062-influence-compensator/code/check_transfer.py','exact physical tree helper'),
 (agent/'runs/20261012T003951Z-fleet05-A062-influence-compensator/code/check_reserve.py','exact rational log helper'),
 (sourceA030/'PROOF.md','complete independent two-core source; mismatch transport review only'),(sourceA030/'CLAIMS.json','v1 exact scope/hash'),
 (root/'agents/A030/LEARNED.md','independent unequal-core work'),(root/'agents/A064/LEARNED.md','new global priority history work'),(root/'agents/A039/LEARNED.md','paired-profile work')]
write('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':s} for p,s in sources])
data=json.loads((run/'out/EXACT_SHARED.json').read_text()); review=json.loads((run/'out/TRANSPORT_REVIEW.json').read_text())
assert data['roots']==2150 and data['assertions']==24499 and review['assertions']==6400
assert data['failures']==review['failures']==0
(agent/'STATUS.md').write_text('STATE: A062 stage6 complete locally: shared-data tagged graft Q_C(F)<=Pr[u!=v]*Q_C(seed)+Q_C(actual profile); false independent-core proxy release1/16; 2150 mixed policies and scoped A030 transport review PASS; FEI OPEN.\nNEXT: Expose the fresh tag while seed unfinished at the unequal shared-core frontier; price its signed collision using carried controller/profile reserves and both actual child references; A087/A094 review general graft.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 12:48 UTC stage6: Read current board/B13/own state and consumed A030 unequal independent-core result rather than repeat it. Proved shared-data tagged spectral identity H(F)=H(M)+t H(seed), with actual t=Pr[u!=v], and full finite adaptive graft R=t*r_seed+r_actual_profile at max source prices. At shared-data queries t is harmonic, controller owner unchanged; no renewed profile credit. Explicit unequal non-flat three-bit cores yield fake mean-product release1/16 but actual0. Point-defect seed ell>1/8 and tensor argument amplify false reserve release arbitrarily, without FEI disproof. Pilot160 roots/1982 assertions PASS in0.05374s; final2150 policies/24499 assertions PASS in1.84093s,1419 rigorous dominance comparisons and731 boundary consistency comparisons distinguished from proofs. Scoped independent A030 mismatch/martingale review1024 queries/6400 assertions PASS in0.02280s. Extended existing candidate v5, no new broad review item. All protocol/rolling/persistence files saved; next tag-exposed collision and universal initial payment remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nFor ANY shared-data Boolean cores u,v and fresh independent sign w, M=(u+v)/2+w(u-v)/2 and F=(u+v)/2+w*a*(u-v)/2 satisfy H(F)=H(M)+Pr[u!=v]H(a). The disjoint fresh-w spectral sectors make this true for arbitrary bias and non-flat spectra. At seed queries D,d scale by t=Pr[u!=v]; data queries have the same D,d as actual M because t is the conditional probability of one fixed disagreement event and is harmonic.\nGiven prescribed nonnegative priced seed/profile reserves, R=t*r_seed+r_M transports them through finite adaptive interleavings at max prices, provided w waits until the seed tree reaches its zero-reserve constant leaf. This retains arbitrary controller difficulty and shared-profile difficulty; it does not price either initial account.\nShared-core data invalidate the independent-core proxy (1-Eu Ev)/2. For u negative{0},v negative{0,2} on3bits, querybit0 gives actualt1/8,childt1/4,0, but proxy5/16 and childmean1/4: false release1/16. General proxy drift beta_u beta_v/2. Tensor copies of3bit point-defect seed have prescribed reserve Q4>=L ell,ell>1/8, so the fake reserve release is unbounded while actual0. This is an account-substitution obstruction, not FEI disproof.\nA030 independent-block mismatch transport independently HOLDS at its stated scope: actual mismatch=(1-mn)/2, untouched mean fixed, own-history controller reserve unchanged and harmonic under one-block data exposure. No price22 or bundled interleaving theorem independently accepted in this review. The fresh-tag removal with unfinished seed is the exact remaining collision frontier.\n')
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
print(json.dumps({'schema_checks_passed':True,'final_validation_assertions':data['assertions']+review['assertions'],'extended_claim_version':5,'full_fei':'OPEN','files_receipted':len(receipts)},indent=2))
