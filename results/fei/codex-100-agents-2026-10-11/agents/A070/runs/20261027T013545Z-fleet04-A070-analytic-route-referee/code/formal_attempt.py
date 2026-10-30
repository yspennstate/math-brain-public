from pathlib import Path
import subprocess, json, os, time, hashlib

root=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
out=root/'out'
admission=subprocess.run(['python','-B','-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=flags,timeout=55)
(out/'memok.txt').write_text(admission.stdout+admission.stderr,encoding='utf-8',newline='\n')
receipt={'memok_exit':admission.returncode,'compiler_launched':False,'statement':'example (a b c d : Int) : (a*c-b*d)^2+(a*d+b*c)^2=(a^2+b^2)*(c^2+d^2) := by ring','scope':'Gaussian integer norm multiplication only, not Fourier entropy or FEI'}
if admission.returncode==0:
    env=dict(os.environ)
    scratch=out/'formal_scratch'
    scratch.mkdir(exist_ok=True)
    env['TEMP']=env['TMP']=str(scratch)
    env['LEAN_CHECK_DIR']=str(scratch)
    env['LEAN_JOB_MEMORY_MB']='1024'
    env['LEAN_PRIORITY']='belownormal'
    env['LEAN_PEAK_LOG']=str(out/'lean_peak.jsonl')
    source=root/'code/GaussianNorm.lean'
    source.write_text('import Mathlib.Tactic.Ring\ntheorem A070GaussianNorm (a b c d : Int) : (a*c-b*d)^2+(a*d+b*c)^2=(a^2+b^2)*(c^2+d^2) := by ring\n',encoding='utf-8',newline='\n')
    receipt['source_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
    receipt['compiler_launched']='UNVERIFIED_WRAPPER_ATTEMPT'
    try:
        proc=subprocess.run(['python','-B','-X','utf8',r'lean_check.py','--file',str(source),'--target','A070GaussianNorm','--reviewed-sha256',receipt['source_sha256'],'--timeout','45','--json'],capture_output=True,text=True,encoding='utf-8',creationflags=flags,timeout=58,env=env)
        (out/'lean_check.txt').write_text(proc.stdout+proc.stderr,encoding='utf-8',newline='\n')
        receipt['wrapper_exit']=proc.returncode
        receipt['wrapper_output']=proc.stdout+proc.stderr
        receipt['status']='SEE_WRAPPER_RECEIPT_NO_AUTOMATIC_FORMAL_ACCEPTANCE'
    except subprocess.TimeoutExpired:
        receipt['status']='WRAPPER_TIMEOUT_UNVERIFIED'
else:
    receipt['status']='HELD_NO_COMPILER_ADMISSION'
(out/'FORMAL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(receipt))
