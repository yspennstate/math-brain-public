from pathlib import Path
import subprocess,os,hashlib,json,time
R=Path(__file__).resolve().parents[1]
src=b'import Std.Tactic\n\ntheorem a027_ledger (raw terminal loss : Int) (h : raw = terminal + loss) : raw - terminal = loss := by omega\n'
p=R/'code/Ledger.lean';p.write_bytes(src)
spec={'family':'integer algebra for exact query-ledger cancellation only','helper_version':'code/formal.py v1','case_count':1,'arithmetic':'Lean core plus Std.Tactic; no Mathlib','memory_estimate_mb':250,'max_runtime_seconds':55,'compiler_timeout_seconds':25,'source_sha256':hashlib.sha256(src).hexdigest(),'scope':'does NOT formalize entropy, channels, Fourier realizability or full theorem'}
(R/'FROZEN_FORMAL.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean')
cmd=['C:/Python314/python.exe','-B','lean_check.py','--file',str(p),'--core','--target','a027_ledger','--reviewed-sha256',spec['source_sha256'],'--timeout','25','--json']
start=time.monotonic()
try:
    v=subprocess.run(cmd,env=env,cwd=R,encoding='utf-8',capture_output=True,timeout=55,creationflags=subprocess.CREATE_NO_WINDOW)
    out={'returncode':v.returncode,'stdout':v.stdout,'stderr':v.stderr,'elapsed_seconds':time.monotonic()-start,'translation':'integer cancellation ONLY; prose entropy theorem not Lean-certified','command':cmd}
except subprocess.TimeoutExpired as e:out={'status':'WRAPPER_TIMEOUT_UNVERIFIED','elapsed_seconds':time.monotonic()-start,'translation':'no proof certification'}
(R/'out/LEAN_RECEIPT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out)[:1200])
