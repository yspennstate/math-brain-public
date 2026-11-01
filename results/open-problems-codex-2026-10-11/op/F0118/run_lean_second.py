import pathlib,subprocess,time
root=pathlib.Path(__file__).resolve().parent;start=time.monotonic()
p=subprocess.run(['lake','env','lean',str(root/'BlackwellAlgebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600,shell=True)
out=f'exit_code: {p.returncode}\nseconds: {time.monotonic()-start:.3f}\n'+p.stdout+p.stderr
(root/'lean_second_check.log').write_text(out,encoding='utf8');print(out,flush=True)
