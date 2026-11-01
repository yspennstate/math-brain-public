import pathlib,subprocess,json
p=pathlib.Path('prior_paths.txt').read_text(encoding='utf8').splitlines()
for i,x in enumerate(p):
 r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+x],capture_output=True,text=True,encoding='utf8')
 pathlib.Path('prior_'+str(i)+'.md').write_text(r.stdout,encoding='utf8');print(x);print(r.stdout[:28000])
