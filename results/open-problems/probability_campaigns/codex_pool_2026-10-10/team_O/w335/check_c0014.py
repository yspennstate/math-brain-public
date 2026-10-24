from fractions import Fraction as F
import json
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
cases=[]
for M in (F(1),F(2),F(10),F(100),F(1000),F(1000000)):
    va,vb=M/(M+1),1/(M+1)
    assert (va-1)+(va-0)/M==0
    assert (vb-1)/M+(vb-0)==0
    current=(1-va)+(1-vb)/M
    original=1/current
    wired=2*M/(M+1)
    assert original==(M+1)/2
    assert wired<=original
    assert original/wired==(M+1)**2/(4*M)
    mismatch=M/(M+1)-1/(M+1)
    assert (mismatch==0)==(M==1)
    cases.append({'M':str(M),'original_R':float(original),'wired_layer_sum':float(wired),'ratio':float(original/wired),'interface_current_mismatch':float(mismatch)})
measurement={'command':'python -X utf8 check_c0014.py','exact_four_vertex_cases':len(cases),'cases':cases,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'c0014_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
statement='In a finite resistor network whose contracted intermediate interfaces yield a series chain of independently wired layer networks, the sum of those wired layer resistances is at most the original effective resistance. Rayleigh monotonicity alone cannot justify the opposite upper bound. On s-a-t and s-b-t with resistances (1,M) and (M,1), respectively, the original resistance is (M+1)/2 and the wired layer sum is 2M/(M+1). Their ratio (M+1)^2/(4M) is unbounded. To upper-bound the original resistance using layer flows, the interface current distributions must match. This does not identify a DGFF limiting law or refute an upper bound constructed using matched flows.'
proof=(root/'C0014_proof.md').read_text(encoding='utf-8').split('For a finite positive-resistance',1)[1].split('\n\nThe earlier C0014 attempt',1)[0]
new=entry('c0014-wiring-direction','probability.electrical-networks','wired-layer-resistance-lower-comparison-and-interface-current-obstruction','lemma','Wired interfaces reverse the unsupported layer upper comparison',statement,'For a finite positive-resistance'+proof,['Finite positive-resistance network','Wired layer terminal minima','Contracted quotient is a series chain'])
relations=[edge_to_problem('C0014',new['key'],'This does not identify a DGFF limiting law'),edge_to_attempt('C0014',new['key'],'Rayleigh monotonicity alone cannot justify the opposite upper bound','Rayleigh monotonicity gives R_eff(x, D_N^c) <= sum over dyadic annuli around x of the resistance across the annulus','refutes')]
emit(6,'C0014',[new],relations,'C0014_proof.md','c0014_measurement.json')
print(json.dumps(measurement),flush=True)
