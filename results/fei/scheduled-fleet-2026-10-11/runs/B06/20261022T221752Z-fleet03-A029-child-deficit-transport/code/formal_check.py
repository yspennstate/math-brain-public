"""Fresh memory admission before submitting the real-valued ledger identity."""
from pathlib import Path
import subprocess,sys,json,time
run=Path(__file__).resolve().parents[1]
stmt='example (u b j d c t : ℝ) (h : d + c + t = j) : u - b - d - c = u - b - j + t := by linarith'
begin=time.perf_counter()
admit=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8')
receipt={'statement':stmt,'scope':'Only the real-valued accounting rearrangement in equation (8), not entropy, tensorization, concavity or FEI.','memok_exit_code':admit.returncode,'memok_stdout':admit.stdout,'memok_stderr':admit.stderr,'status':'NOT_RUN_MEMORY_ADMISSION'}
if admit.returncode==0:
 cmd=[sys.executable,'-X','utf8',r'~\.claude\dreaming\lean_check.py','--stmt',stmt]
 r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
 receipt.update({'command':cmd,'wrapper_exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'status':'WRAPPER_RETURNED_INSPECT_OUTPUT_NOT_AUTOMATIC_PROOF'})
receipt['seconds']=round(time.perf_counter()-begin,6)
(run/'out/LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(receipt,ensure_ascii=False))
