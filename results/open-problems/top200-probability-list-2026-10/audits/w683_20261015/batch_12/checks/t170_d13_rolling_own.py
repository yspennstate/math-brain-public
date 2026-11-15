"""From-proof independent constructive verifier; no author program imports."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime
import json,time,ctypes,struct
ROOT=Path(__file__).resolve().parents[1]
AUTHOR=Path('~/crash_recovery_20261014/workers_1015/term_362ebe34')
def digest(p): return sha256(p.read_bytes()).hexdigest()
def write(name,value): (ROOT/'checks'/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
class Memory(ctypes.Structure):
    _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(s,ctypes.c_ulonglong) for s in ['total_phys','avail_phys','total_page','avail_page','total_virtual','avail_virtual','avail_extended']]
mem=Memory();mem.length=ctypes.sizeof(mem)
assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem))
assert mem.avail_phys>=2*1024**3,'Wait rather than competing for low memory'
start=time.monotonic()
manifest=json.loads((AUTHOR/'T170_D13_SUBMISSION_v2.json').read_text(encoding='utf-8'))
hashes={}
for name,expected in manifest['files'].items():
    actual=digest(AUTHOR/name); assert actual==expected,(name,actual)
    hashes[name]=actual
for name,expected in manifest['dependencies'].items(): assert digest(Path(name))==expected,name
data=json.loads((AUTHOR/'T170_THREE_COMPRESSED_d13_C256_BASE.json').read_text(encoding='utf-8'))
C=data['cap']; S=data['scale']; A=data['alpha0_units']; H=data['base_bias']
assert (data['dimension'],data['width'],C,S,A,len(H))==(13,3,256,2**40,104206661983,65536)
assert all(type(v) is int and -S<=v<=S for v in H)
alpha=Q(A,S)
assert alpha==Q(manifest['axis'])

# Independent horizontal count: exactly the induced Q12 edges.
sigma=[0]
for n in range(1,C+1):
    edges=sum(v<(v^(1<<k))<n for v in range(n) for k in range(12))
    assert edges==sum(v.bit_count() for v in range(n))
    sigma.append(24*n-2*edges)
assert min(sigma[1:])>0

def idx(a,b): return (a-1)*C+b-1
def base(a,b): return H[idx(a,b)]
def ceil_div(n,d):
    q,r=divmod(n,d)
    return q+(r!=0)
assert [ceil_div(n,2) for n in [-5,-4,-1,0,1,4,5]]==[-2,-2,0,0,1,2,3]

# One previous a-plane and one current plane; b,c ascend in storage,
# while all three dependencies are already evaluated in descending loops.
prev=None; value_min=min(H);value_max=max(H); min_slack=None;max_slack=0
max_required=None;witness=None;max_numerator=0;max_total_rate=0
interiors=0;bases=0;fingerprint=sha256()
for a in range(C,0,-1):
    assert time.monotonic()-start<480,'Bounded foreground run only'
    curr=[0]*(C*C)
    ra=sigma[a] if a<C else 0
    for b in range(C,0,-1):
        rb=sigma[b]+max(a-b,0) if b<C else 0
        off=(b-1)*C
        curr[off]=base(a,b)
        for c in range(C,1,-1):
            rc=sigma[c]+max(b-c,0) if c<C else 0
            rate=ra+rb+rc+c
            assert 1<=rate<=19200
            max_total_rate=max(max_total_rate,rate)
            numerator=S+c*(base(b,c)-A)
            if ra: numerator+=ra*prev[off+c-1]
            if rb: numerator+=rb*curr[off+C+c-1]
            if rc: numerator+=rc*curr[off+c]
            value=ceil_div(numerator,rate)
            curr[off+c-1]=value
            # Independent direct generator form, rather than only ceil property.
            residual=S-A*c+c*(base(b,c)-value)
            if ra: residual+=ra*(prev[off+c-1]-value)
            if rb: residual+=rb*(curr[off+C+c-1]-value)
            if rc: residual+=rc*(curr[off+c]-value)
            slack=-residual
            assert 0<=slack<rate and residual==numerator-rate*value
            assert -S<=value<=S
            value_min=min(value_min,value);value_max=max(value_max,value)
            min_slack=slack if min_slack is None else min(min_slack,slack)
            max_slack=max(max_slack,slack);max_numerator=max(max_numerator,abs(numerator))
            interiors+=1
        value=base(a,b)
        rc=sigma[1]+max(b-1,0)
        required=S+(base(b,1)-value)+rc*(curr[off+1]-value)
        if ra: required+=ra*(base(a+1,b)-value)
        if rb: required+=rb*(base(a,b+1)-value)
        assert required<=A,(a,b,required)
        if max_required is None or required>max_required:
            max_required=required
            witness={'a':a,'b':b,'h':value,'h_c2':curr[off+1],'front_h':base(b,1),'ra':ra,'rb':rb,'rc':rc,'a_child':base(a+1,b) if ra else None,'b_child':base(a,b+1) if rb else None,'required':required}
        bases+=1
    fingerprint.update(struct.pack('<'+str(C*C)+'q',*curr))
    prev=curr
    if a%32==0 or a==1:
        write('t170_d13_rolling_checkpoint_own.json',{'completed_a_down_to':a,'interior_states':interiors,'base_states':bases,'max_required_so_far':max_required,'elapsed_seconds':time.monotonic()-start,'restart':'No background process; rerun only if incomplete, full run below480s and <10MB working arrays'})
assert (interiors,bases)==(16711680,65536)
assert max_required==104206641546 and A-max_required==20437
bad_coefficient=max_required-1
actual_fault=S-bad_coefficient+(witness['front_h']-witness['h'])+witness['rc']*(witness['h_c2']-witness['h'])
if witness['ra']: actual_fault+=witness['ra']*(witness['a_child']-witness['h'])
if witness['rb']: actual_fault+=witness['rb']*(witness['b_child']-witness['h'])
assert actual_fault==1 # reconstruct actual generator row, not required-minus-required algebra

def solve(matrix,rhs):
    n=len(rhs);m=[[Q(x) for x in row]+[Q(y)] for row,y in zip(matrix,rhs)]
    for j in range(n):
        k=next(k for k in range(j,n) if m[k][j]);m[j],m[k]=m[k],m[j]
        x=m[j][j];m[j]=[v/x for v in m[j]]
        for k in range(n):
            if k!=j:
                x=m[k][j];m[k]=[v-x*w for v,w in zip(m[k],m[j])]
    return [r[-1] for r in m]
states=[(a,b,c) for a in (1,2) for b in (1,2) for c in (1,2)]
G=[[0]*8 for _ in states];K=[[0]*8 for _ in states]
for i,(a,b,c) in enumerate(states):
    events=[((b,c,1),c)]
    if a<2: events.append(((a+1,b,c),sigma[a]))
    if b<2: events.append(((a,b+1,c),sigma[b]+max(a-b,0)))
    if c<2: events.append(((a,b,c+1),sigma[c]+max(b-c,0)))
    for state,rate in events:
        j=states.index(state);G[i][i]-=rate;G[i][j]+=rate
        K[i][i]+=rate
        if j!=0: K[i][j]-=rate
pi=solve([[G[j][i] for j in range(8)] for i in range(7)]+[[1]*8],[0]*7+[1])
assert all(p>0 for p in pi) and all(sum(pi[j]*G[j][i] for j in range(8))==0 for i in range(8))
stationary=1/sum(p*c for p,(a,b,c) in zip(pi,states))
cycle_t=solve(K,[1]*8)[0];cycle_a=solve(K,[c for a,b,c in states])[0]
wrong_a=solve(K,[0 if (a,b,c)==(1,1,1) else c for a,b,c in states])[0]
assert stationary==cycle_t/cycle_a and cycle_t/wrong_a!=stationary

diag=json.loads(Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json').read_text(encoding='utf-8'))
row=next(r for r in diag['rows'] if r['d']==13)['lower']
lower=Q(int(row['n']),int(row['d']));floor=Q(95165638290,10**12)
assert Q(manifest['diagonal_floor_down'])==floor<=lower and alpha<floor
receipt={'at':datetime.now().astimezone().isoformat(),'status':'exact finite constructive certificate PASS',
 'proof_sha256':hashes['T170-LEAD-ROLLING-D13-001_v2.md'],'artifact_hashes_verified':hashes,'dependency_hashes_verified':manifest['dependencies'],
 'all_states_independently_constructed_and_checked':interiors+bases,'interior_states':interiors,'base_states':bases,
 'source':'from proof only; no author program read, copied, imported or executed','precision':'unbounded Python integers and Fraction controls',
 'scale':S,'alpha_units':A,'max_required_units':max_required,'base_margin_units':A-max_required,'actual_base_fault_witness':witness,
 'min_interior_ceiling_slack':min_slack,'max_interior_ceiling_slack':max_slack,'min_h_units':value_min,'max_h_units':value_max,
 'max_abs_numerator':max_numerator,'max_total_rate':max_total_rate,'all_value_plane_hash':fingerprint.hexdigest(),
 'hash_order':'a descending256..1, then b ascending1..256, then c ascending1..256, little-endian signed64',
 'cap2_stationary':[str(p) for p in pi],'cap2_cycle_time':str(cycle_t),'cap2_cycle_advance':str(cycle_a),'cap2_ratio':str(stationary),'cap2_wrong_self_ratio':str(cycle_t/wrong_a),
 'axis':str(alpha),'diagonal_floor':str(floor),'raw_diagonal_lower':str(lower),'gap':str(floor-alpha),
 'free_memory_bytes_start':mem.avail_phys,'working_array_size':'two256x256 Python-int planes plus65536 base integers; under20MB',
 'elapsed_seconds':time.monotonic()-start,'evaluator_sha256':digest(Path(__file__)),
 'physical_argument':'requires separate full audit','account':'actual account4, same as lead; no distinct-account admission asserted'}
write('t170_d13_rolling_own.json',receipt)
print(json.dumps({k:receipt[k] for k in ['status','all_states_independently_constructed_and_checked','max_required_units','base_margin_units','cap2_ratio','gap','elapsed_seconds']}))
