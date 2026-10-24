from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]; root=agent.parents[1]
registry=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((registry/'EXECUTION_PROTOCOL.json').read_text())
prior=agent/'runs/20261014T015800Z-account05-A062-influence-compensator'
old=json.loads((prior/'CLAIMS.json').read_text())[0]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj): (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
consumers=['A038','A039','A057','A061','A064','A065','A087','A091','A094','B13','B20']
extension=(' Further exact unfinished-core controller ownership: Let a be any finite Boolean seed, T any prescribed finite complete fresh-coordinate tree for it, C>=4, h=w*a with fresh independent sign w, and F=(1+h)u/2+(1-h)v/2 for disjoint parity cores u,v of at least two bits each. A fixed prefix reveals p parity coordinates while leaving each core nonconstant. Its actual frontier has complete reserve Q_C(a,T)/2 for the continuation T on seed coordinates, then w, then remaining parity coordinates; initial complete reserve including that prefix is [Q_C(a,T)-pC]_+/2. Each prefix query has D=0 and influence1/2; at every seed-query history H(F)=2+H(a)/2, D_i(F)=D_i(a)/2 and Inf_i(F)=Inf_i(a)/2. Selector probabilities remain1/2, variance-rarity reserve equals1 with controller release0, and parity-core reserves vanish. The terminal w query has D=2, influence1/2 and zero reserve precisely when C>=4. For the canonical B05 seed with even k>=4,r=2k, its selector D_s/Inf_s>=(1-2^-k)(k-2), which is preserved at the actual mixed-history lift node after a parity bit reveal. Thus a hypothetical price11 all-controller extension using only variance-rarity release and inherited parity-core reserves fails for every even k>=14; any fixed local price likewise fails eventually. A064 stated disjoint ordered-point theorem, other policies and full FEI are not refuted. The seed controller reserve is retained exactly, and preceding data costs cannot be reused at that node.')
statement=old['exact_statement']+extension
hyp=['For retained version-3 conclusions only: '+h for h in old['hypotheses']]+[
 'For new exact ownership: arbitrary finite uniform Boolean seed a and finite prescribed complete physical tree T; C>=4; entropy in bits, ordinary influence',
 'Fresh independent sign tag w, two disjoint nonempty parity cores on at least two coordinates, and no data/controller overlap',
 'Fixed p-query parity prefix leaves both cores nonconstant; declared controller continuation follows T on seed coordinates, then w, then selected remaining parity variables',
 'Phase changes from prefix outcomes are retained; both actual child continuations and terminal w-mux entropy are included',
 'Local no-go uses actual canonical B05 seed r=2k, tag w unqueried, and first seed-selector query at an unfinished-core frontier; it concerns a hypothetical all-controller extension, not the stated ordered-point theorem']
claim={'claim_id':old['claim_id'],'version':4,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A062; retained source credits unchanged; current controller gap and harmonic inherited-core clause credited to A064/A057'],
 'proof_source':{'extension':'DERIVATION.md','retained_version_3_proof':str(prior/'DERIVATION.md'),'retained_version_3_proof_sha256':sha(prior/'DERIVATION.md'),'retained_source_chain':old['proof_source'],'validation':['out/EXACT_OWNER.json','out/RAW_SEED.json']},
 'proof_dependencies':old['proof_dependencies'],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':old['claim_id'],'version':3,'scope':'retain previous scoped conclusions and extend exact controller owner at unfinished core exposure'}],
 'refutes':['Hypothetical extension to all non-point controller queries of D<=11d+release(sum q*r+sum q log2(1/q)Var), even with certified zero-reserve independent parity cores; not A064-REPEATED-FALLBACK-PRIORITY-GLOBAL-DEBT v1 at its stated ordered-point scope'],
 'first_unproved_line':None,'next_consumers':consumers}
write('CLAIMS.json',[claim])
next_action='At one A038/A039 unequal non-flat exposed priority query, graft the prescribed controller seed reserve into actual child continuations and compute the signed profile correction; keep initial capacity and consumed data debit separate. A087/A094 reconstruct complete half-transfer and failing node.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'G-R-MISMATCH','attempt_id':'A062-mixed-controller-owner-1',
 'method':'exact Boolean Fourier-sector half-transfer, finite Bellman induction, single-use prefix debit, compressed all-k actual local witness and scoped independent harmonic-core review',
 'mathematical_delta':'At unfinished parity-core exposure the complete controller reserve equals Q_C(seed,T)/2, initial prefix reserve=[Q_C(seed,T)-pC]_+/2 for C>=4. Variance-plus-core-only arbitrary-controller price fails with unbounded B05 seed selector rate at actual reached nodes. A064 core-weight harmonic clause independently HOLDS.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'EXACT_CONTROLLER_OWNER_PROVED_AND_HYPOTHETICAL_EXTENSION_REFUTED; UNIVERSAL_C019_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':3,'scope':'earlier conclusions retained; prior candidate independently unaccepted'},{'claim_id':'A064-REPEATED-FALLBACK-PRIORITY-GLOBAL-DEBT','version':1,'scope':'gap consumed and inherited-core harmonic term independently reviewed only; point price not assumed'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':4}],
 'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_NOTE.md','FROZEN_SPEC.json','out/EXACT_OWNER.json','out/RAW_SEED.json','out/HARMONIC_REVIEW.json','out/SOURCES.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Independent accumulated reserve-candidate review pending; pricing general inherited controller reserves and unequal-core profile correction open; supervisor adoption and mirrors unverified'],
 'packet_ids':['A062']}
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
sourceA064=root/'agents/A064/runs/20261014T030103Z-account05-A064-global-debt-potential'
sources=[(root/'BOARD.md','Oct14 04:40 UTC updated board'),(root/'claude/B13/STREAM_NOTES.md','complete v2 lead direction'),
 (registry/'EXECUTION_PROTOCOL.json','complete protocol'),(prior/'DERIVATION.md','previous complete reserve continuity'),(prior/'CLAIMS.json','retained version 3'),(prior/'code/check_transfer.py','reused exact physical-tree oracle'),
 (agent/'runs/20261012T003951Z-account05-A062-influence-compensator/code/check_reserve.py','rational logarithm kernel'),
 (root/'agents/A064/LEARNED.md','new priority closure and non-point gap'),(sourceA064/'DERIVATION.md','complete sections1-6; section4 harmonic core clause reviewed'),(sourceA064/'CLAIMS.json','A064 repeated-fallback v1 exact scope'),
 (root/'agents/A057/LEARNED.md','stage4 interleaved variance release and signed U'),(root/'agents/A057/STATUS.md','current conditional-controller transfer direction')]
write('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':scope} for p,scope in sources])
write('out/REVIEW_SCOPE.json',{'reviewer':'A062','claim_id':'A064-REPEATED-FALLBACK-PRIORITY-GLOBAL-DEBT','version':1,'verdict':'HOLDS_AT_STATED_SCOPE','scope':'inherited own-history core term sum q_j*r_j has zero fair controller-query drift only','whole_bundled_claim_accepted':False,'proof':'REVIEW_NOTE.md','validation':'out/HARMONIC_REVIEW.json'})
(agent/'STATUS.md').write_text('STATE: A062 stage5 complete locally: mixed-history controller reserve exactly Q_C(seed)/2, prefix debit [Q_C(seed)-pC]_+/2; variance/core-only all-controller price11 extension fails at an actual node; 4199 exact assertions PASS; FEI OPEN.\nNEXT: Graft controller seed reserve at one A038/A039 unequal non-flat exposed priority query, price its signed profile correction with initial capacity and consumed data debit separate; A087/A094 review half-transfer and failing node.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-14 04:48 UTC stage5: Read updated board/B13, A064 all-width ordered priority completion and A057 interleaved variance release. Consumed ordered-point closure rather than repeat it. Proved exact finite mixed-history reserve transfer: arbitrary seed a tagged by w controlling two balanced independent parity cores has frontier Q_C(a,T)/2 at C>=4; p earlier non-completing parity reveals spend C/2 each, giving initial [Q_C(a,T)-pC]_+/2. Both core reserves and variance release zero at the controller query; balanced B05 seed yields actual local D/d>=(1-2^-k)(k-2), so hypothetical all-controller price11 potential extension fails for k>=14, not the stated A064 theorem. Pilot48 roots/1255 assertions PASS. Final171 complete roots plus6 compressed witnesses/3367 assertions PASS in1.411s. Raw8192-value seed and physical children/8 assertions PASS in3.310s. Scoped independent A064 core-weight harmonic reconstruction:162 queries/824 assertions PASS in1.541s, with nonzero actual inherited core reserves. Extended existing pending reserve candidate v4; saved protocol/source/persistence files, full FEI and generic controller reserve payment remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nFor ANY finite Boolean seed a and complete tree T, tag h=w*a and let it select between two disjoint balanced parity cores. Under seed-tree then w then core completion, at C>=4 the complete reserve is exactly Q_C(a,T)/2 at each seed history: H_lift=2+H_seed/2, D_lift=D_seed/2, Inf_lift=Inf_seed/2, and the terminal w query pays D2 at influence1/2. This is a complete Snell identity, not a whole-path endpoint identity.\nA fixed prefix of p parity-coordinate reveals leaving both cores nonconstant has D0 and influence1/2 per query. Its initial complete reserve is [Q_C(seed,T)-pC]_+/2, but the reached frontier still carries Q_C(seed,T)/2. Each earlier physical debit is spent once and cannot be reused at a later local query.\nAt these tagged controller queries q_u=q_v=1/2 throughout, core reserves are0 and the variance-rarity release is0. Canonical B05 seed selector gives D/d>=(1-2^-k)(k-2) even after partial core exposure. Therefore a variance-plus-core-only all-controller extension of A064 price11 fails at an actual reached node for all even k>=14; its stated ordered-point theorem and existence of another policy remain intact. Retain the controller seed owner rather than resetting it.\nA064 repeated-fallback/global-priority debt v1 inherited-core harmonic clause independently HOLDS: after fixed data history, q_j=avg q_j,child and the same r_j multiplies both children; sum q_j*r_j has zero drift under any controller query. This bookkeeping alone supplies no entropy payment. Full bundled theorem not accepted by the scoped review.\n')
data=json.loads((run/'out/EXACT_OWNER.json').read_text()); raw=json.loads((run/'out/RAW_SEED.json').read_text()); review=json.loads((run/'out/HARMONIC_REVIEW.json').read_text())
assert data['assertions']==3367 and raw['assertions']==8 and review['assertions']==824
assert data['failures']==raw['failures']==review['failures']==0
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
print(json.dumps({'schema_checks_passed':True,'exact_assertions':4199,'extended_claim_version':4,'full_fei':'OPEN','files_receipted':len(receipts)},indent=2))
