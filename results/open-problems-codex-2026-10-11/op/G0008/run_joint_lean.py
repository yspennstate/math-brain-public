from pathlib import Path
import subprocess,time
start=time.time()
r=subprocess.run(['lake','env','lean','~/brain_workers/TRIO_1011/op/G0008/JointCertificate.lean'],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('joint_lean_check.log').write_text(r.stdout+r.stderr+f"\nEXIT_CODE={r.returncode}\nSECONDS={time.time()-start:.2f}\n",encoding='utf8');print(r.stdout,r.stderr,'EXIT',r.returncode)
