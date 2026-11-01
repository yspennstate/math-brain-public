import subprocess,pathlib,time
R=pathlib.Path(__file__).resolve().parent
start=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(R/'SpectrumAlgebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 out=f'exit_code={p.returncode}\nelapsed={time.time()-start:.2f}s\n'+p.stdout+p.stderr
except Exception as e:out=str(e)
(R/'lean_check.txt').write_text(out,encoding='utf8');print(out)
