"""Small deterministic checks; numerical receipts are not proof certificates."""
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
from fractions import Fraction
import json
import math
from pathlib import Path
import shutil
import time

base = Path(__file__).resolve().parent

class MemoryStatus(ctypes.Structure):
    _fields_ = [('length',wintypes.DWORD),('load',wintypes.DWORD),
                ('total_phys',ctypes.c_ulonglong),('avail_phys',ctypes.c_ulonglong),
                ('total_page',ctypes.c_ulonglong),('avail_page',ctypes.c_ulonglong),
                ('total_virtual',ctypes.c_ulonglong),('avail_virtual',ctypes.c_ulonglong),
                ('avail_extended',ctypes.c_ulonglong)]

def cpu_times():
    values = [wintypes.FILETIME() for _ in range(3)]
    if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in values)):
        raise OSError('GetSystemTimes failed')
    return tuple((v.dwHighDateTime << 32) + v.dwLowDateTime for v in values)

memory = MemoryStatus()
memory.length = ctypes.sizeof(memory)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
    raise OSError('GlobalMemoryStatusEx failed')
first = cpu_times()
time.sleep(0.2)
second = cpu_times()
idle, kernel, user = (b-a for a,b in zip(first,second))
total = kernel+user
cpu = 100*(1-idle/total) if total else 100.0
gate = {'utc':datetime.now(timezone.utc).isoformat(),
        'available_memory_bytes':memory.avail_phys,'cpu_percent_sample':cpu,
        'available_disk_bytes':shutil.disk_usage(base).free,
        'limits':{'min_memory_bytes':268435456,'max_cpu_percent':97,
                  'min_disk_bytes':16777216,'max_matrix_dimension':16,
                  'max_pair_points':256,'max_quadrature_steps':8000,
                  'max_compute_wall_seconds':10,'gpu':False,'training':False}}
gate['allowed'] = memory.avail_phys>=268435456 and cpu<97 and gate['available_disk_bytes']>=16777216
(base/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2),encoding='utf-8')
if not gate['allowed']:
    receipt={'status':'SKIPPED_RESOURCE_GATE','gate':gate,'formal_check':False}
    (base/'MATH_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print(json.dumps(receipt),flush=True)
    raise SystemExit(0)

started=time.monotonic()
checks=[]
def record(name, ok, evidence):
    checks.append({'name':name,'pass':bool(ok),'evidence':evidence})
    (base/'MATH_CHECKS.json').write_text(json.dumps({'status':'RUNNING','formal_check':False,'checks':checks},indent=2),encoding='utf-8')
    if time.monotonic()-started>10:
        raise RuntimeError('Fresh compute gate wall budget exceeded; stopping this foreground check')

def poisson(t,eta):
    return eta/(math.pi*(t*t+eta*eta))

energies=[-0.75,0.4,1.25]
weights=[0.2,0.5,0.3]
eta=0.5
pair=math.fsum(a*b*poisson(s-t,2*eta) for s,a in zip(energies,weights) for t,b in zip(energies,weights))
steps=8000
left,right=-40.0,40.0
step=(right-left)/steps
def square_density(x):
    return math.fsum(a*poisson(x-s,eta) for s,a in zip(energies,weights))**2
quadrature=step/3*(square_density(left)+square_density(right)+math.fsum((4 if i%2 else 2)*square_density(left+i*step) for i in range(1,steps)))
record('L1 pair formula vs independent energy quadrature',abs(pair-quadrature)<1e-6,
       {'pair_formula':pair,'quadrature':quadrature,'absolute_error':abs(pair-quadrature),'steps':steps})

n=8
walsh=[[(-1)**((i&j).bit_count()) for j in range(n)] for i in range(n)]
gram_ok=all(sum(walsh[i][k]*walsh[j][k] for k in range(n))==(n if i==j else 0) for i in range(n) for j in range(n))
atoms=[sum(Fraction(2*((j>>i)&1),3**(i+1)) for i in range(3)) for j in range(n)]
h=[[sum(Fraction(walsh[i][q]*walsh[j][q],n)*atoms[q] for q in range(n)) for j in range(n)] for i in range(n)]
eig_ok=all(sum(h[i][q]*walsh[q][j] for q in range(n))==atoms[j]*walsh[i][j] for i in range(n) for j in range(n))
record('L5 exact Walsh orthogonality and constructed eigenvalue equations',gram_ok and eig_ok,
       {'dimension':n,'exact_fraction_arithmetic':True,'flat_squared_component':str(Fraction(1,n))})

alpha=math.log(2)/math.log(3)
cantor_rows=[]
for k in [2,4,6,8]:
    count=2**k
    values=[sum(2*((j>>i)&1)/(3**(i+1)) for i in range(k)) for j in range(count)]
    height=count**-0.5
    s=math.fsum(poisson(x-y,2*height) for x in values for y in values)/(count*count)
    diagonal=1/(2*math.pi*height*count)
    lower=height**(alpha-1)/(5*math.pi)
    cantor_rows.append({'k':k,'N':count,'eta':height,'S':s,'diagonal':diagonal,
                        'off_diagonal':s-diagonal,'proved_lower_bound':lower,
                        'off_diagonal_fraction':(s-diagonal)/s})
record('L5 Cantor positive cross pairs and asymptotic-bound controls',
       all(r['S']>=r['proved_lower_bound'] and r['off_diagonal']>0 for r in cantor_rows)
       and all(a['diagonal']>b['diagonal'] for a,b in zip(cantor_rows,cantor_rows[1:])),
       {'alpha':alpha,'rows':cantor_rows})

sample_energies=[Fraction(0),Fraction(1,7),Fraction(2,7),Fraction(1,2),Fraction(6,7),Fraction(1)]
cover_ok=True
cases=0
for radius in [Fraction(1,16),Fraction(1,7),Fraction(1,2),Fraction(1)]:
    bin_count=math.ceil(Fraction(1)/radius)
    intervals=[(i*radius-radius,min((i+1)*radius,Fraction(1))+radius) for i in range(bin_count)]
    exact_count=sum(1 for i,x in enumerate(sample_energies) for j,y in enumerate(sample_energies) if i!=j and abs(x-y)<=radius)
    covered_count=sum(sum(lo<=x<=hi for x in sample_energies)*(sum(lo<=x<=hi for x in sample_energies)-1) for lo,hi in intervals)
    cover_ok=cover_ok and exact_count<=covered_count and bin_count<=2/radius
    cases+=1
record('L6 short-interval pair covering including endpoint cases',cover_ok,{'exact_fraction_cases':cases})

beta=math.gamma(0.5)*math.gamma(0.25)/math.gamma(0.75)
free_bound=beta**2/(2*math.pi**3)
record('L7 finite explicit free-model bound',0<free_bound<1,{'bound':free_bound,'beta':beta})

heights=[0.5,0.25,0.125,0.0625]
atom_rows=[{'eta':t,'second_moment':1/(2*math.pi*t),
            'averaged_density_max':2*math.atan(0.5/t)/math.pi} for t in heights]
record('L8 bounded averaged density with divergent quenched second moment',
       all(r['averaged_density_max']<=1 for r in atom_rows)
       and all(abs(b['second_moment']/a['second_moment']-2)<1e-12 for a,b in zip(atom_rows,atom_rows[1:])),
       {'rows':atom_rows})

receipt={'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL',
         'formal_check':False,'trusted_axioms':'Not a formal theorem receipt; analytic proofs are in ATTEMPT.md',
         'checks':checks,'check_count':len(checks),'elapsed_compute_seconds':time.monotonic()-started,
         'command':'python -X utf8 -u ~/brain_workers/w483/verify_math.py'}
(base/'MATH_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt),flush=True)
if receipt['status']=='FAIL':
    raise SystemExit(1)
