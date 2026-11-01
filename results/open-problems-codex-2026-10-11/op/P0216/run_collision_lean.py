import subprocess,pathlib,json,hashlib,time
R=pathlib.Path(__file__).resolve().parent
cmd=['lake','env','lean',str(R/'CollisionTruth.lean')]
start=time.monotonic()
try:
 p=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 result={'command':cmd,'timeout_seconds':3600,'exit_code':p.returncode,'output':p.stdout+p.stderr,'wall_seconds':time.monotonic()-start,'sha256':hashlib.sha256((R/'CollisionTruth.lean').read_bytes()).hexdigest()}
except subprocess.TimeoutExpired:
 result={'command':cmd,'timeout_seconds':3600,'status':'timeout','wall_seconds':time.monotonic()-start}
(R/'collision_lean_check.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
