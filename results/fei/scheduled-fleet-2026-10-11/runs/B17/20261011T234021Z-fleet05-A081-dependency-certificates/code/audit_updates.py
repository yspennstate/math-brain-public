from pathlib import Path
import json,copy,time
from dependency_check import validate,key
RUN=Path(__file__).resolve().parents[1]
g=json.loads((RUN/'PROOF_DEPENDENCIES.json').read_text(encoding='utf-8'))
started=time.perf_counter(); result=validate(g)
assert result['status']=='STRUCTURALLY_VALID'
assert not result['unresolved_closure']['B09-BIASED-BLOCK-UNCERTAINTY@1']
assert not result['unresolved_closure']['B17-KB5-CUTOFF@1']
assert all(not r['eligible_for_mathematical_review'] for r in result['candidate_routes'])
results=[]
def node(x,cid):return next(n for n in x['nodes'] if n['claim_id']==cid)
def dep(n):return {'claim_key':key(n),'statement_sha256':n['statement_sha256'],'hypothesis_instantiation':'Audit mutation only.','unit_conversion':None}
def reject(name,change,code):
    x=copy.deepcopy(g); change(x); r=validate(x,check_files=False)
    assert r['status']=='REJECT' and any(e.startswith(code) for e in r['errors']),r
    results.append({'fixture':name,'status':'PASS','error_code':code})
def cycle(x):
    a=node(x,'FEI-FINAL'); b=node(x,'B17-KB-TWO-SIDED')
    a['proof_dependencies']=[dep(b)]; b['proof_dependencies'].append(dep(a))
reject('new selectable route cannot assume FEI',cycle,'CYCLE_THROUGH_FINAL_FEI')
reject('MU pinned statement cannot drift',lambda x:node(x,'MU-FINITE-UNITARY-1988').update(exact_statement='H>=0 instead of original uncertainty theorem'),'STATEMENT_HASH')
reject('B09 dependency must name exact MU hash',lambda x:node(x,'B09-BIASED-BLOCK-UNCERTAINTY')['proof_dependencies'][0].update(statement_sha256='0'*64),'DEPENDENCY_HASH')
reject('unaccepted MU source blocks accepted B09 closure',lambda x:node(x,'MU-FINITE-UNITARY-1988').update(status='UNRESOLVED_SOURCE'),'ACCEPTED_DEPENDS_ON_UNRESOLVED')
reject('C018 candidate cannot pay its own premise',lambda x:x['candidate_routes'][-1]['requires'].append(x['final_claim']),'ROUTE_ASSUMES_CONCLUSION')
reject('an unknown version of finite certificate is not usable',lambda x:node(x,'B17-KB5-CUTOFF')['proof_dependencies'][0].update(claim_key='A082-FINITE-TRUE-ERASURE@2'),'MISSING_EXACT_DEPENDENCY')
reject('source locator cannot disappear',lambda x:node(x,'MU-FINITE-UNITARY-1988')['proof_sources'][0].update(locator=''),'MISSING_LOCATOR')
# Source-byte tampering fixture is isolated inside A081, never an original source.
temp=RUN/'out/tamper_fixture.txt'; temp.write_text('altered fixture bytes',encoding='utf-8')
def badbytes(x):
    x['sources']['MU1988_pdf']['local_path']=str(temp)
x=copy.deepcopy(g); badbytes(x); r=validate(x)
assert r['status']=='REJECT' and 'SOURCE_BYTES:MU1988_pdf' in r['errors']
results.append({'fixture':'primary-source bytes are checked','status':'PASS','error_code':'SOURCE_BYTES'})
saved={'status':'PASS','structural_fixtures':len(results),'fixtures':results,'accepted_B09_core_closure':[],'accepted_KB5_cutoff_closure':[],'all_six_FEI_routes_conditional':True,'elapsed_seconds':time.perf_counter()-started,'finite_census_repeated':False,'old_cycle_engine':'unchanged, stage1 exhaustive 66067 graph cases retained as source-bound evidence'}
(RUN/'out/UPDATE_AUDIT.json').write_text(json.dumps(saved,indent=2)+'\n',encoding='utf-8')
print(json.dumps(saved,indent=2))
