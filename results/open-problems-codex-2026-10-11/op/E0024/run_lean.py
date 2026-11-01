import subprocess,pathlib,time
p=pathlib.Path('SharpComparison.lean').resolve()
t=time.time()
r=subprocess.run(['lake','env','lean',str(p)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
pathlib.Path('lean_check.txt').write_text(r.stdout+'\n'+r.stderr+f'\nexit={r.returncode}; seconds={time.time()-t:.2f}\n',encoding='utf8')
print(r.stdout,r.stderr,'exit',r.returncode)
