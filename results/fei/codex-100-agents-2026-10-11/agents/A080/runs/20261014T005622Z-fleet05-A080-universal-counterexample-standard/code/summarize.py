from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))
records=data['records'];core=records[3];children=records[4:]
K=F(669,200)
assert F(core['minority'])<F(1,16)
assert F(core['E_interval'][0])>K
assert all(F(x['E_interval'][1])<K for x in children)
assert all(F(x['detail']['reserve'][1])<0 for x in children)
def bracket(vals):
 lo,hi=map(F,vals);D=10**9
 return [str(F((lo*D).__floor__(),D)),str(F((hi*D).__ceil__(),D))]
compact=[]
for x in records:
 compact.append({'label':x['detail']['label'],'physical_bits':x['state']['n'],'minority_probability_exact':x['minority'],'minority_probability_display':x['display']['minority'],'E_rational_bracket':bracket(x['E_interval']),'H_over_I_rational_bracket':bracket(x['H_over_I_interval']),'chosen_bias_exact':x['detail'].get('chosen_p'),'reserve_rational_bracket':bracket(x['detail']['reserve']) if 'reserve' in x['detail'] else None,'terminal_Cp_rational_bracket':bracket(x['detail']['terminal_Cp']) if 'terminal_Cp' in x['detail'] else None})
out={'status':'PASS','threshold':str(K),'assertions':5,'input_assertions':data['assertions'],'runtime_seconds':data['runtime_seconds'],'actual_core':'g0=h; g1=h(g0^6); g2=h((-g1)^6); g3=h(g2^6), with disjoint copies','result':'E(g3)>669/200, p_min(g3)<1/16, but E(h(g3^6)) and E(h((-g3)^6)) both <669/200','records':compact,'scope':'Finite exact admission obstruction and all-depth bias absorption; no FEI disproof'}
(R/'out/CERTIFICATE_SUMMARY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','threshold':str(K),'E_brackets':[(x['physical_bits'],x['E_rational_bracket']) for x in compact],'H_over_I_brackets':[(x['physical_bits'],x['H_over_I_rational_bracket']) for x in compact]},indent=2))
