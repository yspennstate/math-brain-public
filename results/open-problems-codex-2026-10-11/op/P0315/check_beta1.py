import pathlib,json,mpmath as mp
mp.mp.dps=80
p=pathlib.Path('checks.json');data=json.loads(p.read_text());rows=[]
for z in [mp.mpf(1),mp.mpf(3),mp.mpf(10),mp.mpf(100),mp.mpf(1000),100*mp.pi+mp.pi/4,1000*mp.pi+mp.pi/4]:
 s,c=mp.sin(z),mp.cos(z)
 exact=-s*s/z**2-(c/z-s/z**2)*(mp.pi/2-mp.si(z))
 first=-1/z**2+(3+mp.cos(2*z))/(2*z**4)
 approx=first+2*mp.sin(2*z)/z**5
 ratio=abs(exact-approx)*z**6/102
 assert ratio<=1
 rows.append({'z':str(z),'fraction_of_beta1_bound':str(ratio),'scaled_missing_sine_term':str((exact-first)*z**5)})
data['beta1_remainders']=rows;p.write_text(json.dumps(data,indent=2),encoding='utf8');print('beta1 remainder checks passed:',len(rows));print('missing sine limit checks:',[r['scaled_missing_sine_term'] for r in rows[-2:]])
