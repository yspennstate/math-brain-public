import subprocess,pathlib,json,time
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
try:
    p=subprocess.run(['lake','env','lean',str(root/'LocalMaps.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
    row={'file':'LocalMaps.lean','returncode':p.returncode,'seconds':time.monotonic()-start}
    (root/'LocalMaps.lean.log').write_text(p.stdout+p.stderr+'\nEXIT '+str(p.returncode),encoding='utf8')
except subprocess.TimeoutExpired as e:
    row={'file':'LocalMaps.lean','returncode':None,'seconds':time.monotonic()-start,'error':'3600 second timeout'}
    (root/'LocalMaps.lean.log').write_text(repr(e),encoding='utf8')
(root/'local_lean_check.json').write_text(json.dumps(row,indent=2),encoding='utf8')
print(json.dumps(row),flush=True)
