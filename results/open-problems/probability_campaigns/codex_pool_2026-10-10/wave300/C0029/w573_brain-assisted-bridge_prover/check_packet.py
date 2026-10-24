"""Bounded scalar checks and draft validation, with a fresh local resource gate."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import math
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
start=time.monotonic()
state_path=Path(r'~/.claude/compute/compute_state.json')
try:
    pressure=json.loads(state_path.read_text(encoding='utf-8'))
    sampled={k:pressure.get(k) for k in ('status','mode','commit_used_pct','commit_avail_mb','physical_avail_mb')}
    age=time.time()-state_path.stat().st_mtime
except (OSError,ValueError):
    sampled={'status':'unknown','mode':'unknown'}
    age=None

# Scalar stdlib work only; no model, matrix enumeration, training, GPU, or runner.
# Governor distress denies even the optional numerical sanity checks.
allowed=age is not None and age<600 and str(sampled['status']).lower() not in {'distress','critical','emergency'} and sampled.get('mode') not in {'distress','pause','suspend'}
gate={'agent':'w573','timestamp_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
 'fresh_local_state':sampled,'state_age_seconds':age,'allowed_optional_scalar_checks':allowed,
 'work':'at most 205 stdlib scalar CDF checks, one n=1 scalar witness, no matrix enumeration',
 'max_wall_seconds':10,'max_dimension':0,'max_random_matrices':0,'no_gpu':True,'no_training':True,'no_subagents':True,
 'policy':'Honor published governor distress; bounded scalar verification only; missing/stale telemetry skips optional experiments.'}
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')

bundle=json.loads((ROOT/'drafts'/'bundle_001.json').read_text(encoding='utf-8'))
keys={e['key'] for e in bundle['entries']}
assert len(keys)==len(bundle['entries'])
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w573'
allowed_edges={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for e in bundle['entries']:
    assert e['kind'] in {'definition','lemma','theorem','concept'}
    assert e['statement'] and e['assumptions'] is not None
    assert e['source']['license'].startswith('owner-own-work')
    assert (bool(e['proof_text']) if e['kind'] in {'lemma','theorem'} else e['proof_text'] is None)
graph={k:[] for k in keys}
for r in bundle['relations']:
    assert r['from_key'] in keys and r['kind'] in allowed_edges
    assert bool(r.get('to_key')) != bool(r.get('to_existing_logical'))
    if 'to_key' in r:
        assert r['to_key'] in keys
        if r['kind']=='depends_on': graph[r['from_key']].append(r['to_key'])
seen=set()
active=set()
def visit(k):
    if k in active: raise AssertionError('dependency cycle')
    if k in seen: return
    active.add(k)
    for q in graph[k]: visit(q)
    active.remove(k)
    seen.add(k)
for k in keys: visit(k)
claimrows=[json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert len({c['id'] for c in claimrows})==len(claimrows)
assert all(c['independent_reviewer'] and c['remaining_gap'] for c in claimrows)

result={'gate_allowed':allowed,'scalar_checks':0,'failures':0,
 'bundle_entries':len(keys),'bundle_relations':len(bundle['relations']),
 'claim_rows':len(claimrows),'valid_dependency_dag':True,
 'independent_review':False,'formal_proof_check':False,'live_store_change':False}
if allowed:
    k=math.exp(-1.5)/3
    for i in range(1,201):
        t=i/200
        f=-math.expm1(-t-t*t/2)
        margin=t-f
        assert k*t**3-1e-14<=margin<=t**3/3+1e-14
        result['scalar_checks']+=1
        if time.monotonic()-start>10: raise RuntimeError('Gate wall-time cap reached')
    for delta in (.25,.125,.0625,.01,.0001):
        t=math.sqrt(delta)
        f=-math.expm1(-t-t*t/2)
        H=min((1+delta)*f,1)
        assert H-t>=.5*delta**1.5-1e-14
        result['scalar_checks']+=1
    t=1/3
    wrong=-math.expm1(-t-t*t/2)
    actual=math.erf(t/math.sqrt(2))
    assert abs(wrong-actual)>.01
    result['finite_gaussian_scope_witness']={'n':1,'t':t,'old_claimed_cdf':wrong,
       'actual_cdf':actual,'old_absolute_error':abs(wrong-actual),
       'corrected_finite_n_cdf':actual,'corrected_absolute_error':0.0,
       'interpretation':'counterexample to the stored finite-n identity, not an engine performance or parent-solution claim'}
else:
    result['optional_numerics']='SKIPPED by fresh gate; analytic n=1 slope witness and written proofs remain available.'
result['elapsed_seconds']=time.monotonic()-start
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
artifacts=['STATEMENT.md','ATTEMPT.md','PRIOR_ATTEMPT_DIGEST.md','CLAIMS.jsonl','EDGES.jsonl','SOURCE_STATUS.json',
 'drafts/bundle_001.json','patches/01_c0029_gaussian_scope.diff','MEASUREMENTS.json','COMPUTE_GATE.json']
hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts}
(ROOT/'ARTIFACT_HASHES.json').write_text(json.dumps({'purpose':'review artifact byte identity only; not a proof receipt or integrator manifest','sha256':hashes},indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
