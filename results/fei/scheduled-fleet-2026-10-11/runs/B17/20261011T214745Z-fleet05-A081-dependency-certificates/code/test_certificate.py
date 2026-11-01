from pathlib import Path
import copy,json,time,sys
from dependency_check import cycle_witness,validate,key,statement_hash
RUN=Path(__file__).resolve().parents[1]
started=time.perf_counter(); g=json.loads((RUN/'PROOF_DEPENDENCIES.json').read_text(encoding='utf-8'))
baseline=validate(g); assert baseline['status']=='STRUCTURALLY_VALID',baseline
assert all(not x['eligible_for_mathematical_review'] for x in baseline['candidate_routes'])
assert all(not v for k,v in baseline['unresolved_closure'].items() if next(n for n in g['nodes'] if key(n)==k)['status'].startswith('IMPORTED_'))
(RUN/'out/VALIDATION.json').write_text(json.dumps(baseline,indent=2)+'\n',encoding='utf-8')

# Independent representation: remove zero-indegree nodes, not DFS or stack state.
def kahn(adj):
    indegree={v:0 for v in adj}
    for ws in adj.values():
        for w in ws: indegree[w]+=1
    todo=[v for v in adj if indegree[v]==0]; removed=0
    while todo:
        v=todo.pop(); removed+=1
        for w in adj[v]:
            indegree[w]-=1
            if indegree[w]==0: todo.append(w)
    return removed==len(adj)
counts={}; dags={}
for n in ([] if '--fixtures-only' in sys.argv else range(5)):
    count=0; dagcount=0
    for mask in range(1<<(n*n)):
        adj={i:[j for j in range(n) if mask & (1<<(i*n+j))] for i in range(n)}
        cycle,order=cycle_witness(adj); isdag=kahn(adj)
        assert bool(cycle)==(not isdag)
        if cycle:
            assert cycle[0]==cycle[-1]
            assert all(b in adj[a] for a,b in zip(cycle,cycle[1:]))
        else:
            assert len(order)==n
            pos={v:i for i,v in enumerate(order)}
            assert all(pos[w]<pos[v] for v,ws in adj.items() for w in ws)
            dagcount+=1
        count+=1
    counts[str(n)]=count; dags[str(n)]=dagcount
    assert time.perf_counter()-started<60

def dep(n): return {'claim_key':key(n),'statement_sha256':n['statement_sha256'],'hypothesis_instantiation':'Fixture only.','unit_conversion':None}
fixtures=[]
def reject(label,mutate,expected):
    x=copy.deepcopy(g); mutate(x); v=validate(x,check_files=False)
    assert v['status']=='REJECT' and any(e.startswith(expected) for e in v['errors']),(label,v)
    fixtures.append({'fixture':label,'expected':expected,'errors':v['errors'],'status':'PASS'})
reject('changed statement',lambda x:x['nodes'][1].update(exact_statement='Different theorem'), 'STATEMENT_HASH')
reject('missing dependency version',lambda x:x['nodes'][1]['proof_dependencies'].append({'claim_key':'B05-SUB-ENTROPY','statement_sha256':'0'*64}), 'MISSING_EXACT_DEPENDENCY')
reject('dependency version hash differs',lambda x:x['nodes'][1]['proof_dependencies'][0].update(statement_sha256='0'*64),'DEPENDENCY_HASH')
reject('accepted relies on final FEI',lambda x:x['nodes'][1]['proof_dependencies'].append(dep(x['nodes'][0])),'ACCEPTED_DEPENDS_ON_UNRESOLVED')
def feicycle(x):
    x['nodes'][0]['proof_dependencies']=[dep(x['nodes'][1])]
    x['nodes'][1]['proof_dependencies'].append(dep(x['nodes'][0]))
reject('FEI proof cycle',feicycle,'CYCLE_THROUGH_FINAL_FEI')
reject('disconnected self-cycle',lambda x:x['nodes'][-1]['proof_dependencies'].append(dep(x['nodes'][-1])),'PROOF_CYCLE')
reject('unexplained entropy unit change',lambda x:x['nodes'][1].update(units={'entropy':'nats'}),'UNIT_CONVERSION_REQUIRED')
reject('empty hypothesis instantiation',lambda x:x['nodes'][1]['proof_dependencies'][0].update(hypothesis_instantiation=''),'MISSING_HYPOTHESIS_INSTANTIATION')
reject('duplicate exact version',lambda x:x['nodes'].append(copy.deepcopy(x['nodes'][0])),'DUPLICATE_VERSION')
reject('unknown source id',lambda x:x['nodes'][1]['proof_sources'][0].update(source_id='absent'),'MISSING_SOURCE')
reject('conditional route assumes conclusion',lambda x:x['candidate_routes'][0]['requires'].append(x['final_claim']),'ROUTE_ASSUMES_CONCLUSION')
def transitive(x):
    n=next(n for n in x['nodes'] if n['claim_id']=='OPEN-ERASURE-PAYMENT')
    n['proof_dependencies'].append(dep(x['nodes'][0]))
reject('conditional route transitively assumes conclusion',transitive,'ROUTE_TRANSITIVELY_ASSUMES_CONCLUSION')
workflow=copy.deepcopy(g); workflow['workflow_edges']+=[{'from':'A001','to':'A081','kind':'ADVISORY_ONLY'}]
assert validate(workflow,check_files=False)['status']=='STRUCTURALLY_VALID'
fixtures.append({'fixture':'advisory workflow feedback allowed','status':'PASS'})
result={'status':'PASS','graph_cases':sum(counts.values()),'graph_cases_by_n':counts,'dag_counts_by_n':dags,'independent_method':'Kahn elimination versus DFS, all adjacency masks including loops','fixture_count':len(fixtures),'fixtures':fixtures,'elapsed_seconds':time.perf_counter()-started,'arithmetic':'integers and exact byte hashes','full_FEI':'OPEN'}
(RUN/('out/FIXTURE_REVALIDATION.json' if '--fixtures-only' in sys.argv else 'out/TEST_RESULTS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
