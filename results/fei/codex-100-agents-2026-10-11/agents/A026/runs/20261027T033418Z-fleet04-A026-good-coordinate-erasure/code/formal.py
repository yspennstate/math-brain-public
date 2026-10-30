from pathlib import Path
import subprocess,sys,json,hashlib
R=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
def run(args):return subprocess.run([sys.executable,'-X','utf8',*args],capture_output=True,text=True,encoding='utf-8',errors='replace',creationflags=flags)
m=run([r'tools\memok.py'])
stmt='example (h d e0 e1 r0 r1 : Real) : h + d + ((r0 - e0) + (r1 - e1)) / 2 = h + (d - (e0 + e1) / 2) + (r0 + r1) / 2 := by ring'
p=run([r'lean_check.py','--stmt',stmt]) if m.returncode==0 else None
receipt={'memok_exit':m.returncode,'memok_stdout':m.stdout,'memok_stderr':m.stderr,'stmt':stmt,
 'lean_exit':p.returncode if p else None,'lean_stdout':p.stdout if p else None,'lean_stderr':p.stderr if p else None,
 'status':'INSPECT_WRAPPER_RECEIPT' if p and p.returncode==0 else 'UNCERTIFIED',
 'source_sha256':hashlib.sha256((R/'code/Accounting.lean').read_bytes()).hexdigest(),
 'scope':'Only single-split real algebra; no entropy, channel, inequality or FEI certification.'}
(R/'out/LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(receipt))
