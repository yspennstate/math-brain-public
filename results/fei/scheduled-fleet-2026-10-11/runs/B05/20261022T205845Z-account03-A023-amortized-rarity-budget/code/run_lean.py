from pathlib import Path
import sys,os,subprocess,json,hashlib,io,contextlib,tempfile
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
localtmp=RUN/'out/lean_tmp';localtmp.mkdir(exist_ok=True)
os.environ['TEMP']=os.environ['TMP']=str(localtmp);tempfile.tempdir=str(localtmp)
gate=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW,timeout=30)
result={'gate_exit_code':gate.returncode,'gate_output':gate.stdout+gate.stderr,'status':'NOT_EXECUTED_RESOURCE_LIMIT','scope':'Only the tail numerator positivity sublemma is formalized; full Fourier/series theorem is an author proof.'}
if gate.returncode==0:
 sys.path.insert(0,r'~\.claude\dreaming')
 import lean_check
 # Admission happens before receipt creation/compilation; all receipt temp files stay in A023.
 buf=io.StringIO();src=RUN/'code/Tail.lean'
 with contextlib.redirect_stdout(buf),contextlib.redirect_stderr(buf):
  code=lean_check.main(['--core','--file',str(src),'--target','A023TailNumerator','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','30','--json'])
 result.update(wrapper_exit_code=code,wrapper_output=buf.getvalue(),status='VERIFIED_SCALAR_SUBLEMMA_ONLY' if code==0 else 'LEAN_UNVERIFIED')
(RUN/'out/lean_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
