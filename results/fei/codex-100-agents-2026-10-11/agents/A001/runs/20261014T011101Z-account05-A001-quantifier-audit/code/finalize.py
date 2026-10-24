from pathlib import Path
import json,hashlib,re
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];TEAM=OWN.parents[1]
SHARED=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def envelope(c):return hashlib.sha256(json.dumps(dict(statement=c['exact_statement'],hypotheses=c['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
protocol=read(SHARED/'EXECUTION_PROTOCOL.json');required=protocol['required_per_run']
text=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert re.findall(r'^# (.+)$',text,re.M)==required['report_fields']
assert text.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
checks=[read(RUN/('out/'+n+'.json')) for n in ['REVIEW','COARSE','SYMBOLIC','TENSOR']]
assert all(x['status']=='PASS' and x['failures']==0 for x in checks)
assert sum(x['assertions'] for x in checks)==7860
assert sum(x['cases'] for x in checks)==144
A096=TEAM/'agents/A096/runs/20261013T220343Z-account05-A096-live-gap-ledger'
A073=TEAM/'agents/A073/runs/20261013T234148Z-account05-A073-certified-logarithms'
A098=TEAM/'agents/A098/runs/20261013T235014Z-account05-A098-resource-reallocation'
sources=[(SHARED/'EXECUTION_PROTOCOL.json','complete execution-v2'),(TEAM/'BOARD.md','2026-10-14 01:10 UTC; stage-start ownership'),(TEAM/'claude/B01/STREAM_NOTES.md','v1; completed argmin assignment'),
 (A096/'REPORT.md','terminal reference and gap'),(A096/'DERIVATION.md','equations 1-6 and cutoff proof'),(A096/'CLAIMS.json','TERMINAL-KL-REFUND-AUDIT@1'),
 (A073/'REPORT.md','independent refund acceptance and support mutation'),(A073/'CLAIMS.json','preserved original claim and A073 review'),
 (A098/'CLAIMS.json','A001 influence-only slice acceptance'),(TEAM/'agents/A031/LEARNED.md','signed carrier and carrier-only no-go duplication guard'),
 (OWN/'runs/20261013T213937Z-account05-A001-quantifier-audit/REPORT.md','prior mechanism audit and conserved joint reference')]
save(RUN/'out/SOURCE_MANIFEST.json',[dict(path=str(p),locator=loc,sha256=sha(p),bytes=p.stat().st_size) for p,loc in sources])

review=next(c for c in read(A073/'CLAIMS.json') if c['claim_id']=='A096-TERMINAL-KL-REFUND-AUDIT')
assert review['exact_statement']==next(c for c in read(A096/'CLAIMS.json') if c['claim_id']==review['claim_id'])['exact_statement']
review['review_records']=review.get('review_records',[])+[dict(reviewer='A001/account05',verdict='ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR',
 scope='Every finite Boolean seed including constants; finite tensor/parity/point activation, complete row and joint KL, all listed finite formulas, every fixed ell>=2 and finite nonnegative sublinear cutoff including nonmonotone cutoffs. No universal payment theorem accepted.',
 method='Independent complete-row likelihood-ratio and KL chain reconstruction; separately implemented direct physical flips/integer Walsh and exact prime-log identity checker; explicit cutoff-tail quantifier proof',
 proof_source=str(RUN/'REPORT.md'),locator='complete derivation section 1',validation_source=str(RUN/'out/REVIEW.json'),source_statement_sha256=review['statement_sha256'],reviewer_contributed_repair=False)]
review['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A073_AND_A001_LOCAL_ADOPTION_PENDING'

statement=('For every fixed integer L>=0, let C_L retain each residual Fourier subset T with |T|<=L separately and merge all |T|>L into one tail. On a finite uniform Boolean cube define mu_i(T)=p_(T+i)/e_i, r_i(T)=p_T+p_(T+i), D_i^L=D(C_L mu_i||C_L r_i) and M^L=sum_i e_i[log2(1/e_i)-D_i^L], omitting irrelevant coordinates. For n>=max(6,2L+2), let f_n be the n-bit one-point defect, e=2^(1-n), m=2^floor(n/2), and G_n=f_n^tensor(m). Every Fourier coefficient of G_n is nonzero and every physical influence equals e, so I(G_n)=mn e tends to zero. Its genuine H/I<4 and M/I<=2, but M^L/I>=floor(n/2)-2-beta(n-1), beta=e sum_(j=0..L)binom(n-1,j), which diverges. The exact lost refund is M^L-M=sum_i e_i mu_i(tail)D(mu_i(.|tail)||r_i(.|tail)), and therefore its ratio is at least floor(n/2)-4-beta(n-1). No auxiliary parity or dummy coordinates are used. This refutes a universal payment using fixed low-degree atom inspection and one undifferentiated normalized tail, or weaker partitions, not the complete row KL, adaptive or structurally refined tail references, or FEI.')
hyp=['Actual Boolean signs on finite uniform cubes, standard physical flip influence','Entropy and KL in bits; continuous zero conventions; relevant rows only','L fixed independently of n; n>=max(6,2L+2)','Complete mu_i and r_i probability laws are coarsened without conditioning on derivative support','Tensor factors use disjoint physical blocks; one-point sign is -1 at one point and +1 elsewhere']
new=dict(claim_id='A001-BOUNDED-DEGREE-REFUND-LOSS',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256='',contributors=['A001'],
 proof_source=dict(path=str(RUN/'REPORT.md'),locator='complete derivation sections 2-3',immediate_derivation=str(RUN/'DERIVATION.md'),validation=str(RUN/'out/TENSOR.json')),
 proof_dependencies=[],review_records=[],status='SCOPED_NORMALIZED_REFERENCE_OBSTRUCTION_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['For some fixed degree L, replacing complete retained KL by individually inspected low-degree atoms and one normalized tail gives M^L<=K I for all Boolean signs, even full-support signs of vanishing total influence'],
 first_unproved_line=None,next_consumers=['A096','A073','A099','A098','A031','A033','A086','A094','B01','B20'])
new['statement_sha256']=envelope(new)
prior=read(A098/'CLAIMS.json')[0]
assert prior['claim_id']=='A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION'
claims=[new,review,prior]
hashnotes=[]
for c in claims:
 assert set(c)==set(required['claim_fields'])
 hashnotes.append(dict(claim_id=c['claim_id'],version=c['version'],recorded_hash=c['statement_sha256'],local_envelope_hash=envelope(c),UTF8_statement_only_hash=hashlib.sha256(c['exact_statement'].encode()).hexdigest(),statement_and_hypotheses_unchanged_except_new_claim=True))
 assert c['statement_sha256'] in (envelope(c),hashlib.sha256(c['exact_statement'].encode()).hexdigest())
save(RUN/'CLAIMS.json',claims);save(RUN/'out/STATEMENT_HASH_NOTES.json',hashnotes)
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B01',packet_id='A001',gap_id='C018/G-BOOLEANITY',attempt_id='A001-BOUNDED-DEGREE-REFUND-1',
 method='Full-scope source review, complete normalized row/joint likelihood ratios, exact prime-log checks and a fixed-degree coarse-graining challenge strengthened to unpadded full-support vanishing-influence tensors',
 mathematical_delta='A096 terminal KL refund accepted at full original scope; A098 prior influence-only slice review adopted; normalized fixed-degree-plus-tail refund refuted by M^L/I>=floor(n/2)-2-beta(n-1) despite genuine M/I<=2 and H/I<4; exact lost within-tail KL isolated.',
 deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION',mathematical_status='SCOPED_MECHANISM_REFUTATION_PROVED_PENDING_REVIEW; A096_FULL_SCOPE_REVIEW_COMPLETE; FULL_FEI_OPEN',
 claim_versions_used=['A096-TERMINAL-KL-REFUND-AUDIT@1 (A073 and this independent full-scope acceptance)','A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1 (A098 influence-only slice acceptance consumed)','Known retained-KL normalizer and chain rule (reconstructed; not new claim)'],
 claims_created_or_changed=[c['claim_id']+'@'+str(c['version']) for c in claims],
 source_artifacts=['REPORT.md','DERIVATION.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/FROZEN_TENSOR_SPEC.json','code/check.py','code/check_tensor.py','out/REVIEW.json','out/COARSE.json','out/SYMBOLIC.json','out/TENSOR.json','out/STATEMENT_HASH_NOTES.json'],
 next_consumers=new['next_consumers'],next_action='Use a spectator-compatible conditional row quotient at the first non-product core, retaining the exact within-tail KL remainder and paying it once from original physical influence; A086/A094 review no-go.',
 stagnant_substantive_attempts=1,blockers=['Fixed bounded-degree refund mechanism fails; change to structural conditional tail information','Complete arbitrary seed divergence and R_ge2 payment remain open','New no-go independent review pending; B01 broad-candidate cap remains active'],packet_ids=['A001'])
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
(OWN/'STATUS.md').write_text('STATE: Stage 4 complete: A096 terminal KL audit independently HOLDS; fixed-degree refund loses unbounded within-tail KL on full-support Boolean tensors with I->0; 7,860 exact checks PASS; FEI OPEN, new no-go review pending.\nNEXT: A086/A094 review; A096/A073/A001 derive spectator-compatible conditional refund on a non-product row with complete Q, exact within-tail KL and one physical influence budget.\n',encoding='utf-8')
entries={
 'WORKLOG.md':'2026-10-14 01:11 UTC stage: Read updated BOARD/B01/STATUS, consumed A073 acceptance and independently reconstructed A096 full terminal/refund/cutoff claim. A098 prior influence-only slice acceptance adopted. Tested fixed low-degree atom inspection with one tail: exact activated-row mutation, then stronger unpadded full-support tensor no-go with I->0, H/I<4, true M/I<=2 but coarse bill/I>=floor(n/2)-2-beta(n-1). Exact within-tail KL loss isolated. Four frozen bounded jobs passed 7,860 assertions in 144 cases; no mathematical failures or heavy job. Full FEI remains open; no shared write.\n',
 'LEARNED.md':'Fixed-degree KL guard: coarse-graining each residual atom |T|<=L separately and all larger atoms into one tail preserves the full normalizer but loses mu_tail*D(conditional tail). For n>=max(6,2L+2), tensor m=2^floor(n/2) copies of an n-bit point defect: all Fourier coefficients nonzero, all influences e=2^(1-n), I=mn e->0, H/I<4 and M/I<=2. Yet coarse M/I>=floor(n/2)-2-beta(n-1), beta=e sum_(j<=L)binom(n-1,j)->0. Reference-tail mass lower bound comes from exactly one high-degree spectator: >=me/4. Complete row likelihood ratios tensor with an identical spectator law; marginalizing that spectator loses zero KL, unlike absolute-degree merging. A096-TERMINAL-KL-REFUND-AUDIT@1 independently accepted at full original scope; arbitrary core refund still unpaid. A098 independently accepts only prior influence-only reference slice, not every old bundled obstruction.\n'}
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
result=dict(status='PASS',exact_assertions=7860,cases=144,protocol_fields='EXACT',claim_hash_notes='VERIFIED_PRESERVED_SOURCE_SCHEMES',compatibility_copy='BYTE_IDENTICAL',final_universal_bridge='PASS',size_cap='PASS',source_files=len(sources),artifacts=artifacts,rolling_files=[dict(path=str(OWN/n),sha256=sha(OWN/n)) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],full_FEI='OPEN',new_claim_review='PENDING',external_adoption='NOT_OBSERVED')
save(RUN/'out/PERSISTENCE_RECEIPT.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['artifacts','rolling_files']}))
