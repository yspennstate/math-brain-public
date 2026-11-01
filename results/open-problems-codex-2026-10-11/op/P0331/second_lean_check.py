import subprocess,pathlib,time,json
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
try:
    p=subprocess.run(['lake','env','lean',str(root/'SpatialEntropy.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
    result={'command':'lake env lean '+str(root/'SpatialEntropy.lean'),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'seconds':time.monotonic()-start,'timeout_seconds':3600}
except subprocess.TimeoutExpired:
    result={'status':'timeout','seconds':time.monotonic()-start,'timeout_seconds':3600}
(root/'second_lean_result.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result),flush=True)
