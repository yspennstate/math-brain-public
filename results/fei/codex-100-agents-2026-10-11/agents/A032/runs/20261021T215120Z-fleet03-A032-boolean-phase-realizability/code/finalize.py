from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
BASE=OWN.parents[1]; NOW=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
P=Path(r'math-open-problems/reports\fei-2026-10-11')
S=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
EXT=BASE/'agents/A079/runs/20261021T153136Z-fleet03-A079-correlated-auxiliaries'
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
source=json.loads((EXT/'CLAIMS.json').read_text(encoding='utf-8'))[1]
review={'reviewer':'A032','at':NOW,'verdict':'HOLDS_AT_STATED_SCOPE','source':str(R/'REVIEW_A079.md'),'method':'Independent direct character sums, physical edges, prime-log/L1 identities, tensor reconstruction; author code not imported','formal_verification':'NOT_CLAIMED; core numeric target runtime unverified'}
source['review_records']=source['review_records']+[review]
source['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A032_LOCAL_REGISTRY_ADOPTION_UNVERIFIED'
statement=('For a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1], b=1-a^2 on four uniform physical bits u and EVERY Boolean seed h on any disjoint finite uniform cube, F_h=a+z*b*h is Boolean. For EVERY adaptive tree T querying only unassigned u bits, stopping at any chosen nodes and keeping z and seed variables unqueried, the weighted sum of actual entropy drops minus four times actual queried influence has sharp maximum 1-(9/16)log2(3), strictly between1/10 and1/8, attained by querying u bit weight1 then stopping. Both complete terminal spectra are retained: at each partial assignment s, H(F_h|s)=H(F_1|s)+beta_s H(h), I(F_h|s)=I(F_1|s)+beta_s I(h), beta_s=E[b|s]; expected leaf beta remains3/8. A single1/8 reserve from original structural component7/2+(9/16)log2(3) pays all such stopping costs without assuming4I(h)>=H(h). The root physical query of u bit weight8 has influence1/2, entropy drop(9/8)log2(3)-1 and rate2 release>1/5; its child influences are7/4+3I(h)/8 and3/2+3I(h)/8. Entropy units are bits. No arbitrary seed query, prescribed nonflat-reference reset or universal FEI bound is asserted.')
new={
'claim_id':'A032-FIXED-SIBLING-CONTROLLER-STOPPING-TRANSPORT','version':1,
'exact_statement':statement,
'hypotheses':['Actual displayed Boolean completion on original independent uniform physical coordinates','Arbitrary Boolean seed h, including constants and biased seeds; no seed FEI hypothesis','History queries only the four original u bits, never z or seed; all adaptive trees and stopping cuts allowed','Complete child/terminal spectra retained; one original structural reserve without renewal','Entropy bits; total influence in original physical coordinates'],
'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
'contributors':['A032'],
'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'certificates':['out/controller_fixtures.json','out/controller_transitions.json','out/controller_stopping.json','out/validation.json','out/replay.json'],'formal_verification':'RUNTIME_UNVERIFIED; submitted core integer inequalities are only a partial translation'},
'proof_dependencies':[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'acceptance':'independently reconstructed by A032 here; exact displayed truth row also checked directly'}],
'review_records':[],
'status':'EXACT_CONTROLLER_CERTIFICATE_ALL_SEED_PROOF_PENDING_INDEPENDENT_REVIEW',
'supersedes':[],'refutes':[], 'first_unproved_line':None,
'next_consumers':['A079','A034','A088','A094','A096','A097','B07-lead','B20']}
claims=[source,new]
fields=protocol['required_per_run']['claim_fields']
for c in claims:
    assert set(c)==set(fields),(set(c)-set(fields),set(fields)-set(c))
    assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
write(R/'CLAIMS.json',claims)
progress={
'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B07','packet_id':'A032',
'gap_id':'G-PHASE-COND','attempt_id':'A032-stage17-controller-history-original-reserve-v1',
'method':'Consume/review A079 obstruction; exact actual-Boolean controller restrictions and independent all-tree integer-power certificate',
'mathematical_delta':'A079 fixed nonfair sibling embedding independently HOLDS; all arbitrary-seed controller stopping cuts paid by one original1/8 structural reserve, sharp cost delta=1-(9/16)log2(3). First weight-eight physical query paid at rate2;10 local rate4 failures kept. Universal seed/reference payment remains open.',
'deliverable_status':'COMPLETE_LOCAL; independent acceptance, registry adoption and remote mirror unverified',
'mathematical_status':'SCOPED_EXACT_CERTIFICATE_AND_ALL_SEED_PROOF; FULL_FEI_OPEN; LEAN_RUNTIME_UNVERIFIED',
'claim_versions_used':[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'acceptance':'A032 independent reconstruction HOLDS'}],
'claims_created_or_changed':[{'claim_id':source['claim_id'],'version':1,'change':'local independent review appended'},{'claim_id':new['claim_id'],'version':1,'change':'new narrow controller certificate'}],
'source_artifacts':['PROOF.md','REVIEW_A079.md','FROZEN_SPEC.json','REPLAY_SPEC.json','AUDIT_EXTENSION_SPEC.json','code/check.py','code/replay.py','out/validation.json','out/replay.json','out/controller_fixtures.json','out/lean_output.txt','out/SOURCE_MANIFEST.json'],
'next_consumers':new['next_consumers'],
'next_action':'Use an actual sourced A096/A097 seed core with inherited nonflat reference and unused seed bank; expose its first seed bit, retaining both complete children, actual prior controller spend and both normalizers; pay prescribed reset from SAME remaining original source.',
'stagnant_substantive_attempts':0,
'blockers':['Universal arbitrary seed entropy/reference transport unpaid','New controller certificate external independent review pending','Lean numeric-target check timed out without verification','Supervisor copying, registry adoption and remote persistence unverified'],
'packet_ids':['A032']}
pfields=[s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(pfields)
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)

# Exact source hashes with explicit reading roles; background is not a new audit.
paths=[(Path(r'~\AGENTS.md'),'machine policy read; current user write boundary overrides shared bookkeeping'),(BASE/'BOARD.md','stage-start current peer frontier'),(BASE/'claude/B07/STREAM_NOTES.md','lead v2 direction, baseline already completed'),(OWN/'STATUS.md','prior stage checkpoint read before update'),(OWN/'LEARNED.md','prior durable mathematical scopes read before append')]
paths += [(P/f,'protocol full' if f=='EXECUTION_PROTOCOL.json' else 'campaign context and relevant B07/A032 or G-PHASE entries') for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [(S/f,'supplement context/scope read') for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [(p,'source introduction inspected; ONE_BIT_ENDPOINT norm arithmetic read in full; no novelty assumed') for p in (S/'sources').iterdir() if p.is_file()]
paths += [(p,'abstract and relevant intro/scope or threshold38 Proposition8.1; explicit cp1252 export, not new full-paper audit') for p in (BASE/'context').glob('*.txt')]
paths += [(EXT/f,'full source claim and proof independently reconstructed') for f in ['REPORT.md','PROOF.md','CLAIMS.json']]
paths += [(p,'prior substantive proof report read') for p in sorted((OWN/'runs').glob('*/REPORT.md')) if p.parent!=R]
manifest=[]
for p,role in paths:
    raw=p.read_bytes()
    encoding='cp1252' if p.parent.name=='context' else 'utf-8'
    txt=raw.decode(encoding)
    manifest.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding,'read_role':role})
write(R/'out/SOURCE_MANIFEST.json',manifest)
markers=[]
for p in sorted((OWN/'runs').glob('*/.final')):
    markers.append({'path':str(p),'sha256':sha(p),'text':p.read_text(encoding='utf-8')[:700]})
write(R/'out/PRIOR_MARKERS.json',markers)

(OWN/'STATUS.md').write_text('STATE: Stage17 complete locally: A079 fixed-sibling scope independently HOLDS; ALL238145 controller stopping trees paid from SAME original1/8 structural reserve;10226 exact checks PASS; Lean unverified; FEI OPEN.\nNEXT: A079/A088/A094 review; expose one sourced A096/A097 active seed bit with inherited reference, prior controller spend, both full terminals and SAME unused seed bank; no reserve renewal.\n',encoding='utf-8')
entry=f'\n{NOW} stage17: Consumed A079 fixed nonfair sibling obstruction and independently reconstructed all-seed entropy/influence/Renyi/dependence formulas. New controller theorem: sharp max stopping cost1-(9/16)log2(3) in(1/10,1/8), ALL238145 adaptive trees, SAME structural reserve1/8, complete seed terminals retained.9481 direct-transform/edge assertions plus745 independent FWHT/integer-power checks PASS. Initial incorrect equal-child-influence assertion rejected at check576; corrected to7/4 and3/2 base child influences, mean13/8.47 rate2 and10 rate4 local failures retained. Core Lean numeric target timed out, RUNTIME_UNVERIFIED; no formal certificate. Strict UTF8 paper decode failed; exports read explicitly cp1252. No git/messages/brain writes/GPU/background work, no other process stopped. NEXT inherited-reference active seed query from same source.\n'
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
lesson='\n\nStage17 (2026-10-21/22): A079 fixed nonfair sibling completion independently HOLDS, including full seed entropy, physical energy, signed Renyi cancellation and balanced tensor FEI reduction. A source-bound controller transport is possible without claiming arbitrary seed FEI: on its displayed16-entry a and b=1-a^2, every partial controller restriction obeys H=h_s+beta_s H(seed), I=i_s+beta_s I(seed), with beta conserved. ALL238145 adaptive four-controller-bit stopping trees have sharp max sum reach*(Delta-4Inf)=1-(9/16)log2(3) in(1/10,1/8); one ORIGINAL structural reserve1/8 pays them while both full terminals persist.10 local rate4 and47 local rate2 failures show a local-payment shortcut is false. First bit-weight8 query is paid at2 with release>1/5; its individual child base influences are7/4 and3/2, not their mean13/8. Independent exact histogram has28 cost values and1690 maximizing trees. Arbitrary seed/nonflat-reference query remains unpaid. ONE_BIT_ENDPOINT (Sept30) already has the dyadic mass proof; no novelty for rediscovery. Lean timeout is not a failed theorem or a formal certificate.\n'
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(lesson)

# Persistence is checked from the files the supervisor will copy.
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert (R/'REPORT.md').read_text(encoding='utf-8').rfind('# Universal bridge')>0
for key in protocol['required_per_run']['report_fields']:assert '# '+key in (R/'REPORT.md').read_text(encoding='utf-8')
v=json.loads((R/'out/validation.json').read_text(encoding='utf-8'));rr=json.loads((R/'out/replay.json').read_text(encoding='utf-8'))
assert v['PASS'] and rr['PASS'] and v['checks']+rr['checks']==10226
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024**2 for p in files)
receipt={'at':NOW,'protocol_fields_exact':True,'claim_statement_hashes_verified':True,'packet_delta_identical':True,'packet_ids':['A032'],'status_two_lines':True,'exact_checks':10226,'controller_trees':238145,'formal_rung':'RUNTIME_UNVERIFIED','local_only':True,'files':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]}
write(R/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'saved_files':len(files)+1,'largest_bytes':max(p.stat().st_size for p in files),'checks':10226,'claims':[c['claim_id'] for c in claims],'prior_marker_count':len(markers),'status':(OWN/'STATUS.md').read_text(encoding='utf-8')},indent=2))
