import subprocess,pathlib,time
cmd=['lake','env','lean',str(pathlib.Path('FiniteSwitch.lean').resolve())]
t=time.time()
r=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
pathlib.Path('lean_check.txt').write_text('Command: '+' '.join(cmd)+'\nElapsed: '+str(time.time()-t)+'\nExit: '+str(r.returncode)+'\n'+r.stdout+r.stderr,encoding='utf8')
print(r.returncode,r.stdout,r.stderr)
