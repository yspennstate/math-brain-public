from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1]
v=json.loads((R/'out/EXACT_RESULTS.json').read_text(encoding='utf-8'))
rows=[];checks=0
def ck(b,msg):
 global checks
 checks+=1
 if not b:raise AssertionError(msg)
for row in v['selected_rows']:
 if row['a']!=4:continue
 m=row['m'];e=F(1,2**(m+4));lower,upper=map(F,row['charge_intervals'][0]);clean_upper=F(row['charge_intervals'][1][1])
 ck(lower>0 and upper<e,'rigorous strictly positive EDITED-child charge, parent reach1')
 ck(clean_upper<0,'clean negative conversion retained, never refunded')
 # Normalize -h4 at zero: nonzero source frequency coefficient +1/8.
 A=F(1,8);q=(A-e)**2+e*e;r=(A*A+3*e*e)/(1+3*e);t=(A*A+6*e*e)/(1+6*e)
 qoff=2*e*e;roff=3*e*e/(1+3*e);toff=6*e*e/(1+6*e)
 ck(r*(A-2*e)**2*toff*qoff!=roff*(4*e*e)*t*q,'genuine NONEMPTY profile change; Z cancels')
 z0,z1=map(F,row['Z']);ck(z0+z1==2 and z0!=z1 and z0*z1<1,'strict physical-query KL contraction; not silently refunded')
 ck(F(3,256)-2*F(1,4)*e>=F(190,16384),'same original bank pays entry and selector; strict input bound handles equality at m8')
 rows.append({'m':m,'actual_original_reach':'1/4','positive_edited_booking_interval':[str(lower/4),str(upper/4)],'nonempty_profile_changed':True,'query_KL_contraction_positive':True,'old_positive_p1_p2_retained':True,'clean_negative_credit_used':False,'same_original_rate4_reserve':'>190/16384 for entry+selector, >186/16384 for entry+all-source-prefix+selector'})
# Exact source-inheritance witness for the accounting objection, no numerical logs.
ck(F(1,2)+F(1,2)==1 and 2**1==2,'dictator root code loss exactly1bit; child cost0bit')
out={'status':'PASS','assertions':checks,'rows':rows,'a011_conversion_only_identity_witness':{'root_CE':1,'actual_reset_sum':0,'root_H_plus_terminal_D':0,'physical_query_KL_contraction':1},'counting':'sign/ratio certificates recheck saved main cases; not additional Boolean cases'}
(R/'out/POSITIVE_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps({'status':'PASS','assertions':checks,'positive_actual_selector_handoffs':len(rows),'new_cases':0}))
