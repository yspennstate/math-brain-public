from fractions import Fraction as Q
from pathlib import Path
import json,time,sys
root=Path(__file__).resolve().parents[1]; start=time.perf_counter()
assert sys.float_info.radix==2 and sys.float_info.mant_dig==53
first_amp=first_empty=first_tail=None; rows=[]
for n in range(1,541):
    assert time.perf_counter()-start<55
    p=Q(1,1<<n); amplitude=1-2*p; empty=amplitude*amplitude; tail=4*p*p
    assert empty+((1<<n)-1)*tail==1
    if n>1 and float(amplitude)==1 and first_amp is None: first_amp=n
    if n>1 and float(empty)==1 and first_empty is None: first_empty=n
    if float(tail)==0 and first_tail is None: first_tail=n
    if n in (54,55,56,537,538,539,540):
        rows.append({'n':n,'amplitude_binary64_hex':float(amplitude).hex(),'empty_binary64_hex':float(empty).hex(),'nonempty_binary64_hex':float(tail).hex(),'nonempty_exact':str(tail)})
assert (first_amp,first_empty,first_tail)==(55,56,539)
n=539; p=Q(1,1<<n); I=2*n*p
missing=8*p*(1-p)*(n-1); ratio=missing/I
assert I>0 and missing>0 and ratio>Q(399,100)
result={'family':'point defect, compressed exact Boolean spectrum','smallest_n_rounded_amplitude_one':first_amp,'smallest_n_rounded_empty_mass_one':first_empty,'smallest_n_zero_nonempty_mass':first_tail,'underflow_witness':{'n':n,'I_exact':str(I),'exact_nonempty_entropy_bits':str(missing),'missing_entropy_over_I_lower_bound':str(ratio),'binary64_compressed_spectrum':'empty=1, every nonempty=0; naive H=I=0'},'selected_rows':rows,'scope':'Floating implementation diagnostic only; no flaw in the audited rational certificates','seconds':time.perf_counter()-start}
(root/'out/underflow_diagnostic.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['selected_rows','underflow_witness']},indent=2))
