"""Bounded arithmetic/shape checks and a scoped native-retrieval development probe."""
import dataclasses
import datetime
import json
import math
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
folder = Path(__file__).resolve().parent
gate_file = Path('~/.claude/compute/compute_state.json')
gate = json.loads(gate_file.read_text(encoding='utf-8-sig'))
stamp = datetime.datetime.fromisoformat(gate['ts'])
if stamp.tzinfo is None:
    stamp = stamp.astimezone()
age = (datetime.datetime.now(datetime.timezone.utc)-stamp).total_seconds()
receipt = {k: gate.get(k) for k in ('ts','status','mode','reasons','mem_avail_mb','disk_free_gb')}
receipt.update(age_seconds=age, planned_work='serial subsecond arithmetic and <=38-node retrieval; no simulation, GPU, training, child or network')
(folder / 'compute_gate.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
if not 0 <= age <= 600 or gate.get('status') not in ('ok','normal','warn'):
    raise SystemExit('Fresh compute gate does not permit this bounded development probe; receipt saved.')

started = time.monotonic()
checks = []
def check(name, passed, **details):
    if not passed:
        raise AssertionError(name)
    checks.append({'name':name, 'passed': True, **details})

bundle = json.loads((folder / 'bundle_001.json').read_text(encoding='utf-8'))
keys = {e['key'] for e in bundle['entries']}
for e in bundle['entries']:
    check('shape:'+e['key'], set(('key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source')) <= set(e))
    check('draft-kind:'+e['key'], e['kind'] in ('concept','definition') and e['proof_text'] is None)
    check('source-license:'+e['key'], e['source']['license'].startswith('owner-own-work'))
for rel in bundle['relations']:
    check('edge:'+rel['from_key'], rel['from_key'] in keys and (rel.get('to_key') in keys or 'to_existing_logical' in rel))

h = lambda t: math.erf(t/math.sqrt(2))
a = math.sqrt(2/math.pi)
for t,t0 in ((.5,1),(.05,.5),(.1,.1),(.25,2)):
    excess = h(t)-(t/t0)*h(t0)
    bound = a*t*(t0*t0-t*t)/6
    check('deterministic-radius:'+str((t,t0)), -1e-14<=excess<=bound+1e-14, excess=excess, upper_bound=bound)
weights,radii = (.2,.5,.3),(0,1,3)
mixed = lambda t: sum(w*math.erf(t*r/math.sqrt(2)) for w,r in zip(weights,radii))
moment3 = sum(w*r**3 for w,r in zip(weights,radii))
excess = mixed(.2)-.2*mixed(1)
check('mixed-radius-remainder', 0<=excess<=a*.2*(1-.2**2)*moment3/6, excess=excess, moment3=moment3)
finite_gaussian = h(1)
limiting_gaussian = -math.expm1(-1.5)
check('finite-vs-limiting-n1', abs(finite_gaussian-limiting_gaussian)>.09,
      finite_n1_cdf=finite_gaussian, limiting_cdf=limiting_gaussian)
check('denominator-drop-witness', (3-math.sqrt(5))/2 < .4 and .8 < 1 < 16/15,
      actual_smin_squared=(3-math.sqrt(5))/2, dropped_threshold=.8, exact_threshold=16/15)
# A lower integral bound proves divergence; checking truncations is only arithmetic.
for eps in (.1,.01,.001):
    lower = math.exp(-.5)*(1/eps-1)
    check('negative-third-moment-truncation:'+str(eps), lower>0, integral_lower_bound=lower)

sys.path.insert(0, '~/math-brain-build/src')
from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import retrieve
from math_brain.store import ResearchStore
baseline = json.loads((folder / 'math_recall.json').read_text(encoding='utf-8'))
with ResearchStore.open_read_only(baseline['store']) as store:
    store.connection.execute('BEGIN')
    old_nodes = tuple(store.get_nodes(row[0] for row in baseline['candidates']).values())
new_nodes = tuple(GraphNode(id='draft_w574_'+e['key'], kind=NodeKind.CLAIM,
                           title=e['title'], body=e['statement'],
                           metadata={'claim_kind':e['kind'], 'truth_status':'unverified',
                                     'logical_id':'math:'+e['namespace']+':'+e['logical_name']})
                  for e in bundle['entries'])
query = baseline['results'][1]['query']
probes = {}
for name,nodes in (('before',old_nodes),('after',old_nodes+new_nodes)):
    begin = time.monotonic()
    decision = retrieve(query,nodes=nodes,edges=(),limit=5,graph_depth=0)
    hits = [{'id':hit.node.id,'title':hit.node.title,
             'score':hit.lexical_score+hit.symbol_score+hit.formula_score+hit.graph_score}
            for hit in decision.hits]
    rank = next((i for i,hit in enumerate(hits,1) if hit['id']=='draft_w574_signed-rescaling'),None)
    probes[name] = {'hit_at_5':int(rank is not None),'rank':rank,'hits':hits,
                    'elapsed_seconds':time.monotonic()-begin,'node_count':len(nodes)}
check('bridge-retrievable-in-local-overlay',probes['after']['hit_at_5']==1)
output = {'command':'python -X utf8 validate_bridge.py','compute_gate':receipt,
          'arithmetic_and_shape_checks':checks,'probe_query':query,'scoped_retrieval':probes,
          'elapsed_seconds':time.monotonic()-started,
          'limitations':['A single designed development query; not held-out or global recall evidence.',
                        'DRAFT concepts only; checks are not independent mathematical review or formal proof.',
                        'Both phases use the same read-only 34-node snapshot; only the four draft nodes differ.',
                        'The separate finite-n source correction is owned by w573.']}
(folder / 'validation.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'before':probes['before'],'after':probes['after'],
                  'elapsed_seconds':output['elapsed_seconds']},ensure_ascii=False))
