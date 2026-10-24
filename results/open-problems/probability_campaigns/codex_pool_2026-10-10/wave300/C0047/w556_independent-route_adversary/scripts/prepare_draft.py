"""Prepare concepts locally and publish only to the two explicitly claimed outputs."""
import datetime
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parents[1]
MESH = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
INBOX = Path('~/math-brain-inbox/w556')
HOOK = Path('~/primary_directive/hooks1000/proposals/math-w556.jsonl')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def source(claim, name='ATTEMPT.md'):
    return {'source_id': 'owner-own-work:w556:C0047:' + claim,
            'url': (HERE / name).as_uri(), 'revision': 'as-reviewed-2026-10-10-draft',
            'license': 'owner-own-work', 'excerpt': None}

entries = [
    {'key':'operator-bound', 'namespace':'probability.percolation',
     'logical_name':'connection-operator-uniform-finite-support-bound', 'kind':'concept',
     'title':'Connection operator: a uniform finite-support bound',
     'statement':'Draft audit concept. For a countable vertex set V and a nonnegative symmetric kernel K, l2 operator boundedness requires a finite constant M bounding ||Kf||_2 by M||f||_2 for every finitely supported f. Testing one delta-function at a time only bounds individual columns; uniformly square-summable columns alone do not establish this operator estimate.',
     'proof_text':None, 'assumptions':['countable vertex set','nonnegative symmetric kernel','counting-measure l2 norm'],
     'domain':'probability', 'source':source('S2')},
    {'key':'nonuniqueness-criterion', 'namespace':'probability.percolation',
     'logical_name':'supercritical-connection-operator-nonuniqueness-criterion-draft', 'kind':'concept',
     'title':'DRAFT: a supercritical connection-operator criterion',
     'statement':'Draft independent rederivation awaiting referee check. On an infinite connected locally finite vertex-transitive graph with iid Bernoulli bond percolation, almost-sure uniqueness and theta(p)>0 force tau_p(x,y)>=theta(p)^2 by Harris association. Normalized indicators of n vertices then have connection-kernel Rayleigh quotient at least n theta(p)^2. Thus T_p is unbounded. A bounded T_p at some p>p_c implies p_c<p_u, but existence of that parameter on every fixed nonamenable Cayley graph is not proved here.',
     'proof_text':None, 'assumptions':['infinite connected locally finite vertex-transitive graph','iid Bernoulli bond percolation','theta(p)>0 for the uniqueness obstruction','a proved bounded operator parameter p>p_c for the criterion'],
     'domain':'probability', 'source':source('S1')},
    {'key':'row-counterexample', 'namespace':'analysis.operators',
     'logical_name':'square-summable-rows-unbounded-positive-kernel-draft', 'kind':'concept',
     'title':'DRAFT: square-summable rows with an unbounded operator',
     'statement':'Draft audit example awaiting referee check. The kernel K(i,j)=(1+|i-j|)^(-3/4) on Z is symmetric, nonnegative, translation invariant, positive semidefinite, and has unit diagonal. Every row has squared l2 norm at most 5, yet normalized indicators of intervals of n vertices have Rayleigh quotient at least n(1+n)^(-3/4), tending to infinity. Positivity follows by averaging one-dimensional Bernoulli connection kernels over R=exp(-T), T Gamma(3/4,rate=1). This mixture is not fixed-parameter iid percolation and Z is amenable; the example refutes a generic operator inference, not the Benjamini-Schramm conjecture.',
     'proof_text':None, 'assumptions':['K(i,j)=(1+|i-j|)^(-3/4) on Z','generic kernel or mixture-percolation setting','no claim of fixed-parameter iid or nonamenable counterexample'],
     'domain':'functional analysis', 'source':source('S2')},
    {'key':'formal-receipt', 'namespace':'logic.proof-auditing',
     'logical_name':'percolation-comparator-statement-not-proof-receipt', 'kind':'concept',
     'title':'Percolation comparator statements need actual proof receipts',
     'statement':'Draft source audit. At public openai/math commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, comparator theorem bodies full_main, critical_laws, cayley_main and arbitrary_cayley are admitted with sorry. Those declarations cannot count as formal proof receipts for the percolation operator gap. This does not refute the accompanying mathematical preprint or exclude a separate implementation. A valid receipt must identify the actual implemented theorem, full assumptions and trusted axioms, excluding admitted placeholders.',
     'proof_text':None, 'assumptions':['the four pinned comparator declarations, not an uninspected separate implementation','source-level audit only; no Lean compilation or axiom trace obtained'],
     'domain':'mathematical logic', 'source':source('S3','PUBLIC_FORMAL_AUDIT.md')},
]
relations = [
    {'from_key':'nonuniqueness-criterion','to_key':'operator-bound','kind':'depends_on',
     'rationale':'The criterion assumes bounded T_p; the target concept defines the required uniform finite-support operator estimate, rather than separate delta-column tests.'},
    {'from_key':'row-counterexample','to_key':'operator-bound','kind':'semantic_association',
     'rationale':'The example has uniformly square-summable rows but divergent finite-set Rayleigh quotients, distinguishing the column test from the uniform operator bound.'},
    {'from_key':'formal-receipt','to_key':'nonuniqueness-criterion','kind':'semantic_association',
     'rationale':'The criterion requires an actual supercritical operator estimate; the pinned admitted comparator declarations do not prove that estimate.'},
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w556',
          'bundle_slug':'c0047-independent-operator-audit-w556-001',
          'entries':entries,'relations':relations}
required = ('key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source')
for entry in entries:
    assert all(k in entry for k in required)
    assert entry['kind']=='concept' and entry['proof_text'] is None
    assert entry['source']['license'].startswith('owner-own-work')
keys = {entry['key'] for entry in entries}
assert len(keys)==len(entries)
for relation in relations:
    assert relation['from_key'] in keys and relation['to_key'] in keys
    assert relation['kind'] in ('depends_on','semantic_association')
local = HERE / 'drafts'
local.mkdir(exist_ok=True)
(local / 'bundle_001.json').write_text(json.dumps(bundle, indent=2), encoding='utf-8')
ends = []
for relation in relations:
    ends.append({**relation,
                 'from_statement':next(e['statement'] for e in entries if e['key']==relation['from_key']),
                 'to_statement':next(e['statement'] for e in entries if e['key']==relation['to_key']),
                 'proof_or_source':'ATTEMPT.md S1/S2 or PUBLIC_FORMAL_AUDIT.md; all drafts pending referee review'})
(HERE / 'RELATION_EVIDENCE.json').write_text(json.dumps(ends, indent=2), encoding='utf-8')

pattern = r'(?is)(?:row|column|root).{0,100}(?:square.?summable|l2|ell.?2).{0,80}\b(?:therefore|hence|thus)\b.{0,100}(?:operator.{0,30}bound|bounded.{0,30}operator)'
positive = ['Each row is square-summable, hence the connection operator is bounded.',
            'Each root column is l2; therefore the operator is bounded.']
negative = ['Each row is square-summable; this does not imply an operator bound.',
            'A uniform bound over every finite-support unit vector proves operator boundedness.',
            'The finite root-row calculation is only a necessary test; the norm estimate is open.']
assert all(re.search(pattern, text) for text in positive)
assert not any(re.search(pattern, text) for text in negative)
hook = {'id':'c0047-w556-01','area':'math','event':'PreToolUse','cue':pattern,
        'fire_when':positive[0], 'silent_when':negative[1],
        'text':'Square-summable rows alone do not bound an l2 operator. Test every finite-support unit vector or derive a valid norm estimate: K(i,j)=(1+|i-j|)^(-3/4) has row-square norm <=5 and unbounded interval Rayleigh quotients.',
        'evidence':'~/brain_workers/w556/ATTEMPT.md S2; VERIFICATION.json: n=64 to 2048 Rayleigh 10.475964 to 35.194557, row-square bound 5',
        'proposer':'w556'}
assert len(hook['text'])<=300
(local / 'math-w556.jsonl').write_text(json.dumps(hook)+'\n', encoding='utf-8')
(HERE / 'HOOK_CONTROLS.json').write_text(json.dumps({'fire_cases':positive,'silent_cases':negative,'fire_passed':2,'silent_passed':3,'text_characters':len(hook['text']),'scope':'five local control strings; no production precision estimate'}, indent=2), encoding='utf-8')

for resource in (INBOX, HOOK):
    check = subprocess.run([sys.executable,'-X','utf8',MESH,'assert','--agent','w556',
                            '--resource',str(resource),'--mode','write'], capture_output=True, text=True, timeout=30)
    print(check.stdout.strip())
    if check.returncode:
        raise RuntimeError('covering lease assertion refused: '+check.stderr)
INBOX.mkdir(exist_ok=True)
destination = INBOX / 'bundle_001.json'
if destination.exists():
    raise FileExistsError('preserve existing bundle; do not overwrite')
part = INBOX / 'bundle_001.part'
assert part.resolve().parent==INBOX.resolve()==destination.resolve().parent
part.write_text(json.dumps(bundle, indent=2), encoding='utf-8')
part.rename(destination)
HOOK.parent.mkdir(exist_ok=True)
existing = HOOK.read_text(encoding='utf-8') if HOOK.exists() else ''
if not any(json.loads(line).get('id')==hook['id'] for line in existing.splitlines() if line.strip()):
    with HOOK.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(hook)+'\n')
states = {'worker':'w556','prepared':{'state':True,'entries':4,'relations':3},
          'submitted':{'state':True,'path':str(destination),'utc':now},
          'reviewed':{'state':False,'referee':'w557','receipt':None},
          'ingested':{'state':False,'receipt':None},
          'retrievable':{'state':False,'receipt':None},
          'proof_promotion_allowed':False,'served_model_evidence':'unavailable',
          'hook_proposal':str(HOOK)}
(HERE / 'BUNDLE_STATES.json').write_text(json.dumps(states, indent=2), encoding='utf-8')
print(json.dumps({'draft':str(destination),'entries':4,'relations':3,'hook':str(HOOK),
                  'hook_controls':'2/2 fire, 3/3 silent','integrator_run':False}))
