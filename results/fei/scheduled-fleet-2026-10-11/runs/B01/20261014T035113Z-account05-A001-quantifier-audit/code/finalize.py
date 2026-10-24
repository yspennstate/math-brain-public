from pathlib import Path
import json,hashlib,re
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];TEAM=OWN.parents[1]
SHARED=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def envelope(c):return hashlib.sha256(json.dumps(dict(statement=c['exact_statement'],hypotheses=c['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
protocol=read(SHARED/'EXECUTION_PROTOCOL.json');req=protocol['required_per_run']
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert re.findall(r'^# (.+)$',report,re.M)==req['report_fields']
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
physical=read(RUN/'out/PHYSICAL.json');symbolic=read(RUN/'out/SYMBOLIC.json')
assert physical['status']==symbolic['status']=='PASS'
assert physical['assertions']+symbolic['assertions']==4796
assert physical['cases']+symbolic['cases']==25
A096=TEAM/'agents/A096/runs/20261014T013836Z-account05-A096-live-gap-ledger'
A073=TEAM/'agents/A073/runs/20261014T023508Z-account05-A073-certified-logarithms'
A098=TEAM/'agents/A098/runs/20261014T024504Z-account05-A098-resource-reallocation'
sources=[(SHARED/'EXECUTION_PROTOCOL.json','full protocol execution-v2'),(TEAM/'BOARD.md','2026-10-14 03:46 UTC snapshot; dispatch'),(TEAM/'claude/B01/STREAM_NOTES.md','v1; completed argmin assignment'),
 (A096/'DERIVATION.md','correlated partner ownership/conditional binary repair, sections 2-5'),(A073/'REPORT.md','positive-erasure binary and explicitly partial reserve'),(A073/'DERIVATION.md','r=1 signed row; exact conditional likelihoods'),(A073/'CLAIMS.json','NONZERO-ERASURE-BINARY-REMAINDER@1'),(A098/'CLAIMS.json','full-scope A073 acceptance'),
 (OWN/'runs/20261014T011101Z-account05-A001-quantifier-audit/REPORT.md','prior normalized coarse-tail information-loss guard')]
save(RUN/'out/SOURCE_MANIFEST.json',[dict(path=str(p),locator=l,bytes=p.stat().st_size,sha256=sha(p)) for p,l in sources])
statement=('For every even d>=2 and integer r>=1, let b be the canonical d-bit quadratic bent sign, Q_r the product of r independent two-bit signs negative only at 11, and F=b+1_(y=0)(Q_r-1). Put delta=2^-d,t=sqrt(delta),alpha=2^-r,w=4^(1-r),e=delta/2,A=1-delta+2delta alpha^2,R_sigma=1+2sigma t(alpha-1)+delta[(alpha-1)^2+alpha^2], and D_y=sum_sigma N_sigma delta log2(A/R_sigma). Every selector influence is e and every core influence is a=1/2+delta(1-alpha). Retaining only a queried selector bit partner gives binary laws (1/2,1/2),(1-e,e) and total influence-weighted binary loss at least r delta(3d/8-1/2) for r>=2; at r=2^d this loss cannot be paid by a fixed multiple of one specified core influence. Retaining also the empty/nonempty occupancy of all other selector pairs gives complete four-cell laws (w/2,(1-w)/2,w/2,(1-w)/2) and (A,e(1-w),ew,e(1-w)). Its per-row loss is e w D_y/2, with 0<=D_y<=log2(3)<2, and its retained price is M_i^C/e=1+(w/2)[d+2r-1+log2 A]. Summing over ALL selectors, their retained prices plus discarded losses above total selector influence J=r delta cost less than (3/2)a, charged once to y_1. Consequently the enlarged root audit bill 2I_core+sum_selector(M_i^C+L_i^C)+J/ln2 is <=(7/2)I(F), and dominates B(F). All spectral atoms are positive and H(F)<=4I(F). This is a complete root-row ownership fixture, not a universal signed partition, hereditary terminal-child reserve, or FEI theorem.')
hyp=['Actual Boolean signs on the uniform physical cube; entropy/KL in bits and ordinary influence','Even d>=2; r>=1 disjoint selector pairs and the specified bent core, edited only at its zero vertex','Complete row laws are marginalized, never conditioned on derivative support; zero cells omitted continuously','The single owner y_1 is allocated its baseline plus the combined selector extra once; no hereditary terminal-child surplus is inferred']
claim=dict(claim_id='A001-SHARED-CORE-FOUR-CELL-OWNERSHIP',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256='',contributors=['A001'],proof_source=dict(path=str(RUN/'REPORT.md'),locator='complete derivation sections 2-6',validation=['out/PHYSICAL.json','out/SYMBOLIC.json'],immediate_derivation='DERIVATION.md'),proof_dependencies=[],review_records=[],status='SCOPED_ROOT_REFERENCE_LEDGER_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['All shared-core binary quotient losses for this family have a uniform payment by a fixed multiple of one core-coordinate influence'],first_unproved_line=None,next_consumers=['A096','A073','A098','A099','A004','A086','A094','B01','B20'])
claim['statement_sha256']=envelope(claim)
source=read(A098/'CLAIMS.json')[0]
assert source['claim_id']=='A073-NONZERO-ERASURE-BINARY-REMAINDER'
assert source['exact_statement']==next(c for c in read(A073/'CLAIMS.json') if c['claim_id']==source['claim_id'])['exact_statement']
claims=[claim,source];notes=[]
for c in claims:
 assert set(c)==set(req['claim_fields'])
 source_envelope=hashlib.sha256(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
 assert c['statement_sha256'] in (envelope(c),source_envelope,hashlib.sha256(c['exact_statement'].encode()).hexdigest())
 notes.append(dict(claim_id=c['claim_id'],recorded_hash=c['statement_sha256'],local_envelope_hash=envelope(c),exact_statement_key_envelope_hash=source_envelope,statement_only_hash=hashlib.sha256(c['exact_statement'].encode()).hexdigest(),source_record_preserved=True))
save(RUN/'CLAIMS.json',claims);save(RUN/'out/STATEMENT_HASH_NOTES.json',notes)
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B01',packet_id='A001',gap_id='C018/G-BOOLEANITY',attempt_id='A001-SHARED-CORE-FOUR-CELL-1',method='Consume reviewed A073 conditional row; exact multi-pair ownership challenge; retain empty-selector event; pay retained quotient and lost KL together from one original root influence partition',mathematical_delta='Binary-only repeated-owner loss unbounded; exact four-cell refinement restores conditional likelihood information and its complete combined root ledger costs <=7/2 I for all d,r; no recursive terminal-slack inference. A098 full-scope A073 acceptance consumed.',deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION',mathematical_status='SCOPED_OWNERSHIP_FIXTURE_CLOSED_PENDING_REVIEW; UNIVERSAL_PAYMENT_AND_FEI_OPEN',claim_versions_used=['A073-NONZERO-ERASURE-BINARY-REMAINDER@1 (independently accepted by A098; r=1 scope retained)','A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 (conditional information guard; source read)','Known complete retained-KL and lower-edge bound (reconstructed)'],claims_created_or_changed=['A001-SHARED-CORE-FOUR-CELL-OWNERSHIP@1','A073-NONZERO-ERASURE-BINARY-REMAINDER@1 (existing A098 acceptance consumed, no new review assertion)'],source_artifacts=['REPORT.md','DERIVATION.md','out/FROZEN_SPEC.json','out/SOURCE_MANIFEST.json','code/check.py','out/PHYSICAL.json','out/SYMBOLIC.json','out/OUTPUT_CORRECTION.json','out/STATEMENT_HASH_NOTES.json'],next_consumers=claim['next_consumers'],next_action='On a non-flat core retain the actual empty-selector conditional reference and fund joint retained price/remainder with one genuinely unused certified child surplus, rather than the fixture root row quota.',stagnant_substantive_attempts=0,blockers=['Flat-core likelihood bound and influential marked root owner do not supply general signed partition or available terminal-child slack','R_ge2<=K I and full FEI remain unproved','New fixture independent review and supervisor adoption pending; broad-candidate cap remains active'],packet_ids=['A001'])
assert set(progress)=={x.split(' (')[0] for x in req['progress_fields']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
(OWN/'STATUS.md').write_text('STATE: Stage 5 saved: shared-core binary losses defeat one repeated owner; four-cell quotient pays retained price plus all remainders in one root ledger <=7/2 I; 4,796 exact checks PASS; FEI OPEN, new claim review pending.\nNEXT: A086/A094 review; A096/A073/A001 replace flat-core ratios and root quota by an actual non-flat conditional reference with genuinely unused certified child surplus and full terminal debt.\n',encoding='utf-8')
entries={'WORKLOG.md':'2026-10-14 03:51 UTC stage: Read BOARD/B01/STATUS, consumed A098 full-scope A073 binary-remnant acceptance. Extended one edited gate to r product pair gates sharing a bent vertex; binary losses at r=2^d cannot use one bounded owner. Kept partner plus selector-vacuum flag: four-cell normalized quotient now pays its retained price AND all discarded KL in one root rate7/2 influence ledger, every d,r. Nine physical and sixteen symbolic cases passed4,796 exact assertions; fixed a displayed symbolic lower-bound prefactor, preserving correction. No universal terminal slack claimed; FEI OPEN.\n','LEARNED.md':'Shared-core quotient guard: for edited bent core and Q_r product AND2 signs, delta=2^-d,alpha=2^-r,w=4^(1-r),selector e=delta/2,core a=1/2+delta(1-alpha). Binary partner quotient loses e D0/2 with D0>=3d/4-1 for r>=2; total at r=2^d grows >=3d/8-1/2 against one core a<=3/4. Retain partner AND empty/nonempty other-selector event: four cells have mu=(w/2,(1-w)/2,w/2,(1-w)/2),r=(A,e(1-w),ew,e(1-w)),A=1-delta+2delta alpha^2. Remaining loss=e w D_y/2,D_y<=log2 3. Retained M^C/e=1+(w/2)(d+2r-1+log2 A). Combined selector extra above J=r delta is <delta(d/2+2)<=(3/2)a once, giving enlarged root B bill<=7/2 I with core baselines2 and selector baselines<5/2. This root quota is not certified hereditary terminal-child surplus. A073 r=1 dedicated reserve remains valid; the repeated-owner extrapolation fails.\n'}
for name,entry in entries.items():
 p=OWN/name
 if entry not in p.read_text(encoding='utf-8'):
  with p.open('a',encoding='utf-8') as f:f.write(entry)
assert len((OWN/'STATUS.md').read_text().splitlines())==2
artifacts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  artifacts.append(dict(path=str(p.relative_to(RUN)),bytes=p.stat().st_size,sha256=sha(p)))
result=dict(status='PASS',exact_assertions=4796,cases=25,protocol_fields='EXACT',statement_hashes='VERIFIED_SOURCE_SCHEMES_PRESERVED',compatibility_copy='BYTE_IDENTICAL',final_universal_bridge='PASS',size_cap='PASS',source_files=len(sources),artifacts=artifacts,rolling_files=[dict(path=str(OWN/n),sha256=sha(OWN/n)) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],full_FEI='OPEN',new_claim_review='PENDING',external_adoption='NOT_OBSERVED')
save(RUN/'out/PERSISTENCE_RECEIPT.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['artifacts','rolling_files']}))
