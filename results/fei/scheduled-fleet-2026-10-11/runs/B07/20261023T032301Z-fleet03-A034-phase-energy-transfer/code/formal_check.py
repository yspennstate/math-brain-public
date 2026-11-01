from pathlib import Path
import sys,subprocess,json,hashlib,os
RUN=Path(__file__).resolve().parents[1];sys.dont_write_bytecode=True
admit=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=30)
receipt={'memok_exit':admit.returncode,'memok_output':admit.stdout+admit.stderr,'formal_status':'RUNTIME_UNVERIFIED','compiler_launched':False}
if admit.returncode==0:
 sys.path.insert(0,r'~\.claude\dreaming')
 import lean_check
 data=(RUN/'code'/'PlaneFiber.lean').read_bytes()
 try:
  result=lean_check.check_source(data,target='A034_column_fibers',reviewed_sha256=hashlib.sha256(data).hexdigest(),timeout=45,output_root=RUN/'out'/'lean',use_mathlib=False)
  receipt['lean']=result;receipt['formal_status']=result['result']['status'];receipt['compiler_launched']=True
 except (RuntimeError,ValueError,OSError) as exc:receipt['reason']=str(exc)
else:receipt['reason']='memok held new compiler work; no compiler started'
(RUN/'out'/'lean_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
