"""Bounded exact regression checks; these do not prove an infinite RWRE theorem."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
start = time.monotonic()
shape = (3,2,1)
sites = list(product(*(range(n) for n in shape)))
idx = {s:i for i,s in enumerate(sites)}
steps = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
rows = [tuple(F(x,10) for x in (3,1,2,1,2,1)),tuple(F(x,10) for x in (1,2,1,1,1,4))]
envs = list(product(range(2),repeat=len(sites)))
def add(x,y): return tuple((x[i]+y[i])%shape[i] for i in range(3))
def neg(x): return tuple((-x[i])%shape[i] for i in range(3))
def shift(env,x): return tuple(env[idx[add(y,x)]] for y in sites)
def transition(env):
    T = [[F(0) for _ in sites] for _ in sites]
    for i,x in enumerate(sites):
        for e,p in zip(steps,rows[env[i]]): T[i][idx[add(x,e)]]+=p
    return T
def advance(v,T): return [sum((v[i]*T[i][j] for i in range(len(sites))),F(0)) for j in range(len(sites))]
trajectories={}
for env in envs:
    T=transition(env)
    trajectories[env]=[]
    for i in range(len(sites)):
        v=[F(int(j==i)) for j in range(len(sites))]; times=[]
        for n in range(7): times.append(tuple(v)); v=advance(v,T)
        trajectories[env].append(times)
mu_checks=covariance_checks=wrong_sign_failures=0
for n in range(7):
    mu={env:F(0) for env in envs}
    for env in envs:
        for x in sites:
            forward=trajectories[env][0][n][idx[x]]
            mu[shift(env,x)]+=forward/F(len(envs))
            translated=trajectories[shift(env,x)][idx[neg(x)]][n][0]
            assert forward==translated
            covariance_checks+=1
            wrong=trajectories[shift(env,x)][idx[x]][n][0]
            wrong_sign_failures+=int(forward!=wrong)
    expected_sum=F(0)
    for env in envs:
        incoming=sum((trajectories[env][i][n][0] for i in range(len(sites))),F(0))
        assert incoming==mu[env]*len(envs)
        expected_sum+=incoming/F(len(envs)); mu_checks+=1
    assert expected_sum==1
tail_checks=[]
for K in [1,2,10,100]:
    m=2*K
    mean=F(m)*F(1,m); tail=F(m)*F(1,m) if m>K else F(0)
    second=F(m*m)*F(1,m)
    assert mean==1 and tail==1 and second==m
    tail_checks.append({'K':K,'m':m,'mean':str(mean),'tail_mass_above_K':str(tail),'second_moment':str(second)})
bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
keys={e['key'] for e in bundle['entries']}
for e in bundle['entries']:
    assert required<=e.keys() and e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert 'DRAFT' in e['statement'] or 'gap record' in e['statement']
deps={k:[] for k in keys}
for rel in bundle['relations']:
    assert rel['from_key'] in keys and rel['to_key'] in keys
    assert rel['kind'] in {'depends_on','cites'}
    assert 'Supporting from-card:' in rel['rationale'] and 'Supporting to-card:' in rel['rationale']
    if rel['kind']=='depends_on': deps[rel['from_key']].append(rel['to_key'])
def walk(k,seen):
    assert k not in seen
    for child in deps[k]: walk(child,seen|{k})
for k in keys: walk(k,set())
assert wrong_sign_failures>0
seconds=time.monotonic()-start
assert seconds<60
receipt={'command':'python -X utf8 ~/brain_workers/w585/verify_packet.py','seconds':seconds,
         'finite_torus_shape':shape,'site_iid_environments':len(envs),'times':7,
         'exact_density_checks':mu_checks,'exact_translation_covariance_checks':covariance_checks,
         'wrong_translation_sign_mutation_failures':wrong_sign_failures,'normalized_non_ui_controls':tail_checks,
         'bundle_entries_validated':len(keys),'bundle_relations_validated':len(bundle['relations']),
         'status':'PASS','scope':'Exact finite quotient algebra and draft-schema checks only; no infinite-time theorem or formal proof receipt.'}
(ROOT/'VALIDATION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
