from pathlib import Path
import subprocess,time
start=time.monotonic();target=str(Path('GeneralBlockCertificate.lean').resolve())
p=subprocess.run(['lake','env','lean',target],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('general_block_lean.txt').write_text('Command: lake env lean '+target+'\nTimeout: 3600 seconds\nExit: '+str(p.returncode)+'\nElapsed: '+str(time.monotonic()-start)+' seconds\n'+p.stdout+p.stderr,encoding='utf8')
print(p.returncode,p.stdout,p.stderr)
