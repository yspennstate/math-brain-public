"""Save protocol-exact claim/progress metadata and local persistence receipts."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
def save(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((supp/'sources').glob('*.md'))+sorted(ctx.glob('*.txt'))+sorted((base/'runs').rglob('REPORT.md'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
inventory=[]
for p in paths:
    data=p.read_bytes(); content=data.decode('utf-8',errors='replace')
    inventory.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'line_count':len(content.splitlines()),'scope':'byte-read provenance; selected mathematical passages inspected as specified in REPORT.md'})
save('out/source_inventory.json',inventory)
protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text())
consumers=['A002','A007','A012','A015','A023','A025','A026','A036','A040','A047','A048','A077','B20']
def claim(cid,statement,hypotheses,source):
    statement_hash=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':statement_hash,'contributors':['A021'],'proof_source':str(run/source),'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
claims=[claim('A021-UNIFORM-RARE-CORE-EXPANSION',
    'For every balanced Boolean b, integers t,k>=1, q=2^-k and c=1/ln2, F=1+A_k(product_{j=1}^t b_j-1) has H(F)=q[tH(b)+4k+2c]-q^2(2k+3c)+R(q), I(F)=q[tI(b)+k], and -2cq^3/[3(1-q)]<=R(q)<=0. The exact entropy is q t H(b)+(4q-2q^2)k-2(1-q)^2 log2(1-q); variance is 2q-q^2 and minority probability q/2. If k=o(t) and 2^-k t->0 for a fixed seed, H(F)/I(F)->H(b)/I(b) with influence tending to zero.',
    ['uniform physical cube','Boolean sign seed with mean zero','disjoint independent seed copies and fresh point controls','bit entropy'], 'REPORT.md'),
    claim('A021-CONTROL-FIRST-KL-LEDGER',
    'For the same family, a control-first stopping tree has terminal entropy 2^-k t H(b), queried influence k2^-k, and exact magnitude-mismatch/KL debt J_tree=2^-k(k+A_k). Here A_k=sum_{s=1}^k 2^-s[2s-1+log2(1-2^(1-s)+2^(1-2s))] and there exists A in [0,3] with 0<=A-A_k<=(2k+3)2^-k. Hence J_tree<=2^-k(k+3)<=4k2^-k uniformly in tensor count. The blind rarity sum before KL subtraction is 2^-k k(k+1)/2. At each active node s, mu=2^-s and J_s=mu-mu^2+mu^2 log2((1-2mu+2mu^2)/mu^2).',
    ['hypotheses of A021-UNIFORM-RARE-CORE-EXPANSION, reproved directly in REPORT.md','controls queried first, stopping on first inactive control','mismatch defined using absolute child Fourier coefficients','complete terminal entropy retained'], 'REPORT.md')]
for cl in claims: assert set(cl)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',claims)
progress={
    'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B05','packet_id':'A021',
    'gap_id':'G-R-MISMATCH','attempt_id':'A021-rare-core-uniform-1','method':'exact Walsh family derivation, uniform analytic logarithmic-series bounds, complete control-first tree, exact prime-log validation',
    'mathematical_delta':'Uniform independent-(k,t) entropy/influence expansions; explicit magnitude-mismatch/KL tree ledger with linear control payment and exact terminal entropy; dropping KL inflates charge quadratically in k; necessary potential coefficient tests.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'PACKET_INTERFACE_PROVED_LOCALLY_REVIEW_PENDING; FULL_FEI_OPEN',
    'claim_versions_used':[],
    'claims_created_or_changed':[{'claim_id':cl['claim_id'],'version':1} for cl in claims],
    'source_artifacts':['REPORT.md','RARE_CORE_EXPANSIONS.tex','POTENTIAL_NECESSITIES.md','code/check.py','out/FROZEN_SPEC.json','out/validation.json','out/source_inventory.json'],
    'next_consumers':consumers,
    'next_action':'A087/A094 independently reconstruct the uniform remainder and exact tree debt; A023 transfer the control-first ledger to sparse-bent point surgery and compare selector-first queries.',
    'stagnant_substantive_attempts':0,
    'blockers':['No global potential or arbitrary terminal-core entropy payment established.','Specified Claude B05 STREAM_NOTES.md absent; independent review and supervisor mirroring unverified.'],
    'packet_ids':['A021']}
# The protocol lists its last field with an explanatory parenthetical;
# compatibility instructions explicitly prescribe the literal key packet_ids.
expected_progress={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
now=datetime.now(timezone.utc).isoformat()
(agent/'STATUS.md').write_text('STATE: A021 packet complete locally: uniform rare-core asymptotics and exact KL control-tree payment; 420 cases / 3,220 exact assertions; review pending; full FEI OPEN.\nNEXT: A087/A094 review; A023 compare this ledger on sparse-bent surgery with selector-first trees, retaining arbitrary terminal entropy.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as out:
    out.write(f'\n{now} | Stage 1, A021/B05: read protocol/board/source passages; Claude stream notes absent. Derived exact independent-k,t activation spectrum and uniform remainder. Computed control-first magnitude-KL debt q(k+A_k), 0<=A_k<=3, terminal qth, physical influence split kq+qti. Frozen 420-case pilot passed 3,220 exact rational/prime-log assertions in 1.2464 seconds. Saved full interface, two review-pending claims, protocol-exact progress and compatible delta. Full FEI and arbitrary terminal-core payment remain open. No external writes or messages.\n')
(agent/'LEARNED.md').write_text('''# A021 durable facts

Balanced seed b with h=H(b), i=I(b), disjoint tensor t and point-controls k, q=2^-k: H(F)=qth+(4q-2q^2)k-2(1-q)^2 log2(1-q); I(F)=q(ti+k). Uniform error after second order: R=-4/ln2 sum_{j>=3}q^j/[j(j-1)(j-2)], between -2q^3/[3 ln2(1-q)] and zero, independent of t and seed dimension.

Control-first exact magnitude-KL debt J_tree=q(k+A_k), where 0<=A_k<=3 and 0<=A-A_k<=(2k+3)q. Terminal entropy is qth. Dropping KL yields qk(k+1)/2 instead of order kq. The separately paid linear source allowance is 3kq/ln2. Do not double spend it.

Signed mismatch equals magnitude mismatch in this control-family because the only nonzero constant-child coefficient aligns with a nonnegative activated mean; this does not extend to arbitrary children.

k=o(t), qt->0 preserves h/i while influence and minority probability vanish. t=k^2 is an explicit sequence. Balancing an arbitrary f as z product f_j preserves arbitrary seed ratios in the same limit; rarity is full-FEI-strength, as already established in threshold Proposition 8.9 / Corollary 8.10.

Exact limit ratio inheritance does not imply a finite same-constant theorem: CI-H=q[t(Ci-h)+(C-4)k-2c+q(2k+3c)]-R. If C=h/i<4, its finite-family deficit eventually is negative.

The independent truth-table/Walsh/edge/prime-log checker validated all 70 balanced three-bit seeds, t=1,2 and k=1,2,3: 420 cases, 3,220 assertions, max dimension 9. Formal prime-log equality is exact; no floating signs are certificates. Independent review pending. Full FEI remains open because arbitrary terminal H(g)/I(g) is unpaid.
''',encoding='utf-8')
receipt=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='artifact_receipt.json':
        data=p.read_bytes(); assert len(data)<20_000_000
        receipt.append({'path':str(p.relative_to(run)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
save('out/artifact_receipt.json',{'saved_at_utc':now,'scope':'local files only; no mirror or review acceptance claimed','artifacts':receipt})
print(json.dumps({'claims':len(claims),'protocol_fields_exact':True,'local_artifacts':len(receipt),'run':str(run)},indent=2))
