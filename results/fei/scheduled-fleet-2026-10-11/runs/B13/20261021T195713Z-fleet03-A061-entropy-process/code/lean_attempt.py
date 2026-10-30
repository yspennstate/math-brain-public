from pathlib import Path
import subprocess,sys,hashlib,json,time
R=Path(__file__).resolve().parents[1];p=R/'code/QuarterBank.lean';sha=hashlib.sha256(p.read_bytes()).hexdigest()
cmd=[sys.executable,'-X','utf8',r'~/.claude/dreaming/lean_check.py','--file',str(p),'--core','--target','quarter_bank_scaled','--reviewed-sha256',sha,'--timeout','45','--json']
t=time.perf_counter();r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
(R/'out/LEAN_STDOUT.txt').write_text(r.stdout,encoding='utf-8');(R/'out/LEAN_STDERR.txt').write_text(r.stderr,encoding='utf-8')
result=dict(returncode=r.returncode,source_sha256=sha,seconds=time.perf_counter()-t,command=cmd,scope='integer-scaled quarter-bank sufficient condition only')
(R/'out/LEAN_ATTEMPT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
