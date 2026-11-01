from pathlib import Path
import subprocess,sys,json,hashlib,time
R=Path(__file__).resolve().parents[1]
gate=subprocess.run([sys.executable,'-X','utf8','tools/memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=35)
out={'estimated_memory_mb':450,'max_runtime_seconds':45,'memok_exit':gate.returncode,'memok_stdout':gate.stdout,'memok_stderr':gate.stderr}
if gate.returncode==0:
    source=R/'code/anchor.lean';digest=hashlib.sha256(source.read_bytes()).hexdigest()
    cmd=[sys.executable,'-X','utf8','lean_check.py','--file',str(source),'--target','A048_bank_drop','--reviewed-sha256',digest,'--timeout','30','--json']
    try:
        r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=45)
        out.update(status='VERIFIED_TARGET' if r.returncode==0 else 'UNVERIFIED',exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,source_sha256=digest)
    except subprocess.TimeoutExpired:out.update(status='UNVERIFIED_TIMEOUT')
else:out.update(status='ADMISSION_HELD_NO_COMPILER_STARTED')
(R/'out/LEAN.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['stdout','stderr','memok_stdout','memok_stderr']}))
