from fractions import Fraction as F
import json
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
cases=[]
previous=None
for a in (F(1,100),F(1,10),F(1,2),F(1),F(2),F(4),F(9),F(99)):
    cs_spine=(2+a)/(2+2*a)
    cs_leaf=a/(2+2*a)
    assert cs_spine+cs_leaf==1
    assert cs_spine*a/(2+a)==cs_leaf
    horizontal_rate=2/(2+a)
    cs_D=cs_spine*horizontal_rate
    vs_D=F(1,2)*2
    assert cs_D==1/(1+a)
    assert cs_D*(2+2*a)==2
    assert vs_D==1
    if previous is not None:
        assert cs_D<previous
    previous=cs_D
    cases.append({'leaf_conductance':str(a),'cs_spine_mass':float(cs_spine),'constant_speed_variance_rate':float(cs_D),'variable_speed_variance_rate':float(vs_D),'conductivity':1})
measurement={'command':'python -X utf8 check_c0073.py','exact_clock_normalization_cases':len(cases),'cases':cases,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'c0073_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
statement='On the integer spine with unit conductances and a conductance-a dangling leaf at each site, a>0, project both vertices in a cell to its integer coordinate. The rate-one constant-speed walk has variance growth D_CS=1/(1+a), whereas the edge-rate variable-speed walk has D_VS=1. Electrical conductivity per cell is one for every a. The speed masses are respectively 2+2a and 2, so increasing leaf conductance slows the constant-speed walk despite nondecreasing conductivity. This is a periodic-network normalization example, not a counterexample to iid high-dimensional percolation monotonicity or its proposed critical exponent.'
proof=(root/'C0073_proof.md').read_text(encoding='utf-8').split('For the continuous-time constant-speed',1)[1].split('\n\nThe prior C0073 attempt',1)[0]
new=entry('c0073-speed-measure-obstruction','probability.random-walks','dangling-leaf-conductance-constant-speed-diffusion-normalization','lemma','Walk clocks change the conductivity-to-diffusion comparison',statement,'For the continuous-time constant-speed'+proof,['Periodic decorated integer spine','Positive dangling conductance a','Diffusion means coordinate variance growth per unit time','Specified constant-speed or edge-rate clock'])
relations=[edge_to_problem('C0073',new['key'],'This is a periodic-network normalization example','analogous_to'),edge_to_attempt('C0073',new['key'],'increasing leaf conductance slows the constant-speed walk','times the degree normalisation','analogous_to')]
emit(7,'C0073',[new],relations,'C0073_proof.md','c0073_measurement.json')
print(json.dumps(measurement),flush=True)
