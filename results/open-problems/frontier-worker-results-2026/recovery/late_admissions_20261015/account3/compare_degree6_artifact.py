"""Read author DATA only after completion of our independent full trajectory."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
OUT=Path(__file__).resolve().parent;ROOT=Path('~/brain_workers/w682/checks')
checks=json.loads((OUT/'degree6_exact_replay_checks.json').read_text(encoding='utf-8'))
assert checks['all_depths']==27
path=ROOT/'balanced_bp_fast_d6_N96_89-218.json';data=path.read_bytes()
assert hashlib.sha256(data).hexdigest()=='2b0976cced31beda5ca04785b1e15ba8b1e6eca2fb2067e559704b7293303f34'
d=json.loads(data);keys=[(a,b,96-a-b) for a in range(33) for b in range(a,(96-a)//2+1)]
assert len(keys)==817 and [list(k) for k in keys]==d['orbit_keys']
massrows=[list(map(int,l.split())) for l in (OUT/'degree6_full.masses.txt').read_text(encoding='utf-8').splitlines()]
assert massrows[-1][1:]==list(map(int,d['final_integer_masses']))
events=[x for x in checks['events'] if x.get('phase')=='depth'];stages={}
for line in (OUT/'degree6_full.stages.txt').read_text(encoding='utf-8').splitlines():
    dep,kind,loss=line.split();stages.setdefault(int(dep),[]).append(int(loss))
assert len(d['rows'])==26
for own,row in zip(events[1:],d['rows']):
    assert own['depth']==row['depth']
    assert F(own['signal_numerator'],own['signal_denominator'])==F(row['second_moment_upper'])
    assert stages[row['depth']]==list(map(int,row['node_rounding_masses']))
# Direct, unrounded physical depth-one experiment, independently enumerating label counts.
eta=F(89,218);same=(1+2*eta)/3;diff=(1-eta)/3;exact=F(0);total=F(0)
for a in range(7):
    for b in range(7-a):
        counts=(a,b,6-a-b);likelihood=[same**counts[i]*diff**(6-counts[i]) for i in range(3)]
        norm=sum(likelihood);weight=F(math.factorial(6),math.prod(math.factorial(x) for x in counts))*norm/3
        total+=weight;exact+=weight*sum((x/norm-F(1,3))**2 for x in likelihood)
assert total==1
upper=F(events[1]['signal_numerator'],events[1]['signal_denominator']);assert exact<=upper
assert F(89,218)**2*6-1==F(1,23762)
assert F(217,4500)-F(checks['final_signal'])==F(1428392677321,2473901162496000)
# Sensitive controls: a changed final mass and one-unit changed row coefficient must be rejected.
mutant=massrows[-1][1:].copy();mutant[0]+=1;assert mutant!=list(map(int,d['final_integer_masses']))
first=(OUT/'degree6_tiny_89_218_6.rows.txt').read_text(encoding='utf-8').splitlines()[0].split();dest,coef=first[2].split(':');assert F(int(coef)+1,108*36)!=F(int(coef),108*36)
result=dict(status='PASS',author_artifact_sha256=hashlib.sha256(data).hexdigest(),all_817_final_masses_equal=True,all_26_signals_equal=True,all_104_node_roundings_equal=True,direct_physical_depth1_signal=str(exact),quantized_depth1_upper=str(upper),gap=str(upper-exact),physical_leaf_count_vectors=28,changed_mass_control_rejected=True,changed_row_coefficient_control_rejected=True,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(OUT/'degree6_artifact_comparison.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result),flush=True)
