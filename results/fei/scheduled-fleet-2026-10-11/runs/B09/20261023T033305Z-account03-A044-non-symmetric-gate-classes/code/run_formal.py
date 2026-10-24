from pathlib import Path
import subprocess,json,hashlib,sys
R=Path(__file__).resolve().parents[1]
p=R/'code/terminal_core.lean'
cmd=[sys.executable,'-X','utf8',r'~\.claude\dreaming\lean_check.py','--core','--file',str(p),'--target','A044_two_level_terminal','--reviewed-sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'--timeout','45','--json']
result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=60)
record={'command':cmd,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'scope':'Only the named Nat finite ledger cancellation; no formal certification of real entropy or Fourier composition.','memok_prior_exit_code':0,'memok_prior_output':'OK: physical free7.2GB;commit free21.2GB','core_only_estimated_memory_mb':150}
(R/'out/FORMAL_CHECK.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exit_code':result.returncode,'output':result.stdout[-1600:],'stderr':result.stderr[-500:]}))
