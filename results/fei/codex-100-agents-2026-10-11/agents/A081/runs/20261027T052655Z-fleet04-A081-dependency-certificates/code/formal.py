from pathlib import Path
import os,subprocess,json,hashlib
R=Path(__file__).resolve().parents[1]
out=R/'out/lean';out.mkdir(parents=True,exist_ok=True)
env=dict(os.environ);env.update(TEMP=str(out),TMP=str(out),TMPDIR=str(out),LEAN_CHECK_DIR=str(out/'checks'),PYTHONDONTWRITEBYTECODE='1')
gate=subprocess.run(['python','-B','-X','utf8','tools/memok.py'],capture_output=True,text=True,encoding='utf-8',env=env,timeout=45)
(out/'MEMOK.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
status={'status':'HELD_COMPUTE_ADMISSION','memok_exit':gate.returncode,'scope':'integer rearrangement of the finite ledger only; never an entropy theorem'}
if gate.returncode==0:
 source='import Std\ntheorem ledgerCancellation (root resets loss terminal : Int) (h : terminal = root + resets - loss) : root + resets = loss + terminal := by omega\n'
 p=out/'Ledger.lean';p.write_bytes(source.encode('utf-8'));s=hashlib.sha256(p.read_bytes()).hexdigest()
 cmd=['python','-B','-X','utf8','lean_check.py','--core','--file',str(p),'--target','ledgerCancellation','--reviewed-sha256',s,'--timeout','25','--json']
 status.update(command=cmd,source_sha256=s,review='Exact Int ledger rearrangement, import Std; source contains no custom macros or execution; fidelity limited to finite accounting algebra')
 try:
  r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=45)
  (out/'CHECK_OUTPUT.txt').write_text(r.stdout+r.stderr,encoding='utf-8')
  status.update(status='VERIFIED_INTEGER_TARGET_ONLY' if r.returncode==0 else 'FORMAL_RUNTIME_OR_TARGET_UNVERIFIED',exit_code=r.returncode)
 except subprocess.TimeoutExpired as e:
  status.update(status='RUNTIME_UNVERIFIED_TIMEOUT',seconds=45)
  (out/'CHECK_OUTPUT.txt').write_text(str(e),encoding='utf-8')
(R/'out/FORMAL_STATUS.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8');print(json.dumps(status))
