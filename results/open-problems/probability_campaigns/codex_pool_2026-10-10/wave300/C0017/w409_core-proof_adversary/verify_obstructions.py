"""Bounded exact-arithmetic mathematical regression checks, not a formal proof."""
from fractions import Fraction as F
from pathlib import Path
import ctypes
import json
import time
import tracemalloc

ROOT = Path(__file__).resolve().parent

class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [
        (name, ctypes.c_ulonglong) for name in
        ('total_phys','avail_phys','total_page','avail_page','total_virtual','avail_virtual','avail_extended')]

gate_time = time.time()
memory = MemoryStatus()
memory.length = ctypes.sizeof(memory)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
    raise RuntimeError('No fresh memory measurement; gate remains closed')
gate = {'measured_unix': gate_time, 'available_physical_bytes': memory.avail_phys,
        'required_available_bytes': 64*1024**2, 'maximum_cells': 85,
        'mesh_counts': [1,2,4,8], 'scope': 'one CPU, exact finite arithmetic only; no simulation, GPU or models',
        'approved': memory.avail_phys >= 64*1024**2}
(ROOT/'compute_gate.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
if not gate['approved']:
    raise RuntimeError('Fresh gate closed: insufficient available RAM')
start = time.perf_counter()
tracemalloc.start()

def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conjugate(z): return (z[0],-z[1])
def scale(z,q): return (z[0]*q,z[1]*q)
ZERO = (F(0),F(0))

def edge(u,v,fn):
    return scale(mul(add(fn(u),fn(v)),sub(v,u)),F(1,2))

def contour(vertices,fn):
    total = ZERO
    for u,v in zip(vertices,vertices[1:]+vertices[:1]):
        total = add(total,edge(u,v,fn))
    return total

rows=[]
checks=0
for n in gate['mesh_counts']:
    delta=F(1,n)
    total=ZERO
    for j in range(n):
        for k in range(n):
            u=(k*delta,j*delta)
            vs=[u,add(u,(delta,F(0))),add(u,(delta,delta)),add(u,(F(0),delta))]
            d=contour(vs,conjugate)
            assert d==(F(0),2*delta**2)
            assert contour(vs,lambda z:z)==ZERO
            checks+=2
            total=add(total,d)
    outer=contour([(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))],conjugate)
    assert total==outer==(F(0),F(2))
    checks+=1
    rows.append({'n':n,'cells':n*n,'individual_defect_imag':str(2*delta**2),
                 'summed_defect_imag':str(total[1]),'outer_integral_imag':str(outer[1])})

cardy_rows=[]
for x,y1,y2 in [(F(1),F(2),F(3)),(F(2),F(3),F(5)),(F(1,2),F(3,2),F(7,2))]:
    coeff=[]
    for y in (y1,y2):
        r=x/y
        log_derivative=-F(2,3)*(1/r-1/(1-r))
        a=(1-r)/y
        b=((1-r)**2*log_derivative-2*(1-r))/y**2
        drift=(2/r-2*r)/y**2
        assert drift+3*b==0
        assert b/(2*a)==-F(1,3)*(1/x+1/y)
        assert drift+2*b!=0  # wrong kappa=4 control
        checks+=3
        coeff.append((a,b))
    det=coeff[0][0]*coeff[1][1]-coeff[1][0]*coeff[0][1]
    assert det!=0
    assert coeff[0][0]*coeff[0][1]-coeff[0][0]*coeff[0][1]==0  # duplicated-observable control
    checks+=2
    cardy_rows.append({'x':str(x),'y1':str(y1),'y2':str(y2),
                       'determinant_divided_by_positive_derivative_product':str(det)})

peak=tracemalloc.get_traced_memory()[1]
receipt={'command':'python -B -X utf8 verify_obstructions.py','exact_assertions_passed':checks,
         'cells_checked':sum(n*n for n in gate['mesh_counts']), 'cell_obstruction':rows,
         'cardy_coefficient_controls':cardy_rows, 'elapsed_seconds':time.perf_counter()-start,
         'peak_traced_bytes':peak, 'formal_proof':False,
         'interpretation':'Exact finite diagnostic controls supplement the written general proofs. No test proves the square-bond probabilistic input.'}
(ROOT/'measurement.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
