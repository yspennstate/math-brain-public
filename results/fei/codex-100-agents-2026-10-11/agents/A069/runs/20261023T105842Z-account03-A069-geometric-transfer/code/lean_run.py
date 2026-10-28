from pathlib import Path
import os,sys,subprocess,json,hashlib
RUN=Path(__file__).resolve().parents[1]
gate=subprocess.run([sys.executable,'-B','-X','utf8',r'tools/memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(RUN/'out/MEMOK.json').write_text(json.dumps({'returncode':gate.returncode,'stdout':gate.stdout,'stderr':gate.stderr},indent=2)+'\n',encoding='utf-8')
src=RUN/'code/BooleanPair.lean';source_sha256=hashlib.sha256(src.read_bytes()).hexdigest()
if gate.returncode:
 result={'status':'NOT_RUN_ADMISSION_HELD','reason':'memok nonzero; no compiler/helper started','source_sha256':source_sha256,'stdout':gate.stdout}
else:
 env=dict(os.environ);env['LEAN_CHECK_DIR']=str(RUN/'out/lean')
 cmd=[sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(src),'--target','boolean_pair_identity','--reviewed-sha256',source_sha256,'--timeout','20','--json']
 p=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
 result={'status':'HELPER_RETURNED','returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'source_sha256':source_sha256}
(RUN/'out/LEAN_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result)[:6000])
