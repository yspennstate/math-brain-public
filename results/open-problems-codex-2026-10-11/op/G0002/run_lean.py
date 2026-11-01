import subprocess,pathlib,os,time
root=pathlib.Path(__file__).resolve().parent
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(root/'Certificate.lean')],cwd='~/lean_verify',env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=3600,text=True,encoding='utf8')
 (root/'lean_check.txt').write_text('exit_code='+str(p.returncode)+'\nseconds='+str(time.time()-t)+'\n'+p.stdout,encoding='utf8')
 print(p.returncode,p.stdout)
except subprocess.TimeoutExpired as e:
 (root/'lean_check.txt').write_text('TIMEOUT after 3600 seconds; not checked\n'+str(e.stdout),encoding='utf8');print('TIMEOUT')
