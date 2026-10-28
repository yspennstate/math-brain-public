from pathlib import Path
import subprocess,os,hashlib,json,sys
R=Path(__file__).resolve().parents[1];out=R/'out';tmp=out/'lean_tmp';tmp.mkdir(exist_ok=True)
mem=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8')
(out/'FORMAL_ADMISSION.json').write_text(json.dumps({'returncode':mem.returncode,'stdout':mem.stdout,'stderr':mem.stderr},indent=2),encoding='utf-8')
if mem.returncode:
 print('FORMAL NOT STARTED: fresh memok refused');sys.exit(0)
env=os.environ.copy();env.update({'TEMP':str(tmp),'TMP':str(tmp),'LEAN_JOB_MEMORY_MB':'1024','LEAN_PEAK_LOG':str(out/'LEAN_PEAKS.jsonl')})
p=R/'code/MaxDrift.lean';digest=hashlib.sha256(p.read_bytes()).hexdigest()
cmd=[sys.executable,'-X','utf8',r'lean_check.py','--core','--file',str(p),'--target','a061_scaled_max','--reviewed-sha256',digest,'--timeout','55','--json']
proc=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=100)
(out/'FORMAL.json').write_text(json.dumps({'returncode':proc.returncode,'source_sha256':digest,'stdout':proc.stdout,'stderr':proc.stderr,'scope':'Nat scaled maximum inequality only; no full entropy or stopping formalization'},indent=2),encoding='utf-8')
print('FORMAL',proc.returncode,proc.stdout[-3500:])
