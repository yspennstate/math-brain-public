import json
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]
x=json.loads((R/'out/neutral_query_controls.json').read_text())
for row in x['rows']:
 for name in ['remaining_margin','margin_after_all_actual_decrements']:
  assert F(row[name]['lower'])>F(1,2)
 if row['class']=='active':assert 0<F(row['signed_new_debit']['lower'])<=F(row['signed_new_debit']['upper'])<F(1,1000000)
 else:assert F(-2,1000)<F(row['signed_new_debit']['lower'])<=F(row['signed_new_debit']['upper'])<0
 assert 0<F(row['remaining_actual_encoder_correction']['lower'])<=F(row['remaining_actual_encoder_correction']['upper'])<F(51,1000)
 for name in ['original_bank_S4','original_booked_margin']:
  assert row[name]==x['rows'][0][name]
certificate={'status':'PASS','same_original_bank_and_debit_for_each_alternative':True,'all_retained_and_full_margins_greater_than':'1/2','active_incremental_debit_interval':['0','1/1000000'],'dummy_incremental_debit_interval':['-2/1000','0'],'actual_future_encoder_correction_interval':['0','51/1000'],'arithmetic':'Comparison of saved outward rational endpoints only; diagnostic decimals not used.'}
(R/'out/readback_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n',encoding='utf-8');print(json.dumps(certificate))
