"""Persist exact-schema A015 handoff and independently read back all local bytes."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json

RUN = Path(__file__).resolve().parents[1]
AGENT = RUN.parents[1]
TEAM = AGENT.parents[1]
CAMPAIGN = Path(r'~\mop_fei100')
PROTOCOL = CAMPAIGN/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
NOW = datetime.now(timezone.utc).isoformat()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def read_json(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def write_json(p, obj):
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    assert read_json(p) == obj

protocol = read_json(PROTOCOL)
source7 = TEAM/'agents/A007/runs/20261023T140735Z-fleet03-A007-root-normalization'
source8 = TEAM/'agents/A008/runs/20261023T144206Z-fleet03-A008-gate-label-compression'
sources = [PROTOCOL, TEAM/'BOARD.md', TEAM/'claude/B03/STREAM_NOTES.md',
           Path(r'~\AGENTS.md')]
for name in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json',
             'PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    sources.append(PROTOCOL.parent/name)
supplement = CAMPAIGN/'research_pushes/2026-10-11-full-fei-100-agents'
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    sources.append(supplement/name)
sources.extend(sorted((supplement/'sources').glob('*.md')))
sources.extend(sorted((TEAM/'context').glob('*.txt')))
sources.extend([source7/'CORE_EMBEDDING.md',source7/'CLAIMS.json',source7/'REPORT.md',
                source7/'code/persist.py',source8/'PROOF_AND_REVIEW.md',
                source8/'CLAIMS.json',source8/'REPORT.md',source8/'code/stage.py'])
pins = [{'path':str(p),'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size} for p in sources]
write_json(RUN/'out/SOURCE_RECEIPTS.json',{'observed_at':NOW,'sources':pins,
  'scope':'Full source-byte pins; contextual files are selected passages as stated in REPORT; mutable pins are final observations.'})

claims = []
ids = ['A007-SIGNED-CORE-PRIVATE-CLAUSE-UNIVERSALITY-AND-NORMALIZATION',
       'A008-ORIENTED-LOGARITHMIC-FINITE-CORE-EXTRACTION']
for src, cid in zip([source7,source8],ids):
    claim = copy.deepcopy(next(c for c in read_json(src/'CLAIMS.json') if c['claim_id'] == cid))
    # Preserve the source's documented hash recipe: A007 hashes text alone;
    # A008 hashes canonical JSON containing both text and hypotheses.
    material = (claim['exact_statement'].encode('utf-8') if cid.startswith('A007-') else
                json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},
                           sort_keys=True,separators=(',',':')).encode('utf-8'))
    assert digest(material) == claim['statement_sha256']
    claim['proof_source'] = [str(src/p) for p in claim['proof_source']] + ['REVIEW_SIGNED.md','out/checks.json']
    claim['review_records'].append({'reviewer':'A015','verdict':'HOLDS_FULL_STATED_SCOPE',
        'role':'Independent full mathematical reconstruction, no substantive repair',
        'reviewed_at':NOW,'evidence':['REVIEW_SIGNED.md','code/check.py','out/checks.json']})
    claim['status'] = 'INDEPENDENTLY_REVIEWED_A015_FULL_STATED_SCOPE'
    claims.append(claim)

statement = ('For every nonconstant monotone sign Boolean g on s>=1 uniform bits and any finite positive CNF '
 'G=(1+g)/2=AND_j C_j(z) with t>=1 nonempty core clauses, form F_L=2 AND_(j,l<=L)(C_j(z) OR y_jl)-1 '
 'using distinct fresh positive private bits, L>=1. Every displayed clause is an irredundant prime implicate '
 'and every private bit is relevant. With b(z)=number of false anchors, epsilon=2^-L, a(z)=epsilon^b(z), '
 'q=Pr[g=-1], the EXACT physical identities are I_private=2L E[b epsilon^b], '
 'I_core=sum_i E|a(z)-a(z xor e_i)| and private spectral mass M=4E[a(1-a)]. '
 'They imply |I(F_L)-I(g)|<=2q(s+L)epsilon and M<=4qepsilon. '
 'Collapsing all private-supported spectral sets to one cemetery atom gives a fixed-size law P_L '
 'with H(P_L)<=H(F_L)<=H(P_L)+4qepsilon(s+tL), and P_L converges to (ghat^2,0). '
 'Thus H(F_L)->H(g), I(F_L)->I(g)>0 and H(F_L)/I(F_L)->H(g)/I(g) for each fixed g and fixed CNF. '
 'The supremum H/I on this positive-core positive-private CNF class equals that on ALL monotone Boolean functions. '
 'For L>=3 an explicit entropy error is |H(F_L)-H(g)|<=h2(4epsilon)+4epsilon s+4qepsilon(s+tL). '
 'This is monotone-FEI universality only, not equivalence with full Boolean FEI. Unlike signed-point anchors, '
 'nonempty core amplitudes need not share a common scaling: AND2 gives ratios 1-epsilon^2 and (1-epsilon)^2. '
 'No universal paid source, common-scaling finite reference extraction, uncharged wrapper or history reset is asserted.')
new = {'claim_id':'A015-POSITIVE-ANCHOR-MONOTONE-UNIVERSALITY','version':1,
 'exact_statement':statement,
 'hypotheses':['Finite uniform physical cube; entropy and reference lengths in bits; g nonconstant and monotone in the positive physical orientation',
   'A fixed finite positive CNF with nonempty anchor clauses; every private bit is fresh and disjoint',
   'Limits fix g,s,t and its anchor representation before L tends to infinity',
   'Nested false-anchor sets are used ONLY for positive anchors; no signed overlap shortcut',
   'Same-constant statement concerns actual full entropy; nonempty source suppliers retain their wrapper'],
 'statement_sha256':digest(statement.encode('utf-8')),'contributors':['A015'],
 'proof_source':['POSITIVE_CORE.md','FROZEN_SPEC.json','code/check.py','out/checks.json'],
 'proof_dependencies':['Direct clause construction and deletion witnesses; exact nested-event pivotal count',
   'Signed core Walsh transform and Parseval; finite-alphabet coupling entropy bound proved in POSITIVE_CORE.md',
   'Elementary b<=2^(b-1) induction; Lean attempt unverified and NOT a dependency'],
 'review_records':[{'reviewer':'A015','role':'Author proof and new exact finite physical validation; not independent-agent acceptance',
    'verdict':'PASS','evidence':['POSITIVE_CORE.md','out/checks.json']}],
 'status':'AUTHOR_PROOF_EXACT_CHECKS_INDEPENDENT_REVIEW_PENDING',
 'supersedes':[],'refutes':[{'statement':'The positive-anchor core amplitudes obey the signed-point common-scaling identity',
    'witness':'AND2 with singleton anchors and any finite L>=1; unequal singleton/pair ratios',
    'scope':'Common-scaling transplantation only; no finite general extraction impossibility is asserted'}],
 'first_unproved_line':None,'next_consumers':['A007','A008','A014','A086','A094','B03','B20']}
claims.append(new)
expected_claim = set(protocol['required_per_run']['claim_fields'])
assert all(set(c) == expected_claim for c in claims)
write_json(RUN/'CLAIMS.json',claims)
result = read_json(RUN/'out/checks.json')
assert result['status']=='PASS' and result['assertions']==73492
assert (result['positive_cases'],result['signed_review_cases'],result['scalar_pairs'])==(69,286,576)
assert result['helper_sha256']==digest((RUN/'code/check.py').read_bytes())
lean = read_json(RUN/'out/lean_receipt.json')
assert lean['result']['status']=='RUNTIME_UNVERIFIED'
progress = {'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B03','packet_id':'A015',
 'gap_id':'G-J-COST','attempt_id':'A015-positive-anchor-universality-v1',
 'method':'Independent signed-source reconstruction and positive nested-event embedding with exact sector accounting',
 'mathematical_delta':'Positive-core prime-private-clause class has exactly ALL monotone H/I supremum; anchor-count-free influence error, explicit entropy tail; A007/A008 source claims independently hold.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_PROOF_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims[:2]],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 'source_artifacts':['REPORT.md','POSITIVE_CORE.md','REVIEW_SIGNED.md','FROZEN_SPEC.json','code/check.py','out/checks.json','out/SOURCE_RECEIPTS.json','out/lean_receipt.json'],
 'next_consumers':['A007','A008','A014','A086','A094','B03','B20'],
 'next_action':'Construct an ORIGINAL influence-paid core-sensitive fixed whole-set reference for nonfactorable interacting anchors; positivity alone retains monotone FEI; keep signed fusion, wrapper, old debits and both terminals.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal original source is unpaid; full FEI OPEN',
   'New positive-anchor theorem awaits independent review; core-only Lean check RUNTIME_UNVERIFIED at45.619s',
   'Initial checklist lock failure; completion command later exit0, ledger readback unverified; remote supervisor adoption unverified'],
 'packet_ids':['A015']}
expected_progress=set(protocol['required_per_run']['progress_fields'])
expected_progress.remove('packet_ids (one primary ID, for compatibility)')
expected_progress.add('packet_ids')
assert set(progress)==expected_progress
write_json(RUN/'PROGRESS.json',progress)
write_json(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()

state = ('STATE: A015 stage21 saved: positive-anchor prime-private CNFs retain ALL monotone H/I; A007 signed universality/A008 finite extraction independently HOLD;73492 exact checks PASS;Lean runtime unverified;FEI OPEN.\n'
 'NEXT: A007/A008 review positive embedding; pay ORIGINAL core-sensitive fixed source for nonfactorable anchors from SAME physical influence; positivity retains monotone FEI, signed anchors retain full FEI; no reset.\n')
(AGENT/'STATUS.md').write_text(state,encoding='utf-8')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for name, message in [
 ('WORKLOG.md','Reviewed A007/A008 whole signed-core claims unchanged. Proved positive-anchor class retains all monotone H/I via nested physical events and explicit growing-private entropy tail; common-scaling transplantation fails at AND2. Main73492 exact assertions PASS; core Lean expires RUNTIME_UNVERIFIED. Universal source remains unpaid. Shared checklist working update hit its lock; no shared lock changed.'),
 ('LEARNED.md','For ANY fixed monotone core positive CNF, repeat every clause L times with distinct private bits. a(z)=2^(-Lb), I_private=2L E[b2^(-Lb)]<=2Lq2^-L, |I_core-I(g)|<=2sq2^-L; M=4E[a(1-a)]<=4q2^-L. Collapsing private spectra has finite core alphabet; entropy detail<=M(s+tL)->0. Hence this positive-anchor irredundant prime-private class has EXACT all-monotone supremum H/I. This is NOT full-FEI equivalence. AND2 disproves A007 common-scaling extraction for these positive anchors. The next universal source lemma must compress a whole arbitrary monotone core; positivity alone is no such compression. A007/A008 signed-source reductions independently reconstructed at unchanged scope; Lean scalar check timed out, not certified.')]:
    p=AGENT/name
    old=p.read_text(encoding='utf-8') if p.exists() else ''
    marker='20261026T235636Z-fleet04-A015-positive-core'
    if marker not in old:
        p.write_text(old+'\n\n## '+NOW+' | '+marker+'\n\n'+message+'\n',encoding='utf-8')

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report
assert report.rfind('## Universal bridge') > report.rfind('## actual persistence')
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        raw=p.read_bytes()
        assert len(raw)<20_000_000, str(p)
        assert raw==p.read_bytes(), str(p)
        receipts.append({'path':str(p.relative_to(RUN)),'sha256':digest(raw),'bytes':len(raw)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=AGENT/name
    receipts.append({'path':str(p),'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size})
write_json(RUN/'out/PERSISTENCE.json',{'observed_at':NOW,'schema':'PASS','source_statement_hashes':'UNCHANGED',
 'main_assertions':73492,'pilot_assertions_not_added':571,'mirror':'UNVERIFIED_SUPERVISOR_OWNED',
 'files':receipts})
print(json.dumps({'status':'SAVED_AND_READBACK_PASS','run':str(RUN),'files':len(receipts),
                  'claims':len(claims),'main_assertions':73492,'new_statement_sha256':new['statement_sha256']}))
