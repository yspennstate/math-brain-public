from pathlib import Path
import subprocess,hashlib,json,sys
root=Path(__file__).resolve().parents[1];src=root/'code/Bank.lean'
cmd=[sys.executable,'-X','utf8',r'lean_check.py','--file',str(src),'--target','interaction_bank_drop','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','45','--json']
p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
out=dict(command=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
(root/'out/FORMAL.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
