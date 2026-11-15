from pathlib import Path
from datetime import datetime
import sys,json,subprocess,hashlib,time,ctypes
H=Path(__file__).resolve().parent
mode=sys.argv[1];assert mode in ['control17','new16']
receipt=H/('T170_SCREEN_'+mode+'_RECEIPT.json');assert not receipt.exists(),'Already completed; inspect receipt'
exe=H/'t170_discrete_screen.exe';build=json.loads((H/'T170_DISCRETE_DIRECT_BUILD_RECEIPT.json').read_bytes())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(exe)==build['exe_sha256']
if mode=='new16':assert json.loads((H/'T170_SCREEN_control17_RECEIPT.json').read_bytes())['control_pass']
inputfile=H/('t170_control_d17.txt' if mode=='control17' else 't170_discrete_d16.txt')
log=H/('T170_SCREEN_'+mode+'.log');started=time.monotonic()
with log.open('wb') as out:
 p=subprocess.Popen([str(exe),str(inputfile)],cwd=H,stdout=out,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS)
 class Power(ctypes.Structure):_fields_=[('Version',ctypes.c_ulong),('ControlMask',ctypes.c_ulong),('StateMask',ctypes.c_ulong)]
 setting=Power(1,1,0);ctypes.windll.kernel32.SetProcessInformation(ctypes.c_void_p(int(p._handle)),4,ctypes.byref(setting),ctypes.sizeof(setting))
 code=p.wait(timeout=290)
assert code==0,'Inspect numeric screen log, do not silently retry'
rows=[json.loads(x) for x in log.read_text(encoding='utf-8').splitlines() if x.startswith('{')]
assert [x['level'] for x in rows]==list(range(1,12))
out={'at':datetime.now().astimezone().isoformat(),'status':'SCREEN ONLY; double precision is not a rigorous certificate','mode':mode,'seconds':time.monotonic()-started,'input_sha256':sha(inputfile),'exe_sha256':sha(exe),'rows':rows}
if mode=='control17':
 old=json.loads(Path('~/brain_workers/w683/checks/t170_c012_binding_own.json').read_bytes())
 errors=[abs(row['normalized_upper']-unit/2**40/(i+1)) for i,(row,unit) in enumerate(zip(rows,old['own_roots']))]
 assert max(errors)<1e-7,(max(errors),'Profile/control assembly wrong')
 out.update(control_pass=True,max_control_error=max(errors))
else:
 floorfile=Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json')
 floor=next(x for x in json.loads(floorfile.read_bytes())['rows'] if x['d']==16)['lower']
 diagonal=int(floor['n'])/int(floor['d']);out.update(diagonal_floor_screen=diagonal,screen_margin=diagonal-rows[-1]['normalized_upper'])
receipt.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
