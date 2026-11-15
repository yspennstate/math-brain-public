from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import json
root=Path(__file__).resolve().parents[1]
source=Path('~/brain_workers/w682/checks/balanced_bp_fast_d6_N96_89-218.json')
expected='2b0976cced31beda5ca04785b1e15ba8b1e6eca2fb2067e559704b7293303f34'
assert sha256(source.read_bytes()).hexdigest()==expected
d=json.loads(source.read_text(encoding='utf-8'));S=2**32;N=96
orbits=[(a,b,N-a-b) for a in range(N+1) for b in range(a,N+1) if N-a-b>=b]
assert len(orbits)==817 and [list(x) for x in orbits]==d['orbit_keys']
assert len(d['rows'])==26
checked=[];artifact_hashes={}
for row in d['rows']:
    depth=row['depth'];p=root/f'checks/t067_d6_N96_own_depth_{depth:03}.txt'
    values=p.read_text().splitlines();mass=list(map(int,values[2:]))
    assert len(mass)==817 and sum(mass)==S
    signal=sum(F(m*(3*sum(k*k for k in o)-N*N),S*3*N*N) for m,o in zip(mass,orbits))
    assert F(values[1])==signal==F(row['second_moment_upper'])
    rp=root/f'checks/t067_d6_N96_own_revealed_{depth:03}.txt'
    reveals=[F(v)*S for v in rp.read_text().splitlines()]
    assert reveals==[int(v) for v in row['node_rounding_masses']]
    artifact_hashes[str(p.relative_to(root))]=sha256(p.read_bytes()).hexdigest()
    artifact_hashes[str(rp.relative_to(root))]=sha256(rp.read_bytes()).hexdigest()
    checked.append({'depth':depth,'signal':str(signal),'revealed':[int(v) for v in reveals]})
assert mass==[int(v) for v in d['final_integer_masses']]
assert signal==F(942948951491,19791209299968)<F(217,4500)
assert F(217,4500)-signal==F(1428392677321,2473901162496000)
assert 6*F(89,218)**2-1==F(1,23762)
preparation=json.loads((root/'checks/t067_degree6_preparation_own.json').read_text(encoding='utf-8'))
for claim,record in preparation['sources'].items():
    assert sha256(Path(record['path']).read_bytes()).hexdigest()==record['sha256'],claim
controls=json.loads((root/'checks/t067_universal_control_own.json').read_text(encoding='utf-8'))
assert controls['native_all7_edge_and49_unit_rows_compared'] and len(controls['native_trajectories_compared'])==4
receipt={'at':datetime.now().astimezone().isoformat(),'status':'complete independent degree6 comparison PASS','proof_bindings':preparation['sources'],
 'source_artifact_sha256':expected,'all_depth_signals_compared':26,'all_node_revelations_compared':104,
 'all_final_masses_compared':817,'all_orbit_keys_compared':817,'first_depths_N6_all_masses_compared':4,
 'own_unit_rows_constructed_and_normalized':667489,'own_unit_nonzeros':10106814,'own_edge_rows_constructed':817,'own_edge_nonzeros':2334,
 'unit_denominator':995328,'edge_denominator':654,'final_signal':str(signal),'radius':'217/4500','strict_gap':str(F(217,4500)-signal),
 'eta_squared_critical_gap':'1/23762','depths':checked,'own_artifact_hashes':artifact_hashes,
 'evaluator_sha256':sha256((root/'checks/t067_degree6_own.cs').read_bytes()).hexdigest(),
 'not_claimed':'No direct per-state comparison of entire N96 fusion table to author table; both are independently derived. No novelty/admission decision.'}
(root/'checks/t067_degree6_compare_own.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','all_depth_signals_compared','all_node_revelations_compared','all_final_masses_compared','strict_gap']}))
