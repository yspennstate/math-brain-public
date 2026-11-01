"""One explicit full-reference replay; shared helper, not independent acceptance."""
from pathlib import Path
import ast,json,hashlib
from fractions import Fraction
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
def write(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8')
write('FROZEN_EXAMPLE.json',{'family':'F=1-2A2+2A5','root':{'a':2,'b':1,'r':2,'reference':'spiked'},'ordered_query_types':'CD','cases':1,'arithmetic':'Fraction/fixedN12 inherited certified helper','memory_MB':120,'max_runtime_seconds':55,'purpose':'Record full atoms for one already-certified spent-bank nonflat dummy row; not a new search.'})
path=RUN/'code/certify_dummy.py'; tree=ast.parse(path.read_text(encoding='utf-8'))
body=[]
for item in tree.body:
    if isinstance(item,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='ROOTS' for x in item.targets):break
    body.append(item)
env={'__file__':str(path),'__name__':'certificate_helpers'}
exec(compile(ast.Module(body=body,type_ignores=[]),str(path),'exec'),env)
F=Fraction; root=(2,1,2,env['ref'](2,1,'spiked'))
env['physical_check'](2,1,2)
amp,p,q,c,W,e=env['node'](*root)
first,_,_=env['advance'](*root,'C')
B0=env['erasure'](p,3); old0=env['marginal'](q,3)
po0=tuple((x-y)**2 for x,y in env['pairs'](amp,3)); off0=env['ce'](po0,old0)
amp1,p1,q1,c1,W1,e1=env['node'](*first)
second,_,row=env['advance'](*first,'D')
B1=env['erasure'](p1,2); inherited=env['marginal'](q1,2)
po1=tuple((x-y)**2 for x,y in env['pairs'](amp1,2))
off1=env['ce'](po1,inherited); p2=env['node'](*second)[1]; q2=env['node'](*second)[2]
on=env['ce'](p2,q2)
add,mul=env['add'],env['mul']
ledger=add(B0,add(mul(F(1,2),off0),add(mul(F(1,2),B1),mul(F(1,4),add(off1,on)))))
Ig=F(1);z=c[1]/Ig;C0=max(F(4),F((z.numerator+z.denominator-1)//z.denominator))
quota=(2*C0+10)*(Ig+e)
assert row['nonflat'] and row['both_children_nonconstant']
assert quota-ledger[1]>=12*e
assert len(p1)==len(q1)==16 and len(p2)==len(q2)==8
write('EXPLICIT_SPENT_ROW.json',{'helper_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'root_parameters':[2,1,2],'root_source_R':root[3],'source_C0':C0,'root_quota':quota,'root_e':e,'history':'CD','reach_at_dummy':F(1,2),'booked_control_erasure':B0,'retained_control_off_cost':off0,'dummy_parent_parameters':list(first[:3]),'dummy_parent_source_R':first[3],'dummy_parent_amplitudes':amp1,'dummy_parent_spectrum':p1,'dummy_parent_full_reference':q1,'dummy_full_inherited_reference':inherited,'dummy_off_true_spectrum':po1,'dummy_on_true_spectrum':p2,'dummy_fresh_on_full_reference':q2,'dummy_fresh_source_R':second[3],'dummy_signed_reset_cost':row['reset_Z'],'dummy_erasure':B1,'dummy_off_full_CE':off1,'dummy_on_full_CE':on,'complete_two_query_ledger':ledger,'certified_remaining':(quota-ledger[1],quota-ledger[0]),'certified_remaining_over_root_e':(quota-ledger[1])/e,'new_acceptance':'NONE: explicit replay shares certified helper'})
result=json.loads((OUT/'RESULT.json').read_text(encoding='utf-8'))
pilot=json.loads((OUT/'PILOT_RESULT.json').read_text(encoding='utf-8'))
claims=json.loads((RUN/'CLAIMS.json').read_text(encoding='utf-8'))
progress=json.loads((RUN/'PROGRESS.json').read_text(encoding='utf-8'))
assert result['status']==pilot['status']=='PASS'
assert claims[0]['statement_sha256']==hashlib.sha256(claims[0]['exact_statement'].encode('utf-8')).hexdigest()
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
status=(RUN.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines()
assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
assert progress['packet_ids']==['A073']
assert 'Universal bridge' in (RUN/'REPORT.md').read_text(encoding='utf-8')
assert all(p.stat().st_size<20*1024**2 for p in RUN.rglob('*') if p.is_file())
manifest=json.loads((OUT/'source_read_manifest.json').read_text(encoding='utf-8'))
assert len(manifest)==29
write('FINAL_AUDIT.json',{'status':'PASS','main_assertions':result['assertions'],'pilot_assertions':pilot['assertions'],'pilot_seconds':pilot['runtime_seconds'],'main_seconds':result['runtime_seconds'],'full_reference_example':'EXPLICIT_SPENT_ROW.json','checks':['statement hash','progress equals delta','two-line status','required bridge paragraph','source manifest29','20MB limits','explicit full-reference CD ledger margin'],'independent_review':'PENDING','Lean':'NOT_CHECKED_ADMISSION_REFUSED','full_FEI':'OPEN'})
files=[]
for p in RUN.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        data=p.read_bytes();files.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
write('PERSISTENCE_RECEIPTS.json',{'field_sets':'PASS in finish_stage.py','statement_sha256':'PASS','progress_equals_delta':True,'final_audit':'PASS','files':files,'remote_copy':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps(json.loads((OUT/'FINAL_AUDIT.json').read_text(encoding='utf-8')),indent=2))
print('STATUS:',status[0])
