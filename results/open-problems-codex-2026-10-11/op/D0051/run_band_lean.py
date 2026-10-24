import subprocess,pathlib,time
R=pathlib.Path(__file__).resolve().parent
start=time.time()
p=subprocess.run(['lake','env','lean',str(R/'BandReduction.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
out=f'exit_code={p.returncode}\nelapsed={time.time()-start:.2f}s\n'+p.stdout+p.stderr
(R/'band_lean_check.txt').write_text(out,encoding='utf8');print(out)
