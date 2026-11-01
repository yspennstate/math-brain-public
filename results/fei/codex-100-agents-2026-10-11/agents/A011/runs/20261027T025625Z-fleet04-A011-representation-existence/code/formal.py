from pathlib import Path
import subprocess,hashlib,json,sys,time
R=Path(__file__).resolve().parents[1]
src='''import Mathlib.Tactic.Linarith

theorem a011_physical_ledger_step (dparent dinherited dchild reset qloss : Real)
    (hq : qloss = dparent - dinherited)
    (hr : reset = dchild - dinherited) :
    dchild = dparent + reset - qloss := by
  linarith
'''
p=R/'code/Ledger.lean';p.write_text(src,encoding='utf-8')
sha=hashlib.sha256(p.read_bytes()).hexdigest()
helper=Path(r'lean_check.py')
cmd=[sys.executable,'-B','-X','utf8',str(helper),'--file',str(p),'--target','a011_physical_ledger_step','--reviewed-sha256',sha,'--timeout','35','--json']
gate=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
ans={'source_sha256':sha,'review':'Caller inspected only the displayed safe Mathlib import and named linarith theorem. This is algebraic node conservation, not a formalization of entropy or the all-dimensional theorem.','command':cmd,'admission_exit':gate.returncode,'admission_stdout':gate.stdout,'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest()}
if gate.returncode==0:
 t=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
 ans.update(exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,wall_seconds=time.monotonic()-t)
else:ans['status']='HELD_MEMORY_ADMISSION_NO_COMPILER_STARTED'
(R/'out/LEAN_RECEIPT.json').write_text(json.dumps(ans,indent=2),encoding='utf-8')
print(json.dumps(ans)[:4500])
