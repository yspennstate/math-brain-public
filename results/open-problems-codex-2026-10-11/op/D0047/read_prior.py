import pathlib,subprocess
p=pathlib.Path('.')
paths=p.joinpath('prior_paths.txt').read_text().splitlines()
for s in paths:
 if s.endswith('report.md'):
  r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+s],capture_output=True,text=True,encoding='utf8',errors='replace'); print('\nFILE '+s+'\n'+r.stdout[:13000]);p.joinpath('prior_'+pathlib.PurePosixPath(s).name.replace('__report','_'+s.split('/')[-1][:19])).write_text(r.stdout,encoding='utf8')
