from pathlib import Path
import hashlib,json,subprocess,sys,time
r=Path(__file__).resolve().parents[1]
check=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=55)
record={'scope':'Core Lean integer-scaled original-book combination and continuation ONLY, not the Fourier/KL theorem','memok_exit':check.returncode,'memok_output':check.stdout+check.stderr,'estimated_core_memory_MB':200,'mathlib_excluded':'documented ~4GB compilation exceeds user1.5GB ceiling'}
if check.returncode==0:
 f=r/'code/ledger.lean';digest=hashlib.sha256(f.read_bytes()).hexdigest()
 cmd=[sys.executable,'-X','utf8',r'~\.claude\dreaming\lean_check.py','--file',str(f),'--core','--target','successive_original_book','--reviewed-sha256',digest,'--timeout','45','--json']
 record.update(command=cmd,source_sha256=digest)
 try:
  result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=55)
  record.update(exit_code=result.returncode,stdout=result.stdout,stderr=result.stderr)
 except subprocess.TimeoutExpired as e:
  record.update(status='RUNTIME_UNVERIFIED',stdout=(e.stdout or b'').decode('utf-8',errors='replace') if isinstance(e.stdout,bytes) else e.stdout,reason='wrapper exceeded55second bound; no mathematical certificate')
else:record.update(status='COMPUTE_ADMISSION_HELD')
(r/'out/LEAN_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k not in ['stdout','stderr','command']},indent=2))
