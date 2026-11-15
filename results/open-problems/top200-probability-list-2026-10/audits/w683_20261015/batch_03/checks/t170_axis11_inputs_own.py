"""Exact d17 rates, eleven Gamma terminal ceilings, and Euclidean comparison."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_t170_axis_own import gamma_units
from fractions import Fraction
from hashlib import sha256
import json

root=Path('~/brain_workers/w676/T170')
base=root/'inputs/axis6_d17_69092f0747019beb.txt'
ext=root/'inputs/axisn_exact_d17_m11_46704de27b8ab538.txt'
a=base.read_text().splitlines(); b=ext.read_text().splitlines()
assert list(map(int,b[0].split()))==[17,40,10000,11]
assert a[2]==b[2]
rates=list(map(int,b[2].split()))
assert len(rates)==10001 and rates[0]==0
for i,q in enumerate(rates[1:],1):
    assert (q-1)**16 < 32**16*i**15 <= q**16
gb=list(map(int,a[1].split())); ge=list(map(int,b[1].split()))
assert len(gb)==6 and len(ge)==6 and gb[-1]==ge[0]
expected=gb+ge[1:]
gammas=[]
for n in range(1,12):
    paths=10000 if n==2 else 1000
    value,degree=gamma_units(n,paths)
    assert value==expected[n-1],(n,value,expected[n-1])
    gammas.append({'shape':n,'paths':paths,'degree':degree,'upper_units':value})
floorpath=Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json')
assert sha256(floorpath.read_bytes()).hexdigest()=='e78ecf283aa59fbfd46b237bcd5dc82d52335b8ff56cf2d56ca9be347a16d7af'
row=next(x for x in json.loads(floorpath.read_text())['rows'] if x['d']==17)
floor=Fraction(int(row['lower']['n']),int(row['lower']['d']))
rounded=Fraction(10313992727,125000000000)
assert floor>=rounded and (floor*10**12).__floor__()==82511941816
axis=Fraction(498895329477,6047313952768)
margin=rounded-axis
assert margin==Fraction(19601449433151403,1476395008000000000000)>0
out={'rates_checked':len(rates),'gamma_boundaries':gammas,'base_sha256':sha256(base.read_bytes()).hexdigest(),'extension_sha256':sha256(ext.read_bytes()).hexdigest(),'axis':str(axis),'diagonal_floor':str(rounded),'strict_margin':str(margin),'complete':True}
Path('checks/t170_axis11_inputs_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'gamma_count':len(gammas),'rate_count':len(rates),'margin':str(margin)}))
