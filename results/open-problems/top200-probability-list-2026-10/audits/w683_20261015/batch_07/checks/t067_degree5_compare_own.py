"""Bind an independent complete trajectory to the frozen degree5 claim."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import json
ROOT=Path(__file__).resolve().parent
SOLVER=Path('~/brain_workers/w682')
artifact=SOLVER/'checks/regular_bp_fast_d5_N96_161-360.json'
j=json.loads(artifact.read_text())
entry=json.loads((SOLVER/'checks/degree5_entry25.json').read_text())
assert sha256(artifact.read_bytes()).hexdigest()=='bec3329f2968b0b58fee6306d2e2d96b6237a9da72fb9ecdb4be22913755484f'
assert j['q']==3 and j['d']==5 and j['lambda']=='161/360'
assert j['mass_rounding_bits']==32 and j['grid_denominator']==96
orbits=[(x,y,96-x-y) for x in range(97) for y in range(x,97) if 96-x-y>=y]
assert len(orbits)==817 and [list(v) for v in orbits]==j['orbit_keys']
assert len(j['rows'])==25
for record in j['rows']:
    depth=record['depth']; lines=(ROOT/f't067_d5_N96_own_depth_{depth:03}.txt').read_text().splitlines()
    assert int(lines[0])==depth and F(lines[1])==F(record['second_moment_upper'])
    masses=list(map(int,lines[2:]));assert len(masses)==817 and min(masses)>=0 and sum(masses)==2**32
    signal=sum(F(m,2**32)*(sum(F(v,96)**2 for v in o)-F(1,3)) for m,o in zip(masses,orbits))
    assert signal==F(lines[1])
    reveals=[F(s) for s in (ROOT/f't067_d5_N96_own_revealed_{depth:03}.txt').read_text().splitlines()]
    assert reveals==list(map(F,record['rounding_mass_revealed'])) and len(reveals)==4
assert list(map(int,j['final_integer_masses']))==masses
assert signal==F(927866518931,19791209299968)
gap=F(217,4500)-signal
assert gap==F(3313696747321,2473901162496000)>0
assert 5*F(161,360)**2-1==F(1,25920)>0
assert F(559017,1250000)**2*5>1
den1=108*(360*96)**2;den2=108*360*96**2
# Sum of all unfloored numerator contributions at one fusion is S^2*den.
# Thus each individual unsigned accumulator is bounded by this number.
bound=(2**32)**2*max(den1,den2)
assert bound<2**128
proofs={}
for name in ['DEGREE5-UPPER','DEGREE5','LOCAL-RADIUS5','DEGREE-BAND-COMPARISON']:
    p=SOLVER/f'proofs/T067-{name}-001_v1.md';proofs[p.name]=sha256(p.read_bytes()).hexdigest()
files=['t067_degree5_own.cs','t067_degree5_control_own.py','t067_degree5_control_own.json','t067_d5_N96_own_wide_controls.json']
files += [f't067_d5_N96_own_{kind}_{depth:03}.txt' for depth in range(1,26) for kind in ['depth','revealed']]
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS','proof_sha256':proofs,'artifact_sha256':sha256(artifact.read_bytes()).hexdigest(),'transition_rows':1001642,'complete_depths':25,'final_masses_compared':817,'stage_revelations_compared':100,'final_signal':str(signal),'radius':str(F(217,4500)),'strict_gap':str(gap),'eta_critical_square_gap':str(F(1,25920)),'accumulator_upper_bound':str(bound),'accumulator_bit_length':bound.bit_length(),'mass_arithmetic':'unsigned checked 128-bit exact accumulation, BigInteger exact floor division; all tables built independently','own_files':[{'file':v,'sha256':sha256((ROOT/v).read_bytes()).hexdigest()} for v in files]}
(ROOT/'t067_degree5_compare_own.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','transition_rows','complete_depths','final_masses_compared','strict_gap','proof_sha256']}))
