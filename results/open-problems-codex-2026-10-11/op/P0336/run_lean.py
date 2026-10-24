import subprocess,pathlib,time
p=pathlib.Path('~/brain_workers/TRIO_1011/op/P0336')
t=time.time()
r=subprocess.run(['lake','env','lean',str(p/'P0336Checks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
(p/'lean_check.txt').write_text('Exit code: '+str(r.returncode)+'\nElapsed: '+str(time.time()-t)+'\n'+r.stdout+r.stderr,encoding='utf8')
print((p/'lean_check.txt').read_text())
