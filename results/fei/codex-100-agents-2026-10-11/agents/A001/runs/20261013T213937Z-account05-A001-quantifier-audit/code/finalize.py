from pathlib import Path
import hashlib,json,re

RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parents[1]; TEAM=ROOT.parents[1]
SHARED=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((SHARED/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
fields=protocol['required_per_run']
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert re.findall(r'^# (.+)$',report,re.M)==fields['report_fields']
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
data=json.loads((RUN/'out/CHECK.json').read_text())
orbit=json.loads((RUN/'out/ORBIT_CHECK.json').read_text())
assert data['status']==orbit['status']=='PASS'
assert data['assertions']+orbit['assertions']==80050

A096=TEAM/'agents/A096/runs/20261011T234252Z-account05-A096-live-gap-ledger'
A098=TEAM/'agents/A098/runs/20261012T024601Z-account05-A098-resource-reallocation'
A015=TEAM/'agents/A015/runs/20261012T044229Z-account05-A015-minterm-barrier-analysis'
sources=[
 (SHARED/'EXECUTION_PROTOCOL.json','read in full; execution-v2'),
 (TEAM/'BOARD.md','stage-start board snapshot; A096/A098 frontier and ownership'),
 (TEAM/'claude/B01/STREAM_NOTES.md','v1; completed A001 argmin assignment'),
 (TEAM/'claude/B20/SYNTHESIS.md','sections 1,3,4'),
 (TEAM/'claude/B12/STREAM_NOTES.md','v2; no-reused-bank guard'),
 (A096/'REPORT.md','equations 1-7; sparse row; remaining line'),
 (A096/'CLAIMS.json','UNIVERSAL-LEVEL12-ERASURE@1'),
 (A098/'REPORT.md','independent layer review and allocation'),
 (A098/'CHECKPOINT_ALLOCATION.json','A001 all-degree budget assignment, A086 reviewer'),
 (A015/'REPORT.md','sections 3-5; exchangeable optimum'),
 (A015/'CLAIMS.json','CONDITIONED-MINTERM-LOCATION-BARRIER@1, optimum slice'),
 (ROOT/'runs/20261011T231625Z-account05-A001-quantifier-audit/REPORT.md','stage continuity; root calibration complete')]
save(RUN/'out/SOURCE_MANIFEST.json',[dict(path=str(p),sha256=digest(p),bytes=p.stat().st_size,locator=s) for p,s in sources])

statement=('For actual finite uniform-cube Boolean signs, the following proposed all-degree reference mechanisms cannot uniformly pay cross entropy or their stated majorants by total influence. On F_r=1+A_r(chi_{123}-1), r>=4, all r+3 influences equal delta=2^-r, H/I<4, and the complete derivative row of a data coordinate has all its energy delta at residual degrees >=2, contradicting a proposed all-degree bound 2 delta^2 ln(2/delta). The normalized nonempty product-influence reference Q(S)=prod_{i in S}Inf_i/[prod_i(1+Inf_i)-1] has nonempty cross entropy X/I>=r-2r/(r+3). On even-dimensional quadratic bent signs, B/I=2 while degree-weighted atom entropy/I=n and influence-weighted normalized derivative entropy/I=n-1. More generally, for every rule selecting a complete spectral subprobability reference using only the labeled influence vector and permutation-invariant metadata, for every integer w>=2 some coordinate permutation of OR of 2^w disjoint width-w point conjunctions has CE/I>=w/18. This last assertion also covers nonexchangeable reference rules; it does not exclude function-specific references or retained-KL corrections, and does not disprove FEI.')
hyp=['Actual Boolean signs, finite uniform cubes, standard physical influence','Entropy and ideal complete subprobability cross entropy in bits; natural logs explicitly ln','Product reference is on nonempty subsets and its actual nonempty spectral mass is retained','Influence-only rule gives the same reference for every Boolean realization with the same labeled influence vector and permitted invariant metadata','Coordinate permutation changes the function, while the equal-influence vector in the stated tribes family is unchanged','No claim that arbitrary conditional-edge references or function-specific spectral references have unbounded cost']
claim=dict(claim_id='A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION',version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest(),contributors=['A001'],
 proof_source=dict(path=str(RUN/'REPORT.md'),locator='complete derivation sections 2-5',validation=['out/CHECK.json','out/ORBIT_CHECK.json']),
 proof_dependencies=[],review_records=[],status='SCOPED_MECHANISM_OBSTRUCTION_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['All-degree extension of sparse degree-one derivative suppression','Uniform payment of the normalized product-influence nonempty reference','Uniform payment of all-degree upper-atom/complete-row entropy majorants','Universal complete spectral-reference cross entropy payment using only influences and invariant metadata'],
 first_unproved_line=None,next_consumers=['A045','A073','A096','A098','A099','A015','A086','A094','B01','B20'])
source=next(c for c in json.loads((A015/'CLAIMS.json').read_text()) if c['claim_id']=='A015-CONDITIONED-MINTERM-LOCATION-BARRIER')
source['review_records']=source.get('review_records',[])+[dict(reviewer='A001/account05',verdict='ACCEPT_EXCHANGEABLE_REFERENCE_OPTIMUM_IDENTITY_ONLY',
 scope='Only inf_Q exchangeable subprobability CE(P,Q)=H(|S|)+E log2 binom(n,|S|), and excess equals degree-conditioned location KL, for any finite subset probability law. No acceptance of the original bundled conditioning, ordered reference repair, regular-core transfer or their constants.',
 method='Independent permutation-orbit symmetrization and subprobability Gibbs reconstruction; REPORT.md section 5 equations (6)-(8)',proof_source=str(RUN/'REPORT.md'),source_statement_sha256=source['statement_sha256'],reviewer_contributed_repair=False)]
source['status']='AUTHOR_PROVED_PENDING_FULL_REVIEW; EXCHANGEABLE_OPTIMUM_SLICE_INDEPENDENTLY_ACCEPTED_BY_A001'
author_hash=source['statement_sha256']
assert author_hash==hashlib.sha256(source['exact_statement'].encode()).hexdigest()
source['statement_sha256']=hashlib.sha256(json.dumps(dict(statement=source['exact_statement'],hypotheses=source['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
save(RUN/'out/SOURCE_HASH_SCHEME.json',dict(source='A015-CONDITIONED-MINTERM-LOCATION-BARRIER@1',author_scheme='SHA256 UTF8 exact_statement only',author_hash=author_hash,local_scheme='SHA256 sorted compact JSON statement plus hypotheses',local_hash=source['statement_sha256'],statement_or_hypotheses_changed=False,first_finalize='Detected different source hashing convention before saving claims; no mathematical assertion failed'))
for c in (claim,source):
 assert set(c)==set(fields['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(json.dumps(dict(statement=c['exact_statement'],hypotheses=c['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
save(RUN/'CLAIMS.json',[claim,source])
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B01',packet_id='A001',gap_id='C018/G-BOOLEANITY',attempt_id='A001-ALL-DEGREE-REFERENCE-AUDIT-1',
 method='Consume reviewed A096/A098 dependency; reconstruct exact joint row normalizer and single budget; actual Boolean counterfamilies; permutation-orbit information bound and independent source-slice review',
 mathematical_delta='Audit complete: all-degree sparse support suppression and entropy majorants fail; normalized product-influence bill diverges on activated parity; every influence-vector-only complete spectral reference has CE/I>=w/18 on some permuted tribes; A015 exchangeable optimum slice independently accepted.',
 deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION',mathematical_status='SCOPED_MECHANISM_OBSTRUCTIONS_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 claim_versions_used=['A096-UNIVERSAL-LEVEL12-ERASURE@1 (reviewed by A098; frontier context)','A015-CONDITIONED-MINTERM-LOCATION-BARRIER@1 (exchangeable optimum slice independently reconstructed)','C018 retained-KL identity (reconstructed; known equivalence, no new claim)'],
 claims_created_or_changed=['A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1','A015-CONDITIONED-MINTERM-LOCATION-BARRIER@1 (scoped review record only)'],
 source_artifacts=['REPORT.md','DERIVATION.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/FROZEN_ORBIT_SPEC.json','code/check_reference.py','code/check_orbit.py','out/CHECK.json','out/ORBIT_CHECK.json','out/ORBIT_PILOT_FAILURE.json'],
 next_consumers=claim['next_consumers'],next_action='Audit a function-specific signed conditional-edge KL refund with one normalized joint reference and one cross-degree influence budget; retain activated-parity, bent and equal-influence permutation guards.',
 stagnant_substantive_attempts=0,blockers=['R_ge2<=K I remains unproved; no new universal layer paid','New diagnostic independent review by A086/A094 pending','B01 broad-candidate review cap remains active; this stage is a scoped audit and review'],packet_ids=['A001'])
assert set(progress)=={x.split(' (')[0] for x in fields['progress_fields']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()

(ROOT/'STATUS.md').write_text('STATE: Stage 3 audit complete: influence-only complete spectral references ruled out (CE/I>=w/18); product-prior and all-degree majorant failures checked; 80,050 exact assertions PASS; A015 optimum slice reviewed; FEI OPEN.\nNEXT: A086/A094 review; audit A096/A045/A073 function-specific conditional-edge KL refund with one cross-degree influence budget. Completed B01 argmin target is archived; new scope follows A098 allocation.\n',encoding='utf-8')
entries={
 'WORKLOG.md':'2026-10-13 21:39 UTC stage: Read updated BOARD/B01/STATUS and consumed A098 all-degree reference reallocation after completed local argmin work. Saved activated parity3 exact product-prior and sparse-row failures, bent all-degree entropy-majorant failures, and an all-parameter permutation-orbit no-go for every influence-vector-only complete spectral reference (CE/I>=w/18). Independently accepted A015 exchangeable optimum identity only. Two bounded jobs passed 80,050 exact assertions. Preserved and corrected signed-mean pilot sign error. Full FEI OPEN; no shared writes or heavy compute.\n',
 'LEARNED.md':'All-degree reference audit: mu_i(T)=p_(T+i)/Inf_i and q_i(T)=p_T+p_(T+i) are normalized; joint P(i,T)=p_(T+i)/I and Q(i,T)=(Inf_i/I)q_i(T) yield M/I=E_(Inf/I)log2(1/Inf_i)-D(P||Q), with M<=B<=M+I/ln2. Activated parity3 has all influences delta, H/I<4, but data derivative energy delta wholly above degree one and normalized product-influence nonempty CE/I>=r-2r/(r+3). Bent signs have B/I=2 but weighted atom and row entropy ratios n,n-1, so all-degree upper-atom replacement destroys necessary cancellation. Every complete spectral reference using only the labeled influence vector (even not permutation-equivariant) fails universal CE payment: equal-influence permuted width-w tribes force CE/I>=w/18. The permutation-averaged spectral law has H>=w^2/9 while I<=2w. Function-specific block/signed information or a retained-KL refund is essential; this does not refute edge coding or FEI. A015 exchangeable optimum slice independently accepted, bundled conditioning/ordered transfer not accepted by association.\n'}
for name,entry in entries.items():
 p=ROOT/name
 if entry not in p.read_text(encoding='utf-8'):
  with p.open('a',encoding='utf-8') as f:f.write(entry)
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  receipts.append(dict(path=str(p.relative_to(RUN)),bytes=p.stat().st_size,sha256=digest(p)))
assert len((ROOT/'STATUS.md').read_text().splitlines())==2
result=dict(status='PASS',exact_assertions=80050,protocol_fields='EXACT',claim_hashes='PASS',compatibility_copy='BYTE_IDENTICAL',final_universal_bridge='PASS',size_cap='PASS',sources=len(sources),artifacts=receipts,rolling_files=[dict(path=str(ROOT/n),sha256=digest(ROOT/n)) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],new_claim_independent_review='PENDING',full_FEI='OPEN',external_adoption='NOT_OBSERVED')
save(RUN/'out/PERSISTENCE_RECEIPT.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['artifacts','rolling_files']}))
