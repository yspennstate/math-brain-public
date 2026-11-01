"""Separate Fraction and arbitrary-integer checks of the radix fusion."""
import os
for name in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
import ctypes,datetime,hashlib,json,time
class Memory(ctypes.Structure):
    _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(k,ctypes.c_ulonglong) for k in ['total','available','page_total','page_available','virtual_total','virtual_available','extended']]
def guard():
    m=Memory();m.length=ctypes.sizeof(m);assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m));assert m.available>=2*1024**3;return m.available
available=guard();start=time.monotonic()
import numpy as np
from radix_unit_fusion import RadixUnitFusion,digest
from universal_fusion import unit_table,reference_pair,edge_table,apply_edge,apply_table,signal
from gw23_mixture_interval_upper import mix
r=Path(__file__).resolve().parent;root=r.parent
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'INCOMPLETE arithmetic checks','source_sha256':{p:digest(r/p) for p in ['radix_unit_fusion.py','validate_radix_unit_fusion.py','universal_fusion.py','ternary_bp_int.py','gw23_mixture_interval_upper.py']},'small_checks':[],'negative_controls':[],'available_bytes_at_start':available}
def save():
    p=r/'radix_unit_fusion_validation.json';temp=p.with_suffix('.json.part');temp.write_text(json.dumps(result,indent=2),encoding='utf-8',newline='');temp.replace(p)
N=6;table=unit_table(N);keys=table[0];vertex=keys.index((0,0,N));fast=RadixUnitFusion(table)
refs={(i,j):reference_pair(N,keys,i,j)[0] for i in range(len(keys)) for j in range(len(keys))}
def rounded(values,scale):
    out=[v.numerator*scale//v.denominator for v in values];out[vertex]+=scale-sum(out);return [F(v,scale) for v in out]
def fuse_ref(left,right,scale):
    out=[F(0)]*len(keys)
    for i,x in enumerate(left):
        for j,y in enumerate(right):
            for k,w in refs[i,j].items():out[k]+=x*y*w
    return rounded(out,scale)
for bits in [8,32,48]:
    S=1<<bits
    for theta in [F(0),F(1,2),F(51,100),F(1)]:
        for eta in [F(0),F(253,400),F(1)]:
            edge=edge_table(N,eta,keys);m=[0]*len(keys);m[vertex]=S;law=[F(v,S) for v in m]
            for depth in range(1,5):
                child_ref=[F(0)]*len(keys)
                for i,x in enumerate(law):
                    for k,n in edge[1][i].items():child_ref[k]+=x*F(n,edge[0])
                child_ref=rounded(child_ref,S);pair_ref=fuse_ref(child_ref,child_ref,S);triple_ref=fuse_ref(pair_ref,child_ref,S)
                law=rounded([(1-theta)*x+theta*y for x,y in zip(pair_ref,triple_ref)],S)
                child,l0=apply_edge(edge,m,S,vertex);prepared=fast.prepare_right(child,S)
                pair,l1=fast.fuse(child,prepared,S);triple,l2=fast.fuse(pair,prepared,S);m,l3=mix(pair,triple,theta,S,vertex)
                assert law==[F(v,S) for v in m]
                result['small_checks'].append({'bits':bits,'theta':str(theta),'eta':str(eta),'depth':depth,'x':str(signal(keys,m,N,S))})
    save();print('SMALL bits'+str(bits)+' complete',flush=True)
for label,fn in [('unsafe_limb',lambda:RadixUnitFusion(table,limb_bits=64)),('negative_input',lambda:fast.prepare_right([-1]+[0]*(len(keys)-2)+[257],256))]:
    try:fn()
    except (AssertionError,ValueError):result['negative_controls'].append(label+' rejected')
    else:raise AssertionError('Invalid arithmetic input accepted: '+label)
bad=list(table);bad[6]=np.array(table[6],copy=True);bad[6][0]+=1
try:RadixUnitFusion(tuple(bad))
except (AssertionError,ValueError):result['negative_controls'].append('changed_coefficient rejected')
else:raise AssertionError('Changed coefficient accepted')
result['status']='PASS144 Fraction updates and3 negative controls; N96 benchmark pending';save()
assert time.monotonic()-start<380,'Small phase saved; inspect budget before the N96 phase.'
available=guard();stem=r/'universal_unit_N96_1';parts=[Path(str(stem)+'_'+name+'.bin') for name in ['dest_indices','numerators','offsets','pair_i','pair_j']]
assert stem.with_suffix('.json').exists() and all(p.exists() for p in parts) and sum(p.stat().st_size for p in parts)==106408056
table=unit_table(96);build=time.monotonic();fast=RadixUnitFusion(table,r/'radix_cache');build_seconds=time.monotonic()-build
p=r/'gw23_interval_1-2_51-100_eta253-400_bits32.json';raw=p.read_bytes();u=json.loads(raw)
for name,h in u['source_sha256'].items():assert digest(r/name)==h
prefix=root/'checkpoints'/('gw23_interval_original_d'+str(u['completed_depth'])+'_'+hashlib.sha256(raw).hexdigest()[:12]+'.json')
if prefix.exists():assert prefix.read_bytes()==raw
else:prefix.write_bytes(raw)
S=1<<u['bits'];keys=table[0];vertex=keys.index((0,0,96));m=list(map(int,u['integer_masses']));edge=edge_table(96,F(u['eta']),keys);child,l0=apply_edge(edge,m,S,vertex)
t=time.monotonic();old_pair,old_l1=apply_table(table,child,child,S,False);old_triple,old_l2=apply_table(table,old_pair,child,S,False);old_seconds=time.monotonic()-t
t=time.monotonic();prepared=fast.prepare_right(child,S);pair,l1=fast.fuse(child,prepared,S);triple,l2=fast.fuse(pair,prepared,S);new_seconds=time.monotonic()-t
assert pair==old_pair and triple==old_triple and (l1,l2)==(old_l1,old_l2)
out,l3=mix(pair,triple,F(u['theta_comparison']),S,vertex);x=signal(keys,out,96,S)
seed={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Exact baseline-matched continuation seed','previous_checkpoint':str(prefix.relative_to(root)),'previous_sha256':digest(prefix),'completed_depth':u['completed_depth']+1,'theta_interval':u['theta_interval'],'eta':u['eta'],'grid':96,'bits':u['bits'],'x':str(x),'strict_entry':x<F(1,50),'orbit_keys':keys,'integer_masses':list(map(str,out)),'rows':u['rows']+[{'depth':u['completed_depth']+1,'x':str(x),'rounding_loss_masses':[l0,l1,l2,l3]}],'source_sha256':result['source_sha256'],'kernel':fast.metadata}
seed_path=r/'radix_gw23_continuation_seed.json';seed_path.write_text(json.dumps(seed,separators=(',',':')),encoding='utf-8',newline='')
result.update(status='PASS144 Fraction updates,3 negative controls and both full N96 fusion outputs/all817 masses against original arbitrary-integer loops',kernel=fast.metadata,cache_setup_seconds=build_seconds,old_two_fusions_seconds=old_seconds,new_two_fusions_seconds=new_seconds,observed_ratio=old_seconds/new_seconds,baseline_depth=u['completed_depth'],seed_depth=seed['completed_depth'],seed_sha256=digest(seed_path),elapsed_seconds=time.monotonic()-start,available_bytes_before_N96=available)
save();print(json.dumps({k:v for k,v in result.items() if k not in ['small_checks','source_sha256']}),flush=True)
