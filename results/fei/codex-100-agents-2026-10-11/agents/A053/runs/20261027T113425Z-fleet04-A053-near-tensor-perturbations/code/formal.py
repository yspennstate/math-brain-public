from pathlib import Path
import os,subprocess,json,hashlib,time
R=Path(__file__).resolve().parents[1];source=R/'code/PairedError.lean'
spec=dict(helper='lean_check.py --core',target='paired_error_cancel',
 source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 domain='integer counts: no-touch repair plus actual first-query derivative error; scalar cancellation ONLY',
 memory_estimate_mb=500,maximum_runtime_seconds=55,admission='memok exit0 AND fresh managed-wrapper admission; no override')
(R/'out/SPEC_LEAN.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
def run(args,timeout):
 try:
  p=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=timeout,creationflags=subprocess.CREATE_NO_WINDOW,env=env)
  return dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
 except subprocess.TimeoutExpired:return dict(exit_code=None,stdout='TIMEOUT; subprocess.run terminated its synchronous child',stderr='')
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean_receipts')
admission=run(['C:/Python314/python.exe','-B','-X','utf8','tools/memok.py'],15)
(R/'out/MEMOK.json').write_text(json.dumps(admission,indent=2)+'\n',encoding='utf-8')
if admission['exit_code']!=0:
 result=dict(exit_code=2,stdout='HELD: memok did not exit0; no compiler started',stderr='')
else:
 result=run(['C:/Python314/python.exe','-B','-X','utf8','lean_check.py',
 '--core','--file',str(source),'--target','paired_error_cancel','--reviewed-sha256',spec['source_sha256'],'--timeout','45','--json'],55)
(R/'out/LEAN_STATUS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(admission=admission,result=result)))
