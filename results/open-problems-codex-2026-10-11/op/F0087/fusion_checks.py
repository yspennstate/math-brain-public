import pathlib,json,cmath,math
from fractions import Fraction
P=pathlib.Path(__file__).parent
src=(P/'finite_checks.py').read_text(encoding='utf-8-sig').split('out=[];start=time.time()')[0]
exec(compile(src,'finite_checks.py definitions','exec'))
W,H=4,6
hs=[heights(M,W,H) for M in matchings(W,H)]
f,g=(1,1),(3,5)
rows=[]
for s in [Fraction(1,4),Fraction(1,3),Fraction(1,5),Fraction(2,5),Fraction(-1,4)]:
 n=s.denominator;values=[cmath.exp(2j*math.pi*float(n*s)*((h[f]-h[g])/4)) for h in hs]
 avg=sum(values)/len(values);err=max(abs(v-values[0]) for v in values)
 assert err<1e-12 and abs(abs(avg)-1)<1e-12
 seq=[{'N':N,'fusion_amplitude_a_s_equal_1':N**float(2*n*s*s),'matching_majorant_upper_bound':math.factorial(n)*2**float(2*n*s*s)} for N in [16,256,4096,65536]]
 rows.append({'s':str(s),'n':n,'tilings':len(hs),'fused_charge':str(n*s),'fused_characteristic_modulus':abs(avg),'maximum_phase_discrepancy':err,'illustrative_scaling':seq})
res={'scope':'Exact rational fusion identity checked on all 281 tilings of 4x6; scaling rows use a_s=1, not the unknown lattice normalization. Infinite-volume contradiction is proved separately.','results':rows}
(P/'fusion_checks.json').write_text(json.dumps(res,indent=2),encoding='utf8')
for r in rows:print(r['s'],r['n'],r['fused_characteristic_modulus'],r['maximum_phase_discrepancy'])
