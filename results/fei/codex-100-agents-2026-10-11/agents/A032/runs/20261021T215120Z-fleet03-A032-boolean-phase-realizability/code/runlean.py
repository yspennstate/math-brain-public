from pathlib import Path
import sys, subprocess, os, hashlib, json, time
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', LEAN_CHECK_DIR=str(R/'out/lean'))
admit=subprocess.run([sys.executable,'-B','-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',env=env,creationflags=0x08000000)
(R/'out/memok.txt').write_text(admit.stdout+admit.stderr,encoding='utf-8')
if admit.returncode:
    (R/'out/lean_attempt.json').write_text(json.dumps({'status':'ADMISSION_HELD','exit':admit.returncode}),encoding='utf-8')
    print('Lean admission held');sys.exit(0)
src=R/'code/Core.lean';sha=hashlib.sha256(src.read_bytes()).hexdigest()
cmd=[sys.executable,'-B','-X','utf8',r'lean_check.py','--file',str(src),'--target','A032_exact_power_guards','--reviewed-sha256',sha,'--core','--timeout','45','--json']
t=time.monotonic()
try:
    p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,creationflags=0x08000000,timeout=100)
    output=p.stdout+p.stderr
    result={'exit':p.returncode,'seconds':time.monotonic()-t,'source_sha256':sha,'command':cmd}
except subprocess.TimeoutExpired as ex:
    output=str(ex);result={'status':'OUTER_TIMEOUT_UNVERIFIED','seconds':time.monotonic()-t,'source_sha256':sha,'command':cmd}
(R/'out/lean_output.txt').write_text(output,encoding='utf-8')
(R/'out/lean_attempt.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
