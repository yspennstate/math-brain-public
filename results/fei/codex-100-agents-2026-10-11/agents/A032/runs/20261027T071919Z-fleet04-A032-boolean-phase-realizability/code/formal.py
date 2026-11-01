from pathlib import Path
import json,subprocess,os,sys
ROOT=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
gate=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=flags)
(ROOT/'out/memok.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
if gate.returncode:
 (ROOT/'out/formal.txt').write_text('HELD: memok exit1; no compiler started\n',encoding='utf-8');sys.exit(0)
d=json.loads((ROOT/'out/validation.json').read_text(encoding='utf-8'))
entries=d['ordered_cones'][0]+d['ordered_cones'][1]
stmt='theorem coneCertificate : (['+','.join(entries)+'] : List Int).all (fun z => decide (0 <= z)) = true := by decide\n'
(ROOT/'code/Cone.lean').write_text(stmt,encoding='utf-8')
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(ROOT/'out/lean')
result=subprocess.run([sys.executable,'-X','utf8',r'lean_check.py','--file',str(ROOT/'code/Cone.lean'),'--target','coneCertificate','--core','--timeout','45','--json'],env=env,capture_output=True,text=True,encoding='utf-8',creationflags=flags)
(ROOT/'out/formal.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
print(json.dumps({'formal_wrapper_exit':result.returncode,'receipt':'out/formal.txt'}))
