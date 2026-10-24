from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]; root=agent.parents[1]
registry=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((registry/'EXECUTION_PROTOCOL.json').read_text())
prior=agent/'runs/20261013T221705Z-account05-A062-influence-compensator'
old=json.loads((prior/'CLAIMS.json').read_text())[0]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj): (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
consumers=['A005','A061','A064','A038','A065','A087','A094','B13','B20']
extension=(' Further arbitrary-core transfer: Fix any Boolean g on r>=0 bits, any vertex v, finite prescribed complete continuation trees for g and its one-vertex sign flip g^v, and finite price C>=0; write R=Q_C(g), Rv=Q_C(g^v). For G_q obtained by appending q>=0 dummy bits and flipping only (dummy=0,x=v), use dummy-first exposure and then these prescribed core trees. With d_q=2^(1-r-q), its complete reserve R_q satisfies |R_q-R|<=E_q=2^-q|Rv-R|+d_q*q*(r-1/2+C+3log2(e)+q/2). Thus R_q tends to R as q tends to infinity at fixed r,g,v,C and continuations. For F_q equal to (-1)^z g(x) except for a sign flip at (z=0,dummy=0,x=v), query fresh z first, followed by the corresponding core trees. Put delta_q=2^(-r-q). Its exact reserve is [D_z-C(1-delta_q)+(R_q+R)/2]_+ and |Q_C(F_q)-[R-C]_+|<=E_q/2+h2(delta_q)+(C+2log2(e))*delta_q. Hence Q_C(F_q) tends to [R-C]_+, retaining arbitrary core reserve rather than assuming zero. More generally opposite branches g and -h with disagreement mass epsilon obey Q_C(separator)<=[h2(epsilon)+2log2(e)*epsilon-C(1-epsilon)+(R_g+R_h)/2]_+ for declared nonnegative child reserve bounds. This query is locally paid for epsilon<=1/2,C>=6, but child reserves remain. No universal core-reserve or changing-core limit bound is asserted.')
statement=old['exact_statement']+extension
hyp=['For retained version-2 conclusions only: '+h for h in old['hypotheses']]+[
 'For the arbitrary-core extension: finite uniform Boolean cubes, bit entropy, ordinary influence; arbitrary fixed r>=0, vertex v, finite C>=0 and two finite prescribed complete physical core continuations',
 'Fresh q dummy bits; one actual output sign flip at their zero assignment and the core vertex v; dummy-first prefix is part of the specified rule',
 'Character family uses a fresh fair z coordinate queried first; its clean opposite branch follows the consistently sign-translated original tree',
 'Core, price and core continuations are fixed during the q limit; no terminal uniform integrability or varying-core passage is presumed',
 'R_g,R_h in the general separator bound dominate the reserves of the actual prescribed physical children; they are not discarded']
scalar=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\ERASURE_REDUCTION.md')
claim={'claim_id':old['claim_id'],'version':3,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A062; retained earlier source credits unchanged; terminal obstruction direction from A061/A005 and actual-boundary direction from A064'],
 'proof_source':{'extension':'DERIVATION.md','retained_version_2_proof':str(prior/'DERIVATION.md'),'retained_version_2_proof_sha256':sha(prior/'DERIVATION.md'),'retained_original_proof':old['proof_source']['original_proof'],'validation':'out/EXACT_TRANSFER.json'},
 'proof_dependencies':[{'source':str(scalar),'sha256':sha(scalar),'scope':'sections 1-2 exact D=B+JS, scalar min(d,1-d) bound; B<=h2(d) is binary conditional entropy monotonicity'},*old['proof_dependencies']],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':old['claim_id'],'version':2,'scope':'retain previous scoped conclusions and extend with arbitrary-core complete-reserve transfer'}],
 'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
write('CLAIMS.json',[claim])
next_action='At the first A064 controller reveal during nonconstant core exposure, compute the exact Bellman update with inherited core reserves and actual child continuations; price it from one unused physical account or retain the explicit residual. A087/A094 independently review fixed-core contraction.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'G-R-MISMATCH','attempt_id':'A062-arbitrary-core-character-transfer-1',
 'method':'finite Bellman contraction with explicit residual core reserves; symmetric scalar JS payment; scoped independent actual-controller boundary reconstruction',
 'mathematical_delta':'For arbitrary fixed Boolean cores and continuations, complete point-edit padded reserve converges to core reserve with explicit O(q^2*2^-q) error; edited fresh-character reserve converges to [Q_C(core)-C]_+; exact positive surviving reserve fixture; A064 boundary clause independently HOLDS.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'ARBITRARY_FIXED_CORE_TRANSFER_PROVED; UNIVERSAL_C019_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':2,'scope':'retained original scoped results; independent acceptance pending'},{'claim_id':'A064-TERMINAL-CORRECTED-GLOBAL-DEBT','version':2,'scope':'actual-boundary identity independently reviewed only; not new-proof premise'},{'claim_id':'A061-ARBITRARY-CORE-EDIT-ADMISSION','version':1,'scope':'terminal obstruction consumed through A061 review, not a logical premise'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':3}],
 'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_NOTE.md','FROZEN_SPEC.json','out/EXACT_TRANSFER.json','out/BOUNDARY_REVIEW.json','out/SOURCES.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Independent reserve candidate review pending; unused-source payment of general inherited core reserves open; supervisor adoption and remote mirrors unverified'],
 'packet_ids':['A062']}
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
sources=[(root/'BOARD.md','updated Oct14 01:51 UTC board'),(root/'claude/B13/STREAM_NOTES.md','v2 complete lead direction'),
 (registry/'EXECUTION_PROTOCOL.json','complete protocol'),(prior/'DERIVATION.md','retained scoped proof'),(prior/'CLAIMS.json','version 2 statement'),
 (agent/'runs/20261012T003951Z-account05-A062-influence-compensator/code/check_reserve.py','reused exact arithmetic kernel'),
 (root/'agents/A061/runs/20261014T012929Z-account05-A061-entropy-process/REVIEW_PROOF.md','complete signed-child review'),
 (root/'agents/A005/LEARNED.md','eligibility and corrected-price frontier'),
 (root/'agents/A064/LEARNED.md','controller boundary and no-reset direction'),
 (root/'agents/A064/runs/20261013T235917Z-account05-A064-global-debt-potential/DERIVATION.md','full prefix and actual-boundary proof; only boundary independently reviewed'),
 (root/'agents/A064/runs/20261013T235917Z-account05-A064-global-debt-potential/CLAIMS.json','v2 exact review scope'),
 (scalar,'sections 1-2 symmetric scalar JS source')]
write('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':scope} for p,scope in sources])
write('out/REVIEW_SCOPE.json',{'reviewer':'A062','claim_id':'A064-TERMINAL-CORRECTED-GLOBAL-DEBT','version':2,'verdict':'HOLDS_AT_STATED_SCOPE','scope':'two-dictator actual data frontier: retained H,I and consistently sign-translated prescribed-tree reserve equal half controller quantities; root controller influence equals I(h)/2','whole_bundled_claim_accepted':False,'proof':'REVIEW_NOTE.md','validation':'out/BOUNDARY_REVIEW.json'})
(agent/'STATUS.md').write_text('STATE: A062 stage 4 complete locally: arbitrary fixed-core complete reserve survives point-edit padding with explicit error; edited character reserve tends to [Q_C(g)-C]_+; 3356 exact assertions PASS; A064 boundary scoped HOLDS; FEI OPEN.\nNEXT: Price the first A064 controller reveal during nonconstant core exposure with inherited core reserves and actual child continuations, using one unused influence account; A087/A094 review fixed-core contraction.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 01:58 UTC stage 4: Read board, B13 v2, own status, A061 stage4 signed-child review, A005 frontier and A064 priced prefix/boundary proof. Changed from quadratic-class geometry to arbitrary fixed-core Bellman contraction. Proved |R_q-R(g)|<=2^-q|R(g^v)-R(g)|+2^(1-r-q)q[r-1/2+C+3log2(e)+q/2], and edited fresh-character reserve tends to [R(g)-C]_+. Symmetric scalar JS suffices; no pending MU dependency needed for new extension. Frozen 32-root pilot/332 assertions PASS. Final 420 roots/3041 exact assertions PASS in 0.884s; strict C1,q6 residual >=3/4 confirms terminal retention. Independently reconstructed A064 actual two-dictator boundary clause: 51 cases/315 assertions PASS; full bundled theorem not accepted. Extended existing reserve candidate to v3, saved schema/source/persistence receipts and rolling files. Full FEI and arbitrary controller/core payment remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nFor ANY fixed r-bit Boolean core g, vertex flip g^v, prescribed complete core trees and C>=0, dummy-first point-edit padding obeys R_j=[D_j-C*2^(1-r-j)+(R_(j-1)+R(g))/2]_+. It preserves full reserve: |R_q-R(g)|<=2^-q|R(g^v)-R(g)|+2^(1-r-q)q[r-1/2+C+3log2(e)+q/2]. This is fixed-core convergence, not a changing-core UI claim.\nAn edited fresh character (-1)^z g has d_z=1-2^(-r-q) and complete reserve tending to [R(g)-C]_+. The exact terminal/core account remains; one character spends at most its one price-C influence account. For general opposite branches g,-h, disagreement epsilon gives D<=h2(epsilon)+(2/ln2)epsilon and reserve bound [that-C(1-epsilon)+(R_g+R_h)/2]_+. Locally paid does not mean child reserve zero.\nA064 terminal-corrected global debt v2 actual two-dictator boundary clause independently HOLDS: frontier +1,-h,h,-1 has retained entropy/influence/prescribed reserve exactly half h quantities, and root controller influence I(h)/2. Full priced-prefix chain was not accepted by this scoped review.\n')
data=json.loads((run/'out/EXACT_TRANSFER.json').read_text()); review=json.loads((run/'out/BOUNDARY_REVIEW.json').read_text())
assert data['assertions']==3041 and review['assertions']==315
assert data['failures']==review['failures']==0
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
print(json.dumps({'schema_checks_passed':True,'exact_assertions':3356,'extended_claim_version':3,'full_fei':'OPEN','files_receipted':len(receipts)},indent=2))
