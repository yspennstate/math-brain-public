import subprocess,pathlib,time
P=pathlib.Path(__file__).parent
start=time.time()
r=subprocess.run(['lake','env','lean',str(P/'HeightResidue.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
(P/'lean_check.log').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}; elapsed_seconds={time.time()-start}\n',encoding='utf8')
print(r.stdout+r.stderr);print('exit_code',r.returncode)
