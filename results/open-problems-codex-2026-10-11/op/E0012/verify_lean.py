import subprocess, pathlib, json, time
root=pathlib.Path(__file__).resolve().parent
rows=[]
for name in ('LocalMaps.lean','Algebra.lean'):
    start=time.monotonic()
    try:
        p=subprocess.run(['lake','env','lean',str(root/name)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
        row={'file':name,'returncode':p.returncode,'seconds':time.monotonic()-start}
        (root/(name+'.log')).write_text(p.stdout+p.stderr+'\nEXIT '+str(p.returncode),encoding='utf8')
    except subprocess.TimeoutExpired as e:
        row={'file':name,'returncode':None,'seconds':time.monotonic()-start,'error':'3600 second timeout'}
        (root/(name+'.log')).write_text(repr(e),encoding='utf8')
    rows.append(row)
    (root/'lean_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
    print(json.dumps(row),flush=True)
