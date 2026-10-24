from pathlib import Path
import sys,subprocess,json,hashlib,time
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1];t=time.perf_counter()
cmd=[sys.executable,'-X','utf8','~/brain_workers/FEI100_20261011/tools/memok.py']
gate=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0),timeout=30)
out={'gate_exit':gate.returncode,'gate_output':gate.stdout+gate.stderr,'status':'HELD_NO_COMPUTE_ADMISSION','compiler_started':False}
if gate.returncode==0:
 sys.path.insert(0,'~/.claude/dreaming')
 import lean_check
 p=R/'code/FluxBudget.lean';raw=p.read_bytes()
 try:
  receipt=lean_check.check_source(raw,source_path=p,output_root=R/'out/lean',use_mathlib=False,target='fluxBudget',reviewed_sha256=hashlib.sha256(raw).hexdigest(),timeout=20)
  out.update(status=receipt['result']['status'],receipt=receipt)
 except RuntimeError as e:out['reason']=str(e)
out['seconds']=time.perf_counter()-t
(R/'out/LEAN_ADMISSION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_exit':gate.returncode,'seconds':out['seconds']}))
