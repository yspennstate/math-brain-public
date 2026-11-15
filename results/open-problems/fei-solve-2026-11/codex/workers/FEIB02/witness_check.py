import json,mpmath as mp
from symmetric import evaluate
from audit import direct_truth
mp.mp.dps=100
v=evaluate([1,1,1,-1],100)
d=direct_truth([1,1,1,1,1,1,1,-1],3)
c=json.load(open('census_03.json'))['maxima']['B/I']['value']
manual=mp.mpf(15)/4-mp.mpf(3)/2*mp.log(3,2)
print('C census',c)
print('finite differences',mp.nstr(v['B/I'],80))
print('direct truth table',d['B']/d['I'])
print('closed form 15/4-(3/2)log2(3)',mp.nstr(manual,80))
assert abs(manual-v['B/I'])<mp.mpf('1e-90')
assert abs(float(manual)-d['B']/d['I'])<1e-14
