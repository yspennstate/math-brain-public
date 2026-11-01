from pathlib import Path
import subprocess,hashlib,json,sys
root=Path(__file__).resolve().parents[1];src=root/'code/Deficit.lean'
admit=[sys.executable,'-X','utf8',r'tools/memok.py']
a=subprocess.run(admit,capture_output=True,text=True,encoding='utf-8')
out=dict(memok_command=admit,memok_exit_code=a.returncode,memok_stdout=a.stdout,memok_stderr=a.stderr)
if a.returncode==0:
 cmd=[sys.executable,'-X','utf8',r'lean_check.py','--file',str(src),'--target','odd_face_deficit','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','45','--json']
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
 out.update(command=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
else:out.update(exit_code=2,stdout='MEMOK_HELD; no compiler started',stderr='')
(root/'out/FORMAL.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
