import subprocess,pathlib
cmd=['lake','env','lean','~/brain_workers/TRIO_1011/op/E0066/RadialRigidity.lean']
try:
 r=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 pathlib.Path('radial_lean_check.log').write_text(r.stdout+r.stderr+f'\nEXIT_CODE: {r.returncode}\n',encoding='utf8'); print(r.stdout,r.stderr,'EXIT_CODE',r.returncode)
except subprocess.TimeoutExpired as e:
 pathlib.Path('radial_lean_check.log').write_text('TIMEOUT at 3600 seconds; not checked\n',encoding='utf8'); print('TIMEOUT')
