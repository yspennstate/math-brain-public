from pathlib import Path
import subprocess,shutil,json,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();lake=shutil.which('lake');receipt={'target':'count_ratio only, not complete theorem','admission':'memok exited 0: physical free 4.6GB, commit free20.1GB','formal_target_verified':False}
if not lake:receipt.update(status='SETUP_UNVERIFIED',reason='lake not found')
else:
 cmd=[lake,'env','lean',str(B/'code/CountPayment.lean')];receipt['command']=cmd
 p=subprocess.Popen(cmd,cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
 try:
  out,_=p.communicate(timeout=45);receipt.update(exit_code=p.returncode,output=out.decode('utf-8',errors='replace')[:12000],status='COUNT_LEMMA_COMPILED' if p.returncode==0 else 'SETUP_OR_COMPILATION_UNVERIFIED',formal_target_verified=p.returncode==0)
 except subprocess.TimeoutExpired:
  subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
  out,_=p.communicate();receipt.update(status='RUNTIME_UNVERIFIED',output=out.decode('utf-8',errors='replace')[:12000])
receipt['seconds']=time.monotonic()-start
(B/'out/LEAN.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(receipt))
