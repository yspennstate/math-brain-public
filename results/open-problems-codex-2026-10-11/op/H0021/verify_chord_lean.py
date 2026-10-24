import pathlib,subprocess,time
st=time.time();r=subprocess.run(['lake','env','lean',str(pathlib.Path('ChordCertificate.lean').resolve())],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
s=r.stdout+r.stderr+f'\nexit_code={r.returncode}; elapsed={time.time()-st:.2f}s\n';pathlib.Path('chord_lean_check.txt').write_text(s,encoding='utf8');print(s)
