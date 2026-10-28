"""Exact integer-power sign certificate for the closed-form drift."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
w=json.loads((R/'out/INDEPENDENT_AUDIT.json').read_text(encoding='utf-8'))
expected={'2':'-37/16','3':'-567/512','5':'-25/1024','7':'3087/2048'}
assert w['drift']==expected
tests=[('positive_drift',7**3087,2**4736*3**2268*5**50),
 ('parent_C_positive',2**14592,3**2862*7**3087),
 ('child0_C_positive',2**3392,3**1701*5**25),
 ('child1_C_positive',2**48,3**27),
 ('AND3_rate3_slack_positive',3**9,2**14)]
rows=[]
for name,lhs,rhs in tests:
 assert lhs>rhs
 rows.append({'name':name,'comparison':'lhs>rhs','lhs_bits':lhs.bit_length(),'rhs_bits':rhs.bit_length(),'lhs_sha256':hashlib.sha256(lhs.to_bytes((lhs.bit_length()+7)//8,'big')).hexdigest(),'rhs_sha256':hashlib.sha256(rhs.to_bytes((rhs.bit_length()+7)//8,'big')).hexdigest()})
out={'formula':'2048*drift=3087log2(7)-4736-2268log2(3)-50log2(5)',
'inequality':'7^3087 > 2^4736 * 3^2268 * 5^50',
'comparisons':rows,'all_K_ge_3':'Every AND_m restriction for m<=3 has H<=3I; AND3 uses3^9>2^14, AND2 H2=2,I2=1, smaller H0. Thus all inner hulls vanish for every real K>=3 and the SAME strict drift remains.',
'seconds':time.perf_counter()-start,'full_fei':'OPEN'}
(R/'out/INTEGER_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_integer_comparisons':len(rows),'drift_positive':True,'rate_scope':'all real K>=3','seconds':out['seconds']}))
