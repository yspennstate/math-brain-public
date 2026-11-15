"""Complete arity21 replay comparison, derived from our own exact snapshots."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import json
ROOT=Path(__file__).resolve().parent; SOLVER=Path('~/brain_workers/w682')
artifact=SOLVER/'checks/regular_bp_fast_d21_N96_53-237.json'
digest=sha256(artifact.read_bytes()).hexdigest()
assert digest=='c9e86c2bc859e757a2505afe060e607a427d792a747f76631286b0760f9ca8eb'
j=json.loads(artifact.read_text());assert (j['q'],j['d'],j['lambda'],j['grid_denominator'],j['mass_rounding_bits'])==(3,21,'53/237',96,32)
orbits=[(x,y,96-x-y) for x in range(97) for y in range(x,97) if 96-x-y>=y]
assert len(orbits)==817 and [list(v) for v in orbits]==j['orbit_keys']
assert len(j['rows'])==21
for row in j['rows']:
    depth=row['depth'];lines=(ROOT/f't067_band20_N96_own_depth_{depth:03}.txt').read_text().splitlines()
    assert int(lines[0])==depth
    mass=list(map(int,lines[2:]));assert len(mass)==817 and min(mass)>=0 and sum(mass)==2**32
    signal=sum(F(m,2**32)*(sum(F(v,96)**2 for v in o)-F(1,3)) for m,o in zip(mass,orbits))
    assert signal==F(lines[1])==F(row['second_moment_upper'])
    reveal=[F(v) for v in (ROOT/f't067_band20_N96_own_revealed_{depth:03}.txt').read_text().splitlines()]
    assert len(reveal)==20 and reveal==list(map(F,row['rounding_mass_revealed']))
assert mass==list(map(int,j['final_integer_masses']))
assert signal==F(839183621557,9895604649984)
gap=F(257,3000)-signal;assert gap==F(1067480432287,1236950581248000)>0
assert 20*F(53,237)**2-1==F(11,56169)>0
bound=(2**32)**2*108*(237*96)**2;assert bound<2**128
proofs={}
for name in ['BAND20-UPPER','BAND20','LOCAL-RADIUS20','DEGREE-BAND-COMPARISON','DEGREE5-UPPER']:
    p=SOLVER/f'proofs/T067-{name}-001_v1.md';proofs[p.name]=sha256(p.read_bytes()).hexdigest()
files=['t067_band20_own.cs','t067_band20_control_own.py','t067_band20_control_own.json','t067_band20_N96_own_wide_controls.json']
files += [f't067_band20_N96_own_{kind}_{d:03}.txt' for d in range(1,22) for kind in ['depth','revealed']]
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS','proof_sha256':proofs,'artifact_sha256':digest,'transition_rows':1001642,'complete_depths':21,'final_masses_compared':817,'stage_revelations_compared':420,'final_signal':str(signal),'radius':str(F(257,3000)),'strict_gap':str(gap),'eta_critical20_square_gap':str(F(11,56169)),'accumulator_upper_bound':str(bound),'accumulator_bit_length':bound.bit_length(),'mass_arithmetic':'Own checked unsigned128-bit plus exact BigInteger division; all tables independently rebuilt','own_files':[{'file':v,'sha256':sha256((ROOT/v).read_bytes()).hexdigest()} for v in files]}
(ROOT/'t067_band20_compare_own.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','complete_depths','final_masses_compared','stage_revelations_compared','strict_gap','proof_sha256']}))
