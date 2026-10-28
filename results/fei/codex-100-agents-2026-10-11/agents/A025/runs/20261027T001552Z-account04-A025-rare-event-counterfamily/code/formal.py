from pathlib import Path
import subprocess, os, json, hashlib
R=Path(__file__).resolve().parents[1]
source='''import Lean.Elab.Tactic.Omega
theorem A025Cancellation :
    (forall x y s d c : Int,
      (2*x-4*y+4*s+4*d-16*c)-(2*x+2*y) = -6*y+4*s+4*d-16*c)
    /\\ ((32:Nat)^32 <= 2^7*31^31) := by
  constructor
  · intro x y s d c
    omega
  · decide
'''
(R/'code/Scalar.lean').write_text(source,encoding='utf-8')
env=os.environ.copy(); env.update(LEAN_CHECK_DIR=str(R/'out/lean'),LEAN_PEAK_LOG=str(R/'out/lean_peaks.jsonl'),LEAN_JOB_MEMORY_MB='1024',LEAN_PRIORITY='belownormal',PYTHONDONTWRITEBYTECODE='1')
cmd=[r'C:\Python314\python.exe','-B',r'lean_check.py','--file',str(R/'code/Scalar.lean'),'--target','A025Cancellation','--reviewed-sha256',hashlib.sha256(source.encode()).hexdigest(),'--core','--timeout','60','--json']
result=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(R/'out/formal_stdout.json').write_text(result.stdout,encoding='utf-8')
(R/'out/formal_stderr.txt').write_text(result.stderr,encoding='utf-8')
(R/'out/formal_result.json').write_text(json.dumps({'exit_code':result.returncode,'command':cmd,'scope':'scalar cancellation and integer boundary only; not the complete analytic proof'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exit_code':result.returncode,'scope':'scalar cancellation plus integer entropy certificate only'}))
