import pathlib,subprocess,time
P=pathlib.Path(__file__).parent
f=P/'FusionExponents.lean';f.write_text(f.read_text(encoding='utf-8-sig'),encoding='utf8')
t=time.time();r=subprocess.run(['lake','env','lean',str(f)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
(P/'fusion_lean_check.log').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}; elapsed_seconds={time.time()-t}\n',encoding='utf8');print(r.stdout+r.stderr);print('exit_code',r.returncode)
