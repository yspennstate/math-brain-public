from pathlib import Path
import subprocess,os,hashlib,json,time
R=Path(__file__).resolve().parents[1]
src=R/'code/Repair.lean'
spec=dict(helper='lean_check.py --core',target='repair_sum',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
          domain='finite lists of natural edit counts; finite-to-infinite entropy bridge NOT formalized',
          memory_estimate_mb=250,maximum_runtime_seconds=55,policy='no compiler if shared helper denies admission; no telemetry override')
(R/'out/SPEC_LEAN.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean_receipts')
p=subprocess.run(['C:/Python314/python.exe','-B','-X','utf8',
 'lean_check.py','--core','--file',str(src),
 '--target','repair_sum','--reviewed-sha256',spec['source_sha256'],'--timeout','45','--json'],
 capture_output=True,text=True,encoding='utf-8',env=env,timeout=55,creationflags=subprocess.CREATE_NO_WINDOW)
out=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
(R/'out/LEAN_ATTEMPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
