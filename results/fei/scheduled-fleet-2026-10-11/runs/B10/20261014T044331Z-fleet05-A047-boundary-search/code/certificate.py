from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1]
rows=json.loads((R/'out/BOUNDARY.json').read_text())
row=next(x for x in rows if x['r']==6 and F(x['alpha'])==1-F(x['a'])**2)
a=F(row['a']);mu=F(row['mu']);d=F(row['query_influence'])
assert a==F(1,1024) and mu==F(1,32) and d==F(31,64)
ratio=(1-a)/a;assert ratio==1023 and 1023>2**9
lower=(1-2*a)*F(9,2);assert lower==F(4599,1024)
assert lower>8*d
out={'status':'PASS','assertions':4,'r':6,'dimension':7,'alpha':row['alpha'],'a':str(a),'removed_query_influence':str(d),'integer_log_certificate':'1023 > 2^9','strict_child_KL_lower_bound_bits':str(lower),'eight_times_removed_influence':str(8*d),'interpretation':'Child conditional KL > 8 times removed query influence; reference source KL and both actual terminal bills retained.'}
(R/'out/STRICT_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out))
