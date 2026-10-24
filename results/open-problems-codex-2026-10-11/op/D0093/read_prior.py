import subprocess,json,pathlib
ps=json.loads(pathlib.Path('repo_paths.json').read_text())
for p in ps:
 if p.endswith('.md'):
  r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+p],capture_output=True,text=True,encoding='utf8');pathlib.Path('prior_'+pathlib.PurePosixPath(p).name).write_text(r.stdout,encoding='utf8'); print('\nFILE',p,'\n',r.stdout[:22000])
