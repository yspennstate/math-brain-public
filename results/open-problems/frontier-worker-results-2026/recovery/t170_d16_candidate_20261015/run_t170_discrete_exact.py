from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import json,subprocess,hashlib,time,ctypes
H=Path(__file__).resolve().parent;rp=H/'T170_DISCRETE_D16_EXACT_RECEIPT.json'
assert not rp.exists(),'Completed exact receipt exists; do not redo'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
b=json.loads((H/'T170_DISCRETE_EXACT_BUILD_RECEIPT.json').read_bytes());exe=H/'t170_discrete_exact.exe';inp=H/'t170_discrete_exact_d16.txt'
assert sha(exe)==b['exe_sha256'] and sha(inp)==b['input_sha256']
log=H/'T170_DISCRETE_D16_EXACT.log';began=time.monotonic()
with log.open('wb') as out:
 p=subprocess.Popen([str(exe),str(inp)],cwd=H,stdout=out,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS)
 class Power(ctypes.Structure):_fields_=[('Version',ctypes.c_ulong),('ControlMask',ctypes.c_ulong),('StateMask',ctypes.c_ulong)]
 setting=Power(1,1,0);ctypes.windll.kernel32.SetProcessInformation(ctypes.c_void_p(int(p._handle)),4,ctypes.byref(setting),ctypes.sizeof(setting))
 code=p.wait(timeout=530)
assert code==0,'Exact run failed; read log and preserve it before any retry'
rows=[json.loads(x) for x in log.read_text(encoding='utf-8').splitlines() if x.startswith('{')]
assert [x['level'] for x in rows]==list(range(1,12)) and all(x['scale']==2**40 for x in rows)
floorfile=Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json')
assert sha(floorfile)=='e78ecf283aa59fbfd46b237bcd5dc82d52335b8ff56cf2d56ca9be347a16d7af'
floorrow=next(x for x in json.loads(floorfile.read_bytes())['rows'] if x['d']==16)['lower'];floor=F(int(floorrow['n']),int(floorrow['d']))
rounded=F(floor.numerator*10**12//floor.denominator,10**12)
axis=F(rows[-1]['raw_upper_units'],2**40*11);margin=rounded-axis
assert margin>0,'No certified crossing: preserve receipt as failure rather than claim admission'
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS exact upward-rounded candidate; NOT ADMITTED pending two independent exact-content reviews','seconds':time.monotonic()-began,'dimension':16,'axis_upper':str(axis),'diagonal_lower_rounded_down':str(rounded),'margin_exact':str(margin),'margin_float':float(margin),'rows':rows,'source_sha256':sha(H/'t170_discrete_exact.cpp'),'input_sha256':sha(inp),'exe_sha256':sha(exe),'floor_data_sha256':sha(floorfile),'build_receipt_sha256':sha(H/'T170_DISCRETE_EXACT_BUILD_RECEIPT.json'),'rate_receipt_sha256':sha(H/'T170_DISCRETE_RATE_RECEIPT.json'),'scope':'Conditional on unary-hypercube finite horizontal boundary lemma, complete caps/recurrence arithmetic, audited C004/C007 physical method and C003v2 diagonal premise. No priority/global-minimality claim.'}
rp.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
